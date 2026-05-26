# 技能难度定义：1=基础入门，2=主流技术，3=进阶/专业
# 计算机专业数据 - 添加岗位描述和技能难度
computer_data = {
    '区块链': {
        '区块链开发工程师': {
            'description': '开发区块链应用和智能合约，构建去中心化系统。',
            'skills': {
                'Go': {
                    'desc': '区块链底层开发，如Fabric、以太坊客户端',
                    'difficulty': 1,
                    'dimensions': ['Go基础语法/数据类型', 'Goroutine协程/并发', 'Channel通道通信', 'defer/panic/recover', 'net/http网络编程', 'gRPC框架', 'database/sql', 'Redis客户端', 'Protocol Buffer', '日志/zap/logrus', '测试/testing', 'Docker容器化', '微服务架构', '密码学基础', '区块链sdk/go-ethereum']
                },
                'Rust': {
                    'desc': '高性能区块链开发，如Solana、Polkadot',
                    'difficulty': 1,
                    'dimensions': ['Rust基础/所有权/借用', '数据类型/结构体/枚举', 'Trait特征/接口', 'Error处理', 'Option/Result', 'Iterator迭代器', '生命周期/Lifetime', '并发/Send/Sync', 'Async/Await异步', 'Crates包管理', 'Cargo构建', '宏/Macro', '所有权系统', '智能指针/Box', 'WASM编译']
                },
                'Solidity': {
                    'desc': '以太坊智能合约开发语言',
                    'difficulty': 1,
                    'dimensions': ['Solidity语法/版本', '数据类型/int/address/string', '函数可见性/public/private', '函数修饰符/modifier', '事件/Event', '继承/接口', '库/Library', 'Fallback函数', 'Receive函数', 'Gas优化', '存储/内存/Memory', 'Try/Catch', 'ABI接口', 'Web3.py调用', '合约安全']
                },
                'DApp开发': {
                    'desc': '去中心化应用前后端开发',
                    'difficulty': 2,
                    'dimensions': ['DApp架构/前端+合约', 'Web3.js连接钱包', 'ethers.js库', 'MetaMask钱包集成', '合约交互/Call/Send', '签名交易', '前端框架/React/Vue', 'IPFS去中心化存储', 'ENS域名解析', 'Chainlink预言机', '去中心化身份/DID', 'DApp部署/IPFS', 'Gas费用计算', '测试网/Faucet', '主网部署']
                },
                'NFT': {
                    'desc': '非同质化代币标准和应用',
                    'difficulty': 2,
                    'dimensions': ['NFT标准/ERC721/ERC1155', 'TokenURI元数据', 'IPFS存储/NFT metadata', '铸造/Mint NFT', '转移/Transfer', '所有权/Owner', '批量铸造/Batch', 'NFT市场/OpenSea', 'NFT合约开发', 'ERC721A优化', 'NFT安全性检查', '版税机制/Royalty', '链上元数据/On-chain', '动态NFT', 'NFT游戏化']
                },
                'Web3.js': {
                    'desc': '与区块链交互的JavaScript库',
                    'difficulty': 2,
                    'dimensions': ['Web3.js安装配置', 'Provider连接/HttpProvider', 'Web3实例创建', '账户/Accounts', '合约实例/Contract', '交易/SendTransaction', '事件监听/Events', '签名/Sign', 'Call调用/read', 'Gas估算', '区块查询/Block', '日志查询/Filter', 'ABI接口', '合约部署/Deploy', '测试网连接']
                },
                '以太坊': {
                    'desc': 'EVM原理、Gas机制、交易流程',
                    'difficulty': 2,
                    'dimensions': ['以太坊概述/ETH', 'EVM虚拟机原理', '账户/EOA/Contract', '交易结构/nonce/gas/value', 'Gas费用/GasPrice/GasLimit', '区块结构/Header', 'Merkle Tree/Patricia Trie', 'Solidity语言', 'EVM执行/Opcode', '预编译合约', '叔块/Uncle', '难度调整/Difficulty', 'Ethash工作量证明', '账户抽象/AA', '分片/Sharding']
                },
                '链上数据分析': {
                    'desc': '区块链浏览器、事件监听',
                    'difficulty': 2,
                    'dimensions': ['Etherscan浏览器', '区块查询/Block Number', '交易查询/TxHash', '合约事件/Events', '日志解析/Log', 'ABI解码', '链上数据/The Graph', 'GraphQL查询', '链分析/Dune Analytics', 'Grafana链上监控', 'Nansen工具', '合约调用追踪', 'Flashbots/MEV', '代币转账追踪', '鲸鱼地址追踪']
                },
                'DeFi': {
                    'desc': '去中心化金融协议开发',
                    'difficulty': 3,
                    'dimensions': ['DeFi概述/AMM/借贷', 'Uniswap兑换协议', 'DEX流动性', 'AMM公式/x*y=k', '流动性挖矿/Liquidity Mining', 'Compound借贷', 'Aave闪电贷', 'Yield Farming', '代币Swap', '流动性池/LP', '无常损失/IL', '预言机喂价/Chainlink', 'DeFi聚合器/Yearn', '治理代币/Governance', 'DeFi安全审计']
                },
                '共识算法': {
                    'desc': 'PoW、PoS、DPoS等共识机制',
                    'difficulty': 3,
                    'dimensions': ['共识算法概述', 'PoW工作量证明', 'SHA256哈希', '挖矿/Mining', '区块奖励/Block Reward', '难度调整/Difficulty Target', 'PoS权益证明', '验证者/Validator', '质押/Staking', 'BFT拜占庭容错', 'PBFT实用拜占庭', 'DPoS委托权益', 'Tendermint', 'HotStuff', 'Casper FFG']
                },
                '密码学': {
                    'desc': '哈希、签名、零知识证明',
                    'difficulty': 3,
                    'dimensions': ['哈希函数/SHA256/Keccak', 'Merkle Tree', '椭圆曲线/ECC/secp256k1', 'ECDSA签名', '公钥/私钥', '数字签名', '零知识证明/ZK-SNARKs', 'ZK-STARKs', 'Merkle Proof', 'Pedersen承诺', 'Poseidon哈希', '环签名/Ring Signature', '多签/Multisig', '门限签名/TSS', '同态加密']
                },
                '智能合约': {
                    'desc': '编写、测试、部署智能合约',
                    'difficulty': 3,
                    'dimensions': ['智能合约概述', 'Solidity开发环境/Truffle/Hardhat', '合约编写/ERC20/ERC721', '测试框架/Waffle/Mocha', '部署脚本', 'Truffle Migrations', 'Hardhat配置', 'OpenZeppelin库', '合约安全漏洞/Reentrancy', '安全审计/Slither', '形式化验证', 'Gas优化技巧', '代理合约/EIP1167', '升级合约/UUPS/Transparent', '多链部署']
                }
            }
        }
    },
    '大数据': {
        '大数据开发工程师': {
            'description': '开发大数据平台，处理海量数据的存储和计算。',
            'skills': {
                'ClickHouse': {
                    'desc': '列式OLAP数据库',
                    'difficulty': 2,
                    'dimensions': ['ClickHouse概述/OLAP特点', 'MergeTree表引擎', '分区/Partition', '主键/索引', 'ReplacingMergeTree', 'AggregatingMergeTree', 'SummingMergeTree', 'TTL生存时间', '物化视图/Materialized View', 'ClickHouse分区裁剪', '列式存储压缩', 'SQL语法/DISTINCT/GROUP BY', 'Join优化/SHARD本地表', '副本/Replication', '分片/Shard/分布式表', '数据类型/String/FixedString']
                },
                'Doris': {
                    'desc': '国产MPP分析型数据库',
                    'difficulty': 2,
                    'dimensions': ['Doris架构/Frontend/Backend', 'Broker导入/HTTP', 'Stream Load流式导入', 'Routine Load例行导入', 'MySQL协议连接', 'Tablet分片', 'Rollup物化视图', 'BitMap聚合', 'BloomFilter索引', '分区表/Range/List', 'FE/BE扩容缩容', 'Colocation Join', 'Stream Load/Batch Load', '查询优化/谓词下推', '数据模型/Aggregate/Unique/Duplicate']
                },
                'Flink': {
                    'desc': '实时流处理框架',
                    'difficulty': 2,
                    'dimensions': ['Flink架构/JobManager/TaskManager', 'DataSet/DataStream API', 'Source/Sink连接器', 'Kafka Source连接', 'Redis Sink连接', 'Window窗口/Tumbling/Sliding', 'Time语义/Event Time/Processing Time', 'Watermark水位线', '状态管理/Checkpoint', 'Exactly-Once语义', 'Flink SQL', 'Table API', 'CEP复杂事件处理', '异步IO/AsyncFunction', '背压/Back Pressure']
                },
                'HBase': {
                    'desc': '分布式列式存储数据库',
                    'difficulty': 2,
                    'dimensions': ['HBase数据模型/RowKey/Column/Family', 'HBase架构/Master/RegionServer', 'Region分裂/负载均衡', 'WAL预写日志', 'MemStore/HFile', 'HFile compaction', 'Scan扫描/Filter过滤', 'Get/Put/Delete操作', '协处理器/Coprocessor', 'Phoenix二级索引', 'BulkLoad批量导入', 'HBase集群部署', 'RowKey设计原则', '布隆过滤器/BloomFilter', '快照/Snapshot']
                },
                'Hadoop': {
                    'desc': 'HDFS分布式存储和MapReduce计算',
                    'difficulty': 2,
                    'dimensions': ['HDFS架构/Namenode/Datanode', 'Block块存储/副本机制', 'HDFS命令/fsck/dfsadmin', 'HDFS读写流程', '机架感知/Rack Awareness', '联邦/Federation', 'HA高可用', 'MapReduce编程模型', 'Mapper/Reducer', 'Combiner/Partitioner', 'Shuffle Sort阶段', 'YARN架构/ResourceManager', 'YARN调度器/FIFO/Capacity/Fair', 'HDFS安全模式', 'HDFS优缺点']
                },
                'Hive': {
                    'desc': '数据仓库工具，SQL方式查询Hadoop数据',
                    'difficulty': 2,
                    'dimensions': ['Hive架构/Driver/Compiler/Optimizer', 'Hive Metastore', '内部表/外部表', '分区表/Partition', '动态分区/静态分区', '分桶表/Bucketed', 'SerDe序列化', 'JOIN优化/Map Join', 'UDF/UDAF/UDTF', '窗口函数/Lead/Lag', 'Lateral View/炸裂函数', 'HiveQL语法', 'Cube/Rollup', '物化视图', 'Hive on Spark/Tez']
                },
                'Kafka': {
                    'desc': '高吞吐量消息队列',
                    'difficulty': 2,
                    'dimensions': ['Kafka架构/Broker/Topic/Partition', '分区副本/Replica/ISR', '生产者/消费者', 'acks确认机制', '幂等性/Transaction', '消费者组/Consumer Group', 'offset提交/自动/手动', '消息压缩/Snappy/GZIP', '主题配置/Retention', '分区策略/Key路由', 'Kafka Connect', 'Kafka Streams', 'Exactly-Once语义', '控制器/Controller', 'Leader选举']
                },
                'Spark': {
                    'desc': '内存计算引擎，支持SQL、流处理、机器学习',
                    'difficulty': 2,
                    'dimensions': ['Spark架构/Driver/Executor', 'RDD弹性分布式数据集', 'Transformation/Action', 'Shuffle过程', 'Broadcast广播变量', '累加器/Accumulator', 'Spark SQL/DataFrame/Dataset', 'Dataset API', 'Spark Streaming', 'Structured Streaming', '窗口操作', 'Checkpoint检查点', 'Spark MLlib', 'Spark GraphX', 'Tungsten内存管理']
                },
                '任务调度': {
                    'desc': 'Airflow、DolphinScheduler',
                    'difficulty': 2,
                    'dimensions': ['Airflow架构/Scheduler/WebServer', 'DAG有向无环图', 'Operator操作符/Bash/Python/SQL', 'Task任务/Instance实例', 'DAG依赖/dag_id/task_id', 'XCom数据传递', 'Airflow变量/Connection', '调度周期/schedule_interval', '任务重试/retry', 'DolphinScheduler架构', '租户管理/项目', '工作流定义/拖拽', '任务节点/Spark/Flink/SQL', '告警机制/邮件', '跨租户调度']
                },
                '数据治理': {
                    'desc': '元数据管理、数据质量、血缘分析',
                    'difficulty': 2,
                    'dimensions': ['元数据管理/DataHub', 'Apache Atlas血缘', '数据质量/DQ规则', '数据目录/Catalog', '敏感数据/脱敏', '数据标准/规范', '数据血缘/Lineage', '字段级血缘', '数据资产/资产地图', '数据标签/分类', '质量管理/完整性', '数据标签化/Tag', '异常数据检测', '治理流程/管理规范', '指标管理']
                },
                '数据湖': {
                    'desc': 'Delta Lake、Iceberg、Hudi',
                    'difficulty': 2,
                    'dimensions': ['数据湖概念/湖仓一体', 'Delta Lake架构', 'ACID事务/DML操作', 'Time Travel时间旅行', 'Schema演进', 'Z-Order排序', 'Iceberg架构/表格式', 'Iceberg隐藏分区', '快照/Snapshot', '分区演化', 'Hudi架构/表类型', 'COW Copy-on-write', 'MOR Merge-on-read', 'Hudi查询类型/快照/增量', 'Upsert操作']
                },
                '资源调度': {
                    'desc': 'YARN、Kubernetes',
                    'difficulty': 2,
                    'dimensions': ['YARN架构/ResourceManager/NodeManager', 'YARN调度器/FIFO/Capacity/Fair', 'YARN Container容器', 'ApplicationMaster', 'YARN命令/yarn application', 'Kubernetes架构/Master/Node', 'Pod/Deployment/Service', '命名空间/Namespace', 'Ingress/Service网络', 'ConfigMap/Secret', 'PV/PVC存储', 'HPA自动伸缩', 'Helm Charts', 'Kubeadm部署', 'kubectl命令']
                },
                'SQL优化': {
                    'desc': '大数据SQL查询优化',
                    'difficulty': 3,
                    'dimensions': ['执行计划/EXPLAIN分析', 'Spark执行计划', 'Hive执行计划', '谓词下推/Predicate Pushdown', '列裁剪/Column Pruning', '分区裁剪/Partition Pruning', '小表广播/Broadcast Join', 'Shuffle优化', '数据倾斜/Skew处理', 'Join顺序优化', 'Limit优化', 'Sort Merge Join', 'Bucket Map Join', '内存管理/GC调优', '并行度/spark.sql.shuffle.partitions']
                }
            }
        }
    }
}
