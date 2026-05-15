"""API路由"""
from typing import Dict, Any, Optional, List, Union
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

# 导入服务
from app.services.vector_service import VectorService
from app.services.ai_service import AIService
from app import config

# 初始化服务
vector_service = VectorService(config)
ai_service = AIService(config)

router = APIRouter()

# ============ 请求/响应模型 ============

class JobSearchRequest(BaseModel):
    """岗位查询请求"""
    major: str  # 专业或就业方向
    top_k: int = 6  # 默认值6
    min_score: float = 0.1  # 最低相似度阈值，降低默认值

class SkillSearchRequest(BaseModel):
    """技能查询请求"""
    jobs: List[str]  # 岗位名称列表（支持多个岗位）
    top_k: int = 5
    min_score: float = 0.3  # 最低相似度阈值
    isNews: Optional[bool] = True  # 是否新请求
    jobToken: Optional[int] = None  # 岗位令牌

class SkillAnalyticalRequest(BaseModel):
    """技能分析对比请求 - 用于大模型提示词生成"""
    text: str  # 用户输入的文本（如"你好"、技能描述、问题等）
    job_names: List[str]  # 岗位名称数组（如["后端开发工程师"]）
    selected_skill: Optional[str] = None  # 用户选中的技能（如"Java"）

class AddDocumentRequest(BaseModel):
    """添加文档请求"""
    texts: List[str]
    metadatas: Optional[List[Dict[str, Any]]] = None

class QuestionRequest(BaseModel):
    """用户提问请求"""
    question: str
    context: Optional[Dict[str, Any]] = None
    use_vector_search: bool = True
    top_k: int = 5

class FetchSkillKnowRequest(BaseModel):
    """获取技能知识点请求"""
    job_names: str  # 岗位名称
    selected_skill: str  # 选中的技能名称

class AnswerResponse(BaseModel):
    """问答响应"""
    answer: str
    sources: Optional[List[Dict[str, Any]]] = None
    vector_results: Optional[List[Dict[str, Any]]] = None
    metadata: Optional[Dict[str, Any]] = None

# ============ API路由 ============

@router.post("/api/jobs/search")
async def search_jobs(request: JobSearchRequest):
    """
    岗位查询接口 - 页面1
    根据专业/就业方向，返回匹配的岗位名称和描述
    """
    try:
        # 向量检索（已按相似度排序）
        results = vector_service.similarity_search(
            query=request.major,
            top_k=50  # 多取一些，后面重新排序
        )

        # 提取所有需要计算相似度的文本（去掉技能，只保留专业+岗位+描述）
        majors = []
        job_texts = []  # 专业+岗位+描述，不包含技能
        valid_indices = []

        for i, r in enumerate(results):
            metadata = r.get("metadata", {})
            if not metadata.get("level3"):
                continue
            majors.append(metadata.get("level2", ""))
            # 构建不包含技能的文本：专业+岗位+描述
            job_text = f"专业：{metadata.get('level2', '')} | 岗位：{metadata.get('level3', '')} | 描述：{metadata.get('level3_desc', '')}"
            job_texts.append(job_text)
            valid_indices.append(i)

        # 批量并行计算专业名称相似度
        similarity_majors = vector_service.compute_similarities_batch(
            request.major, majors
        ) if majors else []

        # 批量并行计算岗位文本相似度（不含技能）
        similarity_jobs = vector_service.compute_similarities_batch(
            request.major, job_texts
        ) if job_texts else []

        # 构建结果列表
        jobs = []
        for idx, (sim_major, sim_job) in enumerate(zip(similarity_majors, similarity_jobs)):
            r = results[valid_indices[idx]]
            metadata = r.get("metadata", {})

            # 检查是否有 >=70% 的原始相似度（不用权重）
            max_raw_similarity = max(sim_major, sim_job)

            if max_raw_similarity >= 0.7:
                # 有 >=70% 的，直接用最大的，不用权重
                final_similarity = max_raw_similarity
            else:
                # 没有达到70% 的，使用权重计算
                final_similarity = sim_major * 0.35 + sim_job * 0.65

            jobs.append({
                "job_name": metadata.get("level3"),
                "job_description": metadata.get("level3_desc"),
                "major": metadata.get("level2"),
                "similarity": round(final_similarity * 100, 2)  # 相似度百分比
            })

        # 按相似度重新排序
        jobs.sort(key=lambda x: x["similarity"], reverse=True)

        # 过滤掉相似度低于60%的结果
        jobs = [j for j in jobs if j["similarity"] >= 60]

        return {
            "jobs": jobs[:6]  # 返回top 6
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败: {str(e)}")


@router.post("/api/skills/search")
async def search_skills(request: SkillSearchRequest):
    """
    技能查询接口 - 页面2
    根据岗位名称列表，返回匹配的技能要求
    """
    try:
        all_skills = []
        
        # 精确匹配：根据岗位名称直接查询
        results = vector_service.get_by_metadata("level3", request.jobs)
        
        # 解析技能详细描述
        for r in results:
            metadata = r.get("metadata", {})
            
            level4_desc = metadata.get("level4_desc", "")
            skills_difficulty = metadata.get("skills_difficulty", "")
            skills_list = []

            # 解析技能难度
            difficulty_map = {}
            if skills_difficulty:
                for item in skills_difficulty.split('; '):
                    if '(' in item and ')' in item:
                        skill_name = item.split('(')[0].strip()
                        difficulty = item.split('(')[1].rstrip(')')
                        difficulty_map[skill_name] = int(difficulty)

            if level4_desc:
                for item in level4_desc.split('; '):
                    if ':' in item:
                        skill_name, skill_desc = item.split(':', 1)
                        skill_name = skill_name.strip()
                        skills_list.append({
                            "name": skill_name,
                            "description": skill_desc.strip(),
                            "difficulty": difficulty_map.get(skill_name, 2)
                        })

            if metadata.get("level3") and skills_list:
                all_skills.append({
                    "job_name": metadata.get("level3"),
                    "skills": skills_list,
                    "major": metadata.get("level2")
                })
        
        response = {
            "success": True,
            "query": request.jobs,
            "skills": all_skills[:request.top_k]
        }
        
        # isNews为false时返回jobToken
        if not request.isNews:
            response["jobToken"] = request.jobToken
        
        return response
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"查询失败: {str(e)}")


