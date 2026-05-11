# Python 后端架构介绍

## 项目概述

这是一个基于 FastAPI 的 AI 问答后端服务，主要功能是根据用户的专业/就业方向，通过向量数据库检索匹配的岗位信息和技能要求。

## 目录结构

```
Learning_Planner_Python/
├── app/                          # 主应用模块
│   ├── __init__.py              # 配置加载和请求/响应模型定义
│   ├── api/                     # API 路由层
│   │   ├── __init__.py
│   │   └── routes.py            # RESTful API 接口定义
│   └── services/                # 业务逻辑服务层
│       ├── __init__.py
│       ├── ai_service.py        # AI 问答服务
│       └── vector_service.py    # 向量数据库服务
├── data/                        # 数据存储目录
│   └── chroma_db/               # ChromaDB 向量数据库持久化存储
├── config.yaml                  # 应用配置文件
├── init_vectors.py              # 向量库数据初始化脚本
├── main.py                      # 应用启动入口
└── requirements.txt             # Python 依赖包列表
```

## 技术栈

### 核心框架
- **FastAPI** (>=0.104.0) - 现代、高性能的 Web 框架，用于构建 RESTful API
- **Uvicorn** (>=0.24.0) - ASGI 服务器，用于运行 FastAPI 应用

### 向量数据库与嵌入
- **ChromaDB** (>=0.4.0) - 本地向量数据库，用于存储和检索文档向量
- **LangChain** (>=0.1.0) - AI 应用开发框架，提供统一的 LLM 接口
- **LangChain Community/Ollama/OpenAI** - LangChain 扩展包，支持不同的嵌入模型

### AI 模型
- **通义千问 (qwen-plus)** - 阿里云 DashScope 提供的大语言模型
- **Ollama (bge-m3)** - 本地嵌入模型，用于生成文本向量

### 其他依赖
- **Pydantic** (>=2.5.0) - 数据验证和设置管理
- **python-dotenv** (>=1.0.0) - 环境变量管理
- **NumPy** (>=1.24.0) - 数值计算，用于向量相似度计算

## 核心模块说明

### 1. 应用入口 (main.py)

负责启动 FastAPI 应用，包括：
- 创建 FastAPI 实例并配置 CORS 中间件
- 注册 API 路由
- 启动 ASGI 服务器（默认地址：0.0.0.0:8000）

**启动方式：**
```bash
python main.py
```

### 2. 配置管理 (config.yaml)

应用配置包含以下部分：
- **service** - 服务运行配置（host, port, debug）
- **vector_db** - 向量数据库配置（类型、存储路径、集合名称）
- **ai** - AI 模型配置（provider, model, temperature, max_tokens）
- **embedding** - 嵌入模型配置（provider, model）
- **prompt** - 提示词模板配置

### 3. API 路由层 (app/api/routes.py)

定义了以下核心 API 接口：

#### 业务接口
- **POST /api/jobs/search** - 岗位查询
  - 参数：major（专业）、top_k（返回数量）、min_score（相似度阈值）
  - 功能：根据专业方向返回匹配的岗位，支持专业名称和岗位描述的双重相似度匹配

- **POST /api/skills/search** - 技能查询
  - 参数：jobs（岗位列表）、top_k、min_score
  - 功能：根据岗位名称返回技能要求（精确匹配）

- **POST /api/skill/analytical** - 学习资料生成
  - 参数：text（用户输入）、job_names（岗位列表）、selected_skill（选中的技能）
  - 功能：调用 AI 服务，基于 ReAct Agent 架构生成学习计划和学习题目

#### 管理接口
- **POST /api/documents** - 添加文档到向量库
- **GET /api/collection/info** - 获取向量库信息
- **DELETE /api/collection** - 清空向量库
- **GET /api/health** - 健康检查

### 4. 服务层 (app/services/)

#### VectorService (vector_service.py)
向量数据库服务，提供以下核心功能：
- **add_documents** - 添加文档到 ChromaDB
- **similarity_search** - 向量相似度检索
- **get_by_metadata** - 根据元数据精确查询
- **compute_similarity** - 计算两个文本的余弦相似度
- **compute_similarities_batch** - 批量计算相似度（使用多线程并行优化）

**优化特性：**
- 使用线程池批量计算相似度，提升性能
- 支持两种嵌入模型：Ollama（本地）和 OpenAI（云端）
- 向量持久化存储，重启后数据不丢失

#### AIService (ai_service.py)
AI 问答服务，基于 **ReAct Agent 架构**，提供以下功能：
- **generate_learning_plan** - 生成学习计划和题目（主入口）
- **generate_quiz 工具** - 生成题目的 StructuredTool

