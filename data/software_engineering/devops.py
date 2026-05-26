"""DevOps工程师数据"""
data = {
    '计算机与信息技术': {
        '软件工程': {
            'DevOps工程师': {
                'description': '负责持续集成/持续部署，自动化运维和基础设施管理。',
                'skills': {
                    'Python': {
                        'desc': '运维自动化和工具开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础与数据类型', '变量', '数字/字符串', 'list/dict/set/tuple', '流程控制', '函数与lambda'],
                            ['面向对象与异常', '类与继承', '多态', 'try/except/finally', 'raise', '自定义异常'],
                            ['模块与包管理', 'import', 'pip/venv/conda', 'requirements.txt', 'poetry/pipenv'],
                            ['文件与数据处理', '文件读写', 'os.path/pathlib', 'CSV/JSON/XML', 'datetime', '正则表达式'],
                            ['并发与系统交互', 'threading/multiprocessing', 'asyncio', 'subprocess', 'paramiko', 'fabric'],
                            ['网络与数据库', 'requests', 'pymysql/psycopg2', 'sqlalchemy', 'Redis/MongoDB', 'Docker SDK'],
                            ['工程化与测试', 'logging', 'configparser/PyYAML', 'unittest/pytest', '类型注解', 'PEP8/black'],
                            ['运维自动化', 'crontab/APScheduler', 'supervisor/systemd', '钉钉/飞书通知', 'CLI工具(argparse/click)']
                        ]
                    },
                    'Ansible': {
                        'desc': '自动化运维工具，批量配置服务器',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与基础', '控制节点/受控节点', 'SSH无密钥', 'inventory清单', '静态/动态清单', '主机分组'],
                            ['ad-hoc与模块', 'ping/command/shell', 'yum/apt', 'service/file/copy', 'template/lineinfile', 'user/group'],
                            ['playbook基础', 'YAML语法', 'hosts/remote_user', 'tasks/handlers', 'vars/register', 'tags'],
                            ['流程与循环', 'when条件', 'loop/with_items', 'until重试', 'ignore_errors', 'check_mode/diff'],
                            ['角色与复用', 'roles目录结构', 'ansible-galaxy', 'include/import', 'ansible-vault加密'],
                            ['高级与集成', 'delegate_to/run_once', 'async异步', '动态清单(AWS/GCP)', 'AWX/Tower', 'Molecule测试']
                        ]
                    },
                    'Docker': {
                        'desc': '容器化技术，实现应用快速部署和环境一致性',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与镜像', 'Docker安装', 'pull/push/tag', 'Dockerfile指令(FROM/COPY/CMD)', '多阶段构建', '镜像优化(alpine/slim)'],
                            ['容器管理', 'run/exec/logs/cp', '端口映射', '环境变量', '数据卷与挂载', '资源限制'],
                            ['网络与编排', 'bridge/host/overlay', 'DNS服务发现', 'Docker Compose', 'Swarm集群', '服务与滚动更新'],
                            ['仓库与安全', 'Harbor私有仓库', '镜像扫描(Trivy)', 'RBAC', '非root运行', '安全实践(seccomp/apparmor)'],
                            ['监控与最佳实践', 'cAdvisor/Prometheus', '日志驱动', '健康检查', 'buildx多架构', 'GC清理']
                        ]
                    },
                    'ELK Stack': {
                        'desc': 'Elasticsearch、Logstash、Kibana日志分析平台',
                        'difficulty': 2,
                        'dimensions': [
                            ['Elasticsearch核心', '集群/节点角色', '索引与映射', 'CRUD与bulk', '分片与副本', '集群健康'],
                            ['查询与聚合', 'Query DSL(match/bool)', 'term/range查询', '聚合(metric/bucket)', 'pipeline聚合', '高亮与分页'],
                            ['分词与ILM', '分词器(standard/ngram)', '同义词/停用词', 'ILM生命周期(hot/warm/cold)', '快照与CCR'],
                            ['安全与告警', 'X-Pack Security', '角色与字段级权限', 'Watcher告警', 'Email/Slack/钉钉通知'],
                            ['Logstash管道', 'input/beats/file', 'filter/grok/mutate', 'output/elasticsearch', 'DLQ死信队列'],
                            ['Kibana与Beats', 'Dashboard/Discover', 'Index Pattern', '告警规则与操作', 'Filebeat/Metricbeat集成', 'APM/Machine Learning']
                        ]
                    },
                    'GitHub Actions': {
                        'desc': 'GitHub的自动化工作流平台',
                        'difficulty': 2,
                        'dimensions': [
                            ['工作流定义', 'workflow文件', '触发器(push/PR/schedule)', 'branches/tags过滤', 'cron表达式', 'workflow_dispatch'],
                            ['Runner与作业', 'ubuntu/windows/macOS', '自托管Runner', 'job/needs/runs-on', 'matrix矩阵构建'],
                            ['步骤与操作', 'steps/run', 'uses引用(actions/checkout)', 'with/env', 'if条件', 'timeout/continue-on-error'],
                            ['密钥与变量', 'secrets加密', 'variables', '环境变量', 'GITHUB_TOKEN权限', 'OIDC认证(AWS)'],
                            ['缓存与产物', 'actions/cache', 'upload/download artifact', '并发控制(concurrency)', 'reusable workflow'],
                            ['CI/CD实践', '代码检查/lint', '测试/覆盖率', 'Docker构建推送', 'release发布', '通知(钉钉/Slack)']
                        ]
                    },
                    'GitLab CI': {
                        'desc': 'GitLab内置的持续集成工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['Pipeline与Stage', '.gitlab-ci.yml', 'stages定义', 'job配置', 'script/before_script', 'timeout/retry'],
                            ['控制与条件', 'rules/only/except', 'when(manual/delayed)', 'trigger触发', 'include包含', 'extends继承'],
                            ['Runner与标签', 'Runner安装注册', 'tags匹配', 'executor(shell/docker/k8s)', '并发与锁定'],
                            ['缓存与工件', 'cache缓存键', 'artifacts工件', 'reports(junit/cobertura)', 'dependencies/needs依赖'],
                            ['安全与最佳实践', 'secrets变量', 'SAST/Secret Detection', '多阶段构建', 'pipeline模块化']
                        ]
                    },
                    'Grafana': {
                        'desc': '数据可视化和监控仪表板',
                        'difficulty': 2,
                        'dimensions': [
                            ['安装与数据源', 'Grafana安装', 'DataSource(Prometheus/Loki/ES)', 'Explore探索', 'Query Editor'],
                            ['Dashboard与面板', '创建/导入Dashboard', 'Graph/Stat/Gauge/Table', 'TimeSeries/Logs', '变量Variables', 'Thresholds'],
                            ['告警引擎', 'Alert Rules', '条件(Reduce/Math/Threshold)', 'Contact Points(Slack/Email)', 'Notification Policies', '告警模板'],
                            ['管理与集成', '用户/组织/权限', 'OAuth/LDAP认证', 'Provisioning配置供给', 'API管理', 'Grafana Cloud']
                        ]
                    },
                    'Helm': {
                        'desc': 'Kubernetes包管理工具，简化应用部署',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与Chart', 'Helm CLI', 'Chart结构(templates/values)', '仓库(repo add/search)', 'install/upgrade/rollback'],
                            ['模板开发', 'Go template语法', 'values引用与管道', '流程控制(if/range)', '命名模板', 'set/--set-file'],
                            ['高级与钩子', 'Hooks(pre/post install)', '依赖管理', 'RBAC/ServiceAccount', 'CI/CD集成(ArgoCD)'],
                            ['安全与最佳实践', 'helm-secrets', 'Chart测试', 'lint检查', '私有仓库(Harbor)', 'CRD/Operator集成']
                        ]
                    },
                    'Jenkins': {
                        'desc': '开源CI/CD工具，自动化构建、测试和部署',
                        'difficulty': 2,
                        'dimensions': [
                            ['安装与基础', 'Jenkins安装(Docker/WAR)', '插件管理', 'Job类型(自由风格/管道)', '源码管理(Git)', '触发器(cron/webhook)'],
                            ['Pipeline核心', '声明式管道', 'Jenkinsfile', 'stage/step', 'agent', 'options/parameters'],
                            ['Pipeline进阶', 'parallel/ matrix', 'when条件', 'credentials', '环境变量', '共享库(Shared Library)'],
                            ['集成与工具', 'Maven/Gradle/npm', 'SonarQube代码扫描', 'JUnit/Pytest报告', 'Nexus/Artifactory', 'Docker/K8s集成'],
                            ['运维与最佳实践', 'RBAC权限', 'LDAP认证', '备份恢复', '日志分析', 'Pipeline as Code']
                        ]
                    },
                    'Kubernetes': {
                        'desc': '容器编排平台，管理大规模容器集群的部署和扩展',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心概念', 'Master/Node/etcd', 'Pod/Service/Ingress', 'Deployment/StatefulSet/DaemonSet', 'Job/CronJob', 'Namespace'],
                            ['工作负载管理', '探针(liveness/readiness)', '资源限制', '滚动更新/回滚', 'HPA弹性伸缩', 'ConfigMap/Secret'],
                            ['网络与存储', 'CNI/NetworkPolicy', 'Ingress/TLS', 'PV/PVC/StorageClass', 'Service类型(ClusterIP/NodePort/LB)'],
                            ['调度与安全', '污点/容忍', '亲和性/反亲和性', 'RBAC/ServiceAccount', 'PodSecurityPolicy', 'QoS等级'],
                            ['运维与生态', 'kubectl常用命令', 'Helm/Operator', '监控(Prometheus/Grafana)', '日志(Fluentd/Loki)', 'GitOps(ArgoCD)']
                        ]
                    },
                    'Nginx': {
                        'desc': 'Web服务器和反向代理配置',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础配置', 'nginx.conf结构', 'worker_processes', 'server/listen', 'location匹配', 'root/try_files'],
                            ['反向代理与负载均衡', 'proxy_pass', 'upstream', '轮询/权重/ip_hash', '健康检查', 'X-Real-IP'],
                            ['SSL与安全', 'HTTPS/HTTP/2', 'SSL证书配置', 'HSTS/CSP', 'IP黑白名单', '防盗链'],
                            ['缓存与压缩', 'proxy_cache', 'gzip压缩', '静态资源缓存', 'logrotate日志切割', 'access/error日志'],
                            ['高级与优化', 'rewrite/301重定向', 'WebSocket代理', 'stream四层代理', 'openresty/Lua', '限流(limit_req/conn)']
                        ]
                    },
                    'Prometheus': {
                        'desc': '监控系统和时间序列数据库',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与数据模型', 'Prometheus Server', 'Exporters', 'Alertmanager', 'Metrics(名称/标签)', 'Counter/Gauge/Histogram'],
                            ['PromQL查询', 'rate/irate', 'increase', 'sum/avg/count', 'by/without', 'histogram_quantile', 'offset/@'],
                            ['告警规则', 'groups/alert', 'expr/for', 'labels/annotations', 'Recording Rules', '告警模板'],
                            ['Alertmanager', '路由与分组', 'receivers(Slack/Email)', '静默/抑制', '高可用集群'],
                            ['采集与集成', 'Exporter(Node/Redis/Kafka)', '服务发现(kubernetes/consul)', 'Prometheus Operator', 'Grafana展示']
                        ]
                    },
                    'Terraform': {
                        'desc': '基础设施即代码工具，自动化云资源管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与语法', 'HCL语言', 'resource/data', 'variable/output', 'provider配置', 'init/plan/apply'],
                            ['状态与模块', 'State管理', '远程后端(S3/GCS)', '工作空间', '模块创建与引用', 'Module Registry'],
                            ['高级特性', 'count/for_each循环', 'dynamic块', '条件表达式', 'depends_on', 'lifecycle规则'],
                            ['CI/CD与安全', 'Terraform Cloud/Enterprise', 'Atlantis自动化', 'OPA/Sentinel策略', 'tfsec扫描', 'Vault集成'],
                            ['最佳实践', '代码结构', '变量验证', '状态锁定', 'GCP/AWS/Azure云Provider', '多云管理']
                        ]
                    },
                    'Linux': {
                        'desc': '服务器操作系统管理和命令行操作',
                        'difficulty': 3,
                        'dimensions': [
                            ['文件与目录', 'ls/cd/mkdir/rm/cp/mv', 'find/locate', 'ln软硬链接', 'xargs', 'tar压缩归档'],
                            ['文本与权限', 'cat/head/tail', 'grep/sed/awk', 'sort/uniq/wc', 'chmod/chown', 'useradd/sudo'],
                            ['进程与系统', 'ps/top/htop', 'kill/pkill/nohup', 'systemctl/service', 'crontab定时任务', 'journalctl日志'],
                            ['网络与磁盘', 'ip/ifconfig/ping', 'ss/netstat/curl', 'df/du/fdisk', 'mount/umount', 'rsync/scp'],
                            ['Shell与脚本', '环境变量', 'bash/zsh配置', '管道与重定向', 'set -e/-x调试', 'vim编辑器'],
                            ['运维工具', 'tmux/screen', 'SSH密钥登录', '防火墙firewalld/iptables', 'sysctl内核参数', 'strace/perf分析']
                        ]
                    },
                    'Shell脚本': {
                        'desc': '自动化运维脚本编写',
                        'difficulty': 3,
                        'dimensions': [
                            ['基础语法', '#!/bin/bash', '变量定义与替换', '数组与关联数组', '算术运算', '字符串操作'],
                            ['流程控制', 'if/case语句', 'for/while/until循环', 'break/continue', '函数定义与参数', 'return/exit'],
                            ['输入输出', 'read读取', '参数($@/$#)', 'getopts解析', 'here document', '管道与tee'],
                            ['高级编程', 'trap信号', 'sed/awk高级', '正则表达式', '临时文件(mktemp)', 'parallel并发'],
                            ['调试与安全', 'set -x/-e', 'shellcheck', '输入验证', '日志记录', 'crontab/定时脚本'],
                            ['实践场景', '备份脚本', '日志分析', '服务健康检查', '批量部署', 'CI/CD集成']
                        ]
                    },
                    '云原生': {
                        'desc': '理解云原生架构和12要素应用',
                        'difficulty': 3,
                        'dimensions': [
                            ['概念与12要素', '云原生定义', '容器/微服务/声明式', '12-Factor App', 'Codebase/依赖/配置', '进程/端口/日志'],
                            ['微服务与网格', '服务拆分', '松耦合/高内聚', 'Service Mesh(Istio)', 'Sidecar模式', 'API网关(Kong/APISIX)'],
                            ['持续交付与GitOps', '不可变基础设施', 'GitOps工作流', 'ArgoCD/Flux', '蓝绿/金丝雀部署', 'Tekton'],
                            ['可观测性', 'OpenTelemetry', 'Prometheus/Loki', '分布式追踪', '健康检查/自愈', '混沌工程'],
                            ['安全与存储', 'mTLS/零信任', 'OPA/Sentinel', '容器安全(distroless)', 'CSI存储', 'RBAC/密钥管理']
                        ]
                    },
                    '网络基础': {
                        'desc': 'TCP/IP、DNS、HTTP等网络协议',
                        'difficulty': 3,
                        'dimensions': [
                            ['协议模型', 'OSI七层', 'TCP/IP四层', '数据封装', '网络设备(交换机/路由器)'],
                            ['TCP/UDP', '三次握手', '四次挥手', '流量控制', '拥塞控制', 'UDP与QUIC'],
                            ['IP与路由', 'IP地址/A类B类', '子网划分/CIDR', '路由表', 'ARP协议', 'ICMP/ping'],
                            ['DNS与应用', '解析过程', 'A/CNAME/MX', 'DNS缓存/TTL', 'HTTP状态码', 'HTTPS/TLS握手'],
                            ['负载与安全', 'L4/L7负载均衡', 'CDN原理', '防火墙/NAT', '常见攻击(XSS/CSRF)', '网络诊断(tcpdump/wireshark)']
                        ]
                    }
                }
            }
        }
    }
}