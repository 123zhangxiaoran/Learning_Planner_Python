"""网络安全工程师数据"""
data = {
    '计算机与信息技术': {
        '网络工程': {
            '网络安全工程师': {
                'description': '负责网络安全防护，渗透测试和安全漏洞修复。',
                'skills': {
                    'Nmap': {
                        'desc': '网络扫描和端口探测工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['扫描技术', 'TCP SYN扫描(-sS)', 'TCP Connect扫描(-sT)', 'UDP扫描(-sU)', 'FIN/NULL/XMAS扫描', 'ACK/Window扫描', '协议扫描(-sO)'],
                            ['主机发现与端口', 'Ping扫描(-sn)', '无Ping扫描(-Pn)', '端口范围(-p)', '快速扫描(-F)', '全面扫描(-A)'],
                            ['服务与系统检测', '版本检测(-sV)', '操作系统检测(-O)', 'NSE脚本引擎', '常见脚本(vuln/safe/auth)', 'Banner抓取'],
                            ['高级选项', '扫描速度(-T0~T5)', '分片扫描(-f)', '诱饵扫描(-D)', '空闲扫描(-sI)', '源地址欺骗(-S)'],
                            ['输出与工具', '输出格式(-oA/-oN/-oX)', '详细调试(-v/-d)', 'Zenmap图形界面', 'Ndiff差异扫描', 'Python集成(python-nmap)']
                        ]
                    },
                    'Web安全': {
                        'desc': 'SQL注入、XSS、CSRF等Web攻击原理和防护',
                        'difficulty': 2,
                        'dimensions': [
                            ['SQL注入', '注入类型(数字/字符/盲注/报错/联合/堆叠)', 'SQLMap自动化', 'Tamper绕过脚本', '防护(参数化查询/预编译/ORM/白名单)'],
                            ['XSS跨站脚本', '反射型/存储型/DOM型', 'Cookie窃取与Session劫持', 'BeEF框架', '防护(HttpOnly/CSP/X-XSS-Protection/HTML转义)'],
                            ['CSRF与SSRF', 'CSRF原理与Token防护', 'SameSite Cookie', 'SSRF内网探测与协议利用(file/gopher)', 'SSRF Redis利用', '防护(URL白名单/协议限制)'],
                            ['文件与代码漏洞', '文件上传(扩展名/Content-Type/MIME绕过)', '文件包含(LFI/RFI/PHP伪协议)', '命令注入与代码执行(RCE)', '反序列化漏洞(Java/PHP/Python)'],
                            ['业务与逻辑漏洞', '越权访问(水平/垂直)', '验证码绕过', '支付漏洞/并发问题', '接口未授权访问', 'XXE外部实体注入']
                        ]
                    },
                    'Wireshark': {
                        'desc': '网络协议分析和抓包工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['捕获与过滤器', '网卡选择/混杂模式', '捕获过滤器(BPF语法)', '主机/端口/协议过滤', '显示过滤器(http/tcp/dns)', '颜色规则与标记'],
                            ['协议分析', 'TCP三次握手/四次挥手', '重传与窗口分析', 'HTTP请求响应', 'TLS握手与证书', 'DNS/ARP/DHCP/ICMP分析'],
                            ['高级功能', 'Follow TCP Stream', 'Expert Info专家信息', 'IO Graphs/Statistics统计', '对象导出(HTTP/SMB)', 'TCP流图(往返时间/吞吐量)'],
                            ['命令行工具', 'tshark捕获与分析', 'editcap裁剪', 'mergecap合并', 'capinfos文件信息', 'text2pcap文本转换']
                        ]
                    },
                    '等保合规': {
                        'desc': '网络安全等级保护测评和整改',
                        'difficulty': 2,
                        'dimensions': [
                            ['等保体系', '等保1.0与2.0', '五级保护等级', '新技术要求(云/大数据/物联网/工控)', 'GB/T 22239-2019'],
                            ['安全要求', '安全物理环境', '安全通信网络', '安全区域边界', '安全计算环境', '安全管理中心', '安全管理制度/机构/人员/建设/运维'],
                            ['测评与整改', '定级备案', '建设整改', '等级测评(CNAS机构)', '高风险判定', '合规报告']
                        ]
                    },
                    '防火墙': {
                        'desc': '访问控制策略配置和网络边界防护',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与区域', '包过滤/状态检测/代理/NGFW', '安全区域(Trust/Untrust/DMZ/Local)', '安全策略与默认拒绝', '会话管理与状态表'],
                            ['NAT与攻击防护', '源NAT/目的NAT/双向NAT', 'DDoS防护(SYN/ICMP/UDP Flood)', '入侵防御(IPS)与WAF', '病毒/URL/内容过滤', 'SSL解密'],
                            ['高可用与运维', '双机热备(主备/主主)', '会话同步', 'Bypass卡', '策略路由', '日志审计与集中管理', '华为USG/思科ASA/Fortinet等'],
                        ]
                    },
                    'Burp Suite': {
                        'desc': 'Web应用安全测试平台',
                        'difficulty': 3,
                        'dimensions': [
                            ['核心代理与目标', 'Proxy拦截/History', 'Target站点地图', 'Scope范围设置', '被动/主动扫描', 'Scanner漏洞列表'],
                            ['攻击与重放', 'Intruder攻击模式(Sniper/Battering Ram/Cluster Bomb)', 'Payload类型(简单列表/数字/暴力)', 'Repeater请求修改', 'Decoder编码解码'],
                            ['扩展与自动化', 'Extender加载BApp', 'SQLMap集成', 'JWT攻击', 'Burp Collaborator(OOB)', '宏/Session处理']
                        ]
                    },
                    'IDS/IPS': {
                        'desc': '入侵检测和防御系统部署',
                        'difficulty': 3,
                        'dimensions': [
                            ['检测类型', 'NIDS/HIDS', '签名检测/异常检测/混合检测', '部署(内联/旁路/SPAN/TAP)'],
                            ['开源平台', 'Snort规则(动作/协议/内容/PCRE)', 'Suricata(高性能)', 'Zeek/Bro脚本', 'OSSEC/Wazuh', 'Samhain/Tripwire文件完整性'],
                            ['规则与告警', 'Snort/Suricata规则编写', '威胁情报(ET/STIX/TAXII/MISP)', '告警优化(误报/漏报)', 'Snorby/BASE/Splunk集成']
                        ]
                    },
                    'Kali Linux': {
                        'desc': '专业渗透测试操作系统及工具使用',
                        'difficulty': 3,
                        'dimensions': [
                            ['信息收集', 'OSINT(whois/dig/theHarvester)', 'Shodan/Google Dorks', 'Nmap/Nikto/Dirb/Gobuster', 'WPScan'],
                            ['漏洞利用', 'Metasploit框架(msfconsole/msfvenom)', '永恒之蓝/MS17-010', 'Mimikatz/哈希传递', 'Kerberos攻击(Golden/Silver Ticket)'],
                            ['Web与密码', 'Burp Suite/ZAP', 'SQLMap', 'Hydra/John/Hashcat', 'SET钓鱼', 'BeEF XSS框架'],
                            ['高级', '内网穿透(端口转发/Pivot)', '免杀(Veil/Shellter)', '无线(Aircrack-ng)', '逆向(Ghidra/Radare2)', '取证(Autopsy/Volatility)']
                        ]
                    },
                    'Metasploit': {
                        'desc': '漏洞利用框架和渗透测试工具',
                        'difficulty': 3,
                        'dimensions': [
                            ['核心使用', 'msfconsole/msfvenom', '模块(Exploit/Auxiliary/Post)', 'search/set/run', 'meterpreter载荷', 'handler监听'],
                            ['后渗透', 'getsystem提权', 'migrate进程迁移', 'hashdump/mimikatz凭证获取', 'portfwd/autoroute内网穿透', 'persistence维持访问'],
                            ['载荷生成', '反向/正向Shell', 'Staged/Stageless', '编码器(shikata_ga_nai)', 'msfvenom多格式输出', '免杀处理']
                        ]
                    },
                    'WAF': {
                        'desc': 'Web应用防火墙配置和规则调优',
                        'difficulty': 3,
                        'dimensions': [
                            ['原理与部署', '透明/反向代理/旁路', 'ModSecurity/CRS规则', '检测引擎(正则/语义/机器学习)'],
                            ['规则与绕过', 'SecRule语法(变量/操作/阶段)', 'CRS Paranoia Level', 'SQL/XSS绕过(编码/注释/等价替换)', '白名单与黑名单'],
                            ['产品与优化', '云WAF(Cloudflare/AWS/阿里云)', '硬件WAF(Imperva/F5)', 'RASP(Safeline/OpenRASP)', 'Bot防护/CC攻击防护', '日志与告警']
                        ]
                    },
                    '代码审计': {
                        'desc': '审查源代码发现安全漏洞',
                        'difficulty': 3,
                        'dimensions': [
                            ['流程与工具', '审计流程(准备/分析/验证)', 'SAST工具(Fortify/SonarQube/Semgrep)', '依赖检查(npm audit/Snyk)', 'Python Bandit/Java FindSecBugs'],
                            ['漏洞模式', 'SQL注入审计点(PHP $_GET/Java JDBC)', 'XSS输出点(echo/print)', '命令注入(system/exec)', '反序列化(unserialize/readObject)', '文件包含/SSRF/XXE'],
                            ['业务与报告', '认证/会话/JWT审计', '越权(IDOR)', '硬编码密码与API密钥', '漏洞评级与修复建议']
                        ]
                    },
                    '安全加固': {
                        'desc': '操作系统和应用的安全配置',
                        'difficulty': 3,
                        'dimensions': [
                            ['Windows加固', '账户重命名/Guest禁用', '密码策略/账户锁定', '审核策略/防火墙', 'SMBv1禁用/PowerShell约束', 'BitLocker/EFS加密', 'RDP安全(NLA)'],
                            ['Linux加固', 'SELinux/AppArmor', 'PAM认证/sudo权限', 'SSH加固(密钥/禁密码/禁Root)', 'iptables/firewalld', '内核参数(sysctl)'],
                            ['服务加固', 'Apache/Nginx(TLS/隐藏版本)', 'MySQL(安全初始化/最小权限)', 'Redis(密码/绑定/危险命令禁用)', 'Tomcat/SSL/TLS', '基线核查(CIS/等保)']
                        ]
                    },
                    '应急响应': {
                        'desc': '安全事件处理和取证分析',
                        'difficulty': 3,
                        'dimensions': [
                            ['响应流程', 'PDCERF模型(准备/检测/遏制/根除/恢复)', 'CSIRT/事件分级', '时间线与IOC', '预案与Playbook'],
                            ['取证分析', '内存镜像(Volatility)', '磁盘镜像(Autopsy/dd)', '日志分析(Windows Event ID 4624/4688, Linux /var/log)', 'Rootkit检测(rkhunter)'],
                            ['恶意软件', '静态分析(PE/IDA Pro/Ghidra)', '动态分析(Process Monitor/TCPView)', '沙箱(Any.Run/Cuckoo)', '勒索软件/WannaCry', 'WebShell检测(冰蝎/哥斯拉)'],
                            ['APT与溯源', '威胁情报(MISP/STIX)', 'APT组织(APT29/Lazarus)', '攻击溯源与画像', '应急演练与复盘']
                        ]
                    },
                    '渗透测试': {
                        'desc': '模拟攻击测试系统安全性，发现安全弱点',
                        'difficulty': 3,
                        'dimensions': [
                            ['方法论与信息收集', 'PTES/OWASP指南', '资产发现(Recon-ng/Shodan)', 'DNS/子域名枚举', 'Google Dorks', '漏洞扫描(Nessus/OpenVAS)'],
                            ['Web渗透', 'SQL注入(Union/盲注/SQLMap)', 'XSS(BeEF)', 'CSRF/SSRF', '文件上传/包含', '业务逻辑(越权/支付)', 'JWT攻击'],
                            ['内网与提权', 'MS17-010永恒之蓝', '哈希传递(PTH)', 'Kerberos攻击(黄金/白银票据)', '横向移动(PsExec/WMI)', '权限提升(UAC/sudo/SUID/内核)'],
                            ['持久化与报告', '注册表/WMI/计划任务后门', '域持久化(AdminSDHolder/DCSync)', '社工钓鱼(SET/邮件)', '渗透测试报告(漏洞详情/POC/修复)']
                        ]
                    },
                    '漏洞扫描': {
                        'desc': 'Nessus、OpenVAS等自动化漏洞扫描工具',
                        'difficulty': 3,
                        'dimensions': [
                            ['漏洞库与标准', 'CVE/CVSS评分', 'NVD/CNVD/CNNVD', '漏洞分类'],
                            ['商业扫描器', 'Nessus(策略/模板/报告)', 'Nexpose/Qualys', 'AWVS/Acunetix', 'AppScan'],
                            ['开源扫描器', 'OpenVAS(GVM)', 'Nikto', 'WPScan/JoomScan', 'OWASP ZAP', 'SQLMap'],
                            ['管理与集成', '扫描调度与凭证', '误报处理与漏洞验证', '修复优先级与补丁', 'CI/CD集成(Jenkins)', '基线扫描(CIS/等保)']
                        ]
                    }
                }
            }
        }
    }
}