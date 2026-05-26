"""游戏服务端工程师数据"""
data = {
    '计算机与信息技术': {
        '游戏开发': {
            '游戏服务端工程师': {
                'description': '开发游戏服务器，处理游戏逻辑和数据同步。',
                'skills': {
                    'C++': {
                        'desc': '高性能游戏服务器开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['语言基础与面向对象', '基础语法与数据类型', '类和对象/继承多态', '虚函数与多态', '运算符重载', '命名空间与作用域'],
                            ['泛型编程与STL', 'STL容器(vector/map/set)', '算法与迭代器', '模板与泛型编程', 'Lambda与函数对象'],
                            ['内存管理与指针', '智能指针(shared/unique)', '内存管理与RAII', '内存映射(mmap)', '对象生命周期与所有权'],
                            ['并发与多线程', '多线程(std::thread)', '互斥锁与条件变量', '原子操作(atomic)', '线程池与任务队列', 'async/Future异步'],
                            ['网络与IO编程', 'Socket编程基础', '异步IO(epoll/IOCP)', 'Protocol Buffer序列化', '文件IO与序列化'],
                            ['系统编程与调试', '信号处理(Signal)', '进程间通信(IPC)', '日志系统(log4cplus)', '性能分析(profiler)', '调试工具(gdb/Valgrind)'],
                            ['设计模式与工程', '单例/工厂/观察者模式', '设计模式在游戏中的应用', '代码规范与审查', '持续集成']
                        ]
                    },
                    'Go': {
                        'desc': '高并发游戏服务端开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['核心语法与并发', '基础语法与数据类型', 'Goroutine协程', 'Channel通道', 'select多路复用', 'Context上下文', '并发控制(sync包)'],
                            ['错误处理与资源', 'defer/panic/recover', '接口与类型断言', '结构体与方法', '包管理与模块'],
                            ['网络与RPC', 'net/http服务开发', 'net/rpc远程调用', 'gRPC框架', 'WebSocket通信'],
                            ['数据访问与序列化', 'database/sql连接池', 'Redis客户端(go-redis)', 'JSON/Protobuf解析', 'ORM框架(GORM)'],
                            ['工程与性能', '性能调优(pprof)', '单元测试与基准测试', '微服务架构设计', '日志与链路追踪']
                        ]
                    },
                    'Java': {
                        'desc': '企业级游戏服务器开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['语言核心与集合', '基础语法与OOP', '继承/接口/多态', '集合框架(List/Map/Set)', '泛型与注解', '异常处理与日志'],
                            ['并发与多线程', '线程与ThreadPoolExecutor', 'JUC并发包(ReentrantLock)', '原子类与CAS', '线程安全集合', '异步编程(CompletableFuture)'],
                            ['网络与框架', 'NIO与Netty框架', 'Spring/Spring Boot生态', 'MyBatis/Hibernate ORM', 'RESTful API设计'],
                            ['数据库与中间件', '数据库连接池(HikariCP)', 'Redis客户端(Jedis/Lettuce)', '消息队列(Kafka)', '缓存策略'],
                            ['性能与JVM', 'JVM内存模型与GC', 'JVM调优与参数配置', '性能分析(VisualVM/JProfiler)', '设计模式实践']
                        ]
                    },
                    '数据库': {
                        'desc': 'MySQL、Redis数据存储',
                        'difficulty': 1,
                        'dimensions': [
                            ['MySQL核心', 'SQL增删改查', '数据类型与表设计', '索引原理与优化', '事务ACID与隔离级别', '慢查询分析与优化'],
                            ['MySQL高级', '主从复制与读写分离', '分库分表策略', '备份与恢复(mysqldump/XtraBackup)', '高可用架构(MHA/InnoDB Cluster)'],
                            ['Redis核心数据结构', 'String/Hash/List/Set/ZSet', '发布订阅与Stream', '过期策略与内存淘汰'],
                            ['Redis高级', '持久化(RDB/AOF)', '主从/Sentinel/Cluster', '分布式锁实现', '缓存穿透/击穿/雪崩防护', 'Redis客户端与连接池'],
                            ['NoSQL扩展', 'MongoDB文档存储', 'Elasticsearch搜索', '时序数据库(InfluxDB)']
                        ]
                    },
                    '匹配系统': {
                        'desc': '玩家匹配算法和房间管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['匹配算法', 'ELO/Glicko积分匹配', 'MMR匹配机制', '基于规则的匹配', '等待队列与超时处理', '匹配冷却与惩罚'],
                            ['房间管理', '房间创建/加入/离开', '房间状态机(等待/开始/游戏中)', '房间解散与回收', '自定义房间与观战'],
                            ['匹配扩展', '快速匹配/排位匹配', '跨服匹配', 'AI补位机制', '匹配效率与负载均衡', '匹配日志与监控']
                        ]
                    },
                    '压测优化': {
                        'desc': '服务器性能测试和优化',
                        'difficulty': 2,
                        'dimensions': [
                            ['压测工具与指标', 'JMeter/wrk/ab', 'QPS/TPS吞吐量', '响应时间(P99/P95/平均)', '并发连接数与错误率'],
                            ['系统与网络优化', 'CPU/内存/磁盘IO分析', '网络带宽与延迟', '系统内核参数调优', 'TCP/IP栈优化'],
                            ['应用层优化', '代码热点分析与Profiler', 'SQL查询优化', '缓存策略优化', '连接池/线程池调优', 'JVM/GC优化'],
                            ['监控与预警', 'Prometheus + Grafana监控', '自定义业务指标', '告警规则与通知', '性能基线建立']
                        ]
                    },
                    '并发编程': {
                        'desc': '多线程、协程、锁机制',
                        'difficulty': 2,
                        'dimensions': [
                            ['线程与协程模型', '线程创建与生命周期', '线程池管理', '协程(Goroutine/Coroutine)', '异步任务调度'],
                            ['锁与同步机制', '互斥锁(Mutex)', '读写锁(RWLock)', '条件变量(Condition Variable)', '信号量(Semaphore)', '原子操作(Atomic)'],
                            ['并发模式与安全', '生产者消费者模式', '无锁编程与CAS', '死锁检测与避免', '并发安全集合', '乐观锁/悲观锁策略'],
                            ['通道与通信', 'Channel通道(Go)', 'BlockingQueue(Java)', '异步回调与Future', 'Actor模型']
                        ]
                    },
                    '战斗校验': {
                        'desc': '服务器端战斗逻辑验证',
                        'difficulty': 2,
                        'dimensions': [
                            ['战斗逻辑校验', '伤害公式与属性校验', '技能CD与消耗验证', 'Buff/Debuff状态校验', '攻击范围与距离判定'],
                            ['反作弊与安全', '客户端数据异常检测', '战斗结果服务器权威验证', '协议篡改检测', '战斗日志记录与回溯'],
                            ['同步与一致性', '帧同步校验与帧验证', '状态一致性检查', '战斗录像与Replay', '异常战斗报告与封禁']
                        ]
                    },
                    '消息队列': {
                        'desc': 'Kafka、RabbitMQ异步处理',
                        'difficulty': 2,
                        'dimensions': [
                            ['Kafka核心', 'Broker/Topic/Partition', '生产者/消费者与消费者组', '分区策略与Rebalance', '高可靠性(acks与ISR)', '性能调优'],
                            ['RabbitMQ核心', 'Exchange/Queue/Binding', '交换机类型(direct/topic/fanout)', '消息确认(ACK)与持久化', '死信队列(DLQ)与延迟队列'],
                            ['消息可靠性', '消息顺序性保证', '幂等性设计', '消息去重与事务', '消息积压与监控'],
                            ['集成与应用', 'Spring Kafka/Stream', 'RabbitMQ与Spring AMQP', 'MQ在游戏中的应用(异步任务/广播)']
                        ]
                    },
                    '网络编程': {
                        'desc': 'Socket、TCP/UDP、IO多路复用',
                        'difficulty': 2,
                        'dimensions': [
                            ['TCP/UDP协议', 'TCP三次握手/四次挥手', 'TCP状态与KeepAlive', 'UDP可靠传输(KCP/ENet)', '粘包/半包与协议解析'],
                            ['IO模型与架构', '阻塞IO与非阻塞IO', 'IO多路复用(select/poll/epoll)', 'IOCP异步IO模型', '高并发网络架构(Reactor/Proactor)'],
                            ['序列化与安全', 'Protocol Buffer/FlatBuffers', '自定义二进制协议设计', 'TLS/SSL加密', '连接池与流量控制'],
                            ['可靠UDP与优化', 'KCP/ENet可靠传输', '网络拥塞控制', '弱网对抗策略', '网络性能指标监控']
                        ]
                    },
                    '防作弊': {
                        'desc': '外挂检测和数据校验',
                        'difficulty': 2,
                        'dimensions': [
                            ['客户端检测', '内存扫描与特征识别', '反调试/反逆向(Anti-debug)', '虚拟机/模拟器检测', '多开/加速器检测'],
                            ['协议与行为分析', '协议异常与频率检测', '行为序列异常检测', '机器学习异常检测', '服务器端数据校验'],
                            ['安全机制', '代码混淆与加密', '签名校验与完整性保护', '设备指纹与IP限制', '举报系统与人工审核'],
                            ['处罚与运营', '封禁策略(阶梯/永久)', '异常数据告警', '防作弊策略更新', 'GM工具与后台审计']
                        ]
                    },
                    '分布式系统': {
                        'desc': '服务拆分、负载均衡、容错',
                        'difficulty': 3,
                        'dimensions': [
                            ['微服务基础', '服务注册与发现(Nacos/Consul)', 'API网关(Gateway)', '服务间RPC通信', '配置中心(Apollo/Nacos)'],
                            ['弹性与容错', '负载均衡算法', '限流熔断(Sentinel/Resilience4j)', '降级与兜底策略', '超时与重试机制'],
                            ['分布式数据', '分布式事务(Seata/TCC)', '分库分表与数据分片', '分布式缓存(Redis Cluster)', '消息总线与事件驱动'],
                            ['容器与编排', 'Docker/Kubernetes部署', 'Service Mesh(Istio)', '链路追踪(SkyWalking/Jaeger)', 'CI/CD与GitOps']
                        ]
                    },
                    '游戏同步': {
                        'desc': '状态同步、帧同步、预测回滚',
                        'difficulty': 3,
                        'dimensions': [
                            ['同步模型', '状态同步原理', '帧同步(Lockstep)', '快照同步', '同步模式选择与权衡'],
                            ['延迟与预测', '客户端预测与服务器和解', '预测回滚(Rollback Netcode)', '输入延迟与缓冲', 'GGPO/网络同步框架'],
                            ['网络优化', '可靠UDP(KCP/ENet)', '网络延迟补偿', '带宽压缩与优化', '断线重连同步'],
                            ['一致性与实现', '确定性模拟与浮点数', '帧同步录像与回放', '同步协议设计', '同步质量监控']
                        ]
                    }
                }
            }
        }
    }
}