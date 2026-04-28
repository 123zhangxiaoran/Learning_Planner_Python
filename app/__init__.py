"""AI问答后端服务主模块"""
import os
import json
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml

# 加载配置
def load_config() -> Dict[str, Any]:
    # 配置在项目根目录
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_path = os.path.join(root_dir, "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

config = load_config()

app = FastAPI(title="AI问答后端服务", version="1.0.0")

# 请求模型
class QuestionRequest(BaseModel):
    """用户提问请求"""
    question: str
    context: Optional[Dict[str, Any]] = None  # Java后端传入的上下文
    user_id: Optional[str] = None

# 响应模型
class AnswerResponse(BaseModel):
    """问答响应"""
    answer: str
    sources: Optional[list] = None
    metadata: Optional[Dict[str, Any]] = None