**架构特点：**
- **双模型设计**：
  - `llm_parser`：意图识别 + 参数提取（temperature=0）
  - `llm_generator`：题目内容生成（temperature=0.7）
- **ReAct Agent**：理解用户意图，自动调用题目生成工具
- **StructuredTool**：将题目生成函数封装为 LangChain 工具

**支持的题目类型**：
| 类型 | 标识 | 说明 |
|------|------|------|
| 选择题 | choice | 4个选项，唯一正确答案，含解析 |
| 填空题 | filling | 留出空白关键词，含答案 |
| 判断题 | true_false | 判断正误，解释原因 |
| 分析题 | analysis | 分析输出结果，附带解析 |
| 写作题 | writing | 写作任务 |

**输入参数**：
- `text`：用户原始输入
- `target_jobs`：目标岗位列表
- `selected_skill`：选中的技能

**输出格式**：
```json
{
    "type": "choice",
    "stem": "题目题干",
    "options": ["A. xxx", "B. xxx", "C. xxx", "D. xxx"],
    "answer": "正确答案",
    "explanation": "详细解析",
    "code_snippet": "代码片段或空字符串"
}
```

### 5. 数据初始化 (init_vectors.py)

用于初始化向量库数据，包含以下内容：
- 计算机类岗位数据（软件工程、人工智能、网络工程等）
- 每个岗位包含描述和技能列表
- 技能格式：`技能名称:技能描述`

**数据结构：**
```python
{
  "level1": "计算机",      # 领域
  "level2": "软件工程",    # 专业/就业方向
  "level3": "前端开发工程师",  # 岗位名称
  "level3_desc": "岗位描述",  # 岗位详细描述
  "level4": "技能列表",     # 技能名称列表
  "level4_desc": "技能:描述; 技能:描述"  # 技能详细描述
}
```

## 工作流程

### 岗位查询流程
1. 用户输入专业方向（如"软件工程"）
2. VectorService 使用向量检索返回相似岗位（初始取 50 个）
3. **相似度匹配算法**：
   - **70% 阈值直接命中**：若专业名称相似度 ≥ 70%，直接使用该结果
   - **否则使用权重计算**：专业名称相似度 35% + 完整文本相似度 65%
4. 批量计算加权相似度并重新排序
5. 返回 Top 岗位结果

### 技能查询流程
1. 用户输入岗位名称列表（如["前端开发工程师", "后端开发工程师"]）
2. VectorService 根据元数据精确匹配查询
3. 解析技能详细描述（格式：`技能:描述; 技能:描述`）
4. 返回技能列表及描述

### 技能分析对比流程（学习计划和题目生成）
1. 用户输入文本、目标岗位列表、选中的技能
2. 调用 `generate_learning_plan` 启动 ReAct Agent
3. Agent 识别用户意图（生成题目）
4. 调用 `generate_quiz` 工具：
   - `llm_parser` 提取参数（难度、题型、知识点）
   - `llm_generator` 生成题目内容
5. 返回格式化题目 JSON

## 环境变量

需要配置以下环境变量：
- `DASHSCOPE_API_KEY` - 阿里云 DashScope API 密钥（用于通义千问）
- `OPENAI_API_KEY` - OpenAI API 密钥（备用）

## 部署说明

### 本地开发
1. 安装依赖：`pip install -r requirements.txt`
2. 设置环境变量
3. 启动服务：`python main.py`
4. 初始化数据：`python init_vectors.py`（可选）

### Docker 部署
可使用 Docker 容器化部署，需要挂载 `data/chroma_db` 目录以持久化向量数据。

## 性能优化

1. **批量计算相似度** - 使用 `compute_similarities_batch` 和线程池并行计算
2. **向量持久化** - ChromaDB 使用持久化存储，避免每次重启重建
3. **缓存嵌入模型** - 嵌入模型在内存中保持，避免重复加载

## 扩展性

项目采用分层架构，易于扩展：
- **新接口**：在 `routes.py` 中添加新的路由
- **新服务**：在 `services/` 目录下添加新的服务类
- **新数据源**：修改 `init_vectors.py` 添加新的数据
- **新 AI 模型**：在 `ai_service.py` 中配置不同的模型提供商

## 注意事项

1. 向量库数据初始化需要先启动服务
2. Ollama 嵌入模型需要提前在本地安装并启动 Ollama 服务
3. 通义千问 API 需要有效的阿里云 DashScope API 密钥
4. 相似度阈值可根据实际需求调整
