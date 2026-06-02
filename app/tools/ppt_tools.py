"""PPT生成工具"""
from langchain_core.tools import StructuredTool
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from io import BytesIO
import base64
import json
import random


# ==================== 柔和学习色系 ====================
# 背景色 — 全部使用淡浅色
BG_SKY = RGBColor(0xE3, 0xF2, 0xFD)         # 天蓝
BG_MINT = RGBColor(0xE0, 0xF2, 0xE9)        # 薄荷
BG_CREAM = RGBColor(0xFF, 0xF8, 0xE1)       # 奶油
BG_LAVENDER = RGBColor(0xF0, 0xE6, 0xFF)    # 薰衣草
BG_PEACH = RGBColor(0xFE, 0xED, 0xE6)       # 蜜桃
BG_ICE = RGBColor(0xE8, 0xF6, 0xFA)         # 冰蓝
BG_BLUSH = RGBColor(0xFC, 0xE4, 0xEC)       # 粉颊

# 装饰/强调色
ACCENT_TEAL = RGBColor(0x38, 0xB2, 0xAC)     # 青绿
ACCENT_SKY = RGBColor(0x4A, 0x90, 0xD9)      # 天蓝
ACCENT_EMERALD = RGBColor(0x5C, 0xB8, 0x7C)  # 翠绿
ACCENT_AMBER = RGBColor(0xE8, 0xB3, 0x3C)    # 琥珀
ACCENT_PLUM = RGBColor(0x9B, 0x72, 0xCB)     # 梅紫
ACCENT_ROSE = RGBColor(0xE8, 0x6C, 0x8A)     # 玫瑰
ACCENT_STEEL = RGBColor(0x5A, 0x7D, 0xA0)    # 钢蓝

DARK_TEXT = RGBColor(0x2C, 0x3E, 0x50)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
DARK_BG = RGBColor(0x3A, 0x5A, 0x80)


def _set_slide_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def _add_shape(slide, mso_shape, left, top, width, height, color, rotation=None):
    shape = slide.shapes.add_shape(mso_shape, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    if rotation:
        shape.rotation = rotation
    return shape


# ==================== 用形状组合"画"装饰图案 ====================
def _draw_book(slide, left, top, color, scale=1.0):
    """画一本打开的书"""
    w, h = Inches(0.7 * scale), Inches(0.9 * scale)
    # 左页
    _add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, left, top, w, h, color)
    # 右页
    _add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, left + w - Inches(0.05 * scale), top, w, h, color)
    # 书脊线
    spine = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + w - Inches(0.05 * scale), top + Inches(0.05 * scale), Inches(0.1 * scale), h - Inches(0.1 * scale))
    spine.fill.solid()
    spine.fill.fore_color.rgb = RGBColor(min(color[0]+20, 255), min(color[1]+20, 255), min(color[2]+20, 255))
    spine.line.fill.background()
    # 书签
    _add_shape(slide, MSO_SHAPE.RECTANGLE, left + w - Inches(0.02 * scale), top - Inches(0.1 * scale), Inches(0.06 * scale), Inches(0.2 * scale), ACCENT_AMBER)


def _draw_pencil(slide, left, top, color, rotation=0):
    """画一支铅笔"""
    # 笔身
    _add_shape(slide, MSO_SHAPE.RECTANGLE, left, top + Inches(0.3), Inches(0.25), Inches(0.8), color, rotation)
    # 笔尖（三角形）
    _add_shape(slide, MSO_SHAPE.ISOSCELES_TRIANGLE, left + Inches(0.02), top + Inches(1.05), Inches(0.21), Inches(0.25), ACCENT_AMBER, rotation)
    # 橡皮
    _add_shape(slide, MSO_SHAPE.RECTANGLE, left + Inches(0.02), top + Inches(0.1), Inches(0.21), Inches(0.22), ACCENT_ROSE, rotation)


def _draw_tree(slide, left, top, color):
    """画一棵知识树"""
    # 树干
    _add_shape(slide, MSO_SHAPE.RECTANGLE, left + Inches(0.25), top + Inches(0.6), Inches(0.2), Inches(0.6), RGBColor(0xA0, 0x7A, 0x5A))
    # 树冠 - 三个叠加的圆
    _add_shape(slide, MSO_SHAPE.OVAL, left, top + Inches(0.1), Inches(0.7), Inches(0.6), color)
    _add_shape(slide, MSO_SHAPE.OVAL, left + Inches(0.3), top, Inches(0.6), Inches(0.5), color)
    _add_shape(slide, MSO_SHAPE.OVAL, left - Inches(0.1), top + Inches(0.15), Inches(0.5), Inches(0.5), color)


