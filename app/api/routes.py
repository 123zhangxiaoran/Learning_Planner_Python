"""API路由"""
import asyncio
import json
import random
from typing import Dict, Any, Optional, List, Union
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

# 导入服务
from app.services.vector_service import VectorService
from app.services.ai_service import AIService
from app.services.question_service import QuestionService
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
    collection_name: Optional[str] = None  # 向量集合名称，默认使用配置值

class SkillSearchRequest(BaseModel):
    """技能查询请求"""
    jobs: List[str]  # 岗位名称列表（支持多个岗位）
    top_k: int = 5
    min_score: float = 0.3  # 最低相似度阈值
    isNews: Optional[bool] = True  # 是否新请求
    jobToken: Optional[int] = None  # 岗位令牌
    collection_name: Optional[str] = None  # 向量集合名称

class SkillAnalyticalRequest(BaseModel):
    """技能分析对比请求 - 用于大模型提示词生成"""
    userinput: str  # 用户输入的文本（如"你好"、技能描述、问题等）
    job_name: str  # 目标岗位
    skill_name: str  # 选中的技能
    dimensions: List[List[str]]  # 知识点维度
    user_id: int

class AddDocumentRequest(BaseModel):
    """添加文档请求"""
    texts: List[str]
    metadatas: Optional[List[Dict[str, Any]]] = None
    collection_name: Optional[str] = None  # 向量集合名称

class FetchSkillKnowRequest(BaseModel):
    """获取技能知识点请求"""
    job_names: str  # 岗位名称
    selected_skill: str  # 选中的技能名称
    collection_name: Optional[str] = None  # 向量集合名称

class LearningPathRequest(BaseModel):
    """学习路径生成请求"""
    skill_name: str
    job_name: str
    dimensions: List[List[str]]
    user_id: int
    userinput: str

class FetchAllSkillRequest(BaseModel):
    """获取所有技能请求"""
    skills: List[List[str]]  # [["岗位名", "技能名"], ...]

class AnalysisAIRequest(BaseModel):
    """AI分析请求"""
    questionText: str  # 题目文本
    userInput: str  # 用户输入
    correctAnswer: str  # 正确答案

class GenerateQuestionsRequest(BaseModel):
    """生成题目请求 - AnalyticalSkillDTO"""
    skill_name: str  # 技能名称（如 HTML）
    job_name: str  # 岗位名称（如 前端开发工程师）
    user_id: int
    dimensions: List[List[str]]  # 知识点维度列表
    userinput: Optional[str] = None  # 用户输入文本
    difficulty: Optional[List[List[Any]]] = None  # 难度列表 [["维度名", 难度值], ...]

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
            top_k=50,  # 多取一些，后面重新排序
            collection_name=request.collection_name
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

        # 过滤掉重复的岗位（按岗位名称去重，保留相似度最高的）
        seen = set()
        unique_jobs = []
        for j in jobs:
            if j["job_name"] not in seen:
                seen.add(j["job_name"])
                unique_jobs.append(j)
        jobs = unique_jobs

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
        results = vector_service.get_by_metadata("level3", request.jobs, collection_name=request.collection_name)
        
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
            metadatas=request.metadatas,
            collection_name=request.collection_name
        )
        return {"success": True, "message": f"成功添加 {len(ids)} 个文档", "ids": ids}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"添加文档失败: {str(e)}")


