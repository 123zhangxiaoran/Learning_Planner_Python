"""题目生成服务"""
import json
from typing import Dict, Any, List


class QuestionService:
    """题目生成服务"""

    def __init__(self, llm_generator, job_name: str, skill_name: str):
        """
        初始化题目服务

        Args:
            llm_generator: LLM实例
            job_name: 岗位名称
            skill_name: 技能名称
        """
        self.llm_generator = llm_generator
        self.job_name = job_name
        self.skill_name = skill_name

    def generate_questions(self, dimensions: List[List[str]], user_id: int = 1) -> Dict[str, Any]:
        """
        根据知识点维度生成题目

        Args:
            dimensions: 知识点维度列表，如 [["HTML5新标签", "HTML标签与属性"], ...]
                       每行的多个字段会合并成一个知识点文本
            user_id: 用户ID

        Returns:
            生成的题目列表和统计信息
        """
        all_questions = []
        print(f"接收到的知识点维度：{dimensions}")

        for i, dim_group in enumerate(dimensions):
            # 把一行的多个字段组成知识点文本：知识点1(HTML5新标签，HTML标签与属性)。知识点2(SEO优化，iframe内联框架)...
            topic = f"知识点{i+1}({("，".join(dim_group))})" if dim_group else ""

            if topic:
                # 构建提示词
                prompt = self._build_question_prompt(topic)
                print(f"生成题目的提示词：{prompt}")

                # 直接调用大模型
                #result = self.llm_generator.invoke(prompt)
                #content = result.content if hasattr(result, 'content') else str(result)
                #questions = json.loads(content)

        return "questions"

    def _build_question_prompt(self, topic: str) -> str:
        """
        构建题目生成提示词

        Args:
            topic: 知识点

        Returns:
            提示词字符串
        """
        return f"""你是一个题目生成机器人，只能输出JSON格式，禁止输出任何其他内容。
角色：你是{self.job_name}的{self.skill_name}教学专家
任务：生成2道题目，每道题里面只有一个正确答案，指明正确答案，并给出解析

出题的知识点方向:{topic}

输出要求：
    1.只输出JSON，不要任何前缀文字，解释说明
    2.JSON格式：{{
        "number": "1",
        "question": {{
            "type": "choice",
            "stem": "题目题干",
            "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
            "answer": "正确答案",
            "explanation": "详细解析",
            "code_snippet": "如果有代码，放在这里，否则为空字符串"
        }},
        "number": "2",
        "question": {{
            "type": "choice",
            "stem": "题目题干",
            "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
            "answer": "正确答案",
            "explanation": "详细解析",
            "code_snippet": "如果有代码，放在这里，否则为空字符串"
        }},
        ...
    }}"""