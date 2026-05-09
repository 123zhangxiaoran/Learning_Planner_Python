"""AI问答服务"""
import os
from typing import Dict, Any, Optional, List
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage


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

        # 阿里云DashScope的通义千问
        self.llm = ChatOpenAI(
            api_key=api_key,
            model="qwen-plus",
            temperature=self.ai_config.get("temperature", 0.4),
            max_tokens=self.ai_config.get("max_tokens", 2000),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 阿里云API端点
        )

    async def generate_learning_plan(self, prompt_data: Dict[str, Any]) -> Dict[str, Any]:
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
        target_jobs = prompt_data.get("target_jobs", "")
        selected_skill = prompt_data.get("selected_skill", "")
        

        return "OK"