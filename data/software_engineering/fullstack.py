"""全栈工程师数据"""
data = {
    '计算机与信息技术': {
        '软件工程': {
            '全栈工程师': {
                'description': '同时负责前端和后端开发，能够独立完成整个Web应用的开发。',
                'skills': {
                    'Git/GitHub': {
                        'desc': '版本控制和代码托管',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础与配置', '安装与配置', 'SSH密钥', '工作区/暂存区/仓库', 'init/clone'],
                            ['日常操作', 'add/commit/status', 'diff/log/reflog', 'reset/revert', 'stash'],
                            ['分支与合并', 'branch/checkout', 'merge/rebase', 'cherry-pick', '冲突解决', '分支策略'],
                            ['远程与协作', 'remote/push/pull/fetch', 'Pull Request流程', 'Code Review', '分支保护'],
                            ['进阶', '标签管理', '子模块', '钩子', '对象模型']
                        ]
                    },
                    'JavaScript': {
                        'desc': '前后端通用的编程语言，Web开发的核心技术',
                        'difficulty': 1,
                        'dimensions': [
                            ['核心基础', '数据类型与转换', '作用域与闭包', '原型与继承', '类', 'this绑定', '解构与展开'],
                            ['模块化', 'CommonJS', 'ES Module', '动态导入'],
                            ['异步编程', '事件循环', 'Promise', 'async/await', 'Generator', '宏任务与微任务'],
                            ['集合与元编程', 'Map/Set/WeakMap/WeakSet', 'Symbol', 'Proxy与Reflect'],
                            ['DOM与事件', 'DOM操作', '事件模型(捕获/冒泡)', '事件委托', 'BOM基础'],
                            ['网络与存储', 'AJAX/Fetch', 'JSON', 'Web Storage', '正则表达式'],
                            ['Node.js端基础', 'Buffer与Stream', 'EventEmitter', 'Crypto', '包管理(npm/yarn/pnpm)']
                        ]
                    },
                    'MySQL/PostgreSQL': {
                        'desc': '关系型数据库，存储应用数据',
                        'difficulty': 1,
                        'dimensions': [
                            ['SQL基础', 'DDL建表与数据类型', 'DML增删改查', 'WHERE与条件', 'JOIN与子查询', '分组与聚合', '排序与分页'],
                            ['约束与索引', '主键/外键/唯一/非空', 'B-Tree索引', '复合索引与最左前缀', '覆盖索引', 'Explain执行计划'],
                            ['事务与锁', 'ACID特性', '隔离级别', 'MVCC原理', '行锁/表锁/间隙锁', '死锁排查'],
                            ['日志与备份', 'redo/undo/binlog', '慢查询日志', 'mysqldump备份与恢复', 'PITR'],
                            ['高级特性', '视图与存储过程', '触发器', '字符集(UTF8MB4)', '主从复制与读写分离'],
                            ['PostgreSQL扩展', 'JSON/JSONB与数组', 'CTE与窗口函数', '物化视图', '流复制与逻辑复制', '分区表'],
                            ['数据库设计', 'ER建模与范式', '连接池(HikariCP/Druid)', '分库分表概念']
                        ]
                    },
                    'Node.js': {
                        'desc': 'JavaScript运行时环境，用于服务端开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['运行时基础', '事件循环与libuv', '非阻塞I/O', '模块系统(CommonJS/ESM)', '全局对象'],
                            ['核心模块', 'path/fs/os', 'http/https', 'Buffer与Stream', '加密(crypto)'],
                            ['进程与线程', '子进程(child_process)', '集群(cluster)', 'Worker Threads'],
                            ['事件与错误', 'EventEmitter', '错误处理模式', 'uncaughtException/unhandledRejection'],
                            ['Web框架', 'Express中间件与路由', 'Koa洋葱模型', '请求/响应处理', 'REST API设计'],
                            ['会话与安全', 'Cookie/Session', 'JWT认证', 'Helmet/XSS/CSRF', 'CORS配置'],
                            ['工程化', '包管理(npm/yarn)', '日志(Winston/Morgan)', '调试与性能分析', 'PM2部署']
                        ]
                    },
                    'RESTful API': {
                        'desc': '设计规范的前后端接口',
                        'difficulty': 1,
                        'dimensions': [
                            ['HTTP基础', '方法(GET/POST/PUT/DELETE)', '状态码分类', 'Content-Type与Accept'],
                            ['URI与资源', '资源命名规范', '路径参数与查询参数', '分页/过滤/排序', '版本控制'],
                            ['请求与响应', 'JSON数据格式', '请求体验证', '统一响应封装', '错误响应设计'],
                            ['认证与安全', 'JWT/OAuth2', 'CORS', '限流', '输入清洗', '幂等性'],
                            ['缓存与文档', 'Cache-Control/ETag', 'HATEOAS概念', 'OpenAPI/Swagger文档'],
                            ['架构对比', 'GraphQL', 'gRPC', 'WebSocket', 'API网关']
                        ]
                    },
                    'TypeScript': {
                        'desc': '带类型的JavaScript，提升大型项目的可维护性',
                        'difficulty': 1,
                        'dimensions': [
                            ['类型基础', '基础类型与any/unknown/never', '联合/交叉类型', '类型推断', '类型断言'],
                            ['接口与别名', '接口定义与扩展', '类型别名', '索引签名', '元组与枚举'],
                            ['函数与泛型', '函数类型声明', '泛型与约束', '工具类型(Partial/Pick/Omit等)', '条件类型'],
                            ['类与模块', '类与修饰符', '抽象类', '模块解析策略', '命名空间', '声明文件'],
                            ['高级类型', '类型守卫', '映射类型与keyof', 'infer', '模板字面量类型'],
                            ['配置与集成', 'tsconfig.json/strict模式', 'React/Vue/Node集成', '装饰器', '类型兼容性']
                        ]
                    },
                    'Docker': {
                        'desc': '容器化部署应用',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心概念', '镜像与容器', 'Dockerfile指令(FROM/RUN/COPY/CMD)', '层缓存与多阶段构建'],
                            ['数据与网络', '数据卷与挂载', '网络模式(bridge/host)', '端口映射', '环境变量'],
                            ['编排与Compose', 'docker-compose.yml', '服务定义', '网络与卷', 'depends_on'],
                            ['镜像管理', 'Docker Hub与私有仓库', '镜像标签与推送', '安全扫描', 'alpine/distroless'],
                            ['运维', '日志与监控', '资源限制', '健康检查', '重启策略'],
                            ['集群与CI/CD', 'Swarm基础', 'Jenkins/GitHub Actions集成', 'Harbor']
                        ]
                    },
                    'Express/Koa': {
                        'desc': 'Node.js Web框架，构建RESTful API服务',
                        'difficulty': 2,
                        'dimensions': [
                            ['Express核心', '中间件机制', '路由与Router', '请求/响应对象', '静态资源服务'],
                            ['Koa核心', '洋葱模型与async中间件', 'ctx上下文', 'koa-router/koa-body'],
                            ['请求处理', 'body解析', '文件上传', 'Cookie与Session', 'CORS'],
                            ['认证与安全', 'JWT签发与验证', 'Helmet', '参数校验', 'XSS/CSRF防护'],
                            ['集成与工程化', '数据库集成(Sequelize/Prisma)', '日志(Morgan/Winston)', 'API文档(Swagger)'],
                            ['测试与部署', 'Jest+supertest', 'PM2', '环境变量与配置']
                        ]
                    },
                    'Next.js/Nuxt.js': {
                        'desc': '全栈框架，提供服务端渲染和静态生成功能',
                        'difficulty': 2,
                        'dimensions': [
                            ['Next.js渲染', 'SSR/SSG/ISR', 'App Router与Pages Router', '服务端组件', '客户端组件'],
                            ['Next.js数据与API', 'getServerSideProps/getStaticProps', 'API Routes', '中间件', 'revalidate'],
                            ['Next.js优化', 'Image/Font优化', '代码分割与懒加载', 'Suspense与流式渲染', 'Bundle Analyzer'],
                            ['Nuxt基础', 'pages/layouts/composables', '自动导入', 'useFetch/useAsyncData', 'SEO与useHead'],
                            ['Nuxt进阶', 'Pinia状态管理', 'Nitro与H3', '内容管理(@nuxt/content)', 'PWA与i18n'],
                            ['部署与测试', 'Vercel/Node部署', 'Playwright/Vitest', '环境变量与runtimeConfig']
                        ]
                    },
                    'Prisma/TypeORM': {
                        'desc': 'ORM工具，简化数据库操作',
                        'difficulty': 2,
                        'dimensions': [
                            ['Prisma建模', 'schema.prisma', '模型与字段', '关系(1-1/1-n/n-n)', '迁移与种子'],
                            ['Prisma Client', 'CRUD与findUnique/findMany', '关联查询与嵌套写入', '聚合与分组', '事务'],
                            ['TypeORM实体', 'Entity与装饰器', '关系(ManyToOne/OneToMany)', 'Repository与DataSource'],
                            ['TypeORM查询', 'QueryBuilder', 'join与预加载', '事务与QueryRunner', '迁移'],
                            ['高级与集成', '连接池配置', '原生SQL', 'TypeScript类型生成', '性能优化建议']
                        ]
                    },
                    'React/Vue': {
                        'desc': '前端组件化框架，构建用户界面',
                        'difficulty': 2,
                        'dimensions': [
                            ['React基础', 'JSX与组件', 'State与Props', '事件处理', '条件与列表渲染'],
                            ['React Hooks', 'useState/useEffect', 'useContext/useReducer', 'useMemo/useCallback/useRef', '自定义Hook'],
                            ['React高级', '虚拟DOM与Fiber', 'React.memo与性能优化', 'Portal与错误边界', 'Suspense与并发模式'],
                            ['Vue基础', '模板语法与指令', '响应式(ref/reactive)', '计算属性与侦听器', '组件Props/Emits'],
                            ['Vue Composition API', 'setup/ref/reactive', 'watch/watchEffect', 'provide/inject', '生命周期钩子'],
                            ['状态管理与路由', 'Redux/Zustand', 'Pinia', 'React Router', 'Vue Router'],
                            ['工程化与测试', 'CSS方案(Modules/Tailwind)', 'Jest/Vitest', 'Cypress/Playwright', '代码分割与懒加载']
                        ]
                    },
                    'Redis': {
                        'desc': '内存数据库，用作缓存和会话存储',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心数据结构', 'String/Hash/List/Set/Sorted Set', '常用命令', 'Key过期与TTL'],
                            ['高级特性', '位图/HyperLogLog/Geo', '发布订阅', 'Stream消息队列'],
                            ['持久化与复制', 'RDB与AOF', '主从复制', '哨兵模式', 'Redis Cluster'],
                            ['事务与脚本', 'MULTI/EXEC', 'WATCH乐观锁', 'Lua脚本与EVALSHA'],
                            ['分布式与缓存', '分布式锁(Redlock)', '缓存穿透/击穿/雪崩', '内存淘汰策略'],
                            ['客户端与运维', 'Jedis/Lettuce/redis-py', '连接池', '慢查询日志', 'INFO监控']
                        ]
                    },
                    '云服务': {
                        'desc': 'AWS、阿里云等云平台服务使用',
                        'difficulty': 2,
                        'dimensions': [
                            ['计算与容器', 'ECS/EC2实例', 'Kubernetes(ACK/EKS)', 'Serverless函数计算/Lambda'],
                            ['存储与CDN', '对象存储(OSS/S3)', 'CDN加速', 'RDS托管数据库', 'Redis/MongoDB托管'],
                            ['网络与安全', 'VPC与子网', '负载均衡', 'API网关', 'WAF与DDoS防护'],
                            ['消息与事件', '消息队列(Kafka/SQS)', '事件总线', '工作流编排'],
                            ['监控与日志', '日志服务/CloudWatch', '分布式追踪', '应用监控告警'],
                            ['权限与成本', 'IAM/RAM权限管理', '成本优化与预算', '资源编排(Terraform)']
                        ]
                    },
                    '系统架构': {
                        'desc': '理解单体应用和微服务架构的优缺点',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构风格', '单体与模块化单体', '微服务', '事件驱动架构', '领域驱动设计(DDD)'],
                            ['分布式核心', 'CAP定理与BASE理论', '服务发现与注册', '配置中心', 'API网关'],
                            ['通信与事务', 'RPC(gRPC)', '消息队列', '分布式事务(Saga/TCC)', '最终一致性'],
                            ['质量属性', '高可用与容错', '限流/熔断/降级', '负载均衡', '幂等与重试'],
                            ['数据架构', '读写分离与分库分表', '多级缓存', '搜索引擎', '冷热分离'],
                            ['部署与演进', '蓝绿/金丝雀发布', 'CI/CD流水线', '可观测性(日志/链路/指标)', '架构评估与重构']
                        ]
                    },
                    '性能优化': {
                        'desc': '前后端性能监控和优化策略',
                        'difficulty': 3,
                        'dimensions': [
                            ['Web指标与度量', 'FCP/LCP/CLS等Core Web Vitals', 'Lighthouse', 'Performance API'],
                            ['加载优化', '代码分割与Tree Shaking', '懒加载与预加载', '图片优化(WebP/AVIF)', 'CDN与HTTP/2'],
                            ['渲染优化', '重排重绘与GPU加速', '虚拟列表', '防抖与节流', '骨架屏与SSR'],
                            ['后端优化', '数据库索引与查询优化', '缓存策略(Redis/多级)', '连接池与N+1问题', '消息队列异步化'],
                            ['流量治理', '负载均衡', '限流与熔断', '超时与重试', '读写分离'],
                            ['压测与监控', 'JMeter/k6', 'APM(SkyWalking/Pinpoint)', '分布式追踪', '全链路压测']
                        ]
                    }
                }
            }
        }
    }
}