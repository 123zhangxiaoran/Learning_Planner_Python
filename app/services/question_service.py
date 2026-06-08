"""题目生成服务"""
import json
from typing import Dict, Any, List


class QuestionService:
    """题目生成服务"""

    def __init__(self, llm_generator, job_name: str, skill_name: str, vector_service=None):
        """
        初始化题目服务

        Args:
            llm_generator: LLM实例
            job_name: 岗位名称
            skill_name: 技能名称
            vector_service: 向量服务实例
        """
        self.llm_generator = llm_generator
        self.job_name = job_name
        self.skill_name = skill_name
        self.vector_service = vector_service
        self.questions_master_collection = "generated_questions_master"  # 主库：所有用户题目
        self.questions_user_prefix = "generated_questions_user"  # 子库前缀：每个用户单独库

    def generate_questions(self, dimensions: List[List[str]], user_id: int = 1, batch_id: str = None) -> Dict[str, Any]:
        """
        根据知识点维度生成题目
        """
        # 将二维数组展平为一维数组，确保至少10个元素
        import random

        all_keywords = []
        dim_count = len(dimensions)

        if dim_count >= 10:
            for dim_group in dimensions:
                if dim_group:
                    all_keywords.append(random.choice(dim_group))
        else:
            pool = [kw for dim_group in dimensions for kw in dim_group]
            all_keywords = [random.choice(dg) for dg in dimensions if dg]
            remaining = [kw for kw in pool if kw not in all_keywords]
            need = 10 - len(all_keywords)
            if need > 0 and remaining:
                extra = random.sample(remaining, min(need, len(remaining)))
                all_keywords.extend(extra)

        while len(all_keywords) < 10:
            candidates = [kw for kw in all_keywords if kw != all_keywords[-1]]
            all_keywords.append(random.choice(candidates))

        all_questions = []         # 最终返回的题目列表
        new_questions = []         # LLM新生成的题（需写入主库+子库）
        sub_only_questions = []    # 从主库复用的题（只需写入子库）

        # 按 7:3 随机生成题型序列（选择题:判断题）
        import random as rnd
        type_list = ["choice"] * 7 + ["judge"] * 3
        question_types = []
        for i in range(len(all_keywords)):
            rnd.shuffle(type_list)
            question_types.append(type_list[0])

        for i, keyword in enumerate(all_keywords):
            q_type = question_types[i]
            # 找到keyword对应的维度组，获取该行的第一个字段作为输出keyword
            dim_first = ""
            for dim_group in dimensions:
                if keyword in dim_group:
                    dim_first = dim_group[0] if dim_group else keyword
                    break
            topic = f"知识点{i+1}({keyword})"
            question_obj = None

            if self.vector_service:
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
                            # 主库有 → 复用，只写子库
                            question_obj = json.loads(master_results[0].get("metadata", {}).get("original_json", "{}"))
                            if question_obj:
                                sub_only_questions.append((keyword, question_obj))
                        else:
                            # 主库也没有 → 大模型出题，写主库+子库
                            prompt = self._build_question_prompt(topic, [], q_type, keyword, dim_first)
                            result = self.llm_generator.invoke(prompt)
                            content = result.content if hasattr(result, 'content') else str(result)
                            question_obj = json.loads(content)
                            new_questions.append((keyword, question_obj))
                    else:
                        # ---- 子库有数据 ----
                        # 当前 keyword 在子库中可能有多道题，收集所有 stem
                        all_existing_stems = []
                        for r in sub_results:
                            meta = r.get("metadata", {})
                            s = meta.get("stem", "")
                            if s:
                                all_existing_stems.append(s)

                        # 已有 stem 太多了，跳过检索，直接让大模型出题
                        stems_too_many = len(all_existing_stems) >= 10

                        if stems_too_many:
                            prompt = self._build_question_prompt(topic, all_existing_stems[:10], q_type, keyword, dim_first)
                            result = self.llm_generator.invoke(prompt)
                            content = result.content if hasattr(result, 'content') else str(result)
                            question_obj = json.loads(content)
                            new_questions.append((keyword, question_obj))
                        else:
                            # 查主库所有同岗位+同技能的向量
                            master_all = self.vector_service.get_by_metadata_multi(
                                filters={
                                    "skill_name": self.skill_name,
                                    "job_name": self.job_name
                                },
                                collection_name=self.questions_master_collection
                            )

                            dissimilar_found = None
                            for r in master_all:
                                meta = r.get("metadata", {})
                                new_stem = meta.get("stem", "")
                                if not new_stem:
                                    continue
                                # 必须与子库所有已有 stem 都低于 0.8
                                all_below = True
                                for existing_stem in all_existing_stems:
                                    sim = self.vector_service.compute_similarity(existing_stem, new_stem)
                                    if sim >= 0.8:
                                        all_below = False
                                        break
                                if all_below:
                                    dissimilar_found = json.loads(meta.get("original_json", "{}"))
                                    break

                            if dissimilar_found:
                                # 找到语义不相似的题 → 复用，只写子库
                                question_obj = dissimilar_found
                                sub_only_questions.append((keyword, question_obj))
                            else:
                                # 没有低于0.8的 → 大模型出题，写主库+子库
                                prompt = self._build_question_prompt(topic, [], q_type, keyword, dim_first)
                                result = self.llm_generator.invoke(prompt)
                                content = result.content if hasattr(result, 'content') else str(result)
                                question_obj = json.loads(content)
                                new_questions.append((keyword, question_obj))

                except Exception:
                    # 异常时降级：大模型出题
                    prompt = self._build_question_prompt(topic, [], q_type, keyword, dim_first)
                    result = self.llm_generator.invoke(prompt)
                    content = result.content if hasattr(result, 'content') else str(result)
                    question_obj = json.loads(content)
                    new_questions.append((keyword, question_obj))

            if question_obj:
                all_questions.append(question_obj)

        # 将题目存入向量库
        if self.vector_service and all_questions:
            if batch_id is None:
                import time
                batch_id = f"batch_{int(time.time())}"

            master_collection = self.questions_master_collection
            user_collection_name = f"{self.questions_user_prefix}{user_id}"

            def _build_docs(items):
                texts, metadatas, ids = [], [], []
                for idx, (keyword, q) in enumerate(items):
                    text = f"{q.get('stem', '')}\n选项：{', '.join(q.get('options', []))}\n答案：{q.get('answer', '')}\n解析：{q.get('explanation', '')}"
                    texts.append(text)
                    question_type = q.get('type', '')
                    metadata = {
                        "user_id": user_id,
                        "job_name": self.job_name,
                        "skill_name": self.skill_name,
                        "keywords": json.dumps([keyword], ensure_ascii=False),
                        "stem": q.get('stem', ''),
                        "question_type": question_type,
                        "rating": 0,
                        "original_json": json.dumps(q, ensure_ascii=False)
                    }
                    metadatas.append(metadata)
                    ids.append(f"q_{user_id}_{batch_id}_{keyword}")
                return texts, metadatas, ids

            def _build_master_docs(items):
                """主库文档，不含 user_id"""
                texts, metadatas, ids = [], [], []
                for idx, (keyword, q) in enumerate(items):
                    text = f"{q.get('stem', '')}\n选项：{', '.join(q.get('options', []))}\n答案：{q.get('answer', '')}\n解析：{q.get('explanation', '')}"
                    texts.append(text)
                    question_type = q.get('type', '')
                    metadata = {
                        "job_name": self.job_name,
                        "skill_name": self.skill_name,
                        "keywords": json.dumps([keyword], ensure_ascii=False),
                        "stem": q.get('stem', ''),
                        "question_type": question_type,
                        "rating": 0,
                        "original_json": json.dumps(q, ensure_ascii=False)
                    }
                    metadatas.append(metadata)
                    ids.append(f"q_{batch_id}_{keyword}")
                return texts, metadatas, ids

            # 新生成的题 → 写子库 + 主库
            if new_questions:
                texts, metadatas, ids = _build_docs(new_questions)
                self.vector_service.add_documents(texts=texts, metadatas=metadatas, ids=ids, collection_name=user_collection_name)
                master_texts, master_metadatas, master_ids = _build_master_docs(new_questions)
                self.vector_service.add_documents(texts=master_texts, metadatas=master_metadatas, ids=master_ids, collection_name=master_collection)

            # 从主库复用的题 → 只写子库
            if sub_only_questions:
                texts, metadatas, ids = _build_docs(sub_only_questions)
                self.vector_service.add_documents(texts=texts, metadatas=metadatas, ids=ids, collection_name=user_collection_name)

        return all_questions

    def _build_question_prompt(self, topic: str, existing_questions: List[str] = None, q_type: str = "choice", output_keyword: str = "", dimension_summary: str = "") -> str:
        """
        构建题目生成提示词
        """
        excluded = ""
        if existing_questions:
            excluded = f"\n\n已有题目（请避免生成相似的）：{existing_questions}"

        if q_type == "judge":
            format_json = f'''{{
        "type": "judge",
        "stem": "题目题干（判断句）",
        "answer": "正确",
        "explanation": "详细解析",
        "dimension": "{dimension_summary}",
        "keyword": "{output_keyword}",
        "difficulty": 10
    }}'''
        else:
            format_json = f'''{{
        "type": "choice",
        "stem": "题目题干",
        "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
        "answer": "B",
        "explanation": "详细解析",
        "dimension": "{dimension_summary}",
        "keyword": "{output_keyword}",
        "difficulty": 10
    }}'''

        return f"""你是一个题目生成机器人，只能输出JSON格式，禁止输出任何其他内容。
角色：你是{self.job_name}的{self.skill_name}教学专家
任务：生成一道{q_type}题目，指定难度为10左右，题里面只有一个正确答案，指明正确答案，并给出解析

出题的知识点方向:{topic}{excluded}

输出要求：
    1.只输出JSON，不要任何前缀文字，解释说明
    2.difficulty字段必须是1-100之间的整数，1最简单，100最难
    3.answer字段只填写答案标识，选择题填选项字母（如"A"/"B"/"C"/"D"），判断题填"正确"或"错误"
    4.JSON格式：{format_json}"""
    