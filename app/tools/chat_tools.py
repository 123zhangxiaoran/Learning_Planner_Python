"""聊天工具集"""
from langchain_core.tools import StructuredTool
import json

def create_chat_tool(llm):
    """
    创建聊天工具

    Args:
        llm: 用于聊天的LLM实例

    Returns:
        StructuredTool: 聊天工具
    """
    def chat(data: str):
        parsed = json.loads(data)
        question = parsed.get("question")
        
        prompt = f"""你是一名AI聊天小顾问，只能输出JSON格式，禁止输出任何其他内容。名字是小文，活泼可爱且善于倾听。
根据用户的输入:{question}来回答

输出要求：
    1.只输出JSON，不要任何前缀文字，解释说明
    2.对话内容里面不要生成图标icon，不要生成表情icon
    3.JSON格式：{{
        "answer": "你输出的内容",
        "tool": "chat(不要修改这个字段，只保留括号外面的部分)"
    }}"""
        
        result = llm.invoke(prompt)

        return result.content

    return StructuredTool.from_function(
        func=chat,
        name="chat",
        description="当用户的意图是：想和你聊天时调用此工具",
        parameters={
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "整个文本"
                }
            },
            "required": ["question"]
        },
        return_direct=True
    )