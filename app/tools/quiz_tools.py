"""题目生成工具集"""
import json
from langchain_core.tools import StructuredTool


def create_quiz_tool(llm_generator, target_jobs: str, selected_skill: str) -> StructuredTool:
    """
    创建题目生成工具

    Args:
        llm_generator: 生成题目的LLM实例
        target_jobs: 目标岗位
        selected_skill: 选中的技能

    Returns:
        StructuredTool: 题目生成工具
    """
    def generate_quiz(data: str):
        """生成一道题目，直接返回JSON格式。"""
        parsed = json.loads(data)
        topic = parsed.get("topic")
        difficulty = parsed.get("difficulty")
        question_type = parsed.get("question_type")

        type_instructions = {
            "choice": "生成一道选择题，包含4个选项，里面只有一个正确答案，指明正确答案，并给出解析",
            "filling": "生成一道填空题，留出一个空白(在重点关键词)，并给出答案",
            "true_false": "生成一道判断题，陈述正确或错误，并解释原因",
            "analysis": "生成一道分析题，要求分析输出结果，并附带解析"
        }
        instruction = type_instructions.get(question_type)
        question_prompt = f"""你是一个题目生成机器人，只能输出JSON格式，禁止输出任何其他内容。
角色：你是{target_jobs}的{selected_skill}教学专家
任务：请根据你的身份{instruction}
参数：
    1.知识点：{topic}
    2.难度：{difficulty}
    3.题型：{question_type}
输出要求：
    1.只输出JSON，不要任何前缀文字，解释说明
    2.JSON格式：{{
        "type": "{question_type}",
        "stem": "题目题干",
        "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
        "answer": "正确答案",(如果是填空题和分析题，只需要答案字符串，不要前面的字母)
        "explanation": "详细解析",
        "code_snippet": "如果有代码，放在这里，否则为空字符串",
        "tool": "generate_quiz(不要修改这个字段，只保留括号外面的部分)"
    }}"""
        result = llm_generator.invoke(question_prompt)

        return result.content

    return StructuredTool.from_function(
        func=generate_quiz,
        name="generate_quiz",
        description="当用户的意图是：帮助我生成学习题目时调用此工具",
        parameters={
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "具体知识点，不指定默认为<基础知识点>"
                },
                "difficulty": {
                    "type": "string",
                    "enum": ["简单", "中等", "困难"],
                    "default": "简单"
                },
                "question_type": {
                    "type": "string",
                    "enum": ["choice", "filling", "true_false", "analysis"],
                    "description": "题型：choice=选择,filling=填空,true_false=判断,analysis=分析",
                    "default": "choice"
                }
            },
            "required": ["topic"]
        },
        return_direct=True
    )