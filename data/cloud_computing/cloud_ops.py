"""云运维工程师数据"""
data = {
    '计算机与信息技术': {
        '云计算': {
            '云运维工程师': {
                'description': '负责云平台运维，保证云服务的高可用性和性能。',
                'skills': {
                    'Docker': {
                        'desc': '容器运维和镜像管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['容器生命周期与基础', '守护进程管理', '镜像pull/push/tag/build', '容器操作(start/stop/exec/logs)', '资源限制(CPU/内存配额)', '健康检查(HEALTHCHECK)'],
                            ['镜像与仓库', 'Dockerfile与多阶段构建', '镜像优化与安全扫描', '私有仓库(Harbor/Distribution)', '镜像版本与标签管理'],
                            ['网络与存储', '网络驱动(bridge/host/overlay)', '数据卷/挂载/持久化', '存储驱动与性能', '日志驱动(json-file/syslog)'],
                            ['编排与集群', 'Docker Compose多容器编排', 'Swarm集群管理', '服务部署与滚动更新', '配置与密钥管理'],
                            ['监控与优化', '容器监控(cAdvisor/Stats)', '日志收集与分析', '安全加固(rootless/Seccomp)', 'Dockerfile最佳实践']
                        ]
                    },
                    'Kubernetes': {
                        'desc': 'K8s集群运维和故障排查',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心操作与调度', 'kubectl命令与上下文', 'Pod调度(亲和/反亲和)', '滚动更新与回滚(Deployment策略)', '资源配额(Request/Limit/Quota)', 'HPA自动伸缩(Metrics Server)'],
                            ['健康与存储', 'liveness/readiness探针', '存储管理(PV/PVC/StorageClass)', 'ConfigMap/Secret配置', '卷快照与备份'],
                            ['网络与安全', 'NetworkPolicy网络策略', '命名空间隔离', 'RBAC权限与角色绑定', 'ServiceAccount与Pod安全'],
                            ['运维与排错', '集群架构(控制平面/工作节点)', '日志收集(Fluentd/EFK/Loki)', '故障排查(Pod状态/Events)', '集群升级与版本兼容', 'etcd备份与恢复'],
                            ['部署与工具', 'kubeadm/kubespray部署', 'Helm包管理', 'Kustomize配置', '监控集成(Prometheus/Grafana)']
                        ]
                    },
                    'Linux': {
                        'desc': 'Linux服务器管理和运维',
                        'difficulty': 2,
                        'dimensions': [
                            ['系统管理与服务', '发行版(CentOS/Ubuntu)', 'systemd服务管理', '用户与权限管理', 'SSH密钥与跳板机', '定时任务(cron/anacron)'],
                            ['磁盘与网络', '磁盘管理(fdisk/df/lvm)', '网络配置(ifcfg/ip/route)', '防火墙(iptables/firewalld)', 'SELinux/AppArmor安全'],
                            ['性能与监控', '进程管理(ps/top/htop)', '日志管理(journalctl/rsyslog)', '性能监控(free/iostat/netstat)', '故障排查(dmesg/strace/lsof)'],
                            ['优化与加固', '系统优化(sysctl/ulimit)', '内核参数调优', '安全加固(端口/服务)', '自动化脚本运维']
                        ]
                    },
                    '云计算平台': {
                        'desc': '主流云平台日常运维管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['计算与实例', 'ECS/EC2/VM实例管理', '弹性伸缩与镜像', '远程连接与诊断', '实例规格与性能选择'],
                            ['存储与数据库', 'RDS/云数据库运维(备份/参数调优)', 'OSS/S3对象存储管理', '文件存储/块存储', '缓存数据库(Redis)'],
                            ['网络与安全', 'VPC/安全组配置', '负载均衡与入口', '堡垒机/访问控制', '跨区域网络与专线'],
                            ['监控与告警', '云监控/告警规则设置', '日志服务与分析', '性能监控与阈值', '健康检查与事件'],
                            ['管理与成本', 'CLI/SDK运维', '多账户/多项目管理', '成本控制与预算', '资源标签与审计']
                        ]
                    },
                    '备份恢复': {
                        'desc': '云数据备份和灾难恢复',
                        'difficulty': 2,
                        'dimensions': [
                            ['备份策略与类型', '全量/增量/差异备份', '快照/自动快照策略', '数据库备份(mysqldump/xtrabackup)', 'Redis RDB/AOF备份'],
                            ['存储与加密', '备份加密与压缩', '异地/跨区域复制', '云存储备份(S3 Glacier)', '备份生命周期管理'],
                            ['恢复与演练', '恢复演练与定期测试', 'RTO/RPO目标设定', '灾难恢复计划(DRP)', '备份脚本与自动化'],
                            ['监控与迁移', '备份监控与告警', '备份成功/失败通知', '云迁移工具/迁云服务', 'VMware/物理机迁移']
                        ]
                    },
                    '安全管理': {
                        'desc': '云安全组、访问控制、密钥管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['身份与访问控制', 'IAM用户/角色/策略', '多因素认证(MFA)', '最小权限原则', '权限审计与隔离'],
                            ['网络安全', '安全组(入/出方向)', '网络ACL/子网防护', 'WAF Web应用防火墙', 'DDoS防护/流量清洗'],
                            ['密钥与凭证', '密钥管理(KMS/对称/非对称)', 'Secret管理/轮换', '凭证存储与审计', '证书管理'],
                            ['审计与合规', 'CloudTrail/操作审计', '安全审计/漏洞扫描', '合规检查(等保/ISO27001)', '安全事件响应']
                        ]
                    },
                    '故障排查': {
                        'desc': '云服务故障诊断和恢复',
                        'difficulty': 2,
                        'dimensions': [
                            ['故障分级与流程', 'P0-P3故障分级', '应急响应流程', '值班机制与事件上报', '故障复盘与报告'],
                            ['网络故障排查', 'ping/telnet/traceroute诊断', 'DNS解析异常', '端口/防火墙/Security Group', '负载均衡与网络延迟'],
                            ['主机与应用故障', 'SSH/远程连接问题', 'CPU/内存/进程异常', '磁盘满/IO性能瓶颈', '服务宕机与自动恢复'],
                            ['证书与配置', 'SSL/TLS证书过期', '配置错误排查', '根因分析与时间线', '监控告警与异常检测']
                        ]
                    },
                    '日志管理': {
                        'desc': 'ELK、Loki等日志收集和分析',
                        'difficulty': 2,
                        'dimensions': [
                            ['ELK Stack', 'Elasticsearch索引/映射/分片', 'Logstash输入/过滤/输出', 'Kibana仪表盘/可视化', 'Filebeat轻量采集'],
                            ['Loki与Grafana', 'Loki日志收集/Promtail', 'Grafana Loki展示/查询', 'LogQL查询语言', '日志告警规则'],
                            ['日志采集与格式', '容器日志/应用日志', '结构化日志(JSON)', '日志采集Agent(Fluentd)', '日志存储/生命周期/压缩'],
                            ['查询与合规', '日志查询(KQL/DSL)', '分布式日志追踪', '日志合规/保留策略', '日志告警与通知']
                        ]
                    },
                    '监控': {
                        'desc': 'Prometheus、Grafana云资源监控和性能调优',
                        'difficulty': 2,
                        'dimensions': [
                            ['Prometheus体系', '架构与TSDB', 'Exporter(Node/cAdvisor)', 'PromQL查询(rate/irate/聚合)', '服务发现与配置', 'Alertmanager告警规则'],
                            ['Grafana可视化', '仪表盘与Panel', '告警规则与通知渠道', 'SLO/SLA监控', '自定义DashBoard'],
                            ['云原生与平台监控', 'Kubernetes监控(kube-state-metrics)', '云平台监控(CloudWatch/Azure Monitor)', '应用APM与业务指标', '网络监控/数据库监控'],
                            ['告警与优化', '告警收敛/去重/抑制', 'PagerDuty/钉钉/飞书', '性能分析(火焰图/pprof)', '告警可靠性优化']
                        ]
                    },
                    '自动化运维': {
                        'desc': 'Ansible、Puppet等自动化运维工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['Ansible运维', 'Inventory/YAML', '模块(command/shell/script)', 'Playbook任务与处理器', 'Role角色复用', 'AWX/Tower Web界面'],
                            ['Puppet与SaltStack', 'Puppet Manifest/资源/类', 'Puppet模块/环境管理', 'SaltStack Master/Minion', '批量执行与状态管理'],
                            ['自动化实践', '配置管理/文件一致性', '自动部署/应用发布', '堡垒机/审批流程/审计', 'CI/CD集成(Jenkins/GitLab)', '配置审计与合规']
                        ]
                    }
                }
            }
        }
    }
}