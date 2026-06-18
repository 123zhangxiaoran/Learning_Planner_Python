"""AI问答后端服务主模块"""
import os
import sys
import json
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import yaml

# 加载配置
def load_config() -> Dict[str, Any]:
    # 尝试多个位置查找 config.yaml
    possible_paths = [
        "config.yaml",  # 当前工作目录
        os.path.join(os.path.dirname(sys.executable), "config.yaml"),  # exe 同级目录
    ]

    # PyInstaller 打包后的临时目录
    if getattr(sys, '_MEIPASS', None):
        possible_paths.insert(0, os.path.join(sys._MEIPASS, "config.yaml"))

    for config_path in possible_paths:
        if os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f)

    raise FileNotFoundError(f"config.yaml not found in: {possible_paths}")

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