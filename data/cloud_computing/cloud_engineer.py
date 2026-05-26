"""云计算工程师数据"""
data = {
    '计算机与信息技术': {
        '云计算': {
            '云计算工程师': {
                'description': '设计和维护云架构，管理和优化云资源。',
                'skills': {
                    'AWS': {
                        'desc': '亚马逊云服务架构设计和部署，EC2、S3、RDS等',
                        'difficulty': 2,
                        'dimensions': [
                            ['计算与伸缩', 'EC2实例类型与AMI', '安全组', 'Auto Scaling弹性伸缩', 'ELB/ALB/NLB负载均衡'],
                            ['存储与数据库', 'S3存储类别与生命周期', '权限与加密', 'RDS/Aurora数据库', 'CloudWatch监控与告警'],
                            ['网络与连接', 'VPC/子网/路由表', 'NAT Gateway/Internet Gateway', 'VPC Peering/PrivateLink', 'VPN/Direct Connect专线'],
                            ['身份与安全', 'IAM角色/策略/用户组', '权限边界与最小权限', 'Cognito/SSO集成', '安全审计与合规'],
                            ['无服务器与集成', 'Lambda函数/触发器', 'SQS队列/SNS通知', 'EventBridge事件总线', 'Step Functions工作流'],
                            ['容器与编排', 'EKS容器服务', 'ECS/Fargate', 'ECR镜像仓库', 'CloudFormation/Infrastructure as Code'],
                            ['成本与优化', 'Cost Explorer成本报告', '预留/竞价实例', '预算告警', '资源标签与成本归集']
                        ]
                    },
                    'Azure': {
                        'desc': '微软云平台服务管理和开发',
                        'difficulty': 2,
                        'dimensions': [
                            ['计算与容器', 'VM/规模集', 'AKS集群', '应用服务(App Service)', '容器实例/函数计算'],
                            ['存储与数据库', 'Azure Storage(Blob/Queue/Table)', 'SQL/MySQL/PostgreSQL', 'Cosmos DB', '数据湖与备份'],
                            ['网络与安全', 'VNet/子网/NSG', '负载均衡器/应用网关', 'VPN/ExpressRoute', '防火墙/DDoS防护'],
                            ['身份与管理', 'Azure AD/Entra ID', 'RBAC角色', '策略与蓝图', 'Key Vault密钥管理'],
                            ['DevOps与监控', 'Azure DevOps管道', 'Application Insights', 'Monitor/日志分析', 'ARM模板/Terraform支持'],
                            ['成本与治理', '成本管理/预算', '资源标签', 'Azure Policy合规', '预留实例优化']
                        ]
                    },
                    'Docker': {
                        'desc': '容器化技术应用部署',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心概念', '镜像/容器/仓库', 'Dockerfile指令(FROM/RUN/COPY/ENTRYPOINT)', '镜像构建与分层', '多阶段构建与缓存优化'],
                            ['网络与存储', '网络驱动(bridge/host/overlay/macvlan)', '数据卷/挂载/持久化', '存储驱动与性能', '网络配置与互联'],
                            ['编排与工具', 'Docker Compose多容器', 'Swarm集群管理', '服务部署与滚动更新', '私有仓库/Harbor'],
                            ['安全与运维', '镜像安全扫描', '资源限制(CPU/内存/IO)', '日志收集与监控', 'Dockerfile最佳实践']
                        ]
                    },
                    'Kubernetes': {
                        'desc': '容器编排和集群管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心工作负载', 'Pod/Deployment/ReplicaSet', 'Service(ClusterIP/NodePort/LB)', 'StatefulSet有状态应用', 'Job/CronJob定时任务'],
                            ['配置与存储', 'ConfigMap/Secret', 'PersistentVolume/PVC', 'StorageClass动态供应', '环境变量与配置注入'],
                            ['网络与安全', 'Ingress/域名路由/TLS', 'NetworkPolicy网络策略', 'RBAC/ServiceAccount权限', 'Pod安全策略/上下文'],
                            ['调度与伸缩', 'HPA/VPA自动伸缩', '资源配额/限制范围', '污点容忍/亲和性', 'PodDisruptionBudget'],
                            ['包管理', 'Helm Charts/仓库', 'Kustomize配置差异化', 'Operator模式', '集群升级与维护'],
                            ['部署与运维', 'kubeadm/kubespray部署', '集群监控(Prometheus)', '日志收集(EFK/ELK)', '备份与灾难恢复']
                        ]
                    },
                    'Serverless': {
                        'desc': '无服务器架构，Lambda、函数计算',
                        'difficulty': 2,
                        'dimensions': [
                            ['概念与平台', '事件驱动架构', 'AWS Lambda/触发器', 'Azure Functions', '阿里云/腾讯云函数计算'],
                            ['开发与集成', '运行时(Python/Node.js/Java)', '依赖打包/Layers', 'API Gateway/HTTP API', 'IAM角色/资源策略'],
                            ['框架与工具', 'Serverless Framework', 'SAM/Claudia.js', 'Terraform部署', '本地调试与测试'],
                            ['性能与成本', '冷启动优化/预置并发', '按调用计费模型', '无服务器数据库(DynamoDB/CosmosDB)', '成本分析与优化']
                        ]
                    },
                    'Terraform': {
                        'desc': '基础设施即代码自动化部署',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心语法', 'HCL语言/Provider', '资源(resource)/数据源(data)', '变量(variable)/输出(output)', 'locals本地值'],
                            ['命令与状态', 'init/plan/apply/destroy', '状态文件与远程后端', '状态锁与协作', 'workspace环境隔离'],
                            ['模块与复用', 'module定义与调用', 'Registry公共模块', '私有模块仓库', '版本约束与升级'],
                            ['高级特性', 'Provisioner远程执行', 'count/for_each循环', '动态块/条件表达式', 'terraform import导入'],
                            ['最佳实践', '代码结构与命名规范', 'CI/CD集成', '策略即代码(Sentinel/OPA)', 'Terraform Cloud/Enterprise']
                        ]
                    },
                    '云原生': {
                        'desc': '微服务、容器化、DevOps、持续交付',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与方法论', '12要素应用', '微服务拆分与治理', 'DDD领域驱动设计', 'CQRS与事件溯源'],
                            ['服务治理', '服务发现(Consul/Eureka/Nacos)', 'API网关(Kong/Envoy)', '熔断器(Sentinel/Hystrix)', '配置中心(Apollo/Nacos)'],
                            ['CI/CD与GitOps', 'Jenkins/GitLab CI', 'GitOps(ArgoCD/Flux)', '镜像构建与扫描', '金丝雀/蓝绿部署'],
                            ['可观测性与安全', '分布式追踪(Jaeger/Zipkin/SkyWalking)', '日志/监控/告警', 'Prometheus/Grafana', 'Secret管理/Vault/网络策略']
                        ]
                    },
                    '云架构': {
                        'desc': '高可用、高并发、弹性伸缩架构设计',
                        'difficulty': 2,
                        'dimensions': [
                            ['高可用与容错', '多可用区/跨区域部署', '负载均衡与健康检查', '数据库读写分离/分库分表', '消息队列异步解耦'],
                            ['弹性与伸缩', '水平/垂直扩展', 'Auto Scaling策略', '无状态服务设计', '容器化弹性调度'],
                            ['性能与缓存', 'CDN加速与全球分发', 'Redis缓存集群', '分布式存储(Ceph/MinIO)', '限流熔断/降级兜底'],
                            ['灾备与安全', '容灾设计与演练', '备份与恢复策略', '安全组/防火墙/零信任', '数据加密与隐私保护'],
                            ['成本与治理', '成本优化/资源利用率', '架构评审与文档', 'FinOps云财务管理', '标签策略与成本归集']
                        ]
                    },
                    '多云管理': {
                        'desc': '跨云平台的统一管理和迁移',
                        'difficulty': 2,
                        'dimensions': [
                            ['战略与迁移', '多云战略/利弊分析', '跨云迁移工具', '应用改造与适配', '数据同步与校验'],
                            ['统一编排', 'Terraform/Pulumi多Provider', 'Crossplane控制平面', 'Ansible多云配置', 'Kubernetes联邦/多集群'],
                            ['网络与连通', '多云专线/VPN', '全局流量管理(GTM)', 'DNS策略(GeoDNS)', '网络延迟与带宽优化'],
                            ['安全与合规', '统一身份管理(IAM)', '策略即代码(OPA)', '多云审计与日志', '数据驻留与合规'],
                            ['监控与运维', '统一监控(Prometheus/Thanos)', 'Grafana多数据源', '告警聚合与降噪', '成本对比与优化']
                        ]
                    },
                    '成本优化': {
                        'desc': '云资源成本分析和优化',
                        'difficulty': 2,
                        'dimensions': [
                            ['模型与分析', '按需/预留/竞价实例', '成本可视化与报表', '成本异常检测', '资源利用率分析'],
                            ['优化策略', '右-sizing实例', '存储生命周期与归档', '无服务器成本优化', '网络流量与CDN优化'],
                            ['预留与竞价', '预留实例/Savings Plans', 'Spot实例与中断处理', '资源包与包年包月', '混合计费模式'],
                            ['治理与运营', '标签策略与成本归集', '预算告警', '成本展示与KPI', 'FinOps文化与流程']
                        ]
                    },
                    '网络规划': {
                        'desc': 'VPC、子网、安全组设计',
                        'difficulty': 2,
                        'dimensions': [
                            ['VPC与子网', 'CIDR规划与IP管理', '公有/私有子网划分', '多VPC对等/Transit Gateway', '子网路由与ACL'],
                            ['网关与连接', 'Internet Gateway/NAT', 'VPN/Direct Connect', 'VPC Endpoint/PrivateLink', 'Bastion Host跳板机'],
                            ['安全与流量', '安全组/网络ACL', '网络防火墙/WAF', 'VPC Flow Logs分析', 'DDoS防护'],
                            ['DNS与负载', 'Route 53/Private Zone', '负载均衡器选择', '全局加速与Anycast', '网络性能监控']
                        ]
                    },
                    '腾讯云': {
                        'desc': '腾讯云产品架构和部署',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心计算', 'CVM云服务器/竞价实例', '批量计算/黑石', '容器服务TKE/Kubernetes', '弹性伸缩AS'],
                            ['存储与数据库', 'COS对象存储', '云数据库(MySQL/Redis/TDSQL)', 'CFS文件存储', '数据迁移/备份'],
                            ['网络与安全', 'VPC私有网络/子网/路由表', 'CLB负载均衡', 'NAT/Internet Gateway', '安全组/DDoS/WAF'],
                            ['无服务器与应用', '云函数SCF', 'API网关', '微服务引擎TSF', '云开发TCB'],
                            ['监控与管理', '云监控/云审计', 'CODING DevOps', '日志服务CLS', '成本管理/资源包']
                        ]
                    },
                    '阿里云': {
                        'desc': '国内主流云服务使用',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心计算', 'ECS云服务器/弹性裸金属', '容器服务ACK/Kubernetes', '弹性伸缩/资源编排ROS', '函数计算FC'],
                            ['存储与数据库', 'OSS对象存储/NAS', 'RDS/MySQL/PostgreSQL/PolarDB', 'Redis/MongoDB', '表格存储OTS'],
                            ['网络与安全', 'VPC专有网络/交换机/路由表', 'SLB/ALB/NLB负载均衡', 'NAT/VPN/高速通道', 'DDoS高防/WAF/云防火墙'],
                            ['应用与集成', 'API网关', '微服务MSF/Nacos', 'Spring Cloud Alibaba', '事件总线EventBridge'],
                            ['管理与运维', '云监控/日志服务SLS', '云效DevOps', 'RAM/资源管理', '成本管家/预算']
                        ]
                    }
                }
            }
        }
    }
}