def _draw_lightbulb(slide, left, top, color):
    """画一个灯泡"""
    # 灯泡（椭圆）
    _add_shape(slide, MSO_SHAPE.OVAL, left + Inches(0.1), top, Inches(0.5), Inches(0.6), color)
    # 底座
    _add_shape(slide, MSO_SHAPE.RECTANGLE, left + Inches(0.22), top + Inches(0.55), Inches(0.26), Inches(0.12), ACCENT_STEEL)
    # 螺丝口
    _add_shape(slide, MSO_SHAPE.RECTANGLE, left + Inches(0.2), top + Inches(0.62), Inches(0.3), Inches(0.08), ACCENT_AMBER)


def _draw_cap(slide, left, top, color):
    """画一顶毕业帽"""
    # 帽顶（菱形/方形旋转）
    _add_shape(slide, MSO_SHAPE.PARALLELOGRAM, left, top + Inches(0.2), Inches(0.9), Inches(0.3), color, 0)
    # 帽穗
    _add_shape(slide, MSO_SHAPE.RECTANGLE, left + Inches(0.75), top + Inches(0.45), Inches(0.04), Inches(0.35), ACCENT_GOLD := RGBColor(0xF4, 0xC5, 0x42))
    # 帽穗头
    _add_shape(slide, MSO_SHAPE.OVAL, left + Inches(0.72), top + Inches(0.75), Inches(0.1), Inches(0.08), ACCENT_GOLD)


def _draw_compass(slide, left, top, color):
    """画一个指南针（代表探索方向）"""
    # 外圈
    ring = _add_shape(slide, MSO_SHAPE.OVAL, left, top, Inches(0.7), Inches(0.7), color)
    ring.fill.background()
    ring.line.color.rgb = color
    ring.line.width = Pt(3)
    # 内圈
    inner = _add_shape(slide, MSO_SHAPE.OVAL, left + Inches(0.15), top + Inches(0.15), Inches(0.4), Inches(0.4), color)
    inner.fill.background()
    inner.line.color.rgb = color
    inner.line.width = Pt(1.5)
    # 指针 - 上三角（北）
    _add_shape(slide, MSO_SHAPE.ISOSCELES_TRIANGLE, left + Inches(0.25), top + Inches(0.05), Inches(0.2), Inches(0.3), ACCENT_ROSE)
    # 指针 - 下三角（南）
    _add_shape(slide, MSO_SHAPE.ISOSCELES_TRIANGLE, left + Inches(0.25), top + Inches(0.35), Inches(0.2), Inches(0.3), ACCENT_SKY, 180)


def _draw_star_medal(slide, left, top, color):
    """画一个星星奖杯"""
    # 大星星
    _add_shape(slide, MSO_SHAPE.STAR_5_POINT, left + Inches(0.15), top, Inches(0.55), Inches(0.55), color, 10)
    # 底座
    _add_shape(slide, MSO_SHAPE.TRAPEZOID, left + Inches(0.15), top + Inches(0.55), Inches(0.55), Inches(0.15), ACCENT_AMBER)
    # 小星星
    _add_shape(slide, MSO_SHAPE.STAR_5_POINT, left, top + Inches(0.1), Inches(0.2), Inches(0.2), ACCENT_AMBER, 0)


# 每页装饰组合（页眉小图）
DECORATIONS = [
    [(_draw_book, Inches(0.3), Inches(0.25), ACCENT_TEAL, 0.6)],
    [(_draw_pencil, Inches(0.4), Inches(0.2), ACCENT_SKY, 15)],
    [(_draw_tree, Inches(0.3), Inches(0.15), ACCENT_EMERALD)],
    [(_draw_lightbulb, Inches(0.35), Inches(0.2), ACCENT_AMBER)],
    [(_draw_cap, Inches(0.3), Inches(0.2), ACCENT_PLUM)],
    [(_draw_compass, Inches(0.3), Inches(0.15), ACCENT_STEEL)],
    [(_draw_star_medal, Inches(0.3), Inches(0.15), ACCENT_TEAL)],
]

# 内容页配色轮换
PAGE_THEMES = [
    (BG_SKY, ACCENT_SKY),
    (BG_MINT, ACCENT_EMERALD),
    (BG_CREAM, ACCENT_AMBER),
    (BG_LAVENDER, ACCENT_PLUM),
    (BG_PEACH, ACCENT_ROSE),
    (BG_ICE, ACCENT_STEEL),
    (BG_BLUSH, ACCENT_TEAL),
]

