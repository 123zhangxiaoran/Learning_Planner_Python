"""测试工程师数据"""
data = {
    '计算机与信息技术': {
        '软件工程': {
            '测试工程师': {
                'description': '负责软件质量保证，设计和执行测试用例，发现并跟踪缺陷，确保产品发布质量。',
                'skills': {
                    'JUnit': {
                        'desc': 'Java单元测试框架，支持TDD开发模式',
                        'difficulty': 1,
                        'dimensions': [
                            ['核心注解与生命周期', '@Test', '@Before/@After', '@BeforeClass/@AfterClass', '@Ignore', '执行顺序'],
                            ['断言与匹配器', 'assertEquals/assertTrue', 'assertThat与Hamcrest', '异常测试(expected)', '超时测试(timeout)'],
                            ['参数化与套件', '@Parameterized与参数源', '测试套件(@Suite)', 'Runner与Rule', 'Theory'],
                            ['Mockito集成', '@Mock/@Spy/@InjectMocks', 'when/thenReturn', 'verify验证', 'ArgumentCaptor', 'BDD风格(given/when/then)'],
                            ['高级特性', '测试隔离', '监听器(TestListener)', '标签过滤', '与Maven/Gradle集成', 'TestNG对比']
                        ]
                    },
                    'Postman': {
                        'desc': 'API接口测试工具，支持自动化测试集合和环境管理',
                        'difficulty': 1,
                        'dimensions': [
                            ['请求与响应', '方法(GET/POST/PUT/DELETE)', 'Headers/Params/Body', '认证(Basic/Bearer/JWT)', 'JSON/XML解析'],
                            ['变量与环境', '环境变量与全局变量', '变量语法{{var}}', 'Pre-request Script', 'Tests脚本与pm对象'],
                            ['集合与运行', 'Collections/Folder', 'Runner与循环迭代', '数据驱动(CSV/JSON)', '批量运行'],
                            ['自动化与集成', 'Newman命令行', 'CI/CD集成(Jenkins/GitHub Actions)', '导出/导入(Swagger/OpenAPI)'],
                            ['进阶与调试', 'Mock Server', '代理与证书', 'WebSocket/gRPC/GraphQL', '脚本调试(console.log)']
                        ]
                    },
                    'pytest': {
                        'desc': 'Python测试框架，功能强大且易于使用',
                        'difficulty': 1,
                        'dimensions': [
                            ['测试发现与执行', 'test_函数与类', 'conftest.py', '命令行参数(-v/-k/-m)', 'skip/skipif/xfail标记'],
                            ['断言与异常', 'assert断言', '异常测试(pytest.raises)', '警告捕获', '自定义断言'],
                            ['fixture机制', '@pytest.fixture', 'scope作用域', 'autouse自动使用', 'conftest共享', 'yield teardown'],
                            ['参数化与数据驱动', '@parametrize', '多参数组合', 'ids用例ID', 'indirect参数传递'],
                            ['插件与扩展', 'pytest-xdist并行', 'pytest-cov覆盖率', 'pytest-html报告', '自定义插件与hook'],
                            ['集成与工具', 'Jenkins/GitHub Actions', 'mock与patch', 'monkeypatch/capsys', '临时目录(tmp_path)', 'unittest混合']
                        ]
                    },
                    '测试用例设计': {
                        'desc': '等价类划分、边界值分析、场景法等测试设计方法',
                        'difficulty': 1,
                        'dimensions': [
                            ['设计方法', '等价类划分', '边界值分析', '场景法(基本流/备选流)', '判定表与因果图', '正交试验法'],
                            ['覆盖准则', '语句覆盖/分支覆盖', '条件覆盖/判定覆盖', '条件组合覆盖/路径覆盖', 'MC/DC覆盖', '循环覆盖'],
                            ['用例要素', '标题/ID/优先级', '前置条件/步骤/数据', '预期结果/实际结果', '状态与跟踪', '需求追溯'],
                            ['测试策略', '冒烟测试/回归测试', '功能/非功能测试', '接口/性能/安全/兼容性测试', '易用性/可靠性/可移植性测试'],
                            ['评审与管理', '用例评审', '测试计划与资源', '覆盖率统计', '测试准出标准', '测试报告']
                        ]
                    },
                    '缺陷管理': {
                        'desc': '使用Jira等工具跟踪和管理Bug',
                        'difficulty': 1,
                        'dimensions': [
                            ['生命周期与流转', '新建/分配/修复/验证/关闭', '重新打开/推迟/重复', '状态流转规则', '缺陷会议'],
                            ['属性与分类', '严重程度(Critical/Major/Minor)', '优先级(P0-P4)', '功能/界面/性能/安全等分类', '环境与版本信息'],
                            ['报告与描述', '复现步骤', '预期/实际结果', '附件与截图', '日志与崩溃信息'],
                            ['统计与度量', '缺陷密度', '收敛趋势', '千行代码缺陷率', '逃逸分析', '根因分析'],
                            ['工具与流程', 'Jira/Bugzilla/禅道', '模板与必填字段', '关联需求/用例', '回归验证', '缺陷关闭标准']
                        ]
                    },
                    'CI/CD集成': {
                        'desc': '将自动化测试集成到持续集成流程',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心概念', 'CI/CD持续集成/交付/部署', 'Pipeline流水线', 'Stage/Step', 'Agent/Node'],
                            ['触发与凭证', 'Webhook/定时/手动触发', '凭证管理(Credentials/Secret)', '环境变量', '分支策略与PR保护'],
                            ['构建与测试', 'Maven/Gradle/npm构建', '单元/集成/E2E测试集成', 'SonarQube代码分析', '测试报告与覆盖率'],
                            ['制品与部署', 'Docker镜像构建与推送', '蓝绿/金丝雀/滚动部署', 'Helm Chart', 'ArgoCD/GitOps'],
                            ['平台实践', 'Jenkins流水线(Groovy)', 'GitLab CI(.gitlab-ci.yml)', 'GitHub Actions', '通知(钉钉/企业微信/Slack)']
                        ]
                    },
                    'Cypress': {
                        'desc': '前端端到端测试框架，提供实时重载和调试功能',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与配置', '安装与项目结构', 'cypress.config配置', 'describe/it用例', '断言(expect/should)'],
                            ['定位与交互', 'get/contains/find定位', 'data-cy最佳实践', 'click/type/submit', 'hover/dblclick/select'],
                            ['等待与别名', '自动等待与超时配置', 'wait/wrap/its/invoke', 'alias别名与then', 'scrollIntoView'],
                            ['网络与fixture', 'intercept拦截与mock', 'fixture加载数据', 'request请求', 'stub与spy'],
                            ['运行与调试', 'cypress run/open', '时间旅行与快照', '截图与视频录制', '控制台日志'],
                            ['进阶与集成', '自定义命令', 'Page Objects', '组件测试(Vue/React)', 'CI/CD与Docker', '并行执行与报告']
                        ]
                    },
                    'JMeter': {
                        'desc': '性能测试工具，进行负载测试和压力测试',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础与计划', 'TestPlan/ThreadGroup', '线程数/Ramp-Up/循环', '调度器', 'GUI与命令行模式'],
                            ['Sampler与控制器', 'HTTP/JDBC/FTP请求', '逻辑控制器(If/While)', '事务控制器', '定时器(固定/随机/同步)'],
                            ['配置与变量', 'HTTP默认值/Header/Cookie管理', '用户变量/CSV数据配置', '函数(__time/__UUID/__V)', '正则/JSON提取器'],
                            ['断言与监听器', '响应断言', 'JSON/大小断言', '聚合报告/结果树', 'HTML报告Dashboard'],
                            ['分布式与监控', 'Master/Slave配置', '远程启动', 'JVM调优', 'Prometheus/Grafana集成'],
                            ['场景设计', '负载/压力/稳定性/容量测试', 'TPS/响应时间/百分位数', '错误率分析', '参数化与关联']
                        ]
                    },
                    'Playwright': {
                        'desc': '微软出品的现代Web测试框架，支持自动等待和并行执行',
                        'difficulty': 2,
                        'dimensions': [
                            ['配置与用例', 'playwright.config.ts', 'test.describe/test', 'expect断言(toHaveText/toBeVisible等)', 'skip/only/fixme'],
                            ['定位器与交互', 'getByRole/Text/Label/TestId', 'locator链式调用', 'click/fill/type/press', 'dragAndDrop/hover'],
                            ['页面与上下文', 'page.goto/waitForLoad', '多标签页与iframe', 'shadow DOM穿透', 'alert/dialog处理'],
                            ['网络与Mock', 'route拦截与mock', 'API测试(request)', 'fixture与storageState', '代理与头部修改'],
                            ['截图与追踪', 'screenshot/video录制', 'trace-viewer时间旅行', 'PDF生成', '错误与日志捕获'],
                            ['CI/CD与并行', 'GitHub Actions/Docker', '并行分片执行', '多浏览器(chromium/firefox/webkit)', 'reporter(allure/html)']
                        ]
                    },
                    'Selenium': {
                        'desc': 'Web应用自动化测试工具，支持多种浏览器和编程语言',
                        'difficulty': 2,
                        'dimensions': [
                            ['驱动与配置', 'WebDriver与各浏览器驱动', 'Options与Capabilities', 'headless模式', '窗口与导航'],
                            ['定位与元素', 'By.id/name/css/xpath', 'findElement/findElements', 'WebElement操作(click/sendKeys/getText)', '等待(隐式/显式/Fluent)'],
                            ['交互与高级操作', 'Actions(拖拽/悬停/右键)', 'JavaScript Executor', '弹窗与frame切换', '文件上传与下载'],
                            ['设计模式', 'Page Object模式', 'PageFactory', '关键字驱动', '数据驱动(Excel/CSV)'],
                            ['分布式与网格', 'Selenium Grid/Hub/Node', 'RemoteWebDriver', '并行执行(TestNG/JUnit)', '跨浏览器测试'],
                            ['监听与报告', 'WebDriverEventListener', 'Allure报告', '失败截图与重试', '日志(log4j)'],
                            ['CI/CD集成', 'Jenkins/GitLab CI', 'Docker部署', '框架分层(Page/Test/Utils)', '异常处理']
                        ]
                    },
                    '接口测试': {
                        'desc': '测试API的正确性、稳定性和性能',
                        'difficulty': 2,
                        'dimensions': [
                            ['协议与基础', 'HTTP/HTTPS方法', '请求/响应结构', '常见状态码', 'JSON/XML数据格式'],
                            ['认证与安全', 'Bearer Token/JWT', 'Basic/OAuth2', 'API Key', '签名与加密(MD5/AES)', 'CSRF/XSS/SQL注入防护'],
                            ['工具与自动化', 'Postman/Insomnia', 'curl命令行', 'Swagger/OpenAPI', 'Mock服务(WireMock)'],
                            ['脚本与变量', 'Pre-request/Tests脚本', '环境变量切换', '数据驱动(CSV/JSON)', '参数提取与关联'],
                            ['进阶与网关', 'GraphQL查询', '限流与重试', '幂等性测试', 'API网关(Kong/Gateway)', '性能测试(JMeter/k6)'],
                            ['CI/CD与文档', 'Newman/Jenkins集成', 'Swagger UI/ReDoc', '接口版本管理', 'Confluence文档']
                        ]
                    },
                    '自动化测试': {
                        'desc': '编写测试脚本实现回归测试自动化',
                        'difficulty': 2,
                        'dimensions': [
                            ['框架与分层', '测试金字塔(单元/接口/UI)', '框架选型(pytest/JUnit/Cypress)', 'Page Object/Screenplay模式', '数据驱动与关键字驱动'],
                            ['数据与环境', '测试数据准备与清理', 'CSV/Excel/JSON/Faker', '环境变量与配置', 'Docker/K8s环境隔离'],
                            ['执行与集成', '并行/分布式执行', 'CI/CD触发(提交/定时)', 'Jenkins Pipeline/GitHub Actions', '构建与部署自动化'],
                            ['报告与维护', 'Allure/ExtentReports', 'HTML/PDF报告', '失败重试与Flaky处理', '代码复用与设计模式'],
                            ['策略与流程', '冒烟/回归/功能/兼容性', '跨浏览器/跨平台', '代码评审', '测试计划与闭环']
                        ]
                    },
                    '性能测试': {
                        'desc': '识别系统瓶颈，测试并发处理能力和响应时间',
                        'difficulty': 3,
                        'dimensions': [
                            ['测试类型与指标', '负载/压力/稳定性/峰值测试', '响应时间(平均/P95/P99)', '吞吐量(TPS/QPS)', '错误率与可用性'],
                            ['工具与脚本', 'JMeter/k6/Locust', '场景设计与参数化', '用户模型与业务模型', '断言与监听器'],
                            ['资源监控', 'CPU/内存/磁盘IO/网络', 'JVM(GC/堆/线程)', '数据库连接池/缓存命中率', 'Prometheus/Grafana'],
                            ['分析与调优', 'APM(SkyWalking/Pinpoint)', '慢SQL与索引优化', '连接池与线程池调优', '缓存/异步/架构调整'],
                            ['报告与流程', '性能测试计划与方案', '场景执行与结果分析', '性能测试报告', '瓶颈定位与回归验证']
                        ]
                    }
                }
            }
        }
    }
}