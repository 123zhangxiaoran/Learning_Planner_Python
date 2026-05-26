"""推荐算法工程师数据"""
data = {
    '计算机与信息技术': {
        '人工智能': {
            '推荐算法工程师': {
                'description': '开发个性化推荐系统，提升用户体验和商业转化率。',
                'skills': {
                    'Python': {
                        'desc': '推荐系统开发语言',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础与科学计算', '数据类型与控制流', 'NumPy矩阵运算', 'Pandas数据处理', 'Scipy稀疏矩阵', 'Scikit-learn预处理'],
                            ['机器学习与深度学习', 'LightGBM/XGBoost', 'PyTorch Embedding', 'TensorFlow推荐模块', 'TF-Ranking', 'Surprise协同过滤'],
                            ['大数据与推荐框架', 'PySpark SQL', 'Spark MLlib', '推荐框架(RecBole/DeepRec)', 'Gensim/Item2Vec', '实时数据处理(Flink)'],
                            ['工程化与工具', 'Linux命令/shell脚本', 'Git版本控制', 'Redis缓存/特征存储', 'FAISS向量检索', 'Docker容器化', '多进程/异步编程']
                        ]
                    },
                    'Embedding': {
                        'desc': '用户和物品的向量表示学习',
                        'difficulty': 2,
                        'dimensions': [
                            ['矩阵分解与基础嵌入', 'One-hot与稀疏问题', 'SVD/ALS矩阵分解', 'SVD++', 'Word2Vec/Item2Vec', 'Skip-gram/负采样'],
                            ['图嵌入', 'DeepWalk/随机游走', 'Node2Vec', 'LINE/SDNE', 'GraphSAGE', 'GCN/GAT图卷积'],
                            ['序列与知识嵌入', '序列Embedding', '多兴趣胶囊网络', '对比学习(SimCLR/SimCSE)', 'Sentence-BERT', '知识图谱嵌入(TransE/RotatE)'],
                            ['多模态与检索', '多模态Embedding(CLIP)', '向量检索(FAISS/Annoy)', 'HNSW/IVF/PQ量化', '在线向量更新', '跨域Embedding迁移']
                        ]
                    },
                    'Redis': {
                        'desc': '缓存推荐结果和用户特征',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础数据结构', 'String/Hash/List/Set/Zset', '用户特征存储(Hash)', '排序推荐(Zset)', '序列化JSON', 'TTL过期策略'],
                            ['持久化与高可用', 'RDB/AOF持久化', '主从复制', 'Sentinel哨兵', 'Cluster集群分片', '连接池/Pipeline'],
                            ['缓存与性能', 'Cache Aside/Write Behind', 'LRU/LFU淘汰策略', '热key/大key问题', '分布式锁(RedLock)', '布隆过滤器去重'],
                            ['高级功能与推荐应用', 'RedisSearch/RedisJSON', 'RedisGraph', '实时特征存储', '排行榜/实时计数(HyperLogLog)', 'AB实验分组缓存']
                        ]
                    },
                    'Spark': {
                        'desc': '大规模数据处理框架',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心概念与API', 'RDD/DataFrame/Dataset', 'Transformation/Action', 'Spark SQL', 'MLlib/ML Pipeline', 'PySpark'],
                            ['推荐算法与优化', '协同过滤ALS', '特征工程Spark处理', 'Hyperparameter tuning', 'MLflow集成', '模型导出'],
                            ['流处理与图计算', 'Structured Streaming', 'Kafka集成', 'GraphX图计算', '窗口函数'],
                            ['部署与调优', 'DAG/Stage/Shuffle', 'Cache持久化策略', '广播变量/累加器', '数据倾斜解决', 'Delta Lake/Iceberg']
                        ]
                    },
                    '冷启动': {
                        'desc': '新用户和新物品的推荐策略',
                        'difficulty': 2,
                        'dimensions': [
                            ['问题与策略', '用户/物品/系统冷启动', '热门/趋势推荐', '人口统计学', '社交网络推荐', 'EE问题'],
                            ['Bandit算法', 'UCB', 'Thompson Sampling', 'Epsilon-Greedy', 'LinUCB', 'Contextual Bandit'],
                            ['内容与知识', '内容特征(Side Info)', '物品Category/Tag', '知识图谱辅助', '跨域推荐', '迁移/元学习'],
                            ['新用户引导', '注册信息/问卷', '主动学习', '兴趣点推荐(POI)', '新用户Onboarding', '小样本/零样本']
                        ]
                    },
                    '协同过滤': {
                        'desc': '基于用户或物品的相似度推荐',
                        'difficulty': 2,
                        'dimensions': [
                            ['基于邻域的方法', 'User-based CF', 'Item-based CF', '相似度计算(余弦/皮尔逊)', 'Top-K近邻', '隐式/显式反馈'],
                            ['矩阵分解方法', 'SVD', 'ALS', 'SVD++', 'NMF', 'FunkSVD', '偏置项', '正则化'],
                            ['评估与优化', '评分预测/RMSE', 'Top-N推荐(NDCG)', '覆盖率/多样性', '新颖性', '稀疏性处理', '增量更新'],
                            ['工程实现', 'Spark ALS', 'Surprise库', '离线计算与在线服务', '实时协同过滤']
                        ]
                    },
                    '召回算法': {
                        'desc': '快速筛选候选集的算法',
                        'difficulty': 2,
                        'dimensions': [
                            ['多路召回与协同', '热门/热榜召回', 'U2I/I2I/U2U', 'Item-CF/User-CF', '矩阵分解召回', 'DeepMatch双塔'],
                            ['向量与图召回', 'Embedding检索(FAISS)', 'HNSW/IVF/PQ', '图神经网络召回(GraphSAGE/GAT)', '向量库(Milvus/Qdrant)'],
                            ['序列与多兴趣', 'GRU4Rec/LSTM4Rec', 'BERT4Rec', 'MIND多兴趣', 'ComiRec', '序列建模'],
                            ['异构与融合', '跨域召回', '知识图谱召回(TransE)', '标签/类目/品牌召回', '实时/离线召回', '召回评估(Precision@K/Recall@K)']
                        ]
                    },
                    '特征工程': {
                        'desc': '构建用户画像和物品特征',
                        'difficulty': 2,
                        'dimensions': [
                            ['用户与物品特征', '用户画像(人口属性)', '行为特征(统计/序列)', '物品内容特征', '标签/类目/品牌', '时间特征(衰减/周期)'],
                            ['编码与变换', 'One-hot/Label Encoding', 'Target Encoding', 'Category Embedding', 'Z-score/MinMax', '对数/分桶', '缺失值处理'],
                            ['特征交叉与选择', '特征交叉(FM/FFM)', 'DeepFM/Deep&Cross', '特征重要性(Tree/SHAP)', '过滤法/包装法/嵌入法', '特征监控'],
                            ['实时与平台', '在线特征计算(滑动窗口)', '离线特征(Spark)', '特征存储(Feature Store)', '特征一致性(线上线下)', '特征回填']
                        ]
                    },
                    '矩阵分解': {
                        'desc': 'SVD、ALS等降维技术',
                        'difficulty': 2,
                        'dimensions': [
                            ['经典方法', 'SVD奇异值分解', 'Truncated SVD', 'ALS交替最小二乘', 'SVD++', 'NMF非负矩阵分解'],
                            ['扩展与实现', '隐式反馈建模', '置信度加权', '偏置项(用户/物品)', 'FunkSVD/SGD优化', 'PyTorch/Spark实现'],
                            ['进阶与评估', 'TimeSVD++时序', 'FM/FFM分解机', '负采样策略', '评估指标(RMSE/MAE)', 'Top-K推荐评估(NDCG)', '在线更新/增量']
                        ]
                    },
                    'A/B测试': {
                        'desc': '评估推荐效果',
                        'difficulty': 3,
                        'dimensions': [
                            ['实验设计', '假设检验/原假设', 'P-value/置信区间', '统计功效/样本量', '随机分组/AA分流', '正交/分层实验'],
                            ['多臂老虎机', 'Epsilon-Greedy', 'Thompson Sampling', 'UCB', 'Contextual Bandit'],
                            ['指标与分析', 'CTR/CVR/GMV', '北极星/辅助指标', '新奇效应/辛普森悖论', '短期vs长期', '下钻/归因分析'],
                            ['平台与工具', 'AB实验平台/流量调度', '分桶/分层隔离', '实验引擎', '结果报告/显著性检验', 'AA检验']
                        ]
                    },
                    'DIN': {
                        'desc': '深度兴趣网络，建模用户动态兴趣',
                        'difficulty': 3,
                        'dimensions': [
                            ['DIN基础', '深度兴趣网络', '注意力激活单元', '用户行为序列', '候选商品', 'Dice激活函数', '加权求和'],
                            ['DIEN进化', '兴趣抽取层(GRU)', '兴趣进化层(AUGRU)', 'DIEN架构', '序列建模', '短期/长期兴趣'],
                            ['多兴趣与变体', 'MIND多兴趣', 'ComiRec', 'Capsule胶囊网络', 'DSIN会话兴趣', '多头注意力'],
                            ['工程实现', 'DeepCTR实现', 'PyTorch实现', '实时预测服务', '特征序列化']
                        ]
                    },
                    'Wide&Deep': {
                        'desc': 'Google的推荐模型架构',
                        'difficulty': 3,
                        'dimensions': [
                            ['模型基础', 'Wide侧记忆', 'Deep侧泛化', '联合训练', '交叉特征(AND)', 'Embedding层', 'ReLU/DNN'],
                            ['变体与扩展', 'DeepFM', 'DCN/Cross Network', 'xDeepFM(CIN)', 'AutoInt自注意力', 'FiBiNet'],
                            ['训练与部署', 'TensorFlow WideDeep', 'DeepCTR实现', '离线训练', '在线Serving', 'Wide/Deep平衡', 'Embedding维度']
                        ]
                    },
                    '实时推荐': {
                        'desc': '流式计算实现实时个性化',
                        'difficulty': 3,
                        'dimensions': [
                            ['流计算框架', 'Flink DataStream/SQL', 'Kafka消息队列', 'Spark Streaming', 'Structured Streaming', '流批一体(Lambda/Kappa)'],
                            ['实时特征与窗口', '滑动/滚动/会话窗口', 'Watermark乱序处理', 'Checkpoint/Exactly-Once', '实时特征计算(Redis存储)', 'Flink+Redis架构'],
                            ['在线学习与召回', 'FTRL在线学习', '增量训练', '实时召回', '在线模型推断(Triton/TF Serving)', '实时TopK计算'],
                            ['推荐服务链路', '实时排序', '特征服务', '推荐服务', 'A/B实时监控', '全链路推荐']
                        ]
                    },
                    '排序算法': {
                        'desc': '精排模型，预测用户点击率或转化率',
                        'difficulty': 3,
                        'dimensions': [
                            ['CTR/CVR预估基础', 'CTR/CVR预估', 'LogLoss/AUC', 'GBDT+LR', 'FM/FFM', 'Wide&Deep'],
                            ['深度CTR模型', 'DeepFM', 'DCN/DCNv2', 'xDeepFM', 'AutoInt', 'DIN/DIEN/DSIN'],
                            ['多任务与序列', 'ESMM全空间', 'MMoE/PLE', 'Share Bottom', '序列建模(GRU/Transformer)', 'BST'],
                            ['学习排序与优化', 'Pointwise/Pairwise/Listwise', 'BPR', 'LambdaMART', '多目标排序', '模型蒸馏', 'NDCG优化']
                        ]
                    },
                    '深度学习推荐': {
                        'desc': '使用神经网络构建推荐模型',
                        'difficulty': 3,
                        'dimensions': [
                            ['基础网络与Embedding', 'DNN/MLP', 'Embedding技术(ID/Multi-hot)', '特征交叉(PNN/Deep Crossing)', '残差连接/BatchNorm'],
                            ['神经协同与序列', 'NCF/NeuMF', 'GMF', 'SASRec/BERT4Rec', 'BST Transformer', 'GRU4Rec'],
                            ['图神经网络推荐', 'NGCF', 'LightGCN', 'GraphSAGE', 'GAT', 'GNN序列推荐'],
                            ['知识图谱与多模态', 'RippleNet', 'KGAT', 'MKR', 'MMGCN', '对比学习推荐(SGL/NCL)'],
                            ['高级学习范式', '强化学习(DRN)', '迁移/跨域推荐', '元学习(MeLU/MAML)', '联邦学习隐私', '在线学习/FTRL', '模型压缩/蒸馏']
                        ]
                    }
                }
            }
        }
    }
}