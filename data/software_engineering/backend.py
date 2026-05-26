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
                        ['基础语法', '数据类型', '流程控制', '函数', 'defer'],
                        ['类型系统', '结构体', '方法', '接口', '类型断言', '类型别名', '泛型'],
                        ['错误处理', 'error接口', '错误包装', 'errors.Is/As', 'panic/recover'],
                        ['并发编程', 'goroutine', '通道', 'select', 'sync包', 'context', 'CSP模型'],
                        ['工程化与测试', 'go mod', '包导入', 'internal包', '单元测试', '基准测试', '示例测试', '测试覆盖率'],
                        ['反射与底层', '反射', 'unsafe'],
                        ['标准库核心', 'time包', 'io与文件操作', '文本模板', '正则表达式', 'JSON处理', '标准日志'],
                        ['Web与RPC', 'net/http', '路由与中间件', 'Web框架概览', 'gRPC/RPC'],
                        ['数据库访问', '连接池/事务', 'SQL驱动', 'NoSQL示例'],
                        ['可观测性', '结构化日志', '监控指标', 'pprof性能分析']                     
                    ]
                },
                'Java': {
                    'desc': '企业级后端开发主流语言，拥有Spring生态和丰富的类库支持',
                    'difficulty': 1,
                    'dimensions': [
                        ['基础语法', '数据类型', '运算符', '流程控制', '数组', '方法定义与重载', '字符串处理'],
                        ['面向对象编程', '类与对象', '封装与继承', '多态', '抽象类与接口', '内部类', '枚举与记录类', 'Object通用方法'],
                        ['异常处理', '异常体系', 'try-catch-finally', 'throw与throws', '受检与非受检异常', 'try-with-resources', '异常链与日志'],
                        ['泛型', '泛型类与接口', '泛型方法', '类型擦除', '通配符与边界', 'PECS原则'],
                        ['集合框架', 'Collection与Map接口', 'List与ArrayList', 'Set与HashSet', 'Map与HashMap', 'TreeMap与排序', '迭代器', 'Collections工具类'],
                        ['函数式与Stream', 'Lambda表达式', '函数式接口', '方法引用', 'Stream创建与操作', 'Optional', 'Collectors收集器'],
                        ['并发编程', '线程与Runnable', 'Callable与Future', 'Executor线程池', 'synchronized与volatile', 'Lock与原子类', '并发集合', '同步工具类', 'CompletableFuture', '虚拟线程'],
                        ['I/O与序列化', '字节流与字符流', '缓冲流', 'NIO基础(Buffer/Channel)', 'Path与Files', 'Java序列化', 'JSON处理(Jackson)', 'XML处理简介'],
                        ['网络编程', 'Socket与TCP/UDP', 'NIO网络模型', 'HTTP客户端', 'Netty框架简介'],
                        ['反射与注解', '反射基础', 'Class与Method', '动态代理', '注解定义与元注解', '编译时注解处理器'],
                        ['JVM与调优', '类加载与双亲委派', '运行时数据区域', '垃圾回收算法与收集器', '常用JVM参数', '内存泄漏与性能分析工具'],
                        ['构建与工程化', 'Maven与Gradle', '单元测试(JUnit5)', 'Mockito', '测试覆盖率', '代码质量工具', 'JPMS模块系统'],
                        ['数据库访问', 'JDBC基础', '连接池(HikariCP)', '事务管理', 'JPA/Hibernate简介', 'MyBatis简介', 'NoSQL示例(Redis)'],
                        ['设计模式与原则', 'SOLID原则', '单例/工厂模式', '代理/观察者模式', '策略/模板方法模式'],
                        ['日志与可观测性', 'SLF4J与Logback', 'MDC跟踪', 'Micrometer指标', 'JFR性能记录', '分布式追踪概念'],
                        ['Web开发入门', 'Servlet与Tomcat', 'Spring Boot入门', 'RESTful API', '拦截器与过滤器', '安全基础(Spring Security)']
                    ]
                },
                'Linux': {
                    'desc': '服务器操作系统，掌握常用命令和系统管理',
                    'difficulty': 1,
                    'dimensions': [
                        ['文件与目录管理', 'ls/cd/cp/mv/rm', 'mkdir与通配符', '软硬链接', 'find与locate', 'xargs', '文件权限初步'],
                        ['文本处理', '管道与重定向', '正则表达式', 'grep', 'sed', 'awk', 'sort/uniq/cut/tr'],
                        ['用户与权限管理', '用户与组管理', 'chmod权限', 'chown与chgrp', 'sudo配置', '特殊权限'],
                        ['进程管理', 'ps与top', 'kill与信号', '前台与后台任务', 'nohup与disown', 'systemd服务单元'],
                        ['网络管理与诊断', 'ip/ifconfig', 'ping与traceroute', 'ss与netstat', 'curl与wget', 'nc/nmap简介'],
                        ['磁盘与存储', 'df与du', 'mount与umount', 'fdisk与lsblk', 'LVM概念', '文件系统简介'],
                        ['压缩与归档', 'tar', 'gzip与bzip2', 'zip与unzip'],
                        ['系统服务管理', 'systemctl', 'service命令', '开机自启管理'],
                        ['定时任务', 'crontab', 'at', '计划任务日志'],
                        ['SSH与远程管理', 'ssh连接', 'scp文件传输', 'ssh-keygen密钥', 'ssh配置优化'],
                        ['文本编辑器', 'vim基本操作', 'vim查找替换', 'nano基础'],
                        ['Shell脚本编程', '环境变量', '条件判断', '循环', '函数', '脚本调试', '执行与权限'],
                        ['软件包管理', 'apt/yum/dnf', '安装与卸载', '更新与升级', '仓库源配置'],
                        ['日志查看与分析', 'journalctl', 'tail与less', '/var/log目录', 'logrotate简介'],
                        ['系统资源监控', 'free', 'vmstat与iostat', 'uptime与top', 'sar简介'],
                        ['防火墙管理', 'iptables基础', 'firewalld', 'ufw'],
                        ['DNS与主机名', '/etc/hosts', 'resolv.conf', 'hostnamectl', 'nslookup/dig'],
                        ['终端复用器', 'tmux基础', 'screen简介']
                    ]
                },
                'MySQL': {
                    'desc': '最流行的开源关系型数据库，用于结构化数据的持久化存储和查询',
                    'difficulty': 1,
                    'dimensions': [
                        ['SQL基础', 'DDL建表', 'DML增删改', 'DQL查询', '常用函数', '数据类型', '运算符与表达式'],
                        ['表设计', '主键与外键', '约束(唯一/非空/检查)', '默认值与自增', '规范化与反规范化', '表分区概念'],
                        ['索引基础', '普通索引', '唯一索引', '复合索引', '前缀索引', '全文索引', '索引数据结构(B+Tree)'],
                        ['索引优化', '最左前缀原则', '覆盖索引', '索引下推', '索引选择性', 'MRR与BKA'],
                        ['查询优化', 'Explain执行计划', '连接与子查询', '分组聚合与排序', '分页查询', 'CASE WHEN', 'NULL处理', 'SQL优化原则'],
                        ['事务与锁', '事务特性(ACID)', '隔离级别', 'MVCC原理', '行锁与表锁', '间隙锁', '死锁排查'],
                        ['日志系统', 'redo log', 'undo log', 'binlog', '慢查询日志', '错误日志'],
                        ['高级对象', '视图', '存储过程', '触发器', '事件', '函数'],
                        ['字符集与编码', 'UTF8MB4', '排序规则', '字符集配置'],
                        ['运维与备份', 'mysqldump备份', '物理备份概念', '主从复制', '读写分离', '连接池配置'],
                        ['性能与监控', 'performance_schema', 'information_schema', '重要状态变量', '资源消耗分析']
                    ]                   
                },
                'PostgreSQL': {
                    'desc': '功能强大的开源关系型数据库，支持高级数据类型和复杂查询',
                    'difficulty': 1,
                    'dimensions': [
                        ['SQL基础与表管理', '数据类型', '表创建与修改', '约束(主键/唯一/检查/非空)', 'DML增删改', '基本查询与过滤', '默认值'],
                        ['高级查询', '连接(JOIN)', '子查询', '公用表表达式(CTE)', '窗口函数', '聚合函数', '集合操作'],
                        ['高级数据类型', '数组操作', 'JSON与JSONB', '全文搜索', '枚举类型', '自定义类型', '域类型'],
                        ['索引与查询优化', '索引类型(B-tree/Hash/GIN/GiST)', 'EXPLAIN执行计划', '查询优化技巧', '索引维护与监控'],
                        ['事务与并发控制', '事务(ACID)', '隔离级别', 'MVCC原理', '行锁与表锁', '死锁检测', '并发控制建议'],
                        ['数据库对象', '视图', '物化视图', '存储过程', '函数', '触发器', '规则', '序列与自增列'],
                        ['高级表特性', '表继承', '声明式分区', '分区管理操作', '表空间'],
                        ['模式与权限', '模式管理', '用户与角色', 'GRANT/REVOKE', '行级安全策略'],
                        ['备份恢复与数据迁移', 'pg_dump逻辑备份', '物理备份与WAL', 'PITR时间点恢复', 'COPY导入导出'],
                        ['复制与高可用', '流复制配置', '逻辑复制', '复制监控', '高可用方案概念'],
                        ['性能监控与优化', 'pg_stat_activity', 'pg_stat_statements', '慢查询日志', '关键配置参数调优'],
                        ['扩展与生态', '扩展安装管理', 'PostGIS', 'pg_cron', '其他常用扩展']
                    ]
                },
                'Python': {
                    'desc': '简洁高效的后端开发语言，适合快速开发和数据处理场景',
                    'difficulty': 1,
                    'dimensions': [
                        ['基础语法', '数据类型', '运算符', '流程控制', '函数定义与参数', 'lambda表达式', '作用域'],
                        ['数据结构', '列表与元组', '字典与集合', '推导式', '切片', 'enumerate与zip'],
                        ['面向对象编程', '类与对象', '继承与多态', '特殊方法', '属性装饰器', '抽象基类'],
                        ['函数进阶', '闭包', '装饰器', '生成器', '迭代器', 'functools模块'],
                        ['异常处理', '异常层次', 'try-except-else-finally', 'raise', '自定义异常', '上下文管理器'],
                        ['模块与包管理', '模块导入', '包结构', 'pip与虚拟环境', '常用内置模块概览'],
                        ['文件与持久化', '文件读写', 'with语句', 'pathlib路径操作', 'pickle序列化'],
                        ['类型注解', '类型提示', 'mypy', '泛型', 'dataclass'],
                        ['数据处理', '正则表达式', 'datetime模块', 'CSV处理', 'collections模块', 'itertools模块'],
                        ['并发编程', '多线程', '多进程', '协程与async/await', 'asyncio', 'concurrent.futures'],
                        ['网络编程', 'socket基础', 'requests库', 'HTTP请求'],
                        ['数据库与ORM', 'psycopg2/pymysql', 'SQLAlchemy基础', 'CRUD操作', '异步ORM'],
                        ['Web框架', 'Django基础', 'Flask基础', 'FastAPI', '路由与视图', '模板引擎'],
                        ['API开发', 'RESTful设计', '序列化与验证', '认证与授权(JWT)', '中间件', '接口文档'],
                        ['测试', 'unittest', 'pytest', 'mock', '测试覆盖率'],
                        ['日志', 'logging模块', '日志级别与格式', 'handler配置', '上下文日志'],
                        ['运行时机制', '垃圾回收', 'GIL', '深拷贝与浅拷贝', '性能分析(cProfile)'],
                        ['安全与加密', 'hashlib', 'hmac', 'cryptography库', 'secrets']
                    ]
                },
                'RESTful API': {
                    'desc': '基于HTTP的API设计规范，使用JSON进行数据交换',
                    'difficulty': 1,
                    'dimensions': [
                        ['HTTP基础', '请求方法(GET/POST/PUT/DELETE/PATCH)', '状态码分类', '常用状态码', '请求头与响应头', '内容协商'],
                        ['URI设计', '资源命名规范', '路径参数', '查询参数', '层级结构', '避免动词'],
                        ['请求与响应', 'JSON数据格式', '请求体验证', '响应封装', '统一响应格式', '分页与排序', '字段筛选'],
                        ['错误处理', '错误码设计', '错误响应结构', '全局异常处理', '常见业务错误'],
                        ['安全与认证', '认证方式(Basic/JWT)', 'OAuth2概念', 'Token刷新', '幂等性', 'HTTPS强制', '常见安全头'],
                        ['设计原则与约束', 'REST核心约束', '无状态', '资源导向', 'HATEOAS', 'Richardson成熟度模型'],
                        ['跨域与缓存', 'CORS配置', 'Cache-Control', 'ETag', 'Last-Modified', '缓存策略'],
                        ['速率限制与网关', '速率限制算法', 'API网关作用', '负载均衡', '超时处理', '重试机制'],
                        ['版本管理', 'URI版本', '请求头版本', '兼容性策略', '废弃处理'],
                        ['文档与对比', 'OpenAPI规范', 'Swagger工具', '文档自动生成', 'GraphQL对比', 'gRPC对比']
                    ]
                },
                '单元测试': {
                    'desc': 'JUnit、pytest等测试框架，编写自动化测试保证代码质量',
                    'difficulty': 1,
                    'dimensions': [
                        ['测试核心概念', '测试金字塔', '测试驱动开发(TDD)', '行为驱动开发(BDD)', '测试策略'],
                        ['测试类型', '单元测试', '集成测试', '端到端测试', '性能测试', '冒烟测试', '回归测试', '探索性测试', '压力测试'],
                        ['测试替身', '模拟(Mock)', '桩(Stub)', '间谍(Spy)', '伪造(Fake)'],
                        ['JUnit', '核心注解', '断言', '异常测试', '参数化测试', '生命周期管理'],
                        ['Mockito', 'Mock创建', 'Spy', 'Stub', '行为验证', '参数匹配器'],
                        ['pytest', '断言', 'fixture', '参数化', 'mock与patch', '插件体系'],
                        ['unittest', 'TestCase', 'setUp与tearDown', 'assert方法', 'subTest', '测试套件'],
                        ['测试工程化', '测试覆盖率(JaCoCo/coverage)', 'CI集成', '测试报告(Allure)', '测试数据管理', '契约测试']
                    ]
                },
                'Django': {
                    'desc': 'Python全栈Web框架，内置ORM、管理后台、认证系统等完整功能',
                    'difficulty': 2,
                    'dimensions': [
                        ['项目结构与路由', 'MTV架构', '项目创建', '应用', 'URLconf配置', '路由命名与反向解析'],
                        ['视图与请求处理', 'Request与Response对象', '基于函数的视图', '基于类的视图', '通用视图', '混合(mixin)'],
                        ['模板系统', '模板语法', '模板标签与过滤器', '模板继承', '静态文件引用'],
                        ['ORM基础', '模型与字段类型', '字段选项', '数据库迁移', '增删改查', '过滤器'],
                        ['ORM高级', 'Q对象与F表达式', '聚合函数', '跨表查询', 'select_related与prefetch_related', '分页'],
                        ['Admin后台', 'Admin注册与展示', '列表搜索与过滤', '自定义Admin行为', 'Actions'],
                        ['表单处理', 'Form类', 'ModelForm', '表单验证', '表单集', '自定义验证器'],
                        ['中间件与上下文', '中间件定义与顺序', '会话(Session)', 'Cookie', '缓存框架', '消息框架'],
                        ['认证与权限', '认证系统', '用户模型扩展', '权限与分组', 'CSRF防护', '登录/登出'],
                        ['静态文件与上传', '静态文件配置', '媒体文件上传', '文件存储后端', 'CDN支持'],
                        ['信号', '内置信号', '自定义信号', '信号处理器', 'connect/disconnect'],
                        ['DRF序列化与视图', '序列化器', '反序列化与验证', '视图集', '路由注册', '分页过滤搜索'],
                        ['DRF认证与限流', '认证类(JWT/Session)', '权限类', '限流策略', '版本管理'],
                        ['异步任务', 'Celery集成', '任务定义', '定时调度', '结果监控'],
                        ['配置与日志', 'settings配置', '环境变量分离', '日志配置', '调试设置'],
                        ['部署与生产', 'gunicorn/uWSGI', 'Nginx反向代理', '生产环境安全设置', 'CORS配置', '性能优化'],
                        ['国际化', '国际化配置', '模板标记翻译', '模型字段翻译', '语言切换']
                    ]                   
                },
                'Docker': {
                    'desc': '容器化技术，将应用及其依赖打包为可移植的容器镜像',
                    'difficulty': 2,
                    'dimensions': [
                        ['Docker基础', 'Docker安装', '镜像概念', '容器概念', '镜像仓库(Docker Hub)', '运行第一个容器'],
                        ['Dockerfile与构建', 'Dockerfile基础指令', 'FROM/RUN/COPY/CMD', '构建上下文', '镜像分层', '层缓存优化', '.dockerignore', '多阶段构建'],
                        ['镜像管理', '镜像tag', '推送与拉取', '镜像优化', 'alpine/slim镜像', 'distroless镜像', 'Dockerfile最佳实践'],
                        ['容器运行与配置', '端口映射', '环境变量', '数据卷与挂载', '容器互联', '资源限制(CPU/内存)'],
                        ['Docker Compose', 'docker-compose.yml', '服务定义', '网络与卷', '环境与依赖', '常用命令'],
                        ['Docker网络', '网络模式(bridge/host/none)', '自定义网络', 'DNS服务发现'],
                        ['容器运维', '日志驱动', '健康检查', '重启策略', '容器监控(cAdvisor)', '资源使用查看'],
                        ['安全与权限', '非root运行', '权限配置', 'rootless模式', '安全扫描', 'Seccomp/AppArmor简介'],
                        ['私有仓库与加速', 'Harbor私有仓库', '镜像加速器配置', '镜像签名与安全'],
                        ['集群与编排入门', 'Docker Swarm概念', '节点与集群管理', '服务部署与扩容', '滚动更新'],
                        ['CI/CD集成', 'Docker与Jenkins', 'GitHub Actions构建镜像', '镜像推送到仓库', 'Kubernetes基础概念']
                    ]                   
                },
                'Elasticsearch': {
                    'desc': '分布式搜索和分析引擎，用于全文搜索和日志分析',
                    'difficulty': 2,
                    'dimensions': [
                        ['索引与文档操作', '索引创建与删除', '文档CRUD', '批量操作', '并发控制与版本', 'Refresh与Flush'],
                        ['映射与字段类型', '动态映射', '显式映射', '核心字段类型(text/keyword/date等)', '多字段', '别名', '索引模板', '运行时字段'],
                        ['文本分析', '倒排索引原理', '内置分词器', '自定义分析器', '拼音分词', '同义词配置', '字符过滤器与令牌过滤器'],
                        ['DSL查询', 'Query与Filter上下文', '全文搜索(match/match_phrase)', '精确查询(term/terms)', '布尔查询', '范围查询', '通配符与正则'],
                        ['聚合分析', '桶聚合(terms/histogram/range)', '指标聚合(sum/avg/min/max)', '管道聚合', '嵌套聚合', '聚合排序与大小'],
                        ['搜索特性', '分页(from/size/search_after)', '排序', '高亮', 'Suggest自动补全', '搜索模板'],
                        ['相关性调优', 'TF-IDF与BM25', 'boosting', '权重调整', 'function_score', 'Explain接口', '慢查询分析'],
                        ['集群架构与高可用', '节点角色(master/data/coordinating)', '分片与副本', '集群健康状态', '冷热分离', '脑裂避免', '故障转移'],
                        ['监控与性能优化', 'Cat与Monitor API', '慢日志', '缓存机制', '段合并策略', '磁盘与内存监控', '写入优化(refresh/translog)', '搜索优化'],
                        ['备份与恢复', '快照与恢复', '快照生命周期', '跨集群复制(CCR)', '跨集群搜索'],
                        ['客户端与集成', 'Java/Python客户端', '连接池配置', '批量写入策略', 'Spring Data Elasticsearch']
                    ]
                },
                'FastAPI': {
                    'desc': '现代Python Web框架，基于类型提示，自动生成OpenAPI文档',
                    'difficulty': 2,
                    'dimensions': [
                        ['路由与请求处理', '路由装饰器', '路径参数', '查询参数', '请求体', '请求方法', '路由分组与标签', '应用生命周期事件'],
                        ['响应处理', '响应模型', '状态码', 'HTTP异常', '响应头与Cookie', '流式响应', '文件上传与下载'],
                        ['数据验证与模型', 'Pydantic模型', '字段类型与校验', '嵌套模型', '可选字段与默认值', '枚举类型', '自定义验证器', '请求体验证'],
                        ['依赖注入与安全', '依赖注入基础', 'OAuth2密码模式', 'JWT认证', '安全依赖', 'OAuth2与OpenID Connect概念'],
                        ['中间件与CORS', '中间件定义', '内置中间件', 'CORS配置'],
                        ['异步与后台任务', '异步async/await', 'BackgroundTasks', 'WebSocket端点'],
                        ['数据库集成', 'SQLAlchemy配置', 'ORM操作与CRUD', '异步数据库支持', '事务管理', 'Alembic数据库迁移'],
                        ['测试与文档', 'TestClient', 'pytest集成', '自动生成OpenAPI文档', 'Swagger与ReDoc'],
                        ['配置与日志', '配置管理', '环境变量', '日志配置', '多环境配置'],
                        ['部署与性能', 'uvicorn与gunicorn', 'Docker化部署', 'nginx反向代理', 'HTTPS配置', '缓存', '限流'],
                        ['静态文件与模板', '静态文件服务', 'Jinja2模板集成']
                    ]                   
                },
                'GraphQL': {
                    'desc': '灵活的API查询语言，客户端可精确获取所需数据',
                    'difficulty': 2,
                    'dimensions': [
                        ['GraphQL类型系统', '对象类型', '字段', '标量类型', '枚举类型', '接口', '联合类型', '输入类型'],
                        ['查询与变更', '查询(Query)', '变更(Mutation)', '字段参数', '别名', '内联片段'],
                        ['解析器与上下文', '字段解析器', '解析器链', '上下文(context)', '参数传递与验证', '错误处理'],
                        ['查询执行与优化', '查询验证', '执行流程', 'N+1问题', 'DataLoader批量处理', '查询缓存'],
                        ['分页规范', 'Offset分页', 'Cursor分页', 'Relay Connection规范', 'Edges与PageInfo'],
                        ['高级查询特性', '片段(Fragment)', '内省(Introspection)', '变量', '指令(@include/@skip)', '自定义指令'],
                        ['Schema设计与管理', 'Schema拼接', '模块化', '版本化策略', '认证授权', '字段级权限', 'JWT集成'],
                        ['性能与监控', '查询复杂度分析', '深度限制', '限流', '缓存策略', '性能监控'],
                        ['订阅与实时推送', '订阅(Subscription)', 'WebSocket传输', '实时数据推送', '订阅过滤'],
                        ['错误处理与工具', '错误格式与扩展', 'GraphQL Playground', 'GraphiQL', '调试技巧'],
                        ['Apollo生态', 'Apollo Server', 'Apollo Client', 'Apollo Federation', 'Apollo Studio'],
                        ['代码生成与类型生成', 'Schema优先开发', '代码优先开发', 'GraphQL Code Generator', '类型安全'],
                        ['框架集成', 'NestJS集成', 'FastAPI集成', 'Django集成', 'Spring Boot集成'],
                        ['高级操作', '批量操作', '文件上传', '持久化查询', '自定义标量']
                    ]               
                },
                'JWT认证': {
                    'desc': 'JSON Web Token，用于无状态的用户身份验证',
                    'difficulty': 2,
                    'dimensions': [
                        ['JWT基础与结构', 'Header', 'Payload', 'Signature', 'Base64URL编码', '紧凑序列化格式'],
                        ['签名与密钥', '签名算法(HS256/RS256/ES256)', '对称密钥', '非对称密钥对', '密钥安全存储', 'kid头部'],
                        ['声明与生命周期', '注册声明(iss/sub/aud/exp/nbf/iat)', '自定义私有声明', 'Token有效期', '刷新Token策略', 'Token撤销方案'],
                        ['认证流程', '无状态认证模型', '登录颁发Token', '携带Token请求', '验证解析Token', '登出处理'],
                        ['存储与传输安全', 'Bearer认证方案', 'Authorization头', '本地存储(localStorage/sessionStorage)', 'Cookie HttpOnly/Secure标志', 'XSS与CSRF防护'],
                        ['安全最佳实践', '短有效期', '密钥轮换', '最小化Payload', '白名单验证算法', '敏感操作重新认证', 'Token黑名单'],
                        ['客户端实现', 'axios/fetch拦截器', 'Token静默刷新', '并发请求排队', 'SPA认证状态管理'],
                        ['服务端实现', '签发与验证库', '中间件', '密钥配置', '统一异常处理'],
                        ['高级主题', '多设备登录', '单点登录(SSO)', 'Token绑定指纹', 'OAuth2与OpenID Connect关联']
                    ]
                },  
                'Kafka': {
                    'desc': '高吞吐量分布式流处理平台，用于实时数据传输和处理',
                    'difficulty': 2,
                    'dimensions': [
                        ['核心概念与架构', '主题与分区', '副本与ISR', 'Leader与Follower', '控制器', '集群协调', '消费者组与再平衡'],
                        ['生产者', '消息发送', '分区策略与key路由', '粘性分区', 'acks配置', '重试与幂等性', '事务消息', '拦截器'],
                        ['消费者与位移管理', '消费模式', 'offset与消费位移', '自动提交与手动提交', '再平衡监听器', '重置策略'],
                        ['消息语义与可靠性', 'At Most/Least/Exactly Once', '幂等Producer', '事务读写', '消息压缩(snappy/gzip/zstd)'],
                        ['序列化与Schema管理', 'JSON/Avro/Protobuf', 'Schema Registry', '序列化器配置', '兼容性策略'],
                        ['Kafka Streams与Connect', 'Streams拓扑', '状态存储', '窗口计算', 'KSQL查询', 'Source/Sink连接器'],
                        ['监控与运维', 'JMX指标', '常用监控工具(Kafka Manager/Eagle)', '性能调优(吞吐/延迟/磁盘/网络)', '消息积压与重复消费排查'],
                        ['客户端与生态集成', 'Spring Kafka', 'kafka-python与confluent-kafka', 'Spring Cloud Stream', 'Flink/Spark Streaming集成']
]                   
                },
                'MongoDB': {
                    'desc': '文档型NoSQL数据库，适合存储非结构化和半结构化数据',
                    'difficulty': 2,
                    'dimensions': [
                        ['基础概念与数据模型', '文档', '集合', '数据库', 'BSON格式', 'ObjectId', '常用数据类型(String/Number/Date/Array等)'],
                        ['CRUD操作', 'insertOne/insertMany', 'find/findOne', 'updateOne/updateMany与upsert', 'deleteOne/deleteMany', '更新操作符($set/$inc/$push等)', '批量写入'],
                        ['查询进阶', '查询条件(比较/逻辑/元素/数组/正则)', '投影', '排序与分页(limit/skip)', '游标', '读取关注与读取偏好'],
                        ['聚合框架', '管道阶段($match,$group,$project,$sort,$limit,$skip,$lookup,$unwind,$addFields)', '聚合表达式', '聚合性能优化'],
                        ['索引管理', '单字段索引', '复合索引', '多键索引', '文本索引', '地理空间索引', '唯一/稀疏/TTL索引', '索引创建与管理'],
                        ['性能分析与优化', '执行计划(explain)', '慢查询日志', '查询优化技巧', '写入优化', 'WiredTiger缓存与存储引擎', '数据压缩'],
                        ['复制与高可用', '副本集架构', '主从复制', '自动选举', '读写分离', '故障转移'],
                        ['分片与扩展', '分片集群', '分片键选择', '哈希分片与范围分片', '均衡器与Chunks', '分片策略'],
                        ['事务与会话', '多文档事务', 'Session', '事务隔离级别', 'Change Stream'],
                        ['安全与权限', '认证机制(SCRAM/X.509)', '角色与权限', '用户管理', '审计日志'],
                        ['运维与备份', 'mongodump与mongorestore', '导入导出(mongoimport/export)', 'MongoDB Compass监控', '连接池配置', '磁盘与内存监控'],
                        ['客户端与生态', 'PyMongo', 'Mongoose', 'Spring Data MongoDB', '连接驱动使用']
                    ]                   
                },
                'Nginx': {
                    'desc': '高性能Web服务器和反向代理，用于负载均衡和静态资源服务',
                    'difficulty': 2,
                    'dimensions': [
                        ['配置基础与运维', 'nginx.conf主配置结构', '全局块/events/http/server/location块', '信号控制与热重载', '配置测试(nginx -t)', 'worker进程与连接数配置'],
                        ['HTTP服务器与静态服务', '监听端口与域名', '根目录与默认页', 'try_files', '静态资源服务', 'gzip压缩与gzip_static', 'expires缓存控制'],
                        ['反向代理与负载均衡', 'proxy_pass反向代理', 'upstream配置', '负载均衡算法(轮询/权重/ip_hash/least_conn)', '健康检查', 'proxy_set_header设置(X-Real-IP等)', '长连接配置', 'WebSocket代理'],
                        ['URL重写与重定向', 'rewrite指令与正则', 'return与状态码(301/302)', '强制HTTPS重定向', 'www重定向', 'location匹配优先级(精确/前缀/正则)', 'if判断与Rewrite规则'],
                        ['SSL/TLS与安全加固', 'SSL证书配置', 'HTTPS与HTTP/2', 'TLS版本与优化', 'HSTS与OCSP stapling', '安全头(X-Frame-Options/CSP等)', 'IP访问控制(allow/deny)'],
                        ['性能调优与超时', 'worker_processes与worker_connections', 'sendfile/tcp_nopush/tcp_nodelay', '缓冲区大小配置', 'keepalive_timeout', 'client_header_buffer_size与body大小限制', 'proxy超时配置'],
                        ['访问控制与限流', 'limit_req请求限流(漏桶)', 'limit_conn连接限流', '令牌桶算法', '速率限制配置'],
                        ['日志与监控', 'access_log与error_log', '日志格式与JSON日志', '日志切割(logrotate)', 'stub_status模块', 'Prometheus监控集成', 'openresty与lua模块简介'],
                        ['后端应用集成与TCP代理', 'FastCGI配置(php-fpm)', 'uWSGI/Node.js代理', 'stream模块TCP/UDP代理', '反向代理到Python/其他应用']
                    ]
                },
                'OAuth2': {
                    'desc': '开放授权协议，支持第三方登录和API访问授权',
                    'difficulty': 2,
                    'dimensions': [
                        ['OAuth2基础与角色', '角色(资源所有者/客户端/授权服务器/资源服务器)', '访问令牌', '刷新令牌', 'scope范围', 'state参数', 'Bearer令牌'],
                        ['授权流程', '授权码模式', '隐式授权(已不推荐)', '密码凭证模式', '客户端凭证模式', '授权码+PKCE推荐', '流程选择与安全考量'],
                        ['PKCE安全扩展', 'PKCE防CSRF攻击', 'code_verifier', 'code_challenge', 'code_challenge_method', '授权码流程集成PKCE'],
                        ['令牌端点与生命周期', 'authorization_endpoint', 'token_endpoint', 'revocation_endpoint', 'introspection_endpoint', '令牌生成与存储', '令牌刷新策略', '令牌撤销机制'],
                        ['JWT与令牌格式', 'JWT作为访问令牌', 'JWT Bearer', 'JWKs与jwks_uri', 'JWT验证', 'JWKS缓存', 'JARM安全响应模式'],
                        ['OpenID Connect', 'OpenID Connect基础', 'ID Token', 'UserInfo端点', 'Discovery文档', '单点登录(SSO)', 'RP-Initiated Logout'],
                        ['客户端注册与安全', 'client_id与client_secret', 'redirect_uri注册', 'CSRF防护(state与PKCE)', '重放攻击防护', '令牌安全存储', '强制TLS', '安全最佳实践'],
                        ['第三方登录与集成', '常见提供商(GitHub/Google/微信/钉钉)', '社交登录流程', '联合登录', '登录流程设计', '用户信息映射'],
                        ['实现框架与库', 'Spring Security OAuth2', 'Authlib(Python)', 'oauthlib', 'Passport.js', '其他SDK']
                    ]
                },
                'RabbitMQ': {
                    'desc': '消息队列中间件，实现应用解耦和异步任务处理',
                    'difficulty': 2,
                    'dimensions': [
                        ['核心概念与AMQP', 'AMQP协议', '消息与属性', '队列与属性', '交换机', '绑定', '路由键', '虚拟主机'],
                        ['交换机类型', 'direct', 'fanout', 'topic', 'headers', '默认交换机', '备用交换机'],
                        ['消息发布与消费', '生产者与消费者', 'basic_publish', 'basic_consume', '连接与信道', '推拉消费模式'],
                        ['消息确认与预取', 'basic_ack与nack', '手动/自动确认', 'QoS预取(prefetch)', '公平调度', 'basic_reject与basic_recover'],
                        ['持久化与可靠性', '消息与队列持久化', 'publisher confirms', '事务', 'mandatory标志', '备份交换机'],
                        ['高级队列特性', '死信队列', 'TTL与过期消息', '延迟队列', '优先级队列', '消息顺序', '消费幂等性'],
                        ['集群与高可用', '集群搭建', '镜像队列', '仲裁队列', '负载均衡', '故障转移', '联邦与Shovels'],
                        ['监控与运维', '管理界面', 'rabbitmqadmin', 'HTTP API', 'Prometheus监控插件', '日志分析', '消息追踪'],
                        ['安全与权限', '用户角色', '虚拟主机', '访问控制', 'TLS加密'],
                        ['客户端与集成', 'Spring AMQP', 'pika(Python)', 'Go amqp091-go', '其他语言SDK'],
                        ['消息模式与最佳实践', '可靠投递', '重试与补偿', '消息堆积与消费能力', '最终一致性', '顺序消息设计']
                    ]
                },
                'Redis': {
                    'desc': '高性能内存键值存储，用作缓存、会话存储和消息队列',
                    'difficulty': 2,
                    'dimensions': [
                        ['核心数据类型', 'String', 'Hash', 'List', 'Set', 'Sorted Set', 'HyperLogLog', 'Geo', 'Stream', 'Bitmap'],
                        ['通用键操作', 'KEYS与SCAN', 'EXPIRE与TTL', 'DEL与UNLINK', 'EXISTS', 'TYPE', 'RENAME', 'DUMP与RESTORE'],
                        ['发布订阅', 'PUBLISH与SUBSCRIBE', 'PSUBSCRIBE模式订阅', '消息队列Stream', '消费者组', '消息确认与pending'],
                        ['管道与Lua脚本', 'Pipeline管道批量操作', 'Lua脚本执行', 'SCRIPT LOAD与EVALSHA', '原子性脚本编写'],
                        ['事务', 'MULTI/EXEC/DISCARD', 'WATCH乐观锁', '事务特性(无回滚)'],
                        ['持久化', 'RDB快照', 'AOF日志', 'AOF重写', '混合持久化', 'RDB与AOF选择策略'],
                        ['主从复制', '主从同步原理', '全量复制与部分复制', '复制积压缓冲区', '读写分离', '无磁盘复制'],
                        ['哨兵模式', 'Sentinel监控', '自动故障转移', '哨兵选举', '通知与客户端发现', 'TILT模式'],
                        ['Redis集群', '集群分片(16384槽)', '节点通信', 'MOVED与ASK重定向', '故障转移', '集群扩容与收缩'],
                        ['客户端与连接池', 'Jedis/Lettuce(Java)', 'redis-py(Python)', 'go-redis', '连接池配置', '超时与重连策略'],
                        ['分布式锁', 'SETNX实现', 'Redlock算法', 'Redisson', '锁续期', '可重入锁', '公平锁'],
                        ['缓存策略与问题', '缓存穿透与空值缓存', '缓存击穿与互斥锁', '缓存雪崩与过期打散', '缓存更新策略(旁路/写入/读写)', '缓存与数据库双写一致性'],
                        ['内存淘汰与优化', '过期删除策略(惰性/定期)', '内存淘汰策略(LRU/LFU/TTL)', '内存优化(ziplist/listpack)', 'bigkey问题与排查'],
                        ['运维与监控', 'INFO命令', '慢查询日志', 'MONITOR', '内存使用分析(memory doctor)', '延迟监控', 'Redis版本升级'],
                        ['安全配置', 'ACL访问控制', 'rename-command禁用危险命令', 'TLS加密', 'bind与protected-mode', '密码认证']
                    ]
                },
                'Spring Boot': {
                    'desc': 'Java生态的简化开发框架，提供自动配置和开箱即用的微服务支持',
                    'difficulty': 2,
                    'dimensions': [
                        ['核心基础与自动配置', '@SpringBootApplication', 'main方法', 'Starter依赖', '嵌入式服务器(Tomcat/Undertow/Jetty)', '打包jar/war', '自动配置原理'],
                        ['配置管理与多环境', 'application.yml/properties', '配置文件加载顺序', '环境变量与命令行参数', '@ActiveProfile', 'bootstrap.yml', 'Nacos配置中心'],
                        ['Web开发', '@RestController与@Controller', '@RequestMapping与派生注解', '路径变量与查询参数', '@RequestBody与响应体', 'JSON处理(Jackson/Gson)', '日期格式化', '静态资源与webjars', '模板引擎(Thymeleaf/FreeMarker)', '国际化'],
                        ['过滤器、拦截器与监听器', '过滤器', '拦截器', '监听器', 'ApplicationRunner与CommandLineRunner', '启动监听器'],
                        ['数据访问与事务', 'JdbcTemplate', 'JPA/Hibernate', 'MyBatis', 'Spring Data JPA', 'Redis与MongoDB集成', '连接池(HikariCP/Druid)', '@Transactional声明式事务', '传播行为与隔离级别', '回滚规则'],
                        ['安全与认证', 'Spring Security', 'OAuth2与JWT', '认证授权', '密码加密', 'CSRF防护', 'CORS配置'],
                        ['缓存与异步任务', 'Spring Cache抽象', 'EhCache/Caffeine/Redis缓存', '@Cacheable/@CachePut/@CacheEvict', '@Async异步执行', '线程池配置', '@Scheduled定时任务'],
                        ['日志与异常处理', 'logback-spring.xml配置', '日志级别与格式', '文件与滚动日志', '@ExceptionHandler与@ControllerAdvice', '全局异常处理'],
                        ['测试与开发工具', '@SpringBootTest', 'MockMvc', '切片测试(WebMvcTest/DataJpaTest)', 'Spring Boot DevTools热重载', 'Lombok'],
                        ['监控与运维', 'Actuator端点(health/info/metrics)', '自定义端点', 'Micrometer指标', 'Prometheus与Grafana', '分布式追踪(Sleuth/Zipkin/SkyWalking)'],
                        ['部署与容器化', 'jar/war部署', 'Docker化', 'Kubernetes部署', '多环境部署'],
                        ['微服务与分布式', '注册中心(Eureka/Nacos)', '服务发现', 'Feign/OpenFeign负载均衡', '配置中心(Spring Cloud Config/Nacos)', '熔断降级(Sentinel/Resilience4j)']
                    ]
                },
                'Spring Cloud': {
                    'desc': '微服务架构解决方案，提供服务注册、配置中心、网关等组件',
                    'difficulty': 2,
                    'dimensions': [
                        ['微服务架构与设计', '微服务概念与拆分', '服务治理', '领域驱动设计(DDD)', 'CQRS与事件溯源', 'Saga模式'],
                        ['服务注册与发现', 'Nacos', 'Consul', 'Zookeeper', '心跳机制', '自我保护', '服务下线', '集群部署'],
                        ['配置中心', 'Nacos配置管理', 'Apollo', '配置动态刷新', '配置热加载', 'Git/SVN配置', '配置优先级'],
                        ['服务调用与负载均衡', 'OpenFeign声明式客户端', 'Spring Cloud LoadBalancer', '负载均衡策略(RoundRobin/Random/Weighted)', '重试机制', '超时与连接池'],
                        ['API网关', 'Spring Cloud Gateway', '路由转发与断言', '动态路由', '网关过滤器', '跨域配置', 'IP黑白名单', '网关限流'],
                        ['熔断与降级', 'Resilience4j', 'Sentinel', '熔断规则', '降级处理', '限流与流量控制', '热点参数限流'],
                        ['认证与授权', '网关统一认证', 'JWT验证', 'Token解析与传递', '白名单与黑名单', 'OAuth2集成', '安全头配置'],
                        ['分布式事务', 'Seata', 'AT模式', 'TCC模式', 'Saga模式', 'XA模式', '事务消息'],
                        ['消息驱动与可靠性', 'Spring Cloud Stream', 'RabbitMQ/RocketMQ/Kafka', '可靠消息投递', '事务消息', '顺序消息', '延迟消息', '幂等性', '消息积压处理'],
                        ['链路追踪与日志', 'Sleuth与Zipkin', 'SkyWalking', 'Jaeger', 'TraceId与SpanId', 'ELK日志收集', '日志级别与格式'],
                        ['监控与可观测性', 'Actuator端点', 'Micrometer', 'Prometheus与Grafana', '监控面板', '告警规则'],
                        ['容器化与部署', 'Docker镜像构建', 'Kubernetes部署', 'Helm编排', '健康检查(就绪/存活探针)', '环境变量与ConfigMap/Secret', '滚动更新与弹性伸缩'],
                        ['服务网格与流量治理', 'Istio', 'Envoy与Sidecar', '灰度发布', '蓝绿部署', '金丝雀发布', 'A/B测试'],
                        ['API设计与测试', 'OpenAPI文档', 'Swagger生成', '契约测试', 'Postman调试', 'API版本管理']
                    ]
                },
                'gRPC': {
                    'desc': '高性能RPC框架，基于Protocol Buffers进行服务间通信',
                    'difficulty': 2,
                        'dimensions': [
                        ['Protobuf基础', '.proto文件', '消息定义', '字段类型与编号', '默认值', '枚举', '嵌套消息', '导入与包管理'],
                        ['服务定义与代码生成', '服务定义', 'rpc方法', 'protoc编译', '代码生成插件(protoc-gen-go/java/python)', '生成代码结构'],
                        ['通信模式', '一元RPC', '服务端流', '客户端流', '双向流', '基于HTTP/2的多路复用'],
                        ['服务端开发', '创建gRPC Server', '注册服务', '启动Serve', '一元与流式处理器实现'],
                        ['客户端开发', '创建连接(Channel)', 'Stub/Client', '一元调用', '流式调用', '阻塞与非阻塞调用'],
                        ['元数据与上下文', 'metadata创建与操作', 'context传递', '截止时间与超时', '取消传播'],
                        ['安全传输', 'TLS配置', '服务器/客户端证书', '双向TLS', 'Token认证', 'ALTS简介'],
                        ['拦截器', 'Unary拦截器', 'Stream拦截器', '服务端/客户端拦截器', '日志/监控/认证拦截器', '拦截器链'],
                        ['可靠性与负载均衡', '重试与退避', '超时与截止时间', '负载均衡策略(pick_first/round_robin)', '连接管理与心跳', 'Channel复用'],
                        ['健康检查与反射', '健康检查服务', 'grpc_health_probe', 'Server Reflection', '反射调用调试'],
                        ['请求验证', 'protovalidate', '自定义验证规则', '字段校验', '错误消息定制'],
                        ['JSON/HTTP转码与文档', 'gRPC-JSON转码', 'HTTP规则映射', 'gRPC-Gateway', 'OpenAPI/Swagger文档生成'],
                        ['工具与调试', 'grpcurl', 'BloomRPC', 'Postman gRPC支持', '拦截器调试'],
                        ['最佳实践', 'Proto风格规范', '命名规范', '错误模型(标准状态码)', '向后兼容策略', '字段演进', '日志与监控建议']
                    ]
                }
            }
        },
    }
    }
}
