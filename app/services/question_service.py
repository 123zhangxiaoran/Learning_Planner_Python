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
        self.questions_collection_name = "generated_questions"

    def generate_questions(self, dimensions: List[List[str]], user_id: int = 1, batch_id: str = None) -> Dict[str, Any]:
        """
        根据知识点维度生成题目

        Args:
            dimensions: 知识点维度列表，如 [["HTML5新标签", "HTML标签与属性"], ...]
                       每行的多个字段会合并成一个知识点文本
            user_id: 用户ID
            batch_id: 题集批次号，默认使用时间戳

        Returns:
            生成的题目列表和统计信息
        """
        all_questions = []
        for i, dim_group in enumerate(dimensions):
            # 把一行的多个字段组成知识点文本：知识点1(HTML5新标签，HTML标签与属性)。知识点2(SEO优化，iframe内联框架)...
            topic = f"知识点{i+1}({("，".join(dim_group))})" if dim_group else ""

            if topic:
                # 查询同知识点已有题目
                existing_questions = []
                if self.vector_service:
                    collection_name = f"generated_questions_user{user_id}"
                    try:
                        # 查询该用户同技能的所有题目
                        all_results = self.vector_service.get_by_metadata(
                            field="skill_name",
                            values=[self.skill_name],
                            collection_name=collection_name
                        )
                        # 筛选包含当前知识点的题目
                        for r in all_results:
                            metadata = r.get("metadata", {})
                            stored_keywords = json.loads(metadata.get("keywords", "[]"))
                            # 检查是否有知识点重叠
                            if any(kw in dim_group for kw in stored_keywords):
                                existing_questions.append(r.get("content", ""))
                    except:
                        pass

                # 构建提示词
                prompt = self._build_question_prompt(topic, i, existing_questions)

                # 调用大模型
                result = self.llm_generator.invoke(prompt)
                content = result.content if hasattr(result, 'content') else str(result)
                questions = json.loads(content)
                all_questions.append(questions)

        # 将题目存入向量库
        if self.vector_service and all_questions:
            # 生成批次号，默认使用时间戳
            if batch_id is None:
                import time
                batch_id = f"batch_{int(time.time())}"

            # 构建collection名称：generated_questions_user{user_id}
            collection_name = f"generated_questions_user{user_id}"

            # 将题目转换为可存储的文本
            texts = []
            metadatas = []
            ids = []

            for idx, q in enumerate(all_questions):
                # 提取题目信息用于向量存储
                question_data = q.get("question", {})
                text = f"题目{q.get('number', '')}：{question_data.get('stem', '')}\n选项：{', '.join(question_data.get('options', []))}\n答案：{question_data.get('answer', '')}\n解析：{question_data.get('explanation', '')}"
                texts.append(text)

                # 获取当前题目对应的知识点
                dim_group = dimensions[idx] if idx < len(dimensions) else []

                # metadata存储原始数据
                metadatas.append({
                    "user_id": user_id,
                    "batch_id": batch_id,
                    "job_name": self.job_name,
                    "skill_name": self.skill_name,
                    "keywords": json.dumps(dim_group, ensure_ascii=False),  # 存储知识点
                    "question_number": q.get("number", ""),
                    "question_type": question_data.get("type", ""),
                    "answer": question_data.get("answer", ""),
                    "original_json": json.dumps(q, ensure_ascii=False)
                })
                ids.append(f"q_{user_id}_{batch_id}_{q.get('number', '')}")

            # 添加到向量库
            self.vector_service.add_documents(
                texts=texts,
                metadatas=metadatas,
                ids=ids,
                collection_name=collection_name
            )

        return all_questions

    def _build_question_prompt(self, topic: str, i: int, existing_questions: List[str] = None) -> str:
        """
        构建题目生成提示词

        Args:
            topic: 知识点
            i: 知识点编号
            existing_questions: 已有题目列表（需避免重复）

        Returns:
            提示词字符串
        """
        excluded = ""
        if existing_questions:
            excluded = f"\n\n已有题目（请避免生成相似的）：{existing_questions}"

        return f"""你是一个题目生成机器人，只能输出JSON格式，禁止输出任何其他内容。
角色：你是{self.job_name}的{self.skill_name}教学专家
任务：生成一道题目，题里面只有一个正确答案，指明正确答案，并给出解析

出题的知识点方向:{topic}{excluded}

输出要求：
    1.只输出JSON，不要任何前缀文字，解释说明
    2.JSON格式：{{
        "number": {i+1},
        "question": {{
            "type": "choice",
            "stem": "题目题干",
            "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
            "answer": "正确答案",
            "explanation": "详细解析",
            "code_snippet": "如果有代码，放在这里，否则为空字符串"
            }}
    }}"""