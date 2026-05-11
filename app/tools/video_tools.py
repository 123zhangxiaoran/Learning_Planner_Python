"""视频生成工具"""
from langchain_core.tools import StructuredTool


def create_video_tool(llm_generator, target_jobs: str, selected_skill: str) -> StructuredTool:
    """创建视频生成工具"""

    def generate_video(data: str):
        """生成视频脚本，直接返回JSON格式。"""
        # TODO: 实现视频生成逻辑
        pass

    return StructuredTool.from_function(
        func=generate_video,
        name="generate_video",
        description="当用户的意图是：帮助我生成视频时调用此工具",
        parameters={
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "视频主题/知识点"
                },
                "duration": {
                    "type": "integer",
                    "description": "视频时长（分钟），默认3分钟",
                    "default": 3
                }
            },
            "required": ["topic"]
        },
        return_direct=True
    )