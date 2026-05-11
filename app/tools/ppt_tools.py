"""PPT生成工具"""
from langchain_core.tools import StructuredTool


def create_ppt_tool(llm_generator, target_jobs: str, selected_skill: str) -> StructuredTool:
    """创建PPT生成工具"""

    def generate_ppt(data: str):
        """生成PPT内容，直接返回JSON格式。"""
        # TODO: 实现PPT生成逻辑
        return "OK"

    return StructuredTool.from_function(
        func=generate_ppt,
        name="generate_ppt",
        description="当用户的意图是：帮助我生成学习规划、ppt时调用此工具",
        parameters={
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "PPT主题/知识点"
                },
                "slides_count": {
                    "type": "integer",
                    "description": "幻灯片数量，默认5页",
                    "default": 5
                }
            },
            "required": ["topic"]
        },
        return_direct=True
    )