#!/usr/bin/env python3
"""
删除所有题库数据脚本（主库 + 所有用户子库）
用法: python scripts/clear_all_question_collections.py
"""
import sys
import os

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yaml
from app.services.vector_service import VectorService


def load_config():
    """加载配置文件"""
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_question_collections(vector_service, master_name, user_prefix):
    """获取所有题库集合名称"""
    all_collections = vector_service.client.list_collections()
    question_collections = []

    for coll in all_collections:
        name = coll.name if hasattr(coll, 'name') else str(coll)
        # 匹配主库或用户子库前缀
        if name == master_name or name.startswith(user_prefix):
            question_collections.append(name)

    return question_collections


def clear_collection(vector_service, collection_name):
    """清空指定集合"""
    try:
        # 获取集合信息
        info = vector_service.get_collection_info(collection_name)
        count = info.get("count", 0)

        if count > 0:
            # 删除并重新创建集合（清空数据）
            vector_service.delete_collection(collection_name)
            print(f"  ✓ 已清空: {collection_name} (原数据量: {count})")
        else:
            print(f"  - 跳过空库: {collection_name}")
        return True
    except Exception as e:
        print(f"  ✗ 失败: {collection_name}, 错误: {e}")
        return False


def main():
    config = load_config()
    vector_config = config.get("vector_db", {})
    question_collections = vector_config.get("question_collections", {})

    master_name = question_collections.get("master", "generated_questions_master")
    user_prefix = question_collections.get("user_prefix", "generated_questions_user")

    # 初始化向量服务
    vector_service = VectorService(config)

    print("正在查找所有题库...")
    collections = get_question_collections(vector_service, master_name, user_prefix)

    if not collections:
        print("未找到任何题库")
        return

    # 分类统计
    master_collections = [c for c in collections if c == master_name]
    user_collections = [c for c in collections if c.startswith(user_prefix)]

    print(f"找到 {len(collections)} 个题库:")
    print(f"  - 主库: {len(master_collections)} 个")
    print(f"  - 用户子库: {len(user_collections)} 个")
    print("\n开始清空...")

    success_count = 0
    for coll_name in collections:
        if clear_collection(vector_service, coll_name):
            success_count += 1

    print(f"\n完成: 成功清空 {success_count}/{len(collections)} 个题库")


if __name__ == "__main__":
    main()
