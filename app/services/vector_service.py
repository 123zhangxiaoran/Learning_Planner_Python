"""向量数据库服务 - Chroma"""
import os
from typing import List, Dict, Any, Optional
import chromadb
from chromadb.config import Settings
from langchain_ollama import OllamaEmbeddings
from langchain_openai import OpenAIEmbeddings

class VectorService:
    """向量数据库服务"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.vector_config = config.get("vector_db", {})
        self.embedding_config = config.get("embedding", {})
        
        # 初始化Chroma客户端
        persist_dir = self.vector_config.get("persist_directory", "./data/chroma_db")
        os.makedirs(persist_dir, exist_ok=True)
        
        self.client = chromadb.PersistentClient(
            path=persist_dir,
            settings=Settings(anonymized_telemetry=False)
        )
        
        # 初始化嵌入模型
        self._init_embeddings()
        
        # 缓存所有集合
        self.collections = {}
        
        # 获取或创建默认collection
        self.default_collection_name = self.vector_config.get("collection_name", "knowledge_base")
        self.collection = self._get_or_create_collection(self.default_collection_name)
    
    def _get_or_create_collection(self, name: str = None) -> chromadb.Collection:
        """获取或创建指定名称的集合"""
        name = name or self.default_collection_name
        if name not in self.collections:
            self.collections[name] = self.client.get_or_create_collection(
                name=name,
                metadata={"description": f"知识库向量存储 - {name}"}
            )
        return self.collections[name]
    
    def _init_embeddings(self):
        """初始化嵌入模型"""
        provider = self.embedding_config.get("provider", "ollama")
        
        if provider == "ollama":
            model = self.embedding_config.get("model", "qwen3-embedding:8b-fp16")
            self.embeddings = OllamaEmbeddings(model=model)
        elif provider == "openai":
            self.embeddings = OpenAIEmbeddings(
                model="text-embedding-3-small"
            )
        else:
            raise ValueError(f"不支持的嵌入provider: {provider}")
    
    def add_documents(self, texts: List[str], metadatas: Optional[List[Dict]] = None, ids: Optional[List[str]] = None, collection_name: str = None) -> List[str]:
        """添加文档到向量库"""
        if ids is None:
            ids = [str(i) for i in range(len(texts))]
        
        collection = self._get_or_create_collection(collection_name)
        
        # 生成嵌入向量
        embeddings = self.embeddings.embed_documents(texts)
        
        # 添加到Chroma
        collection.add(
            documents=texts,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids
        )
        
        return ids
    
    def similarity_search(self, query: str, top_k: int = 5, collection_name: str = None) -> List[Dict[str, Any]]:
        """相似度搜索"""
        collection = self._get_or_create_collection(collection_name)
        
        # 生成查询向量
        query_embedding = self.embeddings.embed_query(query)
        
        # 执行搜索
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        
        # 格式化返回结果
        formatted_results = []
        if results["documents"] and results["documents"][0]:
            for i, doc in enumerate(results["documents"][0]):
                formatted_results.append({
                    "content": doc,
                    "distance": results["distances"][0][i] if "distances" in results else None,
                    "metadata": results["metadatas"][0][i] if "metadatas" in results and results["metadatas"] else None,
                    "id": results["ids"][0][i] if "ids" in results else None
                })
        
        return formatted_results
    
    def delete_collection(self, collection_name: str = None):
        """删除collection"""
        name = collection_name or self.default_collection_name
        self.client.delete_collection(name)
        # 从缓存中移除
        self.collections.pop(name, None)
        # 重新创建collection
        self._get_or_create_collection(name)
    
    def get_collection_info(self, collection_name: str = None) -> Dict[str, Any]:
        """获取collection信息"""
        collection = self._get_or_create_collection(collection_name)
        return {
            "name": collection.name,
            "count": collection.count(),
            "metadata": collection.metadata
        }
    
    def get_by_metadata(self, field: str, values: List[str], collection_name: str = None) -> List[Dict[str, Any]]:
        """根据metadata字段精确匹配查询（单字段）"""
        collection = self._get_or_create_collection(collection_name)
        
        if len(values) == 1:
            # 单个值直接查询
            results = collection.get(
                where={field: values[0]}
            )
        else:
            # 多个值用 $or 查询
            results = collection.get(
                where={"$or": [{field: v} for v in values]}
            )
        
        return self._format_results(results)

    def get_by_metadata_multi(self, filters: Dict[str, Any], collection_name: str = None) -> List[Dict[str, Any]]:
        """根据多个metadata字段精确匹配查询（$and）"""
        collection = self._get_or_create_collection(collection_name)
        where_clause = {"$and": [{k: v} for k, v in filters.items()]}
        results = collection.get(where=where_clause)
        return self._format_results(results)

    @staticmethod
    def _format_results(results) -> List[Dict[str, Any]]:
        """统一格式化查询结果"""
        formatted_results = []
        if results["documents"]:
            for i, doc in enumerate(results["documents"]):
                formatted_results.append({
                    "content": doc,
                    "metadata": results["metadatas"][i] if results["metadatas"] else None,
                    "id": results["ids"][i] if results["ids"] else None
                })
        return formatted_results

    def compute_similarity(self, query: str, text: str) -> float:
        """计算两个文本的相似度（返回0-1之间的值）"""
        if not query or not text:
            return 0.0

        # 生成两个文本的嵌入向量
        query_embedding = self.embeddings.embed_query(query)
        text_embedding = self.embeddings.embed_query(text)

        # 计算余弦相似度
        import numpy as np
        query_vec = np.array(query_embedding)
        text_vec = np.array(text_embedding)

        # 余弦相似度公式
        dot_product = np.dot(query_vec, text_vec)
        norm_query = np.linalg.norm(query_vec)
        norm_text = np.linalg.norm(text_vec)

        if norm_query == 0 or norm_text == 0:
            return 0.0

        similarity = dot_product / (norm_query * norm_text)
        return float(max(0, min(1, similarity)))

    def compute_similarities_batch(self, query: str, texts: List[str]) -> List[float]:
        """批量计算多个文本与查询的相似度（并行优化）"""
        import numpy as np
        from concurrent.futures import ThreadPoolExecutor, as_completed
        import os
        from queue import Queue
        import threading

        if not query or not texts:
            return [0.0] * len(texts)

        # 一次性生成查询向量（避免重复计算）
        query_embedding = self.embeddings.embed_query(query)
        query_vec = np.array(query_embedding)
        norm_query = np.linalg.norm(query_vec)

        if norm_query == 0:
            return [0.0] * len(texts)

        # 创建任务队列和结果存储
        task_queue = Queue()
        results = [0.0] * len(texts)
        results_lock = threading.Lock()

        # 将任务放入队列 (index, text)
        for i, text in enumerate(texts):
            task_queue.put((i, text))

        def worker():
            """工作线程：从队列竞争获取任务并执行"""
            while True:
                try:
                    idx, text = task_queue.get(block=False)
                except:
                    # 队列为空，线程结束
                    break

                # 计算相似度
                if not text:
                    similarity = 0.0
                else:
                    text_embedding = self.embeddings.embed_query(text)
                    text_vec = np.array(text_embedding)
                    dot_product = np.dot(query_vec, text_vec)
                    norm_text = np.linalg.norm(text_vec)
                    if norm_text == 0:
                        similarity = 0.0
                    else:
                        similarity = dot_product / (norm_query * norm_text)
                        similarity = float(max(0, min(1, similarity)))

                # 写入结果（需要加锁保证线程安全）
                with results_lock:
                    results[idx] = similarity

                task_queue.task_done()

        # 使用线程池并行计算
        max_workers = min(8, os.cpu_count() or 4)
        threads = []
        for _ in range(max_workers):
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)

        # 等待所有线程完成
        for t in threads:
            t.join()

        return results