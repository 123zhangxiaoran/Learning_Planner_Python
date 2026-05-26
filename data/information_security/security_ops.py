"""安全运维工程师数据"""
data = {
    '计算机与信息技术': {
        '信息安全': {
            '安全运维工程师': {
                'description': '监控安全事件，进行应急响应和事后分析。',
                'skills': {
                    '取证分析': {
                        'desc': '数字取证和攻击溯源',
                        'difficulty': 2,
                        'dimensions': [
                            ['取证流程与原则', '依法取证与电子证据', '证据链完整性', '证据获取与保存', '内存/磁盘镜像', '证据哈希(MD5/SHA)'],
                            ['内存与磁盘取证', 'Winpmem/LiME', 'FTK Imager/dd', 'Autopsy/EnCase', 'Volatility分析(pslist/netscan/malfind)', '注册表与MFT分析'],
                            ['Windows日志分析', 'Event ID 4624/4625/4648/4697', 'PowerShell日志', 'Sysmon配置与分析', 'Timeline时间线', '日志文件(evtx)'],
                            ['Linux日志分析', '/var/log/secure/messages', 'bash_history', 'SSH登录日志(last)', '进程/网络分析', 'Rootkit检测(chkrootkit/rkhunter)'],
                            ['恶意软件分析', '文件哈希与字符串', 'PE结构与查壳', 'IDA Pro/Ghidra反汇编', '沙箱(VirusTotal/Any.Run/Cuckoo)', '动态分析(ProcMon/TCPView)'],
                            ['溯源与报告', 'IOC指标(IP/域名/Hash)', '攻击路径重建', '威胁情报(MISP/STIX)', '攻击者画像', '取证报告与电子证据鉴定']
                        ]
                    },
                    '安全监控': {
                        'desc': '安全设备和日志实时监控',
                        'difficulty': 2,
                        'dimensions': [
                            ['监控目标与指标', '可用性/性能/威胁监控', 'CPU/内存/磁盘/网络', '连接数/带宽/延迟', '攻击事件数/告警数量', 'MTTD/MTTR/误报漏报率'],
                            ['监控工具与数据源', 'Zabbix/Prometheus/Grafana', 'ELK/Splunk/Graylog', 'SIEM平台', 'Syslog/Windows Event', 'NetFlow/sFlow/IPFIX'],
                            ['日志解析与关联', '日志格式(JSON/Syslog)', 'Grok/正则解析', '字段提取与标准化', '关联分析(规则/场景/资产)', '告警规则编写'],
                            ['告警管理', '告警级别(严重/高/中/低)', '告警聚合/收敛/抑制', '告警升级(Escalation)', '通知(邮件/钉钉/飞书)', '告警处理流程(确认/响应/关闭)'],
                            ['仪表板与报告', '安全仪表板/网络/主机/应用大屏', '实时监控与趋势分析', '攻击统计与告警统计', 'SLA报告', 'SOC值守与交接班']
                        ]
                    },
                    '安全设备': {
                        'desc': '防火墙、IDS/IPS、WAF等设备运维',
                        'difficulty': 2,
                        'dimensions': [
                            ['防火墙运维', '华为USG/思科ASA/Fortinet', 'Juniper/SRX', '安全区域/策略/NAT', 'DDoS/SYN Flood防护', '双机热备/会话同步'],
                            ['IDS/IPS运维', 'NIDS(Snort/Suricata)', 'HIDS', '部署(端口镜像/TAP)', '规则编写与签名更新', '误报优化与告警分析'],
                            ['WAF运维', 'ModSecurity', 'OWASP CRS规则', '部署(反向代理/透明)', '防SQLi/XSS/CSRF', '绕过防护与规则调优'],
                            ['设备管理与高可用', '设备巡检/健康检查', '配置备份/变更管理', 'Syslog/SNMP配置', '集中管理平台', '故障切换与高可用(HA)']
                        ]
                    },
                    '应急响应': {
                        'desc': '安全事件快速响应和处置',
                        'difficulty': 2,
                        'dimensions': [
                            ['响应流程与团队', 'PDCERF模型', 'CSIRT团队', '事件分级(P1-P4)', '应急预案与Playbook', '时间线与IOC指标'],
                            ['事件处置类型', '勒索软件(加密排查/恢复)', '网络攻击(IP定位/阻断)', 'Web攻击(日志/漏洞排查)', '主机入侵(进程/后门/权限)', '数据泄露(评估/控制/通知)'],
                            ['调查与工具', 'Wireshark/tcpdump抓包', '进程分析/启动项检查', 'Memory/Volatility', '日志分析(Splunk/ELK)', '沙箱分析(Any.Run/VT)'],
                            ['报告与演练', '事件报告/调查报告/复盘', '桌面推演(TTX)', '实战演练/红蓝对抗', 'DDoS/勒索专项演练', '整改措施与事后总结']
                        ]
                    },
                    '日志分析': {
                        'desc': '安全日志分析和威胁识别',
                        'difficulty': 2,
                        'dimensions': [
                            ['日志类型与收集', '系统/安全/应用/网络日志', 'Web/DB/主机/设备日志', 'Syslog/Filebeat收集', 'Elasticsearch/Splunk/Loki存储', '日志保留与归档'],
                            ['解析与标准化', '正则/Grok解析', 'Logstash/字段提取', '字段映射与标准化', 'Syslog格式', 'JSON格式处理'],
                            ['关联与分析规则', '暴力破解/SQL注入场景', '横向移动/权限提升', 'Webshell上传/数据外发', '异常登录/访问/流量', 'IOC搜索(IP/Domain/Hash)'],
                            ['告警与可视化', '告警分类与优先级', '误报识别', 'UEBA用户行为分析', '时间线/关系图谱/地图', 'Kibana/Splunk搜索'],
                            ['工具与平台', 'Splunk/ELK/QRadar', 'Windows事件查看器', 'Linux journalctl/grep/awk', '日志脱敏与合规', '安全周报与威胁报告']
                        ]
                    },
                    '漏洞管理': {
                        'desc': '漏洞扫描和修复跟踪',
                        'difficulty': 2,
                        'dimensions': [
                            ['扫描与发现', 'Nessus/OpenVAS/Qualys', 'AWVS/Nikto/WPScan', 'CVSS评分与CVE库', '漏洞分类(系统/应用/配置)', '弱口令与敏感信息检测'],
                            ['评级与跟踪', '严重/高/中/低/信息级', '漏洞生命周期', '工单系统(JIRA)', '修复期限(SLA:P1-P4)', '漏洞处置流程'],
                            ['修复与验证', '系统补丁(WSUS/yum)', '应用升级与配置修复', 'WAF防护/网络隔离', '复测验证与关闭', '漏洞复盘与闭环率'],
                            ['平台与合规', '漏洞管理平台', '0day应急响应', '等保/ISO 27001合规', '补丁管理(SCCM/Lansweeper)', '补丁测试与回滚']
                        ]
                    },
                    'SIEM': {
                        'desc': '安全信息与事件管理系统',
                        'difficulty': 3,
                        'dimensions': [
                            ['架构与产品', '日志收集/处理/存储/分析', 'Splunk(ES/Forwarder)', 'IBM QRadar/ArcSight', 'Azure Sentinel/阿里云SLS', '绿盟ESM/启明天机'],
                            ['Splunk核心', 'SPL搜索(stats/chart/timechart)', '字段提取与eval计算', '实时告警与保存搜索', '仪表板与可视化', 'CIM数据模型与TA'],
                            ['规则与关联', '关联规则开发', '场景检测(暴力破解/SQLi)', 'UEBA与MLTK', 'MITRE ATT&CK映射', '规则优化与误报处理'],
                            ['部署与运营', 'Forwarder部署/索引规划', '日志源接入(Windows/Linux/云/容器)', '告警分诊/调查/响应', 'MTTD/MTTR优化', '集群高可用与数据保留']
                        ]
                    },
                    'SOC': {
                        'desc': '安全运营中心建设',
                        'difficulty': 3,
                        'dimensions': [
                            ['组织与流程', 'SOC类型(自建/托管/混合)', '团队(Level1-3)', '日常运营与值班', '事件分级(P1-P4)与升级流程', 'KPI(MTTD/MTTR/闭环率)'],
                            ['技术平台', 'SIEM/UEBA/SOAR/XDR', 'CMDB/资产发现', '威胁情报平台/工单系统', 'EDR/NDR/CWPP', '数据源集成(网络/主机/云)'],
                            ['告警与响应', '告警分诊规则', '调查模板与工具', '响应剧本(SOAR Playbook)', '自动化响应', '告警关闭与文档记录'],
                            ['报告与建设', '日报/周报/月报/年报', '态势感知大屏', 'SOC成熟度评估', 'Red Team测试/红蓝对抗', '威胁狩猎(IOC/TTP)']
                        ]
                    },
                    '威胁情报': {
                        'desc': '收集和应用威胁情报',
                        'difficulty': 3,
                        'dimensions': [
                            ['情报分类与生命周期', '战略/战术/运营/技术情报', '规划-收集-处理-分析-传播-反馈', 'ATT&CK(战术/技术/子技术)', '杀伤链(CK)与钻石模型', 'APT组织(APT28/Lazarus/海莲花)'],
                            ['情报源与平台', '开源(OTX/VirusTotal/URLhaus)', '商业(Mandiant/CrowdStrike)', 'MISP平台(事件/属性/Galaxy)', 'TIP(ThreatConnect/微步)', 'STIX/TAXII标准'],
                            ['IOC与技术情报', 'IP/域名/URL/文件哈希', 'C2/僵尸网络/恶意软件家族', '威胁狩猎与关联分析', 'APT追踪与团伙画像', '情报评估(准确性/相关性/时效)'],
                            ['应用与集成', 'SIEM/EDR/防火墙规则集成', 'SOAR自动化响应', '情报订阅与推送', 'IOC搜索与批量查询', '威胁报告与行业情报']
                        ]
                    },
                    '安全加固': {
                        'desc': '系统和应用安全配置',
                        'difficulty': 3,
                        'dimensions': [
                            ['Windows加固', '账户与密码策略', 'Guest禁用/管理员重命名', '审核策略/防火墙', 'SMBv1/NetBIOS禁用', 'BitLocker/EFS加密', 'RDP安全(NLA)'],
                            ['Linux加固', 'SELinux/AppArmor', 'PAM认证/sudo权限', 'SSH加固(密钥/禁密码)', 'iptables/firewalld', '内核参数(sysctl)'],
                            ['服务与应用加固', 'Apache/Nginx(隐藏版本/TLS)', 'MySQL/Redis(密码/绑定)', 'Tomcat/中间件安全', 'SSL/TLS/Cipher Suite', 'HSTS与安全头'],
                            ['云与自动化加固', 'IAM/VPC/安全组加固', 'Docker/K8s安全', 'CIS基线核查', 'Ansible/脚本自动化', '漏洞修补与配置审计']
                        ]
                    }
                }
            }
        }
    }
}