@router.get("/api/collection/info")
async def get_collection_info(collection_name: str = None):
    """获取向量库信息"""
    try:
        info = vector_service.get_collection_info(collection_name=collection_name)
        return info
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/api/collection")
async def delete_collection(collection_name: str = None):
    """清空向量库"""
    try:
        vector_service.delete_collection(collection_name=collection_name)
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
    - userinput: 用户输入的原始文本
    - job_name: 目标岗位列表
    - skill_name: 用户选中的技能
    
    同时返回该岗位下的所有技能列表，供大模型分析和生成学习计划
    """
    try:
        # 构建提示词模板所需的数据结构
        prompt_data = {
            "user_id": request.user_id,
            "userinput": request.userinput,                    # 用户输入文本
            "job_name": request.job_name,        # 目标岗位
            "skill_name": request.skill_name,  # 选中的技能
            "dimensions":request.dimensions
        }

        # 使用线程池执行，不阻塞其他用户请求
        ai_response = await asyncio.to_thread(
            ai_service.generate_learning_plan, prompt_data
        )
        return {
            "success": True,
            "data": ai_response,
            "message": "大模型数据推理成功"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"学习资料生成失败: {str(e)}")


@router.post("/api/skill/learningPath")
async def learning_path(request: LearningPathRequest):
    """
    学习路径生成接口
    根据技能、岗位、知识点维度生成个性化学习路径
    """
    try:
        # 构建提示词数据
        prompt_data = {
            "skill_name": request.skill_name,
            "job_name": request.job_name,
            "dimensions": request.dimensions,
            "user_id": request.user_id,
            "userinput": request.userinput
        }

        # 使用线程池执行，不阻塞其他用户请求
        ai_response = await asyncio.to_thread(
            ai_service.generate_learning_plan, prompt_data
        )
        return {
            "success": True,
            "data": ai_response,
            "message": "学习路径生成成功"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"学习路径生成失败: {str(e)}")


@router.post("/api/skill/fetchAllSkill")
async def fetch_all_skill(request: FetchAllSkillRequest):
    """
    获取所有技能接口
    根据岗位+技能列表，并行查询每个技能的知识点维度
    请求体：{"skills": [["前端开发工程师", "vue"], ["前端开发工程师", "js"]]}
    """
    try:
        import concurrent.futures

        def process_single_skill(job_name: str, skill_name: str):
            """处理单个岗位+技能，获取该技能的知识点（同 fetchSkill 逻辑）"""
            results = vector_service.get_by_metadata("level3", [job_name])

            for r in results:
                metadata = r.get("metadata", {})
                level4_desc = metadata.get("level4_desc", "")

                if level4_desc:
                    for item in level4_desc.split('; '):
                        if ':' in item:
                            sname, sdesc = item.split(':', 1)
                            sname = sname.strip()

                            if sname == skill_name:
                                # 从 metadata 中获取该技能的知识点
                                dim_key = f"skill_dims_{sname}"
                                dimensions_str = metadata.get(dim_key, "")
                                try:
                                    dimensions_list = json.loads(dimensions_str) if dimensions_str else []
                                except json.JSONDecodeError:
                                    dimensions_list = [d.strip() for d in dimensions_str.split('; ')] if dimensions_str else []

                                return {
                                    "success": True,
                                    "skill_name": sname,
                                    "dimensions": dimensions_list,
                                    "job_name": metadata.get("level3"),
                                    "major": metadata.get("level2")
                                }

            return {"success": False, "skill_name": skill_name, "dimensions": [], "job_name": job_name}

        # 使用线程池并行执行
        with concurrent.futures.ThreadPoolExecutor(max_workers=len(request.skills) or 1) as executor:
            futures = {
                executor.submit(process_single_skill, pair[0], pair[1]): pair
                for pair in request.skills if len(pair) >= 2
            }
            results = []
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        results.append(result)
                except Exception:
                    pass

        return {
            "success": True,
            "data": results,
            "message": f"成功获取 {len(results)} 个技能的知识点"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取所有技能失败: {str(e)}")
    

@router.post("/api/skill/analysisAI")
async def analysis_ai(request: AnalysisAIRequest):
    """
    AI分析接口
    调用大模型对用户的回答进行评分（0-100分）
    根据题目(questionText)、用户回答(userInput)、正确答案(correctAnswer)
    """
    try:
        # 取出数据
        question_text = request.questionText
        user_input = request.userInput
        correct_answer = request.correctAnswer

        # 构建评分提示词（分析题评分）
        scoring_prompt = f"""你是一个专业的分析题评分助手。请根据题目、参考答案和用户的回答，对用户的分析作答进行评分。

评分规则：
- 评分范围：0-100分
- 分析题没有绝对的标准答案，参考答案仅供参考
- 根据用户回答的完整度、准确性、逻辑性、深度进行综合评分
- 回答全面、逻辑清晰、分析深入 → 高分（80-100）
- 回答基本正确但不够全面 → 中等分（50-79）
- 回答有部分正确内容但存在明显错误或偏差 → 低分（10-49）
- 回答完全错误、答非所问或空白 → 0分

