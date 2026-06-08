#!/usr/bin/env python3
"""
删除用户子库数据脚本
用法: python scripts/clear_user_collections.py [user_id]

如果不指定 user_id，则删除所有用户子库
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


def get_user_collections(vector_service, user_prefix):
    """获取所有用户子库名称"""
    all_collections = vector_service.client.list_collections()
    user_collections = []
    for coll in all_collections:
        name = coll.name if hasattr(coll, 'name') else str(coll)
        if name.startswith(user_prefix):
            user_collections.append(name)
    return user_collections


def clear_user_collection(vector_service, collection_name):
    """清空指定用户子库"""
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
    user_prefix = question_collections.get("user_prefix", "generated_questions_user")

    # 初始化向量服务
    vector_service = VectorService(config)

    # 解析命令行参数
    if len(sys.argv) > 1:
        # 指定了 user_id
        user_id = sys.argv[1]
        collection_name = f"{user_prefix}{user_id}"
        print(f"正在清空用户 {user_id} 的子库...")
        clear_user_collection(vector_service, collection_name)
    else:
        # 未指定 user_id，清空所有用户子库
        print("正在查找所有用户子库...")
        user_collections = get_user_collections(vector_service, user_prefix)

        if not user_collections:
            print("未找到任何用户子库")
            return

        print(f"找到 {len(user_collections)} 个用户子库，开始清空...")
        success_count = 0
        for coll_name in user_collections:
            if clear_user_collection(vector_service, coll_name):
                success_count += 1

        print(f"\n完成: 成功清空 {success_count}/{len(user_collections)} 个用户子库")


if __name__ == "__main__":
    main()
