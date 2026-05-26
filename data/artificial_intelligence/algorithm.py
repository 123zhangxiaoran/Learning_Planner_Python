"""算法工程师数据"""
data = {
    '计算机与信息技术': {
        '人工智能': {
            '算法工程师': {
                'description': '研究和开发机器学习算法，解决实际的AI问题，优化模型性能。',
                'skills': {
                    'NumPy': {
                        'desc': '数值计算库，提供高效的多维数组操作',
                        'difficulty': 1,
                        'dimensions': [
                            ['数组创建与属性', 'ndarray', '数组创建(ones/zeros/arange)', '数据类型(int/float/bool)', '形状(shape/reshape)', '索引与切片'],
                            ['运算与广播', '向量化运算(加减乘除)', '矩阵乘法(@)', '广播机制(Broadcast)', '聚合函数(sum/mean/max)', '排序(sort/argsort)'],
                            ['线性代数', '矩阵分解(svd/eig)', '范数(linalg.norm)', '行列式/逆矩阵', '线性方程求解', '傅里叶变换(fft/ifft)'],
                            ['高级操作', '条件筛选(where/boolean_mask)', '数组拼接/分割(stack/split)', '视图与拷贝(view/copy)', '结构化数组', '内存布局(C/F contiguous)'],
                            ['性能与IO', '向量化避免循环', '随机数生成(randn/randint)', '文件IO(savetxt/loadtxt)', '与列表互转', '性能优化建议']
                        ]
                    },
                    'Pandas': {
                        'desc': '数据处理和分析库，用于数据清洗和预处理',
                        'difficulty': 1,
                        'dimensions': [
                            ['数据结构与读取', 'Series/DataFrame', 'read_csv/excel/json', 'head/tail/info/describe', '列/行选择(loc/iloc)', '布尔索引与条件筛选'],
                            ['数据清洗与预处理', '缺失值处理(isnull/fillna/dropna)', '数据替换(replace)', '类型转换(astype)', '去重(drop_duplicates)', '排序(sort_values)'],
                            ['数据合并与重塑', 'concat/merge/join', 'groupby分组聚合', '透视表(pivot_table)', 'melt/stack/unstack', '多级索引(MultiIndex)'],
                            ['字符串与时间', 'str.contains/replace/split', 'datetime/to_datetime', '日期范围(date_range)', '重采样(resample)', '窗口函数(rolling/expanding)'],
                            ['高级应用', 'map/apply/applymap', '采样(sample)', '分箱(cut/qcut)', '排名(rank)', '输出(to_csv/excel)']
                        ]
                    },
                    'Python': {
                        'desc': 'AI领域主流编程语言，拥有丰富的科学计算和机器学习库',
                        'difficulty': 1,
                        'dimensions': [
                            ['语言核心', '数据类型与结构', '控制流', '函数与lambda', '列表/字典推导式', '生成器与迭代器'],
                            ['高级特性', '装饰器与参数化', '上下文管理器(with)', '异常处理(try/except)', '深拷贝与浅拷贝', '魔术方法(__str__/__repr__)'],
                            ['科学计算与数据', 'numpy/scipy基础', 'pandas数据处理', 'matplotlib/seaborn可视化', 'Jupyter/IPython', 'scikit-learn基础'],
                            ['工程与并发', '正则表达式(re)', '日期时间(datetime)', '类型注解(typing)', 'asyncio/threading', '单元测试(pytest)'],
                            ['环境与规范', 'venv/conda环境管理', 'pip/conda包管理', 'PEP8代码规范', 'logging日志', 'configparser/yaml配置']
                        ]
                    },
                    'A/B测试': {
                        'desc': '设计实验验证算法效果',
                        'difficulty': 2,
                        'dimensions': [
                            ['实验设计', '对照组/实验组', '随机分组', '样本量计算(统计功效)', 'AA测试基准', '实验周期与观察期'],
                            ['显著性检验', 't检验/z检验/p值', '置信区间', '多重比较校正', '方差分析(ANOVA)', '卡方检验'],
                            ['分流与指标', 'hash分流/uid分流', '流量层与分层', '北极星指标与辅助指标', '指标构建与归因', '数据埋点与采集'],
                            ['效应与问题', '提升度(Lift)', '新奇效应/首因效应', '网络效应/溢出', '时间/周末/节假日效应', '用户交互效应'],
                            ['平台与工具', 'AB测试框架', 'Feature Flag/灰度发布', '多臂老虎机(MAB)', '在线实验与监控', '配置中心与报警'],
                            ['因果推断', '倾向得分匹配(PSM)', '双重差分(DID)', 'Uplift Modeling', '异质性因果效应(HTE)', '元分析(Meta Analysis)']
                        ]
                    },
                    'Keras': {
                        'desc': '高级神经网络API，简化深度学习模型构建',
                        'difficulty': 2,
                        'dimensions': [
                            ['模型构建', 'Sequential/Functional API', '层(Dense/Dropout/BN)', '激活函数(relu/sigmoid/softmax)', '损失函数与优化器', 'model.compile'],
                            ['训练与回调', 'model.fit(batch_size/epochs)', 'EarlyStopping/ModelCheckpoint', 'TensorBoard', 'ReduceLROnPlateau', 'history与可视化'],
                            ['数据处理', 'ImageDataGenerator增强', 'tf.data.Dataset管道', 'TFRecord格式', '数据增强(旋转/翻转/缩放)', '数据标准化'],
                            ['CNN与RNN', 'Conv2D/MaxPooling', 'LSTM/GRU/Bidirectional', 'Embedding层', '迁移学习(VGG/ResNet)', 'fine-tuning冻结层'],
                            ['高级定制', '自定义Layer/Loss', '自定义指标', '多输入多输出', '共享层', 'Keras Tuner超参搜索']
                        ]
                    },
                    'LightGBM': {
                        'desc': '微软高效梯度提升框架，训练速度快内存占用低',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与参数', 'Dataset/train/sklearn API', '目标函数(objective)', '评估指标(rmse/auc)', 'num_leaves/max_depth', 'learning_rate/n_estimators'],
                            ['采样与正则', 'bagging_fraction', 'colsample_bytree', 'reg_alpha/reg_lambda', 'min_child_samples', '早停(early_stopping)'],
                            ['核心算法', 'GOSS单边梯度采样', 'EFB互斥特征捆绑', '直方图算法', '分类特征支持(categorical_feature)', '缺失值处理'],
                            ['进阶与调优', '交叉验证(cv)', '特征重要性', 'DART下拉树', 'GPU训练(gpu_use_dp)', '与XGBoost对比与调参']
                        ]
                    },
                    'PyTorch': {
                        'desc': 'Facebook开源深度学习框架，动态图机制灵活易用',
                        'difficulty': 2,
                        'dimensions': [
                            ['张量与自动求导', 'Tensor创建与设备(CUDA)', '索引/变换/运算', 'requires_grad与backward', '计算图与梯度', 'zero_grad'],
                            ['网络与层', 'nn.Module定义', 'Linear/Conv2d/RNN', '激活函数与Dropout', 'BatchNorm/LayerNorm', '参数初始化'],
                            ['训练循环', 'DataLoader与Dataset', '损失函数(CrossEntropy/MSE)', '优化器(Adam/AdamW)', '学习率调度(Cosine/Step)', 'train/eval模式'],
                            ['高级功能', 'GPU训练与混合精度(AMP)', '梯度裁剪', 'DistributedDataParallel', '模型保存/加载(state_dict)', 'torch.compile优化'],
                            ['迁移与部署', '微调(Fine-tuning)', '预训练模型(torchvision)', 'HuggingFace集成', 'TorchScript/JIT', 'ONNX导出']
                        ]
                    },
                    'Scikit-learn': {
                        'desc': '传统机器学习算法库，包含分类、回归、聚类等算法',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与预处理', 'fit/predict/transform', 'StandardScaler/MinMaxScaler', 'LabelEncoder/OneHotEncoder', 'SimpleImputer', 'Pipeline'],
                            ['监督学习', '线性/逻辑回归', '决策树/随机森林', 'SVM/SVC/SVR', 'KNN/朴素贝叶斯', 'GradientBoosting/AdaBoost'],
                            ['无监督学习', 'KMeans聚类', 'DBSCAN/层次聚类', '降维(PCA/LDA/t-SNE)', '异常检测(IsolationForest)', '高斯混合模型(GMM)'],
                            ['特征与评估', 'SelectKBest/RFE', '特征重要性', 'cross_val_score', '混淆矩阵/分类报告', 'ROC/AUC曲线'],
                            ['模型选择', 'GridSearchCV', 'RandomizedSearchCV', 'KFold/StratifiedKFold', '学习曲线/验证曲线', 'joblib模型持久化']
                        ]
                    },
                    'TensorFlow': {
                        'desc': 'Google开源深度学习框架，支持大规模分布式训练',
                        'difficulty': 2,
                        'dimensions': [
                            ['张量与计算', 'constant/Variable', '自动求导(GradientTape)', '运算(matmul/加)', 'Eager Execution', '函数计算图'],
                            ['模型与层', 'Sequential/Functional/Subclassing', 'Dense/Conv2D/BatchNorm', '激活函数与Dropout', '损失函数与优化器', 'model.fit/evaluate'],
                            ['数据与训练', 'tf.data.Dataset管道', 'TFRecord序列化', '数据增强', '回调(EarlyStopping/TensorBoard)', '自定义训练循环'],
                            ['分布式与优化', 'MirroredStrategy多GPU', 'MultiWorkerMirroredStrategy', '混合精度训练', 'XLA编译', 'TPU支持'],
                            ['部署与生态', 'SavedModel格式', 'TensorFlow Serving', 'TensorFlow Lite量化', 'TensorFlow.js', 'TensorFlow Hub/TFX']
                        ]
                    },
                    'XGBoost': {
                        'desc': '梯度提升决策树库，在结构化数据上表现优异',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与参数', 'XGBClassifier/Regressor', 'objective与eval_metric', 'max_depth/eta', 'n_estimators', 'subsample/colsample_bytree'],
                            ['正则与分裂', 'gamma/reg_alpha/reg_lambda', 'min_child_weight', '树方法(hist/approx)', '早停(early_stopping_rounds)', '交叉验证(xgb.cv)'],
                            ['特性与解释', '特征重要性', 'plot_tree可视化', 'DMatrix格式', '缺失值自动处理', 'SHAP/TreeSHAP特征归因'],
                            ['高级特性', 'GPU训练(gpu_hist)', '自定义目标/评估函数', 'DART与增强', '特征交互约束', '与sklearn Pipeline集成']
                        ]
                    },
                    '机器学习': {
                        'desc': '监督学习、无监督学习、强化学习等算法原理和应用',
                        'difficulty': 2,
                        'dimensions': [
                            ['监督学习', '线性回归与正则化', '逻辑回归(sigmoid/odds)', '决策树(ID3/C4.5/CART)', '随机森林/Bagging', 'AdaBoost/GBDT/XGBoost'],
                            ['SVM与贝叶斯', '支持向量机(核函数/间隔)', 'K近邻(KNN)', '朴素贝叶斯(条件独立)', '概率校准(Platt Scaling)', '概率图模型概念'],
                            ['无监督学习', '聚类(K-Means/DBSCAN)', '层次聚类', '高斯混合(GMM/EM)', '降维(PCA/LDA)', '异常检测(IsolationForest/LOF)'],
                            ['强化学习', 'MDP/马尔可夫决策', '价值迭代/策略迭代', '蒙特卡洛方法', '时序差分(TD/Q-Learning)', 'DQN/Policy Gradient/Actor-Critic'],
                            ['模型评估与选择', '交叉验证/留出法', '偏差方差权衡', '正则化(L1/L2/Dropout)', '归一化/标准化', '集成学习(Stacking/Blending)']
                        ]
                    },
                    '特征工程': {
                        'desc': '从原始数据中提取有效特征，提升模型性能',
                        'difficulty': 2,
                        'dimensions': [
                            ['数据清洗', '缺失值处理(删除/填充/预测)', '异常值检测(Z-score/IQR)', '异常值处理(缩尾/替换)', '重复值处理', '数据一致性验证'],
                            ['数值特征', '标准化(Z-score/MinMax)', '分箱(等频/等距/决策树)', '对数/Box-Cox变换', '幂变换', '多项式特征'],
                            ['类别与时间', 'One-Hot/Label Encoding', 'Target Encoding(均值编码)', '哈希编码', '时间特征(年/月/日/星期)', '滑动窗口/滞后特征'],
                            ['特征构造与选择', '特征交叉/组合', '聚合特征(groupby)', '统计特征(count/mean/std)', '方差阈值过滤', '卡方检验/互信息'],
                            ['降维与监控', 'PCA/SVD降维', '特征重要性(SHAP)', '递归特征消除(RFE)', '类别不平衡(SMOTE/ADASYN)', '特征漂移监控']
                        ]
                    },
                    'MLOps': {
                        'desc': '机器学习模型的开发运维一体化',
                        'difficulty': 3,
                        'dimensions': [
                            ['流程与平台', 'CI/CD/CT for ML', 'MLflow实验跟踪', '特征存储(Feast/Tecton)', '模型注册与版本管理', 'Kubeflow/Pipeline'],
                            ['部署与服务', '模型服务化(Triton/Seldon)', '实时/批处理推理', 'API封装', 'Docker/K8s部署', 'TF Serving/MLflow Serving'],
                            ['监控与治理', '数据漂移检测(Evidently)', '概念漂移', '业务指标监控', '模型告警与回滚', '审计与合规(GDPR)'],
                            ['优化与工具', 'AutoML与超参优化(Katib)', '模型压缩(量化/剪枝)', 'ONNX/TensorRT优化', 'DVC数据版本控制', 'Airflow/Prefect调度']
                        ]
                    },
                    '数学基础': {
                        'desc': '线性代数、概率统计、微积分、优化理论',
                        'difficulty': 3,
                        'dimensions': [
                            ['线性代数', '向量/矩阵运算', '特征值与特征向量', '奇异值分解(SVD)', '正定矩阵/伪逆', '矩阵分解(LU/QR/Cholesky)'],
                            ['概率与统计', '常见分布(伯努利/正态)', '贝叶斯定理', '最大似然估计(MLE)', '假设检验与置信区间', '相关性(Pearson/Spearman)'],
                            ['信息论', '熵与条件熵', '互信息', '交叉熵', 'KL散度', '信息增益(决策树)'],
                            ['微积分与优化', '导数/偏导数/梯度', '链式法则', '泰勒展开', '梯度下降法(批量/随机)', '牛顿法与拟牛顿法'],
                            ['凸优化', '凸函数定义', '拉格朗日乘数法', 'KKT条件', '对偶问题', 'EM算法与变分推断']
                        ]
                    },
                    '模型优化': {
                        'desc': '超参数调优、模型压缩、量化部署',
                        'difficulty': 3,
                        'dimensions': [
                            ['超参数搜索', '网格搜索/随机搜索', '贝叶斯优化(GP)', 'Hyperband/PBT', '进化算法/遗传算法', '学习率warmup与衰减'],
                            ['剪枝与蒸馏', '结构化/非结构化剪枝', '通道剪枝', '知识蒸馏(Teacher-Student)', '温度参数', '特征蒸馏'],
                            ['量化', '静态量化(PTQ)', '量化感知训练(QAT)', 'INT8/INT4量化', 'TFLite量化', '混合精度训练(FP16/BF16)'],
                            ['推理优化', 'TensorRT/ONNX Runtime', 'XLA编译', '图优化(Fuse Op)', '模型分片/流水线并行', 'CPU(OpenVINO)/GPU(cuDNN)优化'],
                            ['轻量网络', 'MobileNet/ShuffleNet', 'EfficientNet复合缩放', 'SENet注意力', '神经网络架构搜索(NAS)', '推理延迟与内存分析']
                        ]
                    },
                    '深度学习': {
                        'desc': '神经网络架构设计，CNN、RNN、Transformer等模型',
                        'difficulty': 3,
                        'dimensions': [
                            ['基础网络', 'MLP与激活函数', '反向传播与梯度消失/爆炸', '权重初始化(Xavier/He)', '优化器(Adam/AdamW)', 'BatchNorm/LayerNorm'],
                            ['卷积网络', 'Conv/池化', '空洞卷积/可分离卷积', 'SENet/CBAM注意力', 'ResNet/DenseNet', 'EfficientNet/Inception'],
                            ['序列与Transformer', 'RNN/LSTM/GRU', 'Seq2Seq与Attention', 'Self-Attention/多头注意力', 'Transformer/位置编码', 'BERT/GPT/T5'],
                            ['生成与自监督', 'VAE/GAN/DCGAN', 'Diffusion Model(DDPM/Stable Diffusion)', '对比学习(SimCLR/MoCo)', '自监督预训练', 'MAE/Masked Autoencoder'],
                            ['检测与分割', 'Faster R-CNN/YOLO/SSD', 'Anchor与Anchor Free', 'NMS/mAP', 'U-Net/Mask R-CNN', 'DeepLab/FCN']
                        ]
                    },
                    '自然语言处理': {
                        'desc': '文本分类、序列标注、文本生成等NLP任务',
                        'difficulty': 3,
                        'dimensions': [
                            ['文本表示', '分词(Jieba/HanLP)', '词性/命名实体(NER)', 'Word2Vec/GloVe', 'FastText', 'ELMo/上下文词向量'],
                            ['预训练模型', 'BERT/RoBERTa/ALBERT', 'GPT系列(GPT-3/GPT-4)', 'T5/BART', 'LLM大语言模型', 'ChatGPT/RLHF'],
                            ['NLP任务', '文本分类(TextCNN)', '序列标注(NER/BERT+CRF)', '机器翻译(Transformer)', '文本摘要(抽取/生成)', '问答系统(MRC)'],
                            ['生成与对话', '解码策略(Beam Search/采样)', '可控生成(top-k/top-p)', '意图识别与槽位填充', '对话系统(检索/生成)', '文本纠错'],
                            ['新范式与工程', '提示工程(Prompt/P-tuning)', 'Few-shot/Zero-shot', 'Chain-of-Thought', 'LangChain工具', 'LLM部署与量化(GPTQ/GGML)']
                        ]
                    },
                    '计算机视觉': {
                        'desc': '图像分类、目标检测、图像分割等视觉任务',
                        'difficulty': 3,
                        'dimensions': [
                            ['图像处理基础', '像素/通道/颜色空间', 'OpenCV/PIL读写', '滤波/边缘检测(Canny)', '霍夫变换', '形态学操作(腐蚀/膨胀)'],
                            ['分类与主干网络', 'AlexNet/VGG/ResNet', 'DenseNet/EfficientNet', 'ViT/Swin Transformer', 'CLIP对比视觉语言', '轻量网络(MobileNet)'],
                            ['目标检测', 'Faster R-CNN/FPN', 'YOLO系列(v1-v8)', 'SSD/RetinaNet', 'Anchor机制', 'mAP/IoU/NMS'],
                            ['图像分割', '语义分割(FCN/U-Net/DeepLab)', '实例分割(Mask R-CNN)', '全景分割(Panoptic FPN)', '抠图(Matting)', '分割评估指标'],
                            ['生成与高级任务', 'GAN/DCGAN/CycleGAN', 'Diffusion Model(DDPM/SD)', '风格迁移', '超分辨率(ESRGAN)', '姿态估计/OCR(CRNN)']
                        ]
                    }
                }
            }
        }
    }
}