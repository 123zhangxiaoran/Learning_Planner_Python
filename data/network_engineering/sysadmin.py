"""系统管理员数据"""
data = {
    '计算机与信息技术': {
        '网络工程': {
            '系统管理员': {
                'description': '负责服务器和系统的日常运维管理工作。',
                'skills': {
                    'Python': {
                        'desc': '运维自动化脚本和工具开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['语言核心', '数据类型(list/dict/set)', '控制流与函数', '面向对象(类/继承)', '异常处理(try-except)', 're正则表达式', 'JSON/YAML解析'],
                            ['系统交互', 'os/pathlib文件目录', 'subprocess执行命令', 'paramiko/SSH/SFTP', 'logging日志', '配置文件读取(ConfigParser)'],
                            ['自动化与工具', '脚本编写与执行', 'argparse/CLI工具', '定时任务(schedule/APScheduler)', 'Celery分布式任务', 'requests API调用', 'pymysql/redis-py数据库'],
                            ['工程化', 'venv/virtualenv环境', 'requirements.txt依赖', 'Git版本控制', 'PEP8规范', 'unittest/pytest测试']
                        ]
                    },
                    'Windows Server': {
                        'desc': 'Windows服务器管理和AD域配置',
                        'difficulty': 1,
                        'dimensions': [
                            ['系统基础', 'Server 2016/2019/2022', 'Core与GUI安装', '远程桌面RDP', '服务器管理器', '角色和功能'],
                            ['AD域服务', '域控制器DC', 'AD DS/域账号', '组织单位OU', '组策略GPO', '安全策略与审核'],
                            ['文件与存储', 'NTFS权限/ACL', '共享权限', '文件服务器', 'DFS命名空间', 'iSCSI目标/发起程序'],
                            ['网络服务', 'DHCP作用域与中继', 'DNS区域/转发器', 'IIS网站/应用程序池', 'HTTPS绑定', 'NLB负载均衡'],
                            ['虚拟化与管理', 'Hyper-V管理器', '虚拟机创建/检查点', '故障转移集群', 'PowerShell管理', '任务计划/事件查看器']
                        ]
                    },
                    'Ansible': {
                        'desc': '自动化运维工具，批量配置管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础架构', 'Agentless架构', 'Inventory清单(静态/动态)', 'ansible.cfg配置', 'ad-hoc命令', '主机模式与变量'],
                            ['常用模块', 'command/shell/script', 'file/copy/template', 'yum/apt包管理', 'service/systemd', 'user/group/cron'],
                            ['Playbook核心', 'YAML剧本结构', 'tasks/handlers/tags', 'vars/register', 'when条件', 'loop/with_items循环'],
                            ['高级特性', 'roles角色与目录结构', 'ansible-galaxy', 'ansible-vault加密', 'delegate_to委托', 'async异步', 'check/diff模式'],
                            ['扩展与集成', 'lookup/filter插件', '动态清单脚本', '云模块(ec2/vmware)', 'docker/k8s模块', '回调插件与facts缓存']
                        ]
                    },
                    'Linux': {
                        'desc': 'Linux服务器安装配置和日常维护，包括CentOS、Ubuntu等',
                        'difficulty': 2,
                        'dimensions': [
                            ['系统管理', '发行版(CentOS/Ubuntu)', '安装与引导', 'LVM逻辑卷', 'fdisk/parted分区', '文件系统(ext4/xfs)', '挂载与fstab'],
                            ['网络与包管理', 'IP/子网/网关/DNS', 'nmcli/nmtui配置', 'yum/dnf/apt包管理', 'EPEL/软件源', 'systemd服务管理'],
                            ['用户与权限', 'useradd/usermod/sudo', 'chmod/chown/ACL', 'Selinux/AppArmor', 'sshd_config安全', '密钥登录'],
                            ['性能与监控', 'ps/top/htop进程', 'free/vmstat/sar', 'iostat/df/du磁盘', 'ss/netstat网络', 'cron定时任务', 'journalctl/syslog日志'],
                            ['运维自动化', 'Shell脚本编写', 'vim编辑器', 'rsync/tar备份', 'firewalld/iptables防火墙', '环境变量与重定向']
                        ]
                    },
                    'Shell': {
                        'desc': 'Linux自动化运维脚本编写',
                        'difficulty': 2,
                        'dimensions': [
                            ['脚本基础', 'shebang/注释', '变量与环境变量', '位置参数($1/$@)', '特殊变量($?/$$)', '命令替换($()/``)'],
                            ['控制结构', 'if/test/[[ ]]', 'case模式匹配', 'for/while/until循环', 'select菜单', '函数与return/local'],
                            ['文本处理', 'grep/正则', 'sed替换/删除', 'awk字段/条件', 'cut/tr/sort/uniq', 'xargs参数构建'],
                            ['高级特性', '重定向与管道', 'here文档/字符串处理', '数组与关联数组', 'trap信号捕获', 'set -x/-e调试'],
                            ['自动化实践', 'read交互输入', 'crontab定时任务', 'curl/wget网络请求', 'expect自动化', '脚本模板与shellcheck']
                        ]
                    },
                    '备份恢复': {
                        'desc': '数据备份策略制定和灾难恢复',
                        'difficulty': 2,
                        'dimensions': [
                            ['备份策略', '3-2-1原则', '全量/增量/差异备份', 'RPO与RTO', '备份窗口与频率', '3-2-1-1防勒索'],
                            ['工具与操作', 'tar/rsync/dd', 'mysqldump/XtraBackup', 'pg_dump/mongodump', 'Restic/Rclone', 'Veeam/Bacula'],
                            ['备份存储', '磁盘/磁带/云存储', 'NAS/SAN目标', 'OSS/S3/Azure', '备份加密与压缩', '备份验证与恢复测试'],
                            ['灾难恢复', 'DR站点/冷温热备', '主备切换/回切', '同步/异步复制', 'CDP持续保护', '快照(存储/LVM/VMware)'],
                            ['生命周期', '备份归档与长期保留', '合规保留策略', '过期清理', '裸机恢复', 'K8s备份(velero)']
                        ]
                    },
                    '网络配置': {
                        'desc': '服务器网络参数配置和故障排查',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础配置', 'IP/掩码/网关/DNS', '静态IP(ifcfg/netplan)', 'NetworkManager/nmcli', 'DHCP动态获取', '多网卡Bonding/Teaming'],
                            ['高级网络', 'VLAN子接口', '网桥Bridge', 'IP别名/隧道(GRE/VXLAN)', 'MTU巨型帧', 'Loopback接口'],
                            ['诊断工具', 'ping/traceroute/mtr', 'nslookup/dig', 'netstat/ss/ip addr', 'arp/ethtool', 'iperf3带宽测试'],
                            ['排障与抓包', 'tcpdump/wireshark', 'nc/netcat', 'curl/telnet', 'DNS/网关/路由故障', '防火墙/Selinux影响'],
                            ['监控', '网络服务管理', 'iftop/nethogs流量', '带宽/延迟/丢包', 'MTU/NAT问题', '端口冲突排查']
                        ]
                    },
                    'ELK': {
                        'desc': 'Elasticsearch、Logstash、Kibana日志分析',
                        'difficulty': 3,
                        'dimensions': [
                            ['Elasticsearch核心', '集群/节点/分片/副本', '索引/文档/映射', 'REST API与查询DSL', '倒排索引/IK分词器', 'ILM索引生命周期'],
                            ['Logstash管道', 'Input(beats/file/tcp)', 'Filter(grok/mutate/date)', 'Output(ES/file/kafka)', '多管道配置', '死信队列'],
                            ['Beats采集', 'Filebeat模块', 'Metricbeat系统指标', 'Packetbeat/Heartbeat', 'Auditbeat/Winlogbeat', 'Journalbeat'],
                            ['Kibana可视化', 'Discover/Dev Tools', 'Visualize/Dashboard', 'Lens/TSVB/Canvas', 'Alerting告警', 'Machine Learning'],
                            ['运维与安全', '集群监控(Stack Monitoring)', 'X-Pack安全/RBAC', 'TLS/HTTPS', '快照与CCR', 'JVM调优']
                        ]
                    },
                    'ITIL': {
                        'desc': 'IT服务管理流程和最佳实践',
                        'difficulty': 3,
                        'dimensions': [
                            ['框架与原则', 'ITIL 4 SVS', '指导原则', '服务价值链', '四维度模型', '实践(Practice)'],
                            ['服务运营', '服务台(本地/集中/虚拟)', '事件管理(P1-P4/升级)', '问题管理(RCA/已知错误)', '变更管理(CAB/RFC)', '发布管理(策略/部署)'],
                            ['服务设计', 'SLA/OLA', '容量管理', '可用性管理', '连续性管理', '供应商管理'],
                            ['关键实践', '配置管理(CMDB/CI)', '资产与财务管理', '知识管理(KB)', '服务请求管理', '服务目录'],
                            ['工具与认证', 'ServiceNow/Jira SM', 'ITIL Foundation', '流程审计/优化', 'KPI/SLA报告', 'SOAR/自动化']
                        ]
                    },
                    'KVM': {
                        'desc': '开源虚拟化技术',
                        'difficulty': 3,
                        'dimensions': [
                            ['虚拟化架构', 'KVM模块/qemu-kvm', 'libvirt管理', 'virsh命令行', 'virt-manager图形', 'VT-x/AMD-V硬件辅助'],
                            ['虚拟机管理', '创建(virt-install)', '克隆/模板', 'qcow2磁盘/快照', 'raw格式', 'VNC/SPICE控制台'],
                            ['网络与存储', '桥接/NAT/Host-only', 'SR-IOV/PCI直通', 'libvirt网络XML', '存储池(dir/lvm/iscsi/rbd)', 'virtio驱动'],
                            ['高级特性', '热迁移(Live Migration)', 'NUMA/CPU绑定', '大页内存', 'cloud-init初始化', '安全(SELinux/AppArmor)'],
                            ['监控与排错', 'virsh dominfo/stats', '日志分析', '资源配额(CPU/内存/IO)', '嵌套虚拟化', '性能优化']
                        ]
                    },
                    'Nagios': {
                        'desc': '系统和网络监控工具',
                        'difficulty': 3,
                        'dimensions': [
                            ['架构与安装', 'Nagios Core/XI', 'nagios.cfg主配置', '对象定义(host/service/contact)', '主机组/服务组', 'NRPE远程执行', 'NSClient++(Windows)'],
                            ['检查与插件', 'check_ping/disk/load', 'check_http/ssh/mysql', '自定义插件(Shell/Python)', '插件返回码(0-3)', '性能数据(PNP4Nagios)'],
                            ['告警与通知', 'Notification配置', '升级(Escalation)', 'Email/SMS/Webhook', '状态类型(Hard/Soft)', '通知周期与依赖'],
                            ['高级配置', '模板/继承', '宏($HOSTNAME$等)', '分布式监控(DNX/Fusion)', '事件处理', '维护期(Maintenance)'],
                            ['生态与工具', 'NagiosGraph/Thruk', 'Centreon/Icinga', 'NRDP/NSCA', 'Web界面/GUI配置', '可用性报告']
                        ]
                    },
                    'VMware': {
                        'desc': '虚拟化平台管理和虚拟机部署',
                        'difficulty': 3,
                        'dimensions': [
                            ['平台基础', 'ESXi安装/DCUI', 'vCenter Server(VCSA)', 'vSphere Client', '集群与DRS/HA', 'EVC与vMotion'],
                            ['计算与存储', 'FT容错', '虚拟机创建/模板', 'Thin/Thick磁盘', '快照管理', 'vSAN分布式存储', 'RDM/iSCSI/NFS存储'],
                            ['网络', '标准交换机(vSS)', '分布式交换机(VDS)', '端口组/VLAN', 'NIC Teaming/LACP', 'vMotion网络'],
                            ['生命周期', 'vSphere Lifecycle Manager', '基线/扫描/修复', 'ESXi/vCenter升级', 'VMware Tools', '内容库(OVA/OVF)'],
                            ['运维与安全', '角色权限(RBAC)', 'ESXi锁定模式', '证书管理', '备份(Veeam/SRM)', 'vRealize Operations监控']
                        ]
                    },
                    'Zabbix': {
                        'desc': '开源监控系统',
                        'difficulty': 3,
                        'dimensions': [
                            ['架构部署', 'Server/Agent/Proxy', 'Web前端/LAMP', '数据库(MySQL/PG)', '主机与组', '模板与继承'],
                            ['采集与监控项', 'Item键值(system.cpu.load等)', 'Agent/SNMP/IPMI', '自定义UserParameter', 'HTTP Agent/Web监控', '日志文件监控'],
                            ['告警与通知', 'Trigger表达式', '严重程度(Disaster-High)', 'Action条件与操作', '媒介(Email/Webhook/钉钉)', '告警确认与升级'],
                            ['可视化与发现', 'Graph/Dashboard', 'Map拓扑图', 'Screen/幻灯片', 'LLD低级别发现', '网络发现/Action自动注册'],
                            ['管理与优化', '宏与值映射', '维护期', 'Proxy分布式', 'API集成', '数据库Housekeeping', '性能调优']
                        ]
                    },
                    '存储管理': {
                        'desc': 'SAN、NAS存储配置和管理',
                        'difficulty': 3,
                        'dimensions': [
                            ['存储类型与协议', 'DAS/SAN/NAS', 'FC/iSCSI/NFS/CIFS', '块/文件/对象存储', 'iSCSI Initiator/Target', 'CHAP认证', 'NFS导出与挂载'],
                            ['RAID与磁盘', 'RAID 0/1/5/6/10', '硬件RAID卡/BBU', '热备盘/重建', 'LUN划分与映射', 'Thin/Thick置备'],
                            ['高级特性', '存储多路径(ALUA)', '快照/克隆', '同步/异步复制', '重删/压缩/加密', '存储分层/QoS'],
                            ['分布式存储', 'Ceph架构(OSD/MON/MDS)', 'RBD块存储', 'CephFS文件系统', 'RGW对象存储', 'CRUSH Map', 'GlusterFS/MinIO'],
                            ['运维与性能', '容量监控', 'IOPS/吞吐量计算', '延迟监控', '光纤/SAN排错', '存储品牌(华为/EMC/NetApp)']
                        ]
                    },
                    '高可用': {
                        'desc': 'Keepalived、HAProxy等高可用方案',
                        'difficulty': 3,
                        'dimensions': [
                            ['基本概念', 'HA指标(99.9%/99.99%)', 'SPOF单点故障', 'N+1/2N冗余', 'MTTF/MTTR', 'SLA/停机时间'],
                            ['负载均衡', 'HAProxy frontend/backend', '负载算法(roundrobin/leastconn)', '健康检查(tcp/httpchk)', 'Cookie会话保持', 'ACL与use_backend', 'Stats监控页面'],
                            ['VRRP与Keepalived', 'Keepalived vrrp_instance', 'Master/Backup/priority', 'virtual_ipaddress', 'track_script脚本', 'nopreempt抢占', '脑裂预防'],
                            ['应用高可用', 'Redis Sentinel/Cluster', 'MySQL MHA/Galera', 'PostgreSQL Patroni', 'Pacemaker/Corosync/DRBD', 'Fence/STONITH'],
                            ['架构设计', 'Nginx+Keepalived', 'LVS+Keepalived', 'DNS轮询', '双活数据中心', '故障演练与测试']
                        ]
                    }
                }
            }
        }
    }
}