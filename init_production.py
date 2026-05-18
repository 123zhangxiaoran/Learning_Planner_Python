import requests
import importlib
import pkgutil
import os
import json

# 导入 data 目录下所有数据模块
data_dir = os.path.join(os.path.dirname(__file__), 'data')
data_modules = []

for importer, modname, ispkg in pkgutil.iter_modules([data_dir]):
    if modname != '__init__' and not modname.startswith('_'):
        mod = importlib.import_module(f'data.{modname}')
        if hasattr(mod, 'data'):
            data_modules.append(mod.data)

if not data_modules:
    print("未在 data/ 目录下找到任何数据模块")
    exit(1)

COLLECTION_NAME = "knowledge_base_prod"

# 先查看向量库状态
try:
    info = requests.get(f'http://localhost:8000/api/collection/info?collection_name={COLLECTION_NAME}')
    if info.status_code == 200:
        print(f"当前向量库: {info.json().get('name', 'unknown')}")
except:
    pass

texts = []
metadatas = []

# 合并所有数据模块
for data in data_modules:
    for level1, majors in data.items():
        for major, jobs in majors.items():
            for job, info in jobs.items():
                skills_list = []
                skills_with_desc = []
                skills_with_difficulty = []
                skills_dimensions = {}
                for skill_name, skill_info in info['skills'].items():
                    skills_list.append(skill_name)
                    skills_with_desc.append(f"{skill_name}:{skill_info['desc']}")
                    skills_with_difficulty.append(f"{skill_name}({skill_info['difficulty']})")
                    if 'dimensions' in skill_info:
                        skills_dimensions[f"skill_dims_{skill_name}"] = json.dumps(skill_info['dimensions'], ensure_ascii=False)

                text = f"专业：{level1} | 方向：{major} | 岗位：{job} | 描述：{info['description']} | 技能：{', '.join(skills_list)}"
                texts.append(text)
                metadatas.append({
                    'level1': level1,
                    'level2': major,
                    'level3': job,
                    'level3_desc': info['description'],
                    'level4': ', '.join(skills_list),
                    'level4_desc': '; '.join(skills_with_desc),
                    'skills_difficulty': '; '.join(skills_with_difficulty),
                    **skills_dimensions
                })

# 调用API添加文档
try:
    response = requests.post('http://localhost:8000/api/documents', json={
        'texts': texts,
        'metadatas': metadatas,
        'collection_name': COLLECTION_NAME
    })
    if response.status_code == 200:
        print(f"成功添加 {len(texts)} 条文档")
    else:
        print(f"添加失败: {response.text}")
except Exception as e:
    print(f"添加文档失败: {e}")

# 查看向量库状态
info = requests.get(f'http://localhost:8000/api/collection/info?collection_name={COLLECTION_NAME}')
print(f"添加文档数量: {len(texts)}")
if info.status_code == 200:
    print(f"向量库文档总数: {info.json().get('count', 'unknown')}")