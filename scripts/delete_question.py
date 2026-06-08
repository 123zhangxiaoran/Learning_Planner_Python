#!/usr/bin/env python3
"""
删除指定题目脚本
用法: python scripts/delete_question.py <collection_name> <question_id>

示例:
  python scripts/delete_question.py generated_questions_user1 q_1_batch_1780837122_层叠与继承
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


def delete_question(vector_service, collection_name, question_id):
    """删除指定题目"""
    try:
        collection = vector_service._get_or_create_collection(collection_name)

        # 先检查记录是否存在
        result = collection.get(ids=[question_id])
        if not result or not result["ids"]:
            print(f"✗ 未找到记录: ID={question_id}")
            return False

        # 删除记录
        collection.delete(ids=[question_id])
        print(f"✓ 已删除: ID={question_id}")
        print(f"  库名: {collection_name}")
        if result["metadatas"] and result["metadatas"][0]:
            meta = result["metadatas"][0]
            print(f"  岗位: {meta.get('job_name', 'N/A')}")
            print(f"  技能: {meta.get('skill_name', 'N/A')}")
            print(f"  题型: {meta.get('question_type', 'N/A')}")
        return True

    except Exception as e:
        print(f"✗ 删除失败: {e}")
        return False


def main():
    if len(sys.argv) < 3:
        print("用法: python scripts/delete_question.py <collection_name> <question_id>")
        print("\n示例:")
        print('  python scripts/delete_question.py generated_questions_user1 q_1_batch_1780837122_层叠与继承')
        print("\n查看所有库及ID:")
        print("  python scripts/view_question_collections.py")
        sys.exit(1)

    collection_name = sys.argv[1]
    question_id = sys.argv[2]

    config = load_config()
    vector_service = VectorService(config)

    delete_question(vector_service, collection_name, question_id)


if __name__ == "__main__":
    main()
