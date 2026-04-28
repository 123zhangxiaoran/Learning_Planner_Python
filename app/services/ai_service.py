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
        self.prompt_config = config.get("prompt", {})
        
        # 初始化通义千问（阿里云DashScope）
        api_key = os.getenv("DASHSCOPE_API_KEY")
        if not api_key:
            api_key = os.getenv("OPENAI_API_KEY")  # 兼容旧环境变量
        
        if not api_key:
            raise ValueError("未设置环境变量 DASHSCOPE_API_KEY 或 OPENAI_API_KEY")
        
        # 阿里云DashScope的通义千问
        self.llm = ChatOpenAI(
            api_key=api_key,
            model="qwen-turbo",  # 或 qwen-plus, qwen-max
            temperature=self.ai_config.get("temperature", 0.7),
            max_tokens=self.ai_config.get("max_tokens", 2000),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"  # 阿里云API端点
        )

        # 加载提示词模板
        self.system_template = self.prompt_config.get("system_template", 
            "你是一个专业的问答助手，请根据提供的上下文信息回答用户的问题。")
        self.user_template = self.prompt_config.get("user_template",
            "上下文信息：\n{context}\n\n用户问题：{question}\n\n请根据以上上下文信息回答问题。")
    
    def build_context_from_json(self, context_json: Dict[str, Any]) -> str:
        """从Java后端传入的JSON构建上下文"""
        context_parts = []
        
        if isinstance(context_json, dict):
            for key, value in context_json.items():
                if isinstance(value, (str, int, float)):
                    context_parts.append(f"{key}: {value}")
                elif isinstance(value, list):
                    context_parts.append(f"{key}:")
                    for item in value:
                        if isinstance(item, dict):
                            for k, v in item.items():
                                context_parts.append(f"  - {k}: {v}")
                        else:
                            context_parts.append(f"  - {item}")
                elif isinstance(value, dict):
                    context_parts.append(f"{key}:")
                    for k, v in value.items():
                        context_parts.append(f"  - {k}: {v}")
        
        return "\n".join(context_parts) if context_parts else "无额外上下文信息"
    
    def build_context_from_vector_results(self, vector_results: List[Dict[str, Any]]) -> str:
        """从向量检索结果构建上下文"""
        context_parts = []
        
        for i, result in enumerate(vector_results, 1):
            content = result.get("content", "")
            metadata = result.get("metadata", {})
            
            context_parts.append(f"【参考文档 {i}】")
            if metadata:
                context_parts.append(f"来源: {metadata}")
            context_parts.append(f"内容: {content}")
            context_parts.append("")
        
        return "\n".join(context_parts) if context_parts else "未找到相关参考信息"
    
    def generate_answer(
        self, 
        question: str, 
        context_json: Optional[Dict[str, Any]] = None,
        vector_results: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """生成答案"""
        # 构建上下文
        context_parts = []
        
        # 添加JSON上下文
        if context_json:
            json_context = self.build_context_from_json(context_json)
            context_parts.append(f"【传入数据】\n{json_context}")
        
        # 添加向量检索上下文
        if vector_results:
            vector_context = self.build_context_from_vector_results(vector_results)
            context_parts.append(f"【知识库检索结果】\n{vector_context}")
        
        full_context = "\n\n".join(context_parts) if context_parts else "无上下文信息"
        
        # 构建提示词
        user_prompt = self.user_template.format(
            context=full_context,
            question=question
        )
        
        # 调用AI生成答案
        messages = [
            SystemMessage(content=self.system_template),
            HumanMessage(content=user_prompt)
        ]
        
        response = self.llm.invoke(messages)
        answer = response.content if hasattr(response, "content") else str(response)
        
        # 提取参考来源
        sources = []
        if vector_results:
            for result in vector_results:
                if result.get("metadata"):
                    sources.append(result["metadata"])
        
        return {
            "answer": answer,
            "sources": sources,
            "context_used": {
                "json_context": context_json is not None,
                "vector_results_count": len(vector_results) if vector_results else 0
            }
        }
    
    def chat(self, messages: List[Dict[str, str]]) -> str:
        """通用聊天接口"""
        langchain_messages = []
        
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            
            if role == "system":
                langchain_messages.append(SystemMessage(content=content))
            else:
                langchain_messages.append(HumanMessage(content=content))
        
        response = self.llm.invoke(langchain_messages)
        return response.content if hasattr(response, "content") else str(response)