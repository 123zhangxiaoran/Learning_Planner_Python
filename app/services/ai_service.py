"""AI问答服务"""
import os
import json
from typing import Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.agents import AgentExecutor, create_react_agent

from app.tools.quiz_tools import create_quiz_tool
from app.tools.chat_tools import create_chat_tool
from app.tools.ppt_tools import create_ppt_tool
from app.services.question_service import QuestionService

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
            model=self.ai_config.get("model", "qwen-plus"),
            temperature=self.ai_config.get("temperature", 0.7),
            max_tokens=self.ai_config.get("max_tokens", 5000),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        
        # 提取模型
        self.llm_parser = ChatOpenAI(
            api_key=api_key,
            model=self.ai_config.get("model", "qwen-plus"),
            temperature=self.ai_config.get("temperature", 0),
            max_tokens=self.ai_config.get("max_tokens", 5000),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )

    def generate_learning_plan(self, prompt_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        生成学习计划

        Args:
            prompt_data: 包含以下字段的字典
                - userinput: 用户输入的文本
                - task: 任务类型（可选，如 "generate_questions" 表示直接出题）

        Returns:
            大模型生成的学习计划
        """

        # 检查是否为专门的题目生成任务
        task_type = prompt_data.get("task", "")
        if task_type == "generate_questions":
            # 使用 QuestionService 生成题目
            question_service = QuestionService(
                self.llm_generator,
                prompt_data.get("job_name", ""),
                prompt_data.get("skill_name", "")
            )
            return question_service.generate_questions(
                prompt_data.get("dimensions", []),
                prompt_data.get("user_id", 1)
            )

        # 创建题目生成工具
        quiz_tool = create_quiz_tool(self.llm_generator, prompt_data.get("job_name", ""), prompt_data.get("skill_name", ""))
        # 创建聊天工具
        chat_tool = create_chat_tool(self.llm_generator)
        # 创建生成ppt学习规划工具
        ppt_tool = create_ppt_tool(self.llm_generator, prompt_data.get("skill_name", ""), prompt_data.get("job_name", ""), prompt_data.get("dimensions", ""), prompt_data.get("user_id"))

        # 创建ReAct格式的prompt
        react_prompt = PromptTemplate.from_template(
            """你是专门理解用户意图的机器人，识别用户的意图，使用对应的工具：
        {tools}
        可用工具: {tool_names}

        用户输入: {input}

        重要规则：
            1.严格按照"tool.parameters"里面的参数提取，如果没有指定，则使用默认值
            2.只输出 Thought、Action、Action Input 三行，不要输出其他内容
            3.一次只能调用一个工具，不要同时调用多个工具
            4.使用一次工具的返回结果后，直接输出Final Answer
            5.Final Answer 输出的是工具返回的原始数据，不要再做任何处理，不要丢数据

        格式：
        Thought: 分析用户的意图，并调用对应的工具，按照"parameters"里的定义提取参数
        Action: 工具名称
        Action Input: {{"参数名": "参数值", ...}}
        

        示例1：
        用户："出一道关于底层原理比较难的判断题"
        Thought: 用户要出题目，使用出题工具，根据工具"parameters"提取参数：topic指定"底层原理"，difficulty有"困难"选项，question_type有"true_false"对应判断题
        Action: generate_quiz
        Action Input: {{"topic": "底层原理", "difficulty": "困难", "question_type": "true_false"}}

        示例2：
        用户："出一道编写题"
        Thought: 用户要出题目，使用出题工具，根据工具"parameters"提取参数：topic未指定填"基础知识点"，difficulty未指定填"简单"，question_type在tool.parameters里不存在，使用默认值"choice"
        Action: generate_quiz
        Action Input: {{"topic": "基础知识点", "difficulty": "简单", "question_type": "choice"}}
        
        示例3：
        用户："出个填空题"
        Thought: 用户要出题目，使用出题工具，根据工具"parameters"提取参数：topic未指定填"基础知识点"，difficulty未指定填"简单"，question_type对应填空题为"filling"
        Action: generate_quiz
        Action Input: {{"topic": "基础知识点", "difficulty": "简单", "question_type": "filling"}}
        
        示例4：
        用户："出一道还行的分析题"
        Thought: 用户要出题目，使用出题工具，根据工具"parameters"提取参数：topic未指定填"基础知识点"，difficulty有"中等"，question_type对应填空题为"analysis"
        Action: generate_quiz
        Action Input: {{"topic": "基础知识点", "difficulty": "中等", "question_type": "analysis"}}
        
        示例5：
        用户："小文，你好啊！"
        Thought: 用户要聊天，使用聊天工具，根据工具"parameters"提取参数：question是用户的输入
        Action: chat
        Action Input: {{"question": "用户的输入"}}
        
        示例6：
        用户："帮我生成一份ppt"
        Thought: 用户要生成ppt，使用生成ppt工具，根据工具"parameters"提取参数：没有parameters字段，不需要提取参数，直接调用工具
        Action: generate_ppt
        Action Input: {{}}


        {agent_scratchpad}"""
        )

        # 初始化ReAct智能体
        agent = create_react_agent(
            llm=self.llm_parser,
            tools=[quiz_tool, chat_tool, ppt_tool],
            prompt=react_prompt
        )

        # 创建AgentExecutor
        agent_executor = AgentExecutor(
            agent=agent,
            tools=[quiz_tool, chat_tool, ppt_tool],
            verbose=True,
            handle_parsing_errors="""Agent stopped due to iteration limit or time limit.""",
            max_iterations=5
        )

        # 调用智能体
        response = agent_executor.invoke({"input": prompt_data.get("userinput", "")})

        return response["output"]
