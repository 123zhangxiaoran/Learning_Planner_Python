"""后端开发工程师数据"""
data = {
    '计算机与信息技术': {
        '软件工程': {
            '后端开发工程师': {
            'description': '负责服务器端业务逻辑开发，设计和维护数据库API接口。',
            'skills': {
                'Go': {
                    'desc': 'Google开发的高性能语言，原生支持并发，适合高并发微服务',
                    'difficulty': 1,
                    'dimensions': [
                        ['基础语法', '数据类型', '流程控制', '函数', '方法'],
                        ['类型系统', '接口', '结构体', '类型断言', '类型别名', '泛型'],
                        ['并发编程', 'goroutine', '通道', 'select', 'context', 'sync包', '协程调度', 'CSP模型'],
                        ['错误处理', 'defer', 'panic', 'recover', '错误包装'],
                        ['包管理与模块', 'go mod'],
                        ['测试'],
                        ['反射', 'JSON处理', '正则表达式'],
                        ['HTTP服务', 'net/http', 'gin框架', 'gRPC'],
                        ['数据库', 'MySQL驱动', 'Redis客户端', '数据库事务', '连接池'],
                        ['日志与监控'],
                        ['标准库实用包', 'time包', 'io操作', '文件操作', '模板']
                    ]
                },
                'Java': {
                    'desc': '企业级后端开发主流语言，拥有Spring生态和丰富的类库支持',
                    'difficulty': 1,
                    'dimensions': [
                        ['基础语法', '数据类型', '流程控制'],
                        ['面向对象', '类', '对象', '封装', '继承', '多态', '抽象类', '接口', '内部类'],
                        ['异常处理'],
                        ['泛型'],
                        ['集合框架', 'List', 'Set', 'Map', 'ArrayList', 'LinkedList', 'HashMap', 'HashSet', 'HashTable', 'Iterator'],
                        ['Stream API', 'Lambda表达式', '方法引用', '函数式接口', 'Optional'],
                        ['并发编程', '线程基础', 'Thread', 'Runnable', 'Callable', 'Future', 'ExecutorService', '线程池', 'synchronized', 'volatile', '原子类', '并发容器', 'JUC包', 'ReentrantLock', 'CountDownLatch', 'CyclicBarrier'],
                        ['I/O流', 'NIO', 'File操作'],
                        ['网络编程', 'TCP', 'UDP'],
                        ['注解', '反射'],
                        ['序列化', 'XML', 'JSON'],
                        ['JVM', '类加载器', '内存模型', '垃圾回收', '参数调优'],
                        ['构建与测试', 'Maven', 'Gradle', '单元测试'],
                        ['设计模式']
                    ]
                },
                'Linux': {
                    'desc': '服务器操作系统，掌握常用命令和系统管理',
                    'difficulty': 1,
                    'dimensions': [
                        ['文件命令', 'xargs命令', '软链接'],
                        ['文本处理', '管道重定向', '正则表达式', '三剑客'],
                        ['用户权限'],
                        ['进程管理'],
                        ['网络命令'],
                        ['磁盘管理'],
                        ['压缩解压'],
                        ['系统服务'],
                        ['定时任务'],
                        ['SSH远程连接'],
                        ['文本编辑器(vim/nano)'],
                        ['Shell脚本', '环境变量', 'Shell函数', '条件判断', '循环', '脚本调试'],
                        ['软件包管理'],
                        ['日志查看'],
                        ['系统资源查看'],
                        ['网络配置'],
                        ['防火墙'],
                        ['DNS与主机名配置'],
                        ['终端复用器(screen/tmux)']
                    ]
                },
                'MySQL': {
                    'desc': '最流行的开源关系型数据库，用于结构化数据的持久化存储和查询',
                    'difficulty': 1,
                    'dimensions': [
                        ['DDL建库建表', 'DML增删改查', 'DQL查询', '数据类型'],
                        ['约束'],
                        ['索引类型', '普通索引', '唯一索引', '复合索引'],
                        ['Explain执行计划', 'SQL优化', '优化器', 'ICP', 'MRR', 'BKA', '索引下推'],
                        ['连接', '子查询', '分组聚合', '排序', '去重'],
                        ['事务', '隔离级别', 'MVCC', '锁'],
                        ['redo log', 'undo log', 'binlog', '慢查询日志'],
                        ['分页查询', 'NULL处理', 'IFNULL', 'COALESCE', 'CASE WHEN'],
                        ['存储过程', '触发器', '视图', '字符集', '编码', 'UTF8MB4'],
                        ['并发控制', '连接池', '主从复制', '读写分离'],
                        ['备份恢复', 'mysqldump', 'performance_schema', 'information_schema'],
                        ['前缀索引', '覆盖索引', '最左前缀原则']
                    ]
                },
                'PostgreSQL': {
                    'desc': '功能强大的开源关系型数据库，支持高级数据类型和复杂查询',
                    'difficulty': 1,
                    'dimensions': [
                        ['SQL基础', '数据类型', '表创建管理', '约束'],
                        ['索引与查询优化', '索引', '执行计划', '查询优化'],
                        ['高级查询', '连接', '子查询', '公用表表达式', '窗口函数', '聚合函数'],
                        ['数组/JSON/全文搜索', '数组操作', 'JSON', 'JSONB', '全文搜索'],
                        ['事务与并发控制', '事务', 'MVCC', '并发控制', '锁'],
                        ['数据库对象', '存储过程', '函数', '触发器', '规则', '视图', '物化视图', '继承', '序列', '自增列'],
                        ['分区表', '分区表'],
                        ['自定义类型', '自定义类型', '枚举类型', '域类型'],
                        ['模式与权限', '模式', '权限控制'],
                        ['备份与恢复', '备份', '恢复'],
                        ['性能监控与优化', '性能监控', 'pg_stat_activity', 'pg_stat_statements', '性能优化'],
                        ['复制', '复制配置', '流复制', '逻辑复制'],
                        ['扩展插件', '扩展插件', 'PostGIS'],
                        ['数据导入导出', 'COPY导入导出']
                    ]
                },
                'Python': {
                    'desc': '简洁高效的后端开发语言，适合快速开发和数据处理场景',
                    'difficulty': 1,
                    'dimensions': [
                        ['基础语法', '数据类型', '流程控制', '函数定义', '参数传递', '匿名函数'],
                        ['数据结构', '列表', '字典', '推导式', '生成器', '迭代器', '字符串操作'],
                        ['面向对象', '类与对象', '继承', '多态', '特殊方法'],
                        ['装饰器', '闭包'],
                        ['异常处理'],
                        ['模块与包管理', '模块导入', 'pip', '虚拟环境'],
                        ['文件操作'],
                        ['类型注解'],
                        ['数据格式', 'JSON', 'CSV', '正则表达式', '日期时间处理'],
                        ['并发编程', '多线程', '多进程', '协程', 'async/await', 'aiohttp'],
                        ['网络编程', 'socket', 'requests'],
                        ['数据库与ORM', 'psycopg2', 'pymysql', 'sqlalchemy'],
                        ['Web框架', 'Django', 'Flask', 'FastAPI'],
                        ['API开发', '接口文档', '中间件', '认证授权', '序列化'],
                        ['测试', '单元测试', 'pytest'],
                        ['日志'],
                        ['内存与运行时', '垃圾回收', '全局解释器锁', '深拷贝', '浅拷贝'],
                        ['安全与加密', 'hashlib', 'cryptography']
                    ]
                },
                'RESTful API': {
                    'desc': '基于HTTP的API设计规范，使用JSON进行数据交换',
                    'difficulty': 1,
                    'dimensions': [
                        ['HTTP方法'],
                        ['URI规范', '资源命名'],
                        ['状态码'],
                        ['请求头', '响应头'],
                        ['请求体', '响应体', 'JSON数据格式'],
                        ['分页', '过滤', '排序', '字段筛选'],
                        ['错误处理'],
                        ['HATEOAS', '幂等性', '安全性'],
                        ['跨域', '缓存控制', '速率限制'],
                        ['API文档'],
                        ['REST约束', 'Richardson成熟度模型'],
                        ['GraphQL对比', 'gRPC对比', 'REST API设计原则'],
                        ['URL设计', '查询参数', '路径参数'],
                        ['请求验证', '响应封装', '统一响应格式'],
                        ['版本管理'],
                        ['认证方式', 'token刷新', 'OAuth2'],
                        ['API网关', '负载均衡', '超时处理', '重试机制']
                    ]
                },
                '单元测试': {
                    'desc': 'JUnit、pytest等测试框架，编写自动化测试保证代码质量',
                    'difficulty': 1,
                    'dimensions': [
                        ['测试金字塔', '测试驱动开发', '行为驱动开发'],
                        ['端到端测试'],
                        ['集成测试'],
                        ['性能测试'],
                        ['测试类型', '压力测试', '冒烟测试', '回归测试', '探索性测试'],
                        ['测试替身', '模拟', '桩', '间谍'],
                        ['JUnit', '注解', '断言', '异常测试', '参数化测试'],
                        ['Mockito', '模拟', 'Spy', 'Stub', '测试隔离'],
                        ['pytest', '断言', 'fixture', '参数化', 'mock', 'patch'],
                        ['unittest', 'TestCase', 'setUp', 'tearDown', 'assert方法', 'subTest'],
                        ['测试覆盖', 'CI集成'],
                        ['测试报告'],
                        ['测试数据'],
                        ['契约测试']
                    ]
                },
                'Django': {
                    'desc': 'Python全栈Web框架，内置ORM、管理后台、认证系统等完整功能',
                    'difficulty': 2,
                    'dimensions': [
                        ['MTV架构', '项目创建', '应用', 'URLconf'],
                        ['视图', 'Request', 'Response'],
                        ['模板', '模板语法', '模板标签过滤器'],
                        ['ORM模型', '字段类型', '字段选项', '查询集', '过滤器', 'Q对象', 'F表达式', '聚合函数'],
                        ['跨表查询', 'select_related', 'prefetch_related', '分页'],
                        ['Admin后台', 'Admin自定义'],
                        ['表单', 'ModelForm', '表单验证'],
                        ['中间件', '会话', 'Cookie', '缓存', '消息框架'],
                        ['认证', '用户模型扩展', '权限', '分组', 'CSRF防护'],
                        ['静态文件', '文件上传', '迁移'],
                        ['基于类的视图', '基于函数的视图', '混合', '通用视图'],
                        ['信号', '信号处理器', '表单集'],
                        ['Django REST Framework', '序列化器', '视图集', '路由', '分页', '过滤', '搜索'],
                        ['认证类', '权限类', '限流'],
                        ['Celery异步任务'],
                        ['日志配置'],
                        ['settings配置'],
                        ['部署', 'gunicorn', 'uWSGI', 'Nginx反向代理'],
                        ['生产环境配置'],
                        ['安全设置'],
                        ['跨域CORS'],
                        ['国际化']
                    ]
                },
                'Docker': {
                    'desc': '容器化技术，将应用及其依赖打包为可移植的容器镜像',
                    'difficulty': 2,
                    'dimensions': [
                        ['Docker安装', '镜像', '容器', '镜像仓库'],
                        ['Dockerfile', '基础指令', '指令优化', '层缓存', '.dockerignore'],
                        ['构建上下文', '镜像分层', '多阶段构建'],
                        ['Docker Compose', 'docker-compose.yml', '服务编排'],
                        ['Docker网络', '网络模式', 'DNS服务发现'],
                        ['容器配置', '数据卷', '挂载', '端口映射', '环境变量', '容器互联'],
                        ['容器运维', '日志驱动', '资源限制', '健康检查', '重启策略', '容器监控'],
                        ['Docker Swarm', 'Docker Hub', '镜像加速器', 'Harbor私有仓库', '镜像安全扫描'],
                        ['镜像优化', 'Dockerfile最佳实践', '镜像压缩优化', 'distroless镜像', 'alpine镜像'],
                        ['安全配置', '权限配置', 'rootless', 'Seccomp', 'AppArmor', 'Docker API', '远程管理'],
                        ['镜像管理', '镜像tag', '推送拉取'],
                        ['Docker-machine'],
                        ['CI/CD集成', 'Jenkins集成', 'GitHub Actions', 'Kubernetes']
                    ]
                },
                'Elasticsearch': {
                    'desc': '分布式搜索和分析引擎，用于全文搜索和日志分析',
                    'difficulty': 2,
                    'dimensions': [
                        ['索引与文档', '索引', '文档', 'CRUD', '批量操作'],
                        ['映射管理', '映射', '动态映射', '显式映射', '字段类型', '别名', '索引模板'],
                        ['文本分析', '分词器', '倒排索引'],
                        ['搜索', 'DSL查询', '过滤', '全文搜索', '精确查询'],
                        ['聚合'],
                        ['搜索特性', '分页', '排序', '高亮', '自动补全'],
                        ['搜索扩展', '拼音搜索', '同义词搜索'],
                        ['相关性优化', '评分', 'TF-IDF', 'BM25', 'boosting', '权重调整'],
                        ['集群与高可用', '节点', '集群', '分片', '副本', '冷热分离', '故障转移', '脑裂问题'],
                        ['备份与恢复', '快照', '跨集群搜索'],
                        ['监控与性能', '监控', '性能优化', 'ES客户端', '连接池', '批量写入', '写入优化', '搜索优化', '缓存', 'segment合并']
                    ]
                },
                'FastAPI': {
                    'desc': '现代Python Web框架，基于类型提示，自动生成OpenAPI文档',
                    'difficulty': 2,
                    'dimensions': [
                        ['路由与请求', '路由装饰器', '路径参数', '查询参数', '请求方法', '请求体模型'],
                        ['响应处理', '响应模型', '状态码', 'HTTP异常', '响应参数', '流式响应', '文件上传下载', 'Cookie', 'Headers'],
                        ['依赖注入与安全', '依赖注入', 'OAuth2密码模式', 'JWT认证', '安全机制'],
                        ['中间件与跨域', '中间件', '跨域'],
                        ['异步与后台任务', '异步', 'BackgroundTasks', 'WebSocket'],
                        ['数据库集成', 'SQLAlchemy', 'ORM操作', '异步数据库', '事务', '数据库迁移'],
                        ['参数验证', '字段校验', '嵌套模型', '列表字段', '可选字段', '默认值', '枚举类型', '自定义验证器'],
                        ['测试与文档', 'TestClient', 'pytest', '自动文档', 'OpenAPI'],
                        ['路由高级', '标签', '分组路由', '应用生命周期'],
                        ['配置与日志', '配置', '日志', '环境变量'],
                        ['部署与性能', '部署', 'uvicorn', 'gunicorn', 'Docker', 'nginx', 'HTTPS', '缓存', '限流'],
                        ['静态文件与模板', '静态文件', 'Jinja2模板']
                    ]
                },
                'GraphQL': {
                    'desc': '灵活的API查询语言，客户端可精确获取所需数据',
                    'difficulty': 2,
                    'dimensions': [
                        ['类型系统', '对象类型', '字段', '标量类型', '枚举类型', '接口', '联合类型', '输入类型'],
                        ['操作', '查询', '变更'],
                        ['解析器', '字段解析', '上下文', '参数传递'],
                        ['查询执行与优化', '查询验证', '查询执行', 'N+1问题', 'DataLoader'],
                        ['分页', 'Cursor分页', 'Offset分页', 'Relay规范', 'Connection规范'],
                        ['碎片', '内省', '变量', '指令', '内建指令'],
                        ['错误处理与开发工具', '错误扩展', 'GraphQL Playground', 'GraphiQL'],
                        ['Apollo生态', 'Apollo Server', 'Apollo Client', 'Apollo Federation'],
                        ['Schema设计与管理', '版本化', '认证授权', '权限控制', 'JWT集成', '字段级权限'],
                        ['性能与监控', '缓存策略', '性能监控', '查询复杂度分析', '限流'],
                        ['订阅与实时推送', '订阅', 'WebSocket', '实时推送'],
                        ['代码生成与类型生成', '代码优先', 'Schema优先'],
                        ['框架集成', 'NestJS集成', 'FastAPI集成', 'Django集成', 'Spring Boot集成', '批量操作', '文件上传']
                    ]
                },
                'JWT认证': {
                    'desc': 'JSON Web Token，用于无状态的用户身份验证',
                    'difficulty': 2,
                    'dimensions': [
                        ['JWT结构'],
                        ['签名算法'],
                        ['密钥与Token操作'],
                        ['标准声明'],
                        ['Token生命周期'],
                        ['认证架构'],
                        ['客户端存储与安全'],
                        ['请求头与传输安全'],
                        ['安全强化'],
                        ['最佳实践'],
                        ['多语言库'],
                        ['认证流程']
                    ]
                },
                'Kafka': {
                    'desc': '高吞吐量分布式流处理平台，用于实时数据传输和处理',
                    'difficulty': 2,
                    'dimensions': [
                        ['消息队列模式', '发布订阅', '主题', '分区', '副本', 'ISR'],
                        ['Leader', 'Follower', '生产者', '消费者', 'Consumer Group'],
                        ['消息顺序', '消息偏移', '消费位移', '自动提交', '手动提交', '消费模式'],
                        ['Exactly Once', 'At Least Once', 'At Most Once'],
                        ['消息压缩', 'snappy', 'gzip', 'lz4', 'zstd', '消息路由', '分区策略', 'key路由', '粘性分区'],
                        ['幂等性', '事务消息', '幂等Producer', 'acks配置', '重试', '拦截器'],
                        ['序列化', 'JSON', 'Avro', 'Protobuf', 'Schema Registry'],
                        ['连接器', 'Source Connector', 'Sink Connector', '流处理', 'Kafka Streams'],
                        ['状态存储', '窗口计算', 'KSQL'],
                        ['集群架构', '控制器', '选举机制', '副本分配', '再平衡'],
                        ['分区分配策略', '消费者协调', '协调器', 'offset管理'],
                        ['监控JMX', 'Kafka Manager', 'Kafka Eagle', 'Kafka UI'],
                        ['性能调优', '吞吐量优化', '延迟优化', '磁盘优化', '网络优化'],
                        ['Spring Kafka', 'Python kafka-python', 'confluent-kafka', 'Go segment', 'kafka-go', 'Java KafkaClient'],
                        ['Spring Cloud Stream', 'Flink集成', 'Spark Streaming集成'],
                        ['消费者组偏移量', '消息积压', '消费者停滞', '重复消费', '消息丢失']
                    ]
                },
                'MongoDB': {
                    'desc': '文档型NoSQL数据库，适合存储非结构化和半结构化数据',
                    'difficulty': 2,
                    'dimensions': [
                        ['文档', '集合', '数据库', 'BSON格式', 'ObjectId'],
                        ['数据类型'],
                        ['插入', 'insertMany', '查询', 'findOne'],
                        ['查询条件'],
                        ['投影', '排序', '分页', 'limit', '游标'],
                        ['更新', 'updateMany', 'upsert', '更新操作符', '数组更新'],
                        ['删除', 'deleteMany'],
                        ['聚合管道', '$match', '$group', '$project', '$sort', '$limit', '$skip', '$lookup', '$unwind', '$addFields', '$replaceRoot', '聚合表达式'],
                        ['索引', '单字段索引', '复合索引', '多键索引', '文本索引', '地理空间索引', '唯一索引', '稀疏索引', 'TTL索引', '索引管理'],
                        ['执行计划', '慢查询日志', '写入', '读取'],
                        ['副本集', '主从复制', '选举', '分片', '分片键', '哈希分片', '范围分片', '均衡器', 'Chunks'],
                        ['事务', 'Sessions', 'Change Stream'],
                        ['存储引擎', 'WiredTiger缓存', '压缩'],
                        ['认证授权', '角色', '用户管理', '备份', '恢复', '导入导出'],
                        ['监控', 'MongoDB Compass', '性能优化', '连接池', 'PyMongo', 'Mongoose', 'Spring Data MongoDB']
                    ]
                },
                'Nginx': {
                    'desc': '高性能Web服务器和反向代理，用于负载均衡和静态资源服务',
                    'difficulty': 2,
                    'dimensions': [
                        ['安装配置', 'nginx.conf主配置', '全局块', 'events块', 'http块', 'server块', 'location块'],
                        ['静态资源服务', '反向代理proxy_pass'],
                        ['负载均衡upstream', '轮询', '权重', 'ip_hash', 'least_conn', '长连接', '健康检查'],
                        ['HTTP服务器', '监听端口', '域名', '根目录', '默认页', 'try_files'],
                        ['重定向rewrite', 'redirect', 'permanent', 'temp', '正则rewrite', 'return', '301', '302', '强制HTTPS', 'www重定向'],
                        ['SSL/TLS配置', 'HTTPS证书', 'SSL证书配置', 'HTTP/2', 'TLS版本', 'TLS握手', 'HSTS', 'OCSP stapling'],
                        ['gzip压缩', 'gzip_types', 'gzip_static'],
                        ['缓存配置', 'expires', 'Cache-Control', 'proxy_cache'],
                        ['反向代理头proxy_set_header', 'X-Real-IP', 'X-Forwarded-For'],
                        ['WebSocket代理', 'proxy_http_version 1.1', 'Upgrade头', '连接升级'],
                        ['限流limit_req', 'limit_conn', '漏桶算法', '令牌桶'],
                        ['IP白名单', '黑名单', 'allow', 'deny'],
                        ['日志配置', 'access_log', 'error_log', '日志格式', 'JSON日志', '日志切割', 'logrotate'],
                        ['进程管理', '信号控制', '热重载', '测试配置nginx -t'],
                        ['性能优化', 'worker进程', 'worker_connections', '多核利用', 'sendfile', 'tcp_nopush', 'tcp_nodelay', '缓冲区大小'],
                        ['超时配置', 'keepalive_timeout', 'client_header_buffer_size', 'body大小限制', '请求超时', '反向代理超时'],
                        ['FastCGI', 'php-fpm', 'Python', 'uWSGI', 'Node.js'],
                        ['location优先级', '正则匹配', '精确匹配', '前缀匹配', 'Rewrite规则', 'if判断'],
                        ['安全头', 'X-Frame-Options', 'X-Content-Type-Options', 'X-XSS-Protection', 'Content-Security-Policy', 'Referrer Policy'],
                        ['监控', 'status模块', 'Prometheus', 'lua模块', 'openresty', 'stream模块', 'TCP代理', 'UDP代理']
                    ]
                },
                'OAuth2': {
                    'desc': '开放授权协议，支持第三方登录和API访问授权',
                    'difficulty': 2,
                    'dimensions': [
                        ['OAuth2角色'],
                        ['授权流程', '授权码', '隐式授权', '密码凭证', '客户端凭证'],
                        ['刷新令牌', '访问令牌', '范围', '状态参数'],
                        ['PKCE防CSRF', 'code_verifier', 'code_challenge', 'code_challenge_method'],
                        ['authorization_endpoint', 'token_endpoint', 'revocation_endpoint', 'introspection_endpoint'],
                        ['JARM JWT Secured Authorization Response Mode', 'JWT作为令牌', 'JWT Bearer', 'JWKs', 'jwks_uri'],
                        ['JWT验证', 'JWKS缓存'],
                        ['授权服务器', '客户端注册', 'client_id', 'client_secret', 'redirect_uri'],
                        ['授权页', '登录页', '同意页', '令牌生成', '令牌存储', '令牌撤销', '令牌刷新', '刷新策略'],
                        ['GitHub OAuth', 'Google OAuth', '微信OAuth', '微博OAuth', '钉钉OAuth', '支付宝OAuth'],
                        ['单点登录', 'OpenID Connect', 'ID Token', 'UserInfo端点', 'Discovery文档'],
                        ['JWT配置文件', '授权服务器实现', 'Spring Security OAuth2', 'Authlib', 'oauthlib'],
                        ['社交登录', '第三方登录', '联合登录', '登录流程设计'],
                        ['安全考虑', 'CSRF防护', '重放攻击防护', '令牌安全存储', '传输安全']
                    ]
                },
                'RabbitMQ': {
                    'desc': '消息队列中间件，实现应用解耦和异步任务处理',
                    'difficulty': 2,
                    'dimensions': [
                        ['AMQP协议', '消息', '消息属性'],
                        ['队列', '队列属性'],
                        ['交换机', '交换机类型', '绑定', '路由键'],
                        ['生产者', '消费者', 'basic_publish', 'basic_consume'],
                        ['basic_ack', 'basic_nack', 'basic_reject', '手动确认', '自动确认'],
                        ['QoS预取', 'prefetch_count', 'prefetch_size', '公平调度'],
                        ['消息持久化', 'publisher confirms', '事务', '发送方确认', 'mandatory标志'],
                        ['备份交换机', '死信队列'],
                        ['TTL消息过期', '队列TTL', '延迟队列', '延迟插件'],
                        ['优先级队列', '消息顺序', '消息优先级', '幂等性'],
                        ['重复消费', '消费确认', '消费模式', '推拉模式', '多消费者'],
                        ['集群', '镜像队列', '仲裁队列', '负载均衡', '故障转移', '联邦', 'Shovels'],
                        ['管理界面', 'rabbitmqadmin', '监控', 'Prometheus插件', 'HTTP API', 'Web管理插件'],
                        ['虚拟主机', '权限控制', '用户权限', '访问控制'],
                        ['Spring AMQP', 'pika', 'java-javax-amqp', 'Go amqp091-go'],
                        ['消息堆积', '消费能力', '重试机制', '补偿机制', '最终一致性', '可靠投递', '消费幂等', '顺序消息', '延迟消息', '事务消息']                      
                    ]
                },
                'Redis': {
                    'desc': '高性能内存键值存储，用作缓存、会话存储和消息队列',
                    'difficulty': 2,
                    'dimensions': [
                        ['数据类型'],
                        ['通用键操作'],
                        ['发布订阅'],
                        ['高级数据结构'],
                        ['管道与Lua脚本'],
                        ['事务'],
                        ['持久化'],
                        ['主从复制'],
                        ['哨兵模式'],
                        ['Redis集群'],
                        ['客户端与连接池'],
                        ['分布式锁'],
                        ['缓存策略与问题'],
                        ['内存淘汰与优化'],
                        ['运维与监控'],
                        ['安全配置']                    
                    ]
                },
                'Spring Boot': {
                    'desc': 'Java生态的简化开发框架，提供自动配置和开箱即用的微服务支持',
                    'difficulty': 2,
                    'dimensions': [
                        ['自动配置', 'Starter依赖', 'spring-boot-starter', '@SpringBootApplication', 'main方法', '打包jar'],
                        ['嵌入式服务器Tomcat', 'Undertow', 'Jetty'],
                        ['application.yml', 'properties', '配置文件加载顺序', '环境变量', '命令行参数'],
                        ['多环境', '@ActiveProfile'],
                        ['Spring Boot Actuator', 'actuator端点', 'health', 'info', 'metrics', '健康检查', '自定义端点'],
                        ['Spring Boot DevTools', '热重载', 'LiveReload', '依赖管理', 'parent继承', '版本仲裁'],
                        ['Web开发', '@RestController', '@Controller', '@RequestMapping', '@GetMapping', '@PostMapping'],
                        ['路径变量', '查询参数', '@RequestParam', '@RequestBody', '响应体', 'JSON处理', 'Jackson', 'Gson', '日期格式化'],
                        ['国际化', '静态资源', 'webjars', '模板引擎Thymeleaf', 'FreeMarker'],
                        ['数据访问JdbcTemplate', 'JPA', 'Hibernate', 'MyBatis', 'Spring Data JPA', 'Redis', 'MongoDB'],
                        ['事务管理@Transactional', '声明式事务', '编程式事务', '传播行为', '隔离级别', '回滚规则'],
                        ['异常处理@ExceptionHandler', '@ControllerAdvice', '全局异常处理', '自定义异常', '错误页面'],
                        ['日志配置logback-spring.xml', '日志级别', '日志格式', '日志输出', '文件日志', '滚动日志'],
                        ['Lombok', '@Data', '@Getter', '@Setter', '@NoArgsConstructor', '@AllArgsConstructor', '@Builder', '@Slf4j'],
                        ['安全Spring Security', 'OAuth2', 'JWT', '认证授权', '密码加密', 'CSRF', 'CORS'],
                        ['过滤器', '拦截器', '监听器', '启动监听器', 'ApplicationRunner', 'CommandLineRunner'],
                        ['事件机制ApplicationEvent', '@EventListener'],
                        ['异步执行@Async', '@EnableAsync', '线程池配置', '定时任务@Scheduled', '@EnableScheduling'],
                        ['缓存Spring Cache', 'EhCache', 'Caffeine', 'Redis缓存', '缓存注解', '@Cacheable', '@CachePut', '@CacheEvict'],
                        ['单元测试@SpringBootTest', 'MockMvc', '切片测试', 'WebMvcTest', 'DataJpaTest'],
                        ['数据库连接池HikariCP', 'Druid'],
                        ['监控Prometheus', 'Grafana', 'micrometer'],
                        ['链路追踪zipkin', 'Sleuth', 'SkyWalking'],
                        ['部署jar', 'war', 'Docker', 'Kubernetes', '多环境配置', 'bootstrap.yml'],
                        ['配置中心Spring Cloud Config', 'Nacos', '注册中心Eureka', 'Nacos'],
                        ['服务发现', '客户端负载均衡Feign', 'OpenFeign'],
                        ['熔断器Sentinel', 'Resilience4j', '限流', '降级']                      
                    ]
                },
                'Spring Cloud': {
                    'desc': '微服务架构解决方案，提供服务注册、配置中心、网关等组件',
                    'difficulty': 2,
                    'dimensions': [
                        ['微服务架构', '服务拆分', '服务治理'],
                        ['服务注册发现', 'Nacos', 'Consul', 'Zookeeper', '心跳机制', '自我保护', '服务下线'],
                        ['客户端负载均衡', 'LoadBalancer', 'RoundRobin', 'Random', 'Weighted', 'Retry'],
                        ['服务调用', 'OpenFeign', '声明式HTTP客户端'],
                        ['熔断与降级', 'Resilience4j', 'Sentinel', '熔断规则', '降级处理', '限流', '流量控制'],
                        ['配置中心', 'Nacos', 'Apollo', '配置刷新', '热加载', 'Git配置', 'SVN配置'],
                        ['API网关', 'Spring Cloud Gateway', 'Zuul', '路由转发', '动态路由', '路由断言'],
                        ['认证授权', 'JWT验证', 'Token验证', '白名单', '黑名单', '限流', '令牌桶', '滑动窗口', '熔断'],
                        ['跨域配置', '白名单', '黑名单', 'IP限流', '限流算法', '令牌桶', '滑动窗口', '漏桶算法'],
                        ['链路追踪', 'Zipkin', 'SkyWalking', 'Jaeger', 'TraceId', 'SpanId'],
                        ['日志与监控', 'ELK', 'Actuator', 'Prometheus', 'Grafana', '监控面板'],
                        ['分布式事务', 'Seata', 'AT模式', 'TCC模式', 'Saga模式', 'XA模式'],
                        ['消息队列', 'RabbitMQ', 'Kafka', 'RocketMQ', '可靠消息', '事务消息', '消息确认', '消息补偿', '批量消息', '延迟消息', '顺序消息', '幂等性', '消息积压', '消息丢失'],
                        ['服务网格', 'Istio', 'Envoy', 'Sidecar', '流量管理', '灰度发布', '蓝绿部署', '金丝雀发布', 'A/B测试'],
                        ['容器化部署', 'Docker', 'Kubernetes', 'Helm', 'YAML', '部署配置', '弹性伸缩', '滚动更新'],
                        ['健康检查与配置', '就绪探针', '存活探针', '环境变量', 'ConfigMap', 'Secret'],
                        ['架构设计', '领域驱动设计', 'CQRS', '事件溯源', 'Saga模式'],
                        ['API设计', '契约测试', '文档', 'OpenAPI']                      
                    ]
                },
                'gRPC': {
                    'desc': '高性能RPC框架，基于Protocol Buffers进行服务间通信',
                    'difficulty': 2,
                        'dimensions': [
                        ['Protocol Buffers基础', '.proto文件', '消息定义', '字段类型', '字段编号', '默认值', '枚举', '嵌套消息', '导入'],
                        ['包管理', '包名', '选项', '服务定义', 'rpc方法'],
                        ['流式RPC', '一元', '服务端流', '客户端流', '双向流'],
                        ['HTTP/2', '多路复用', '头部压缩', '双向流', '连接复用'],
                        ['编译与代码生成', 'IDL', 'proto编译', 'protoc', 'protoc-gen-go', 'protoc-gen-java', 'protoc-gen-python', '生成代码'],
                        ['语言实现', 'Go gRPC', 'Java gRPC', 'Python gRPC', 'JavaScript gRPC'],
                        ['服务端开发', 'grpc.Server', 'RegisterService', 'Serve', 'StreamingHandler'],
                        ['客户端开发', 'grpc.Dial', 'NewStub', '调用方法', '阻塞调用', '非阻塞调用', '流式调用'],
                        ['元数据', 'metadata.New', 'metadata.Pairs', 'context传递'],
                        ['传输安全', 'TLS', 'SSL', '证书配置', '双向TLS', 'token认证'],
                        ['拦截器', 'UnaryInterceptor', 'StreamingInterceptor', '服务端拦截器', '客户端拦截器', '日志拦截器', '监控拦截器', '认证拦截器', '错误处理'],
                        ['可靠性机制', '重试机制', '超时设置', 'context超时', '截止时间', '负载均衡', 'pick_first', 'grpclb', '自定义负载均衡', '连接管理', '心跳', '健康检查', '连接池', 'Channel池'],
                        ['反射与健康检查服务', 'gRPC Reflection', 'Server Reflection', '健康检查服务', 'ProtoReflection'],
                        ['开发工具', 'grpcurl', 'BloomRPC', 'Postman', '拦截器链', '验证器', 'protovalidate', '自定义验证'],
                        ['HTTP & JSON 转码', 'JSON映射', 'JSON转码', 'HTTP规则', 'rest transcoding', 'gRPC-JSON', 'Swagger文档', 'OpenAPI导出'],
                        ['最佳实践', '命名规范', '错误规范', '超时规范', '重试规范', '日志规范', '监控规范', 'Proto风格', '向后兼容', '可选字段', '字段演进'],                      
                    ]
                }
            }
        },
    }
    }
}
