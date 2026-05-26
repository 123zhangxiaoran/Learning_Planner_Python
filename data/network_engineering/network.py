"""网络工程师数据"""
data = {
    '计算机与信息技术': {
        '网络工程': {
            '网络工程师': {
                'description': '负责企业网络规划、搭建和维护，保障网络稳定运行。',
                'skills': {
                    'ACL': {
                        'desc': '访问控制列表，网络安全策略配置',
                        'difficulty': 2,
                        'dimensions': [
                            ['ACL概述与类型', '标准ACL(基于源IP)', '扩展ACL(多条件)', 'ACL编号(1-99标准/100-199扩展)', '命名ACL', '通配符掩码与any/host匹配'],
                            ['应用与方向', '入站ACL/出站ACL', '接口应用(Interface apply)', 'VLAN ACL(VACL)', 'PACL', '自反ACL/动态ACL/时间ACL'],
                            ['配置与优化', '思科ACL配置(IOS)', '华为ACL配置(VRP)', 'ACL顺序与隐含deny any', 'ACL日志与注释', 'ACL性能影响与条目优化'],
                            ['扩展应用', '策略路由(PBR)', '流量过滤', '安全策略实施', 'DMZ隔离', 'QoS基础', 'IPv6 ACL']
                        ]
                    },
                    'NAT': {
                        'desc': '网络地址转换，实现内外网通信',
                        'difficulty': 2,
                        'dimensions': [
                            ['地址类型与原理', '私有IP地址(A/B/C类)', '公有IP地址', '静态NAT/动态NAT', 'PAT/端口地址转换(Overloading)', 'Easy IP'],
                            ['地址域与术语', 'Inside Local/Inside Global', 'Outside Local/Outside Global', 'NAT inside/outside接口', '会话表与超时时间'],
                            ['配置与应用', '静态NAT/动态NAT配置', 'overload端口复用', '源NAT(SNAT)/目的NAT(DNAT)', '端口映射/服务器映射', 'NAT Pool地址池'],
                            ['高级NAT', '双向NAT', 'NAT ALG(FTP/DNS/VoIP)', 'NAT穿透(STUN/TURN/ICE)', '对称NAT/Cone NAT', '高可用NAT/负载均衡NAT']
                        ]
                    },
                    'TCP/IP': {
                        'desc': '网络通信核心协议栈，理解IP寻址和路由原理',
                        'difficulty': 2,
                        'dimensions': [
                            ['模型与分层', 'OSI七层模型', 'TCP/IP四层模型', '数据封装与解封装', 'MTU与分片重组'],
                            ['传输层协议', 'TCP三次握手/四次挥手', 'TCP状态机', 'TCP可靠性(ACK/重传)', '滑动窗口与流量控制', '拥塞控制(慢启动/快恢复)', 'UDP协议特点'],
                            ['网络层与IP', 'IPv4地址分类(A/B/C/D/E)', '子网掩码与CIDR/VLSM', '公/私有IP', 'ARP/RARP/ICMP', 'Ping/Traceroute原理', 'IPv6地址格式'],
                            ['应用层协议', 'DNS域名解析', 'DHCP动态地址获取', 'HTTP/HTTPS', 'FTP/SFTP/TFTP', 'SMTP/POP3/IMAP', 'SSH/Telnet/SNMP'],
                            ['路由基础', '路由表与路由原理', '直连路由/静态路由/默认路由', '动态路由协议分类(RIP/OSPF/BGP)', '路由聚合与IP地址规划']
                        ]
                    },
                    'VLAN': {
                        'desc': '虚拟局域网划分和配置',
                        'difficulty': 2,
                        'dimensions': [
                            ['VLAN基础', '广播域与冲突域', 'VLAN划分方式(端口/MAC/协议)', 'Access端口/Trunk端口/Hybrid端口', 'PVID与VLAN ID(1-4094)', '802.1Q标签与Native VLAN'],
                            ['VLAN间路由', '单臂路由(子接口)', '三层交换(SVI接口)', 'VLAN间路由配置', 'VLANIF接口'],
                            ['高级VLAN', 'VTP协议(Server/Client/Transparent)', 'VTP裁剪', 'QinQ(双层标签/VLAN Tunnel)', '私有VLAN(PVLAN)', 'Super VLAN/聚合VLAN', 'Voice VLAN/Guest VLAN'],
                            ['生成树与高可用', 'PVST/PVST+/Rapid-PVST', 'MSTP多实例生成树', '堆叠/iStack/CSS', 'VSS/vPC/MLAG', 'VLAN安全与VLAN映射'],
                            ['配置实践', '华为VLAN配置(port default vlan/port trunk allow-pass)', '思科VLAN配置(switchport mode/switchport trunk)', 'VLAN规划与IP对应']
                        ]
                    },
                    '网络协议': {
                        'desc': 'HTTP、DNS、DHCP、FTP等应用层协议原理',
                        'difficulty': 2,
                        'dimensions': [
                            ['HTTP与Web', 'HTTP/1.1 vs HTTP/2/3', '请求方法/状态码', '请求/响应头', 'Keep-Alive与Cookie', '缓存机制(Cache-Control/ETag)', 'HTTPS/TLS握手与证书'],
                            ['DNS系统', '根域名服务器/TLD/权威DNS', '递归与迭代查询', 'DNS记录类型(A/AAAA/CNAME/MX)', 'DNS缓存与TTL', 'DNS负载均衡', 'DNSSEC/DoH'],
                            ['邮件与文件传输', 'SMTP/POP3/IMAP4', 'MIME/Base64编码', 'FTP主动/被动模式', 'SFTP/FTPS/TFTP', 'SSH/SCP/SFTP'],
                            ['管理与监控', 'SNMP(v1/v2c/v3)与MIB/OID', 'SNMP Get/Set/Trap', 'NTP时间同步', 'LDAP目录服务', 'RADIUS/TACACS+认证', 'WebSocket/WebRTC']
                        ]
                    },
                    '网络排障': {
                        'desc': '使用ping、traceroute、Wireshark等工具排查故障',
                        'difficulty': 2,
                        'dimensions': [
                            ['排障方法', '分层排障(自顶向下/自底向上)', '替换法与分而治之', '物理层/链路层/网络层/传输层/应用层排障', '基线对比法'],
                            ['基础命令', 'ping/tracert/pathping', 'ipconfig/ifconfig/ip addr', 'netstat/ss', 'arp -a/route/nslookup/dig'],
                            ['抓包与分析', 'Wireshark过滤(Display/Capture Filter)', 'tcpdump/tshark', 'Follow TCP Stream', 'Expert Info与IO Graph', 'TCP三次握手/四次挥手分析', 'HTTP/DNS请求分析'],
                            ['扫描与工具', 'nmap端口扫描(SYN/TCP/UDP/O)', '日志分析(Syslog)', '网络监控工具', '设备日志查看与等级']
                        ]
                    },
                    '网络监控': {
                        'desc': 'SNMP、Zabbix等网络监控工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['SNMP监控', 'SNMP架构(Manager/Agent)', 'SNMPv2c/v3与Community', 'GET/SET/Trap/Inform', 'MIB/OID与MIB Browser', 'SNMP轮询与Trap接收'],
                            ['Zabbix平台', 'Zabbix Server/Agent/Proxy架构', '主机/模板/监控项/触发器', '告警与动作', '自动发现与网络发现', 'Zabbix API'],
                            ['开源与商业工具', 'Prometheus + Exporter + Grafana', 'Cacti(RRDtool)', 'Nagios/Centreon/OpenNMS', 'SolarWinds NPM/PRTG', 'LibreNMS'],
                            ['监控指标与告警', 'CPU/内存/接口流量监控', '带宽/延迟/丢包/抖动', 'Syslog收集(ELK/Loki)', 'Dashboard大屏', '告警收敛/抑制/升级', 'SLA与可用性报告']
                        ]
                    },
                    '防火墙': {
                        'desc': '网络安全边界防护设备配置和管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['防火墙类型与区域', '包过滤/状态检测/代理/NGFW', '安全区域(Trust/Untrust/DMZ/Local)', '安全策略与默认策略', '会话管理与状态表', '用户身份认证与时间计划'],
                            ['NAT与攻击防护', '源NAT/目的NAT/双向NAT', 'Server Map与黑洞路由', 'DDoS防护(SYN/ICMP/UDP Flood)', '扫描/IP欺骗/Land攻击防护', '入侵防御(IPS)与WAF集成', 'URL/内容过滤与病毒防护'],
                            ['高级功能', 'SSL解密与证书验证', '沙箱检测与威胁情报', 'QoS带宽限制与连接限制', '高可用(主备/主主/会话同步)', 'Bypass卡与故障切换', '策略路由与链路聚合'],
                            ['运维与产品', '日志审计与集中管理', '策略备份与优化', '吞吐/新建/并发性能指标', '华为USG/思科ASA/Firepower', 'Juniper SRX/Fortinet FortiGate', 'Palo Alto/天融信/启明星辰']
                        ]
                    },
                    'BGP': {
                        'desc': '边界网关协议，互联网核心路由协议',
                        'difficulty': 3,
                        'dimensions': [
                            ['BGP基础与邻居', '路径矢量协议/TCP 179', 'IBGP/EBGP', '邻居状态机(Idle→Established)', '消息类型(Open/Update/Keepalive/Notification)', 'BGP路由宣告(Network/Import)'],
                            ['路径属性与选路', 'AS-Path/Next-Hop/Origin', 'Local Preference/MED', 'Weight/Community', '8条选路规则详解', 'AS-Path长度与MED比较'],
                            ['高级功能', '路由反射器(RR)与联盟(Confederation)', 'IBGP水平分割与同步', 'BGP路由聚合(AS-SET)', '路由过滤(前缀列表/AS-Path列表/Route Map)', 'Community属性应用(No-Export/No-Advertise)'],
                            ['可靠性与优化', 'BFD联动', 'Graceful Restart(GR)', 'BGP Dampening(路由抖动惩罚)', '多宿主与负载均衡', 'MP-BGP与MPLS VPN', 'BGP Flowspec/BGPsec/RPKI']
                        ]
                    },
                    'Cisco': {
                        'desc': '思科网络设备配置和管理，CCNA/CCNP认证相关技术',
                        'difficulty': 3,
                        'dimensions': [
                            ['基础操作', 'IOS CLI模式(用户/特权/全局/接口)', 'show命令族(version/ip interface brief/running-config/ip route/vlan)', 'hostname/enable密码/SSH配置', '接口配置(ip address/no shutdown/speed/duplex)'],
                            ['交换技术', 'VLAN创建与端口模式(access/trunk)', 'DTP/VTP配置', 'STP模式/PortFast/BPDUGuard', 'EtherChannel(PAGP/LACP)', 'HSRP/VRRP/GLBP网关冗余', '堆叠(StackWise)/VSS'],
                            ['路由与安全', '静态/默认/RIP/EIGRP/OSPF/BGP配置', 'ACL(access-list/ip access-group)', 'NAT(ip nat inside/static/pool)', 'DHCP(ip dhcp pool)', 'IPSec VPN(crypto isakmp/ipsec/transform-set)'],
                            ['运维与工具', '配置保存(copy run start)/备份恢复', 'IOS升级/密码恢复', 'CDP/LLDP/SPAN/RSPAN', 'Cisco DNA Center/SD-Access/SD-WAN', 'Meraki云管理', 'CCNA/CCNP/CCIE认证']
                        ]
                    },
                    'H3C': {
                        'desc': '华三网络设备配置和管理',
                        'difficulty': 3,
                        'dimensions': [
                            ['CLI与基础配置', 'Comware CLI视图(用户/系统/接口)', 'display命令族(current-configuration/interface brief/ip routing-table/vlan)', 'sysname/ip address/undo shutdown', '接口与VLAN(port access/trunk/hybrid/vlan batch)'],
                            ['交换与高可用', 'STP/MSTP配置', '端口安全/802.1X/MAC绑定', 'IRF堆叠与MAD检测', '链路聚合(静态/LACP)', 'VRRP配置'],
                            ['路由与策略', '静态/默认/RIP/OSPF/BGP配置', 'BFD联动', '路由策略(route-policy/if-match/apply)', '路由引入与聚合'],
                            ['安全与特性', 'ACL(acl/rule/packet-filter)', 'NAT(nat outbound/nat server/easy-ip)', 'DHCP(dhcp enable/server/relay)', 'IPSec/SSL VPN', 'QoS(流分类/流行为/流策略/CAR/GTS)'],
                            ['运维管理', 'info-center日志/snmp-agent/ntp', 'SSH/telnet/stelnet', 'FTP/配置文件保存(save)', 'HRP双机热备', 'H3C认证(H3CNE/H3CSE/H3CIE)']
                        ]
                    },
                    'OSPF': {
                        'desc': '开放式最短路径优先，内部网关路由协议',
                        'difficulty': 3,
                        'dimensions': [
                            ['基本概念', '链路状态协议/SPF算法', '区域(Area 0/非骨干)', 'Stub/Totally Stub/NSSA', '路由器类型(IR/ABR/ASBR)', 'Router ID'],
                            ['邻居与网络类型', '邻居状态机(Down→Full)', 'DR/BDR选举(Priority)', '广播/点对点/NBMA/P2MP网络类型', 'Hello/Dead间隔', 'LSA类型(1-5/7)与泛洪'],
                            ['路由与汇总', '区域间路由(Summary LSA)', '外部路由(E1/E2/N1/N2)', '路由汇总(ABR/ASBR)', '虚链路(Virtual Link)', '默认路由(default-information originate)'],
                            ['认证与优化', '区域/接口认证(明文/MD5)', 'Cost计算与参考带宽', 'OSPFv3(IPv6)', 'GR/Graceful Restart', 'BFD联动', '路由过滤与重分发']
                        ]
                    },
                    'STP': {
                        'desc': '生成树协议，防止网络环路',
                        'difficulty': 3,
                        'dimensions': [
                            ['STP基础与选举', '广播风暴/MAC地址震荡', 'BPDU(Config/TCN)', 'Bridge ID与根桥选举', '根端口/指定端口/阻塞端口选举', '端口状态(Blocking→Forwarding)', '路径开销与计时器(Hello/Forward Delay/Max Age)'],
                            ['快速与多实例', 'RSTP(802.1w)端口角色与边缘端口', 'RSTP提案/同意机制', 'MSTP(802.1s)实例与VLAN映射', 'CIST/IST/区域根', 'PVST/PVST+/Rapid-PVST'],
                            ['防护与优化', 'BPDU Guard/BPDU Filter', 'Root Guard/Loop Guard', 'UDLD/Storm Control', 'TCN防护/TC BPDU Guard', 'UplinkFast/BackboneFast', 'P/A机制与BFD联动'],
                            ['高可用集成', '堆叠/iStack与STP', 'VSS/vPC与STP', 'M-LAG与STP', 'STP配置与调试']
                        ]
                    },
                    'VPN': {
                        'desc': '虚拟专用网络，IPSec和SSL VPN配置',
                        'difficulty': 3,
                        'dimensions': [
                            ['IPSec VPN原理', 'IPSec协议族(ESP/AH)', 'IKEv1/IKEv2(Phase1/Phase2)', '主模式/野蛮模式/快速模式', 'DH密钥交换', '加密(AES)/哈希(SHA)/认证(PSK/证书)', 'NAT穿越(NAT-T)'],
                            ['IPSec VPN配置', 'ISAKMP策略(crypto isakmp policy)', 'IPSec变换集(transform-set)', '加密图(crypto map)与ACL', 'GRE over IPSec', 'DMVPN(mGRE+NHRP)', 'FlexVPN'],
                            ['SSL/L2TP VPN', 'SSL VPN(Web/客户端模式)', 'AnyConnect客户端', 'L2TP VPN(L2TP over IPSec)', 'PPTP VPN', 'WireGuard', 'VxLAN隧道'],
                            ['MPLS VPN', 'MPLS标签与LDP', 'VRF/RT/RD', 'PE/CE/P路由器', 'MP-BGP', 'VPN高可用与冗余']
                        ]
                    },
                    'VRRP': {
                        'desc': '虚拟路由冗余协议，实现网关高可用',
                        'difficulty': 3,
                        'dimensions': [
                            ['协议基础', 'VRRP组/虚拟IP/虚拟MAC', '主/备份路由器', '优先级与抢占(Preempt)', '定时器(Hello/Master Down)', '状态(Master/Backup)', 'VRRPv2 vs VRRPv3(IPv6)'],
                            ['跟踪与联动', 'Track接口/路由/优先级下降', 'BFD快速检测联动', 'NQA联动', '与OSPF/BGP联动', '备份通道'],
                            ['对比与扩展', 'HSRP/GLBP对比', 'VRRP多组负载均衡', '双主问题与优化', 'VGMP/HRP华为组管理', 'M-LAG+VRRP', 'VXLAN+VRRP'],
                            ['配置与实践', 'vrrp vrid/virtual-ip/priority/preempt/track', '思科vrrp配置', '故障切换与收敛时间', '日志与监控']
                        ]
                    },
                    '华为设备': {
                        'desc': '华为路由交换设备配置，HCIA/HCIP认证',
                        'difficulty': 3,
                        'dimensions': [
                            ['VRP系统与CLI', 'VRP视图(用户/系统/接口/协议)', 'display命令族', 'sysname/clock/header', '用户接口与认证(authentication-mode/protocol inbound)', 'FTP/SFTP/SSH(stelnet)'],
                            ['接口与交换', '接口配置(ip address/undo shutdown/description/mtu/combo-port)', 'VLAN(vlan batch/port default vlan/port trunk allow-pass)', 'STP(stp enable/stp mode/stp root)', 'Eth-Trunk(手工/LACP)', '堆叠(Stack)与MAD'],
                            ['路由协议', '静态/默认路由(ip route-static)', 'RIP/OSPF/ISIS/BGP配置', 'import-route/aggregate', 'route-policy/filter-policy', 'BFD联动'],
                            ['安全与特性', 'ACL(acl/rule/traffic-filter)', 'NAT(nat address-group/nat server/easy-ip)', 'DHCP(dhcp enable/dhcp server/relay)', 'QoS(流分类/流行为/流策略/CAR/GTS/HQoS)', 'SNMP/日志/NTP'],
                            ['高可靠与认证', 'VRRP(vrrp vrid/virtual-ip/priority/preempt/track)', 'HRP双机热备', 'MPLS LDP', 'SSH/HTTPS/证书', '配置保存(save)与备份', 'HCIA/HCIP/HCIE认证']
                        ]
                    },
                    '负载均衡': {
                        'desc': 'F5、Nginx等负载均衡设备配置',
                        'difficulty': 3,
                        'dimensions': [
                            ['概念与算法', 'L4/L7负载均衡', '轮询/加权轮询/最少连接/加权最少连接', 'IP Hash/URL Hash/一致性哈希', '最小响应时间', '全局负载均衡(GSLB)'],
                            ['健康检查与会话保持', 'TCP/HTTP/HTTPS健康检查', '主动/被动健康检查', '故障检测与转移', 'Cookie会话保持(Sticky Cookie)', '源IP会话保持'],
                            ['产品与平台', 'F5 Big-IP LTM(VS/Pool/Node/iRule/OneConnect)', 'Nginx upstream(ip_hash/least_conn/proxy_pass)', 'HAProxy(frontend/backend/balance/option httpchk)', 'LVS(NAT/DR/TUN模式)', '阿里云SLB/ALB/NLB/CLB'],
                            ['高级功能与运维', 'SSL卸载/终止/证书配置', '连接复用(Keep-Alive)', '会话同步与高可用(Active-Active/Active-Passive)', '连接限速/带宽限速', '日志/监控/QPS/并发/响应时间', '负载均衡算法选择与故障排查']
                        ]
                    }
                }
            }
        }
    }
}