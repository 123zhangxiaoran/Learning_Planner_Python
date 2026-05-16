"""PPT生成工具"""
from langchain_core.tools import StructuredTool
from pptx import Presentation
from io import BytesIO
import base64


def create_ppt_tool(llm_generator, skill_name: str, job_name: str, dimensions: list[str], user_id: int) -> StructuredTool:
    """创建PPT生成工具"""

    def generate_ppt():
        # 创建一个新的PPT文件
        prs = Presentation()
        # 设置幻灯片的布局
        slide_layout = prs.slide_layouts[1]
        # 添加一个新的幻灯片
        slide = prs.slides.add_slide(slide_layout)
        # 设置幻灯片的主题
        slide.shapes.title.text = "学习规划"
        # 保存PPT文件到内存流中
        ppt_stream = BytesIO()
        prs.save(ppt_stream)
        ppt_stream.seek(0)
        ppt_base64 = base64.b64encode(ppt_stream.getvalue()).decode("utf-8")

        return ppt_base64

    return StructuredTool.from_function(
        func=generate_ppt,
        name="generate_ppt",
        description="当用户的意图是：帮助我生成学习规划、ppt时调用此工具",
        return_direct=True
    )