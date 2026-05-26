"""云原生工程师数据"""
data = {
    '计算机与信息技术': {
        '云计算': {
            '云原生工程师': {
                'description': '构建和维护云原生应用和基础设施。',
                'skills': {
                    'ArgoCD': {
                        'desc': 'K8s声明式持续交付工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与理念', 'Application/ApplicationSet', 'GitOps声明式部署', 'ArgoCD安装与配置'],
                            ['部署与同步', '同步策略与Sync Wave', '自动同步与回滚(History/rollback)', 'Helm/Kustomize集成', 'Argo Rollouts(金丝雀/蓝绿)'],
                            ['多集群与通知', '多集群部署(Cluster ADD)', 'Webhook通知', 'Argo Workflows工作流'],
                            ['安全与管理', 'RBAC权限控制', 'Secret集成与密码管理', 'Argo CD Image Updater']
                        ]
                    },
                    'CNI': {
                        'desc': '容器网络接口和网络方案',
                        'difficulty': 2,
                        'dimensions': [
                            ['规范与IPAM', 'CNI规范/接口定义', 'IPAM地址管理', 'Host-local分配'],
                            ['常用插件', 'Flannel(VXLAN)', 'Calico(策略/BGP)', 'Cilium(eBPF)', 'Weave/Macvlan/Vlan'],
                            ['网络模型', 'Bridge/网桥', '网络命名空间与Veth对', 'K8s网络策略/Ingress']
                        ]
                    },
                    'CSI': {
                        'desc': '容器存储接口和存储方案',
                        'difficulty': 2,
                        'dimensions': [
                            ['规范与供给', 'CSI规范(Controller/Node)', 'PV/PVC绑定', 'StorageClass动态供给'],
                            ['存储方案', 'NFS/HostPath/EmptyDir', '公有云驱动(AWS EBS/GCE PD)', 'Ceph RBD/CephFS', 'Longhorn分布式存储'],
                            ['高级功能', 'Local PV持久化', '存储QoS/IOPS限制', '快照/克隆/备份']
                        ]
                    },
                    'Docker': {
                        'desc': '容器技术原理和最佳实践',
                        'difficulty': 2,
                        'dimensions': [
                            ['运行时与架构', '容器运行时(runc)', '镜像分层与联合文件系统', 'Docker Daemon配置', 'Containerd独立运行'],
                            ['镜像与构建', 'Dockerfile最佳实践', '多阶段构建与优化', 'Docker Registry/镜像分发'],
                            ['网络与存储', 'bridge/overlay网络', '存储驱动(overlay2)', 'Docker Compose本地编排'],
                            ['安全与监控', '安全配置文件(Security Profiles)', 'Docker监控(Stats/API)', '日志驱动与收集'],
                            ['集群与编排', 'Swarm Mode集群', '服务部署与滚动更新', '配置与密钥管理']
                        ]
                    },
                    'GitOps': {
                        'desc': '基于Git的持续交付模式',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心原则', '声明式/版本化/自动化', 'Git仓库结构与应用程序仓库'],
                            ['工具与工作流', 'ArgoCD/Flux CD', '开发/staging/prod环境管理', 'Pull Request审核流程'],
                            ['配置与安全', 'Kustomize差异化配置', 'Helm Chart管理', 'Sealed Secrets加密', '代码签名与安全'],
                            ['监控与恢复', '同步状态监控', '灾难恢复(Git回滚)', '多集群GitOps']
                        ]
                    },
                    'Grafana': {
                        'desc': '监控数据可视化',
                        'difficulty': 2,
                        'dimensions': [
                            ['安装与数据源', '安装与配置', 'Prometheus/Loki数据源', '数据源管理'],
                            ['仪表盘与面板', 'Dashboard与Panel', 'Graph/Time Series/Stat图表', '变量模板与动态仪表盘'],
                            ['告警与通知', 'Alert规则/Alertmanager', 'Slack/邮件/Webhook', 'Annotations注解'],
                            ['管理与自动化', '用户/团队/权限', 'Provisioning自动化配置', 'Grafana Cloud托管'],
                            ['探索与日志', 'Explore查询', 'Loki日志', '仪表盘共享与协作']
                        ]
                    },
                    'Helm': {
                        'desc': 'K8s包管理和应用部署',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心与Chart', 'Helm架构(客户端)', 'Chart结构(templates/Chart.yaml/values)', 'Chart仓库(ChartMuseum/Harbor)'],
                            ['模板与渲染', 'Go模板语法', 'Sprig函数库', '条件与with作用域'],
                            ['发布管理', 'install/upgrade/rollback', 'Release状态追踪', 'Hooks生命周期钩子', 'Test Charts'],
                            ['安全与版本', 'Helm3免Tiller', '签名验证', '版本管理']
                        ]
                    },
                    'Istio': {
                        'desc': '服务网格，微服务流量管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与代理', 'Control Plane/Data Plane', 'Envoy代理/sidecar注入'],
                            ['流量管理', 'VirtualService路由', 'DestinationRule负载均衡', 'Gateway/Ingress', '流量镜像/故障注入'],
                            ['安全与认证', 'mTLS双向认证', 'Security Policy', 'ServiceEntry外部服务'],
                            ['可观测性', 'Kiali服务可视化', 'Jaeger链路追踪', 'Telemetry V2'],
                            ['最佳实践', '超时重试/熔断/限流', 'Istio配置最佳实践']
                        ]
                    },
                    'Knative': {
                        'desc': 'K8s无服务器框架',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与Serving', 'Knative架构(Eventing/Serving)', '服务部署', 'Revision版本路由'],
                            ['自动伸缩', 'Serverless自动伸缩(KPA)', '冷启动优化/预热', '流量分割/金丝雀发布'],
                            ['Eventing事件', 'CloudEvents事件规范', 'Trigger/Broker订阅', 'Kafka事件源'],
                            ['API与集成', 'Knative API/kubectl', '健康检查/探测', '云厂商集成']
                        ]
                    },
                    'Kubernetes': {
                        'desc': '深度掌握K8s架构和原理',
                        'difficulty': 2,
                        'dimensions': [
                            ['控制平面', 'API Server认证授权', 'etcd存储/一致性', 'Scheduler调度算法', 'Controller Manager/控制器'],
                            ['工作负载与配置', 'Pod生命周期/Init容器', 'ConfigMap/Secret', '调度亲和性/污点容忍', 'ResourceQuota/LimitRange'],
                            ['网络与存储', 'Service/Ingress', 'NetworkPolicy', 'Volume/PV/PVC', 'StorageClass'],
                            ['安全与扩展', 'SecurityContext/PSP/PodSecurity', 'RBAC权限', 'CRD自定义资源', 'Operator模式']
                        ]
                    },
                    'Prometheus': {
                        'desc': '云原生监控方案',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与指标', 'TSDB存储', '指标类型(Counter/Gauge/Histogram)', 'PromQL查询语言'],
                            ['采集与发现', 'Exporter暴露', '服务发现(SD)', 'Prometheus Operator'],
                            ['告警与管理', 'Alertmanager告警', 'Recording Rules预计算', 'Prometheus联邦'],
                            ['集成与优化', 'Grafana集成', 'Remote Write远程存储', 'BlackboxExporter探针', '性能调优']
                        ]
                    },
                    'etcd': {
                        'desc': '分布式键值存储',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与Raft', 'etcd架构', 'Raft共识协议', 'Leader选举'],
                            ['数据与API', '键值对模型', 'gRPC API', 'MVCC多版本', 'Watch事件监听', 'Lease租约/TTL'],
                            ['集群与运维', '集群部署与发现', '一致性问题/脑裂', '备份(snapshot)与恢复', '性能优化'],
                            ['安全与监控', 'TLS/mTLS', 'metrics监控', 'etcd最佳实践']
                        ]
                    },
                    'Operator': {
                        'desc': 'K8s Operator开发和运维',
                        'difficulty': 3,
                        'dimensions': [
                            ['模式与框架', 'Operator模式', 'Kubebuilder框架', 'Operator SDK(Golang)', 'CRD定义'],
                            ['控制器机制', 'Reconciliation Loop', 'Status/Subresource', 'Finalizer清理', 'Owner References'],
                            ['高级开发', 'Webhooks(验证/变更)', 'Leader Election', 'Operator测试(suite)'],
                            ['实践与示例', 'Prometheus Operator', 'etcd Operator', '生命周期管理', '最佳实践']
                        ]
                    }
                }
            }
        }
    }
}