import requests

# 先查看向量库状态
try:
    info = requests.get('http://localhost:8000/api/collection/info')
    if info.status_code == 200:
        requests.delete('http://localhost:8000/api/collection')
except:
    pass

# 重新构建数据 - 包含岗位描述
texts = []
metadatas = []

# 技能难度定义：1=基础入门，2=主流技术，3=进阶/专业
# 计算机专业数据 - 添加岗位描述和技能难度
computer_data = {
    '软件工程': {
        '前端开发工程师': {
            'description': '负责网站和Web应用的前端开发，将UI设计转化为可交互的页面。',
            'skills': {
                'CSS': {'desc': '层叠样式表，用于控制网页的视觉表现，包括布局、颜色、字体、动画、响应式设计等', 'difficulty': 1},
                'Git': {'desc': '分布式版本控制系统，用于代码管理和团队协作', 'difficulty': 1},
                'HTML': {'desc': '超文本标记语言，用于定义网页的内容结构和语义，包括标签、属性、表单、多媒体嵌入等', 'difficulty': 1},
                'JavaScript': {'desc': '网页脚本语言，用于实现页面交互功能、DOM操作、事件处理、异步请求等动态效果', 'difficulty': 1},
                'TypeScript': {'desc': 'JavaScript的超集，提供静态类型检查、接口定义和更好的IDE支持', 'difficulty': 1},
                'npm/yarn/pnpm': {'desc': 'JavaScript包管理工具，用于安装和管理项目依赖', 'difficulty': 1},
                'ES6+': {'desc': '现代JavaScript语法，包括箭头函数、解构赋值、Promise、async/await等', 'difficulty': 2},
                'React': {'desc': 'Facebook开发的组件化UI库，使用虚拟DOM和单向数据流构建复杂的单页应用', 'difficulty': 2},
                'Sass/Less': {'desc': 'CSS预处理器，提供变量、嵌套、混合等高级特性', 'difficulty': 2},
                'Tailwind CSS': {'desc': '实用优先的CSS框架，通过原子类快速构建自定义设计', 'difficulty': 2},
                'Vite': {'desc': '新一代前端构建工具，提供极速的开发服务器启动和热更新', 'difficulty': 2},
                'Vue': {'desc': '渐进式JavaScript框架，提供响应式数据绑定和组件化开发，易于上手且灵活', 'difficulty': 2},
                'Webpack': {'desc': '前端模块打包工具，支持代码分割、资源优化和开发服务器', 'difficulty': 2},
                '浏览器兼容性': {'desc': '处理不同浏览器的渲染差异，使用polyfill和特性检测', 'difficulty': 2},
                '移动端适配': {'desc': '响应式布局、rem/vw适配、触摸事件处理等移动端开发技术', 'difficulty': 2},
                '前端性能优化': {'desc': '代码分割、懒加载、缓存策略、资源压缩等性能提升技术', 'difficulty': 3}
            }
        },
        '后端开发工程师': {
            'description': '负责服务器端业务逻辑开发，设计和维护数据库API接口。',
            'skills': {
                'Go': {'desc': 'Google开发的高性能语言，原生支持并发，适合高并发微服务', 'difficulty': 1},
                'Java': {'desc': '企业级后端开发主流语言，拥有Spring生态和丰富的类库支持', 'difficulty': 1},
                'Linux': {'desc': '服务器操作系统，掌握常用命令和系统管理', 'difficulty': 1},
                'MySQL': {'desc': '最流行的开源关系型数据库，用于结构化数据的持久化存储和查询', 'difficulty': 1},
                'PostgreSQL': {'desc': '功能强大的开源关系型数据库，支持高级数据类型和复杂查询', 'difficulty': 1},
                'Python': {'desc': '简洁高效的后端开发语言，适合快速开发和数据处理场景', 'difficulty': 1},
                'RESTful API': {'desc': '基于HTTP的API设计规范，使用JSON进行数据交换', 'difficulty': 1},
                '单元测试': {'desc': 'JUnit、pytest等测试框架，编写自动化测试保证代码质量', 'difficulty': 1},
                'Django': {'desc': 'Python全栈Web框架，内置ORM、管理后台、认证系统等完整功能', 'difficulty': 2},
                'Docker': {'desc': '容器化技术，将应用及其依赖打包为可移植的容器镜像', 'difficulty': 2},
                'Elasticsearch': {'desc': '分布式搜索和分析引擎，用于全文搜索和日志分析', 'difficulty': 2},
                'FastAPI': {'desc': '现代Python Web框架，基于类型提示，自动生成OpenAPI文档', 'difficulty': 2},
                'GraphQL': {'desc': '灵活的API查询语言，客户端可精确获取所需数据', 'difficulty': 2},
                'JWT认证': {'desc': 'JSON Web Token，用于无状态的用户身份验证', 'difficulty': 2},
                'Kafka': {'desc': '高吞吐量分布式流处理平台，用于实时数据传输和处理', 'difficulty': 2},
                'MongoDB': {'desc': '文档型NoSQL数据库，适合存储非结构化和半结构化数据', 'difficulty': 2},
                'Nginx': {'desc': '高性能Web服务器和反向代理，用于负载均衡和静态资源服务', 'difficulty': 2},
                'OAuth2': {'desc': '开放授权协议，支持第三方登录和API访问授权', 'difficulty': 2},
                'RabbitMQ': {'desc': '消息队列中间件，实现应用解耦和异步任务处理', 'difficulty': 2},
                'Redis': {'desc': '高性能内存键值存储，用作缓存、会话存储和消息队列', 'difficulty': 2},
                'Spring Boot': {'desc': 'Java生态的简化开发框架，提供自动配置和开箱即用的微服务支持', 'difficulty': 2},
                'Spring Cloud': {'desc': '微服务架构解决方案，提供服务注册、配置中心、网关等组件', 'difficulty': 2},
                'gRPC': {'desc': '高性能RPC框架，基于Protocol Buffers进行服务间通信', 'difficulty': 2}
            }
        },
        '全栈工程师': {
            'description': '同时负责前端和后端开发，能够独立完成整个Web应用的开发。',
            'skills': {
                'Git/GitHub': {'desc': '版本控制和代码托管', 'difficulty': 1},
                'JavaScript': {'desc': '前后端通用的编程语言，Web开发的核心技术', 'difficulty': 1},
                'MySQL/PostgreSQL': {'desc': '关系型数据库，存储应用数据', 'difficulty': 1},
                'Node.js': {'desc': 'JavaScript运行时环境，用于服务端开发', 'difficulty': 1},
                'RESTful API': {'desc': '设计规范的前后端接口', 'difficulty': 1},
                'TypeScript': {'desc': '带类型的JavaScript，提升大型项目的可维护性', 'difficulty': 1},
                'Docker': {'desc': '容器化部署应用', 'difficulty': 2},
                'Express/Koa': {'desc': 'Node.js Web框架，构建RESTful API服务', 'difficulty': 2},
                'Next.js/Nuxt.js': {'desc': '全栈框架，提供服务端渲染和静态生成功能', 'difficulty': 2},
                'Prisma/TypeORM': {'desc': 'ORM工具，简化数据库操作', 'difficulty': 2},
                'React/Vue': {'desc': '前端组件化框架，构建用户界面', 'difficulty': 2},
                'Redis': {'desc': '内存数据库，用作缓存和会话存储', 'difficulty': 2},
                '云服务': {'desc': 'AWS、阿里云等云平台服务使用', 'difficulty': 2},
                '系统架构': {'desc': '理解单体应用和微服务架构的优缺点', 'difficulty': 2},
                '性能优化': {'desc': '前后端性能监控和优化策略', 'difficulty': 3}
            }
        },
        '测试工程师': {
            'description': '负责软件测试工作，编写测试用例，执行功能测试和性能测试。',
            'skills': {
                'JUnit': {'desc': 'Java单元测试框架，支持TDD开发模式', 'difficulty': 1},
                'Postman': {'desc': 'API接口测试工具，支持自动化测试集合和环境管理', 'difficulty': 1},
                'pytest': {'desc': 'Python测试框架，功能强大且易于使用', 'difficulty': 1},
                '测试用例设计': {'desc': '等价类划分、边界值分析、场景法等测试设计方法', 'difficulty': 1},
                '缺陷管理': {'desc': '使用Jira等工具跟踪和管理Bug', 'difficulty': 1},
                'CI/CD集成': {'desc': '将自动化测试集成到持续集成流程', 'difficulty': 2},
                'Cypress': {'desc': '前端端到端测试框架，提供实时重载和调试功能', 'difficulty': 2},
                'JMeter': {'desc': '性能测试工具，进行负载测试和压力测试', 'difficulty': 2},
                'Playwright': {'desc': '微软出品的现代Web测试框架，支持自动等待和并行执行', 'difficulty': 2},
                'Selenium': {'desc': 'Web应用自动化测试工具，支持多种浏览器和编程语言', 'difficulty': 2},
                '接口测试': {'desc': '测试API的正确性、稳定性和性能', 'difficulty': 2},
                '自动化测试': {'desc': '编写测试脚本实现回归测试自动化', 'difficulty': 2},
                '性能测试': {'desc': '识别系统瓶颈，测试并发处理能力和响应时间', 'difficulty': 3}
            }
        },
        'DevOps工程师': {
            'description': '负责持续集成/持续部署，自动化运维和基础设施管理。',
            'skills': {
                'Python': {'desc': '运维自动化和工具开发', 'difficulty': 1},
                'Ansible': {'desc': '自动化运维工具，批量配置服务器', 'difficulty': 2},
                'Docker': {'desc': '容器化技术，实现应用快速部署和环境一致性', 'difficulty': 2},
                'ELK Stack': {'desc': 'Elasticsearch、Logstash、Kibana日志分析平台', 'difficulty': 2},
                'GitHub Actions': {'desc': 'GitHub的自动化工作流平台', 'difficulty': 2},
                'GitLab CI': {'desc': 'GitLab内置的持续集成工具', 'difficulty': 2},
                'Grafana': {'desc': '数据可视化和监控仪表板', 'difficulty': 2},
                'Helm': {'desc': 'Kubernetes包管理工具，简化应用部署', 'difficulty': 2},
                'Jenkins': {'desc': '开源CI/CD工具，自动化构建、测试和部署', 'difficulty': 2},
                'Kubernetes': {'desc': '容器编排平台，管理大规模容器集群的部署和扩展', 'difficulty': 2},
                'Nginx': {'desc': 'Web服务器和反向代理配置', 'difficulty': 2},
                'Prometheus': {'desc': '监控系统和时间序列数据库', 'difficulty': 2},
                'Terraform': {'desc': '基础设施即代码工具，自动化云资源管理', 'difficulty': 2},
                'Linux': {'desc': '服务器操作系统管理和命令行操作', 'difficulty': 3},
                'Shell脚本': {'desc': '自动化运维脚本编写', 'difficulty': 3},
                '云原生': {'desc': '理解云原生架构和12要素应用', 'difficulty': 3},
                '网络基础': {'desc': 'TCP/IP、DNS、HTTP等网络协议', 'difficulty': 3}
            }
        },
        '移动端开发工程师': {
            'description': '开发iOS和Android移动应用，实现原生或跨平台功能。',
            'skills': {
                'Java': {'desc': 'Android传统开发语言，生态成熟', 'difficulty': 1},
                'Kotlin': {'desc': 'Android官方推荐开发语言，与Java完全互操作', 'difficulty': 1},
                'Swift': {'desc': 'Apple开发的iOS应用编程语言，现代、安全、高效', 'difficulty': 1},
                'App发布': {'desc': '应用商店审核流程和发布管理', 'difficulty': 2},
                'Flutter': {'desc': 'Google跨平台UI框架，使用Dart语言，一套代码多端运行', 'difficulty': 2},
                'React Native': {'desc': '使用React构建原生移动应用的框架', 'difficulty': 2},
                '地图定位': {'desc': 'GPS定位、地图SDK集成', 'difficulty': 2},
                '推送服务': {'desc': 'APNs、FCM等推送通知集成', 'difficulty': 2},
                '支付集成': {'desc': '微信支付、支付宝、Apple Pay等', 'difficulty': 2},
                '混合开发': {'desc': 'WebView、Cordova、Ionic等混合应用方案', 'difficulty': 2},
                '移动端UI': {'desc': '移动端设计规范、适配不同屏幕尺寸', 'difficulty': 2},
                'Android开发': {'desc': 'Android SDK、Jetpack组件、Material Design', 'difficulty': 3},
                'iOS开发': {'desc': 'UIKit、SwiftUI、Core Data等iOS框架', 'difficulty': 3},
                '性能优化': {'desc': '启动优化、内存管理、电量优化', 'difficulty': 3},
                '热更新': {'desc': '动态下发代码修复线上问题', 'difficulty': 3}
            }
        }
    },
    '人工智能': {
        '算法工程师': {
            'description': '研究和开发机器学习算法，解决实际的AI问题，优化模型性能。',
            'skills': {
                'NumPy': {'desc': '数值计算库，提供高效的多维数组操作', 'difficulty': 1},
                'Pandas': {'desc': '数据处理和分析库，用于数据清洗和预处理', 'difficulty': 1},
                'Python': {'desc': 'AI领域主流编程语言，拥有丰富的科学计算和机器学习库', 'difficulty': 1},
                'A/B测试': {'desc': '设计实验验证算法效果', 'difficulty': 2},
                'Keras': {'desc': '高级神经网络API，简化深度学习模型构建', 'difficulty': 2},
                'LightGBM': {'desc': '微软高效梯度提升框架，训练速度快内存占用低', 'difficulty': 2},
                'PyTorch': {'desc': 'Facebook开源深度学习框架，动态图机制灵活易用', 'difficulty': 2},
                'Scikit-learn': {'desc': '传统机器学习算法库，包含分类、回归、聚类等算法', 'difficulty': 2},
                'TensorFlow': {'desc': 'Google开源深度学习框架，支持大规模分布式训练', 'difficulty': 2},
                'XGBoost': {'desc': '梯度提升决策树库，在结构化数据上表现优异', 'difficulty': 2},
                '机器学习': {'desc': '监督学习、无监督学习、强化学习等算法原理和应用', 'difficulty': 2},
                '特征工程': {'desc': '从原始数据中提取有效特征，提升模型性能', 'difficulty': 2},
                'MLOps': {'desc': '机器学习模型的开发运维一体化', 'difficulty': 3},
                '数学基础': {'desc': '线性代数、概率统计、微积分、优化理论', 'difficulty': 3},
                '模型优化': {'desc': '超参数调优、模型压缩、量化部署', 'difficulty': 3},
                '深度学习': {'desc': '神经网络架构设计，CNN、RNN、Transformer等模型', 'difficulty': 3},
                '自然语言处理': {'desc': '文本分类、序列标注、文本生成等NLP任务', 'difficulty': 3},
                '计算机视觉': {'desc': '图像分类、目标检测、图像分割等视觉任务', 'difficulty': 3}
            }
        },
        '数据科学家': {
            'description': '通过数据分析挖掘业务价值，建立数据模型支持决策。',
            'skills': {
                'NumPy': {'desc': '数值计算和矩阵运算', 'difficulty': 1},
                'Pandas': {'desc': '数据清洗、转换和分析', 'difficulty': 1},
                'Python/R': {'desc': '数据分析和建模的主要工具语言', 'difficulty': 1},
                'SQL': {'desc': '从数据库中提取和处理数据', 'difficulty': 1},
                'A/B测试': {'desc': '设计实验评估产品改动效果', 'difficulty': 2},
                'Tableau/Power BI': {'desc': '商业智能工具制作交互式仪表板', 'difficulty': 2},
                '业务理解': {'desc': '将业务问题转化为数据问题', 'difficulty': 2},
                '探索性数据分析': {'desc': '使用统计方法和可视化理解数据分布', 'difficulty': 2},
                '数据可视化': {'desc': '使用Matplotlib、Seaborn、Plotly展示数据洞察', 'difficulty': 2},
                '数据报告': {'desc': '撰写数据分析报告，提供决策建议', 'difficulty': 2},
                '数据清洗': {'desc': '处理缺失值、异常值、重复数据', 'difficulty': 2},
                '机器学习': {'desc': '构建预测模型和分类模型', 'difficulty': 2},
                '特征工程': {'desc': '构建和选择对模型有用的特征', 'difficulty': 2},
                '统计学': {'desc': '假设检验、回归分析、时间序列分析等统计方法', 'difficulty': 2}
            }
        },
        'NLP工程师': {
            'description': '开发自然语言处理应用，如文本分类、情感分析、机器翻译等。',
            'skills': {
                'Jieba': {'desc': '中文分词工具，支持自定义词典', 'difficulty': 1},
                'NLTK': {'desc': '自然语言处理工具包，提供文本处理基础功能', 'difficulty': 1},
                'Python': {'desc': 'NLP开发的主要编程语言', 'difficulty': 1},
                'spaCy': {'desc': '工业级NLP库，提供高效的文本处理流水线', 'difficulty': 1},
                'BERT': {'desc': 'Google双向编码器表示模型，用于文本理解', 'difficulty': 2},
                'GPT': {'desc': 'OpenAI生成式预训练模型，用于文本生成', 'difficulty': 2},
                'Prompt工程': {'desc': '设计有效的提示词引导模型输出', 'difficulty': 2},
                'Transformers': {'desc': 'Hugging Face提供的预训练模型库', 'difficulty': 2},
                '序列标注': {'desc': '命名实体识别、词性标注', 'difficulty': 2},
                '文本分类': {'desc': '情感分析、主题分类、意图识别', 'difficulty': 2},
                '文本生成': {'desc': '机器翻译、摘要生成、对话系统', 'difficulty': 2},
                '注意力机制': {'desc': 'Self-Attention、Multi-Head Attention原理', 'difficulty': 2},
                '词嵌入': {'desc': 'Word2Vec、GloVe、FastText等词向量技术', 'difficulty': 2},
                '问答系统': {'desc': '阅读理解、知识图谱问答', 'difficulty': 2},
                'LLM微调': {'desc': '大语言模型的领域适配和指令微调', 'difficulty': 3},
                'RAG': {'desc': '检索增强生成，结合外部知识库提升回答质量', 'difficulty': 3},
                '深度学习': {'desc': '神经网络在文本处理中的应用', 'difficulty': 3}
            }
        },
        '计算机视觉工程师': {
            'description': '开发图像和视频处理算法，如目标检测、人脸识别、图像分割等。',
            'skills': {
                'Python': {'desc': '计算机视觉开发的主流语言', 'difficulty': 1},
                'CNN': {'desc': '卷积神经网络，图像特征提取的基础', 'difficulty': 2},
                'Keras': {'desc': '高级神经网络API', 'difficulty': 2},
                'OpenCV': {'desc': '开源计算机视觉库，提供图像处理基础功能', 'difficulty': 2},
                'PIL/Pillow': {'desc': 'Python图像处理库', 'difficulty': 2},
                'PyTorch': {'desc': '研究友好的深度学习框架', 'difficulty': 2},
                'TensorFlow': {'desc': '深度学习模型训练和部署', 'difficulty': 2},
                '图像分类': {'desc': '识别图像中的物体类别', 'difficulty': 2},
                '图像增强': {'desc': '去噪、超分辨率、风格迁移', 'difficulty': 2},
                'OCR': {'desc': '光学字符识别，从图像中提取文字', 'difficulty': 3},
                'ResNet': {'desc': '残差网络，解决深层网络训练问题', 'difficulty': 3},
                'YOLO': {'desc': '实时目标检测算法', 'difficulty': 3},
                '人脸识别': {'desc': '人脸检测、特征提取、身份验证', 'difficulty': 3},
                '图像分割': {'desc': '像素级图像分割，包括语义分割和实例分割', 'difficulty': 3},
                '模型部署': {'desc': '模型转换、量化、边缘设备部署', 'difficulty': 3},
                '目标检测': {'desc': '定位并识别图像中的多个物体', 'difficulty': 3},
                '视频分析': {'desc': '目标跟踪、行为识别、视频理解', 'difficulty': 3}
            }
        },
        '推荐算法工程师': {
            'description': '开发个性化推荐系统，提升用户体验和商业转化率。',
            'skills': {
                'Python': {'desc': '推荐系统开发语言', 'difficulty': 1},
                'Embedding': {'desc': '用户和物品的向量表示学习', 'difficulty': 2},
                'Redis': {'desc': '缓存推荐结果和用户特征', 'difficulty': 2},
                'Spark': {'desc': '大规模数据处理框架', 'difficulty': 2},
                '冷启动': {'desc': '新用户和新物品的推荐策略', 'difficulty': 2},
                '协同过滤': {'desc': '基于用户或物品的相似度推荐', 'difficulty': 2},
                '召回算法': {'desc': '快速筛选候选集的算法', 'difficulty': 2},
                '特征工程': {'desc': '构建用户画像和物品特征', 'difficulty': 2},
                '矩阵分解': {'desc': 'SVD、ALS等降维技术', 'difficulty': 2},
                'A/B测试': {'desc': '评估推荐效果', 'difficulty': 3},
                'DIN': {'desc': '深度兴趣网络，建模用户动态兴趣', 'difficulty': 3},
                'Wide&Deep': {'desc': 'Google的推荐模型架构', 'difficulty': 3},
                '实时推荐': {'desc': '流式计算实现实时个性化', 'difficulty': 3},
                '排序算法': {'desc': '精排模型，预测用户点击率或转化率', 'difficulty': 3},
                '深度学习推荐': {'desc': '使用神经网络构建推荐模型', 'difficulty': 3}
            }
        }
    },
    '网络工程': {
        '网络工程师': {
            'description': '负责企业网络规划、搭建和维护，保障网络稳定运行。',
            'skills': {
                'ACL': {'desc': '访问控制列表，网络安全策略配置', 'difficulty': 2},
                'NAT': {'desc': '网络地址转换，实现内外网通信', 'difficulty': 2},
                'TCP/IP': {'desc': '网络通信核心协议栈，理解IP寻址和路由原理', 'difficulty': 2},
                'VLAN': {'desc': '虚拟局域网划分和配置', 'difficulty': 2},
                '网络协议': {'desc': 'HTTP、DNS、DHCP、FTP等应用层协议原理', 'difficulty': 2},
                '网络排障': {'desc': '使用ping、traceroute、Wireshark等工具排查故障', 'difficulty': 2},
                '网络监控': {'desc': 'SNMP、Zabbix等网络监控工具', 'difficulty': 2},
                '防火墙': {'desc': '网络安全边界防护设备配置和管理', 'difficulty': 2},
                'BGP': {'desc': '边界网关协议，互联网核心路由协议', 'difficulty': 3},
                'Cisco': {'desc': '思科网络设备配置和管理，CCNA/CCNP认证相关技术', 'difficulty': 3},
                'H3C': {'desc': '华三网络设备配置和管理', 'difficulty': 3},
                'OSPF': {'desc': '开放式最短路径优先，内部网关路由协议', 'difficulty': 3},
                'STP': {'desc': '生成树协议，防止网络环路', 'difficulty': 3},
                'VPN': {'desc': '虚拟专用网络，IPSec和SSL VPN配置', 'difficulty': 3},
                'VRRP': {'desc': '虚拟路由冗余协议，实现网关高可用', 'difficulty': 3},
                '华为设备': {'desc': '华为路由交换设备配置，HCIA/HCIP认证', 'difficulty': 3},
                '负载均衡': {'desc': 'F5、Nginx等负载均衡设备配置', 'difficulty': 3}
            }
        },
        '网络安全工程师': {
            'description': '负责网络安全防护，渗透测试和安全漏洞修复。',
            'skills': {
                'Nmap': {'desc': '网络扫描和端口探测工具', 'difficulty': 2},
                'Web安全': {'desc': 'SQL注入、XSS、CSRF等Web攻击原理和防护', 'difficulty': 2},
                'Wireshark': {'desc': '网络协议分析和抓包工具', 'difficulty': 2},
                '等保合规': {'desc': '网络安全等级保护测评和整改', 'difficulty': 2},
                '防火墙': {'desc': '访问控制策略配置和网络边界防护', 'difficulty': 2},
                'Burp Suite': {'desc': 'Web应用安全测试平台', 'difficulty': 3},
                'IDS/IPS': {'desc': '入侵检测和防御系统部署', 'difficulty': 3},
                'Kali Linux': {'desc': '专业渗透测试操作系统及工具使用', 'difficulty': 3},
                'Metasploit': {'desc': '漏洞利用框架和渗透测试工具', 'difficulty': 3},
                'WAF': {'desc': 'Web应用防火墙配置和规则调优', 'difficulty': 3},
                '代码审计': {'desc': '审查源代码发现安全漏洞', 'difficulty': 3},
                '安全加固': {'desc': '操作系统和应用的安全配置', 'difficulty': 3},
                '应急响应': {'desc': '安全事件处理和取证分析', 'difficulty': 3},
                '渗透测试': {'desc': '模拟攻击测试系统安全性，发现安全弱点', 'difficulty': 3},
                '漏洞扫描': {'desc': 'Nessus、OpenVAS等自动化漏洞扫描工具', 'difficulty': 3}
            }
        },
        '系统管理员': {
            'description': '负责服务器和系统的日常运维管理工作。',
            'skills': {
                'Python': {'desc': '运维自动化脚本和工具开发', 'difficulty': 1},
                'Windows Server': {'desc': 'Windows服务器管理和AD域配置', 'difficulty': 1},
                'Ansible': {'desc': '自动化运维工具，批量配置管理', 'difficulty': 2},
                'Linux': {'desc': 'Linux服务器安装配置和日常维护，包括CentOS、Ubuntu等', 'difficulty': 2},
                'Shell': {'desc': 'Linux自动化运维脚本编写', 'difficulty': 2},
                '备份恢复': {'desc': '数据备份策略制定和灾难恢复', 'difficulty': 2},
                '网络配置': {'desc': '服务器网络参数配置和故障排查', 'difficulty': 2},
                'ELK': {'desc': 'Elasticsearch、Logstash、Kibana日志分析', 'difficulty': 3},
                'ITIL': {'desc': 'IT服务管理流程和最佳实践', 'difficulty': 3},
                'KVM': {'desc': '开源虚拟化技术', 'difficulty': 3},
                'Nagios': {'desc': '系统和网络监控工具', 'difficulty': 3},
                'VMware': {'desc': '虚拟化平台管理和虚拟机部署', 'difficulty': 3},
                'Zabbix': {'desc': '开源监控系统', 'difficulty': 3},
                '存储管理': {'desc': 'SAN、NAS存储配置和管理', 'difficulty': 3},
                '高可用': {'desc': 'Keepalived、HAProxy等高可用方案', 'difficulty': 3}
            }
        }
    },
    '数据科学': {
        '数据分析师': {
            'description': '收集、处理和分析数据，制作数据报表和可视化图表。',
            'skills': {
                'Excel': {'desc': '电子表格数据处理和基础分析，包括透视表和函数', 'difficulty': 1},
                'Python': {'desc': '数据处理和分析的编程工具', 'difficulty': 1},
                'SQL': {'desc': '数据库查询和数据提取', 'difficulty': 1},
                'A/B测试': {'desc': '设计实验验证假设，评估产品改动效果', 'difficulty': 2},
                'FineBI': {'desc': '国产商业智能工具', 'difficulty': 2},
                'Power BI': {'desc': '微软商业智能分析工具', 'difficulty': 2},
                'Tableau': {'desc': '商业智能可视化工具，制作交互式图表和仪表板', 'difficulty': 2},
                '业务理解': {'desc': '深入理解业务场景，将数据转化为业务洞察', 'difficulty': 2},
                '报表开发': {'desc': '定期生成业务报表，监控关键指标', 'difficulty': 2},
                '数据可视化': {'desc': '将数据转化为图表和仪表板展示，设计清晰的数据故事', 'difficulty': 2},
                '数据报告': {'desc': '撰写数据分析报告，提供决策建议', 'difficulty': 2},
                '数据清洗': {'desc': '处理缺失值、异常值、重复数据', 'difficulty': 2},
                '统计分析': {'desc': '描述统计、推断统计、相关分析、回归分析等方法', 'difficulty': 2}
            }
        },
        '数据工程师': {
            'description': '搭建和维护数据管道，开发ETL流程，处理大规模数据。',
            'skills': {
                'Python': {'desc': '数据管道开发和数据处理脚本', 'difficulty': 1},
                'SQL': {'desc': '数据仓库查询和优化', 'difficulty': 1},
                'Scala': {'desc': '大数据处理语言，Spark原生支持', 'difficulty': 1},
                'ETL': {'desc': '数据抽取、转换、加载流程开发', 'difficulty': 2},
                'Flink': {'desc': '实时流处理框架', 'difficulty': 2},
                'Hadoop': {'desc': '大数据存储和处理生态系统，包括HDFS和MapReduce', 'difficulty': 2},
                'Hive': {'desc': '基于Hadoop的数据仓库工具', 'difficulty': 2},
                'Kafka': {'desc': '高吞吐量消息队列，数据采集和传输', 'difficulty': 2},
                'Spark': {'desc': '大数据分布式计算框架，支持批处理和流处理', 'difficulty': 2},
                '数据仓库': {'desc': '维度建模、事实表设计、星型/雪花模型', 'difficulty': 2},
                '数据治理': {'desc': '数据质量、元数据管理、数据血缘', 'difficulty': 2},
                '数据湖': {'desc': '存储原始格式的大规模数据', 'difficulty': 2},
                '调度系统': {'desc': 'Airflow、DolphinScheduler等任务调度', 'difficulty': 2},
                '大数据技术': {'desc': '分布式系统和大数据架构设计', 'difficulty': 3}
            }
        },
        'BI工程师': {
            'description': '开发商业智能报表和仪表板，为业务决策提供数据支持。',
            'skills': {
                'SQL': {'desc': '数据查询和报表数据源配置', 'difficulty': 1},
                'ETL': {'desc': '简单的数据抽取和转换', 'difficulty': 2},
                'FineReport': {'desc': '国产报表开发工具', 'difficulty': 2},
                'Power BI': {'desc': '微软商业智能分析工具', 'difficulty': 2},
                'Tableau': {'desc': '数据可视化和仪表板开发工具', 'difficulty': 2},
                '报表开发': {'desc': '企业级报表和KPI仪表板制作', 'difficulty': 2},
                '指标体系': {'desc': '构建业务指标体系和KPI', 'difficulty': 2},
                '数据仓库': {'desc': '理解数据仓库架构和模型', 'difficulty': 2},
                '数据建模': {'desc': '维度建模和事实表设计', 'difficulty': 2},
                '权限管理': {'desc': '报表和数据行级权限控制', 'difficulty': 2},
                '移动端': {'desc': '移动端报表适配和发布', 'difficulty': 2}
            }
        }
    },
    '信息安全': {
        '安全工程师': {
            'description': '负责企业信息安全体系建设，安全风险评估和防护。',
            'skills': {
                'VPN': {'desc': '虚拟专用网络配置和安全接入', 'difficulty': 2},
                '云安全': {'desc': '云计算环境的安全配置和防护', 'difficulty': 2},
                '应用安全': {'desc': 'SDL安全开发生命周期', 'difficulty': 2},
                '数据安全': {'desc': '数据分类分级、加密、脱敏', 'difficulty': 2},
                '渗透测试': {'desc': '模拟攻击测试系统安全性，发现安全弱点', 'difficulty': 2},
                '等保2.0': {'desc': '网络安全等级保护标准和测评', 'difficulty': 2},
                '网络安全': {'desc': '网络边界防护、入侵检测和流量监控', 'difficulty': 2},
                '防火墙': {'desc': '访问控制策略配置和网络边界防护', 'difficulty': 2},
                '风险评估': {'desc': '安全风险识别和评估报告编写', 'difficulty': 2},
                'ISO27001': {'desc': '信息安全管理体系', 'difficulty': 3},
                '安全加固': {'desc': '系统安全配置和漏洞修复', 'difficulty': 3},
                '安全审计': {'desc': '日志审计和行为分析', 'difficulty': 3}
            }
        },
        '渗透测试工程师': {
            'description': '模拟黑客攻击测试系统安全性，发现并报告安全漏洞。',
            'skills': {
                'Nmap': {'desc': '网络扫描和端口探测', 'difficulty': 2},
                'OWASP': {'desc': 'Web安全漏洞标准和测试方法', 'difficulty': 2},
                'SQLMap': {'desc': '自动化SQL注入检测工具', 'difficulty': 2},
                '应急响应': {'desc': '协助修复发现的安全漏洞', 'difficulty': 2},
                '渗透测试': {'desc': 'Web应用、网络和系统的安全测试', 'difficulty': 2},
                '漏洞报告': {'desc': '编写专业的渗透测试报告', 'difficulty': 2},
                'Burp Suite': {'desc': 'Web应用安全测试平台', 'difficulty': 3},
                'Kali Linux': {'desc': '专业渗透测试操作系统及工具集', 'difficulty': 3},
                'Metasploit': {'desc': '漏洞利用框架和渗透测试工具', 'difficulty': 3},
                '内网渗透': {'desc': '横向移动、权限提升、域渗透', 'difficulty': 3},
                '漏洞利用': {'desc': '漏洞验证和利用脚本编写', 'difficulty': 3},
                '社会工程学': {'desc': '钓鱼攻击、物理渗透测试', 'difficulty': 3}
            }
        },
        '安全运维工程师': {
            'description': '监控安全事件，进行应急响应和事后分析。',
            'skills': {
                '取证分析': {'desc': '数字取证和攻击溯源', 'difficulty': 2},
                '安全监控': {'desc': '安全设备和日志实时监控', 'difficulty': 2},
                '安全设备': {'desc': '防火墙、IDS/IPS、WAF等设备运维', 'difficulty': 2},
                '应急响应': {'desc': '安全事件快速响应和处置', 'difficulty': 2},
                '日志分析': {'desc': '安全日志分析和威胁识别', 'difficulty': 2},
                '漏洞管理': {'desc': '漏洞扫描和修复跟踪', 'difficulty': 2},
                'SIEM': {'desc': '安全信息与事件管理系统', 'difficulty': 3},
                'SOC': {'desc': '安全运营中心建设', 'difficulty': 3},
                '威胁情报': {'desc': '收集和应用威胁情报', 'difficulty': 3},
                '安全加固': {'desc': '系统和应用安全配置', 'difficulty': 3}
            }
        }
    },
    '物联网工程': {
        '嵌入式工程师': {
            'description': '开发嵌入式系统，编写硬件驱动，实现设备功能。',
            'skills': {
                'C': {'desc': '嵌入式开发底层编程语言', 'difficulty': 1},
                'C++': {'desc': '面向对象嵌入式开发', 'difficulty': 1},
                'ADC/DAC': {'desc': '模数/数模转换', 'difficulty': 2},
                'ESP32': {'desc': '乐鑫WiFi/蓝牙芯片开发', 'difficulty': 2},
                'GPIO': {'desc': '通用输入输出控制', 'difficulty': 2},
                'I2C/SPI/UART': {'desc': '常用硬件通信协议', 'difficulty': 2},
                'PWM': {'desc': '脉冲宽度调制', 'difficulty': 2},
                'RTOS': {'desc': '实时操作系统开发和任务调度，如FreeRTOS', 'difficulty': 2},
                'STM32': {'desc': '意法半导体ARM Cortex-M系列开发', 'difficulty': 2},
                '调试工具': {'desc': '示波器、逻辑分析仪、JTAG调试器', 'difficulty': 2},
                'ARM': {'desc': 'ARM处理器架构和编程', 'difficulty': 3},
                '嵌入式Linux': {'desc': 'Linux内核裁剪和驱动开发', 'difficulty': 3},
                '汇编': {'desc': '底层硬件操作和性能优化', 'difficulty': 3},
                '硬件驱动': {'desc': '设备驱动开发和硬件接口编程', 'difficulty': 3}
            }
        },
        'IoT开发工程师': {
            'description': '开发物联网应用，实现设备连接、云端数据传输和控制。',
            'skills': {
                'Python': {'desc': '物联网应用层开发语言', 'difficulty': 1},
                'CoAP': {'desc': '受限应用协议，适用于低功耗设备', 'difficulty': 2},
                'HTTP/REST': {'desc': 'Web API通信', 'difficulty': 2},
                'MQTT': {'desc': '物联网轻量级消息传输协议', 'difficulty': 2},
                '云平台': {'desc': '阿里云IoT、AWS IoT、Azure IoT等平台', 'difficulty': 2},
                '传感器': {'desc': '温湿度、光照、加速度等各类传感器数据采集', 'difficulty': 2},
                '单片机': {'desc': 'Arduino、ESP32、树莓派等开发', 'difficulty': 2},
                '可视化': {'desc': '设备数据可视化和监控', 'difficulty': 2},
                '数据传输协议': {'desc': 'HTTP、CoAP、LwM2M等协议', 'difficulty': 2},
                '数据存储': {'desc': '时序数据库如InfluxDB', 'difficulty': 2},
                '设备管理': {'desc': 'OTA升级、设备注册、生命周期管理', 'difficulty': 2},
                '边缘计算': {'desc': '边缘网关和本地数据处理', 'difficulty': 3}
            }
        },
        '硬件工程师': {
            'description': '设计硬件电路，绘制PCB，调试硬件样机。',
            'skills': {
                '元器件选型': {'desc': '电阻电容芯片等器件参数选型和成本控制', 'difficulty': 2},
                '制板工艺': {'desc': 'PCB制造工艺和工厂对接', 'difficulty': 2},
                '原理图': {'desc': '电路原理图设计和分析', 'difficulty': 2},
                '焊接': {'desc': 'SMT和手工焊接技术', 'difficulty': 2},
                '电源设计': {'desc': '开关电源、LDO等电源方案', 'difficulty': 2},
                '电路设计': {'desc': '模拟电路和数字电路设计', 'difficulty': 2},
                '硬件调试': {'desc': '示波器、万用表、逻辑分析仪等调试工具', 'difficulty': 2},
                'EMC': {'desc': '电磁兼容性设计和整改', 'difficulty': 3},
                'PCB设计': {'desc': 'Altium Designer、Cadence等PCB设计软件', 'difficulty': 3},
                '信号完整性': {'desc': '高速信号PCB设计', 'difficulty': 3}
            }
        }
    },
    '云计算': {
        '云计算工程师': {
            'description': '设计和维护云架构，管理和优化云资源。',
            'skills': {
                'AWS': {'desc': '亚马逊云服务架构设计和部署，EC2、S3、RDS等', 'difficulty': 2},
                'Azure': {'desc': '微软云平台服务管理和开发', 'difficulty': 2},
                'Docker': {'desc': '容器化技术应用部署', 'difficulty': 2},
                'Kubernetes': {'desc': '容器编排和集群管理', 'difficulty': 2},
                'Serverless': {'desc': '无服务器架构，Lambda、函数计算', 'difficulty': 2},
                'Terraform': {'desc': '基础设施即代码自动化部署', 'difficulty': 2},
                '云原生': {'desc': '微服务、容器化、DevOps、持续交付', 'difficulty': 2},
                '云架构': {'desc': '高可用、高并发、弹性伸缩架构设计', 'difficulty': 2},
                '多云管理': {'desc': '跨云平台的统一管理和迁移', 'difficulty': 2},
                '成本优化': {'desc': '云资源成本分析和优化', 'difficulty': 2},
                '网络规划': {'desc': 'VPC、子网、安全组设计', 'difficulty': 2},
                '腾讯云': {'desc': '腾讯云产品架构和部署', 'difficulty': 2},
                '阿里云': {'desc': '国内主流云服务使用', 'difficulty': 2}
            }
        },
        '云运维工程师': {
            'description': '负责云平台运维，保证云服务的高可用性和性能。',
            'skills': {
                'Docker': {'desc': '容器运维和镜像管理', 'difficulty': 2},
                'Kubernetes': {'desc': 'K8s集群运维和故障排查', 'difficulty': 2},
                'Linux': {'desc': 'Linux服务器管理和运维', 'difficulty': 2},
                '云计算平台': {'desc': '主流云平台日常运维管理', 'difficulty': 2},
                '备份恢复': {'desc': '云数据备份和灾难恢复', 'difficulty': 2},
                '安全管理': {'desc': '云安全组、访问控制、密钥管理', 'difficulty': 2},
                '故障排查': {'desc': '云服务故障诊断和恢复', 'difficulty': 2},
                '日志管理': {'desc': 'ELK、Loki等日志收集和分析', 'difficulty': 2},
                '监控': {'desc': 'Prometheus、Grafana云资源监控和性能调优', 'difficulty': 2},
                '自动化运维': {'desc': 'Ansible、Puppet等自动化运维工具', 'difficulty': 2}
            }
        },
        '云原生工程师': {
            'description': '构建和维护云原生应用和基础设施。',
            'skills': {
                'ArgoCD': {'desc': 'K8s声明式持续交付工具', 'difficulty': 2},
                'CNI': {'desc': '容器网络接口和网络方案', 'difficulty': 2},
                'CSI': {'desc': '容器存储接口和存储方案', 'difficulty': 2},
                'Docker': {'desc': '容器技术原理和最佳实践', 'difficulty': 2},
                'GitOps': {'desc': '基于Git的持续交付模式', 'difficulty': 2},
                'Grafana': {'desc': '监控数据可视化', 'difficulty': 2},
                'Helm': {'desc': 'K8s包管理和应用部署', 'difficulty': 2},
                'Istio': {'desc': '服务网格，微服务流量管理', 'difficulty': 2},
                'Knative': {'desc': 'K8s无服务器框架', 'difficulty': 2},
                'Kubernetes': {'desc': '深度掌握K8s架构和原理', 'difficulty': 2},
                'Prometheus': {'desc': '云原生监控方案', 'difficulty': 2},
                'etcd': {'desc': '分布式键值存储', 'difficulty': 2},
                'Operator': {'desc': 'K8s Operator开发和运维', 'difficulty': 3}
            }
        }
    },
    '游戏开发': {
        'Unity开发工程师': {
            'description': '使用Unity引擎开发游戏，实现游戏逻辑和交互功能。',
            'skills': {
                'C#': {'desc': 'Unity主要编程语言，游戏逻辑开发', 'difficulty': 1},
                'UGUI': {'desc': 'Unity用户界面系统', 'difficulty': 2},
                'UI设计': {'desc': '游戏界面和交互设计', 'difficulty': 2},
                'Unity3D': {'desc': '跨平台游戏引擎使用，场景管理和资源管理', 'difficulty': 2},
                '动画系统': {'desc': 'Animator、Animation动画控制', 'difficulty': 2},
                '多平台发布': {'desc': 'iOS、Android、PC、WebGL发布', 'difficulty': 2},
                '寻路系统': {'desc': 'NavMesh导航网格', 'difficulty': 2},
                '游戏物理': {'desc': '物理引擎实现碰撞和运动效果', 'difficulty': 2},
                '物理引擎': {'desc': 'Rigidbody、Collider物理组件使用', 'difficulty': 2},
                '粒子系统': {'desc': '特效制作和粒子控制', 'difficulty': 2},
                '资源打包': {'desc': 'AssetBundle资源管理和热更新', 'difficulty': 2},
                'Shader': {'desc': 'ShaderLab编写自定义着色器', 'difficulty': 3},
                '性能优化': {'desc': 'DrawCall优化、资源管理、内存优化', 'difficulty': 3}
            }
        },
        'Unreal开发工程师': {
            'description': '使用Unreal引擎开发高质量游戏，负责图形渲染和性能优化。',
            'skills': {
                'C++': {'desc': 'Unreal核心编程语言，高性能开发', 'difficulty': 1},
                'AI行为树': {'desc': '游戏AI设计和实现', 'difficulty': 2},
                'UMG': {'desc': 'Unreal用户界面系统', 'difficulty': 2},
                'Unreal Engine': {'desc': 'Unreal游戏引擎深度使用', 'difficulty': 2},
                '光照系统': {'desc': '静态光照、动态光照、Lumen', 'difficulty': 2},
                '动画系统': {'desc': '动画蓝图和混合空间', 'difficulty': 2},
                '性能分析': {'desc': 'Unreal Insights性能分析工具', 'difficulty': 2},
                '材质系统': {'desc': 'Material Editor材质编辑', 'difficulty': 2},
                '游戏物理': {'desc': '物理模拟和角色控制', 'difficulty': 2},
                '网络同步': {'desc': '多人游戏网络架构', 'difficulty': 2},
                '蓝图': {'desc': 'Unreal可视化脚本编程', 'difficulty': 2},
                'Nanite': {'desc': '虚拟几何体系统', 'difficulty': 3},
                '图形渲染': {'desc': '渲染管线理解和优化', 'difficulty': 3}
            }
        },
        '游戏客户端工程师': {
            'description': '开发游戏客户端，实现游戏玩法和交互体验。',
            'skills': {
                'C++': {'desc': '游戏客户端高性能开发', 'difficulty': 1},
                'Lua': {'desc': '游戏脚本语言，热更新支持', 'difficulty': 1},
                'UI系统': {'desc': '游戏UI框架和布局', 'difficulty': 2},
                '任务系统': {'desc': '任务流程设计和状态管理', 'difficulty': 2},
                '存档系统': {'desc': '游戏数据持久化', 'difficulty': 2},
                '对象池': {'desc': '游戏对象复用和性能优化', 'difficulty': 2},
                '战斗系统': {'desc': '技能系统、伤害计算、碰撞检测', 'difficulty': 2},
                '游戏框架': {'desc': '游戏循环、状态机、事件系统', 'difficulty': 2},
                '热更新': {'desc': '资源热更新和代码热修复', 'difficulty': 2},
                '网络编程': {'desc': 'TCP/UDP、协议设计、网络同步', 'difficulty': 2},
                '资源管理': {'desc': '资源加载、缓存、释放策略', 'difficulty': 2},
                '图形学': {'desc': '渲染原理、坐标变换、光照模型', 'difficulty': 3}
            }
        },
        '游戏服务端工程师': {
            'description': '开发游戏服务器，处理游戏逻辑和数据同步。',
            'skills': {
                'C++': {'desc': '高性能游戏服务器开发', 'difficulty': 1},
                'Go': {'desc': '高并发游戏服务端开发', 'difficulty': 1},
                'Java': {'desc': '企业级游戏服务器开发', 'difficulty': 1},
                '数据库': {'desc': 'MySQL、Redis数据存储', 'difficulty': 1},
                '匹配系统': {'desc': '玩家匹配算法和房间管理', 'difficulty': 2},
                '压测优化': {'desc': '服务器性能测试和优化', 'difficulty': 2},
                '并发编程': {'desc': '多线程、协程、锁机制', 'difficulty': 2},
                '战斗校验': {'desc': '服务器端战斗逻辑验证', 'difficulty': 2},
                '消息队列': {'desc': 'Kafka、RabbitMQ异步处理', 'difficulty': 2},
                '网络编程': {'desc': 'Socket、TCP/UDP、IO多路复用', 'difficulty': 2},
                '防作弊': {'desc': '外挂检测和数据校验', 'difficulty': 2},
                '分布式系统': {'desc': '服务拆分、负载均衡、容错', 'difficulty': 3},
                '游戏同步': {'desc': '状态同步、帧同步、预测回滚', 'difficulty': 3}
            }
        }
    },
    '区块链': {
        '区块链开发工程师': {
            'description': '开发区块链应用和智能合约，构建去中心化系统。',
            'skills': {
                'Go': {'desc': '区块链底层开发，如Fabric、以太坊客户端', 'difficulty': 1},
                'Rust': {'desc': '高性能区块链开发，如Solana、Polkadot', 'difficulty': 1},
                'Solidity': {'desc': '以太坊智能合约开发语言', 'difficulty': 1},
                'DApp开发': {'desc': '去中心化应用前后端开发', 'difficulty': 2},
                'NFT': {'desc': '非同质化代币标准和应用', 'difficulty': 2},
                'Web3.js': {'desc': '与区块链交互的JavaScript库', 'difficulty': 2},
                '以太坊': {'desc': 'EVM原理、Gas机制、交易流程', 'difficulty': 2},
                '链上数据分析': {'desc': '区块链浏览器、事件监听', 'difficulty': 2},
                'DeFi': {'desc': '去中心化金融协议开发', 'difficulty': 3},
                '共识算法': {'desc': 'PoW、PoS、DPoS等共识机制', 'difficulty': 3},
                '密码学': {'desc': '哈希、签名、零知识证明', 'difficulty': 3},
                '智能合约': {'desc': '编写、测试、部署智能合约', 'difficulty': 3}
            }
        }
    },
    '大数据': {
        '大数据开发工程师': {
            'description': '开发大数据平台，处理海量数据的存储和计算。',
            'skills': {
                'ClickHouse': {'desc': '列式OLAP数据库', 'difficulty': 2},
                'Doris': {'desc': '国产MPP分析型数据库', 'difficulty': 2},
                'Flink': {'desc': '实时流处理框架', 'difficulty': 2},
                'HBase': {'desc': '分布式列式存储数据库', 'difficulty': 2},
                'Hadoop': {'desc': 'HDFS分布式存储和MapReduce计算', 'difficulty': 2},
                'Hive': {'desc': '数据仓库工具，SQL方式查询Hadoop数据', 'difficulty': 2},
                'Kafka': {'desc': '高吞吐量消息队列', 'difficulty': 2},
                'Spark': {'desc': '内存计算引擎，支持SQL、流处理、机器学习', 'difficulty': 2},
                '任务调度': {'desc': 'Airflow、DolphinScheduler', 'difficulty': 2},
                '数据治理': {'desc': '元数据管理、数据质量、血缘分析', 'difficulty': 2},
                '数据湖': {'desc': 'Delta Lake、Iceberg、Hudi', 'difficulty': 2},
                '资源调度': {'desc': 'YARN、Kubernetes', 'difficulty': 2},
                'SQL优化': {'desc': '大数据SQL查询优化', 'difficulty': 3}
            }
        }
    }
}

