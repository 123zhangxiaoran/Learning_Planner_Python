"""大数据开发工程师数据"""
data = {
    '计算机与信息技术': {
        '大数据': {
            '大数据开发工程师': {
                'description': '开发大数据平台，处理海量数据的存储和计算。',
                'skills': {
                    'Hadoop': {
                        'desc': 'HDFS分布式存储和MapReduce计算',
                        'difficulty': 2,
                        'dimensions': [
                            ['HDFS基础与读写', 'NameNode/DataNode', 'Block块', '读写流程', '副本机制'],
                            ['HDFS架构与高可用', '联邦/Federation', 'HA高可用', 'ViewFS', '快照'],
                            ['MapReduce计算', 'Mapper/Reducer', 'Shuffle过程', 'Combiner', 'Input/OutputFormat'],
                            ['YARN资源管理', 'ResourceManager/NodeManager', '调度器(FIFO/Capacity/Fair)', 'Container', '应用提交流程'],
                            ['运维与命令', 'hdfs dfs常用命令', 'fsck检查', 'dfsadmin管理', 'Balancer均衡']
                        ]
                    },
                    'Hive': {
                        'desc': '数据仓库工具，SQL方式查询Hadoop数据',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与元数据', 'Driver/Compiler', 'Metastore服务', '内部表/外部表', '分区表/分桶表'],
                            ['查询与函数', 'UDF/UDAF/UDTF', '窗口函数', 'Lateral View', '复杂数据类型(Array/Map/Struct)'],
                            ['优化策略', 'JOIN优化(MapJoin/Bucket Join)', '谓词下推', '列裁剪', '分区裁剪', '向量化执行'],
                            ['高级特性', 'Cube/Rollup', '物化视图', '事务与ACID', 'Hive on Tez/Spark']
                        ]
                    },
                    'Spark': {
                        'desc': '内存计算引擎，支持SQL、流处理、机器学习',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与RDD', 'Driver/Executor', 'RDD弹性数据集', '宽窄依赖', 'Stage与Task'],
                            ['DataFrame与SQL', 'DataFrame/Dataset', 'Spark SQL', 'Catalyst优化器', 'Tungsten列式存储'],
                            ['流处理', 'Spark Streaming(DStream)', 'Structured Streaming', '窗口与水印', 'Kafka集成'],
                            ['优化与运维', 'Shuffle优化', 'Broadcast变量', 'Checkpoint', '动态资源分配', 'Spark on YARN/K8s'],
                            ['MLlib与GraphX', '机器学习流水线', '常见算法(ALS/决策树)', '图计算基础']
                        ]
                    },
                    'Kafka': {
                        'desc': '高吞吐量消息队列',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心架构', 'Broker/Topic/Partition', '副本与ISR', 'Leader/Follower', 'Offset管理'],
                            ['生产者与消费者', 'acks确认机制', '幂等性与事务', 'Consumer Group', 'Rebalance与分配策略'],
                            ['高级特性', 'Exactly-Once语义', 'Kafka Streams流处理', 'KTable/KStream', '窗口操作'],
                            ['运维与集成', 'Kafka Connect', 'MirrorMaker跨集群', 'JMX监控', '性能调优']
                        ]
                    },
                    'Flink': {
                        'desc': '实时流处理框架',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与部署', 'JobManager/TaskManager', 'Slot与并行度', 'YARN/K8s部署'],
                            ['DataStream API', 'Source/Sink', 'map/filter/keyBy', 'ProcessFunction', '侧输出'],
                            ['窗口与水印', '时间语义(Event/Processing)', '滚动/滑动/会话窗口', 'Watermark机制', '迟到数据处理'],
                            ['状态与容错', 'Keyed State/Operator State', 'Checkpoint与Savepoint', 'Exactly-Once状态一致性', 'RocksDB后端'],
                            ['Table API与SQL', 'Flink SQL', 'UDF/UDAF/UDTF', '窗口聚合(TUMBLE/HOP)', 'CEP复杂事件处理']
                        ]
                    },
                    'HBase': {
                        'desc': '分布式列式存储数据库',
                        'difficulty': 2,
                        'dimensions': [
                            ['数据模型与架构', 'RowKey/Column/Family', 'Master/RegionServer', 'ZooKeeper协调'],
                            ['存储与读写', 'WAL/MemStore/HFile', 'Get/Put/Scan操作', 'Filter过滤器', 'BulkLoad批量导入'],
                            ['优化与设计', 'RowKey设计原则', '预分区/热点问题', '协处理器(Coprocessor)', 'Phoenix SQL层']
                        ]
                    },
                    'ClickHouse': {
                        'desc': '列式OLAP数据库',
                        'difficulty': 2,
                        'dimensions': [
                            ['表引擎与存储', 'MergeTree家族', '分区与排序键', '物化视图', 'AggregatingMergeTree'],
                            ['查询与SQL', 'DISTINCT/GROUP BY优化', 'JOIN策略', '向量化执行', '数据类型与压缩'],
                            ['分布式与高可用', '副本(ReplicatedMergeTree)', '分片(Distributed表)', '集群管理', '扩容缩容']
                        ]
                    },
                    'Doris': {
                        'desc': '国产MPP分析型数据库',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与导入', 'Frontend/Backend', 'Stream Load/Routine Load', 'Broker Load', '数据模型(Unique/Aggregate/Duplicate)'],
                            ['物化视图与查询', 'Rollup物化', 'BitMap索引', '查询优化器', '谓词下推', 'Colocate Join'],
                            ['运维与扩展', 'FE/BE扩缩容', '副本与故障恢复', '监控与告警', '多租户']
                        ]
                    },
                    '数据湖': {
                        'desc': 'Delta Lake、Iceberg、Hudi',
                        'difficulty': 2,
                        'dimensions': [
                            ['Delta Lake', 'ACID事务', 'Time Travel时间旅行', 'Schema演进', 'Z-Ordering优化'],
                            ['Iceberg', '隐藏分区', '分区演进', '快照与回滚', 'Manifest管理'],
                            ['Hudi', 'COW/MOR表类型', 'Upsert/Insert', '快照查询', '增量查询'],
                            ['湖仓一体', '湖仓一体概念', '数据湖架构设计', 'Presto/Trino查询引擎', '数据湖治理']
                        ]
                    },
                    '数据治理': {
                        'desc': '元数据管理、数据质量、血缘分析',
                        'difficulty': 2,
                        'dimensions': [
                            ['元数据管理', 'DataHub/Atlas', '数据目录', '技术/业务元数据'],
                            ['数据质量', 'DQ规则配置', '完整性/准确性/一致性检测', '异常告警', '质量报告'],
                            ['数据血缘', '血缘解析(Spark/Hive)', '字段级血缘', '影响分析与追溯'],
                            ['数据标准与安全', '数据标准落地', '敏感数据识别', '数据脱敏', '合规审计']
                        ]
                    },
                    '任务调度': {
                        'desc': 'Airflow、DolphinScheduler',
                        'difficulty': 2,
                        'dimensions': [
                            ['Airflow', 'DAG定义', 'Operator(Bash/Python)', 'XCom通信', 'schedule_interval调度'],
                            ['任务编排', '任务依赖与重试', 'Trigger Rule', 'SLA监控', '跨DAG触发'],
                            ['DolphinScheduler', '工作流定义', '任务节点(Shell/Spark)', '定时与告警', '租户与资源管理'],
                            ['通知与集成', '邮件/钉钉/飞书通知', '与Hadoop生态集成', '任务监控面板']
                        ]
                    },
                    '资源调度': {
                        'desc': 'YARN、Kubernetes',
                        'difficulty': 2,
                        'dimensions': [
                            ['YARN', 'ResourceManager/NodeManager', 'Container分配', '调度器策略', '队列管理'],
                            ['Kubernetes基础', 'Pod/Deployment', 'Service', 'ConfigMap/Secret', 'PV/PVC'],
                            ['Kubernetes高级', 'Ingress', 'HPA自动伸缩', 'Helm Charts', 'Operator模式'],
                            ['集群管理', 'Kubeadm部署', '监控(Prometheus)', '日志收集(EFK)', '安全(RBAC)']
                        ]
                    },
                    'SQL优化': {
                        'desc': '大数据SQL查询优化',
                        'difficulty': 3,
                        'dimensions': [
                            ['执行计划分析', 'EXPLAIN解读', '谓词下推', '列裁剪', '分区裁剪'],
                            ['JOIN优化', '小表广播(Broadcast Join)', 'SortMerge Join', 'Bucket Join', '数据倾斜处理'],
                            ['内存与并行', 'Shuffle分区数设置', '堆外内存管理', 'GC调优', '并行度调整'],
                            ['引擎特定优化', 'Spark AQE自适应查询', 'Flink MiniBatch优化', 'Hive CBO优化']
                        ]
                    }
                }
            }
        }
    }
}