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
import time
import concurrent.futures
import threading


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
    ring.line.fill.solid()
    ring.line.color.rgb = color
    ring.line.width = Pt(3)
    # 内圈
    inner = _add_shape(slide, MSO_SHAPE.OVAL, left + Inches(0.15), top + Inches(0.15), Inches(0.4), Inches(0.4), color)
    inner.fill.background()
    inner.line.fill.solid()
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
        # 收集所有知识点并建立索引映射
        llm_tasks = []  # [(row_idx, sub_idx, knowledge_point), ...]
        for row_idx, dim in enumerate(dimensions):
            if len(dim) <= 1:
                llm_tasks.append((row_idx, 0, dim[0]))
            else:
                for sub_idx in range(1, len(dim)):
                    llm_tasks.append((row_idx, sub_idx, dim[sub_idx]))
        print(f"[PPT] 待生成知识点: {len(llm_tasks)}个")

        PPT_PROMPT_BATCH = """你是一位专业学习规划师。请为以下知识点分别生成详细定义。

【技能方向】{skill_name}
【职业方向】{job_name}

知识点列表：
{knowledge_list}

要求：
1. 每个讲解写详细定义，准确完整地解释该知识点，不要长篇大论
2. 不要在讲解中出现中文冒号和单引号
3. 返回JSON数组，按顺序对应上面的知识点列表：
[
  {{"knowledge_point": "知识点1", "explain": "详细定义"}},
  {{"knowledge_point": "知识点2", "explain": "详细定义"}}
]"""

        def generate_batch(knowledge_points: list[str]) -> list[dict]:
            """为一批知识点批量生成讲解（一次大模型调用）"""
            knowledge_text = "\n".join(f"{i+1}. {kp}" for i, kp in enumerate(knowledge_points))
            prompt = PPT_PROMPT_BATCH.format(
                skill_name=skill_name,
                job_name=job_name,
                knowledge_list=knowledge_text
            )
            for attempt in range(3):
                try:
                    result = llm_generator.invoke(prompt)
                    result_text = result.content if hasattr(result, 'content') else str(result)

                    cleaned_text = result_text.strip()
                    if cleaned_text.startswith("```"):
                        first_newline = cleaned_text.find('\n')
                        if first_newline != -1:
                            cleaned_text = cleaned_text[first_newline + 1:]
                        if cleaned_text.endswith("```"):
                            cleaned_text = cleaned_text[:-3]
                        cleaned_text = cleaned_text.strip()

                    start_idx = cleaned_text.find('[')
                    end_idx = cleaned_text.rfind(']')
                    if start_idx != -1 and end_idx != -1:
                        cleaned_text = cleaned_text[start_idx:end_idx + 1]

                    results = json.loads(cleaned_text)
                    if not isinstance(results, list):
                        raise ValueError("返回结果不是数组")
                    print(f"[PPT] ✓ 生成一批 {len(results)} 个知识点")
                    return results
                except Exception as e:
                    error_type = type(e).__name__
                    print(f"[PPT] 尝试{attempt+1}/3 批量生成失败: {error_type}")
                    if attempt < 2:
                        time.sleep((attempt + 1) * 2)
            print(f"[PPT] ✗ 批量生成最终失败，使用默认值")
            return [{"knowledge_point": kp, "explain": f"{kp}的核心知识点"} for kp in knowledge_points]

        # 并发分批次调用大模型（每批15个知识点，并发跑）
        ppt_data = {}
        batch_size = 8
        knowledge_points = [kp for _, _, kp in llm_tasks]

        # 将知识点分成多批
        batches = []
        for batch_start in range(0, len(knowledge_points), batch_size):
            batch_kps = knowledge_points[batch_start:batch_start + batch_size]
            batches.append((batch_start, batch_kps))

        if batches:
            rate_limiter = threading.Semaphore(3)  # 最多同时3批并发
            def run_batch(batch_start, batch_kps):
                with rate_limiter:
                    return batch_start, generate_batch(batch_kps)

            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                future_map = {executor.submit(run_batch, bs, bkp): bs for bs, bkp in batches}
                for future in concurrent.futures.as_completed(future_map):
                    batch_start = future_map[future]
                    batch_kps = knowledge_points[batch_start:batch_start + batch_size]
                    try:
                        batch_results = future.result()[1]
                        for i, result in enumerate(batch_results):
                            if i < len(batch_kps):
                                actual_idx = batch_start + i
                                row_idx, sub_idx, _ = llm_tasks[actual_idx]
                                ppt_data[(row_idx, sub_idx)] = {"explain": result.get("explain", f"{batch_kps[i]}的核心知识点")}
                    except Exception as e:
                        print(f"[PPT] 批次 {batch_start} 执行异常: {e}")
                        for i, kp in enumerate(batch_kps):
                            actual_idx = batch_start + i
                            row_idx, sub_idx, _ = llm_tasks[actual_idx]
                            ppt_data[(row_idx, sub_idx)] = {"explain": f"{kp}的核心知识点"}

        # 没有任务时填充默认值
        if not llm_tasks:
            for row_idx, dim in enumerate(dimensions):
                if len(dim) <= 1:
                    ppt_data[(row_idx, 0)] = {"explain": f"{dim[0]}的核心知识点"}

        prs = Presentation()
        slide_w = prs.slide_width
        slide_h = prs.slide_height

        # ==================== 1. 首页 ====================
        slide = prs.slides.add_slide(prs.slide_layouts[0])
        _set_slide_bg(slide, DARK_BG)

        _draw_book(slide, Inches(0.5), slide_h - Inches(1.1), ACCENT_SKY, 0.8)
        _draw_star_medal(slide, slide_w - Inches(1.5), Inches(0.3), ACCENT_AMBER)
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

        _add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                   slide_w, Inches(0.06), ACCENT_AMBER)

        _draw_book(slide, Inches(0.3), Inches(0.2), ACCENT_TEAL, 0.5)
        _draw_lightbulb(slide, slide_w - Inches(1.0), Inches(0.15), ACCENT_AMBER)

        tx_title = slide.shapes.add_textbox(Inches(1.5), Inches(0.5), Inches(7), Inches(0.8))
        tf = tx_title.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = "目  录"
        p.font.size = Pt(28)
        p.font.bold = True
        p.font.color.rgb = DARK_TEXT
        p.alignment = PP_ALIGN.CENTER

        # 提取所有维度第一个字段作为目录标题
        dim_names = [dim[0] for dim in dimensions]

        left_margin = Inches(0.6)
        top_margin = Inches(1.5)
        col_width = Inches(2.8)
        col_gap = Inches(0.3)
        item_height = Inches(0.5)
        max_per_col = 10

        for idx, name in enumerate(dim_names):
            col_idx = idx // max_per_col
            row_idx = idx % max_per_col
            left = left_margin + col_idx * (col_width + col_gap)
            top = top_margin + row_idx * item_height

            _add_shape(slide, MSO_SHAPE.OVAL, left, top + Inches(0.08), Inches(0.18), Inches(0.18), ACCENT_AMBER)
            tx_num = slide.shapes.add_textbox(left, top + Inches(0.08), Inches(0.18), Inches(0.18))
            tfn = tx_num.text_frame
            tfn.paragraphs[0].text = str(idx + 1)
            tfn.paragraphs[0].font.size = Pt(8)
            tfn.paragraphs[0].font.color.rgb = WHITE
            tfn.paragraphs[0].font.bold = True
            tfn.paragraphs[0].alignment = PP_ALIGN.CENTER

            tx_box = slide.shapes.add_textbox(left + Inches(0.28), top, col_width - Inches(0.28), item_height)
            tf = tx_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = name
            p.font.size = Pt(13)
            p.font.color.rgb = DARK_TEXT
            p.alignment = PP_ALIGN.LEFT
            tf.paragraphs[0].space_before = Pt(4)

        # ==================== 3. 中间内容页 ====================
        for row_idx, dim in enumerate(dimensions):
            summary_title = dim[0]

            if len(dim) <= 1:
                # 只有标题，直接生成一页内容
                bg_color, accent = PAGE_THEMES[row_idx % len(PAGE_THEMES)]
                layout_style = LAYOUTS[row_idx % len(LAYOUTS)]
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                _set_slide_bg(slide, bg_color)

                _add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                           slide_w, Inches(0.06), accent)

                right_corner = [
                    (_draw_star_medal, slide_w - Inches(1.2), slide_h - Inches(1.1), ACCENT_AMBER),
                    (_draw_lightbulb, slide_w - Inches(1.2), slide_h - Inches(1.1), ACCENT_AMBER),
                    (_draw_tree, slide_w - Inches(1.3), slide_h - Inches(1.2), ACCENT_EMERALD),
                ]
                draw_fn2, *args2 = right_corner[row_idx % len(right_corner)]
                draw_fn2(slide, *args2)

                item_data = ppt_data.get((row_idx, 0), {})
                explain_text = item_data.get("explain", "")

                tx_title = slide.shapes.add_textbox(Inches(1), Inches(0.6), Inches(8), Inches(0.8))
                tf = tx_title.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = summary_title
                p.font.size = Pt(22)
                p.font.bold = True
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.CENTER

                tx_explain = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(4.0))
                tfe = tx_explain.text_frame
                tfe.word_wrap = True
                p = tfe.paragraphs[0]
                p.text = explain_text
                p.font.size = Pt(12)
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.LEFT
                p.line_spacing = Pt(18)

            else:
                # ===== 有子知识点 =====
                # 先添加一页总结页：标题是 dim[0]，下面列出 dim[1:] 作为要点
                bg_color, accent = PAGE_THEMES[row_idx % len(PAGE_THEMES)]
                slide = prs.slides.add_slide(prs.slide_layouts[6])
                _set_slide_bg(slide, bg_color)

                _add_shape(slide, MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                           slide_w, Inches(0.06), accent)

                _draw_book(slide, Inches(0.3), Inches(0.2), ACCENT_TEAL, 0.5)

                # 标题
                tx_title = slide.shapes.add_textbox(Inches(1), Inches(0.6), Inches(8), Inches(0.8))
                tf = tx_title.text_frame
                tf.word_wrap = True
                p = tf.paragraphs[0]
                p.text = summary_title
                p.font.size = Pt(26)
                p.font.bold = True
                p.font.color.rgb = DARK_TEXT
                p.alignment = PP_ALIGN.CENTER

                # 子知识点列表
                bullet_top = Inches(1.6)
                for sub_idx, sub_point in enumerate(dim[1:]):
                    tx_bullet = slide.shapes.add_textbox(Inches(1.2), bullet_top + Inches(sub_idx * 0.55), Inches(7.5), Inches(0.5))
                    tf = tx_bullet.text_frame
                    tf.word_wrap = True
                    p = tf.paragraphs[0]
                    p.text = f"● {sub_point}"
                    p.font.size = Pt(14)
                    p.font.color.rgb = DARK_TEXT
                    p.alignment = PP_ALIGN.LEFT
                    p.line_spacing = Pt(22)

                # 再为每个子知识点添加一页内容页
                for sub_idx in range(1, len(dim)):
                    sub_point = dim[sub_idx]
                    item_data = ppt_data.get((row_idx, sub_idx), {})
                    explain_text = item_data.get("explain", "")

                    bg_color2, accent2 = PAGE_THEMES[(row_idx + sub_idx) % len(PAGE_THEMES)]
                    layout_style = LAYOUTS[(row_idx + sub_idx) % len(LAYOUTS)]
                    slide2 = prs.slides.add_slide(prs.slide_layouts[6])
                    _set_slide_bg(slide2, bg_color2)

                    _add_shape(slide2, MSO_SHAPE.RECTANGLE, Inches(0), Inches(0),
                               slide_w, Inches(0.06), accent2)

                    right_corner = [
                        (_draw_star_medal, slide_w - Inches(1.2), slide_h - Inches(1.1), ACCENT_AMBER),
                        (_draw_lightbulb, slide_w - Inches(1.2), slide_h - Inches(1.1), ACCENT_AMBER),
                        (_draw_tree, slide_w - Inches(1.3), slide_h - Inches(1.2), ACCENT_EMERALD),
                    ]
                    draw_fn2, *args2 = right_corner[(row_idx + sub_idx) % len(right_corner)]
                    draw_fn2(slide2, *args2)

                    tx_title2 = slide2.shapes.add_textbox(Inches(1), Inches(0.6), Inches(8), Inches(0.8))
                    tf2 = tx_title2.text_frame
                    tf2.word_wrap = True
                    p2 = tf2.paragraphs[0]
                    p2.text = sub_point
                    p2.font.size = Pt(22)
                    p2.font.bold = True
                    p2.font.color.rgb = DARK_TEXT
                    p2.alignment = PP_ALIGN.CENTER

                    tx_explain2 = slide2.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(4.0))
                    tfe2 = tx_explain2.text_frame
                    tfe2.word_wrap = True
                    p2 = tfe2.paragraphs[0]
                    p2.text = explain_text
                    p2.font.size = Pt(12)
                    p2.font.color.rgb = DARK_TEXT
                    p2.alignment = PP_ALIGN.LEFT
                    p2.line_spacing = Pt(18)
                
                

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