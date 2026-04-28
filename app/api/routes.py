"""API路由"""
from typing import Dict, Any, Optional, List
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

class SkillAnalyticalRequest(BaseModel):
    """技能分析对比请求"""
    text: str  # 用户输入的文本（包含技能描述等信息）
    job_names: List[str]  # 岗位名称数组

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

        # 提取所有需要计算相似度的文本
        majors = []
        full_texts = []
        valid_indices = []

        for i, r in enumerate(results):
            metadata = r.get("metadata", {})
            if not metadata.get("level3"):
                continue
            majors.append(metadata.get("level2", ""))
            full_texts.append(r.get("content", ""))
            valid_indices.append(i)

        # 批量并行计算专业名称相似度
        similarity_majors = vector_service.compute_similarities_batch(
            request.major, majors
        ) if majors else []

        # 批量并行计算完整文本相似度
        similarity_fulls = vector_service.compute_similarities_batch(
            request.major, full_texts
        ) if full_texts else []

        # 构建结果列表
        jobs = []
        for idx, (sim_major, sim_full) in enumerate(zip(similarity_majors, similarity_fulls)):
            r = results[valid_indices[idx]]
            metadata = r.get("metadata", {})

            # 取平均值
            avg_similarity = (sim_major + sim_full) / 2

            jobs.append({
                "job_name": metadata.get("level3"),
                "job_description": metadata.get("level3_desc"),
                "major": metadata.get("level2"),
                "similarity": round(avg_similarity * 100, 2)  # 相似度百分比
            })

        # 按平均相似度重新排序
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
            skills_list = []
            if level4_desc:
                for item in level4_desc.split('; '):
                    if ':' in item:
                        skill_name, skill_desc = item.split(':', 1)
                        skills_list.append({
                            "name": skill_name.strip(),
                            "description": skill_desc.strip()
                        })
            
            if metadata.get("level3") and skills_list:
                all_skills.append({
                    "job_name": metadata.get("level3"),
                    "skills": skills_list,
                    "major": metadata.get("level2")
                })
        
        return {
            "success": True,
            "query": request.jobs,
            "skills": all_skills[:request.top_k]
        }
    
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
    技能分析对比接口
    根据输入文本和岗位名称数组，返回相似度最高的技能名称（异步多线程优化）
    """
    try:
        # 根据岗位名称数组获取对应岗位数据
        results = vector_service.get_by_metadata("level3", request.job_names)

        # 收集所有技能数据
        skills_data = []
        for r in results:
            metadata = r.get("metadata", {})
            level4_desc = metadata.get("level4_desc", "")

            if level4_desc:
                for item in level4_desc.split('; '):
                    if ':' in item:
                        skill_name, skill_desc = item.split(':', 1)
                        skills_data.append({
                            "skill_name": skill_name.strip(),
                            "skill_desc": skill_desc.strip(),
                            "job_name": metadata.get("level3"),
                            "major": metadata.get("level2")
                        })

        if not skills_data:
            return {"best_match_skill": None}

        # 提取所有技能名称和描述用于批量计算
        skill_names = [s["skill_name"] for s in skills_data]
        skill_descs = [s["skill_desc"] for s in skills_data]

        # 批量并行计算技能名称相似度
        name_sims = vector_service.compute_similarities_batch(
            request.text, skill_names
        )

        # 批量并行计算技能描述相似度
        desc_sims = vector_service.compute_similarities_batch(
            request.text, skill_descs
        )

        # 找出最大值作为最终匹配度
        best_skill = None
        best_similarity = -1

        for i, skill in enumerate(skills_data):
            combined_sim = max(name_sims[i], desc_sims[i])  # 取最大值
            if combined_sim > best_similarity:
                best_similarity = combined_sim
                best_skill = skill

        # 如果匹配度低于阈值（0.6，即60%），返回空值
        if best_similarity < 0.6:
            return {
                "best_match_skill": None
            }

        if best_skill:
            return {
                "best_match_skill": best_skill["skill_name"]
            }
        else:
            return {
                "best_match_skill": None
            }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"技能分析失败: {str(e)}")