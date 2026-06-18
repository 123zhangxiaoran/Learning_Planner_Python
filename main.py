"""AI问答后端服务启动入口"""
import os
import sys
import logging

# 配置日志 - 关闭 INFO 输出，只显示 WARNING 及以上
logging.basicConfig(
    level=logging.WARNING,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yaml

# 导入配置和路由
from app import config
from app.api.routes import router

# 创建FastAPI应用
app = FastAPI(
    title="AI问答后端服务",
    description="接收Java后端JSON数据，结合向量库检索，生成AI回答",
    version="1.0.0"
)

# 添加CORS中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(router)

# 启动配置
HOST = config.get("service", {}).get("host", "0.0.0.0")
PORT = config.get("service", {}).get("port", 8000)
DEBUG = config.get("service", {}).get("debug", True)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=HOST,
        port=PORT,
        reload=DEBUG
    )