LAYOUTS = [1, 3, 7]


def create_ppt_tool(llm_generator, skill_name: str, job_name: str, dimensions: list[list[str]], user_id: int) -> StructuredTool:
    """创建PPT生成工具"""
    def generate_ppt():

        knowledge_points = "\n".join(
            f"知识点{i+1}. {', '.join(dim)}"
            for i, dim in enumerate(dimensions)
        )

        PPT_PROMPT_TEMPLATE = """你是一位专业学习规划师。请根据以下信息，为每个知识点生成简明的定义和简洁的代码示例。

【技能方向】{skill_name}
【职业方向】{job_name}

【知识点】
{knowledge_points}

要求：
1. 讲解只写核心定义，一句话概括，一个知识点一行，不要长篇大论
2. 代码示例要极度简洁，最多10行，只写核心代码片段，不要import、不要主函数、不要打印语句、不要其他运行代码
3. 代码中的换行符必须使用 \\n 转义字符表示，不要使用实际的换行符
4. 不要在讲解中出现中文冒号和单引号
5. 返回JSON数组格式：
[
    {{"explain": "一句话核心定义", "example": "简洁的核心代码"}},
    ...
]
"""

        prompt = PPT_PROMPT_TEMPLATE.format(skill_name=skill_name, job_name=job_name, knowledge_points=knowledge_points)
        result = llm_generator.invoke(prompt)

        # 解析JSON结果
        try:
            result_text = result.content if hasattr(result, 'content') else str(result)

            # 多步骤解析策略
            parsed_data = None

            # 步骤1: 直接尝试解析
            try:
                parsed_data = json.loads(result_text)
            except:
                pass

            # 步骤2: 清理markdown格式后尝试
            if parsed_data is None:
                cleaned_text = result_text.strip()
                # 去掉markdown代码块格式
                if cleaned_text.startswith("```"):
                    first_newline = cleaned_text.find('\n')
                    if first_newline != -1:
                        cleaned_text = cleaned_text[first_newline + 1:]
                    if cleaned_text.endswith("```"):
                        cleaned_text = cleaned_text[:-3]
                    cleaned_text = cleaned_text.strip()

                # 找到JSON数组边界
                start_idx = cleaned_text.find('[')
                end_idx = cleaned_text.rfind(']')
                if start_idx != -1 and end_idx != -1:
                    cleaned_text = cleaned_text[start_idx:end_idx + 1]

                try:
                    parsed_data = json.loads(cleaned_text)
                except:
                    pass

            # 步骤3: 使用解析结果或默认值
            if parsed_data is not None and isinstance(parsed_data, list):
                ppt_data = parsed_data
            else:
                ppt_data = None

        except Exception as e:
            ppt_data = None

        # 最终检查：如果没有有效数据，使用默认值
        if ppt_data is None or not isinstance(ppt_data, list) or len(ppt_data) == 0:
            # 使用维度名称作为默认值
            ppt_data = [{"explain": f"{dim[0]}学习的核心知识点", "example": "# 学习内容\n# 代码示例"} for dim in dimensions]
        
        prs = Presentation()
        slide_w = prs.slide_width
        slide_h = prs.slide_height

        # ==================== 1. 首页 ====================
        slide = prs.slides.add_slide(prs.slide_layouts[0])
        _set_slide_bg(slide, DARK_BG)

        # 底部书本装饰
        _draw_book(slide, Inches(0.5), slide_h - Inches(1.1), ACCENT_SKY, 0.8)
        _draw_star_medal(slide, slide_w - Inches(1.5), Inches(0.3), ACCENT_AMBER)
        # 铅笔装饰
        _draw_pencil(slide, Inches(8.5), Inches(0.4), ACCENT_ROSE, 20)

        title_shape = slide.shapes.title
        title_shape.text = f"学习规划：{job_name}"
        for p in title_shape.text_frame.paragraphs:
            p.font.size = Pt(36)
            p.font.color.rgb = WHITE

        slide.placeholders[1].text = f"{skill_name}篇"
        for p in slide.placeholders[1].text_frame.paragraphs:
            p.font.size = Pt(24)
            p.font.color.rgb = ACCENT_AMBER

        # ==================== 2. 目录页 ====================
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        _set_slide_bg(slide, BG_CREAM)

        # 顶部装饰细线
        _add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                   slide_w, Inches(0.06), ACCENT_AMBER)

        # 装饰
        _draw_book(slide, Inches(0.3), Inches(0.2), ACCENT_TEAL, 0.5)
        _draw_lightbulb(slide, slide_w - Inches(1.0), Inches(0.15), ACCENT_AMBER)

        # 标题
        tx_title = slide.shapes.add_textbox(Inches(1.5), Inches(0.5), Inches(7), Inches(0.8))
        tf = tx_title.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "目  录"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = DARK_TEXT
        p.alignment = PP_ALIGN.CENTER

        # 提取所有维度第一个字段
        dim_names = [dim[0] for dim in dimensions]

        # 列布局参数：垂直分布，一列满了自动换列
        left_margin = Inches(0.6)
        top_margin = Inches(1.5)
        col_width = Inches(2.8)
        col_gap = Inches(0.3)
        item_height = Inches(0.5)
        max_per_col = 10

        num_cols = (len(dim_names) + max_per_col - 1) // max_per_col

        for idx, name in enumerate(dim_names):
            col_idx = idx // max_per_col
            row_idx = idx % max_per_col
            left = left_margin + col_idx * (col_width + col_gap)
            top = top_margin + row_idx * item_height

            # 序号圆点
            _add_shape(slide, MSO_SHAPE.OVAL, left, top + Inches(0.08), Inches(0.18), Inches(0.18), ACCENT_AMBER)
            # 序号数字
            tx_num = slide.shapes.add_textbox(left, top + Inches(0.08), Inches(0.18), Inches(0.18))
            tfn = tx_num.text_frame
            tfn.paragraphs[0].text = str(idx + 1)
            tfn.paragraphs[0].font.size = Pt(8)
            tfn.paragraphs[0].font.color.rgb = WHITE
            tfn.paragraphs[0].font.bold = True
            tfn.paragraphs[0].alignment = PP_ALIGN.CENTER

            # 维度名称（仅取第一个字段 dim[0]）
            tx_box = slide.shapes.add_textbox(left + Inches(0.28), top, col_width - Inches(0.28), item_height)
            tf = tx_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = name
            p.font.size = Pt(13)
            p.font.color.rgb = DARK_TEXT
            p.alignment = PP_ALIGN.LEFT
            tf.paragraphs[0].space_before = Pt(4)

        # ==================== 3. 中间内容页（全部用空白布局，手动居中） ====================
        for i, dim in enumerate(dimensions):
            bg_color, accent = PAGE_THEMES[i % len(PAGE_THEMES)]
            layout_style = LAYOUTS[i % len(LAYOUTS)]
            slide = prs.slides.add_slide(prs.slide_layouts[6])  # 空白布局
            _set_slide_bg(slide, bg_color)

            # 顶部装饰细线
            _add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                       slide_w, Inches(0.06), accent)

            # 右下角装饰画
            right_corner = [
                (_draw_star_medal, slide_w - Inches(1.2), slide_h - Inches(1.1), ACCENT_AMBER),
                (_draw_lightbulb, slide_w - Inches(1.2), slide_h - Inches(1.1), ACCENT_AMBER),
                (_draw_tree, slide_w - Inches(1.3), slide_h - Inches(1.2), ACCENT_EMERALD),
            ]
            draw_fn2, *args2 = right_corner[i % len(right_corner)]
            draw_fn2(slide, *args2)

            # 获取当前知识点的内容
            item_data = ppt_data[i] if i < len(ppt_data) else {}
            explain_text = item_data.get("explain", "")
            # 把代码中的 \\n 替换为真正的换行符
            example_text = item_data.get("example", "").replace('\\n', '\n')

            if layout_style == 1:
                # 上下布局：标题顶部居中，解释在上，代码块在下，宽度80%居中
                tx_title = slide.shapes.add_textbox(Inches(1), Inches(0.6), Inches(8), Inches(0.8))
                tf = tx_title.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = dim[0]
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.CENTER

                # 解释内容
                tx_explain = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(1.5))
                tfe = tx_explain.text_frame
                tfe.word_wrap = True
                p = tfe.paragraphs[0]
                p.text = explain_text
                p.font.size = Pt(12)
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.LEFT
                p.line_spacing = Pt(18)

                # 代码背景块（黑色矩形，80%宽度居中）
                code_bg = _add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE,
                                    Inches(1), Inches(3.0), Inches(8), Inches(3.5),
                                    RGBColor(0x1E, 0x1E, 0x1E))

                # 代码文本
                tx_code = slide.shapes.add_textbox(Inches(1.2), Inches(3.1), Inches(7.6), Inches(3.3))
                tfc = tx_code.text_frame
                tfc.word_wrap = True
                p = tfc.paragraphs[0]
                p.text = example_text
                p.font.size = Pt(10)
                p.font.name = "Consolas"
                p.font.color.rgb = RGBColor(0xA9, 0xB7, 0xC6)
                p.alignment = PP_ALIGN.LEFT
                p.line_spacing = Pt(14)

            elif layout_style == 3:
                # 左右布局：统一为上下布局，宽度80%居中
                tx_title = slide.shapes.add_textbox(Inches(1), Inches(0.6), Inches(8), Inches(0.8))
                tf = tx_title.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = dim[0]
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.CENTER

                # 解释内容
                tx_explain = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(1.5))
                tfe = tx_explain.text_frame
                tfe.word_wrap = True
                p = tfe.paragraphs[0]
                p.text = explain_text
                p.font.size = Pt(12)
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.LEFT
                p.line_spacing = Pt(18)

                # 代码背景块（黑色矩形）
                code_bg = _add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE,
                                    Inches(1), Inches(3.0), Inches(8), Inches(3.5),
                                    RGBColor(0x1E, 0x1E, 0x1E))

                # 代码文本
                tx_code = slide.shapes.add_textbox(Inches(1.2), Inches(3.1), Inches(7.6), Inches(3.3))
                tfc = tx_code.text_frame
                tfc.word_wrap = True
                p = tfc.paragraphs[0]
                p.text = example_text
                p.font.size = Pt(10)
                p.font.name = "Consolas"
                p.font.color.rgb = RGBColor(0xA9, 0xB7, 0xC6)
                p.alignment = PP_ALIGN.LEFT
                p.line_spacing = Pt(14)

            else:
                # 简洁布局：标题顶部居中，解释在上，代码块在下，宽度80%居中
                tx_title = slide.shapes.add_textbox(Inches(1), Inches(0.6), Inches(8), Inches(0.8))
                tf = tx_title.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = dim[0]
                p.font.size = Pt(26)
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.CENTER
                tf.paragraphs[0].alignment = PP_ALIGN.CENTER

                # 解释内容
                tx_explain = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(1.5))
                tfe = tx_explain.text_frame
                tfe.word_wrap = True
                p = tfe.paragraphs[0]
                p.text = explain_text
                p.font.size = Pt(12)
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.LEFT
                p.line_spacing = Pt(18)

                # 代码背景块（黑色矩形）
                code_bg = _add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE,
                                    Inches(1), Inches(3.0), Inches(8), Inches(3.5),
                                    RGBColor(0x1E, 0x1E, 0x1E))

                # 代码文本
                tx_code = slide.shapes.add_textbox(Inches(1.2), Inches(3.1), Inches(7.6), Inches(3.3))
                tfc = tx_code.text_frame
                tfc.word_wrap = True
                p = tfc.paragraphs[0]
                p.text = example_text
                p.font.size = Pt(10)
                p.font.name = "Consolas"
                p.font.color.rgb = RGBColor(0xA9, 0xB7, 0xC6)
                p.alignment = PP_ALIGN.LEFT
                p.line_spacing = Pt(14)
                
                

        # ==================== 4. 结尾页 ====================
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        _set_slide_bg(slide, DARK_BG)

        # 底部装饰：打开的书+树
        _draw_book(slide, Inches(0.4), slide_h - Inches(1.2), ACCENT_TEAL, 0.7)
        _draw_tree(slide, slide_w - Inches(1.3), slide_h - Inches(1.5), ACCENT_EMERALD)
        # 左上角毕业帽
        _draw_cap(slide, Inches(0.4), Inches(0.2), ACCENT_AMBER)

        txBox = slide.shapes.add_textbox(Inches(1), Inches(2.8), Inches(8), Inches(2.5))
        tf = txBox.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = "小顾问祝你一路顺风~"
        p.font.size = Pt(32)
        p.font.color.rgb = WHITE
        p.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = "学习路上，与你同行"
        p2.font.size = Pt(16)
        p2.font.color.rgb = ACCENT_AMBER
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(12)

        # 保存
        ppt_stream = BytesIO()
        prs.save(ppt_stream)
        ppt_stream.seek(0)
        ppt_base64 = base64.b64encode(ppt_stream.getvalue()).decode("utf-8")
        return {
            "data": ppt_base64,
            "tool": "generate_ppt"
        }

    return StructuredTool.from_function(
        func=generate_ppt,
        name="generate_ppt",
        description="当用户的意图是：帮助我生成学习规划、ppt时调用此工具",
        return_direct=True
    )