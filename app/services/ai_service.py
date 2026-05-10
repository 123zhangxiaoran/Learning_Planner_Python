"""AI问答服务"""
import os
import json
from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.tools import StructuredTool
from langchain_core.prompts import PromptTemplate
from langchain_classic.agents import AgentExecutor, create_react_agent


class AIService:
    """AI问答服务"""

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.ai_config = config.get("ai", {})

        # 初始化通义千问（阿里云DashScope）
        api_key = os.getenv("DASHSCOPE_API_KEY")
        if not api_key:
            api_key = os.getenv("OPENAI_API_KEY")  # 兼容旧环境变量

        if not api_key:
            raise ValueError("未设置环境变量 DASHSCOPE_API_KEY 或 OPENAI_API_KEY")

        # 分析模型
        self.llm_generator = ChatOpenAI(
            api_key=api_key,
            model="qwen-plus",
            temperature=self.ai_config.get("temperature", 0.8),
            max_tokens=self.ai_config.get("max_tokens", 2000),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        
        # 提取模型
        self.llm_parser = ChatOpenAI(
            api_key=api_key,
            model="qwen-plus",
            temperature=self.ai_config.get("temperature", 0),
            max_tokens=self.ai_config.get("max_tokens", 2000),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

    def generate_learning_plan(self, prompt_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        生成学习计划

        Args:
            prompt_data: 包含以下字段的字典
                - text: 用户输入的文本
                - target_jobs: 目标岗位
                - selected_skill: 选中的技能

        Returns:
            大模型生成的学习计划
        """
        text = prompt_data.get("text", "")
        target_jobs = prompt_data.get("target_jobs", [])
        selected_skill = prompt_data.get("selected_skill", "")

        # 题目生成函数
        def generate_quiz(input: str):
            """生成一道题目，直接返回JSON格式。"""
            
            # 调用提取LLM生成题目
            parse_prompt = f"""从用户输入中提取参数：
        用户输入：{input}

        可选值：
            - difficulty: "简单"/"中等"/"困难"，没有默认值：简单
            - question_type: "choice(选择题)"/"filling(填空题)"/"true_false(判断题)"/"analysis(分析题)"/"writing(编写题)"，没有默认值：choice
            - topic: 知识点，没有默认值：基础知识点

        直接返回 JSON 格式：{{"topic": "...", "difficulty": "简单", "question_type": "choice"}}"""
            result = self.llm_parser.invoke(parse_prompt)
            params = json.loads(result.content)
            difficulty = params.get("difficulty", "简单")
            question_type = params.get("question_type", "choice")
            topic = params.get("topic", "基础知识点")
            
            # 调用生成LLM生成题目
            type_instructions = {
                "choice": "生成一道选择题，包含4个选项，里面只有一个正确答案，指明正确答案，并给出解析",
                "filling": "生成一道填空题，留出一个空白(在重点关键词)，并给出答案",
                "true_false": "生成一道判断题，陈述正确或错误，并解释原因",
                "analysis": "生成一道分析题，要求分析输出结果，并附带解析",
                "writing": "生成一道编写大题，并给出参考答案"
            }
            instruction = type_instructions.get(question_type, type_instructions["choice"])
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
                "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"]
                "answer": "正确答案",
                "explanation": "详细解析",
                "code_snippet": "如果有代码，放在这里，否则为空字符串"
            }}"""
            result = self.llm_generator.invoke(question_prompt)
            
            # 返回结果
            return result.content

        # 包装题目生成函数为工具
        quiz_tool = StructuredTool.from_function(
            func=generate_quiz,
            name="generate_quiz",
            description="""当用户的意图是：帮助我生成学习题目时调用此工具
        输入：user_input(用户的原始需求，如"出一道简单选择题"、"出Python题目")
        输出：生成的题目JSON"""
        )

        # 创建ReAct格式的prompt
        react_prompt = PromptTemplate.from_template(
            f"""你是专门理解用户意图的机器人，识别用户的意图，使用对应的工具：
        {{tools}}
        可用工具: {{tool_names}}
        
        重要规则：
            - Action Input 只能放用户原始输入，不要放其他内容
            - 工具返回后，进入 Observation 阶段
            - 工具返回后，输出 Final Answer 结束，不要再调用工具

        格式：
        Thought: 分析用户的意图？这个意图需要使用哪些工具？
        Action: [工具名称]
        Action Input: {{input}}(只放用户输入，不要放工具返回的内容)
        Observation: 工具返回结果
        Final Answer: 最终回答(工具返回的内容)

        {{agent_scratchpad}}"""
        )

        # 初始化ReAct智能体
        agent = create_react_agent(
            llm=self.llm_generator,
            tools=[quiz_tool],
            prompt=react_prompt
        )

        # 创建AgentExecutor
        agent_executor = AgentExecutor(
            agent=agent,
            tools=[quiz_tool],
            verbose=False,
            handle_parsing_errors=True,
            max_iterations=5
        )

        # 调用智能体
        response = agent_executor.invoke({"input": text})

        return response["output"]
