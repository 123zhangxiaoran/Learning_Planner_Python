"""题目生成服务"""
import json
import logging
from typing import Dict, List, Optional

from app.agents.question_agent import QuestionAgent

logger = logging.getLogger(__name__)


class QuestionService:
    """题目生成服务"""

    def __init__(self, llm_generator, job_name: str, skill_name: str, vector_service=None, precomputed_embeddings: dict = None):
        """
        初始化题目服务

        Args:
            llm_generator: LLM实例
            job_name: 岗位名称
            skill_name: 技能名称
            vector_service: 向量服务实例
            precomputed_embeddings: 预计算的嵌入向量字典 {text: embedding}
        """
        self.llm_generator = llm_generator
        self.job_name = job_name
        self.skill_name = skill_name
        self.vector_service = vector_service
        self.questions_master_collection = "generated_questions_master"  # 主库：所有用户题目
        self.questions_user_prefix = "generated_questions_user"  # 子库前缀：每个用户单独库
        self.precomputed_embeddings = precomputed_embeddings or {}  # 预计算嵌入向量

    def generate_questions(self, keywords: List[str], questions: List[Dict], user_id: int = 1, batch_id: str = None) -> List[Dict]:
        """
        批量存储生成的题目到向量库

        Args:
            keywords: 知识点关键词列表
            questions: 题目对象列表
            user_id: 用户ID
            batch_id: 批次ID

        Returns:
            题目列表
        """
        if not questions or not self.vector_service:
            return questions

        if batch_id is None:
            import time
            batch_id = f"batch_{int(time.time())}"

        master_collection = self.questions_master_collection
        user_collection_name = f"{self.questions_user_prefix}{user_id}"

        # 按 keyword:question 配对
        paired = list(zip(keywords, questions))
        texts, metadatas, ids = [], [], []

        for idx, (keyword, q) in enumerate(paired):
            text = f"{q.get('stem', '')}\n选项：{', '.join(q.get('options', []))}\n答案：{q.get('answer', '')}\n解析：{q.get('explanation', '')}"
            texts.append(text)
            question_type = q.get('type', '')
            # 使用预计算的嵌入向量
            stem_text = q.get('stem', '')
            stem_vector = self.precomputed_embeddings.get(stem_text)
            if stem_vector is None:
                stem_vector = json.dumps(self.vector_service.compute_embedding(stem_text), ensure_ascii=False)
            else:
                stem_vector = json.dumps(stem_vector, ensure_ascii=False)
            metadata = {
                "user_id": user_id,
                "job_name": self.job_name,
                "skill_name": self.skill_name,
                "keywords": json.dumps([keyword], ensure_ascii=False),
                "stem": q.get('stem', ''),
                "stem_vector": stem_vector,
                "question_type": question_type,
                "rating": 0,
                "original_json": json.dumps(q, ensure_ascii=False)
            }
            metadatas.append(metadata)
            ids.append(f"q_{user_id}_{batch_id}_{keyword}_{idx}")

        self.vector_service.add_documents(texts=texts, metadatas=metadatas, ids=ids, collection_name=user_collection_name)

        # 主库不含 user_id
        master_texts, master_metadatas, master_ids = [], [], []
        for idx, (keyword, q) in enumerate(paired):
            text = f"{q.get('stem', '')}\n选项：{', '.join(q.get('options', []))}\n答案：{q.get('answer', '')}\n解析：{q.get('explanation', '')}"
            master_texts.append(text)
            question_type = q.get('type', '')
            # 主库也使用预计算的嵌入向量
            stem_text = q.get('stem', '')
            stem_vector = self.precomputed_embeddings.get(stem_text)
            if stem_vector is None:
                stem_vector = json.dumps(self.vector_service.compute_embedding(stem_text), ensure_ascii=False)
            else:
                stem_vector = json.dumps(stem_vector, ensure_ascii=False)
            metadata = {
                "job_name": self.job_name,
                "skill_name": self.skill_name,
                "keywords": json.dumps([keyword], ensure_ascii=False),
                "stem": q.get('stem', ''),
                "stem_vector": stem_vector,
                "question_type": question_type,
                "rating": 0,
                "original_json": json.dumps(q, ensure_ascii=False)
            }
            master_metadatas.append(metadata)
            master_ids.append(f"q_{batch_id}_{keyword}_{idx}")

        self.vector_service.add_documents(texts=master_texts, metadatas=master_metadatas, ids=master_ids, collection_name=master_collection)

        return questions

    def generate_single_question(self, keyword: str, dim_first: str, q_type: str,
                                  user_id: int = 1,
                                  difficulty: int = None,
                                  save_logs: bool = False) -> Optional[Dict]:
        """
        根据单个知识点生成一道题目（使用多智能体框架）

        Args:
            keyword: 知识点关键词
            dim_first: 维度组的第一个字段
            q_type: 题目类型 ("choice" 或 "judge")
            user_id: 用户ID
            save_logs: 是否直接打印思考过程

        Returns:
            题目对象，生成失败返回 None
        """
        # 每次调用创建新的智能体实例，避免多线程共享状态
        from app.agents.question_agent import QuestionAgent
        agent = QuestionAgent(self.llm_generator, self.job_name, self.skill_name)

        if not self.vector_service:
            return agent.generate(
                keyword=keyword,
                dim_first=dim_first,
                existing_questions=None,
                q_type=q_type,
                difficulty=difficulty,
                save_logs=save_logs
            )

        user_collection_name = f"{self.questions_user_prefix}{user_id}"
        try:
            # 精确查子库：该用户是否有该知识点的题目
            sub_results = self.vector_service.get_by_metadata_multi(
                filters={
                    "skill_name": self.skill_name,
                    "job_name": self.job_name,
                    "keywords": json.dumps([keyword], ensure_ascii=False),
                    "question_type": q_type
                },
                collection_name=user_collection_name
            )

            if not sub_results:
                # ---- 子库没有数据 ----
                # 去主库精准匹配
                master_results = self.vector_service.get_by_metadata_multi(
                    filters={
                        "skill_name": self.skill_name,
                        "job_name": self.job_name,
                        "keywords": json.dumps([keyword], ensure_ascii=False),
                        "question_type": q_type
                    },
                    collection_name=self.questions_master_collection
                )
                if master_results:
                    # 主库有 → 复用
                    return json.loads(master_results[0].get("metadata", {}).get("original_json", "{}"))
                else:
                    # 主库也没有 → 智能体出题
                    return agent.generate(
                        keyword=keyword,
                        dim_first=dim_first,
                        existing_questions=None,
                        q_type=q_type,
                        difficulty=difficulty,
                        save_logs=save_logs
                    )
            else:
                # ---- 子库有数据 ----
                all_existing_vectors = []
                for r in sub_results:
                    meta = r.get("metadata", {})
                    vec = meta.get("stem_vector", "")
                    if vec:
                        all_existing_vectors.append(vec)

                stems_too_many = len(all_existing_vectors) >= 10

                if stems_too_many:
                    # 子库已有太多题 → 智能体出题（传入已有题目避免重复）
                    all_existing_stems = []
                    for r in sub_results:
                        s = r.get("metadata", {}).get("stem", "")
                        if s:
                            all_existing_stems.append(s)
                    return agent.generate(
                        keyword=keyword,
                        dim_first=dim_first,
                        existing_questions=all_existing_stems[:10],
                        q_type=q_type,
                        difficulty=difficulty,
                        save_logs=save_logs
                    )
                else:
                    # 查主库找语义不相似的题（直接用预存向量计算余弦，不调 ollama）
                    master_all = self.vector_service.get_by_metadata_multi(
                        filters={
                            "skill_name": self.skill_name,
                            "job_name": self.job_name,
                            "keywords": json.dumps([keyword], ensure_ascii=False),
                            "question_type": q_type
                        },
                        collection_name=self.questions_master_collection
                    )

                    import json as _json
                    import numpy as np
                    # 子库向量转为矩阵（只算一次）
                    sub_vecs = np.array([_json.loads(v) for v in all_existing_vectors])
                    sub_norms = np.linalg.norm(sub_vecs, axis=1, keepdims=True)

                    for r in master_all:
                        meta = r.get("metadata", {})
                        new_vec_str = meta.get("stem_vector", "")
                        if not new_vec_str:
                            continue
                        new_vec = np.array(_json.loads(new_vec_str))
                        # 一次矩阵运算算出与所有子库的余弦相似度
                        sims = np.dot(sub_vecs, new_vec) / (sub_norms.flatten() * np.linalg.norm(new_vec) + 1e-10)
                        if np.all(sims < 0.8):
                            return _json.loads(meta.get("original_json", "{}"))

                    # 没有低于0.8的 → 智能体出题
                    return agent.generate(
                        keyword=keyword,
                        dim_first=dim_first,
                        existing_questions=None,
                        q_type=q_type,
                        difficulty=difficulty,
                        save_logs=save_logs
                    )

        except Exception:
            # 异常时降级：智能体出题
            return agent.generate(
                keyword=keyword,
                dim_first=dim_first,
                existing_questions=None,
                q_type=q_type,
                difficulty=difficulty,
                save_logs=save_logs
            )