请严格按照以下JSON格式返回，不要包含其他内容：
{{"score": 分数, "reason": "评分理由（只输出理由本身，不要引用用户的回答内容，不要包含'用户回答为'等描述）"}}

题目：{question_text}
参考答案：{correct_answer}
用户回答：{user_input}"""

        # 调用大模型评分（使用线程池避免阻塞）
        from langchain_core.prompts import PromptTemplate

        llm = ai_service.llm_generator
        response = await asyncio.to_thread(
            lambda: llm.invoke(scoring_prompt)
        )

        # 解析大模型返回的JSON
        content = response.content if hasattr(response, 'content') else str(response)
        try:
            # 尝试提取JSON部分
            import re
            json_match = re.search(r'\{[^}]+\}', content)
            if json_match:
                result = json.loads(json_match.group())
            else:
                result = json.loads(content)
        except (json.JSONDecodeError, AttributeError):
            # 解析失败时返回原始内容
            result = {"score": 0, "reason": "评分解析失败"}

        score = result.get("score", 0)
        reason = result.get("reason", "")

        return {
            "success": True,
            "data": {
                "score": score,
                "reason": reason,
            },
            "message": "评分成功"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI分析失败: {str(e)}")


@router.post("/api/skill/fetchSkill")
async def fetch_skill_knowledge(request: FetchSkillKnowRequest):
    """
    获取技能知识点接口
    根据岗位名称列表和选中的技能，返回该技能的知识点维度
    """
    try:
        # 使用 get_by_metadata 根据岗位名称精确查询
        results = vector_service.get_by_metadata("level3", [request.job_names], collection_name=request.collection_name)

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
                            try:
                                dimensions_list = json.loads(dimensions_str) if dimensions_str else []
                            except json.JSONDecodeError:
                                # 兼容旧格式：; 分隔的字符串
                                dimensions_list = [d.strip() for d in dimensions_str.split('; ')] if dimensions_str else []

                            return {
                                "success": True,
                                "skill_name": skill_name,
                                "dimensions": dimensions_list,
                                "job_name": metadata.get("level3")
                            }

        return {
            "success": False,
            "message": f"未找到技能 '{request.selected_skill}' 对应的知识点"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"获取技能知识点失败: {str(e)}")


@router.post("/api/skill/generateQuestions")
async def generate_questions(request: GenerateQuestionsRequest):
    """
    生成题目接口 - 基于知识点维度生成练习题目

    参数：
    - skill_name: 技能名称（如 HTML）
    - job_name: 岗位名称（如 前端开发工程师）
    - user_id: 用户ID
    - dimensions: 知识点维度列表
    """
    try:
        # 创建 QuestionService 实例，传入 vector_service
        llm = ai_service.llm_generator
        question_service = QuestionService(
            llm_generator=llm,
            job_name=request.job_name,
            skill_name=request.skill_name,
            vector_service=vector_service
        )

        # ========== 知识点采样逻辑（从 dimensions 采样至少10个） ==========
        all_keywords = []
        dim_count = len(request.dimensions)

        if dim_count >= 10:
            for dim_group in request.dimensions:
                if dim_group:
                    all_keywords.append(random.choice(dim_group))
        else:
            pool = [kw for dim_group in request.dimensions for kw in dim_group]
            all_keywords = [random.choice(dg) for dg in request.dimensions if dg]
            remaining = [kw for kw in pool if kw not in all_keywords]
            need = 10 - len(all_keywords)
            if need > 0 and remaining:
                extra = random.sample(remaining, min(need, len(remaining)))
                all_keywords.extend(extra)

        while len(all_keywords) < 10:
            candidates = [kw for kw in all_keywords if kw != all_keywords[-1]]
            all_keywords.append(random.choice(candidates))

        # 构建 keyword -> dim_first 的映射
        keyword_to_dim_first = {}
        for keyword in all_keywords:
            for dim_group in request.dimensions:
                if keyword in dim_group:
                    keyword_to_dim_first[keyword] = dim_group[0] if dim_group else keyword
                    break

        # 构建 keyword -> difficulty 的映射
        keyword_to_difficulty = {}
        if request.difficulty:
            for diff_item in request.difficulty:
                if len(diff_item) >= 2:
                    dim_name = str(diff_item[0])
                    try:
                        diff_value = int(diff_item[1])
                    except (ValueError, TypeError):
                        diff_value = 0
                    keyword_to_difficulty[dim_name] = diff_value

        # 根据知识点分数决定题型组合
        def get_question_types_by_score(score):
            """根据分数返回题型列表"""
            if score <= 10:
                return ["judge"] * 7 + ["choice"] * 3
            elif score <= 30:
                return ["judge"] * 3 + ["choice"] * 7
            elif score <= 50:
                return ["judge"] * 3 + ["choice"] * 5 + ["fill"] * 2
            elif score <= 75:
                return ["judge"] * 2 + ["choice"] * 3 + ["fill"] * 3
            elif score <= 90:
                return ["choice"] * 4 + ["fill"] * 6
            else:  # >90 and <=100
                return ["analysis"] * 10

        # 为每个知识点分配题型
        question_types = []
        for keyword in all_keywords:
            # 找到该 keyword 对应的 difficulty 分数
            score = 0  # 默认分数为0（最低难度）
            for dim_group in request.dimensions:
                if keyword in dim_group:
                    dim_first = dim_group[0]
                    score = keyword_to_difficulty.get(dim_first, 0)
                    break
            type_list = get_question_types_by_score(score)
            question_types.append(random.choice(type_list))

        # ========== 并行处理每个知识点 ==========

        def _generate_all():
            """在子线程中并行执行所有知识点生成"""
            import concurrent.futures

            def generate_one(keyword, dim_first, q_type, user_id, idx, difficulty=None):
                """生成单个知识点的题目"""
                return question_service.generate_single_question(
                    keyword=keyword,
                    dim_first=dim_first,
                    q_type=q_type,
                    user_id=user_id,
                    difficulty=difficulty,
                    save_logs=(idx == 0)
                )

            # 使用线程池并行执行
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                futures = []
                for i, keyword in enumerate(all_keywords):
                    dim_first = keyword_to_dim_first.get(keyword, keyword)
                    # 从 keyword 所在维度组获取第一个元素作为 difficulty 的 key
                    diff_key = None
                    for dim_group in request.dimensions:
                        if keyword in dim_group:
                            diff_key = dim_group[0] if dim_group else keyword
                            break
                    difficulty = keyword_to_difficulty.get(diff_key)
                    future = executor.submit(
                        generate_one,
                        keyword=keyword,
                        dim_first=dim_first,
                        q_type=question_types[i],
                        user_id=request.user_id,
                        idx=i,
                        difficulty=difficulty
                    )
                    futures.append(future)

                # 等待所有任务完成
                results = []
                for future in concurrent.futures.as_completed(futures):
                    try:
                        result = future.result()
                        if result:
                            results.append(result)
                    except Exception:
                        pass
                return results

        questions = await asyncio.to_thread(_generate_all)

        # ========== 立即返回题目（后台异步写入向量库）==========
        # 先创建返回数据
        result = {
            "success": True,
            "data": questions,
            "message": f"成功生成 {len(questions)} 道题目"
        }

        # 后台异步写入向量库（不阻塞返回）
        if questions and vector_service:
            async def background_save():
                try:
                    # 收集所有需要嵌入的文本
                    texts_to_embed = list(set(all_keywords))
                    stems = [q.get('stem', '') for q in questions if q.get('stem')]
                    texts_to_embed.extend(stems)
                    texts_to_embed = list(set(texts_to_embed))

                    # 批量异步计算嵌入向量
                    embeddings_list = await vector_service.compute_embeddings_batch_async(texts_to_embed)
                    precomputed_embeddings = {text: emb for text, emb in zip(texts_to_embed, embeddings_list)}

                    # 存储题目
                    qs = QuestionService(
                        llm_generator=llm,
                        job_name=request.job_name,
                        skill_name=request.skill_name,
                        vector_service=vector_service,
                        precomputed_embeddings=precomputed_embeddings
                    )
                    qs.generate_questions(
                        keywords=all_keywords,
                        questions=questions,
                        user_id=request.user_id
                    )
                except Exception:
                    pass

            # 创建后台任务，立即返回
            asyncio.create_task(background_save())

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"题目生成失败: {str(e)}")