# ============ 辅助接口（管理用）===========

@router.post("/api/documents")
async def add_documents(request: AddDocumentRequest):
    """添加文档到向量库"""
    try:
        ids = vector_service.add_documents(
            texts=request.texts,
            metadatas=request.metadatas
        )
        return {"success": True, "message": f"成功添加 {len(ids)} 个文档", "ids": ids}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"添加文档失败: {str(e)}")


@router.get("/api/collection/info")
async def get_collection_info():
    """获取向量库信息"""
    try:
        info = vector_service.get_collection_info()
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/api/collection")
async def delete_collection():
    """清空向量库"""
    try:
        vector_service.delete_collection()
        return {"success": True, "message": "向量库已清空"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/api/health")
async def health_check():
    """健康检查"""
    return {"status": "ok"}


@router.post("/api/skill/analytical")
async def skill_analytical(request: SkillAnalyticalRequest):
    """
    技能分析接口 - 为大模型提示词模板提供数据
    
    提取三个核心字段用于提示词生成：
    - text: 用户输入的原始文本
    - job_names: 目标岗位列表
    - selected_skill: 用户选中的技能
    
    同时返回该岗位下的所有技能列表，供大模型分析和生成学习计划
    """
    try:
        # 构建提示词模板所需的数据结构
        prompt_data = {
            "text": request.text,                    # 用户输入文本
            "target_jobs": request.job_names[0],        # 目标岗位
            "selected_skill": request.selected_skill  # 选中的技能
        }

        # 在调用大模型生成学习资料
        ai_response = ai_service.generate_learning_plan(prompt_data)
        return {
            "success": True,
            "data": ai_response,
            "message": "大模型数据推理成功"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"学习资料生成失败: {str(e)}")


@router.post("/api/skill/fetchSkill")
async def fetch_skill_knowledge(request: FetchSkillKnowRequest):
    """
    获取技能知识点接口
    根据岗位名称列表和选中的技能，返回该技能的知识点维度
    """
    try:
        # 使用 get_by_metadata 根据岗位名称精确查询
        results = vector_service.get_by_metadata("level3", [request.job_names])

        for r in results:
            metadata = r.get("metadata", {})
            # 从 level4_desc 中解析技能和描述
            level4_desc = metadata.get("level4_desc", "")
            skills_difficulty = metadata.get("skills_difficulty", "")

            # 构建技能难度映射
            difficulty_map = {}
            if skills_difficulty:
                for item in skills_difficulty.split('; '):
                    if '(' in item and item.endswith(')'):
                        skill_name = item.split('(')[0].strip()
                        difficulty = item.split('(')[1].rstrip(')')
                        difficulty_map[skill_name] = int(difficulty)

            # 解析技能描述，找到用户选中的技能
            if level4_desc:
                for item in level4_desc.split('; '):
                    if ':' in item:
                        skill_name, skill_desc = item.split(':', 1)
                        skill_name = skill_name.strip()

                        # 找到匹配的技能
                        if skill_name == request.selected_skill:
                            # 从 metadata 中获取该技能的知识点
                            dim_key = f"skill_dims_{skill_name}"
                            dimensions_str = metadata.get(dim_key, "")
                            dimensions_list = [d.strip() for d in dimensions_str.split('; ')] if dimensions_str else []

                            return {
                                "success": True,
                                "skill_name": skill_name,
                                "skill_description": skill_desc.strip(),
                                "difficulty": difficulty_map.get(skill_name, 2),
                                "dimensions": dimensions_list,
                                "job_name": metadata.get("level3"),
                                "major": metadata.get("level2")
                            }

        return {
            "success": False,
            "message": f"未找到技能 '{request.selected_skill}' 对应的知识点"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取技能知识点失败: {str(e)}")