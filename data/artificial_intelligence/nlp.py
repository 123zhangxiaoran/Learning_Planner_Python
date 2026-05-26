"""NLP工程师数据"""
data = {
    '计算机与信息技术': {
        '人工智能': {
            'NLP工程师': {
                'description': '开发自然语言处理应用，如文本分类、情感分析、机器翻译等。',
                'skills': {
                    'Jieba': {
                        'desc': '中文分词工具，支持自定义词典',
                        'difficulty': 1,
                        'dimensions': [
                            ['分词与词性', '精确/全/搜索模式', 'cut/cut_for_search', '并行分词', '词性标注(posseg)', 'PaddlePaddle模式'],
                            ['关键词提取', 'TF-IDF关键词', 'TextRank关键词', '停用词处理', '自定义词典(add_word)', '词典优先级'],
                            ['高级功能', 'Tokenize返回位置', '新词发现', '繁简转换', '拼音转换(pypinyin)', '命名实体识别(NER)'],
                            ['工程与优化', '分词速度优化', '批量分词', '词频统计', '中文句子分割', '正则表达式支持']
                        ]
                    },
                    'NLTK': {
                        'desc': '自然语言处理工具包，提供文本处理基础功能',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础文本处理', '分词(word_tokenize)', '句子分割(sent_tokenize)', '词性标注(pos_tag)', '停用词(stopwords)', '词干提取(Porter/Lancaster)'],
                            ['词形与语义', '词形还原(WordNetLemmatizer)', 'WordNet同义词/反义词', '语义相似度(path_similarity)', '频率分布(FreqDist)'],
                            ['N-gram与搭配', 'unigram/bigram/trigram', '条件频率分布', '搭配提取(collocations)', 'Bigram关联度量'],
                            ['分类与情感', '朴素贝叶斯分类', '情感分析(VADER)', '文本分类器训练', 'Maxent分类器', '信息抽取(IE)'],
                            ['语料库与解析', 'Brown/CNKI语料库', '分块(chunking)', '浅层解析(Shallow Parsing)', '依存分析概念', '与Scikit-learn集成']
                        ]
                    },
                    'Python': {
                        'desc': 'NLP开发的主要编程语言',
                        'difficulty': 1,
                        'dimensions': [
                            ['核心编程', '数据类型与控制流', '函数与lambda', '面向对象(类/继承)', '异常处理', '迭代器与生成器'],
                            ['文本与数据处理', '字符串与正则(re)', '文件读写', 'JSON/编码处理', 'NumPy数组', 'Pandas处理表格'],
                            ['高级特性', '装饰器', '上下文管理器(with)', '类型提示', '列表/字典推导式', '日志(logging)'],
                            ['生态与工具', 'pip/venv环境', 'Jupyter Notebook', 'requests HTTP请求', 'Matplotlib可视化', '单元测试(unittest)']
                        ]
                    },
                    'spaCy': {
                        'desc': '工业级NLP库，提供高效的文本处理流水线',
                        'difficulty': 1,
                        'dimensions': [
                            ['核心流水线', 'nlp对象/Pipeline', '分词与词性标注', '依存分析', '命名实体识别(NER)', '句子边界检测'],
                            ['相似度与向量', '词向量与相似度', 'doc/span.similarity', '多语言支持(zh/en)', '预训练模型(sm/lg/trf)'],
                            ['规则与匹配', 'Matcher规则匹配', 'PhraseMatcher', 'EntityRuler', '正则模式', '自定义属性扩展'],
                            ['自定义与训练', '自定义流水线组件', '训练模型(Train)', '数据标注与格式(JSONL)', '模型评估(evaluate)', '模型打包与加载'],
                            ['集成与进阶', '文本分类(TextCategorizer)', '实体链接', '共指消解概念', 'Transformers集成(spacy-transformers)', 'SentencePiece集成']
                        ]
                    },
                    'BERT': {
                        'desc': 'Google双向编码器表示模型，用于文本理解',
                        'difficulty': 2,
                        'dimensions': [
                            ['模型架构与输入', 'Transformer双向编码', 'WordPiece分词', 'Position/Segment Embedding', 'MLM与NSP任务', 'BERT-BASE/LARGE配置'],
                            ['变体与发展', 'RoBERTa动态遮蔽', 'ALBERT参数共享', 'DistilBERT蒸馏', 'ERNIE知识增强', 'MacBERT与XLNet'],
                            ['微调与应用', 'HuggingFace AutoModel/Tokenizer', '文本分类(BERTForSequenceClassification)', '命名实体识别(BERTForTokenClassification)', 'BERT+CRF/BiLSTM', 'Question Answering(SQuAD)'],
                            ['微调技巧', '学习率与epoch', '梯度累积与早停', '学习率调度', '微调数据处理', '中文模型(bert-base-chinese)'],
                            ['部署与优化', '模型压缩(剪枝/量化)', 'ONNX/TensorRT加速', 'BERT-as-service', 'Sentence-BERT(SBERT)', '对比学习(SimCSE)']
                        ]
                    },
                    'GPT': {
                        'desc': 'OpenAI生成式预训练模型，用于文本生成',
                        'difficulty': 2,
                        'dimensions': [
                            ['模型演进', 'GPT-1/2/3/4架构', 'Transformer Decoder Only', '自回归生成', 'Causal Language Modeling', 'GPT-3.5/ChatGPT/GPT-4 Turbo'],
                            ['API与参数', 'OpenAI Chat Completions API', 'API Key认证', 'Temperature/Top-p/Max Tokens', 'Streaming流式输出', 'JSON Mode与Function Calling'],
                            ['提示与进阶', 'System/User/Assistant Message', 'Few-shot/Zero-shot', 'Chain-of-Thought', 'Embedding API', 'Tokens计数'],
                            ['微调与安全', 'Fine-tuning数据格式(JSONL)', '微调成本与场景', '内容过滤与安全', '幻觉问题', '上下文长度限制'],
                            ['集成与生态', 'LangChain集成', 'GPT在对话/写作/代码/数据分析', 'Llama等开源替代', 'GPT-4V多模态', '推理模型(GPT-o1)']
                        ]
                    },
                    'Prompt工程': {
                        'desc': '设计有效的提示词引导模型输出',
                        'difficulty': 2,
                        'dimensions': [
                            ['结构与策略', '指令/上下文/输入/输出', 'Zero-shot/Few-shot', 'Chain-of-Thought思维链', 'Self-Consistency自洽性', 'Tree of Thoughts'],
                            ['技巧与控制', '角色扮演(Role Prompting)', '格式化输出(JSON/XML)', '任务分解(Step-by-step)', '约束与负面Prompt', 'Temperature/Top-p控制'],
                            ['优化与迭代', '迭代优化策略', 'Prompt模板与版本管理', 'Prompt压缩', '示例选择与格式', '长度与风格控制'],
                            ['安全与多模态', 'Prompt注入攻击与防护', '角色设定与安全边界', '多模态Prompt(图像/视频)', '代码/数学/推理专用Prompt', '创意与分析Prompt']
                        ]
                    },
                    'Transformers': {
                        'desc': 'Hugging Face提供的预训练模型库',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心API与模型', 'AutoModel/AutoTokenizer', 'Pipeline推理', 'BERT/GPT/RoBERTa/BART等', '模型加载与保存(save_pretrained)', 'Hub上传与共享'],
                            ['数据与分词', 'Tokenizer编码/解码', 'Truncation/Padding', 'Attention Mask/Position IDs', '分词器训练(train_new_from_iterator)', 'DataCollator批处理'],
                            ['训练与微调', 'Trainer API', 'TrainingArguments', '模型Fine-tuning流程', '数据处理(Map Dataset)', '梯度累积与混合精度'],
                            ['多框架与导出', 'PyTorch/TensorFlow/Flax', 'ONNX/ORT导出', 'TorchScript', '分布式训练', '多GPU训练策略'],
                            ['任务专用', '文本分类(SequenceClassification)', 'Token分类(TokenClassification)', '问答(QuestionAnswering)', '摘要(Summarization)', '文本生成(TextGeneration)']
                        ]
                    },
                    '序列标注': {
                        'desc': '命名实体识别、词性标注',
                        'difficulty': 2,
                        'dimensions': [
                            ['任务与标注模式', 'NER/POS/Chunking', 'BIO/BMES/BIOES标注', '实体类型(PER/LOC/ORG等)', '嵌套NER', '中文分词与NER联合'],
                            ['经典模型', 'CRF条件随机场', 'BiLSTM-CRF', 'BERT-CRF', 'BERT-BiLSTM-CRF', 'GlobalPointer/TPLinker'],
                            ['预训练与微调', 'RoBERTa-CRF/MacBERT-CRF', '数据标注工具(Brat/doccano)', '数据增强(回译/同义词)', 'F1/CoNLL评估', '模型推理Pipeline'],
                            ['进阶与应用', '实体链接与消歧', '知识库集成', '金融/医疗/法律领域NER', '在线/批处理预测', 'NER后处理与错误分析']
                        ]
                    },
                    '文本分类': {
                        'desc': '情感分析、主题分类、意图识别',
                        'difficulty': 2,
                        'dimensions': [
                            ['任务类型与数据', '二分类/多分类/多标签', '情感分析(方面级)', '主题/新闻分类', '意图识别/垃圾检测', '数据标注(Label Studio)'],
                            ['传统与深度模型', 'TF-IDF+SVM', 'TextCNN/TextRNN', 'BiLSTM+Attention', 'BERT/RoBERTa微调', 'Sentence-BERT分类'],
                            ['不平衡与评估', '过采样/欠采样', '类别权重', '混淆矩阵/F1/AUC', '分层采样与交叉验证', 'LIME/SHAP可解释性'],
                            ['前沿与部署', 'Few-shot Prompt分类', '零样本分类(BART)', '增量学习', 'ONNX/FastAPI部署', '模型压缩与蒸馏']
                        ]
                    },
                    '文本生成': {
                        'desc': '机器翻译、摘要生成、对话系统',
                        'difficulty': 2,
                        'dimensions': [
                            ['任务与模型', '语言模型/Seq2Seq', 'GPT/T5/BART', '机器翻译(NMT/Transformer)', '抽取式/生成式摘要', '对话系统(开放域/任务型)'],
                            ['解码与可控生成', 'Beam Search/Greedy', 'Top-k/Top-p采样', 'Temperature与重复惩罚', 'RLHF/PPO优化', '风格迁移/关键词控制'],
                            ['评估与应用', 'BLEU/ROUGE/METEOR', 'Pointer-Generator网络', '代码生成/诗歌/文案', 'ChatGLM等开源对话', '文本改写与续写']
                        ]
                    },
                    '注意力机制': {
                        'desc': 'Self-Attention、Multi-Head Attention原理',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础注意力', 'Query/Key/Value', '缩放点积注意力', '多头注意力(Multi-Head)', '自注意力(Self-Attention)', '交叉注意力(Cross-Attention)'],
                            ['变体与位置', 'Bahdanau/Luong Attention', '全局/局部注意力', '绝对/相对位置编码', 'RoPE旋转位置编码', 'ALiBi线性偏置'],
                            ['Transformer结构', 'Transformer Block', '残差连接与LayerNorm', 'FFN前馈网络', 'Encoder-Decoder架构', 'Padding/Causal Mask'],
                            ['高效注意力', 'Flash Attention', 'Sparse Attention', 'Reformer/LSH', 'Longformer滑动窗口', 'BigBird稀疏注意力']
                        ]
                    },
                    '词嵌入': {
                        'desc': 'Word2Vec、GloVe、FastText等词向量技术',
                        'difficulty': 2,
                        'dimensions': [
                            ['静态词向量', 'Word2Vec(CBOW/Skip-gram)', '负采样与分层Softmax', 'GloVe全局共现', 'FastText子词嵌入', 'OOV处理'],
                            ['上下文词向量', 'ELMo', 'BERT Embedding', '句子向量(SBERT)', 'Doc2Vec', 'SIF加权平均'],
                            ['评估与应用', '词向量相似度/类比任务', '可视化(t-SNE/UMAP)', '领域适应与微调', '多义词消歧', '跨语言对齐(MUSE)'],
                            ['向量检索', 'Faiss/ANN检索', '余弦/欧式距离', '词向量压缩', '偏置消除(Debiasing)', '中文预训练词向量']
                        ]
                    },
                    '问答系统': {
                        'desc': '阅读理解、知识图谱问答',
                        'difficulty': 2,
                        'dimensions': [
                            ['MRC阅读理解', 'Span抽取式(BiDAF/QANet)', 'BERT for QA', 'SQuAD/CMRC数据集', 'EM/F1评估', '多跳推理(HotpotQA)'],
                            ['知识图谱问答', '实体识别与关系抽取', 'SPARQL/Neo4j', '语义解析', '模板匹配', '实体链接'],
                            ['检索与对话', '开放域QA(Retriever-Reader)', 'Dense Retrieval', 'FAQ问答', '对话状态跟踪', '意图识别与槽位填充'],
                            ['多模态与前沿', 'Text-to-SQL', 'RAG检索增强', '视频/图片问答', '表格问答(Table QA)', 'Generative QA']
                        ]
                    },
                    'LLM微调': {
                        'desc': '大语言模型的领域适配和指令微调',
                        'difficulty': 3,
                        'dimensions': [
                            ['微调方法', '全参数微调', 'LoRA/QLoRA', 'Adapter/Prefix Tuning', 'Prompt Tuning/P-tuning', '知识蒸馏'],
                            ['对齐训练', 'SFT监督微调', 'RLHF(奖励模型/PPO)', 'DPO直接偏好优化', 'ORPO/KTO', 'RLAIF AI反馈'],
                            ['数据与框架', 'Alpaca/ShareGPT格式', '数据清洗与质量', 'LLaMA-Factory/xtuner', 'DeepSpeed/HuggingFace PEFT', 'Chat模板'],
                            ['训练与评估', '学习率/批次/Epoch', '混合精度(FP16/BF16)', '梯度累积与Warmup', '灾难遗忘', 'MT-Bench/AlpacaEval评估'],
                            ['部署与安全', 'LoRA合并与增量', '分布式训练', '安全微调/对齐微调', '有毒输出缓解', '参数高效微调(PEFT)']
                        ]
                    },
                    'RAG': {
                        'desc': '检索增强生成，结合外部知识库提升回答质量',
                        'difficulty': 3,
                        'dimensions': [
                            ['架构与基础', '检索+阅读+生成', 'Embedding模型(bge/m3e)', '文本分块(语义/固定)', '文档解析(PDF/Word)', '向量数据库(Milvus/FAISS)'],
                            ['检索优化', '混合检索(BM25+稠密)', 'Rerank重排序', 'Query改写/扩展', '上下文压缩', '迭代/多跳RAG'],
                            ['框架与评估', 'LangChain LlamaIndex', 'RAGAS评估(Faithfulness/Relevancy)', '上下文精度/召回', 'Self-RAG/CRAG', 'Agentic RAG'],
                            ['高级应用', '幻觉缓解', '知识冲突处理', '多模态RAG', '表格/代码RAG', 'Memory增强']
                        ]
                    },
                    '深度学习': {
                        'desc': '神经网络在文本处理中的应用',
                        'difficulty': 3,
                        'dimensions': [
                            ['基础模块', 'MLP/激活函数', '损失函数(CEE/MSE)', '反向传播与梯度下降', '优化器(Adam/SGD)', 'Dropout/BatchNorm'],
                            ['卷积与循环', 'TextCNN架构', 'LSTM/GRU', 'BiLSTM', '梯度消失与爆炸', '残差连接与LayerNorm'],
                            ['序列模型与注意力', 'Seq2Seq编码器解码器', '注意力机制', 'Transformer架构', '位置编码', '多头注意力'],
                            ['预训练与微调', 'BERT双向编码', 'GPT自回归生成', '预训练与微调策略', '模型初始化(Xavier/He)', '词向量层'],
                            ['任务与优化', '文本分类/序列标注', '机器翻译/文本生成', '模型压缩(剪枝/量化)', '知识蒸馏', '图神经网络(GNN)在NLP']
                        ]
                    }
                }
            }
        }
    }
}