# 构建文本数据
for major, jobs in computer_data.items():
    for job, info in jobs.items():
        # 将技能字典转换为带描述和难度的格式
        skills_list = []
        skills_with_desc = []
        skills_with_difficulty = []
        for skill_name, skill_info in info['skills'].items():
            skills_list.append(skill_name)
            skills_with_desc.append(f"{skill_name}:{skill_info['desc']}")
            skills_with_difficulty.append(f"{skill_name}({skill_info['difficulty']})")
        
        text = f"专业：{major} | 岗位：{job} | 描述：{info['description']} | 技能：{', '.join(skills_list)}"
        texts.append(text)
        metadatas.append({
            'level1': '计算机',
            'level2': major,
            'level3': job,
            'level3_desc': info['description'],
            'level4': ', '.join(skills_list),
            'level4_desc': '; '.join(skills_with_desc),  # 技能详细描述
            'skills_difficulty': '; '.join(skills_with_difficulty)  # 技能难度信息
        })

# 添加医学（空）
texts.append('领域：医学')
metadatas.append({
    'level1': '医学',
    'level2': '',
    'level3': '',
    'level3_desc': '',
    'level4': ''
})

# 添加数据
resp = requests.post('http://localhost:8000/api/documents', json={
    'texts': texts,
    'metadatas': metadatas
})

# 查看向量库状态
info = requests.get('http://localhost:8000/api/collection/info')
print(f"添加文档数量: {len(texts)}")
if info.status_code == 200:
    print(f"向量库文档总数: {info.json().get('count', 'unknown')}")
