"""数据工程师数据"""
data = {
    '计算机与信息技术': {
        '数据科学': {
            '数据工程师': {
                'description': '搭建和维护数据管道，开发ETL流程，处理大规模数据。',
                'skills': {
                    'Python': {
                        'desc': '数据管道开发和数据处理脚本',
                        'difficulty': 1,
                        'dimensions': [
                            ['语言核心', '数据类型与控制流', '函数与lambda', '面向对象(类/继承)', '异常处理', 're正则', 'JSON/YAML解析'],
                            ['数据处理', 'NumPy数组与广播', 'Pandas DataFrame读写', '合并与聚合(merge/groupby)', '时间序列处理', 'PyArrow/Parquet操作'],
                            ['数据工程', '数据库连接(pymysql/SQLAlchemy)', 'Redis/ES客户端', '文件与路径(os/pathlib/glob)', 'subprocess/系统交互', '日志(logging)'],
                            ['并发与调度', '多线程/多进程', 'asyncio异步编程', 'schedule/APScheduler', 'Celery分布式队列', 'PySpark交互'],
                            ['工程化', '单元测试(unittest/pytest)', 'Git版本控制', 'CI/CD集成', 'Airflow PythonOperator', 'ETL脚本开发']
                        ]
                    },
                    'SQL': {
                        'desc': '数据仓库查询和优化',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础查询', 'SELECT/聚合/分组', 'JOIN与子查询', 'UNION与CASE WHEN', '字符串/日期函数', 'NULL处理(COALESCE)'],
                            ['窗口函数', 'OVER与PARTITION BY', 'ROW_NUMBER/RANK/DENSE_RANK', 'LAG/LEAD偏移', 'SUM/AVG累计窗口', 'RANGE/ROWS帧'],
                            ['数据仓库建模', '星型/雪花模型', '事实表与维度表', '分区表与分桶表', 'SCD缓慢变化维', 'Hive/Spark SQL语法差异'],
                            ['高级特性', 'CTE与递归查询', '数组/JSON/Map处理', 'Lateral View/Explode', 'Hive/ClickHouse特有语法'],
                            ['优化与执行', 'EXPLAIN执行计划', '谓词下推与列裁剪', 'Broadcast/Shuffle Join', '数据倾斜处理', '物化视图与索引']
                        ]
                    },
                    'Scala': {
                        'desc': '大数据处理语言，Spark原生支持',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础语法', '变量(val/var)', '函数/高阶函数', '模式匹配', 'Option/Either/Try', '隐式转换'],
                            ['函数式编程', '不可变集合', 'map/flatMap/filter', 'reduce/fold/groupBy', 'for推导与yield', '偏函数与柯里化'],
                            ['并发与异步', 'Future/Promise', 'Await与并发控制', 'Actor模型概念'],
                            ['Spark集成', 'RDD/DataFrame/Dataset', 'Spark SQL', 'Spark Streaming/Structured Streaming', 'MLlib/GraphX', 'SparkSubmit与打包']
                        ]
                    },
                    'ETL': {
                        'desc': '数据抽取、转换、加载流程开发',
                        'difficulty': 2,
                        'dimensions': [
                            ['概念与工具', 'ETL vs ELT', '数据管道(Pipeline)', 'CDC变更捕获(Debezium/Canal)', 'Sqoop/DataX/Kettle', 'Airbyte/NiFi'],
                            ['抽取(Extract)', '全量/增量抽取', '基于时间戳/日志增量', 'API与文件源', 'Kafka流式抽取'],
                            ['转换(Transform)', '数据清洗(空值/重复/格式)', '脱敏与标准化', 'SCD Type1/2/3', '字段映射/计算/拆分合并'],
                            ['加载(Load)', '全量/增量/Upsert', '分区加载', 'Hive/ClickHouse/Doris加载', '维度/事实表加载策略'],
                            ['调度与治理', 'Airflow/Oozie/DolphinScheduler', '任务依赖与重试', '数据质量检查', '血缘与元数据', 'ETL监控与日志']
                        ]
                    },
                    'Flink': {
                        'desc': '实时流处理框架',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与部署', 'JobManager/TaskManager', 'Standalone/YARN/K8s部署', 'Slot与并行度', 'Flink Dashboard'],
                            ['DataStream API', 'Source/Sink', 'map/filter/keyBy/reduce', 'connect与侧输出', 'ProcessFunction'],
                            ['窗口与水印', '时间语义(Event/Processing)', '滚动/滑动/会话窗口', 'Watermark策略', '迟到数据处理(allowedLateness)', '侧输出迟到数据'],
                            ['状态与容错', 'Keyed/Operator State', 'RocksDB后端', 'Checkpoint与Savepoint', 'Exactly-Once语义', '重启策略'],
                            ['Table API & SQL', 'TableEnvironment', '窗口聚合(TUMBLE/HOP)', 'UDF/UDAF/UDTF', 'Connector(Kafka/CDC/JDBC)', 'Flink CDC集成']
                        ]
                    },
                    'Hadoop': {
                        'desc': '大数据存储和处理生态系统，包括HDFS和MapReduce',
                        'difficulty': 2,
                        'dimensions': [
                            ['HDFS基础', 'NameNode/DataNode', 'Block与副本机制', '读写流程', '机架感知与数据均衡', 'HDFS命令(hdfs dfs)'],
                            ['YARN资源管理', 'ResourceManager/NodeManager', '队列与调度器(Capacity/Fair)', '应用提交与监控', 'HA配置'],
                            ['MapReduce计算', 'Mapper/Reducer/Driver', 'Shuffle与排序', 'InputFormat/OutputFormat', 'Combiner优化', '计数器与分布式缓存'],
                            ['生态与运维', 'HBase/ZooKeeper', 'Sqoop/Flume/Oozie', 'Hadoop HA', '集群监控与扩容', '小文件处理']
                        ]
                    },
                    'Hive': {
                        'desc': '基于Hadoop的数据仓库工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与表设计', '内部/外部表', '分区表/分桶表', 'SerDe与存储格式(ORC/Parquet)', 'Metastore服务', 'CTAS与数据加载'],
                            ['HQL查询', 'JOIN(Inner/Semi/Map)', '子查询与Lateral View', '窗口函数(OVER)', 'CTE与UNION', '数组/Map/Struct处理'],
                            ['优化与函数', 'MapJoin/Bucket Join', '分区裁剪与列裁剪', '向量化与CBO', 'JVM重用与压缩', 'UDF/UDAF/UDTF开发'],
                            ['引擎与权限', 'Hive on Tez/Spark', 'LLAP', 'HiveServer2/JDBC', 'Kerberos认证', '事务与ACID']
                        ]
                    },
                    'Kafka': {
                        'desc': '高吞吐量消息队列，数据采集和传输',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心概念', 'Topic/Partition/Replication', 'Producer/Consumer/Consumer Group', 'Offset/ISR/HW/LEO', 'Broker与Controller', 'ZooKeeper/KRaft'],
                            ['生产者与消费者', 'acks与重试机制', '幂等与事务', '分区策略', '手动/自动提交Offset', 'Rebalance与分配策略'],
                            ['Connect与Streams', 'Source/Sink Connector', 'JDBC/ES/HDFS连接器', 'KStream/KTable', '窗口与状态存储', 'Exactly-Once语义'],
                            ['运维与安全', 'JMX/Prometheus监控', '吞吐与延迟优化', 'Page Cache与零拷贝', 'SASL/SSL/Kerberos', 'ACL授权', 'MirrorMaker跨集群']
                        ]
                    },
                    'Spark': {
                        'desc': '大数据分布式计算框架，支持批处理和流处理',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心RDD', 'RDD创建与转换(map/filter/reduceByKey)', '宽窄依赖与Stage', '缓存与持久化', '广播变量与累加器'],
                            ['Spark SQL/DataFrame', 'DataFrame读写(CSV/Parquet/JDBC)', 'select/join/groupBy', 'UDF与Pandas UDF', '窗口函数', '数组/JSON处理'],
                            ['流处理', 'Structured Streaming(输入源/输出)', '窗口与水印', '状态管理', 'Kafka集成', 'Trigger与容错'],
                            ['优化与部署', 'Catalyst优化器', 'Tungsten列式存储', 'Broadcast Join/Shuffle优化', '动态资源分配', 'YARN/K8s部署', 'ML Pipeline']
                        ]
                    },
                    '数据仓库': {
                        'desc': '维度建模、事实表设计、星型/雪花模型',
                        'difficulty': 2,
                        'dimensions': [
                            ['建模方法论', 'Kimball vs Inmon', '星型/雪花/星座模型', '事实表类型(事务/周期/累积)', '粒度与一致性维度', '总线架构'],
                            ['维度设计', '代理键与自然键', '缓慢变化维(SCD Type1/2/3)', '拉链表', '退化维度/杂项维度', '日期与角色扮演维度'],
                            ['事实表设计', '可加/半可加指标', '事实表粒度', '累积快照设计', '事务事实与周期快照区别', '多维交叉事实'],
                            ['分层与落地', 'ODS/DWD/DWS/ADS分层', '数据域与主题划分', 'Hive/ClickHouse/Doris建模', '实时数仓(Lambda/Kappa)', '湖仓一体']
                        ]
                    },
                    '数据治理': {
                        'desc': '数据质量、元数据管理、数据血缘',
                        'difficulty': 2,
                        'dimensions': [
                            ['数据质量', '完整性/准确性/一致性', '及时性/唯一性/有效性', '质量规则与检测', '质量报告与监控', '改进闭环'],
                            ['元数据与血缘', '技术/业务/操作元数据', 'Apache Atlas/DataHub', '字段级/表级/ETL血缘', '影响分析与追溯', '元数据采集与标准'],
                            ['主数据管理', '主数据(MDM)识别', '客户/产品/供应商主数据', '主数据建模与集成', '主数据平台与治理'],
                            ['安全与合规', '数据分类分级', '敏感数据脱敏(静态/动态)', '数据加密与访问控制', '行/列级安全', 'GDPR/个保法合规']
                        ]
                    },
                    '数据湖': {
                        'desc': '存储原始格式的大规模数据',
                        'difficulty': 2,
                        'dimensions': [
                            ['概念与存储', '数据湖vs数据仓库', 'Schema-on-Read', 'HDFS/S3/OSS对象存储', 'Parquet/ORC/Avro格式', '列式存储与压缩'],
                            ['湖仓格式', 'Delta Lake(ACID/Time Travel/CDF)', 'Apache Iceberg(分区演进/快照)', 'Apache Hudi(COW/MOR/Upsert)', 'Catalog(Hive/Glue/REST)'],
                            ['分层与治理', 'Bronze/Silver/Gold分层', '元数据与血缘(Atlas/DataHub)', '数据质量与安全', '小文件合并与优化', '查询引擎(Presto/Trino/Spark)']
                        ]
                    },
                    '调度系统': {
                        'desc': 'Airflow、DolphinScheduler等任务调度',
                        'difficulty': 2,
                        'dimensions': [
                            ['Airflow基础', '架构(WebServer/Scheduler/Executor)', 'DAG定义(default_args/interval)', 'Operator(Bash/Python/SQL)', '任务依赖与Trigger Rule', 'XCom/Variable/Connection'],
                            ['Airflow进阶', 'TaskGroup/SubDAG', 'Pool/SLA/重试', 'KubernetesPodOperator', '自定义Hook/Provider', 'REST API与CLI'],
                            ['DolphinScheduler', 'Master/Worker架构', 'Shell/SQL/Spark/Flink任务', '条件分支与子流程', '资源中心与租户', '定时与告警(钉钉/邮件)'],
                            ['其他工具', 'Oozie(Coordinator/Bundle)', 'Azkaban', 'Prefect', 'Dagster/DataOps', '调度选型对比']
                        ]
                    },
                    '大数据技术': {
                        'desc': '分布式系统和大数据架构设计',
                        'difficulty': 3,
                        'dimensions': [
                            ['数据采集', 'Flume/Sqoop', 'Kafka/FileBeat', 'CDC(Debezium/Canal)', 'DataX/Sync', '实时采集与批量导入'],
                            ['存储与计算', 'HDFS/HBase/Kudu', 'Hive/Spark/Flink', 'Presto/Impala/ClickHouse', 'Doris/StarRocks', '批流一体'],
                            ['架构与平台', 'Lambda/Kappa架构', '实时数仓与湖仓一体', '数据服务(API)', '多租户与资源隔离', 'Ranger/Kerberos安全'],
                            ['运维与优化', 'HA与故障转移', '集群监控与扩容', '数据倾斜/小文件处理', 'JVM与GC调优', '备份恢复与容灾']
                        ]
                    }
                }
            }
        }
    }
}