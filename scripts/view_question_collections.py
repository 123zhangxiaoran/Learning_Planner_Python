#!/usr/bin/env python3
"""
查看题库数据脚本
用法: python scripts/view_question_collections.py [选项]

选项:
  --master          只查看主库
  --user [user_id]  查看指定用户子库
  --sample N        每库显示N条样本（默认5条）
  --details         显示详细数据（完整JSON）
"""
import sys
import os
import json
import argparse

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yaml
from app.services.vector_service import VectorService


def load_config():
    """加载配置文件"""
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_collections(vector_service, master_name, user_prefix, filter_type="all"):
    """获取题库集合列表"""
    all_collections = vector_service.client.list_collections()
    collections = {"master": [], "user": []}
    
    for coll in all_collections:
        name = coll.name if hasattr(coll, 'name') else str(coll)
        if name == master_name:
            collections["master"].append(name)
        elif name.startswith(user_prefix):
            collections["user"].append(name)
    
    return collections


def show_collection_data(vector_service, collection_name, sample_size=5, show_details=False):
    """显示单个库的数据"""
    try:
        collection = vector_service._get_or_create_collection(collection_name)
        count = collection.count()
        
        print(f"\n{'='*60}")
        print(f"库名: {collection_name}")
        print(f"数据量: {count} 条")
        print(f"{'='*60}")
        
        if count == 0:
            print("(空库)")
            return
        
        # 获取样本数据
        results = collection.get(limit=sample_size)
        
        for i, (doc_id, doc, metadata) in enumerate(zip(results["ids"], results["documents"], results["metadatas"])):
            print(f"\n--- 样本 {i+1}/{min(count, sample_size)} (ID: {doc_id}) ---")
            
            if metadata:
                print(f"岗位: {metadata.get('job_name', 'N/A')}")
                print(f"技能: {metadata.get('skill_name', 'N/A')}")
                print(f"题型: {metadata.get('question_type', 'N/A')}")
                print(f"关键词: {metadata.get('keywords', 'N/A')}")
                print(f"题干: {metadata.get('stem', 'N/A')[:100]}...")
                
                # 解析原始JSON显示更多信息
                original_json = metadata.get('original_json', '{}')
                try:
                    question_data = json.loads(original_json)
                    if 'answer' in question_data:
                        print(f"答案: {question_data['answer']}")
                    if 'difficulty' in question_data:
                        print(f"难度: {question_data['difficulty']}")
                except:
                    pass
                
                if show_details:
                    print(f"\n完整数据:")
                    print(json.dumps(metadata, ensure_ascii=False, indent=2))
                    if doc:
                        print(f"\n文档内容:\n{doc[:500]}...")
        
        # 统计信息
        if count > sample_size:
            print(f"\n... 还有 {count - sample_size} 条数据未显示")
            
    except Exception as e:
        print(f"✗ 读取失败: {collection_name}, 错误: {e}")


def main():
    parser = argparse.ArgumentParser(description="查看题库数据")
    parser.add_argument("--master", action="store_true", help="只查看主库")
    parser.add_argument("--user", type=str, metavar="USER_ID", help="查看指定用户子库")
    parser.add_argument("--sample", type=int, default=5, help="每库显示样本数（默认5）")
    parser.add_argument("--details", action="store_true", help="显示详细数据")
    
    args = parser.parse_args()
    
    config = load_config()
    vector_config = config.get("vector_db", {})
    question_collections = vector_config.get("question_collections", {})
    
    master_name = question_collections.get("master", "generated_questions_master")
    user_prefix = question_collections.get("user_prefix", "generated_questions_user")
    
    vector_service = VectorService(config)
    
    # 确定要查看的库
    if args.master:
        print("\n【主库数据】")
        show_collection_data(vector_service, master_name, args.sample, args.details)
    elif args.user:
        collection_name = f"{user_prefix}{args.user}"
        print(f"\n【用户 {args.user} 的子库数据】")
        show_collection_data(vector_service, collection_name, args.sample, args.details)
    else:
        # 查看所有库
        collections = get_collections(vector_service, master_name, user_prefix)
        
        # 主库
        if collections["master"]:
            print("\n" + "="*60)
            print("【主库 (Master Collection)】")
            print("="*60)
            for name in collections["master"]:
                show_collection_data(vector_service, name, args.sample, args.details)
        
        # 子库
        if collections["user"]:
            print("\n" + "="*60)
            print(f"【用户子库 (共 {len(collections['user'])} 个)】")
            print("="*60)
            for name in sorted(collections["user"]):
                show_collection_data(vector_service, name, args.sample, args.details)
        
        if not collections["master"] and not collections["user"]:
            print("未找到任何题库数据")


if __name__ == "__main__":
    main()
