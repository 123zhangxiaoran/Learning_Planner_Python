"""题目生成智能体模块"""
import json
import re
import time
from typing import Dict, Optional
from datetime import datetime


class QuestionAgent:
    """
    题目生成智能体

    流程：生成 → 质检 → 验证，不达标则改进，最多3轮
    """

    def __init__(self, llm_generator, job_name: str = "", skill_name: str = ""):
        self.llm = llm_generator
        self.job_name = job_name
        self.skill_name = skill_name

    def _invoke_with_retry(self, prompt: str, max_retries: int = 3, log=None) -> Optional[str]:
        """带重试的 LLM 调用"""
        for attempt in range(max_retries):
            try:
                result = self.llm.invoke(prompt)
                return result.content if hasattr(result, 'content') else str(result)
            except Exception as e:
                error_type = type(e).__name__
                if "RateLimitError" in error_type and attempt < max_retries - 1:
                    wait_time = (attempt + 1) * 2  # 2, 4, 6 秒
                    if log:
                        log(f"[重试] {error_type}，{wait_time}秒后重试 ({attempt + 1}/{max_retries})")
                    time.sleep(wait_time)
                else:
                    if log:
                        log(f"[错误] LLM调用异常: {error_type}: {e}")
                    raise

    def generate(self, keyword: str, dim_first: str = "",
                 existing_questions: list = None, q_type: str = "choice",
                 difficulty: int = None,
                 max_iterations: int = 3,
                 save_logs: bool = False) -> Optional[Dict]:
        def log(*args):
            if save_logs:
                print(f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {' '.join(str(a) for a in args)}")

        existing_ref = ""
        if existing_questions:
            existing_ref = "已有相似题目（请避免重复）：\n" + "\n".join(f"- {q}" for q in existing_questions[:5])

        last_question = None
        last_suggestion = ""

        for iteration in range(max_iterations):
            # 1. 生成题目（第一轮无改进建议，后续传入质检/验证的改进建议）
            question = self._generate_question(keyword, dim_first, q_type, existing_ref, last_suggestion, difficulty, log)
            if not question:
                continue
            last_question = question
            log(f"[生成] 第{iteration + 1}轮: {question.get('stem', '')[:50]}...")

            # 2. 质检
            quality_result = self._check_quality(question, q_type)
            quality_score = quality_result.get("score", 0)
            log(f"[质检] 评分={quality_score}分 {'✅' if quality_score >= 7 else '❌'}")

            if quality_score < 7:
                last_suggestion = f"质检不通过: {quality_result.get('issues', [])} {quality_result.get('suggestions', [])}"
                log(f"[改进] {last_suggestion}")
                continue

            # 3. 验证准确性
            accuracy_result = self._verify_accuracy(question, keyword, dim_first, q_type)
            accuracy_score = accuracy_result.get("score", 0)
            log(f"[验证] 评分={accuracy_score}分 {'✅' if accuracy_score >= 7 else '❌'}")

            if accuracy_score >= 7 and accuracy_result.get("is_correct", False):
                log(f"[完成] 题目生成成功")
                return question

            last_suggestion = f"验证不通过: {accuracy_result.get('issues', [])}"
            log(f"[改进] {last_suggestion}")

        log(f"[结束] 未达标，返回最后一道题目")
        return last_question

    def _generate_question(self, keyword: str, dim_first: str, q_type: str,
                          existing_ref: str, improvement: str, difficulty, log) -> Optional[Dict]:
        """生成题目"""
        # 设置难度默认值并确保是整数
        try:
            difficulty_value = int(difficulty) if difficulty is not None else 10
        except (ValueError, TypeError):
            difficulty_value = 10
        if difficulty_value < 1:
            difficulty_value = 1
        elif difficulty_value > 100:
            difficulty_value = 100

        if q_type == "judge":
            prompt = f"""你是{self.job_name}的{self.skill_name}教学专家，负责生成高质量判断题。

知识点：{keyword}
维度描述：{dim_first}
{existing_ref}
{improvement}

要求：
1. 只输出JSON，不要任何前缀文字
2. 判断题格式：stem开头必须是"判断"或"以下说法"，让考生回答"正确"或"错误"
3. 判断题【禁止】包含options字段，不能有任何选项
4. answer字段必须是"正确"或"错误"
5. difficulty字段必须是1-100之间的整数

JSON格式：
{{
    "type": "judge",
    "stem": "以下关于{keyword}的说法，判断是否正确：xxx",
    "answer": "正确" 或 "错误",
    "explanation": "详细解析为什么正确或错误",
    "dimension": "{dim_first}",
    "keyword": "{keyword}",
    "difficulty": {difficulty_value}
}}"""
        elif q_type == "fill":
            prompt = f"""你是{self.job_name}的{self.skill_name}教学专家，负责生成高质量填空题。

知识点：{keyword}
维度描述：{dim_first}
{existing_ref}
{improvement}

要求：
1. 只输出JSON，不要任何前缀文字
2. 填空题格式：stem中使用"___"表示填空位置，每个空填一个关键词或短语
3. 填空题【禁止】包含options字段，不能有任何选项
4. answer字段填答案，多个空用"|"分隔，如"SQL|结构化查询语言"
5. difficulty字段必须是1-100之间的整数

JSON格式：
{{
    "type": "fill",
    "stem": "SQL的英文全称是___，是一种___语言",
    "answer": "Structured Query Language|数据库",
    "explanation": "SQL = Structured Query Language，中文意思是结构化查询语言，是一种用于管理关系型数据库的编程语言",
    "dimension": "{dim_first}",
    "keyword": "{keyword}",
    "difficulty": {difficulty_value}
}}"""
        elif q_type == "analysis":
            prompt = f"""你是{self.job_name}的{self.skill_name}教学专家，负责生成高质量分析题。

知识点：{keyword}
维度描述：{dim_first}
{existing_ref}
{improvement}

要求：
1. 只输出JSON，不要任何前缀文字
2. 分析题格式：stem是开放性问题，要求考生进行分析、解释或论述
3. 分析题【禁止】包含options字段，不能有任何选项
4. answer字段填标准答案要点，用"|"分隔多个要点
5. difficulty字段必须是1-100之间的整数
6. 【注意】分析题不包含explanation字段

JSON格式：
{{
    "type": "analysis",
    "stem": "请分析{keyword}的工作原理，并说明其主要应用场景",
    "answer": "原理说明|应用场景1|应用场景2",
    "dimension": "{dim_first}",
    "keyword": "{keyword}",
    "difficulty": {difficulty_value}
}}"""
        else:
            prompt = f"""你是{self.job_name}的{self.skill_name}教学专家，负责生成高质量选择题。

知识点：{keyword}
维度描述：{dim_first}
{existing_ref}
{improvement}

要求：
1. 只输出JSON，不要任何前缀文字
2. difficulty字段必须是1-100之间的整数
3. answer字段填选项字母（A/B/C/D）
4. 选项必须4个，且有区分度，不能有明显提示

JSON格式：
{{
    "type": "choice",
    "stem": "题目题干",
    "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
    "answer": "A",
    "explanation": "详细解析",
    "dimension": "{dim_first}",
    "keyword": "{keyword}",
    "difficulty": {difficulty_value}
}}"""

        try:
            content = self._invoke_with_retry(prompt, log=log)
            return self._parse_json(content)
        except Exception:
            return None

    def _check_quality(self, question: Dict, q_type: str) -> Dict:
        """质检"""
        if q_type == "judge":
            prompt = f"""你是一个题目质量审核专家，严格审核以下判断题。

题干：{question.get('stem', '')}
答案：{question.get('answer', '')}
解析：{question.get('explanation', '')}
题型：判断题（回答"正确"或"错误"）

审核维度：
1. 题干清晰度 - 判断题题干必须开头是"判断"或"以下说法"，让考生明确是判断题
2. 答案正确性 - 答案必须是"正确"或"错误"
3. 解析完整性 - 解析必须解释为什么正确或错误

评分0-10分，7分以上合格。注意：判断题没有选项是正常的，不需要为此扣分。

只输出JSON：{{"score": 0-10, "issues": [...], "suggestions": [...]}}"""
        elif q_type == "fill":
            prompt = f"""你是一个题目质量审核专家，严格审核以下填空题。

题干：{question.get('stem', '')}
答案：{question.get('answer', '')}
解析：{question.get('explanation', '')}
题型：填空题（使用"___"表示填空）

审核维度：
1. 题干清晰度 - 填空题题干中必须用"___"表示填空位置
2. 答案正确性 - 答案必须合理，多个空用"|"分隔
3. 解析完整性 - 解析必须解释每个空的答案

评分0-10分，7分以上合格。注意：填空题没有选项是正常的，不需要为此扣分。

只输出JSON：{{"score": 0-10, "issues": [...], "suggestions": [...]}}"""
        elif q_type == "analysis":
            prompt = f"""你是一个题目质量审核专家，严格审核以下分析题。

题干：{question.get('stem', '')}
答案：{question.get('answer', '')}
题型：分析题（开放性问题，用"|"分隔多个要点）

审核维度：
1. 题干清晰度 - 分析题题干必须是开放性问题，能引发深入思考
2. 答案合理性 - 答案要点必须合理，多个要点用"|"分隔

评分0-10分，7分以上合格。注意：分析题没有选项和解析是正常的，不需要为此扣分。

只输出JSON：{{"score": 0-10, "issues": [...], "suggestions": [...]}}"""
        else:
            prompt = f"""你是一个题目质量审核专家，严格审核以下选择题。

题干：{question.get('stem', '')}
选项：{question.get('options', [])}
答案：{question.get('answer', '')}
解析：{question.get('explanation', '')}

审核维度：题干清晰度、选项互斥性、答案正确性、解析完整性
评分0-10分，7分以上合格

只输出JSON：{{"score": 0-10, "issues": [...], "suggestions": [...]}}"""

        try:
            content = self._invoke_with_retry(prompt)
            return self._parse_json(content) or {}
        except Exception:
            return {"score": 0, "issues": ["质检调用失败"], "suggestions": []}

    def _verify_accuracy(self, question: Dict, keyword: str, dim_first: str, q_type: str) -> Dict:
        """验证准确性"""
        if q_type == "judge":
            prompt = f"""你是一个专业知识验证专家，验证以下判断题知识点是否准确。

目标知识点：{keyword}
知识点描述：{dim_first}
题干：{question.get('stem', '')}
答案：{question.get('answer', '')}

验证：答案"正确"或"错误"是否符合该知识点的描述？
评分0-10分，7分以上合格，is_correct表示答案是否正确

只输出JSON：{{"score": 0-10, "is_correct": true/false, "issues": [...]}}"""
        elif q_type == "fill":
            prompt = f"""你是一个专业知识验证专家，验证以下填空题知识点是否准确。

目标知识点：{keyword}
知识点描述：{dim_first}
题干：{question.get('stem', '')}
答案：{question.get('answer', '')}

验证：填空题的答案是否准确？多个答案用"|"分隔，每个答案是否正确？
评分0-10分，7分以上合格，is_correct表示答案是否正确

只输出JSON：{{"score": 0-10, "is_correct": true/false, "issues": [...]}}"""
        elif q_type == "analysis":
            prompt = f"""你是一个专业知识验证专家，验证以下分析题知识点是否准确。

目标知识点：{keyword}
知识点描述：{dim_first}
题干：{question.get('stem', '')}
答案：{question.get('answer', '')}

验证：分析题的答案要点是否准确？多个要点用"|"分隔，每个要点是否正确？
评分0-10分，7分以上合格，is_correct表示答案是否正确

只输出JSON：{{"score": 0-10, "is_correct": true/false, "issues": [...]}}"""
        else:
            prompt = f"""你是一个专业知识验证专家，验证以下选择题知识点是否准确。

目标知识点：{keyword}
知识点描述：{dim_first}
题干：{question.get('stem', '')}
答案：{question.get('answer', '')}

验证：答案是否正确？题干是否符合该知识点？
评分0-10分，7分以上合格，is_correct表示答案是否正确

只输出JSON：{{"score": 0-10, "is_correct": true/false, "issues": [...]}}"""

        try:
            content = self._invoke_with_retry(prompt)
            return self._parse_json(content) or {}
        except Exception:
            return {"score": 0, "is_correct": False, "issues": ["验证调用失败"]}

    def _parse_json(self, content: str) -> Optional[Dict]:
        """解析JSON响应"""
        if not content:
            return None
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            pass
        patterns = [
            r'```json\s*([\s\S]*?)\s*```',
            r'```\s*([\s\S]*?)\s*```',
            r'\{[\s\S]*\}'
        ]
        for pattern in patterns:
            match = re.search(pattern, content)
            if match:
                try:
                    json_str = match.group(1) if match.lastindex else match.group(0)
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    continue
        return None
