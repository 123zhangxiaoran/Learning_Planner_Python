# 技能难度定义：1=基础入门，2=主流技术，3=进阶/专业
# 计算机专业数据 - 添加岗位描述和技能难度
computer_data = {
    '软件工程': {
        '测试工程师': {
            'description': '负责软件测试工作，编写测试用例，执行功能测试和性能测试。',
            'skills': {
                'JUnit': {
                    'desc': 'Java单元测试框架，支持TDD开发模式',
                    'difficulty': 1,
                    'dimensions': ['测试框架基础/注解@Test/@Before/@After/@BeforeClass/@AfterClass', '断言assertEquals/assertTrue/assertThat/异常测试expected/参数化测试@Parameterized', '测试套件TestSuite/Mockito模拟框架/@Mock/@Spy/@InjectMocks', 'BDD风格given-when-then/Mockito验证verify/when/ArgumentCaptor参数捕获', 'Spy监控/Stub存根/测试隔离/测试执行顺序/超时测试', 'groups分组/测试运行器Runner/规则Rule/理论Theory/测试监听器', 'Java单元测试/IntelliJ IDEA/Eclipse/Maven/Gradle集成/Jenkins集成/测试报告/HTML报告/TestNG对比']
                },
                'Postman': {
                    'desc': 'API接口测试工具，支持自动化测试集合和环境管理',
                    'difficulty': 1,
                    'dimensions': ['Collections集合/Environment环境变量/Globals全局变量', '请求方法GET/POST/PUT/PATCH/DELETE/Params参数', 'Headers请求头/Body参数JSON/form-data/x-www-form-urlencoded/raw/binary', '认证Authentication/Basic/Bearer/AWS/授权Authorization', 'Pre-request Script请求前脚本/Tests测试脚本', '变量{{variable}}/pm对象/pm.test/pm.expect/pm.request/pm.response', 'JSON/XML解析/数据驱动/CSV/JSON数据文件', '运行器Runner/循环迭代/增量运行/监控Monitors/定时任务', '自动化测试/Newman命令行/CI/CD集成/GitHub Actions/Jenkins/GitLab CI', '导出导入Collection/导入OpenAPI/Swagger/WSDL/代码生成', 'Mock Server模拟服务/代理Proxy设置/证书配置/SSL关闭', '请求超时/重试机制/Cookie管理/Sessions会话', 'WebSocket/Socket.IO/gRPC/GraphQL/SOAP/批量运行', 'Collection排序/Folder文件夹/脚本调试/console.log/断点调试']
                },
                'pytest': {
                    'desc': 'Python测试框架，功能强大且易于使用',
                    'difficulty': 1,
                    'dimensions': ['pytest安装/测试发现conftest.py/测试函数test_开头/测试类Test开头', '断言assert/assertEqual/assertTrue/assertIs/assertIn/自定义断言', '异常测试pytest.raises/警告捕获warnings', 'fixture装饰器@pytest.fixture/scope作用域/autouse自动使用', 'params参数化/ids用例ID/indirect参数间接传递/yield_fixture', 'setup/teardown/类级别/模块级别/session级别/conftest.py共享fixture', '标记marker@pytest.mark/skip/skipif条件跳过/xfail预期失败', 'parametrize参数化/多参数组合/mark推荐', 'pytest.ini配置/setup.cfg/pyproject.toml', '命令行参数-v/-s/-k/-m/-x/--tb/并行执行pytest-xdist/覆盖率pytest-cov', '输出报告/HTML报告pytest-html/日志输出/自定义插件/hook函数', 'Jenkins集成/GitHub Actions/CI/CD集成/Mock/Patch/unittest混合', 'fixture级联依赖/工厂fixture/临时目录tmp_path/tmpdir/monkeypatch/capsys/capfd', 'contextmanager/raises/warns/导入技巧/循环导入/测试隔离']
                },
                '测试用例设计': {
                    'desc': '等价类划分、边界值分析、场景法等测试设计方法',
                    'difficulty': 1,
                    'dimensions': ['等价类划分/有效等价类/无效等价类', '边界值分析/边界值/次边界值/外边界值', '场景法/基本流/备选流/异常流', '判定表法/条件桩/动作桩/条件组合/因果图', '正交试验法/因素水平/pairwise正交表', '错误推测法/经验推断/试探性思维', '路径测试/语句覆盖/分支覆盖/条件覆盖/判定覆盖/条件组合覆盖/路径覆盖/循环覆盖/MC/DC覆盖', '测试用例要素/用例ID/标题/优先级/前置条件/测试步骤/测试数据/预期结果/实际结果/用例状态', '用例评审/用例执行/用例跟踪/测试覆盖度/覆盖率统计', '需求追溯/双向追溯/测试计划/测试策略/测试范围/测试进度/测试资源/风险评估', '测试准出标准/测试报告/回归测试/冒烟测试', '功能测试/非功能测试/接口测试/性能测试/安全测试/兼容性测试/易用性测试/可靠性测试/可维护性测试/可移植性测试']
                },
                '缺陷管理': {
                    'desc': '使用Jira等工具跟踪和管理Bug',
                    'difficulty': 1,
                    'dimensions': ['Bug生命周期/新建New/确认Open/分配Assigned/修复Fixed/验证Verified/关闭Closed/重新打开Reopened/推迟Deferred/重复Duplicate/无法复现Cannot Reproduce/不是问题Not a Bug', '缺陷严重程度Critical/Major/Normal/Minor/Trivial', '缺陷优先级P0/P1/P2/P3/P4/紧急/高/中/低', '缺陷分类/功能错误/界面错误/性能问题/安全问题/易用性问题/需求问题/文档问题/代码缺陷/架构缺陷/设计缺陷', 'Jira使用/Bugzilla/禅道/Teambition/Tapd', '缺陷模板/必填字段/附件上传/截图标注/日志上传', '缺陷描述/复现步骤/预期结果/实际结果/环境信息/版本信息/设备信息/浏览器信息', '指派人员/抄送人员/相关需求/相关用例/相关代码', '影响分析/回归测试/缺陷评审/缺陷统计/缺陷趋势/缺陷密度', '千行代码缺陷率/缺陷收敛/缺陷地图/优先级判定/严重程度判定', '定级标准/修复成本/验证成本/沟通成本/回归成本', '缺陷关闭/缺陷打开/缺陷超时/缺陷遗漏/缺陷逃逸', '冒烟测试/单元测试/集成测试/系统测试/验收测试']
                },
                'CI/CD集成': {
                    'desc': '将自动化测试集成到持续集成流程',
                    'difficulty': 2,
                    'dimensions': ['持续集成CI/持续交付CD/持续部署CD/构建自动化/测试自动化/部署自动化', '流水线Pipeline/Jenkins流水线/声明式/脚本式', 'stage阶段/step步骤/agent代理/node节点/parameters参数', 'triggers触发器/cron定时/webhook/poll SCM/构建触发/构建参数', '凭证管理Credentials/secret/环境变量', '构建工具Maven/Gradle/npm/yarn/pnpm/Ant/MSBuild/CMake/Make', '版本管理Git/SVN/分支策略/主分支保护/代码审查/Pull Request', '构建结果/单元测试集成/集成测试/E2E测试/测试报告/覆盖率报告', '代码质量SonarQube/静态分析/代码风格/重复/复杂度/安全扫描/依赖扫描', '容器镜像Docker/镜像构建/推送/拉取/标签/版本/Harbor', '部署策略/蓝绿部署/金丝雀部署/滚动部署/回滚/人工确认/审批流程', '通知Email/钉钉/企业微信/Slack/飞书', 'GitLab CI/Runner/.gitlab-ci.yml/stages/before_script/script/after_script/artifacts/cache', 'dependencies/needs/rules/when/manual/always/on_failure/on_success', 'template/include/extends/variables/secrets/environment/protection', 'Kubernetes部署/Helm Chart/ArgoCD/GitOps/Terraform', '云原生/Serverless/AWS CodePipeline/Azure DevOps', 'GitHub Actions/workflow/runs-on/steps/uses/run/with/env/if/matrix', 'strategy/concurrency/timeout-minutes/secrets/permissions/触发条件', 'push/pull_request/schedule/workflow_dispatch/repository_dispatch']
                },
                'Cypress': {
                    'desc': '前端端到端测试框架，提供实时重载和调试功能',
                    'difficulty': 2,
                    'dimensions': ['Cypress安装/cypress.json配置/项目结构/cypress目录', '测试文件describe/it/测试套件/测试用例', '断言expect/should/assert/常用命令get/contains/find', 'CSS选择器/XPath/data-cy属性/data-testid', '交互命令type/click/submit/clear/check/uncheck/select/hover/右键dblclick', '滚动scroll-into-view/等待wait/自动等待/超时配置', 'alias别名as/then回调/each遍历/spread/wrap/its属性/invoke调用', 'window窗口/document/body/root', 'fixture加载/stub拦截/spy监控/Sinon.js/request请求/API测试', '网络拦截route路由/interception/fixtures数据/seed数据/环境变量', 'Cypress.env/CYPRESS_配置/baseUrl/viewport设置/响应式测试', '模拟设备/浏览器测试/多浏览器/并行测试', 'cypress run/cypress open/交互模式/时间穿梭/快照对比/测试重试', '失败截图/视频录制/控制台日志/网络日志', '组件测试cypress-component-testing/Vue/React/Angular/Svelte', 'Webpack配置/Vite配置/TypeScript支持/Page Objects', '自定义命令/commands.js/beforeEach/afterEach/skip/only', '调试debugger/console.log/日志输出/错误处理/异常捕获', 'CI/CD集成/Jenkins/GitHub Actions/GitLab CI/Docker/Cypress Docker镜像', '并行执行/负载均衡/报告生成/mochaawesome/Junit报告/覆盖率']
                },
                'JMeter': {
                    'desc': '性能测试工具，进行负载测试和压力测试',
                    'difficulty': 2,
                    'dimensions': ['JMeter安装/JDK要求/GUI模式/命令行模式/分布式测试', '测试计划TestPlan/线程组Thread Group/线程数Users/Ramp-Up时间/循环次数/永恒运行Forever/调度器Scheduler', 'Sampler采样器/HTTP请求/JDBC请求/FTP请求/SMTP请求/TCP请求/OS Process/Java请求', 'HTTP Request Defaults/HTTP Header Manager/HTTP Cookie Manager/HTTP Cache Manager/HTTP Authorization Manager', '用户定义的变量/CSV数据文件设置/配置元件/前置处理器/后置处理器', '正则表达式提取器/JSON Extractor/XPath Extractor/Boundary Extractor/CSS Selector Extractor/JSON JMESPath', '响应断言/断言持续时间/响应大小断言/JSON断言/XPath Assertion/SMIME Assertion', '监听器/查看结果树/聚合报告/Summary Report/Simple Data Writer/HTML报告/CSV结果', '并发用户/吞吐量Throughput/响应时间/延迟Latency/连接时间/错误率/标准差/中位数/90%95%99%/Percentiles', '事务控制器/循环控制器/IF控制器/While控制器/ForEach控制器/Switch控制器/Random Controller', 'Recording控制器/HTTP(S) Test Script Recorder/代理服务器/CA证书/抓包录制', '参数化/变量/函数__V/__P/__time/__random/__UUID/__split/__substring/__eval', '逻辑控制器/定时器/固定定时器/高斯随机定时器/Uniform Random Timer/Constant Throughput Timer/Synchronizing Timer', '关联Correlation/正则表达式/JSON提取/XPath提取/边界提取/模板/匹配数字/缺省值', 'JMeter函数/JMeter属性/JMeter变量/全局变量/局部变量', 'Cookie处理/Session处理/CSRF Token/单点登录/JWT认证/OAuth2', '分布式测试/Master配置/Slave配置/远程启动/RMI配置/防火墙/端口配置', '聚合报告分析/响应时间分析/吞吐量分析/错误分析/TPS计算', '性能测试计划/负载测试/压力测试/稳定性测试/容量测试/峰值测试/渐变测试/陡增测试', 'Dashboard/HTML报告/趋势分析/性能瓶颈', '监控集成Prometheus/Grafana/InfluxDB/JMX配置', 'JVM调优/GC调优/连接池/JDBC配置/HTTP配置/缓存配置']
                },
                'Playwright': {
                    'desc': '微软出品的现代Web测试框架，支持自动等待和并行执行',
                    'difficulty': 2,
                    'dimensions': ['Playwright安装/npm install playwright/浏览器安装/@playwright/test', '测试配置playwright.config.ts/baseURL/webServer/reporter/use', 'test.describe/test/it/test.before/beforeEach/afterEach/skip/only/fixme', 'expect断言/toBe/toEqual/toContain/toHaveCount/toHaveText/toHaveTitle/toHaveURL', 'toBeVisible/toBeHidden/toBeEnabled/toBeDisabled/toBeChecked/toBeSelected', 'locator定位器/page.locator/frame.locator/getByRole/getByText/getByLabel', 'getByPlaceholder/getByTestId/getByTitle/getByAltText/locator方法', 'click/dblclick/rightclick/hover/fill/clear/type/press/check/uncheck/selectOption/dragAndDrop', 'scrollIntoViewIfNeeded/screenshot截屏/video录制', 'page操作page.goto/reload/goBack/goForward/waitForURL/waitForLoadState', 'waitForSelector/waitForResponse/waitForRequest/waitForFunction/waitForTimeout', 'page.context/browser操作/apiRequest/fetch/请求拦截/响应拦截', 'route拦截/mock/stub/spy/Mock Modules', 'fixture固定装置/test.extend/storageState/headless/fullPage截屏', 'trace追踪/trace-viewer/压缩/报告/allure/html/json/junit', '并行执行/串行执行test.describe.serial/跨浏览器chromium/firefox/webkit', '多标签页/iframe嵌套/shadow DOM/组件测试', '定位策略CSS选择器/XPath/文本定位/ARIA角色/过滤条件', '网络请求API测试/REST API/GraphQL/请求体/响应体/状态码', 'viewport/windowSize/emulateDevice/Mobile/iPhone/Android', '性能指标LCP/FID/CLS/Core Web Vitals', '自定义命令/fixtures/page.addInitScript/serviceWorkers/通知/权限/地理位置/暗黑模式', 'PDF生成/截图对比/trace时间旅行/控制台日志/网络日志/错误捕获', '自动等待/智能等待/force点击/超时配置', 'CI/CD集成/GitHub Actions/Jenkins/GitLab CI/Docker/并行分片', 'TypeScript/JavaScript/Python/.NET/Java', '框架集成Vue/React/Svelte/Angular/Next.js/Nuxt/Remix/Astro/Vite']
                },
                'Selenium': {
                    'desc': 'Web应用自动化测试工具，支持多种浏览器和编程语言',
                    'difficulty': 2,
                    'dimensions': ['Selenium IDE/WebDriver/Selenium RC/Selenium Grid/Selenium 4.x新特性', '浏览器驱动ChromeDriver/FirefoxDriver/EdgeDriver/SafariDriver/IEDriverServer', 'WebDriver接口/RemoteWebDriver/Capabilities/Options', 'driver初始化get/navigate/back/forward/refresh/currentUrl/title/pageSource', 'window窗口switchTo/frame/alert/多窗口/locator定位器By.id/name/className/tagName/linkText/cssSelector/xpath', 'findElement/findElements/Actions操作click/contextClick/doubleClick/moveToElement/dragAndDrop/sendKeys/keyDown/keyUp/release', 'WebElement操作click/sendKeys/clear/submit/getText/getAttribute/getCssValue/getLocation/getSize/isDisplayed/isEnabled/isSelected', '截图screenshot/截取元素/executeScript/executeAsyncScript', 'implicitlyWait/setScriptTimeout/pageLoadTimeout/显式等待WebDriverWait/ExpectedCondition', '等待条件Timeout/Polling Interval/Fluent Wait流畅等待', 'JavaScript Executor/JavaScript点击/滚动/高亮/注入/jQuery支持', 'Cookie操作getCookies/getCookieNamed/addCookie/deleteCookie/deleteAllCookies', 'Options配置启动参数--headless/--no-sandbox/--disable-gpu/proxy/profile/extension', '下载路径/上传input[type=file]/文件上传', '处理弹窗alert/prompt/confirm/Actions拖拽/悬停/双击/右键/键盘Keys', '截图takeScreenshot/全屏截图/Base64编码/文件保存', 'Java/Python/JavaScript/断言assert/verify/softAssert/hardAssert', 'Test Report/Allure Report/日志log4j/logback/失败截图/失败重试', '并发执行Selenium Grid/Hub节点/RemoteWebDriver/分布式测试/跨浏览器测试', '并行测试/TestNG多线程/DataProvider数据驱动/Excel/CSV数据源', 'Page Object模式/PageFactory/Screenplay模式/关键字驱动/数据驱动/Hybrid混合', '框架设计封装/继承/多态/设计模式/单例/工厂/建造者/观察者/策略', 'Common层/Page层/Test层/Utils层/异常处理/自定义异常', '监听器WebDriverEventListener/EventFiringWebDriver/日志监听/截图监听', 'CI/CD集成Jenkins/GitLab CI/GitHub Actions/Docker/Swarm/Kubernetes']
                },
                '接口测试': {
                    'desc': '测试API的正确性、稳定性和性能',
                    'difficulty': 2,
                    'dimensions': ['HTTP/HTTPS/TCP/IP协议/OSI七层/TCP三次握手/四次挥手', 'HTTP方法GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS', '请求结构请求行请求头请求体/响应结构状态行响应头响应体', '状态码1xx/2xx/3xx/4xx/5xx/常见状态码', '请求头Content-Type/Accept/Authorization/Cookie/User-Agent/Host/Referer/Origin', '响应头Content-Type/Content-Length/Date/Server/Set-Cookie/Cache-Control', 'JSON数据格式/JSON语法/JSON.parse/JSON.stringify/JSON Schema验证', 'XML数据格式/语法/XPath/表单数据application/x-www-form-urlencoded/multipart/form-data', 'Query参数/Path参数/Header参数/Body参数/RESTful API/REST规范', 'GraphQL API/Query/Mutation/Subscription/字段选择/嵌套查询/别名/分页', 'API测试工具Postman/Insomnia/Paw/HTTPie/curl命令', '请求构造/发送请求/解析响应/断言验证', 'Swagger/OpenAPI/接口文档/接口版本v1/v2', 'Mock服务WireMock/Mockoon/JSON Server/faker.js', 'Charles Proxy/Fiddler/mitmproxy/抓包分析/代理设置/证书安装/HTTPS抓包', '接口自动化/自动化测试/数据驱动/参数化/CSV/Excel/数据库', '环境变量/环境切换dev/test/stage/prod/脚本逻辑', '加密解密MD5/SHA/AES/DES/RSA/Base64/签名sign/timestamp/nonce/token', '认证方式Bearer Token/Basic Auth/OAuth1.0/OAuth2.0/API Key/JWT/Session/Cookie', '接口安全XSS防护/CSRF防护/SQL注入/参数验证/权限验证/RBAC', '接口限流Rate Limit/429/重试机制/幂等性/并发测试', '性能测试JMeter/k6/Locust/Pytest/响应时间/TPS/QPS/并发用户', 'CI/CD集成Jenkins/GitHub Actions/GitLab CI', '接口文档管理Confluence/Wiki/Swagger UI/Redoc/Stoplight', '接口网关Kong/APISIX/Zuul/Spring Cloud Gateway']
                },
                '自动化测试': {
                    'desc': '编写测试脚本实现回归测试自动化',
                    'difficulty': 2,
                    'dimensions': ['自动化测试分层/单元自动化/接口自动化/UI自动化', '自动化测试金字塔/分层自动化/技术选型', '测试框架Python pytest/Java JUnit/TestNG/JavaScript Jest/Mocha', 'Cypress/Playwright/Selenium/Appium', '框架设计Page Object/Screenplay/关键字驱动/数据驱动/混合驱动', '测试数据/准备/清理/隔离/数据库/Mock/fixture', '测试环境搭建/配置/环境变量/配置文件/参数化', '数据源CSV/Excel/JSON/YAML/数据库/API/Faker/随机数据', '测试执行本地/远程/分布式/并行/CI/CD', 'Jenkins Pipeline/GitLab CI/GitHub Actions', '自动化构建/部署/测试/触发时机/代码提交/定时/手动/分支', '测试环境/预发布环境/生产环境/环境一致性/容器化', 'Docker/Kubernetes/隔离性/稳定性/可重复性', '测试报告/结果/覆盖率/Allure/ExtentReports/HTML/PDF', '邮件发送/通知/失败重试/Retry/Flaky/维护成本', '代码规范/命名/注释/分层设计/封装继承多态', '设计模式单例/工厂/建造者/策略/观察者', '代码复用/公共方法/基础类/工具类', '日志工具/数据库工具/文件工具/加密工具', '断言工具SoftAssert/BDD/Hamcrest/AssertJ/chai', '测试策略冒烟/回归/功能/非功能/性能/安全/兼容性', '跨浏览器/跨平台/版本兼容', '代码评审/测试评审/Design Review/Test Review', '测试计划/方案/用例/脚本/数据/环境/资源/进度/风险/里程碑', '测试交付物/总结/报告/质量评估/测试闭环']
                },
                '性能测试': {
                    'desc': '识别系统瓶颈，测试并发处理能力和响应时间',
                    'difficulty': 3,
                    'dimensions': ['性能测试类型/负载测试Load/压力测试Stress/容量测试/峰值测试/稳定性测试Endurance/陡增测试Spike/基准测试', '性能指标响应时间RT/平均/最大/最小/中位数/百分位数P50/P75/P90/P95/P99', '吞吐量TPS/QPS/RPS/HPS/并发用户/在线用户/活跃用户', '业务量DAU/MAU/PV/UV/转化率/GMV/订单量/下单成功率/支付成功率', '错误率Error Rate/成功率/失败率/可用性', '系统资源CPU/Memory/磁盘IO/网络IO/数据库连接/连接池', '缓存命中率/穿透率/JVM指标GC次数/GC时间/Full GC/Young GC/Old GC', '堆内存/非堆内存/线程数/死锁检测', '测试流程需求分析/确认/测试计划/方案/场景设计/脚本开发/执行/结果分析/调优/复测/报告', '测试工具JMeter/LoadRunner/k6/Locust/Gatling/Artillery/Apache Bench/wrk/Vegeta/siege/Tsung/NeoLoad', 'APM监控SkyWalking/Pinpoint/CAT/Zipkin/Jaeger/Prometheus/Grafana/ELK', 'JVM监控/GC监控/线程监控/内存监控/CPU监控', '数据库MySQL/PostgreSQL/Redis/MongoDB/缓存/消息队列Kafka/RabbitMQ', '服务器Linux监控top/vmstat/iostat/netstat/sar/nmon/zabbix', '性能测试报告/概要/环境/数据/场景/脚本/执行/结果/瓶颈/优化/结论', '性能调优代码/SQL/索引/缓存/异步/并发/架构/数据库/连接池/JVM/GC/参数/操作系统', '场景设计基准/负载/峰值/异常/数据量/并发量/思考时间/资源依赖', '测试模型用户模型/业务模型/数据模型/二八法则']
                }
            }
        },
        'DevOps工程师': {
            'description': '负责持续集成/持续部署，自动化运维和基础设施管理。',
            'skills': {
                'Python': {
                    'desc': '运维自动化和工具开发', 
                    'difficulty': 1, 
                    'dimensions': ['Python基础/数据类型/list/dict/set/tuple/控制流/循环/函数/类/继承/多态', '异常处理/try/except/finally/raise', '模块导入/包管理/pip/venv/virtualenv/conda/requirements.txt', '文件操作/open/read/write/CSV/JSON/XML', '路径处理/os.path/pathlib', '日期时间/datetime/time/calendar/时区/格式化', '正则表达式/re模块/match/search/findall/sub', '网络请求/requests库/HTTP请求/headers/认证', '并发编程/threading/multiprocessing/concurrent.futures/asyncio/async/await', 'subprocess/Popen/run/call/shell命令执行', 'paramiko/SSH连接/fabric远程执行/ansible API', '密码学/hashlib/AES/RSA/Base64/cryptography', '数据库/pymysql/sqlalchemy/psycopg2/asyncpg/Redis/MongoDB/ES', '日志/logging/日志级别/日志轮转/RotatingFileHandler', '配置管理/configparser/PyYAML/toml/.env', 'Docker SDK/docker-py/构建镜像/容器管理', 'Kubernetes客户端/kubernetes/API/资源管理', '告警通知/钉钉/飞书/企业微信/Webhook', '性能分析/cProfile/memory_profiler/pdb/ipdb', '单元测试/unittest/pytest/mock/coverage', '类型注解/typing/TypeVar/mypy', '代码规范/PEP8/Pylint/Flake8/black/isort', '打包分发/setup.py/pyproject.toml/wheel/twine', 'CLI工具/argparse/click/Typer/Fire', '数据处理/pandas/numpy/itertools/functools/collections', 'venv/pipenv/poetry/pyenv/版本管理', '自动化测试/pytest/CI/CD/GitHub Actions/Jenkins/GitLab CI', '定时任务/crontab/APScheduler/Celery', '进程管理/supervisor/systemd/daemon化/signal', 'Dockerfile/多阶段构建/镜像优化/ENTRYPOINT/WORKDIR', '性能优化/列表推导式/生成器表达式/循环优化', '最佳实践/模块化设计/代码复用/跨平台兼容']
                },
                'Ansible': {
                    'desc': '自动化运维工具，批量配置服务器', 
                    'difficulty': 2, 
                    'dimensions': ['Ansible安装/架构/控制节点/受控节点', 'SSH连接/无密钥认证/SSH密钥分发', 'inventory主机清单/静态/动态/主机组/变量', '主机模式/all/targeted/group/*', 'ad-hoc命令/ansible命令行/模块', '常用模块/ping/command/shell/script/raw/yum/apt', '系统模块/service/file/copy/template/lineinfile', '用户模块/user/group/cron/filesystem', '网络模块/mount/sysctl/firewalld/iptables', 'Docker模块/docker_container/image/login/config/stack', '数据库模块/mysql/postgresql', '信息模块/setup/debug/fail/pause/assert', '等待模块/wait_for/wait_for_connection', '其他模块/uri/get_url/unarchive/archive/git/svn', 'playbook剧本/YAML语法/hosts/remote_user/become', 'tasks任务列表/handlers处理器/notify触发', 'tags标签/vars变量/register注册', '条件when/循环loop/with_items/list/dict/fileglob/lines/nested', '重试until/retries/delay/ignore_errors', '检查模式/check_mode/diff_mode', 'roles角色/tasks/main.yml/handlers/vars/defaults/meta', 'ansible-galaxy/角色管理/init/install', 'ansible-vault/加密/解密/view/create/edit', 'tags执行/tagged/untagged/skip-tags/limit-tags', '执行策略/check/diff/step/start-at-task', '异步任务/async/poll/async_status', '并行执行/forks/serial/max_fail_percentage', '委托/delegate_to/local_action/run_once', 'include导入/include_tasks/import_playbook', 'lookup插件/file/pipe/env/passwordstore/redis/vault/csvfile', '动态清单/AWS EC2/Azure/GCP/VMware', 'Tower/AWX/Web界面/作业模板/工作流', 'ansible.cfg配置/inventory/privilege_escalation', 'fact收集/fact_caching/json_cache/redis_cache', 'callback回调/profile_roles/timer/profile_tasks', 'ansible-pull/拉取模式/push模式', '幂等性/changed_when/failed_when/断言检查', 'Jinja2模板/变量引用{{}}/条件循环/宏定义', '过滤器/ipaddr/json_query/flatten/unique/intersect/difference/union', '哈希/sha1/sha256/base64/yaml/json/uuid/regex', '自定义模块/模块开发/模块参数/文档', '最佳实践/模块化设计/测试验证/Molecule/CI集成']
                },
                'Docker': {
                    'desc': '容器化技术，实现应用快速部署和环境一致性', 
                    'difficulty': 2, 
                    'dimensions': ['Docker安装/Docker Engine/daemon/CLI/API', '镜像操作/pull/push/build/tag/rmi/save/load/inspect', 'Dockerfile指令/FROM/RUN/CMD/ENTRYPOINT/EXPOSE/ENV/ARG/LABEL/COPY/ADD/WORKDIR/USER/VOLUME/HEALTHCHECK', '多阶段构建/AS name/COPY --from/构建缓存', '镜像优化/减少层数/alpine/slim/distroless/scratch', '.dockerignore忽略文件', '容器操作/run/create/start/stop/restart/rm/ps/logs/exec/cp/attach', '容器参数/-i/-t/-d/--rm/--name/-e/-p/-v/--network/--privileged/--restart', '数据卷/volume类型/host/tmpfs/named/anonymous/数据持久化/数据备份', '网络模式/bridge/host/overlay/macvlan/none', 'network CLI/create/ls/rm/inspect/connect/disconnect', 'DNS服务发现/端口映射/NAT/跨主机通信', 'Docker Swarm/Manager/Worker/Node/Service/Task/Stack', 'Swarm命令/init/join/leave/service create/scale/update/rollback', '副本模式/全局模式/副本数replicas', '健康检查/liveness/readiness/startup探针', '滚动更新/蓝绿部署/金丝雀部署', 'Swarm密钥/Secret创建/更新/删除/使用', 'Swarm配置/Config创建/更新/删除/使用', 'Docker Compose/compose文件/up/down/ps/logs/build/pull/push/scale', 'compose配置/services/networks/volumes/secrets/configs/depends_on/ports', 'deploy配置/resources/limits/restart_policy/placement/constraints', 'Docker Registry/harbor私有仓库/harbor安装配置/用户管理/角色管理', '镜像安全/Clair/Trivy/镜像签名/cosign/漏洞扫描', '访问控制/RBAC/项目/仓库权限/LDAP/OIDC', 'Harbor replication/镜像复制/过滤规则/同步策略', '镜像清理/GC垃圾回收/保留策略', '构建加速/buildx/builder/manifest/多架构构建', '存储驱动/overlay2/aufs/devicemapper/btrfs/zfs', '资源限制/cpu/memory/IO/网络/PIDs/ulimits', '日志收集/ELK/Fluentd/json-file/syslog/journald', '容器监控/cAdvisor/Prometheus采集', '安全实践/非root/只读文件系统/seccomp/apparmor/selinux/capabilities', 'Docker Machine/云驱动/AWS/Azure/GCP', '最佳实践/镜像优化/安全加固']
                },
                'ELK Stack': {
                    'desc': 'Elasticsearch、Logstash、Kibana日志分析平台', 
                    'difficulty': 2, 
                    'dimensions': ['ELK架构/Elasticsearch/Logstash/Kibana/Beats/完整栈', 'ES安装/集群配置/节点类型/master/data/ingest/coordinating', '节点发现/Zen/EC2/Azure/GCP/K8s', '集群健康/green/yellow/red/集群统计/节点统计', '分片/shard/主分片/副本分片/分片路由/负载均衡', '索引index/索引创建/模板/别名/打开关闭/删除/刷新', '文档CRUD/index/get/update/delete/bulk/mget/msearch', '查询Query DSL/match/term/range/bool/must_not/should/filter', '聚合aggregations/metric聚合/bucket聚合/pipeline聚合', '聚合函数/avg/sum/min/max/count/stats/percentiles', 'bucket聚合/terms/range/histogram/date_histogram/nested/top_hits', 'pipeline聚合/cumulative_sum/moving_avg/derivative', 'mapping映射/text/keyword/date/boolean/ip/geo_point/nested/join', '分词analyzer/tokenizer/filter/char_filter/同义词/停用词', '分词器/standard/simple/whitespace/keyword/pattern/edge_ngram/ngram', '动态映射dynamic mapping/runtime field', 'painless脚本/脚本执行/脚本参数/脚本缓存', 'scroll/search_after/PIT时间点', 'ILM索引生命周期/hot/warm/cold/delete', 'ILM操作/rollover/shrink/forcemerge/freeze', '高亮highlight/fvh/plain/unified', '跨集群搜索CCS/CCR跨集群复制/快照snapshot', 'snapshot仓库/fs/s3/hdfs/gcs/azure', '集群安全/X-Pack/Security/LDAP/AD/SAML/OIDC/PKI', '角色权限/field level/document level/审计日志', 'Watch监控/watcher/input/schedule/condition/action', '告警通知/Email/Slack/钉钉/webhook/PagerDuty/Jira', 'Logstash配置/pipeline/input/filter/output', 'input插件/beats/file/syslog/tcp/http/jdbc/kafka/redis', 'filter插件/grok/date/mutate/ruby/geoip/useragent/dns', 'filter操作/clone/drop/sleep/throttle/fingerprint/json/csv/xml', 'output输出/elasticsearch/stdout/file/kafka/redis/s3/jdbc', 'pipeline队列/DLQ死信队列/重试机制/backpressure', 'Logstash条件/if/and/or/not/regex/表达式', '插件开发/Ruby/filter/input/output/codec', 'Kibana配置/kibana.yml/elasticsearch.hosts/TLS/空间spaces', 'Kibana界面/Dashboard/Explore/Visualize/Alerting/Machine Learning/APM', 'index pattern索引模式/字段映射/字段格式/format', '图表类型/Graph/Stat/Gauge/Table/Pie/Heatmap/TimeSeries/Logs', '告警规则/阈值/ES query/inventory/metrics/uptime/logs', '告警动作/Email/webhook/Slack/Jira/ServiceNow/钉钉/企业微信', 'APM配置/Java/Python/Node.js/Go/.NET/PHP/Ruby Agent', 'APM指标/transaction/trace/span/error/service map/service graph', 'Machine Learning/异常检测/anomaly job/detector/influencer', 'ML功能/forecast/regression/classification/outlier_detection', 'Maps地图/tile layer/region map/heatmap/geo_shape/geo_point', 'Uptime监控/HTTP/TCP/ICMP/Browser/TLS monitor', '证书监控/可用性/宕机/downtime', 'Logs日志/log stream/log filters/log query', 'Beats集成/Filebeat/Metricbeat/Heartbeat/Packetbeat/Auditbeat', '集成模块/nginx/apache/mysql/postgresql/mongodb/redis/kafka/docker/k8s', 'beats安全/TLS/认证/加密/与ES连接', 'Stack Management/索引管理/模板/生命周期/恢复/分片', 'Kibana高级配置/reporting/PDF/CSV/theming/dark/light/language']
                },
                'GitHub Actions': {
                    'desc': 'GitHub的自动化工作流平台', 
                    'difficulty': 2, 
                    'dimensions': ['workflow工作流/workflow定义/触发器', 'runners/Ubuntu/Windows/macOS/self-hosted/runner管理', '触发器/push/pull_request/schedule/workflow_dispatch/repository_dispatch', '触发过滤/branches/tags/paths/workflow_filter', 'cron表达式/minute/hour/day-of-month/month/day-of-week', 'steps步骤/run/uses/with/env/if/timeout/id', 'uses动作/actions/checkout/setup-node/setup-python/setup-java/setup-go', 'uses动作/cache/upload-artifact/download-artifact/create-release', 'secrets密钥/secret创建/secret使用/secret加密', '环境变量/env/env定义/env引用/defaults', 'concurrency并发/group/cancel-in-progress', 'jobs作业/job/id/needs/runs-on/strategy', 'runs-on/操作系统/标签/自托管/组', 'matrix矩阵/include/exclude/fail-fast/continue-on-error', 'permissions权限/actions/contents/deployments/issues/packages', 'inputs输入/name/required/default/type', 'checkout操作/fetch-depth/lfs/clean/submodules/sparse-checkout', 'OIDC认证/AWS/Azure/GCP/OIDC信任', '预定义变量/github.event_name/sha/ref/repository/run_id', 'if表达式/success/failure/cancelled/always/never', 'needs依赖/needs状态/needs.outputs/job.status', 'context上下文/steps.context/needs.context/matrix.context/github.context', '矩阵组合/matrix组合/并行执行/依赖关系', 'services服务/Redis/PostgreSQL/MySQL/MongoDB/MariaDB', '容器container/image/ports/volumes/credentials', '缓存actions/cache/缓存键/路径/restore-keys', '产物artifact/upload-artifact/download-artifact/retention-days', 'release发布/create-release/tag/draft/prerelease/merge/squash', '标签tag/tag创建/tag推送/tag保护', '语义版本/semantic versioning/版本号/major/minor/patch', 'workflow_call/workflow_dispatch/reusable workflow/子工作流', 'action市场/action发现/action创建/action开发/action打包', '认证配置/github_token/token权限/GITHUB_TOKEN', '环境environments/environment配置/保护规则/审查者/定时器', '变量variables/variables创建/variables使用/variables组织', 'Runner安全/安全策略/安全审计/安全监控', 'CI/CD设计/代码检查/lint/format/单元测试/测试覆盖/安全扫描', '监控集成/Prometheus/Grafana/ELK/CloudWatch', '通知集成/Email/Slack/钉钉/Teams/webhook/飞书', '状态检查/构建状态/PR状态/required status checks', '云配置/AWS/Azure/GCP/阿里云/华为云/腾讯云', '产物策略/产物上传/产物下载/产物清理/产物保留', '版本控制/版本标签/自动版本/changelog/release notes', '最佳实践/工作流设计/变量设计/矩阵设计/缓存设计']
                },
                'GitLab CI': {
                    'desc': 'GitLab内置的持续集成工具', 
                    'difficulty': 2, 
                    'dimensions': ['GitLab CI/CD概述/CI/CD/持续集成/持续交付/持续部署', 'pipeline流水线/stage阶段/job作业/配置/脚本/依赖/触发', 'stages阶段/定义/配置/顺序/名称', 'scripts脚本/before_script/after_script/script', 'timeout超时/retry重试/retry次数/条件', 'when何时/always/never/on_failure/on_success/manual/delayed', '触发器/pipeline触发/git推送/merge_request/schedules/trigger/webhook/API', 'include包含/project/模板/文件/远程/本地/URL/refs', 'extends继承/override/override', 'variables变量/类型/值/描述/可见性/保护/环境/作用域', '预定义变量/GITLAB_USER_*/CI_PIPELINE_*/CI_COMMIT_*/CI_PROJECT_*/CI_JOB_*', 'Runner执行器/shell/docker/kubernetes/ssh/VM/AWS/Azure/GCP', 'Runner管理/安装/注册/标签/限制/并发/锁定/状态/组/权限', 'Runner标签/tags匹配/约束/限制/only/except', 'rules规则/条件/允许/拒绝/变量/脚本', 'cache缓存/键/路径/策略/分享/依赖/恢复/保存/失效', 'artifacts工件/路径/名称/类型/策略/过期/报告/依赖/分享/下载', 'reports报告/junit/cobertura/clover/lcov/coverage/codequality/sast', 'dependencies依赖/配置/作业/继承/排除/限制', 'needs需求/配置/作业/继承/排除/限制/状态/结果/工 件', 'trigger触发器/配置/规则/作业/管道/项目/分支/标签/令牌/API', 'bridge桥接/作业/管道/项目/触发/配置/规则/设置/状态/依赖/工件/输出/变量', '最佳实践/pipeline设计/模块化/重用/测试']
                },
                'Grafana': {
                    'desc': '数据可视化和监控仪表板', 
                    'difficulty': 2, 
                    'dimensions': ['Grafana安装配置/默认端口3000', '界面导航/Dashboard/Explore/Alerting/Plugins', '数据源DataSource/Prometheus/Loki/Elasticsearch/InfluxDB/MySQL/PostgreSQL/Azure', 'Query查询/PromQL/LogQL/SQL/Metrics/Logs/Traces', '变量Variables/Custom/Constant/DataSource/Interval/Query/TextBox/MultiSelect/Repeat', 'Dashboard仪表板/创建/编辑/导出/导入/分享/权限/文件夹/JSON配置', '面板Panel/Graph/Stat/Gauge/Table/Text/PieChart/Heatmap/TimeSeries/Logs', '图表配置/Legend/Thresholds/DataLinks/Annotations/SeriesOverrides', '告警Alerting/Alert规则/ContactPoints/NotificationPolicies/Routes/Grouping/Timing', '告警条件/Classic条件/Reduce/Math/Threshold/Resample/Evaluate/For/Pending', 'Contact Points/Email/Slack/Pagerduty/OpsGenie/DingTalk/WeChat/Webhook/Telegram', '告警模板/AlertTemplating/模板语法/labels/values/CommonLabels', '表达式Expressions/Reduce减少/Math数学/Threshold阈值/Resample/OrganizeFields', '插件Plugin/安装/管理/市场/Panel插件/Datasource插件/App插件', 'API/GrafanaAPI/认证/APIKey/BearerToken/端点/DashboardAPI/FolderAPI', 'Provisioning配置/配置供应/DashboardProvision/DatasourceProvision/AlertingProvision', '配置管理/Database/MySQL/PostgreSQL/SQLite/安全性/OAuth/LDAP/SAML/日志', 'Grafana Cloud/GrafanaCloud托管/Prometheus/Loki/Tempo/Graphite/InfluxDB', 'Explore探索/Logs日志/Traces追踪/Split分割/Filter过滤/Parser/Dedup', '用户管理/组织Org/用户邀请/角色权限/Admin/Editor/Viewer', '认证集成/LDAP/SAML/OAuth/GitHub/GitLab/Google/AzureAD/Okta/匿名访问', '主题设置/Dark/Light/时区/日期格式/语言/本地时间/UTC', '快照Snapshot/创建/分享/导出/导入/删除', '团队协作/权限管理/Dashboard分享/LibraryPanels/Report报告', '最佳实践/仪表板设计/查询优化/告警优化/性能优化']
                },
                'Helm': {
                    'desc': 'Kubernetes包管理工具，简化应用部署', 
                    'difficulty': 2, 
                    'dimensions': ['Helm安装/Helm3架构/client端/Tiller移除', 'Chart包/templates/values.yaml/Chart.yaml/charts依赖', 'Helm命令/install/upgrade/rollback/uninstall/list/history/status/get', '仓库Repository/repo add/update/remove/list/search/pull', 'Chart开发/create/package/lint/test/template', '模板语法/Go template/values引用/流程控制/functions/filters/命名模板', 'values配置/--set/--set-file/--set-string/环境变量', 'Release管理/版本记录/回滚/升级/多版本共存', 'Hooks钩子/pre-install/post-install/pre-upgrade/post-upgrade/hook-weight/delete-policy', '依赖管理/Chart依赖/requirements.yaml/子Chart', '安全策略/RBAC/权限控制/安全上下文', '插件Plugins/helm plugin install/list/uninstall/update/helm-secrets/helm-diff', 'CI/CD集成/Jenkins/GitHubActions/GitLabCI/ArgoCD/Flux', '版本控制/SemVer语义化/版本范围/版本比较', 'Chart仓库/Helm Hub/私有仓库/ChartMuseum/Harbor', '推送拉取/helm push/pull', '自定义资源/CRD/自定义资源定义/Operator模式', '测试Chart/helm test/测试框架', '调试/helm get manifest/template/--debug', 'lint检查/yaml语法/模板检查/值验证', 'Kustomize集成/kustomize overlay', '命名空间/Namespace/跨命名空间', '资源配置/limit/request/cpu/memory/存储', '服务账户/ServiceAccount/RBAC角色/ClusterRole', '健康检查/探针配置/liveness/readiness/startup探针', '持久化存储/PVC/StorageClass/持久卷挂载', '数据卷/emptyDir/hostPath/configMap/Secret', 'ingress配置/ingressClass/annotations/TLS/路径路由', '服务类型/ClusterIP/NodePort/LoadBalancer/ExternalIP', '部署策略/rollingUpdate/recreate', 'HPA配置/水平自动扩缩容/metrics/自定义指标', 'Pod策略/PodDisruptionBudget/priorityClass', '安全上下文/runAsUser/runAsGroup/fsGroup/selinux', '网络策略/NetworkPolicy/入站出站规则', '服务账号/ServiceAccount/ImagePullSecrets', '镜像配置/repository/tag/pullPolicy/imagePullPolicy', 'init容器/initContainers', 'sidecar容器/辅助容器/日志收集/代理', '多容器Pod/共享Volume/共享网络', '污点容忍/Taints/Tolerations/节点亲和性/反亲和性', '最佳实践/版本管理/测试流程/安全扫描/Chart审核']
                },
                'Jenkins': {
                    'desc': '开源CI/CD工具，自动化构建、测试和部署', 
                    'difficulty': 2, 
                    'dimensions': ['Jenkins安装/Tomcat/Docker/二进制/Java环境', 'Jenkins配置/插件管理/系统配置/全局配置/目录配置', 'Job项目/自由风格/管道/多配置/文件夹', 'Job配置/源码管理/Git/SVN/构建触发器/构建步骤', '构建触发/定时/Poll SCM/Webhook/GitHook/远程/条件', 'Pipeline/声明式/脚本式/stage/step/agent', 'Pipeline语法/Jenkinsfile/groovy/options/triggers/parameters', 'Pipeline进阶/parallel/matrix/when/environment/credentials', '分布式构建/Agent/Node/Label/执行器', 'Agent配置/SSH/Windows/Docker/Kubernetes/VM', 'Credentials/UsernamePassword/SSH/SecretText/API Key', '权限管理/RBAC/角色/Users/矩阵权限', '插件生态/插件市场/Git/Blue Ocean/Pipeline/Kubernetes/Docker/Slack/钉钉', '构建工具/Maven/Gradle/npm/yarn/ant/MSBuild/CMake/Make', '单元测试/JUnit/TestNG/Pytest/JavaScript', '代码质量/SonarQube/PMD/Checkstyle/Fortify/代码扫描', '覆盖率/Cobertura/Jacoco/Istanbul/HTML报告', '安全扫描/OWASP/ZAP/Snyk/漏洞扫描', '构件管理/Artifact/Nexus/Artifactory/归档/推送', '通知集成/Email/Slack/钉钉/企业微信/PagerDuty', '参数化构建/字符串/布尔/选择/文件参数', '环境变量/系统变量/构建变量/变量注入', 'Blue Ocean/可视化Pipeline/图形化界面', 'Jenkinsfile/版本控制/Pipeline as Code', '构建记录/控制台输出/工作空间/工件', '日志分析/调试模式/错误定位', '超时配置/重试机制', '并行执行/Parallel/多分支/阶段并行', '矩阵构建/axis/控件/组合/配置切片', 'GitHub集成/Webhook/Pull Request/分支状态', 'GitLab集成/Webhook/Merge Request', 'Jira集成/问题关联/状态同步', 'Docker集成/镜像构建/容器测试/镜像推送', 'Kubernetes集成/动态Agent/命名空间', 'Terraform集成/基础设施代码/plan/apply', 'Ansible集成/playbook执行/清单管理', '认证配置/LDAP/ActiveDirectory/SAML/OAuth', '端口配置/反向代理/Nginx/HTTPS', '备份恢复/配置备份/数据迁移', '性能调优/JVM配置/内存/线程/GC调优', '监控集成/Prometheus/Grafana', '最佳实践/Pipeline设计/模块化/测试/部署策略']
                },
                'Kubernetes': {
                    'desc': '容器编排平台，管理大规模容器集群的部署和扩展', 
                    'difficulty': 2, 
                    'dimensions': ['K8s架构/Master/Node/etcd/APIServer/Controller/Scheduler/Kubelet/Kube-proxy', '核心概念/Pod/Service/Ingress/Deployment/StatefulSet/DaemonSet/Job/CronJob', '命名空间/Namespace/资源隔离/多租户', 'Pod管理/创建/删除/扩缩容/重启策略/健康检查/调度', 'Pod配置/探针配置/initContainers/容器资源限制', '多容器Pod/sharedVolume/共享网络/sidecar模式', 'Service服务/ClusterIP/NodePort/LoadBalancer/ExternalIP/headless', 'Ingress/ingressController/annotations/TLS/路径路由/域名/SSL证书', 'Deployment/部署策略/滚动更新/回滚/replicaSet/扩缩容', 'StatefulSet/有状态部署/持久存储/稳定主机名/稳定存储', 'ConfigMap/Secret/配置管理/环境变量/挂载/加密配置', 'PV/PVC/存储管理/StorageClass/动态供应/持久卷', '网络模型/CNI/Service/DNS/ClusterIP/NodePort/LoadBalancer', '网络策略/NetworkPolicy/入站/出站/命名空间隔离', '调度机制/Scheduler/节点选择/亲和性/反亲和性/污点容忍', '污点Taints/容忍Tolerations/节点亲和性/标签选择器', 'HPA/水平自动扩缩容/VPA/自定义指标', 'RBAC/Role/ClusterRole/RoleBinding/ClusterRoleBinding/ServiceAccount', '资源配额/ResourceQuota/limitRange/请求/限制/cpu/memory', 'QoS服务等级/Guaranteed/Burstable/BestEffort/优先级', 'Helm部署/Chart包/values.yaml/install/upgrade/rollback', '运维操作/kubectl get/describe/apply/delete/logs/exec/port-forward', '集群升级/滚动升级/备份恢复/版本迁移', '监控集成/Prometheus Operator/metrics-server/Grafana', '日志管理/ELK集成/Fluentd/Loki/日志收集', '安全策略/PodSecurityPolicy/networkPolicy/RBAC', 'Pod调度/污点/容忍/优先级/抢占/拓扑分布', '多集群管理/kubeconfig/联邦/Federation/多集群通信', 'Operator模式/CRD/自定义控制器/Operator SDK', '服务网格/Istio/Linkerd/流量管理/mTLS', '存储类型/emptyDir/hostPath/NFS/GlusterFS/Ceph/云存储', '云原生存储/Longhorn/Rook/Cinder/EBS/AzureDisk', 'CI/CD集成/Jenkins X/ArgoCD/Flux/GitOps', '最佳实践/资源规划/监控告警/日志/安全/高可用']
                },
                'Nginx': {
                    'desc': 'Web服务器和反向代理配置', 
                    'difficulty': 2, 
                    'dimensions': ['Nginx安装/Yum/APT/源码编译/Docker', '核心配置/nginx.conf/worker进程/error_log', '基本配置/server/location/listen/server_name/root', 'location匹配/精确/前缀/正则/优先级/rewrite', '反向代理/proxy_pass/upstream/负载均衡/健康检查', '负载均衡/roundrobin/ip_hash/least_conn/weight/fair', '缓存配置/proxy_cache/proxy_cache_path', 'SSL/TLS/HTTPS证书/私钥/TLS版本', 'HTTP/2/ALPN/协议优化', '安全配置/headers/CORS/referer/IP限制', '限流配置/limit_req/limit_conn/rate/突发', '日志配置/access_log/error_log/JSON日志', 'Gzip压缩/gzip_types/压缩比', '静态资源/缓存/防盗链/autoindex', '日志切割/logrotate', '反向代理进阶/WebSocket/X-Real-IP/X-Forwarded', 'FastCGI/php-fpm/uwsgi/Node', '动静分离/静态分离/动态请求', '高可用/keepalived/VRRP/双机热备', '性能优化/worker数/cpu亲和/连接复用', '健康检查/主动/被动/阈值', 'Lua扩展/ngx_lua/openresty', 'stream模块/TCP代理/UDP代理/四层负载', '安全头/X-Frame-Options/CSP/HSTS/X-Content-Type', '重定向/301/302/redirect', '防盗链/valid_referers', 'IP访问控制/allow/deny/白名单/黑名单', '请求限制/limit_rate/连接限制', '监控集成/status模块/Prometheus', '错误页面/error_page/自定义错误', '容器化/Docker/docker-compose', '进程管理/reload/reopen/upgrade/信号', '调试排错/error_log级别/debug模式', '最佳实践/配置模块化/安全加固/性能调优']
                },
                'Prometheus': {
                    'desc': '监控系统和时间序列数据库', 
                    'difficulty': 2, 
                    'dimensions': ['Prometheus架构/Server/Pushgateway/Exporters/Alertmanager', '安装部署/二进制/Docker/Kubernetes/systemd', '配置prometheus.yml/targets/scrape_interval/metrics_path', '数据模型/指标名称/标签/时间戳/样本', '指标类型/Counter/Gauge/Histogram/Summary', 'PromQL查询/聚合操作/范围查询/子查询', 'PromQL函数/rate/increase/histogram_quantile/label_replace', '聚合/sum/avg/min/max/count/stddev/by/without', '范围向量/时间范围/offset/@时间锚点', 'Recording Rules/预聚合规则/规则文件', '告警规则/groups/alert/expr/for/labels/annotations', 'Alertmanager配置/告警路由/receivers/抑制/静默', '告警渠道/Email/Slack/钉钉/企业微信/Webhook/PagerDuty', '告警分组/group_wait/group_interval/repeat_interval', '告警模板/模板语法/labels/annotations', 'Exporters/Node/MySQL/Redis/Postgres/JMX/Blackbox', 'Exporter开发/Go/Java/Python/Ruby/自定义指标', '服务发现/consul/DNS/file/kubernetes/EC2/云发现', '服务发现配置/标签过滤/元数据/角色', '远程存储/Remote Write/Remote Read/InfluxDB/Thanos', '联邦集群/Federation/跨集群/HA高可用', '可视化/Grafana集成/Dashboard/Explore', 'Recording Rules/预聚合/性能优化', 'Grafana集成/Dashboard/仪表板', 'Grafana数据源/配置/查询/告警', '监控自身/自监控/资源使用', 'K8s集成/Prometheus Operator/ServiceMonitor/PodMonitor', 'CRD资源/ServiceMonitor/PodMonitor/PrometheusRule', 'Alertmanager集群/HA/副本/一致性', '静默规则/Silence/匹配器', '抑制规则/Inhibit/源告警/目标告警', '最佳实践/命名规范/标签设计/查询优化/告警优化']
                },
                'Terraform': {
                    'desc': '基础设施即代码工具，自动化云资源管理', 
                    'difficulty': 2, 
                    'dimensions': ['Terraform安装/版本管理/provider插件/阿里云/AWS/Azure/GCP', '配置语法/HCL/resource/dataSource/variable/output/module', '资源管理/创建/更新/删除/依赖/引用/生命周期', '变量Variables/输入/输出/局部变量/数据类型', '变量定义/type/default/validation/sensitive', 'Provider配置/provider/alias/version', '状态管理/State/本地/远程后端/S3/锁定', '状态锁定/DynamoDB/Redis/并发控制', '工作空间/Workspace/开发/测试/生产/隔离', '模块Module/模块调用/模块复用/输入输出', '数据源Data/查询/远程状态/外部数据', 'Provisioner/local-exec/remote-exec/file', '资源图谱/Dependency Graph/执行计划', '命令行/init/plan/apply/destroy/show/state/output', '命令行进阶/import/refresh/taint/untaint/fmt/validate', '循环结构/count/for_each/dynamic/for', '条件表达式/三元表达式', '函数/内置函数/string/numeric/collection/encoding', '文件函数/file/fileexists/templatefile/path', '状态操作/state list/mv/rm/pull/push', '后端配置/local/s3/azurerm/gcs', '多云部署/多Provider/资源映射', '远程状态/Remote State/状态共享', '团队协作/分支策略/代码审查/状态隔离', '模块市场/Module Registry/公共模块/私有模块', '安全实践/密钥管理/敏感变量/加密存储', 'CI/CD集成/Jenkins/GitHubActions/GitLabCI/Atlantis', '测试框架/Terraform Test/Terratest/mock', '导入现有资源/import/导入ID/状态管理', '调试配置/TF_LOG/调试日志', '变量文件/terraform.tfvars/*.auto.tfvars', '输出管理/output/sensitive', '资源依赖/depends_on/隐式依赖/显式依赖', '生命周期/create_before_destroy/prevent_destroy', '生命周期进阶/ignore_changes/replace_triggered_by', 'drifts检测/配置漂移/状态对比', 'Atlantis集成/自动plan/自动apply/PR评论', '政策即代码/OPA/Sentinel', 'IaC安全/扫描工具/tfsec/Checkov', 'Provisioner连接/connection/bastion/SSH/WinRM', 'Docker集成/Docker Provider/镜像构建', 'Kubernetes集成/K8s Provider/Helm Provider', 'Vault集成/Vault Provider/动态凭证', '最佳实践/模块化/变量验证/状态管理']
                },
                'Linux': {
                    'desc': '服务器操作系统管理和命令行操作',
                    'difficulty': 3,
                    'dimensions': ['Linux发行版/CentOS/Ubuntu/Debian/RedHat/系统选择', '文件系统结构/根目录/bin/etc/usr/var/home/目录结构', '文件命令ls/cd/mkdir/rm/cp/mv/find/locate/xargs/ln', '文本处理cat/head/tail/grep/sed/awk/wc/sort/uniq/tr/cut/column', '管道重定向>/>>/</dev/null/2>/1/&/&&/||', '用户权限chmod/chown/useradd/usermod/passwd/sudo/su', '进程管理ps/top/pstree/pgrep/pkill/kill/nohup/bg/fg', '网络命令ifconfig/ip/netstat/ss/ping/traceroute/mtr/curl/wget/nslookup/dig', '磁盘管理df/du/fdisk/mkfs/mount/umount/lsblk/blkid', '压缩解压tar/gzip/zip/unzip/bzip2/xz/7z', '系统服务systemctl/service/init.d/systemd/target', 'SSH远程连接密钥登录/ssh-copy-id/SSH配置/ProxyJump', 'vim/nano编辑器配置/宏/搜索替换', 'shell基础bash/zsh/fish环境配置', '环境变量PATH/ENV/export/set/declare/local/作用域', '软件包管理yum/apt/dnf/zypper/pacman/apk', '定时任务cron/crontab/anacron/at/batch', '日志管理journalctl/rsyslog/日志轮转/logrotate', '内存free/top/vmstat/pmap', 'CPUtop/htop/atop/uptime/lscpu', '磁盘IOiostat/iotop/pidstat', '网络配置ip/ifconfig/网卡/路由表/gateway', '防火墙iptables/firewalld/ufw/nft', 'DNS配置/etc/hosts/resolv.conf', '主机名配置hostname/etc/hostname', 'screen/tmux会话管理', '正则表达式基础', 'find/grep/sed高级用法', 'awk高级编程', 'Shell函数定义/参数传递/返回值', '条件判断if/case', '循环for/while/until/select', '脚本调试set-x/set-e/trap/DEBUG', '管道与子shell', '进程间通信', '信号处理', '守护进程', 'selinux/AppArmor', '系统监控prometheus/node_exporter', '性能分析perf/strace/ltrace', '内核参数调优sysctl', '资源限制ulimit', '系统日志审计auditd']
                },
                'Shell脚本': {
                    'desc': '自动化运维脚本编写',
                    'difficulty': 3,
                    'dimensions': ['Shell脚本基础/首行#!/bin/bash/执行方式', '变量定义/字符串/数组/关联数组/环境变量/位置参数', '变量替换${var}/${var:-default}/${var:=default}/${var:?error}', '数据类型/整数/字符串/浮点数/文件', '算术运算(())/let/expr/bc/awk', '比较运算-eq/-ne/-lt/-le/-gt/-ge/==/!=', '字符串比较/==/!=/-z/-n/=~/正则', '文件测试-r/-w/-x/-f/-d/-L/-s', '条件语句if/then/elif/else/fi单双括号', 'case语句模式匹配', '循环for/in/do/done/while/do/done/until/do/done', 'C风格for((i=0;i<n;i++))', '循环控制break/continue/continue[n]', '函数定义function name()/name()参数$@/$*/$#/$?/$!', '函数返回值return/echo/exit', '局部变量local', '递归函数', '数组操作/定义/访问/切片/长度/遍历', '关联数组declare -A', '字符串操作/长度/截取/替换/删除/大小写', '读取输入read/-p/-t/-s', '命令行参数getopts/getopt/case', '参数展开~/`command`/$()/${var:-}/${var:=}/${var:?}', '进程替换<(cmd)/(cmd>)', '信号与trap/DEBUG/EXIT/ERR', '调试选项set -x/-e/-u/-n/-v', 'shellcheck静态检查', '管道与命令组合/tee/stderr', 'xargs参数替换', 'parallel并发执行', 'expect自动交互', 'here document/<<EOF', 'here string/<<<', '临时文件mktemp', '重定向高级/exec/FD', '日志记录logger', '错误处理set -o pipefail', '安全脚本/输入验证/sanitize', '常用命令seq/yes/no/shuf/fold/column', '正则表达式grep/sed/awk/perl', 'sed高级编辑/a/i/c/d/p/q/r/w/y', 'awk高级编程/BEGIN/END/FS/OFS/RS/ORS/NR/FNR', 'awk条件与循环/函数/数组/正则', 'awk关联数组/sort/asort', 'shell脚本模板', '脚本优化技巧', '批量操作/并发/队列', '日志分析脚本', '系统巡检脚本', '备份脚本', '自动化部署脚本', '监控告警脚本', 'CI/CD脚本集成']
                },
                '云原生': {
                    'desc': '理解云原生架构和12要素应用',
                    'difficulty': 3,
                    'dimensions': ['云原生概念/Cloud Native/定义/核心理念', '云原生技术栈/容器/微服务/声明式API/不可变基础设施', '12-Factor App/IaaS/PaaS/SaaS', '12要素编码基准/codebase/依赖/配置/后端服务/构建发布运行/进程/端口绑定/并发/易处理/开发生产等价/日志/开发进程', '微服务架构/服务拆分/独立部署/康威定律', '微服务设计原则/SOA对比/松耦合/高内聚', '服务网格Service Mesh/边车模式/Sidecar', 'Istio/Linkerd/Envoy/架构/流量管理', '服务发现/Consul/Etcd/Zookeeper/DNS', '配置中心/Apollo/Nacos/Spring Cloud Config', 'API网关/Kong/APISIX/Envoy/路由/限流', '容器化Docker/镜像/仓库/网络/存储', '容器编排Kubernetes/声明式/资源管理', '不可变基础设施/镜像即构建/不可变部署', '声明式配置GitOps/基础设施即代码', 'ArgoCD/Flux/GitOps工作流', '持续交付/自动化流水线/蓝绿/金丝雀', '云原生存储/CSI/持久卷/存储类', '云原生网络/CNI/IPv6/NetworkPolicy', '服务网格安全/mTLS/零信任', '可观测性/监控/日志/追踪/OpenTelemetry', 'Prometheus/Loki/Tempo/分布式追踪', '故障隔离/熔断/限流/重试/超时', '弹性伸缩/HPA/VPA/KEDA', '自愈/健康检查/重启/驱逐', '混沌工程/Chaos Monkey/故障注入', '应用交付/Jenkins X/Tekton/Spinnaker', '云原生安全/镜像扫描/密钥管理/RBAC', 'Secrets管理/Vault/Kubernetes Secrets', '策略即代码/OPA/Sentinel', '多云/混合云/边缘计算', 'Serverless/FaaS/Knative/OpenFaaS', '函数计算/冷启动/自动扩缩', '云原生数据库/CockroachDB/TiDB/PlanetScale', '消息队列/CloudEvents/事件驱动', '云原生中间件/缓存/消息/搜索引擎', '容器运行时/containerd/cri-o/安全', '镜像安全/distroless/scratch/最小镜像', '最佳实践/架构设计/部署策略/监控告警']
                },
                '网络基础': {
                    'desc': 'TCP/IP、DNS、HTTP等网络协议',
                    'difficulty': 3,
                    'dimensions': ['OSI七层模型/应用层/传输层/网络层/链路层/物理层', 'TCP/IP四层模型/对应关系', 'TCP三次握手/SYN/SYN-ACK/ACK/序列号', 'TCP四次挥手/FIN/ACK/等待2MSL', 'TCP状态机/CLOSED/LISTEN/SYN_SENT/SYN_RCVD/ESTABLISHED', 'TCP可靠传输/确认机制/序列号/重传/流量控制/窗口', 'TCP拥塞控制/慢启动/拥塞避免/快速重传/快速恢复', 'TCP流量控制/滑动窗口/rwnd', 'UDP特性/无连接/不可靠/高效', 'UDP应用/DNS/QUIC/视频/游戏', 'IP协议/首部结构/分片/TTL/校验和', 'IP地址分类/A/B/C/D/E类', 'IPv4私有地址/10.0.0.0/172.16.0.0/192.168.0.0', 'IPv6地址/128位/压缩表示/类型', '子网划分/子网掩码/CIDR/VLSM', '路由基础/路由表/默认路由/静态路由', '动态路由/RIP/OSPF/BGP', 'ARP协议/地址解析/缓存', 'ICMP协议/ping/traceroute/错误报告', 'DNS协议/递归查询/迭代查询/根域名服务器', 'DNS记录类型/A/AAAA/CNAME/MX/TXT/NS/PTR', 'DNS缓存/TTL/TTL设置', 'DNS安全/DNSSEC/DOH/DOT', 'CDN原理/就近访问/缓存/回源', '负载均衡/L4/L7/算法', 'HTTP协议/请求行/请求头/请求体', 'HTTP方法/GET/POST/PUT/PATCH/DELETE/HEAD/OPTIONS', 'HTTP状态码/1xx/2xx/3xx/4xx/5xx', 'HTTP首部/Content-Type/Content-Length/Host/Cookie/Cache-Control', 'HTTP/1.0/1.1/2.0/3.0区别', 'HTTP/2 multiplexing/header compression/server push', 'HTTP/3 QUIC/0-RTT/连接迁移', 'HTTPS/TLS/SSL/加密过程', 'TLS握手/证书/密钥交换', '对称加密/非对称加密/混合加密', '数字签名/证书/CA/PKI', 'Session/Cookie/Token/JWT', '长连接/keep-alive/连接复用', '代理服务器/正向代理/反向代理/透明代理', 'CDN/缓存策略/Cache-Control/ETag/Last-Modified', 'WebSocket/全双工/握手/心跳', 'QUIC协议/可靠传输/拥塞控制', '网络安全/XSS/CSRF/SQL注入', 'ARP欺骗/DNS欺骗/中间人攻击', '防火墙/iptables/netfilter', 'NAT/网络地址转换/SNAT/DNAT/端口映射', 'VPN/隧道/IPSec/SSL VPN/OpenVPN', '网络诊断工具/ping/traceroute/mtr/nslookup/dig/tcpdump/wireshark', 'Socket编程/TCP Socket/UDP Socket', '三次握手四次挥手状态图', 'TCP粘包拆包/解决方案', 'HTTP缓存机制/强缓存/协商缓存', 'CDN加速原理/回源/边缘节点', '网络性能优化/连接复用/HTTP/2/压缩', '网络安全防护/WAF/IPS/IDS']
                },
            }
        },
        '移动端开发工程师': {
            'description': '开发iOS和Android移动应用，实现原生或跨平台功能。',
            'skills': {
                'Java': {
                    'desc': 'Android传统开发语言，生态成熟',
                    'difficulty': 1,
                    'dimensions': ['Java基础语法/数据类型/控制流', '面向对象/类/对象/继承/多态/接口', '异常处理/try-catch/throw/finally', '集合框架List/Set/Map/ArrayList/HashMap', '泛型/装箱拆箱', 'Lambda表达式/函数式接口', 'Stream API/函数式编程', 'IO流/文件操作/序列化', '多线程/Thread/Runnable/ExecutorService', '并发编程/synchronized/volatile/Atomic', 'JVM基础/内存管理/GC/类加载', 'Android环境/Android Studio/SDK', '四大组件Activity/Service/Broadcast/ContentProvider', 'Activity生命周期/onCreate/onStart/onResume', 'Activity状态保存onSaveInstanceState', 'Intent/IntentFilter/显式隐式启动', 'Layout布局/ConstraintLayout/LinearLayout/RelativeLayout', 'View绘制/onDraw/自定义View', '事件分发/touch事件/onTouchEvent', 'Handler机制/Looper/MessageQueue', 'AsyncTask/线程池', '内存泄漏/Handler泄漏/静态内部类', 'AndroidManifest/权限声明/组件注册', '资源管理/res/values/drawable', '构建系统/Gradle/依赖管理', 'APK打包/签名/混淆', 'Jetpack组件/Lifecycle/ViewModel/LiveData', 'Room数据库/ORM', 'WorkManager/后台任务', 'Navigation/Fragment导航', 'Paging分页加载', 'DataBinding/ViewBinding', 'Kotlin协程并发', '单元测试/JUnit/Mockito', '调试/Android Profiler/Memory Profiler', 'ADB调试/日志cat/logcat', '发布Google Play/签名配置']
                },
                'Kotlin': {
                    'desc': 'Android官方推荐开发语言，与Java完全互操作',
                    'difficulty': 1,
                    'dimensions': ['Kotlin基础/空安全/类型推断', 'var/val/可变/不可变变量', '函数定义/默认参数/命名参数', '扩展函数/扩展属性', 'Lambda表达式/高阶函数', '协程async/await/suspend', 'Coroutine上下文/Dispatchers', 'Flow/冷流/热流', '面向对象/类/对象/数据类/密封类', '继承/抽象类/接口', '可见性/ public/protected/private/internal', '集合/List/Set/Map/可变集合', '集合操作/filter/map/reduce/groupBy', ' lateinit/ by lazy/ Delegates', '协程scope/CoroutineScope/GlobalScope', '异常处理/try-catch/throw', '内联函数/inline/noinline/crossinline', '泛型/上界/协变/逆变', '解构/对象解构/Map解构', '运算符重载', 'DSL/领域特定语言', '注解/@Deprecated/@JvmName/@Parcelize', 'Kotlin与Java互调/JNI', '协程取消/isActive/withContext', 'Channel/Fan-out/Fan-in', 'Flow操作符/buffer/conflate/collectLatest', '单元测试/Kotest', '协程测试/runTest', 'Kotlin多平台/KMM']
                },
                'Swift': {
                    'desc': 'Apple开发的iOS应用编程语言，现代、安全、高效',
                    'difficulty': 1,
                    'dimensions': ['Swift基础/类型推断/Option', 'var/let常量变量', 'Optional/解包/guard/if let', '函数定义/参数标签/返回值', '闭包/尾随闭包/逃逸闭包', '类/结构体/枚举/协议', '继承/重写/ super', '属性/计算属性/懒加载属性/属性观察', '方法/静态方法/下标', '初始化/指定初始化/可失败初始化', '泛型/泛型约束', '协议/协议扩展/默认实现', '访问控制/public/private/open/file', '错误处理/throws/do-catch/try', '类型转换/is/as/Any/AnyObject', '自动引用计数ARC/强引用/弱引用/无主引用', '内存管理/weak/unowned', '集合类型/Array/Dictionary/Set', '字符串/String/Character', '函数式/Map/Filter/Reduce', '高阶函数/闭包表达式', 'Async/Await异步编程', 'Actor并发模型', '结构体/值类型', 'Copy-on-write', 'SwiftUI/声明式UI', 'Combine/响应式编程', 'Result类型', 'Swift Package Manager', '单元测试/XCTest']
                },
                'App发布': {
                    'desc': '应用商店审核流程和发布管理',
                    'difficulty': 2,
                    'dimensions': ['App Store审核指南/审核时长/被拒原因', 'App Store Connect/开发者账号/协议', '应用签名/证书/Certificate/Provisioning', 'Ad Hoc/企业签名/开发测试', 'App ID/Bundle ID/Package Name', '应用图标/启动图/App Store图片', '应用描述/关键词/隐私政策', '年龄分级/内容分级', 'Google Play Console/开发者控制台', '签名密钥/ keystore/上传密钥', 'AAB包/APK包/打包配置', 'Beta测试/内部测试/封闭式/开放式', 'Google Play内测/测试链接/测试组', 'TestFlight/iOS Beta测试', '版本号/Version Code/Version Name', '灰度发布/百分比发布', '热修复发布/Texure OTA', '应用市场ASO/关键词优化/排名', '隐私政策/用户协议', '权限说明/数据收集声明', '应用截图/宣传图/视频预览', '多语言/本地化/国际i18n', '应用大小优化/混淆压缩', '崩溃报告/Crashlytics/Firebase', '审核被拒/上诉/重新提交', 'App Store推广/付费推广/ASA', 'Google Play推广/Google Ads', '应用更新/增量更新/整包更新', '应用下架/撤回/重新上架', '应用市场规则/合规/数据安全']
                },
                'Flutter': {
                    'desc': 'Google跨平台UI框架，使用Dart语言，一套代码多端运行',
                    'difficulty': 2,
                    'dimensions': ['Flutter架构/Dart/引擎/Platform Channel', 'Widget/StatelessWidget/StatefulWidget', 'StatefulWidget生命周期/initState/didUpdateWidget/dispose', '布局Widget/Row/Column/Stack/Flex', 'Container/Padding/Margin/DecoratedBox', 'Text/Image/Icon/Asset', 'ListView/GridView/CustomScrollView', 'ScrollController/滚动控制', '手势GestureDetector/onTap/onPan', '状态管理/setState', '状态管理Provider/ChangeNotifierProvider', '状态管理Bloc/Event/State/BlocProvider', '状态管理Riverpod/StateNotifier/AsyncValue', '状态管理GetX/Controller/GetView', '状态管理Redux/Store/Reducer/Action', '路由Navigator/命明路由/参数传递', '路由go_router/路由守卫/嵌套路由', '网络请求dio/http包', 'JSON解析/json_serializable/model', '本地存储/SharedPreferences/sqflite', '数据库/Room/Isar/Moor', '图片缓存/cached_network_image', '图片选择器/image_picker', '视频播放器/video_player', '音频/just_audio/audjust', '地图/ google_maps_flutter/amap_fluttify', '定位/location/geolocator', '推送/flutter_local_notifications', '第三方登录/google_sign_in/apple_sign_in', '分享/share_plus', '分享/友盟/ShareSDK', '扫码/barcode_scan/qr_code_scanner', '权限/permission_handler', '国际化/intl/arb文件', '热重载/Hot Reload/热重启', '性能优化/RepaintBoundary/const', '构建release/apk/aab', '混淆/Dartobfuscate', 'Platform Channel/原生交互', '单元测试/flutter_test', '集成测试/integration_test', 'CI/CD/ Codemagic/GitHub Actions', '代码生成/freezed/json_serializable']
                },
                'React Native': {
                    'desc': '使用React构建原生移动应用的框架',
                    'difficulty': 2,
                    'dimensions': ['React Native架构/Bridge/新架构/TurboModule/Fabric', '组件/View/Text/Image/TextInput', 'StyleSheet/样式表', 'Flexbox布局/flexDirection/justifyContent', 'Props/组件属性传递', 'State/状态管理/useState', '生命周期/constructor/render/mount', 'Hook/useEffect/useCallback/useMemo/useRef', '自定义Hook', 'FlatList/虚拟列表/下拉刷新/上拉加载', 'SectionList/分组列表', 'ScrollView/可滚动视图', 'Navigation/React Navigation/Stack', 'Navigation/Tab/ Drawer', '路由传参/navigate/params', '网络请求fetch/axios', 'XMLHttpRequest', 'AsyncStorage/持久化存储', 'MMKV/Realm/数据库', '图片缓存/FastImage', '手势/Responder/gesture-handler', '动画 Animated/spring/loop/timing', '动画/Reanimated/useAnimatedStyle', '动画/Lottie', '状态管理/Context/useContext', '状态管理/Redux/Store', '状态管理/Zustand', '状态管理/MobX', 'Native Modules/原生模块', 'Native Components/原生组件', 'JSI/直接调用JS', 'TypeScript配合', '调试/Js bundle/Xcode/Android Studio', 'Hot Reload/热重载', '性能优化/FlatList key/渲染优化', '打包iOS/Xcode/archive', '打包Android/APK/AAB/签名', 'JS Bundle/产物分离', 'CI/CD/GitHub Actions/Fastlane', '单元测试/Jest', 'E2E测试/Detox', '地图SDK/react-native-maps', '推送/极光/友盟', '微信SDK/分享/登录/支付', '代码分割/Lazy/Suspense', ' Hermes引擎']
                },
                '地图定位': {
                    'desc': 'GPS定位、地图SDK集成',
                    'difficulty': 2,
                    'dimensions': ['GPS定位原理/卫星定位/AGPS', '基站定位/WiFi定位/IP定位', '定位精度/高精度/低精度', 'Android定位/LocationManager/FusedLocation', 'iOS定位/CoreLocation/CLLocationManager', '权限请求/动态权限/权限说明', '前台定位/后台定位/持续定位', '定位模式/高精度/低功耗/仅设备', '位置监听/RequestLocationUpdates', '逆地理编码/Geocoder', '地理编码/经纬度转地址', '地图SDK/高德/百度/腾讯/Google', '地图显示/MapView/MapFragment', '地图类型/普通/卫星/实时路况', '地图控件/缩放/定位/指南针', '地图标记/Marker/InfoWindow', '自定义标记/图标/弹窗', '坐标系统/ GCJ-02/BD-09/WGS-84', '坐标转换/互转', '地理围栏/Geo-fence', '室内定位/iBeacon/WiFi', '室内地图', '路径规划/步行/骑行/驾车', '导航/Navigation/路线引导', 'POI搜索/关键字搜索/周边搜索', '地图覆盖物/Overlay/Polygon/Polyline', '地图截屏', '地图交互/点击/长按/拖拽', '地图动画/移动/缩放', '离线地图', '定位误差处理', '省电策略', '后台定位保活', '地图SDK集成配置', 'API Key配置', '混淆配置']
                },
                '推送服务': {
                    'desc': 'APNs、FCM等推送通知集成',
                    'difficulty': 2,
                    'dimensions': ['推送原理/长连接/轮询', 'APNs/Apple Push Notification service', 'APNs证书/密钥/Auth Key', 'Device Token/设备令牌', 'VoIP推送', 'FCM/Firebase Cloud Messaging', 'FCM Server Key/ VAPID Key', '消息类型/通知消息/数据消息', '推送Payload/通知/ badge/ sound/ title/ body', '推送渠道/Channel/Category', '推送权限/请求/授权状态', '前台推送/后台推送/静默推送', '静默推送/ Silent Push/Content-Available', '本地推送/Local Notification', '极光推送/JPush', '友盟推送/UMPush', '华为推送/Huawei Push Kit', '小米推送/MiPush', 'OPPO推送/Vivo推送', '个推/Getui', '推送送达率/点击率', '推送打开率/统计', '推送点击跳转/Deep Link', '用户画像推送/标签推送', '推送定时/定时推送', '推送群发/批量推送', '推送测试/测试推送', '推送消息格式/JSON/APNs', 'iOS推送配置/entitlements', 'Android推送配置/manifest', '角标/Badge/红点', '通知渠道/Android 8.0+', '通知样式/大图/横幅', '交互式通知/Actions/Category', '推送策略/防打扰/静默期', '推送到达延迟', '推送失败处理', '设备注册/Token刷新', '主题订阅/Topic', 'iOS 16/实时活动/灵动岛']
                },
                '支付集成': {
                    'desc': '微信支付、支付宝、Apple Pay等',
                    'difficulty': 2,
                    'dimensions': ['支付流程/下单/支付/回调', '微信支付申请/商户号/APPID', '微信支付SDK/WXPay/调起支付', '微信支付签名/PaySign/校验', '微信支付回调/异步通知', '支付宝申请/商户号/APPID', '支付宝SDK/Alipay/调起支付', '支付宝签名/加签/验签', '支付宝回调/异步通知', 'Apple Pay/开发者账号', 'Apple Pay证书/Merchant ID', 'PKPaymentRequest/支付请求', 'PKPaymentAuthorizationViewController', 'Google Pay/商户ID', 'Google Pay API/PaymentData', 'PayPal/ Stripe/ Square', '银联支付/UPOP', '合并支付/多渠道支付', '支付密码/指纹/ Face ID', '生物识别支付', '支付安全/加密/防篡改', '支付结果查询/轮询/回调', '支付超时/订单取消', '退款流程/全额退款/部分退款', '退款回调', '对账/平账', '风控/限频/异常检测', '支付页面/H5支付', '原生支付/SDK支付', '扫码支付', '刷卡支付', '跨境支付', '虚拟支付', '支付异常处理', '支付日志', '支付统计', '聚合支付/综合平台']
                },
                '混合开发': {
                    'desc': 'WebView、Cordova、Ionic等混合应用方案',
                    'difficulty': 2,
                    'dimensions': ['混合开发原理/WebView/原生交互', 'WebView加载/loadUrl/loadData', 'WebView配置/JavaScriptEnabled', 'JSBridge/Hybrid/桥接', 'JSBridge原理/注入/拦截', 'JS调用原生/native.js', '原生调JS/evaluateJS', 'Cordova/PhoneGap', 'Cordova插件/生命周期', 'Ionic/Angular/Ionic Angular', 'Ionic React', 'React Native/原生渲染', 'Flutter/平台通道', '离线包/预加载/增量更新', '热更新/CodePush', 'RN Bundle/JS Bundle', 'Web实时通讯/WebSocket', 'Native与H5交互/事件传递', 'H5调用相机/相册', 'H5调用分享', 'H5调用定位', 'H5支付/调起支付', 'H5推送', '微信SDK/H5微信登录', '微信SDK/微信支付', '支付宝H5支付', 'App与H5共享登录态', 'Cookie/Token共享', 'Native Schem e/Deep Link', 'URL Scheme/通用链接', 'App Link/关联域名', 'H5页面调试', 'Chrome DevTools远程', 'Safari远程调试', 'H5性能优化', '离线缓存', '预加载WebView', '硬件加速', '内存管理', '安全/XSS/注入', '证书配置/HTTPS']
                },
                '移动端UI': {
                    'desc': '移动端设计规范、适配不同屏幕尺寸',
                    'difficulty': 2,
                    'dimensions': ['设计尺寸/iPhone/Android尺寸', '设计单位/dp/sp/pt', '分辨率/像素密度/DPI/PPI', '屏幕尺寸/5寸/5.5寸/6.7寸', '刘海屏/水滴屏/挖孔屏/屏下摄像头', '安全区域/Safe Area', '状态栏/导航栏高度', 'iOS设计规范/HIG', 'Material Design/MD3', 'Android设计/设计语言', '响应式布局/自适应', '百分比布局', 'Flexbox布局', 'Grid布局', '约束布局/ConstraintLayout', '自动布局/Masonry/SnapKit', '屏幕适配/ smallestWidth', '图片适配/@1x/@2x/@3x/@2x/@3x', '图片资源/drawable/mipmap', '多语言/i18n/本地化', '主题切换/暗色模式', '字体适配/缩放', '图片资源管理', '切图规范', '图标的绘制', '按钮状态/正常/按下/禁用', '颜色系统/主色/辅色/中性色', 'Typography/字体层级', 'Spacing/间距系统', '阴影Elevation', '圆角规范', '设计系统/Design System', '组件库/Element/Material-ui', '动画/过渡动画/微交互', '手势/滑动手势/长按/双击', '导航设计/Tab/抽屉/底部导航', '空状态/加载状态/错误状态', 'App Store截图', 'UI验收/设计还原']
                },
                'Android开发': {
                    'desc': 'Android SDK、Jetpack组件、Material Design',
                    'difficulty': 3,
                    'dimensions': ['Android架构/MVC/MVP/MVVM/Flux', '四大组件深入/Activity启动模式', 'Service/IntentService/前台Service', 'BroadcastReceiver/静态动态注册', 'ContentProvider/数据共享', 'View体系/ViewGroup/View测量/布局/绘制', '自定义View/onMeasure/onLayout/onDraw', 'Canvas/Paint/Bitmap/Path', '贝塞尔曲线', '动画/ValueAnimator/ObjectAnimator', '属性动画/插值器', 'RecyclerView/RecycleView.Adapter', 'DiffUtil/列表更新', 'ItemDecoration/分隔线/吸附', 'ViewPager2/PageTransformer', 'ViewStub/LayoutInflater', 'DataBinding/双向绑定', 'ViewBinding/非侵入式', 'Jetpack/Lifecycle/ViewModel', 'Jetpack/LiveData/生命周期感知', 'Jetpack/Navigation/Fragment导航图', 'Jetpack/Room/数据库ORM', 'Jetpack/Paging分页/数据懒加载', 'Jetpack/WorkManager/后台任务', 'Jetpack/DataStore/KV存储', 'Jetpack/Hilt/依赖注入', 'Jetpack/Startup/启动优化', 'Jetpack/Compose声明式UI', 'Material Design/组件库', 'Material/Button/TextField/AppBar', 'Material/BottomSheet/Dialog/Sheet', 'Material/ BottomNavigation/TabLayout', 'Material/Chip/ToggleButton/Switch', 'Material/CardView/RecyclerView', 'Material/FloatingActionButton', 'Material/Snackbar/Toast', 'Material/ProgressIndicator', 'Material/Switch/Toggle', 'Material Design Theme', 'Material Dark Mode', 'Material动效', 'Kotlin/协程/Flow', '架构组件/Repository/UseCase', 'Clean架构/分层', 'DDD/领域驱动设计', '模块化/组件化', '热修复/Tinker/Andfix', '插件化/ VirtualAPK', 'Hook技术/反射', '性能优化/启动优化', '布局优化/过度绘制', '内存优化/LeakCanary', '网络优化/缓存', '电量优化', 'APM/监控', '逆向/反编译/混淆', '安全/加固/加密']
                },
                'iOS开发': {
                    'desc': 'UIKit、SwiftUI、Core Data等iOS框架',
                    'difficulty': 3,
                    'dimensions': ['UIKit/UIViewController', 'UIView/控件层次', 'Auto Layout/Masonry/SnapKit', 'Size Class/Size Classes', '布局适配/安全区域', 'UITableView/ UITableViewCell', 'UICollectionView/Compositional Layout', 'UICollectionViewDiffableDataSource', '手势/UIGestureRecognizer', '动画/UIView.animate', 'Core Animation/CALayer', 'UIBezierPath/贝塞尔曲线', 'Core Graphics/Quartz 2D', 'Core Image/图片滤镜', 'ImageIO/图片编解码', 'Texture/异步布局', 'UIKit交互/响应链', 'UIKit/UIControl', 'UIKit/UIButton/UITextField', 'UIKit/UIScrollView', 'UIKit/UIWebView/WKWebView', 'WebKit/WKWebViewConfiguration', 'WebKit/JS交互/WKScriptMessageHandler', 'Navigation/ UINavigationController', 'TabBar/UITabBarController', 'PageController/UIPageViewController', 'Modal/Present/Dismiss', 'iOS 13/Sheet/全屏', 'SwiftUI/声明式UI', 'SwiftUI/@State/@Binding/@ObservedObject', 'SwiftUI/@Environment/@EnvironmentObject', 'SwiftUI/Modifier/ViewModifier', 'SwiftUI/Stack/LazyVStack', 'SwiftUI/List/ForEach', 'SwiftUI/NavigationStack', 'SwiftUI/Sheet/FullScreenCover', 'SwiftUI/Combine', 'SwiftUI/Toolbar', 'SwiftUI/偏好设置', 'Core Data/ORM', 'Realm/Swift', 'SQLite/ FMDB/SQLite.swift', 'UserDefaults/Keychain', 'FileManager/沙盒', 'URLSession/网络', 'Alamofire/Moya', 'Kingfisher/图片缓存', 'SnapKit/约束', 'SnapKit/动画', 'Combine/发布者/订阅者', 'Combine/操作符/map/filter', 'Combine编码解码', 'iOS动画/Transition', 'iOS动画/Interactive', 'iOS动画/UIDynamic', 'iOS动画/Physics', 'Core Location定位', 'MapKit/地图', 'CoreBluetooth/蓝牙', 'AVFoundation/音视频', 'Photos/照片库', 'Contacts/通讯录', 'HealthKit/健康数据', 'Widget/WidgetKit', 'Widget/TimelineProvider', 'Widget/Small/Medium/Large', 'iOS 14+/App Clips', 'iOS 15+/SF Symbols', 'iOS 16+/实时活动/灵动岛', 'Swift Concurrency/async/await', 'Swift/Structured Concurrency', 'Swift/Actor/隔离', 'Swift/TaskGroup', 'TestFlight测试', '上架App Store', '隐私政策/权限说明', 'iOS自动化测试/XCUITest', ' Instruments/性能分析', '内存管理/Autorelease Pool', 'ARC/循环引用', '内存管理/weak/unowned', '内存管理/weakSafe', 'Instruments/Leaks/Allocations']
                },
                '性能优化': {
                    'desc': '启动优化、内存管理、电量优化',
                    'difficulty': 3,
                    'dimensions': ['启动时间/冷启动/热启动/温启动', '启动流程/main之前/load/dylibs', '启动流程/main之后/applicationDidFinishLaunching', '启动优化/懒加载/预加载', '启动优化/二进制重排/Page In', '启动优化/启动窗口', '内存管理/内存警告', '内存管理/内存峰值', '内存优化/Autorelease Pool', '内存优化/图片优化', '内存优化/大图处理', '内存泄漏/LeakCanary/Instruments', '循环引用/strong/weak', 'Core Memory/内存分析', '电量优化/节能模式', 'CPU占用/计算优化', 'GPU占用/渲染优化', 'I/O优化/磁盘读写', '网络优化/请求合并', '网络优化/缓存/CDN', '网络优化/压缩/Gzip', '网络优化/Keep Alive', '电量监控/Instruments/Energy Log', '后台耗电/后台任务', '电量优化技巧', '帧率/FPS/卡顿检测', '卡顿优化/主线程', '卡顿监控/Method Swizzling', '卡顿监控/Runloop', '离屏渲染/光栅化', '离屏渲染优化', '图片优化/编解码', '图片优化/WebP/HEIC', '列表优化/ Cell预加载', '列表优化/Cell复用', '列表优化/预估高度', '列表优化/DiffUtil', '列表优化/图片懒加载', '内存缓存/LRU/NSCache', '磁盘缓存/缓存策略', '缓存淘汰/LRU/FIFO', '包体积/无用资源', '包体积/代码混淆', '包体积/资源优化', '包体积/动态库', '性能监控/APM', '性能监控/上报', '性能打点', '真机测试', '模拟器测试', 'profile工具']
                },
                '热更新': {
                    'desc': '动态下发代码修复线上问题',
                    'difficulty': 3,
                    'dimensions': ['热更新原理/动态下发', 'iOS热更新限制/苹果政策', 'Android热更新/Tinker', 'Android热更新/Andfix', 'Android热更新/ Robust', 'Android热更新/ Amigo', 'Tinker集成/ patch.dex', 'Tinker生成补丁', 'Tinker/差量合成', 'Tinker/加载流程', 'RN热更新/CodePush', 'RN Bundle/JS Bundle', 'RN Bundle/产物分离', 'Flutter热更新/Dart Hot Reload', 'Flutter热更新/热重启', 'Flutter热更新/增量更新', 'React Native/Metro', 'React Native/开发者菜单', 'Lua热更新/Cocos2dx', 'Lua脚本/更新流程', 'JS引擎/XCode内置/JSContext', 'JS引擎/Facebook Hermes', 'JS引擎/V8', 'JS引擎/jscore', '小程序热更新', 'Wasm热更新', '资源热更新/图片/配置', '配置热更新/开关', 'AB测试/灰度', '功能开关/远程配置', 'A/B测试框架', '灰度发布/百分比', '版本兼容性', '热更新失败处理', '热更新回退', '热更新推送', '热更新统计', '热更新安全/校验', '代码安全/混淆/加密', 'H5热更新/离线包', 'Electron热更新', '更新策略/强制更新', '更新提示/用户交互', '下载管理/断点续传', '版本对比/语义化版本']
                }
            }
        }
    },
    '人工智能': {
        '算法工程师': {
            'description': '研究和开发机器学习算法，解决实际的AI问题，优化模型性能。',
            'skills': {
                'NumPy': {
                    'desc': '数值计算库，提供高效的多维数组操作',
                    'difficulty': 1,
                    'dimensions': ['NumPy基础/ndarray/数组创建/数组属性', '数据类型/int/float/complex/bool', '数组索引/整数索引/切片/布尔索引', '数组形状/shape/reshape/flatten/ravel', '数组运算/加减乘除/矩阵乘法/@', '广播机制/Broadcast/维度匹配', '聚合函数/sum/mean/std/var/max/min', '排序/sort/argsort/lexsort', '查找/nonzero/where', '拼接/stack/vstack/hstack/concatenate', '分割/split/hsplit/vsplit/array_split', '复制/copy/deep copy/shallow copy', '向量化/ufunc/通用函数', '数学函数/sin/cos/exp/log', '随机数/random/randn/randint/shuffle', '线性代数/eigenvalue/svd/matrix_rank/dot', '范数/linalg.norm', '行列式/linalg.det', '逆矩阵/linalg.inv', '解线性方程/linalg.solve', '傅里叶变换/fft/ifft', '文件IO/savetxt/loadtxt/tofile/fromfile', '内存布局/C-contiguous/F-contiguous', '视图与拷贝/view/copy', '条件筛选/boolean_mask', '分位点/quantile/percentile', '数组去重/unique', '数组堆叠/dstack/apstack', '数组重排/transpose/T/swapaxes', '字符串函数/chararray', '结构化数组/dtype/structured', '掩码数组/MaskedArray', '性能优化/向量化/避免循环', '与列表转换/list/array']
                },
                'Pandas': {
                    'desc': '数据处理和分析库，用于数据清洗和预处理',
                    'difficulty': 1,
                    'dimensions': ['Pandas基础/Series/DataFrame', '数据读取/read_csv/read_excel/read_json/read_sql', '数据查看/head/tail/info/describe/shape', '数据选择/列选择/行选择/loc/iloc', '布尔索引/条件筛选', '缺失值/isnull/notnull/fillna/dropna', '数据替换/replace/fillna', '数据排序/sort_values/sort_index', '数据合并/concat/merge/join', '拼接append/prepend', '分组groupby/agg/apply/transform', '聚合函数/sum/mean/count/std/describe', '透视表pivot_table/crosstab', '数据重塑/melt/pivot/stack/unstack', '字符串操作/str.contains/str.replace/str.split', '日期时间/datetime/to_datetime/date_range', '时间序列/resample/asfreq/shift', '窗口函数/rolling/expanding', '数据去重/duplicated/drop_duplicates', '数据映射/map/apply/applymap', '类型转换/astype/dtypes', '重命名rename/columns/index', '索引操作/set_index/reset_index', '随机采样/sample', '分箱cut/qcut', '数据计算/加减乘除/累计计算', '排名rank', '值统计/value_counts', '迭代iterrows/itertuples', '文件保存/to_csv/to_excel/to_json', '性能优化/向量化/分类数据类型', '多索引MultiIndex/层次化索引', '数据验证/assert_series_equal']
                },
                'Python': {
                    'desc': 'AI领域主流编程语言，拥有丰富的科学计算和机器学习库',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/控制流/函数', '列表/字典/集合/元组', '列表推导式/字典推导式', '生成器/yield/next/StopIteration', '迭代器/Iterator/Iterable', '装饰器/@wraps/functools', '装饰器/参数化装饰器', '上下文管理器/with/__enter__/__exit__', '异常处理/try-except/raise', '文件操作/read/write/上下文', '正则表达式/re模块/match/search/findall/sub', '日期时间/datetime/time/calendar', '类型注解/typing/TypeVar/Generic', '抽象基类/ABC/abstractmethod', '接口/Protocol/duck typing', '魔术方法/__init__/__str__/__repr__', '深拷贝/浅拷贝/copy模块', '哈希/hashlib', '序列化/json/pickle', '并发/asyncio/threading/multiprocessing', '单元测试/unittest/pytest', '科学计算/numpy/scipy', '数据处理/pandas', '数据可视化/matplotlib/seaborn/plotly', '机器学习/scikit-learn/xgboost/lightgbm', '深度学习/tensorflow/pytorch/keras', 'Jupyter/IPython', '环境管理/venv/conda', '包管理/pip/conda', '代码规范/PEP8', '虚拟环境隔离', '类型检查/mypy', '文档/docstring', '日志logging', '配置管理/configparser/yaml']
                },
                'A/B测试': {
                    'desc': '设计实验验证算法效果',
                    'difficulty': 2,
                    'dimensions': ['A/B测试原理/对照组/实验组', '实验设计/随机分组/均匀分布', '样本量计算/统计功效/Power Analysis', '显著性检验/t检验/z检验/p值', '置信区间/95%置信度', '多重比较问题/多重检验校正', '分流策略/均匀分流/分层分流', '分流算法/hash分流/uid分流', '流量分配/流量层/实验层', '实验周期/样本量/观察期', '指标选择/北极星指标/辅助指标', '指标构建/归因窗口', '数据埋点/事件上报', '数据采集/日志收集', '统计检验/配对t检验/卡方检验', '效果评估/提升度/Lift', '效果评估/置信度/置信区间', '方差分析/ANOVA', '回归分析/协变量调整', '分层抽样/分层比例', '分群分析/同质性检验', 'AA测试/基准测试', '冷启动问题', '新奇效应/首因效应', '网络效应/溢出效应', '地理实验', '时间效应/周末效应/节假日效应', '用户交互效应', '实验监控/报警', '实验平台/配置中心', '灰度发布', '特征开关/Feature Flag', 'Canary Release', 'AB测试框架', '在线实验/Jurewitz', '因果推断/Causal Inference', '倾向得分匹配/PSM', '双重差分/DID', 'Uplift Modeling', '异质性因果效应/HTE', '元分析/Meta Analysis', 'Sequential Testing', '多臂老虎机/MAB']
                },
                'Keras': {
                    'desc': '高级神经网络API，简化深度学习模型构建',
                    'difficulty': 2,
                    'dimensions': ['Keras基础/ Sequential/Functional API', '层/Layer/Dense/Activation/Dropout/BatchNormalization', '激活函数/relu/sigmoid/softmax/tanh', '损失函数/categorical_crossentropy/binary_crossentropy/mse', '优化器/SGD/Adam/RMSprop/Adagrad', '编译model.compile', '训练model.fit/epochs/batch_size', '回调Callback/ EarlyStopping/ ModelCheckpoint/ TensorBoard', '模型保存/load_model/h5/ SavedModel', '模型加载/save/load_weights', '数据处理/ImageDataGenerator', '数据增强/旋转/翻转/缩放/裁剪', '卷积层/Conv1D/Conv2D/MaxPooling/AveragePooling', '循环层/LSTM/GRU/Bidirectional', '嵌入层/Embedding', '注意力层/Attention/AdditiveAttention', 'Transformer/ MultiHeadAttention', '自定义层/Lambda/自定义Layer', '自定义损失函数', '自定义指标/Accuracy/Precision/Recall/F1', '多输入多输出/Functional API', '共享层/Shared Layers', '迁移学习/预训练模型/VGG/ResNet/BERT', 'fine-tuning/冻结层', '模型可视化/plot_model', '训练历史/history', '欠拟合过拟合/正则化', '学习率调度/ReduceLROnPlateau', '梯度裁剪', '分布式训练/MirroredStrategy', 'TFRecord数据格式', 'tf.data数据管道', 'Dataset API', 'Eager Execution', 'Keras Tuner/Hyperband', 'Scikit-learn API/wrapper']
                },
                'LightGBM': {
                    'desc': '微软高效梯度提升框架，训练速度快内存占用低',
                    'difficulty': 2,
                    'dimensions': ['LightGBM基础/lgb.Dataset/lgb.train/lgb/sklearn API', '安装配置/pip install', '训练参数/objective/metric', '分类任务/ binary/multiclass', '回归任务/regression', '学习目标/reg:squarederror/reg:squaredlogerror', '评估指标/rmse/mae/auc/logloss', '叶节点数/num_leaves', '树深度/max_depth', '样本采样/subsample/bagging_fraction', '特征采样/colsample_bytree', '学习率/learning_rate/eta', '迭代次数/n_estimators/num_iterations', '正则化/reg_alpha/reg_lambda', '最小数据量/min_child_samples', '特征重要性/feature_importance/plot_importance', '分类特征/categorical_feature', '缺失值处理', '早停/early_stopping/valid_sets', '交叉验证/cv', '预测predict/predict_proba', '线性模型/LGBMRegressor/LGBMClassifier', '剪枝/lambda_l1/lambda_l2', 'DART/Dropouts meet Multiple Additive Regression Trees', 'GOSS/Gradient-based One-Side Sampling', 'EFB/Exclusive Feature Bundling', '直方图算法/Histogram-based', '并行学习/特征并行/数据并行', 'GPU训练/device/gpu_use_dp', '大规模数据训练', '特征交叉/interaction_constraints', '目标编码/categorical_feature/ Target Encoding', 'SHAP/TreeSHAP/特征归因', '调参策略/贝叶斯优化', '特征选择', '输出日志/logging_level', '与XGBoost对比']
                },
                'PyTorch': {
                    'desc': 'Facebook开源深度学习框架，动态图机制灵活易用',
                    'difficulty': 2,
                    'dimensions': ['PyTorch基础/Tensor/Device/CUDA', '张量创建/ones/zeros/randn/arange/linspace', '张量操作/indexing/slicing/reshape/transpose', '自动求导/requires_grad/backward', '计算图/Graph/Node', '梯度计算/grad/ zero_grad', '神经网络/nn.Module', '层/Linear/Conv2d/MaxPool2d/AvgPool2d', '激活函数/ReLU/Sigmoid/Tanh/Softmax', 'Dropout/BatchNorm/LayerNorm', '损失函数/MSELoss/BCELoss/CrossEntropyLoss', '优化器/SGD/Adam/AdamW/RMSprop', '学习率调度/StepLR/ReduceLROnPlateau/CosineAnnealing', '数据加载/DataLoader/Dataset/TensorDataset', '数据增强/transforms', '训练循环/backward/optimizer.step', '验证循环/eval/train', '模型保存/torch.save/state_dict', '模型加载/torch.load/load_state_dict', 'GPU训练/.to(device)/.cuda()', '分布式/DistributedDataParallel', '混合精度/AMP/autocast', '梯度裁剪/clip_grad_norm_', 'EarlyStopping', 'FGM/对抗训练', '模型微调/Fine-tuning', '预训练模型/torchvision/models', 'Hugging Face/transformers', 'TorchScript/ JIT编译', 'ONNX导出/torch.onnx.export', '自定义Dataset', 'collate_fn', 'WeightedRandomSampler', 'Checkpoint保存加载', '梯度累积/accumulation_steps', 'PyTorch Lightning', 'torch.compile', 'nn.functional/API']
                },
                'Scikit-learn': {
                    'desc': '传统机器学习算法库，包含分类、回归、聚类等算法',
                    'difficulty': 2,
                    'dimensions': ['sklearn基础/API设计/fit/predict/transform', '线性回归/LinearRegression', '逻辑回归/LogisticRegression', '岭回归/Ridge/Lasso/ElasticNet', '决策树/DecisionTreeClassifier/Regressor', '随机森林/RandomForestClassifier/Regressor', '梯度提升/GradientBoostingClassifier', 'AdaBoost', 'SVM/Support Vector Machine', 'SVC/SVR/SVR', '朴素贝叶斯/NaiveBayes/GaussianNB/MultinomialNB', 'KNN/KNeighborsClassifier/KNeighborsRegressor', '聚类/KMeans/Agglomerative/DBSCAN/Spectral', 'DBSCAN/密度聚类', '层次聚类/linkage/cophenet', '降维/PCA/LDA/ t-SNE/UMAP', 'PCA/主成分分析/方差解释率', '特征选择/SelectKBest/SelectFromModel/RFE', '特征缩放/StandardScaler/MinMaxScaler/RobustScaler', '数据预处理/Imputer/LabelEncoder/OneHotEncoder', 'Pipeline/管道', 'ColumnTransformer', '模型评估/cross_val_score', '分类指标/accuracy/precision/recall/f1/roc_auc', '回归指标/mse/rmse/mae/r2', '聚类指标/silhouette_score', '混淆矩阵/confusion_matrix', '分类报告/classification_report', 'ROC曲线/roc_curve/auc', '学习曲线/learning_curve', '验证曲线/validation_curve', '网格搜索/GridSearchCV', '随机搜索/RandomizedSearchCV', '交叉验证/KFold/StratifiedKFold', '留一法/LeaveOneOut', '模型持久化/joblib/dump/load', '标签编码/LabelEncoder', '独热编码/OneHotEncoder', '缺失值填充/Imputer/SimpleImputer', '异常检测/IsolationForest/EllipticEnvelope', '高斯混合/GMM', '贝叶斯优化/Hyperopt/Optuna', '多标签分类/MultiLabelBinarizer']
                },
                'TensorFlow': {
                    'desc': 'Google开源深度学习框架，支持大规模分布式训练',
                    'difficulty': 2,
                    'dimensions': ['TensorFlow基础/2.x/Keras API', '张量/Tensor/constant/variable', '运算/add/subtract/multiply/div matmul', '自动求导/GradientTape', '层/ Dense/Conv2D/MaxPooling2D/Dropout/BatchNormalization', '激活函数/relu/sigmoid/softmax', '模型构建/Sequential/Functional/Subclassing', '损失函数/MSE/BinaryCrossentropy/CategoricalCrossentropy', '优化器/Adam/SGD/RMSprop', '训练/fit/evaluate/predict', '回调/ EarlyStopping/ ModelCheckpoint/ TensorBoard', '数据管道/tf.data.Dataset', '数据增强/图像增强', 'TensorBoard可视化', '模型保存/SavedModel/keras/h5', '模型加载/load_model', 'GPU配置/gpu_options', '分布式策略/MirroredStrategy/MultiWorkerMirroredStrategy', 'TFRecord/数据序列化', '特征列/feature_column', '迁移学习/预训练模型', '自定义训练循环', '梯度裁剪', '混合精度训练', 'TensorFlow Lite/TFLite', '模型量化/Post-training quantization', 'TensorFlow.js', 'TensorFlow Serving', 'TensorFlow Extended/TFX', 'Data Validation', 'Schema Definition', 'Transform', 'Example Gen', 'Statistics Gen', 'Model Analysis', 'TensorFlow Hub', 'EfficientNet/ResNet/VGG', 'Object Detection API', 'BERT/Transformer', 'TensorFlow Probability', 'TensorFlow Addons', 'tf.estimator', 'Feature Spec', 'Wide & Deep', 'Cloud TPU', 'XLA编译']
                },
                'XGBoost': {
                    'desc': '梯度提升决策树库，在结构化数据上表现优异',
                    'difficulty': 2,
                    'dimensions': ['XGBoost基础/xgb.XGBClassifier/xgb.XGBRegressor', '安装配置/pip install', '训练参数/objective/eval_metric', '分类/binary:logistic/binary:logitraw', '回归/reg:squarederror/reg:squaredlogerror', '评估指标/rmse/mae/logloss/auc/error', '树参数/max_depth/min_child_weight', '叶子数/num_leaves(lightgbm对比)', '样本采样/subsample/colsample_bytree', '学习率/learning_rate/eta', '迭代次数/n_estimators/num_boost_round', '正则化/reg_alpha/reg_lambda/gamma', '列采样/colsample_bylevel', '缺失值处理', '早停/early_stopping_rounds', '交叉验证/xgb.cv', '特征重要性/feature_importances_/plot_importance', '树可视化/plot_tree', '预测/predict/predict_proba', '与sklearn集成', 'DMatrix数据格式', '稀疏矩阵处理', '直方图算法/hist/tree_method', '近似算法/approx', '并行化/n_jobs', 'GPU训练/tree_method=gpu_hist', '深度学习/DART/Dropout', '叶子节点权重计算', '增益计算/gain', '分裂搜索策略', '特征交叉/interaction_constraints', '自定义目标函数', '自定义评估函数', 'SHAP/TreeSHAP/特征归因', '调参经验', '与其他GBDT对比/LightGBM/CatBoost', '大规模数据处理', '稀疏特征处理']
                },
                '机器学习': {
                    'desc': '监督学习、无监督学习、强化学习等算法原理和应用',
                    'difficulty': 2,
                    'dimensions': ['机器学习分类/监督/无监督/半监督/强化', '监督学习/分类/回归', '无监督学习/聚类/降维/异常检测', '线性回归/最小二乘法/正则化', '逻辑回归/sigmoid/odds/对数几率', '决策树/ID3/C4.5/CART', '信息增益/基尼系数', '决策树剪枝/预剪枝/后剪枝', '随机森林/Bagging/样本扰动/特征扰动', 'AdaBoost/Boosting/弱分类器组合', '梯度提升/GBDT/负梯度拟合', 'XGBoost/二阶导数/正则化', 'LightGBM/直方图/叶节点优化', 'CatBoost/类别特征/有序提升', '支持向量机/核函数/间隔', '核函数/线性核/多项式核/高斯核', 'K近邻/KNN/Lazy Learning', '朴素贝叶斯/贝叶斯定理/条件独立', '概率校准/Platt Scaling', '聚类/K-Means/K-Medoids', '层次聚类/凝聚式/分裂式', 'DBSCAN/密度可达/核心点', 'GMM/高斯混合/EM算法', '降维/PCA/SVD/LDA', '流形学习/t-SNE/Isomap/LLE', '异常检测/IsolationForest/LOF', '强化学习/MDP/马尔可夫决策过程', '策略/Policy/Value Function', '动态规划/Value Iteration/Policy Iteration', '蒙特卡洛/Monte Carlo方法', '时序差分/TD Learning', 'Q-Learning', 'SARSA', '深度Q网络/DQN', 'Policy Gradient', 'Actor-Critic/A2C/A3C', 'DDPG/TD3/SAC', '模型评估/交叉验证/留出法', '过拟合/欠拟合/偏差方差', '正则化/L1/L2/Dropout', '归一化/标准化/特征缩放', '特征选择/过滤法/包装法/嵌入法', '集成学习/Stacking/Voting/Blending', '概率论基础/概率分布/贝叶斯', '信息论/熵/互信息/KL散度', '最优化/梯度下降/牛顿法']
                },
                '特征工程': {
                    'desc': '从原始数据中提取有效特征，提升模型性能',
                    'difficulty': 2,
                    'dimensions': ['特征工程概述/重要性/方法论', '数据清洗/缺失值/异常值/重复值', '缺失值处理/删除/填充/预测填充', '异常值检测/Z-score/IQR/IsolationForest', '异常值处理/删除/替换/缩尾', '数值特征/标准化/Z-score/MinMax', '数值特征/归一化/RobustScaler', '分箱/Binning/等频/等距/决策树分箱', '对数变换/log/sqrt', '幂变换/Box-Cox/Yeo-Johnson', '类别特征编码/Label Encoding/One-Hot', 'Target Encoding/均值编码', '特征哈希/Hashing', '有序类别编码', '时间特征/年/月/日/时/分/秒', '时间特征/星期/工作日/节假日', '时间序列滞后/lag/lead', '滚动统计量/rolling/expanding', '差分/一阶差分/季节差分', '日期特征/DateOffset/Python datetime', '文本特征/TF-IDF/词袋模型', '文本特征/Word2Vec/FastText', '文本特征/分词/词性/命名实体', '交叉特征/组合特征/笛卡尔积', '特征组合/数学运算', '聚合特征/groupby聚合', '统计特征/count/mean/std/sum', '比率特征/比例计算', '特征选择/方差阈值', '特征选择/相关性分析', '特征选择/卡方检验', '特征选择/互信息', '特征选择/L1正则化', '特征选择/树模型重要性', '特征选择/递归消除RFE', '特征提取/PCA/SVD', '特征提取/自编码器', '特征构造/业务理解', '特征监控/分布变化', '特征重要性分析', 'SHAP/特征归因', '类别不平衡/SMOTE/ADASYN', '降噪/Autoencoder/Denoising', '特征工程自动化/AutoFE', '用户特征/画像特征', '物品特征/Content特征', '交互特征/行为特征']
                },
                'MLOps': {
                    'desc': '机器学习模型的开发运维一体化',
                    'difficulty': 3,
                    'dimensions': ['MLOps概述/定义/核心理念', 'MLOps成熟度模型/Level 0-5', 'CI/CD for ML/持续集成/持续交付', '自动化机器学习/AutoML', '超参数优化/HPO', '模型注册/Model Registry', '模型版本管理', '特征存储/Feature Store', '离线特征/在线特征', '特征平台/Pinecone/Feast/Tecton', '数据版本控制/DVC', '实验跟踪/MLflow/Weights & Biases', '实验跟踪/Neptune/Comet', '日志记录/参数/指标/工件', '模型监控/数据漂移/概念漂移', '漂移检测/EvidentlyAI', '告警机制', 'A/B测试/灰度发布', '金丝雀发布', '模型回滚', '容器化/Docker/镜像', 'Kubernetes部署', 'Kubeflow/Pipeline', 'Kubeflow Katib/超参搜索', 'Seldon/Seldon Core', 'MLflow Serving', 'Triton Inference Server', '模型服务化/Serving/Endpoint', '实时推理/Batch Inference', '模型压缩/Pruning', '模型量化/INT8/FP16', '知识蒸馏/Distillation', 'ONNX Runtime', 'TensorRT', '模型加密', '模型审计/可解释性', 'ML Metadata/MLMD', '数据验证/TFDV', '数据漂移/Docker', '特征重要性/Drift', '模型性能监控', '业务指标监控', '资源管理/CPU/GPU', '成本优化', 'SLA管理', '安全/鉴权/加密', '合规/GDPR/隐私', 'ML平台架构', 'Metaflow', 'ZenML', 'Flyte', 'KubeFlow vs Airflow', 'Data Pipeline/调度', 'Apache Airflow', 'Dagster', 'Prefect', '增量训练', '在线学习', 'Federated Learning', 'MLOps最佳实践']
                },
                '数学基础': {
                    'desc': '线性代数、概率统计、微积分、优化理论',
                    'difficulty': 3,
                    'dimensions': ['线性代数/向量/矩阵运算', '矩阵乘法/维度变换', '行列式/计算/性质', '逆矩阵/伪逆/Moore-Penrose', '特征值/特征向量/谱分解', '正定矩阵/半正定', '矩阵范数/Frobenius/L1/L2', '奇异值分解/SVD', '矩阵分解/LU/QR/Cholesky', '向量空间/基/维数', '正交/正交基/正交化', '概率论/概率分布/期望方差', '离散分布/伯努利/二项/泊松', '连续分布/正态/指数/均匀', '中心极限定理', '贝叶斯定理/后验/先验', '最大似然估计/MLE', '最大后验估计/MAP', '假设检验/t检验/z检验', '置信区间', '相关性分析/Pearson/Spearman', '信息论/熵/条件熵', '互信息/KL散度/交叉熵', '微积分/极限/连续/导数', '偏导数/梯度', '链式法则', '积分/不定积分/定积分', '多重积分', '泰勒展开', '梯度下降法/随机梯度', '牛顿法/拟牛顿法', '共轭梯度法', '约束优化/拉格朗日乘数', 'KKT条件', '凸优化/凸函数', '非凸优化', '拉格朗日对偶', 'SVM对偶问题', '信息增益/决策树', 'EM算法', '变分推断', '矩阵求导', '概率图模型/贝叶斯网络', '马尔可夫链', '随机过程', '蒙特卡洛方法', '采样方法/MCMC', 'Gumbel-Softmax']
                },
                '模型优化': {
                    'desc': '超参数调优、模型压缩、量化部署',
                    'difficulty': 3,
                    'dimensions': ['超参数调优概述/策略', '网格搜索/Grid Search', '随机搜索/Random Search', '贝叶斯优化/BO', '贝叶斯优化/GP/Acquisition Function', 'Hyperband/Population Based Training', '神经架构搜索/NAS', 'DARTS/可微分架构搜索', '进化算法/遗传算法调参', '早停/Early Stopping', '学习率调度/Step/Cosine/Polynomial', '学习率warmup', '批量大小选择', '正则化/L1/L2/Elastic Net', 'Dropout/DropConnect', 'Batch Normalization', '权重衰减/Weight Decay', 'Label Smoothing', '数据增强/MixUp/CutMix', '数据增强/自动增强/AutoAugment', '模型压缩概述', '结构化剪枝/Unstructured Pruning', '剪枝/通道剪枝/权重剪枝', '剪枝/神经元剪枝', '剪枝/再训练恢复', '量化/Post-training Quantization', '量化/Dynamic Quantization', '量化/Static Quantization', '量化/INT8/INT4', '量化/QAT/Quantization Aware Training', '量化/TFLite/ONNX', '知识蒸馏/Distillation/Teacher-Student', '知识蒸馏/温度参数', '蒸馏损失/Feature Distillation', '模型小型化/MobileNet/ShuffleNet', 'EfficientNet/复合缩放', '神经网络架构/ResNet/ResNeXt', 'Inception/VGG/AlexNet', '轻量化网络/MobileNetV1-3/EfficientNet-Lite', '部署优化/图优化/Fuse Op', 'TensorRT优化', 'XLA编译优化', 'CPU优化/AVX512', 'GPU优化/CUDA/cuDNN', '推理延迟优化', '模型缓存', '模型版本管理', '模型分片', '流水线并行', '模型服务化', 'ONNX Runtime', 'OpenVINO', 'CoreML/TFLite', 'Benchmark']
                },
                '深度学习': {
                    'desc': '神经网络架构设计，CNN、RNN、Transformer等模型',
                    'difficulty': 3,
                    'dimensions': ['神经网络基础/Perceptron/MLP', '激活函数/sigmoid/tanh/ReLU/Leaky ReLU/ELU/GELU', '损失函数/MSE/CEE/Hinge', '反向传播/Backpropagation/梯度计算', '梯度消失/梯度爆炸', '权重初始化/Xavier/He/Kaiming', '优化算法/SGD/Momentum/Adam/AdamW/NAdam', '学习率衰减/CosineAnnealing/Step', 'Batch Normalization/层归一化', 'Dropout/正则化', '归一化方法/BatchNorm/LayerNorm/GroupNorm/InstanceNorm', '卷积神经网络CNN/Conv/ pooling', '卷积/Valid/Same/Full', '卷积核大小/步长/填充', '空洞卷积/Dilated/Atrous', '深度可分离卷积/DW Conv/PW Conv', '分组卷积/Group Conv', 'SENet/通道注意力', 'CBAM/空间注意力', 'ResNet/残差连接/shortcut', 'ResNet变体/ResNeXt/WideNet/PyramidNet', 'DenseNet/密集连接', 'Inception模块/GoogLeNet', 'EfficientNet/复合缩放', '目标检测/YOLO/Faster RCNN/SSD', 'Anchor机制/Anchor Free', 'NMS/非极大值抑制', 'mAP/IoU/检测评估', '图像分割/U-Net/Mask RCNN/DeepLab', '语义分割/实例分割', '全卷积网络/FCN/FCN-8s', '循环神经网络RNN/LSTM/GRU', '门控机制/Gate', '梯度裁剪/Gradient Clipping', '序列到序列/Seq2Seq', 'Attention机制/注意力', 'Bahdanau Attention/Luong Attention', 'Self-Attention/自注意力', 'Multi-Head Attention', 'Transformer架构/Encoder-Decoder', 'Positional Encoding', 'BERT/双向编码器', 'GPT/生成式预训练', 'GPT-2/GPT-3/GPT-4', 'T5/Text-to-Text', 'ViT/Vision Transformer', 'Swin Transformer', 'CLIP/对比学习', 'Diffusion Model/扩散模型', 'DDPM/DDIM/采样', 'VAE/变分自编码器', 'GAN/生成对抗网络', 'WGAN/条件GAN', 'StyleGAN/ProGAN', '自监督学习/SimCLR/MoCo/SimSiam', '对比学习', '表示学习/表征学习', '度量学习/Metric Learning', '元学习/MAML/Prototypical Networks', '图神经网络/GNN/GCN/GAT', '神经架构搜索/NAS/AutoML']
                },
                '自然语言处理': {
                    'desc': '文本分类、序列标注、文本生成等NLP任务',
                    'difficulty': 3,
                    'dimensions': ['NLP基础/分词/词性标注/POS', '中文分词/Jieba/HanLP/LTP', '分词挑战/歧义/新词发现', '词性标注/宾州词性/CTB', '命名实体识别/NER/BIO标注', 'NER工具/SpaCy/HanLP', '词向量/Word2Vec/CBOW/Skip-gram', 'GloVe/全局词向量', 'FastText/子词嵌入', 'ELMo/上下文词向量', 'BERT/预训练/微调', 'RoBERTa/ALBERT/DistilBERT', 'GPT/生成式/自回归', 'GPT-2/可控生成', 'GPT-Neo/GPT-J/GPT-3/Codex', 'ChatGPT/InstructGPT/RLHF', 'LLM/大语言模型', 'T5/Text-to-Text', 'BART/去噪自编码', '命名实体识别/BERT+CRF', '文本分类/BERT/TextCNN', '情感分析/Aspect级/观点挖掘', '文本生成/seq2seq/Beam Search', '文本生成/采样/温度/top-k/top-p', '机器翻译/Transformer/注意力', 'Seq2Seq/编码器-解码器', 'Attention注意力机制', 'Transformer/位置编码/残差', '文本摘要/抽取式/生成式', '问答系统/阅读理解/MRC', '对话系统/检索式/生成式', '意图识别/槽位填充', '语义匹配/DSSM/SimBERT', '文本相似度/余弦/欧式', 'Sentence-BERT', '主题模型/LDA/PLSA', '主题模型/Neural Topic Model', '关键词提取/TextRank/TF-IDF', '信息抽取/关系抽取/事件抽取', '知识图谱/实体链接/实体消歧', '文本纠错/拼写检查', '文本预处理/清洗/标准化', '数据增强/回译/同义词替换', 'NLP评估指标/BLEU/ROUGE/METEOR', '模型蒸馏/DistilBERT', '模型压缩/量化/剪枝', '少样本学习/Prompt/P-tuning', '提示工程/Prompt Engineering', 'Few-shot/Zero-shot', 'In-context Learning', 'Chain-of-Thought', 'RLHF/人类反馈强化学习', 'LLM部署/量化/GPTQ/GGML', 'LangChain/工具调用']
                },
                '计算机视觉': {
                    'desc': '图像分类、目标检测、图像分割等视觉任务',
                    'difficulty': 3,
                    'dimensions': ['图像基础/像素/通道/分辨率', '图像格式/RGB/BGR/灰度', '图像读取/OpenCV/PIL', '图像预处理/归一化/标准化', '图像增强/翻转/旋转/裁剪', '颜色空间/HSV/Lab', '直方图/均衡化', '滤波/均值/高斯/中值/双边', '边缘检测/Sobel/Canny/Laplacian', '霍夫变换/直线检测/圆检测', '图像分割/阈值分割', '图像分割/GrabCut/分水岭', '形态学/腐蚀/膨胀/开运算/闭运算', '特征检测/角点/斑点', 'SIFT/SURF/ORB', '特征匹配/Brute Force/FLANN', '图像配准/全景拼接', '目标检测/两阶段/Faster RCNN', '目标检测/单阶段/YOLO/SSD', 'Anchor机制/Anchor Free', 'NMS/Soft-NMS', 'mAP/IoU评估', 'YOLO v1-v8系列', 'Faster RCNN/Mask RCNN', 'RetinaNet/Focal Loss', '图像分割/语义分割', '语义分割/FCN/U-Net/DeepLab', '实例分割/Mask RCNN/Panoptic', '全景分割/Panoptic FPN', '人脸检测/MTCNN/RetinaFace', '人脸识别/FaceNet/ArcFace', '人体姿态估计/关键点检测', '图像分类/AlexNet/VGG/ResNet', 'ResNet/DenseNet/Pre-activation', '轻量化网络/MobileNet/SqueezeNet', 'EfficientNet/复合缩放', '注意力机制/SE/SK/Non-Local', 'Vision Transformer/ViT', 'Swin Transformer', 'CLIP/对比视觉语言', '超分辨率/ESRGAN/SRResNet', '图像去噪/DnCNN/BM3D', '图像去模糊/DeepDeblur', '图像修复/Inpainting/GAN', '风格迁移/Neural Style', 'GAN/生成对抗/DCGAN', 'CycleGAN/风格迁移', 'Diffusion Model/图像生成', 'DDPM/稳定扩散/SD', '图像编辑/ControlNet/T2I', '3D视觉/点云/NeRF', '目标跟踪/SORT/DeepSORT', 'OCR/文字识别/CRNN', '场景文字识别/STR']
                }
            }
        },
        '数据科学家': {
            'description': '通过数据分析挖掘业务价值，建立数据模型支持决策。',
            'skills': {
                'NumPy': {
                    'desc': '数值计算和矩阵运算',
                    'difficulty': 1,
                    'dimensions': ['NumPy基础/ndarray/数组创建', '数据类型/int/float/complex/bool', '数组索引/切片/布尔索引', '数组形状/reshape/flatten', '数组运算/加减乘除/矩阵乘法', '广播机制/Broadcast', '聚合函数/sum/mean/std/max/min', '排序/sort/argsort', '拼接/stack/concatenate/vstack/hstack', '分割/split/vsplit', '复制/copy', '向量化/ufunc', '数学函数/sin/cos/exp/log', '随机数/randn/randint/shuffle', '线性代数/eigenvalue/svd/dot', '范数/linalg.norm', '行列式/linalg.det', '逆矩阵/linalg.inv', '解线性方程/linalg.solve', '傅里叶变换/fft', '文件IO/savetxt/loadtxt', '性能优化/向量化']
                },
                'Pandas': {
                    'desc': '数据清洗、转换和分析',
                    'difficulty': 1,
                    'dimensions': ['Pandas基础/Series/DataFrame', '数据读取/read_csv/read_excel', '数据查看/head/tail/info/describe', '数据选择/loc/iloc', '布尔索引/条件筛选', '缺失值/isnull/fillna/dropna', '数据替换/replace', '数据排序/sort_values', '数据合并/concat/merge', '分组groupby/agg/apply', '透视表pivot_table', '字符串操作/str', '日期时间/to_datetime', '时间序列/resample/shift', '窗口函数/rolling/expanding', '数据去重/duplicated', '数据映射/map/apply', '类型转换/astype', '重命名rename', '索引操作/set_index', '文件保存/to_csv/to_excel', '性能优化']
                },
                'Python/R': {
                    'desc': '数据分析和建模的主要工具语言',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/控制流/函数', '列表/字典/集合推导式', 'Python科学计算/numpy/scipy', 'Pandas数据处理', 'Matplotlib可视化', 'Seaborn统计图', 'Plotly交互图表', 'Scikit-learn机器学习', 'Jupyter Notebook', 'R基础/向量/矩阵/数据框', 'R数据处理/dplyr/tidyr', 'R可视化/ggplot2', 'R统计建模/lm/glm', 'R tidyverse生态', 'Python与R互转', 'Python环境管理/conda', 'Python包管理/pip', 'R包管理/install.packages', '数据科学工作流', '代码规范/PEP8']
                },
                'SQL': {
                    'desc': '从数据库中提取和处理数据',
                    'difficulty': 1,
                    'dimensions': ['SQL基础/SELECT/FROM/WHERE', '条件查询/AND/OR/NOT', '排序/ORDER BY/ASC/DESC', '去重/DISTINCT', '聚合函数/COUNT/SUM/AVG/MIN/MAX', '分组/GROUP BY/HAVING', '子查询/嵌套查询', '表连接/INNER/LEFT/RIGHT/FULL', 'UNION/UNION ALL', '窗口函数/OVER/PARTITION BY', '排名函数/ROW_NUMBER/RANK/DENSE_RANK', 'LAG/LEAD偏移函数', 'WITH语句/CTE公用表表达式', '数据插入/INSERT', '数据更新/UPDATE', '数据删除/DELETE', '表创建/CREATE TABLE', '约束/主键/外键/唯一/非空', '索引/INDEX/CREATE INDEX', '视图/VIEW', '存储过程/PROCEDURE', '触发器/TRIGGER', '事务/BEGIN/COMMIT/ROLLBACK', 'MySQL语法', 'PostgreSQL语法', 'HiveQL', 'Spark SQL', 'SQL优化/EXPLAIN', '慢查询分析', '索引设计', '查询改写']
                },
                'A/B测试': {
                    'desc': '设计实验评估产品改动效果',
                    'difficulty': 2,
                    'dimensions': ['A/B测试原理/对照组/实验组', '实验设计/随机分组', '样本量计算/统计功效', '显著性检验/t检验/p值', '置信区间/95%置信度', '分流策略/均匀分流', '分流算法/hash分流', '实验周期/样本量', '指标选择/北极星指标', '数据埋点/事件上报', '效果评估/提升度', '方差分析/ANOVA', '分层抽样', 'AA测试', '多重比较校正', '辛普森悖论', '新奇效应', '因果推断', '倾向得分匹配/PSM', '双重差分/DID', '在线实验平台', '灰度发布', '特征开关', 'AB测试框架']
                },
                'Tableau/Power BI': {
                    'desc': '商业智能工具制作交互式仪表板',
                    'difficulty': 2,
                    'dimensions': ['Tableau基础/工作表/仪表板', '数据连接/Live/Extract', '数据源连接/Excel/SQL/CSV', '维度/度量字段', '图表类型/柱状图/折线图/饼图/散点图', '计算字段/LOD表达式', '表计算/Window函数', '参数/参数过滤器', '筛选器/上下文筛选', '排序/分组', '仪表板布局/平铺/浮动', '交互操作/动作筛选/高亮', '配色方案/主题', 'Tableau Prep/数据清洗', 'Tableau Server/发布', 'Tableau Online', '权限管理', '数据刷新/计划刷新', 'Power BI基础/报表/数据集', 'Power Query/数据转换', 'DAX公式', '度量值/计算列', 'Power BI Desktop', 'Power BI Service', 'Power BI Embedded', '行级安全/RLS', '网关配置', '数据流/Dataflow', '增量刷新', '分享协作', 'Power BI移动端']
                },
                '业务理解': {
                    'desc': '将业务问题转化为数据问题',
                    'difficulty': 2,
                    'dimensions': ['业务分析/业务流程', '指标体系/AARRR/海盗模型', '北极星指标', '指标拆解/指标下钻', 'OMTM唯一关键指标', '用户画像/标签体系', '用户分层/RFM模型', '用户生命周期', '转化漏斗', '业务模型/C2C/B2C/B2B/SaaS', '商业模式画布', '行业知识/电商/金融/教育', '业务需求沟通', '需求分析/PRD', '需求优先级/RICE/ICE', '业务指标监控', '指标异常分析', '归因分析', '数据字典', '数据资产', '数据治理', '指标一致性', '数据口径', '业务问题定义', '数据假设验证', 'AB实验设计', '业务迭代评估']
                },
                '探索性数据分析': {
                    'desc': '使用统计方法和可视化理解数据分布',
                    'difficulty': 2,
                    'dimensions': ['EDA概述/目的/方法', '数据概览/shape/info/describe', '缺失值分析/可视化', '数据类型检查', '数值变量分布/hist/distplot', '类别变量分布/countplot/bar', '分布特征/正态/偏态/峰度', '集中趋势/均值/中位数/众数', '离散程度/方差/标准差/四分位', '相关性分析/heatmap/corr', '变量关系/scatter/matrix', '分组分析/groupby', '交叉表分析', '时间序列趋势', '异常值检测/IQR/Z-score', '箱线图/boxplot', '小提琴图/violinplot', '密度图/kdeplot', '热力图/heatmap', '配对图/pairplot', 'QQ图/正态性检验', '数据质量报告', '假设生成', '探索结论总结', '可视化故事化', '业务含义解读']
                },
                '数据可视化': {
                    'desc': '使用Matplotlib、Seaborn、Plotly展示数据洞察',
                    'difficulty': 2,
                    'dimensions': ['Matplotlib基础/figure/axes', '折线图/plot', '散点图/scatter', '柱状图/bar/barh', '直方图/hist', '箱线图/boxplot', '饼图/pie', '热力图/heatmap', '子图/subplot/subplots', '坐标轴设置/labels/title/legend', '颜色/Colormap', '样式/style', '中文显示/字体配置', '保存图片/figsize/dpi', 'Seaborn基础/set_style', 'Seaborn分布图/distplot/kdeplot', 'Seaborn关系图/relplot', 'Seaborn分类图/catplot', 'Seaborn回归图/lmplot', 'Seaborn热力图/clustermap', 'Plotly交互图表', 'Plotly Express/px', 'Plotly图形对象/go', 'Plotly子图make_subplots', 'Plotly导出html', 'Dashboard制作', '地理可视化/地图', '动态图表/动画', '图表配色/主题', '图表优化技巧', '数据故事化', '可视化原则', '配色心理学', '图表选择指南']
                },
                '数据报告': {
                    'desc': '撰写数据分析报告，提供决策建议',
                    'difficulty': 2,
                    'dimensions': ['报告结构/背景/方法/结论/建议', '报告类型/周报/月报/专题报告', 'Executive Summary', '报告受众/管理层/业务方', '数据来源说明', '指标定义/数据口径', '分析方法说明', '图表选择/数据故事', '结论提炼', '行动建议', '风险提示', '附录/数据字典', 'PPT制作技巧', '数据讲故事', '自动化报告', '邮件报告', '钉钉/飞书推送', '数据门户', '看板/Dashboard', 'PowerPoint导出', 'Word报告', 'Markdown报告', 'Jupyter报告', '可视化报告', 'PDF导出', 'HTML报告', '报告模板', '报告审核', '数据更新', '报告分发']
                },
                '数据清洗': {
                    'desc': '处理缺失值、异常值、重复数据',
                    'difficulty': 2,
                    'dimensions': ['缺失值识别/isnull/sum', '缺失值原因分析', '删除法/dropna', '均值填充/中位数填充', '众数填充', '前向填充/后向填充', '插值法/interpolate', '模型预测填充/KNN/回归', '缺失值指示变量', '异常值识别/Z-score/IQR', '异常值处理/删除/替换', '盖帽法/Winsorization', '重复值检测/duplicated', '删除重复行', '文本清洗/去空格/大小写', '特殊字符处理', '日期格式标准化', '数据类型转换', '格式统一', '编码问题/乱码处理', '数据合并/主键对齐', '宽表长表转换', '数据拆分', '数据脱敏', '数据采样', '数据不平衡处理', 'Python清洗/pandas', 'R清洗/tidyr', 'SQL数据清洗', '数据质量框架', '数据清洗流程']
                },
                '机器学习': {
                    'desc': '构建预测模型和分类模型',
                    'difficulty': 2,
                    'dimensions': ['机器学习流程/数据准备/特征/建模/评估', '线性回归/最小二乘法', '逻辑回归/分类', '决策树/ID3/CART', '随机森林/Bagging', '梯度提升/XGBoost/LightGBM', '支持向量机/SVM', 'K近邻/KNN', '朴素贝叶斯/Naive Bayes', '聚类/K-Means/层次聚类/DBSCAN', '降维/PCA/ t-SNE', '模型评估/交叉验证', '过拟合/欠拟合', '正则化/L1/L2', '超参数调优/GridSearchCV', '特征选择', '特征重要性', '分类指标/Accuracy/Precision/Recall/F1', '回归指标/MSE/RMSE/MAE/R2', 'ROC曲线/AUC', '混淆矩阵', '留出法/训练集测试集', 'K折交叉验证', 'Scikit-learn API', 'Python建模', 'R建模/caret', 'AutoML/automl', '模型选择', '模型集成/Stacking', '时间序列预测']
                },
                '特征工程': {
                    'desc': '构建和选择对模型有用的特征',
                    'difficulty': 2,
                    'dimensions': ['特征工程概述', '数值特征标准化/Z-score/MinMax', '数值特征分箱/等距/等频', '类别特征编码/One-Hot/Label', '目标编码/Target Encoding', '特征组合/交叉特征', '时间特征/年/月/日/星期', '聚合特征/groupby统计', '文本特征/TF-IDF', '文本特征/词向量', '缺失值特征', '异常值特征', '特征选择/方差阈值', '特征选择/相关性', '特征选择/模型重要性', '特征选择/递归消除', '特征提取/PCA/SVD', '特征交互/乘法/除法', '比例特征', '差值特征', '统计特征', '滑动窗口特征', '用户特征/画像', '物品特征', '行为特征', '交叉特征', '特征监控', '特征上线', '特征回填', '特征版本管理', '离线特征/在线特征']
                },
                '统计学': {
                    'desc': '假设检验、回归分析、时间序列分析等统计方法',
                    'difficulty': 2,
                    'dimensions': ['描述性统计/均值/中位数/众数', '离散程度/方差/标准差/变异系数', '分布形状/偏度/峰度', '概率分布/正态分布/二项分布/泊松分布', '中心极限定理', '置信区间/置信水平', '假设检验/t检验/z检验', 'p值/显著性水平', '第一类错误/第二类错误', '功效分析/样本量计算', '方差分析/ANOVA/单因素/双因素', '协方差/相关系数/Pearson/Spearman', '简单线性回归', '多元线性回归', '回归诊断/残差分析', '多重共线性/VIF', '异方差检验', '自相关检验', '逻辑回归/对数几率回归', '分类模型评估', '时间序列基础/趋势/季节/周期', '时间序列分解', '移动平均/指数平滑', 'ARIMA模型', 'SARIMA/季节性ARIMA', '趋势检验/Mann-Kendall', '季节性检验', '白噪声检验/LB检验', '平稳性检验/ADF检验', 'Granger因果检验', '协整检验', '时间序列预测', '预测置信区间', '非参数统计', '贝叶斯统计/先验/后验', '贝叶斯推断', 'AB测试统计', '多重比较校正']
                }
            }
        },
        'NLP工程师': {
            'description': '开发自然语言处理应用，如文本分类、情感分析、机器翻译等。',
            'skills': {
                'Jieba': {
                    'desc': '中文分词工具，支持自定义词典',
                    'difficulty': 1,
                    'dimensions': ['Jieba分词模式/精确模式/全模式/搜索模式', '分词API/cut/cut_for_search', '并行分词jieba.enable_parallel', '词性标注/posseg', '关键词提取/jieba.analyse.extract_tags', 'TF-IDF关键词/TFIDF', 'TextRank关键词', '停用词/自定义词典', '加载词典/add_word/disable_word', 'Tokenize/返回词在原文位置', 'Chinese Sentence Breaking', '繁简转换', '拼音转换/pypinyin', '正则表达式支持', '自定义分词器', 'PaddlePaddle模式/深度学习', '词性标注集/ICTPOS/863POS', '命名实体识别/NER', '新词发现', '分词速度优化', 'Python集成/import jieba', '批量分词', '分词结果处理', '词频统计', '自定义词典格式', '词典优先级', '融合数字/英文处理']
                },
                'NLTK': {
                    'desc': '自然语言处理工具包，提供文本处理基础功能',
                    'difficulty': 1,
                    'dimensions': ['NLTK基础/语料库/Corpus', 'NLTK安装/download', '语料库下载/nltk.download', '文本分词/tokenize/word_tokenize', '句子分割/sent_tokenize', '词干提取/stem/PorterStemmer/LancasterStemmer', '词形还原/lemmatize/WordNetLemmatizer', '词性标注/pos_tag', 'POS标注集/Penn Treebank', '命名实体识别/named entity', '停用词/stopwords', '频率分布/FreqDist', '条件频率分布/ConditionalFreqDist', 'N-gram模型/unigram/bigram/trigram', 'BigramAssocMeasures/TrigramAssocMeasures', '搭配提取/collocations', 'WordNet/同义词/反义词/上位词/下位词', '语义相似度/synset/path_similarity', '文本分类/NaiveBayesClassifier', '情感分析/SentimentAnalyzer', '情感词典/vader', '分块/chunking/Shallow Parsing', '树结构/Named Entity Chunk', '语法树解析/Tree/ParentedTree', '依存分析/Dependency Parsing', '语义标注/Semgram', '语料库Brown/Corpus', '语料库CNKI', '自定义语料库', '文本检索/search', '文本相似度/text_distance', '信息抽取/IE', 'WordNet接口', '资源加载器/CorpusReader', '数据分割/train_test_split', '朴素贝叶斯/NLTKClassify', 'Maxent Classifier', '序列标注/IOB编码', 'SVM集成', 'Scikit-learn集成']
                },
                'Python': {
                    'desc': 'NLP开发的主要编程语言',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/控制流', '字符串处理/正则/re模块', '文件IO/读写文本', '列表/字典/集合操作', '函数定义/参数/返回值', '列表推导式/生成器', '异常处理/try-except', '面向对象/类/继承', 'NumPy数组操作', 'Pandas数据处理', 'Matplotlib可视化', 'Scikit-learn机器学习', 'Jupyter Notebook', 'pip包管理', '虚拟环境/venv', 'Python类型提示', '装饰器/@wraps', '上下文管理器/with', '迭代器/Iterator', '日志logging', '单元测试/unittest', '字符串格式化', 'JSON处理', '编码问题/UTF-8', '日期时间处理', '多线程/asyncio', 'HTTP请求/requests', 'API调用', '数据清洗', '正则表达式', 'Lambda表达式', '匿名函数']
                },
                'spaCy': {
                    'desc': '工业级NLP库，提供高效的文本处理流水线',
                    'difficulty': 1,
                    'dimensions': ['spaCy基础/nlp对象/Pipeline', '分词/Tokenization', '词性标注/POS Tagging', '依存分析/Dependency Parsing', '命名实体识别/Named Entity Recognition', '实体类型/PERSON/ORG/GPE/LOC', '句子边界检测/Sentence Segmentation', '词形还原/Lemmatization', '词向量/Word Vectors/span.similarity', '相似度计算/doc.similarity/span.similarity', '词语搭配/Collocation', '多语言支持/en/zh', '预训练模型/en_core_web_sm/lg/xl', '自定义流水线/Component', '自定义分词器/Tokenizer', '自定义属性扩展/Extension Attributes', '规则匹配/Rule-based Matching', 'PhraseMatcher', 'EntityRuler', '正则匹配/Pattern', ' Matcher/PhraseMatcher', '词性模式/LemmaPattern', '依存模式/DEP Pattern', '实体模式/Entity Pattern', '训练数据标注/Annotation', '训练数据格式/JSONL', '训练模型/Train', '评估/evaluate', '模型打包/model package', '模型加载/spacy.load', '工厂方法/create_pipe', '管道组件/nlp.add_pipe', '实体链接/Entity Linking', '核心ference Resolution', '文本分类/TextCategorizer', 'SentencePiece集成', 'PyTorch集成/Thinc', ' transformers集成', '词向量训练', '在线学习/online learning']
                },
                'BERT': {
                    'desc': 'Google双向编码器表示模型，用于文本理解',
                    'difficulty': 2,
                    'dimensions': ['BERT基础/Transformer架构/双向编码', 'BERT输入/Token/Piece分词', 'Tokenization/BERT Tokenizer', 'Position Embedding', 'Segment Embedding', 'MLM任务/遮蔽语言模型', 'NSP任务/下一句预测', '预训练/BERT-LARGE/BERT-BASE', '中文BERT/bert-base-chinese', 'RoBERTa/动态遮蔽', 'ALBERT/参数共享', 'DistilBERT/蒸馏', 'TinyBERT/知识蒸馏', 'ERNIE/知识增强', 'MacBERT/MLM as correction', 'XLNet/置换语言模型', 'Hugging Face Transformers', '模型加载/AutoModel', '分词器/AutoTokenizer', '特征提取/BERTEmbedding', '文本分类/BERTForSequenceClassification', '命名实体识别/BERTForTokenClassification', 'BERT+CRF/NER', 'BERT+CNN/文本分类', 'BERT+BiLSTM', 'Fine-tuning/微调', '微调参数/learning_rate/epoch', '微调数据处理', '梯度累积', '早停策略', '学习率调度', 'Text Classification', 'Sentence Pair Classification', 'Question Answering', 'Question Answering Squad', 'BERT模型部署', 'BERT-as-service', 'ONNX导出', 'TensorRT加速', '模型压缩/剪枝/量化', 'BERT在搜索中的应用', 'BERT在推荐中的应用', 'Sentence BERT/SBERT', '对比学习/SimCSE']
                },
                'GPT': {
                    'desc': 'OpenAI生成式预训练模型，用于文本生成',
                    'difficulty': 2,
                    'dimensions': ['GPT基础/Transformer Decoder', 'GPT-1/改进的Transformer', 'GPT-2/更大模型/多任务', 'GPT-3/In-context Learning', 'GPT-3.5/Turbo/ChatGPT', 'GPT-4/多模态/更长上下文', 'GPT-4V/视觉', 'GPT-4 Turbo', 'GPT-o1/推理模型', '自回归生成/Autoregressive', 'Causal Language Modeling', 'Transformer架构/Decoder Only', '注意力掩码/Causal Mask', 'Position Encoding/Rotary', '分词器/Tokenizer', 'OpenAI API/Completions', 'Chat Completion API', 'API Key/认证', 'Temperature/随机性', 'Top-p采样/nucleus sampling', 'Max Tokens/生成长度', 'Stop Sequences', 'Streaming/流式输出', 'JSON Mode/response_format', 'Function Calling', 'Tokens计数', 'Embedding API', 'Fine-tuning/微调', '微调数据格式/JSONL', '微调成本计算', 'Prompt工程/Best Practices', 'Few-shot Learning', 'Zero-shot Learning', 'Chain-of-Thought', 'System Message/系统提示', 'User Message/用户消息', 'Assistant Message/助手消息', 'Token计算', '上下文长度/Context Length', 'GPT在对话系统', 'GPT在写作助手', 'GPT在代码生成', 'GPT在数据分析', 'GPT安全/内容过滤', 'GPT局限性/幻觉', 'LangChain集成', 'Llama/开源GPT']
                },
                'Prompt工程': {
                    'desc': '设计有效的提示词引导模型输出',
                    'difficulty': 2,
                    'dimensions': ['Prompt基础/提示词结构', 'Prompt组件/指令/上下文/输入/输出', '零样本Prompt/Zero-shot', '少样本Prompt/Few-shot', '示例选择/Example Selection', '示例格式/Example Format', 'Chain-of-Thought/思维链', 'Self-Consistency/自洽性', 'Tree of Thoughts/思维树', 'Prompt模板/Template', 'Prompt压缩', 'Prompt版本管理', 'Temperature/温度参数', 'Top-p采样', 'Top-k采样', 'Max Tokens/最大token', 'Stop Sequences/停止词', 'System Prompt/系统提示', 'User Prompt/用户提示', 'Few-shot Examples', 'In-context Learning', '角色扮演/Role Prompting', '格式化输出/JSON/XML', '任务分解/Step-by-step', '指定步骤/First...Then', '指定格式/输出格式', '约束条件/Constraints', '反面Prompt/Negative Prompt', '迭代优化/Iterative', 'Prompt注入攻击', 'Prompt安全', '角色设定/Role Setting', '风格控制/Style Control', '情感控制', '长度控制', '简洁性Prompt', '详细性Prompt', '问句Prompt', '陈述句Prompt', '代码Prompt', '数学Prompt', '推理Prompt', '创意Prompt', '分析Prompt', 'Multi-modal Prompt', 'Image Prompt', 'Video Prompt', 'Audio Prompt']
                },
                'Transformers': {
                    'desc': 'Hugging Face提供的预训练模型库',
                    'difficulty': 2,
                    'dimensions': ['Transformers库基础/AutoClass', 'AutoModel/AutoTokenizer', 'Pipeline/推理Pipeline', '预训练模型/BERT/GPT/RoBERTa', '模型加载/save_pretrained', '模型共享/Hub上传', 'Tokenizer/分词器', '分词器训练/train_new_from_iterator', 'Tokenization/编码解码', 'Truncation/Padding', 'Attention Mask', 'Position IDs', '模型配置/Config', 'Config.save_pretrained', 'BERT模型/BertModel/BertForSequenceClassification', 'GPT模型/GPT2Model/GPT2LMHeadModel', 'T5模型/T5ForConditionalGeneration', 'BART模型/BartModel', 'RoBERTa模型/RoBERTaModel', 'XLNet模型/XLNetModel', 'ALBERT模型/AlbertModel', 'DistilBERT模型', '模型Fine-tuning', 'Trainer API', 'TrainingArguments', 'Trainer.train', 'Trainer.evaluate', 'Trainer.predict', '数据收集器/DataCollator', '数据处理/Map Dataset', '批处理/Batch', '优化器/AdamW', '学习率调度器/Scheduler', '梯度累积/Gradient Accumulation', '混合精度/FP16/BF16', '分布式训练/Distributed', '多GPU训练/Multi-GPU', 'ONNX导出/ORT', 'TorchScript导出', 'TensorFlow模型', 'Flax/JAX模型', 'Tokenizer定制', '自定义模型/PreTrainedModel', '模型注册/Registry', 'Feature Extractors', 'Image Processors', 'Audio Processors', 'Text Generation/文本生成', 'Fill-Mask/完形填空', 'Question Answering/问答', 'Sentence Similarity/句子相似度', 'Feature Extraction/特征提取', 'Summarization/摘要', 'Translation/翻译', 'Text Classification/文本分类', 'Token Classification/Token分类']
                },
                '序列标注': {
                    'desc': '命名实体识别、词性标注',
                    'difficulty': 2,
                    'dimensions': ['序列标注任务/Named Entity Recognition', 'NER任务类型/NER/POS/Chunking', 'BIO标注/B-实体/I-实体/O', 'BMES标注/B-Middle-End-Start', 'BIOES标注/Single/Begin/Inside/Outside/End', '词性标注集/Penn Treebank/ICTPOS', '词性标注/POS Tagging', '中文词性/863词性/北大词性', '命名实体类型/PER/LOC/ORG/TIME/MONEY', '嵌套命名实体/Nested NER', '嵌套实体处理', '中文分词与NER联合', 'CRF/条件随机场', 'BiLSTM-CRF', 'BERT-CRF/NER', 'BERT-BiLSTM-CRF', 'LightNER/高效NER', 'GlobalPointer/全局指针', 'TPLinker/联合抽取', '苏格拉底/多任务学习', '预训练模型/BERT/BERT-CRF', 'RoBERTa-CRF', 'MacBERT-CRF', '数据标注/BIO标注', '标注工具/Brat/doccano', '标注质量控制', '数据增强/回译/同义词', '错误分析/Error Analysis', 'F1分数/评估指标', 'CoNLL评估', '模型推理/Pipeline', '在线预测', '批处理预测', 'NER后处理', '实体链接/Entity Linking', '实体消歧/Entity Disambiguation', '知识库/Knowledge Base', 'NER在搜索/Named Entity in Search', 'NER在问答', 'NER在对话', '金融NER/医疗NER/法律NER', '嵌套NER/Flat NER']
                },
                '文本分类': {
                    'desc': '情感分析、主题分类、意图识别',
                    'difficulty': 2,
                    'dimensions': ['文本分类任务/Text Classification', '二分类/多分类/多标签', '情感分析/Sentiment Analysis', '情感极性/正面/负面/中性', '细粒度情感/Fine-grained Sentiment', '方面情感/Aspect-based Sentiment', '主题分类/Topic Classification', '新闻分类/News Classification', '意图识别/Intent Detection', '垃圾邮件检测/Spam Detection', '仇恨言论检测/Hate Speech', '虚假新闻检测/Fake News', '评论审核/Content Moderation', '传统方法/TF-IDF+SVM', 'TextCNN/卷积神经网络', 'TextRNN/LSTM/GRU', 'BiLSTM/双向LSTM', 'Attention机制/文本分类', 'BERT/预训练微调', 'RoBERTa/ERNIE微调', 'XLNet/Transformer-XL', 'GPT分类/生成式分类', 'Sentence-BERT/相似度分类', 'Few-shot分类/Prompt Learning', 'Zero-shot分类/BART', '数据标注/Label Studio', '标注工具/doccano', '标注质量/标注指南', '数据增强/EDA/回译', '数据不平衡/过采样/欠采样', '类别权重', 'F1/Accuracy/Precision/Recall', '混淆矩阵分析', 'Cross Validation', '分层采样/Stratified', '模型选择/对比实验', '特征重要性/LIME/SHAP', 'CNN vs RNN vs Transformer', '在线学习/增量学习', '部署/TorchServe', 'ONNX Runtime', 'FastAPI服务', '模型压缩/知识蒸馏']
                },
                '文本生成': {
                    'desc': '机器翻译、摘要生成、对话系统',
                    'difficulty': 2,
                    'dimensions': ['文本生成任务/Text Generation', '语言模型/Language Model', 'GPT/Decoder-only生成', 'T5/Seq2Seq生成', 'BART/去噪生成', 'CTRL/Conditional Generation', '机器翻译/Machine Translation', '统计机器翻译/SMT', '神经机器翻译/NMT', 'Seq2Seq/Encoder-Decoder', '注意力机制翻译', 'Transformer翻译', 'BLEU评分/翻译评估', '摘要生成/Summarization', '抽取式摘要/Extractive', '生成式摘要/Abstractive', 'TextRank摘要', 'Lead-3摘要', 'Pointer-Generator网络', '预训练摘要/BERTsum', '对话生成/Dialogue Generation', '开放域对话', '任务导向对话', '检索式对话', '生成式对话', 'Seq2Seq对话', 'GPT对话', 'ChatGLM/开源对话', '代码生成/Code Generation', 'Copilot/GitHub', '诗歌生成/Story Generation', '歌词生成', '文案生成', '文本改写/Paraphrasing', '文本续写/Text Completion', 'Beam Search/束搜索', 'Greedy Decoding', 'Sampling/随机采样', 'Top-k Sampling', 'Top-p Sampling/Nucleus', 'Temperature采样', 'Repetition Penalty', 'Length Penalty', 'Coverage Penalty', '最大似然估计/MLE', '强化学习/RLHF', 'PPO算法/生成优化', '可控生成/Controlled Generation', '风格迁移/Style Transfer', '关键词控制', '长度控制']
                },
                '注意力机制': {
                    'desc': 'Self-Attention、Multi-Head Attention原理',
                    'difficulty': 2,
                    'dimensions': ['注意力机制基础/Attention', '注意力计算/Query/Key/Value', '缩放点积注意力/Scaled Dot-Product', '注意力函数/Attention(Q,K,V)', 'Multi-Head Attention/多头注意力', '自注意力/Self-Attention', '交叉注意力/Cross-Attention', 'Bahdanau Attention/加性注意力', 'Luong Attention/乘性注意力', 'Global Attention/全局注意力', 'Local Attention/局部注意力', '硬注意力/Hard Attention', '软注意力/Soft Attention', '多头数选择/num_heads', '线性变换/W_Q/W_K/W_V', '多头输出拼接/Concat', '线性变换/W_O', '位置编码/Positional Encoding', '绝对位置编码', '相对位置编码/Relative Position', 'RoPE/旋转位置编码', 'ALiBi/线性偏置', '注意力分数计算', 'Mask机制/Masking', 'Padding Mask', 'Sequence Mask/因果掩码', 'Attention Dropout', 'FFN/前馈网络', 'Layer Normalization', 'Residual Connection', 'Transformer Block', 'Encoder/Decoder Attention', 'Transformer Encoder', 'Transformer Decoder', '注意力可视化/Attention Map', '注意力权重分析', '高效注意力/Linear Attention', 'Reformer/LSH Attention', 'Longformer/滑动窗口', 'BigBird/稀疏注意力', 'Flash Attention', 'Sparse Attention', 'CosFormer', 'Performer', '闲聊对话注意力', '机器翻译注意力', '文本分类注意力', '推荐系统注意力']
                },
                '词嵌入': {
                    'desc': 'Word2Vec、GloVe、FastText等词向量技术',
                    'difficulty': 2,
                    'dimensions': ['词嵌入基础/Word Embedding', '分布式假设/Distributional Hypothesis', 'One-hot编码/稀疏向量', '稠密向量/Dense Vector', 'Word2Vec/CBOW', 'Word2Vec/Skip-gram', '负采样/Negative Sampling', '分层Softmax/Hierarchical Softmax', '高频词抽样/Subsampling', 'Skip-gram Negative Sampling/SGNS', 'GloVe/全局词向量', 'GloVe损失函数/共现矩阵', 'FastText/子词嵌入', 'FastText训练/字符ngram', 'Out-of-Vocabulary/OOV', '词向量维度/Embedding Size', '词向量质量评估', '内部评估/相似度/类比', '外部评估/下游任务', '词向量可视化/t-SNE', '词向量可视化/UMAP', '中文词向量/中文分词影响', '预训练中文词向量', '腾讯词向量/搜狗词向量', '词向量微调/Fine-tuning', '词向量归一化', '余弦相似度/欧式距离', '词向量聚合/平均池化', '加权词向量/TF-IDF权重', 'SIF/Smooth Inverse Frequency', '句子向量/Sentence Embedding', 'Doc2Vec/DM/Doc2Vec-DBOW', 'ELMo/上下文词向量', '生僻词处理', '多义词问题', '领域自适应', '跨语言词向量', 'MUSE/对齐词向量', '词向量偏置/Debiasing', '词向量压缩', '词向量聚类', '词向量检索/ANN', 'Faiss向量检索']
                },
                '问答系统': {
                    'desc': '阅读理解、知识图谱问答',
                    'difficulty': 2,
                    'dimensions': ['问答系统概述/Q&A System', '问答任务类型/开放域/限定域', '阅读理解/Machine Reading Comprehension', 'MRC数据集/SQuAD/CMRC', 'MRC评估指标/EM/F1', 'Span抽取式MRC', '机器理解模型/BiDAF', '机器理解模型/QANet', 'BERT MRC/BERT for QA', 'RoBERTa MRC', 'XLNet MRC', '预训练阅读理解', 'DocQA', 'FusionNet', '问答匹配模型/QA Matching', '语义匹配/DSSM', 'ESIM/句子交互', 'BERT句子对分类', '知识图谱问答/KBQA', '知识图谱/Entity/Relation', 'SPARKQL查询', '图数据库/Neo4j', '实体识别+关系抽取', '语义解析/Semantic Parsing', '模板匹配/Rule-based', '意图识别/Intent Detection', '槽位填充/Slot Filling', '对话状态跟踪/DST', '对话策略/Dialogue Policy', '答案排序/Answer Ranking', '多跳推理/Multi-hop', 'HotpotQA/多跳问答', 'Hybrid QA/知识+阅读', '社区问答/CQA', 'FAQ问答', '视频问答/VideoQA', '图片问答/VQA', '表格问答/Table QA', 'Text-to-SQL', 'IR-based QA', 'Dense Retrieval', 'Sparse Retrieval', 'Reader-Retriever', '开放域问答/ODQA', 'Retrospective Reader', 'Generative QA', 'RAG/检索增强生成', 'LLM问答']
                },
                'LLM微调': {
                    'desc': '大语言模型的领域适配和指令微调',
                    'difficulty': 3,
                    'dimensions': ['LLM微调概述/Fine-tuning', '全参数微调/Full Fine-tuning', 'LoRA/低秩适配', 'QLoRA/量化LoRA', 'Adapter/适配器微调', 'Prefix Tuning/前缀微调', 'Prompt Tuning', 'P-tuning v1/v2', 'Frozen/Frozen LM', '知识蒸馏/Distillation', '指令微调/Instruction Tuning', 'SFT/监督微调', 'RLHF/人类反馈强化学习', 'Reward Model/奖励模型', 'PPO算法/近端策略', 'DPO/直接偏好优化', 'ORPO/概率比优化', 'RLAIF/AI反馈', 'KTO/卡尼曼-特沃斯基', '微调数据格式/JSONL', 'Alpaca格式/ShareGPT格式', '数据质量清洗', '数据格式转换', '训练框架/DeepSpeed', '训练框架/HuggingFace PEFT', 'LLaMA-Factory', 'xtuner', '训练超参数/learning_rate', 'Epoch/batch_size', '梯度累积', '混合精度/FP16/BF16', '学习率调度/Warmup', '早停/Early Stopping', 'LoRA配置/rank/alpha', 'LoRA目标模块/q_proj/v_proj', 'lora_dropout', '适配器合并/Merge LoRA', '增量微调/Incremental Tuning', '灾难遗忘/Catastrophic Forgetting', '领域适应/Domain Adaptation', '多任务学习', '参数高效微调/PEFT', 'HuggingFace Trainer', '分布式训练', '模型评估/Benchmark', 'MT-Bench/AlpacaEval', '安全微调/对齐微调', '有毒输出缓解', 'Chat模板/System Prompt']
                },
                'RAG': {
                    'desc': '检索增强生成，结合外部知识库提升回答质量',
                    'difficulty': 3,
                    'dimensions': ['RAG概述/Retrieval-Augmented Generation', 'RAG架构/Retrieve-Read-Generate', '检索模块/Retriever', '生成模块/Generator/LLM', '向量化/Embedding', '文本分割/Chunking/分块', '固定长度分块/Overlap', '语义分块/Semantic Chunking', '文档解析/PDF/Word/HTML', '文档解析/OCR', 'Embedding模型/BERT/Sentence-BERT', 'Embedding模型/OpenAI/text-embedding', 'Embedding模型/bge/m3e', '向量数据库/Vector Database', 'Milvus/Qdrant/Pinecone', 'Chroma/FAISS', '向量检索/近似最近邻/ANN', '余弦相似度/欧式距离', 'Top-k检索', '相似度阈值', '混合检索/Hybrid Search', '稀疏检索+稠密检索', 'BM25/稀疏检索', 'Rerank/重排序', 'Cross-Encoder Rerank', 'Cohere Rerank', '上下文压缩/Context Compression', 'Query Expansion', 'Query改写/Query Rewriting', '多跳推理/Multi-hop RAG', '迭代RAG/Iterative', 'Agentic RAG', 'Self-RAG/自我反思', 'RAG评估/指标/RAGAS', 'RAGAS/Faithfulness', 'RAGAS/Answer Relevancy', 'RAGAS/Context Precision/Recall', '检索增强/Knowledge Retrieval', 'LangChain/RetrievalQA', 'LlamaIndex', 'LlamaIndex/Data Framework', 'RAG优化策略', '索引优化', '查询优化', 'LLM优化', '幻觉缓解', '知识冲突', '时效性问题', 'RAG在问答', 'RAG在摘要', 'RAG在对话', 'RAG在推理', 'Memory增强/RAG in Memory', '表格RAG/TableRAG', '代码RAG/CodeRAG', '多模态RAG']
                },
                '深度学习': {
                    'desc': '神经网络在文本处理中的应用',
                    'difficulty': 3,
                    'dimensions': ['深度学习基础/神经网络/MLP', '激活函数/ReLU/Sigmoid/Tanh', '损失函数/CEE/MSE', '反向传播/Backpropagation', '梯度下降/Gradient Descent', '优化器/SGD/Adam/Momentum', '学习率/Learning Rate', 'Batch Normalization', 'Dropout正则化', 'CNN/TextCNN文本分类', '卷积核/Filter', '池化层/Pooling', 'TextCNN架构', 'RNN/LSTM/GRU', '循环神经网络', 'LSTM/Long Short-Term Memory', 'GRU/Gated Recurrent Unit', 'BiLSTM/双向LSTM', 'Seq2Seq/编码器解码器', '注意力机制/Attention', '机器翻译/Neural MT', 'Transformer/自注意力', '位置编码/PE', '多头注意力/Multi-Head', 'BERT/双向Transformer', 'GPT/自回归GPT', '预训练模型/Pretraining', '微调/Fine-tuning', '词向量/Embedding', '词向量层', '序列填充/Padding', '掩码/Mask', '梯度消失/梯度爆炸', '残差连接/Residual', '层归一化/Layer Norm', '模型初始化/Xavier/He', '正则化/Dropout/L2', 'Text Classification', '序列标注/Named Entity', '文本生成/Text Generation', '文本摘要/Summarization', '问答系统/QA', '情感分析/Sentiment', '神经机器翻译/NMT', '语音识别/ASR', '知识图谱嵌入/KGE', '图神经网络/GNN', '注意力可视化', '模型压缩/Pruning/Quantization', '知识蒸馏/Distillation']
                }
            }
        },
        '计算机视觉工程师': {
            'description': '开发图像和视频处理算法，如目标检测、人脸识别、图像分割等。',
            'skills': {
                'Python': {
                    'desc': '计算机视觉开发的主流语言',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/list/dict/set/tuple/控制流/循环/函数/类/继承/多态', 'NumPy数组操作/np.array/广播/索引/切片/形状变换', 'OpenCV基础/cv2.imread/imwrite/numpy互转', 'PIL/Pillow图像读取/PIL.Image.open/格式转换', 'Matplotlib图像可视化/plt.imshow/子图/保存', '图像处理基础/通道分离/合并/颜色空间转换', 'Scikit-image图像处理/滤波/边缘检测/形态学', '批量图像处理/文件夹遍历/数据增强', '图像读写性能优化/OpenCV vs PIL选择', 'Jupyter Notebook/CVS/Git版本控制', 'NumPy/SciPy科学计算', '多线程图像加载/multiprocessing', 'GPU加速/CUDA基础/PyTorch环境', '深度学习框架/PyTorch/TensorFlow/Keras', 'Jupyter Lab/Colab/GPU云环境']
                },
                'CNN': {
                    'desc': '卷积神经网络，图像特征提取的基础',
                    'difficulty': 2,
                    'dimensions': ['卷积神经网络基础/Convolutional Neural Network', '卷积层/Conv2D/卷积核/Filter/Stride/Padding', '卷积运算/滑动窗口/特征图/Feature Map', 'Padding/Same/Valid填充', 'Stride/步长/降采样', '池化层/Max Pooling/Avg Pooling', '全局平均池化/Global Average Pooling', '全连接层/Fully Connected/FC', '卷积网络结构/LeNet/AlexNet/VGG', '特征图可视化/Feature Map', '感受野/Receptive Field', '1x1卷积/通道降维/升维', '深度可分离卷积/Depthwise Separable', '分组卷积/Group Convolution', '空洞卷积/Dilated/Atrous Conv', '反卷积/转置卷积/Upconvolution', '膨胀系数/Dilation Rate', '权重初始化/Xavier/He初始化', 'Batch Normalization/批归一化', 'Dropout正则化', '梯度消失/梯度爆炸问题', 'ResNet残差连接/Skip Connection', '特征金字塔/Feature Pyramid', '多尺度特征融合', '注意力机制/CBAM/SE-Net', '通道注意力/空间注意力', '特征融合/Add vs Concat', '上采样/下采样', '图像特征提取/Transfer Learning']
                },
                'Keras': {
                    'desc': '高级神经网络API',
                    'difficulty': 2,
                    'dimensions': ['Keras概述/高层神经网络API/TensorFlow集成', 'Sequential模型/序贯模型/线性堆叠', 'Dense层/全连接层/units/activation', 'Activation激活函数/relu/sigmoid/softmax', '编译配置/compile/loss/optimizer/metrics', '优化器/SGD/Adam/RMSprop/Adagrad', '损失函数/binary_crossentropy/categorical_crossentropy/mse', '模型训练/fit/batch_size/epochs/validation_split', 'EarlyStopping早停/patience/monitor', 'ModelCheckpoint保存/best_only', 'ReduceLROnPlateau学习率衰减', '数据生成器/ImageDataGenerator/数据增强', '图像预处理/flow_from_directory/flow_from_dataframe', '数据增强/旋转/翻转/缩放/裁剪/亮度', '回调函数/Callbacks/LambdaCallback', 'TensorBoard可视化/log_dir', '模型评估/evaluate/accuracy/loss', '模型预测/predict/predict_classes', '函数式API/Functional API/多输入输出', '共享层/Shared Layers', '层堆叠/Layer stacking', 'Input层/Input(shape)', 'Model类/自定义模型', 'Lambda层/自定义计算', '正则化/l1/l2/kernel_regularizer', 'Dropout层/Dropout(rate)', 'BatchNormalization层', 'Embedding层/词嵌入', 'LSTM层/GRU层/循环神经网络', 'Conv2D层/Conv1D/Conv3D', 'MaxPooling2D/AvgPooling2D', 'GlobalAveragePooling2D', 'Flatten层/展平', '预训练模型/VGG16/ResNet50/Inception', '迁移学习/Transfer Learning/Fine-tuning', '模型保存/load_model/h5格式', '权重保存/load_weights/save_weights', 'ONNX导出/跨框架部署']
                },
                'OpenCV': {
                    'desc': '开源计算机视觉库，提供图像处理基础功能',
                    'difficulty': 2,
                    'dimensions': ['OpenCV概述/开源计算机视觉库/cv2', '图像读取/imread/flags/灰度/彩色', '图像显示/imshow/namedWindow/waitKey', '图像保存/imwrite/编码格式/质量', '颜色空间/BGR/RGB/HSV/Gray/ LAB', '颜色空间转换/cvtColor', '图像通道/split/merge/通道操作', 'ROI区域/Region of Interest', '图像缩放/resize/插值方法', '图像旋转/warpAffine/getRotationMatrix2D', '图像翻转/flip/轴对称', '图像裁剪/数组切片/Numpy操作', '几何变换/warpAffine/仿射变换', '透视变换/getPerspectiveTransform/warpPerspective', '图像平移/translation', '阈值处理/threshold/固定阈值', '自适应阈值/adaptiveThreshold', 'Otsu大津法/双峰图像', '图像平滑/模糊/均值/高斯/中值', '高斯模糊/GaussianBlur/核大小/ sigma', '中值滤波/medianBlur/椒盐噪声', '双边滤波/bilateralFilter/保边滤波', '形态学/膨胀/腐蚀/opening/closing', '开运算/闭运算/形态学梯度', '结构元素/getStructuringElement', '边缘检测/Sobel/Laplacian/Canny', 'Canny边缘检测/双阈值/边缘连接', '轮廓检测/findContours/drawContours', '轮廓特征/contourArea/arcLength/approxPolyDP', '边界矩形/boundingRect/minAreaRect', '霍夫变换/HoughLines/HoughCircles', '霍夫直线检测/概率霍夫变换', '模板匹配/matchTemplate/matchMask', '直方图/calcHist/归一化', '直方图均衡化/equalizeHist', '2D直方图/颜色直方图', '反向投影/backProject', 'GrabCut交互式分割', 'MeanShift/ camshift追踪', 'ORB/SIFT/SURF特征点检测', '特征描述/ORB/BRIEF/描述子匹配', '视频处理/VideoCapture/ VideoWriter', '摄像头读取/camera/视频流', '图像拼接/stitch/Stitcher', 'DNN模块/deep neural network', '深度学习推理/cv2.dnn.blobFromImage', '人脸检测/dnn.readNet/预训练模型', 'OCR基础/文本检测/文本识别', '去畸变/undistort/remap', '相机标定/calibrateCamera/内参外参']
                },
                'PIL/Pillow': {
                    'desc': 'Python图像处理库',
                    'difficulty': 2,
                    'dimensions': ['Pillow概述/PIL/Image模块', '图像读取/Image.open/文件打开', '图像保存/save/format/png/jpeg', '图像显示/show/默认查看器', '图像模式/mode/RGB/RGBA/L/CMYK', '图像尺寸/size/width/height', '图像转换/convert/灰度/调色板', '缩放/resize/antialias/抗锯齿', 'thumbnail/缩略图/保持比例', '旋转/rotate/expand/填充', '翻转/flip/transpose/旋转', '裁剪/crop/box参数', '粘贴/paste/合并图像', '过滤/Filter/BLUR/CONTOUR/DETAIL', '增强/ImageEnhance/亮度对比度', '点操作/point/像素变换', '变换/transform/AFFINE/PERSPECTIVE', '分离通道/split/合并通道/merge', '通道操作/putpixel/getpixel', '新建图像/new/创建空白图', '画图/draw/ImageDraw/矩形圆形', '绘制文字/draw.text/字体/Font', 'ImageDraw.polygon/多边形', 'ImageFont/truetype/加载字体', 'ImageFilter/高斯模糊/锐化/边缘', 'ImageChops/通道运算/加减乘除', 'ImageStat/统计信息/均值方差', 'ImageOps/自动化图像处理', 'ImageOps.autocontrast/自动对比度', 'ImageOps.equalize/直方图均衡化', 'ImageOps.grayscale/灰度化', 'ImageSequence/序列图像/gif帧', 'ImageSequenceIterator/逐帧迭代', 'GIF动画读取/split/merge', 'PNG透明度/transparency', 'JPEG质量/quality/optimize', '大图像处理/Image.open_lazy', '内存优化/chunksize/tiled', 'NumPy互转/numpy.array/tobytes', '色彩空间/convert/RGB LAB转换']
                },
                'PyTorch': {
                    'desc': '研究友好的深度学习框架',
                    'difficulty': 2,
                    'dimensions': ['PyTorch概述/张量框架/动态计算图', '张量创建/torch.tensor/torch.zeros/ones/rand', '张量属性/shape/dtype/device', '张量操作/view/reshape/squeeze/unsqueeze', '张量运算/加法乘法矩阵运算', 'GPU加速/cuda/torch.device', 'CPU/GPU切换/to(device)', '自动求导/requires_grad/backward', '梯度计算/grad/zero_grad', '优化器/ torch.optim/Adam/SGD', '学习率/lr/learning rate', '损失函数/nn.CrossEntropyLoss/MSELoss', '神经网络/nn.Module/自定义网络', '卷积层/nn.Conv2d/in_channels/out_channels', '池化层/nn.MaxPool2d/AvgPool2d', '全连接层/nn.Linear', '激活层/ReLU/Sigmoid/Softmax', 'Dropout/nn.Dropout/正则化', 'BatchNorm/nn.BatchNorm2d', 'Sequential/ nn.Sequential/容器', '数据加载/DataLoader/dataset', 'Dataset自定义/collate_fn', 'transforms/图像预处理/数据增强', 'ToTensor/Normalize/Resize', 'RandomHorizontalFlip/随机翻转', 'ImageFolder/文件夹数据集', '预训练模型/torchvision.models', 'ResNet/VGG/AlexNet预训练', '迁移学习/微调/ freeze', '模型训练/train/eval模式', '模型保存/torch.save/entire model', '权重保存/state_dict/load_state_dict', '断点续训/checkpoint保存加载', 'GPU训练/batch_size调整', '分布式训练/DistributedDataParallel', 'TorchScript/模型部署', 'ONNX导出/torch.onnx.export', 'torch.jit/即时编译', '混合精度/amp/autocast', '学习率调度/StepLR/CosineAnnealing', 'tensorboard集成/PyTorchProfiler']
                },
                'TensorFlow': {
                    'desc': '深度学习模型训练和部署',
                    'difficulty': 2,
                    'dimensions': ['TensorFlow概述/Google深度学习框架', 'TensorFlow 2.x/Eager Execution', 'Tensor张量/shape/dtype/numpy互转', '变量/ tf.Variable/可训练变量', '操作/tf.add/tf.matmul/运算', '自动求导/GradientTape', '优化器/tf.keras.optimizers/Adam/SGD', '损失函数/tf.keras.losses', '模型构建/Functional API/Sequential', '层/layers.Dense/Conv2D/MaxPooling', '激活函数/relu/sigmoid/softmax/tanh', '正则化/l2_regularizer/Dropout', 'BatchNormalization层', '模型训练/model.fit/batch_size/epochs', '回调函数/Callbacks/EarlyStopping', 'TensorBoard/logs写入', '数据管道/tf.data.Dataset', 'tf.data.Dataset.from_tensor_slices', 'map/prefetch/batch/autotune', '数据增强/tf.image/旋转翻转缩放', '图像预处理/resize/normalize', '图像分类/CIFAR-10/ImageNet', '预训练模型/tf.keras.applications', 'VGG/ResNet/Inception/MobileNet', '迁移学习/Fine-tuning', '模型保存/model.save/h5/SavedModel', '权重保存/load_weights/save_weights', 'TensorFlow Serving/模型部署', 'TensorFlow Lite/移动端部署', 'TensorFlow.js/浏览器部署', 'ONNX导出/跨框架', '分布式策略/MirroredStrategy', '混合精度训练/tf.train.experimental.MixedPrecision', 'TensorFlow Hub/模型复用', 'Keras Tuner/超参数搜索', 'tf.function/图执行优化', '条件计算/tf.cond/if-else', '循环计算/tf.while_loop', '特征列/tf.feature_column', 'Estimator/高级API', 'TFRecord/数据序列化', 'Protobuf格式/数据存储']
                },
                '图像分类': {
                    'desc': '识别图像中的物体类别',
                    'difficulty': 2,
                    'dimensions': ['图像分类任务/Image Classification', '多分类/Multi-class Classification', '二分类/Binary Classification', '多标签分类/Multi-label', '数据集/CIFAR-10/100/ImageNet/Caltech', '数据划分/Train/Val/Test', '数据增强/旋转翻转/色彩变换/几何变换', 'Mixup/CutMix数据增强', '标签平滑/Label Smoothing', 'LeNet-5/手写数字识别', 'AlexNet/ImageNet突破', 'VGGNet/VGG16/VGG19', 'GoogLeNet/Inception模块', 'Inception V1-V4/1x1卷积降维', 'Batch Normalization/批归一化', 'ResNet/残差连接/跳过连接', 'ResNet50/101/152', 'DenseNet/密集连接', 'SE-Net/通道注意力', 'MobileNet/深度可分离卷积', 'EfficientNet/复合缩放', 'ConvNeXt/现代CNN架构', '预训练模型/Pretrained Models', '迁移学习/Transfer Learning', '微调/Fine-tuning全部层/部分层', '特征提取/Feature Extraction', 'Global Average Pooling', '全连接层分类', 'Softmax分类器', '交叉熵损失/Cross Entropy', 'Top-1/Top-5准确率', '混淆矩阵/Confusion Matrix', 'Precision/Recall/F1', 'ROC曲线/AUC', 'Grad-CAM可视化/热力图', '模型集成/Ensemble', 'TTA/Test Time Augmentation']
                },
                '图像增强': {
                    'desc': '去噪、超分辨率、风格迁移',
                    'difficulty': 2,
                    'dimensions': ['图像增强概述/Image Enhancement', '去噪/Denoising/噪声类型', '高斯噪声/椒盐噪声/泊松噪声', '均值滤波/中值滤波/高斯滤波', '双边滤波/Bilateral Filter/保边', '非局部均值/NLM/Non-local Means', 'BM3D/块匹配3D滤波', '深度学习去噪/U-Net/DnCNN', '超分辨率/Super Resolution/SR', '插值法/SR/双线性/双立方/Lanczos', 'SRCNN/超分辨率CNN', 'ESRGAN/增强SRGAN', 'SRGAN/感知损失/对抗损失', 'EDSR/高效超分辨率', 'Real-ESRGAN/真实场景SR', '上采样/UpSampling2D/转置卷积', '亚像素卷积/Sub-pixel', ' Bicubic/双立方插值', '风格迁移/Style Transfer', '神经风格迁移/Gatys/Content+Style', 'VGG网络特征提取', 'Gram矩阵/风格表示', '内容损失/Content Loss', '风格损失/Style Loss', '总变差损失/TV Loss', '快速风格迁移/Johnson/实时', 'AdaIN/自适应实例归一化', 'WCT/白化与着色变换', 'Avatar-Net/多风格迁移', '图像修复/Image Inpainting', '纹理合成/Texture Synthesis', 'HDR/高动态范围成像', '色调映射/Tone Mapping', '伽马校正/Gamma Correction', '对比度增强/CLAHE', '锐化/Unsharp Mask', '色彩校正/Color Correction', '白平衡/White Balance']
                },
                'OCR': {
                    'desc': '光学字符识别，从图像中提取文字',
                    'difficulty': 3,
                    'dimensions': ['OCR概述/Optical Character Recognition', '文本检测/Text Detection', 'CTPN/Connectionist Text Proposal Network', 'EAST/Efficient and Accuracy Scene Text', 'PixelLink/实例分割文本检测', 'DBNet/Differentiable Binarization', 'PSENet/渐进尺度扩展网络', 'CRAFT/字符区域感知', '文字识别/Text Recognition', 'CRNN/Convolutional Recurrent NN', 'CTC/Connectionist Temporal Classification', 'RNN/LSTM/序列到序列', 'Attention机制/注意力OCR', 'ASTER/Attention-based SRNet', 'Rosetta/FCRN', 'SATRN/自注意力Transformer', '端到端OCR/Master系统', 'CRNN+CTC流程', 'Transformer OCR/SVTR/TRBA', '多语言OCR/中英日韩', '手写体识别/Handwriting Recognition', '表格识别/Table Recognition', 'TATR/表格结构识别', '表格内容OCR', '文档结构化/OCR+Layout', 'PDF解析/PDF转图像/PyMuPDF', '自然场景文字/Natural Scene Text', '弯曲文字检测/TextFuseNet', '任意形状文字/Arbitrary Shape', '古籍OCR/古籍文字识别', '车牌识别/License Plate Recognition', '身份证OCR/银行卡OCR', '票据OCR/发票识别', 'OCR后处理/字典校正/语言模型', 'PaddleOCR/百度开源OCR', 'Tesseract/开源OCR引擎', 'EasyOCR/Python OCR', 'TrOCR/Microsoft OCR', '评估指标/Edit Distance/BLEU', '端到端评估/End-to-End Metrics']
                },
                'ResNet': {
                    'desc': '残差网络，解决深层网络训练问题',
                    'difficulty': 3,
                    'dimensions': ['ResNet概述/残差网络/Deep Residual Learning', '退化问题/Degradation Problem', '残差学习/Residual Learning', '恒等映射/Identity Mapping', '残差块/Residual Block', 'Skip Connection/Shortcut', 'F(x)+x/残差连接', '1x1卷积降维/Projection Shortcut', '瓶颈设计/Bottleneck Design', 'ResNet-18/34/50/101/152', 'ResNet-50/3层瓶颈结构', 'ResNet-18/34/2层残差块', '维度匹配/Same Dimension', '特征图尺寸变化/下采样', 'ResNet-V2/Batch Normalization顺序', 'ResNet-V2/预激活/Pre-activation', '残差单元设计/BN-ReLU-Conv vs Conv-BN-ReLU', 'ImageNet预训练/大规模图像', 'CIFAR-10/100数据集', '迁移学习/模型复用', '微调策略/Fine-tuning策略', 'ResNet-FPN/特征金字塔', '特征金字塔/FPN架构', '多尺度特征融合', 'ResNeXt/分组卷积', 'Cardinality/基数/分组数', 'SE-ResNet/注意力增强', 'SE模块/Squeeze-and-Excitation', '通道注意力/全局池化', 'CBAM/Convolutional Block Attention', 'Res2Net/多尺度残差', 'ResNeSt/Split-Attention', 'EfficientNet-R/复合缩放', 'Wide ResNet/宽残差网络', 'DenseNet vs ResNet/密集vs残差', '神经架构搜索/NAS for ResNet', 'ResNet在检测分割/Backbone', 'Faster R-CNN with ResNet', 'Mask R-CNN with ResNet', 'CIFAR实验/小图像ResNet', '100层/1000层ResNet探索']
                },
                'YOLO': {
                    'desc': '实时目标检测算法',
                    'difficulty': 3,
                    'dimensions': ['YOLO概述/You Only Look Once/实时检测', 'YOLOv1/网格划分/边界框预测', 'YOLOv1/每格多框/NMS后处理', 'YOLOv2/Anchor Boxes/先验框', 'K-Means聚类/Anchor尺寸', 'Darknet-19/骨干网络', 'Batch Normalization/批归一化', 'High Resolution Classifier', 'YOLOv3/多尺度预测/FPN', 'FPN/特征金字塔网络', '多尺度特征图/P3/P4/P5', 'Anchor数量/9个先验框', '类别预测/Logistic/多标签', 'YOLOv4/CSPDarknet53骨干', 'Mish激活函数', 'PANet/路径聚合网络', 'CIOU Loss/完整IoU损失', 'DIoU/Distance IoU', 'SPP/Spatial Pyramid Pooling', 'SAM/Spatial Attention Module', 'CutMix/Mosaic数据增强', 'YOLOv5/Mosaic增强/AutoAnchor', 'YOLOv5/PP-YiBo backbone', 'YOLOv6/RepVGG/重参数化', 'YOLOv7/ELAN/高效层聚合', 'YOLOv8/anchor-free/无锚框', 'YOLOv8/任务无关学习', 'YOLOv8/PyTorch原生', 'YOLOv9/GELAN/泛化高效层聚合', 'YOLOv9/可编程梯度信息', 'YOLOv10/端到端/NMS-free', 'YOLOv11/优化架构', '检测头/Detection Head', 'NMS/非极大值抑制', 'IoU/Intersection over Union', '置信度阈值/Objectness Threshold', 'AP/Average Precision', 'mAP/mean Average Precision', '实时性能/30+ FPS/边缘部署', 'YOLO-NAS/神经架构搜索', 'PP-YOLOE/百度YOLO', 'YOLOR/隐式知识/Implicit', 'YOLOX/YOLOX-Darknet53', 'YOLOX/无锚框/Decoupled Head', '部署/ONNX/TensorRT/NCNN', 'TensorRT加速/INT8量化', '边缘部署/Jetson/移动端', '小目标检测/小YOLO/高分辨率']
                },
                '人脸识别': {
                    'desc': '人脸检测、特征提取、身份验证',
                    'difficulty': 3,
                    'dimensions': ['人脸识别概述/Face Recognition', '人脸检测/Face Detection', 'MTCNN/多任务级联CNN', 'RetinaFace/多尺度检测', 'SSH/Single Stage Headless', 'HRNet/高分辨率网络', 'YOLOv5-Face/人脸检测', 'DBFace/轻量人脸检测', 'FaceBoxes/实时检测', 'One-stage/Two-stage人脸检测', '人脸关键点/Facial Landmarks', '68点/5点/106点关键点', 'Dlib/68点关键点', 'FaceLandmarkDetection', '人脸对齐/Face Alignment', '仿射变换对齐', '关键点几何校正', '人脸归一化/姿态归一化', '人脸特征提取/Face Feature', 'FaceNet/三元组损失', '孪生网络/Siamese Network', 'ArcFace/加性角度间隔损失', 'CosFace/余弦Face', 'SphereFace/角度间隔', 'InsightFace/MXNet实现', 'VGGFace/VGGFace2数据集', 'LFW数据集/Labeled Faces', '人脸识别验证/Verification', '人脸识别识别/Identification', '人脸检索/1:N比对', '人脸聚类/Face Clustering', '活体检测/Liveness Detection', '眨眼检测/张嘴检测', '3D活体/红外活体', '表情识别/Emotion Recognition', 'FER2013/RAF-DB数据集', '口罩检测/Mask Detection', '遮挡人脸识别', '跨姿态识别/Cross-pose', '跨年龄识别/Age Invariant', '人脸属性/Age/Gender/Race', '年龄估计/Age Estimation', '性别识别/Gender Classification', '种族分类/Race Classification', '人脸生成/Face Generation', 'StyleGAN/高分辨率人脸', '人脸编辑/Face Editing', '人脸替换/Face Swap/DeepFake', '人脸修复/Face Restoration', '人脸超分辨率/Face SR', '人脸防伪/Anti-Spoofing', 'Face ID/Apple Face ID', '红外人脸识别', '3D人脸识别/3DMM', '度量学习/Metric Learning', '中心损失/Center Loss', '多任务学习/人脸多属性']
                },
                '图像分割': {
                    'desc': '像素级图像分割，包括语义分割和实例分割',
                    'difficulty': 3,
                    'dimensions': ['图像分割概述/Image Segmentation', '语义分割/Semantic Segmentation', '实例分割/Instance Segmentation', '全景分割/Panoptic Segmentation', 'FCN/全卷积网络/End-to-End', '上采样/反卷积/转置卷积', '跳跃连接/Skip Connection', 'VGG16-FCN/骨干网络', '空洞卷积/Dilated Convolution', '空间金字塔池化/SPP', 'DeepLab系列/DeepLabv1/v2/v3', 'ASPP/Atrous Spatial Pyramid Pooling', '空洞空间金字塔池化/Atrous', '条件随机场/CRF/后处理', 'DeepLabv3+/编码器解码器', 'MobileNet-ASPP/轻量DeepLab', 'U-Net/医学图像分割', '编码器解码器架构/Encoder-Decoder', '跳跃连接/Concatenation', 'UNet++/嵌套密集跳跃', 'UNet3+/全尺度跳跃连接', 'Res-UNet/残差U-Net', 'Attention UNet/注意力机制', 'V-Net/3D医学图像分割', 'SegNet/编码器解码器对称', 'PSPNet/金字塔场景解析', '金字塔池化模块/PPM', '全局场景信息', 'Deeplab系列/DeeplabV3+/ASPP+', 'Mask R-CNN/实例分割', 'RPN/区域提议网络', 'RoI Align/双线性插值', 'Mask分支/实例掩码预测', 'YOLACT/实时实例分割', 'YOLACT++/Fast NMS', 'BlendMask/Bottom-up', 'SOLOv2/动态实例分割', 'TensorMask/密集滑动窗口', 'Panoptic FPN/全景特征金字塔', '全景分割质量/PQ指标', '语义分割指标/mIoU', 'IoU/Jaccard Index', '像素准确率/Pixel Accuracy', 'Dice系数/F1-Score', '评估指标/PA/mIoU/FWIoU', '数据标注/COCO/Pascal VOC', 'Cityscapes/街景分割', 'ADE20K/场景解析', '数据增强/随机翻转/缩放/旋转', 'Test-Time Augmentation/TTA', '模型剪枝/通道剪枝', '知识蒸馏/分割模型', '边缘计算部署/实时分割', '遥感图像分割', '医学图像分割/CT/MRI']
                },
                '模型部署': {
                    'desc': '模型转换、量化、边缘设备部署',
                    'difficulty': 3,
                    'dimensions': ['模型部署概述/Model Deployment', '模型导出/Export/保存格式', 'PyTorch保存/torch.save/state_dict', 'TensorFlow保存/SavedModel/h5', 'ONNX/Open Neural Network Exchange', 'ONNX导出/PyTorch to ONNX', 'ONNX Runtime推理', 'ONNX模型优化/优化器', '模型量化/Quantization', 'INT8量化/INT4量化', '动态量化/Dynamic Quantization', '静态量化/Static Quantization', 'PTQ/Post-Training Quantization', 'QAT/Quantization-Aware Training', 'TensorRT/NVIDIA推理引擎', 'TRT推理优化/FP16/INT8', 'TensorRT插件/Custom Layer', 'CoreML/Apple设备部署', 'CoreML转换/ONNX to CoreML', 'TFLite/TensorFlow Lite', 'TFLite量化/Float16/Int8', 'TFLite FlatBuffer格式', 'NCNN/腾讯移动端框架', 'NCNN/ARM/树莓派部署', 'MNN/阿里巴巴端侧推理', 'MNN/CPU/GPU/Vulkan', 'RKNN/瑞芯微/边缘芯片', 'NNIE/华为海思/安防芯片', 'Edge TPU/Google Coral', 'TPU加速器/Edge部署', 'FPGA部署/FPGA加速', 'NVIDIA Jetson/Jetson Nano/TX2/Xavier', 'Jetson推理/TensorRT部署', '服务器部署/TorchServe', 'TensorFlow Serving/TFS', 'RESTful API/模型服务', 'gRPC/高效模型服务', 'Docker容器部署', 'Kubernetes/K8s部署', '模型版本管理', 'AB测试/灰度发布', '滚动更新/回滚机制', '模型监控/Monitoring', '推理延迟/Latency优化', '吞吐量/Throughput', '批处理推理/Batch Inference', '流式推理/Streaming', '模型压缩/Pruning/剪枝', '结构化剪枝/非结构化剪枝', '通道剪枝/Channel Pruning', '知识蒸馏/Distillation', '模型微调/Edge适配', '边缘设备内存优化', '模型缓存/Cache', '离在线混合部署']
                },
                '目标检测': {
                    'desc': '定位并识别图像中的多个物体',
                    'difficulty': 3,
                    'dimensions': ['目标检测概述/Object Detection', '两阶段检测/Two-Stage', 'R-CNN/区域提议+CNN', 'Fast R-CNN/RoI池化', 'Faster R-CNN/区域提议网络', 'RPN/Region Proposal Network', 'Anchor Boxes/先验框/锚点', 'RoI Pooling/兴趣域池化', 'RoI Align/双线性插值', 'NMS/非极大值抑制', '单阶段检测/One-Stage', 'YOLO系列/网格检测', 'SSD/Single Shot Detector', 'SSD/Prior Boxes/默认框', '多尺度特征图/Multi-scale', 'DSSD/反卷积SSD', 'RetinaNet/焦点损失', 'Focal Loss/解决类别不平衡', 'FPN/特征金字塔网络', 'FPN/Top-Down路径增强', 'PANet/路径聚合网络', 'Cascade R-CNN/级联检测', 'FCOS/Anchor-Free检测', 'CenterNet/关键点检测', 'CornetNet/角点检测', 'DETR/Transformer检测', 'Deformable DETR/可变注意力', 'Anchor机制/Anchor-based', 'Anchor Free/无锚检测', 'Center-based/中心点检测', 'IoU/Intersection over Union', '边界框回归/Bounding Box Regression', '边界框编码/编码解码', '分类损失/Focal Loss', '定位损失/Smooth L1/L2', 'GIOU/DIOU/CIOU Loss', '数据增强/Mosaic/CutMix', '数据集/COCO/Pascal VOC', 'COCO指标/AP/AP50/AP75', 'mAP/mean Average Precision', '检测头/Detection Head', '多尺度检测/Multi-scale', '小目标检测/Small Object', '密集目标检测/Dense Detection', '遮挡目标检测/Occlusion', '旋转目标检测/RSDet/RSDet', '遥感目标检测/RSOD', '医学影像检测', '视频目标检测/VOD', '跟踪检测/SOT/TOT', 'Zero-shot检测/小样本检测', '模型压缩/剪枝蒸馏量化', '实时检测优化/30FPS+', 'GPU部署优化', '边缘设备部署/移动端']
                },
                '视频分析': {
                    'desc': '目标跟踪、行为识别、视频理解',
                    'difficulty': 3,
                    'dimensions': ['视频分析概述/Video Analysis', '视频预处理/解码/帧提取', '视频编解码/FFmpeg/H.264/H.265', '帧采样/均匀采样/关键帧', '光流/Optical Flow', 'Lucas-Kanade光流法', 'Farneback光流/Dense Optical Flow', 'Horn-Schunck光流法', '光流可视化/Flow RGB', 'TVL1光流/OpenCV', '动作识别/Action Recognition', '2D CNN + 时序建模', '3D CNN/C3D/I3D', 'C3D/3D卷积网络', 'I3D/Inflated 3D/Inflated from 2D', 'SlowFast Networks/双路径', 'Slow路径/低帧率/语义', 'Fast路径/高帧率/运动', 'TSN/Temporal Segment Networks', '分段共识/Temporal Segment', 'TSM/Temporal Shift Module', '时序建模/Temporal Modeling', 'LSTM/GRU/循环建模', 'Transformer/Video Transformer', 'TimeSformer/时空注意力', 'ViViT/Video Vision Transformer', '行为识别数据集/Kinetics-400/600', 'UCF-101/HMDB-51数据集', 'Something-Something/细粒度动作', '视频分类/Video Classification', '时空特征融合', '视频描述/Video Captioning', '视频问答/Video QA', '视频生成/Video Generation', '目标跟踪/Object Tracking', 'SOT/单目标跟踪/Single Object', 'MOT/多目标跟踪/Multi Object', 'Siamese Network/孪生网络', 'SiamFC/全卷积孪生', 'SiamRPN/区域提议网络', 'SiamMask/模板匹配分割', 'ATOM/Accurate Tracking', 'DiMP/Discriminative Model', 'TransT/Transformer跟踪', 'OSTrack/视觉Transformer跟踪', 'TADam/跟踪任意检测', 'SORT/卡尔曼滤波', 'DeepSORT/深度特征', 'ByteTrack/ByteTrack跟踪', 'FairMOT/中心点跟踪', 'JDE/检测+跟踪联合', 'ReID/重识别/特征提取', '行人重识别/Person ReID', '车辆重识别/Vehicle ReID', '视频摘要/Video Summarization', '视频浓缩/Video Synopsis', '异常行为检测/Anomaly Detection', '打架检测/摔倒检测', '入侵检测/周界防范', '人数统计/Crowd Counting', '人流密度估计/Density Map', '步态识别/Gait Recognition', '手势识别/Gesture Recognition', '表情识别/Facial Expression', '视线追踪/Gaze Tracking', '视频理解/Video Understanding', '时空动作定位/Temporal Action', '时序动作检测/Action Detection', '动作提议/Action Proposal', 'BSN/边界敏感网络', 'BMN/边界匹配网络', 'AVA数据集/时空动作', '视频分割/Video Segmentation', '光流引导分割', 'Video Matting/视频抠图']
                }
            }
        },
        '推荐算法工程师': {
            'description': '开发个性化推荐系统，提升用户体验和商业转化率。',
            'skills': {
                'Python': {
                    'desc': '推荐系统开发语言',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/list/dict/set/tuple/控制流/循环/函数/类/继承/多态', 'NumPy数值计算/数组操作/矩阵运算/广播机制', 'Pandas数据处理/DataFrame/Series/缺失值处理', 'Scipy科学计算/稀疏矩阵/scipy.sparse', 'Scikit-learn机器学习/数据预处理/模型评估', 'PyTorch深度学习/Embedding/张量计算/GPU加速', 'TensorFlow推荐/TF-Ranking/Factorization Machines', 'LightGBM/XGBoost/梯度提升树', '大数据处理/PySpark/DataFrame/SQL', 'SQL查询/窗口函数/聚合函数', 'Linux命令/sed/awk/shell脚本', 'Git版本控制/代码管理', '特征工程工具/特征编码/特征选择', '推荐系统框架/RecBole/DeepRec', '协同过滤实现/Surprise/Gensim', '实时数据处理/Flink实时/Streaming', 'Redis缓存/FAISS向量检索', 'Docker容器化/环境配置', 'Jupyter/Spark Notebook', 'Python多进程/多线程/异步编程']
                },
                'Embedding': {
                    'desc': '用户和物品的向量表示学习',
                    'difficulty': 2,
                    'dimensions': ['Embedding概述/向量嵌入/稠密表示', 'One-hot编码/稀疏向量/维度灾难', '矩阵分解/Matrix Factorization', 'SVD奇异值分解/Singular Value', 'ALS交替最小二乘/Alternating Least Squares', 'SVD++/隐式反馈建模', 'Word2Vec/Item2Vec/物品向量化', 'Skip-gram/CBOW/负采样', 'Item2Vec/购物车序列', 'Doc2Vec/文档向量化', '图嵌入/Graph Embedding', 'DeepWalk/随机游走', 'Node2Vec/结构/邻居游走', 'LINE/一阶二阶相似度', 'SDNE/深度神经网络嵌入', 'GraphSAGE/图采样聚合', 'GCN图卷积/谱域卷积', 'GAT注意力图神经网络', '知识图谱嵌入/KGE/TransE/RotatE', '协同过滤嵌入/隐向量学习', '用户Embedding/用户ID嵌入', '物品Embedding/Item Embedding', '序列Embedding/序列建模', '多兴趣Embedding/胶囊网络', '对比学习/Contrastive Learning', 'SimCLR/SimCSE/对比', 'Sentence-BERT/句子向量', '多模态Embedding/图文向量', 'CLIP图文对齐', '向量检索/FAISS/Annoy', 'HNSW分层可导航小世界', 'IVF倒排索引/聚类索引', '余弦相似度/内积/欧式距离', '向量量化/PQ/Product Quantization', '在线向量更新/增量学习', '跨域Embedding/迁移学习']
                },
                'Redis': {
                    'desc': '缓存推荐结果和用户特征',
                    'difficulty': 2,
                    'dimensions': ['Redis概述/内存数据库/键值存储', '数据结构/String/Hash/List/Set/Zset', 'Hash/散列/用户特征存储', 'List/列表/推荐队列', 'Sorted Set/有序集合/排序推荐', 'Redis String/序列化JSON/推荐结果', '过期策略/TTL/键过期删除', '持久化/RDB/AOF/混合持久化', '主从复制/读写分离/Replication', 'Sentinel哨兵/高可用', 'Cluster集群/分片/槽位', '客户端连接/Redis-py/Python连接', '连接池/Connection Pool', 'Pipeline管道/批量操作', '事务/MULTI/EXEC/WATCH', '缓存策略/Cache Aside/Write Behind', '缓存失效/主动失效/被动失效', 'LRU/LFU淘汰策略/maxmemory-policy', '热key问题/热点探测', '大key问题/拆分/压缩', '分布式锁/RedLock/SetNX', '布隆过滤器/Bloom Filter/去重', 'Redis搜索/RediSearch', 'RedisJSON/JSON文档', 'RedisGraph/图数据库', 'RedisML/机器学习模块', '实时推荐缓存/用户实时特征', 'Session缓存/用户会话', '排行榜/热榜/实时更新', '计数统计/HyperLogLog', '推荐结果缓存/AB实验分组', '实时特征存储/用户点击序列', '特征服务器/Feature Store', 'Redis限流/滑动窗口']
                },
                'Spark': {
                    'desc': '大规模数据处理框架',
                    'difficulty': 2,
                    'dimensions': ['Spark概述/大数据计算引擎/In-Memory', 'RDD弹性分布式数据集/Resilient Distributed', 'Transformation/转换操作/map/filter/flatMap', 'Action/行动操作/collect/count/save', 'DataFrame/API结构化数据', 'Dataset/API类型安全', 'Spark SQL/结构化查询', 'Spark MLlib/机器学习库', 'Spark ML/DataFrame API', '协同过滤ALS/MatrixFactorization', '交替最小二乘法/隐式反馈', '特征工程/Spark处理', 'ML Pipeline/机器学习流水线', '超参数调优/CrossValidator', '模型导出/MLflow集成', 'Spark Streaming/微批处理', 'Structured Streaming/流处理', 'Kafka集成/流式数据源', 'Spark GraphX/图计算', 'Spark作业调度/DAG/Stage', 'Shuffle过程/数据重分区', '分区策略/PartitionBy', 'Cache缓存/persist/cache', '广播变量/Broadcast变量', '累加器/Accumulator', 'Spark优化/内存管理/GC调优', 'Spark并行度/parallelism', '数据倾斜/Skew/解决', 'Kubernetes Spark/集群部署', 'EMR/Auto Scaling', 'Spark on Yarn/集群管理器', 'DataSource V2/数据源API', 'Delta Lake/ACID事务', 'Iceberg/表格式', 'PySpark/Python API', 'Spark UDF/用户自定义函数', '窗口函数/Window Functions', 'Join优化/广播join/ shuffle join']
                },
                '冷启动': {
                    'desc': '新用户和新物品的推荐策略',
                    'difficulty': 2,
                    'dimensions': ['冷启动概述/Cold Start', '用户冷启动/New User Cold Start', '物品冷启动/Item Cold Start', '系统冷启动/System Cold Start', '热门推荐/Popularity Based', '趋势推荐/Trending/Hot Items', '专家推荐/Expert Recommendation', '注册信息/Registration Data', '人口统计学/Demographic', '社交网络推荐/Social Recommendation', '第三方登录/Social Login', '探索与利用/EE问题/Exploration-Exploitation', 'UCB上置信界/Upper Confidence Bound', 'Thompson Sampling/汤普森采样', 'Epsilon-Greedy/贪心', 'Bandit算法/多臂老虎机', 'LinUCB/线性上置信界', '物品相似传导/Similarity Propagation', '跨域推荐/Cross-Domain', '迁移学习/Transfer Learning', '元学习/Meta Learning', '小样本学习/Few-shot Learning', '零样本学习/Zero-shot Learning', '用户行为序列/首触推荐', '内容特征/Side Information', '物品内容信息/Category/Tag', '知识图谱辅助/Knowledge Graph', '强化学习探索/RL-based', '深度学习泛化/Deep Model', 'Embedding初始化/预训练', '模型微调/Fine-tuning', '热度降权/Time Decay', '非冷启动样本学习', '标签推荐/Tag Recommendation', '兴趣点推荐/POI Recommendation', '位置推荐/LBS/Location', '新用户引导/Onboarding', '问卷调查/Preference Survey', '主动学习/Active Learning']
                },
                '协同过滤': {
                    'desc': '基于用户或物品的相似度推荐',
                    'difficulty': 2,
                    'dimensions': ['协同过滤概述/Collaborative Filtering', 'User-based CF/用户协同', 'Item-based CF/物品协同', '隐式反馈/Implicit Feedback/点击浏览', '显式反馈/Explicit Feedback/评分', '相似度计算/Similarity', '余弦相似度/Cosine Similarity', '皮尔逊相关系数/Pearson', '杰卡德相似度/Jaccard', '欧式距离/曼哈顿距离', '用户相似度/User Similarity', '物品相似度/Item Similarity', 'Top-K近邻/K-Nearest Neighbor', '相似度阈值/Threshold', '邻域模型/Neighborhood Model', '基于记忆/Memory-based', '基于模型/Model-based', '矩阵分解/Matrix Factorization', 'SVD奇异值分解', 'ALS交替最小二乘法', 'SVD++/隐式因子', 'NMF非负矩阵分解', 'FunkSVD/梯度下降SVD', '_bias偏置项/Bias Term', '正则化/Regularization', '过拟合/Underfitting', '稀疏性/Sparsity', '评分预测/Rating Prediction', 'Top-N推荐列表', '排序推荐/Ranking', 'MRR平均倒数排名', 'NDCG归一化折损增益', 'Coverage覆盖率', 'Diversity多样性', '新颖性/Novelty', '实时协同过滤', '增量更新/Incremental Update', '离线计算/Online Serving', 'Spark协同过滤/ALS实现', 'Surprise库/Python实现', '离线矩阵分解', '在线近邻计算']
                },
                '召回算法': {
                    'desc': '快速筛选候选集的算法',
                    'difficulty': 2,
                    'dimensions': ['召回概述/Retrieval/Candidate Generation', '多路召回/Multi-channel Retrieval', '召回链路/Pipeline', '热门召回/Popularity Recall', '热榜召回/Top-K Popular', '时序召回/Sequence Recall', '协同召回/Collaborative Recall', 'U2I召回/用户到物品', 'I2I召回/物品到物品', 'U2U召回/用户到用户', '基于物品相似度/Item Similarity', 'Item-CF协同过滤召回', 'User-CF用户协同召回', '矩阵分解召回/MF Recall', 'Embedding召回/向量检索', 'FAISS向量检索/Facebook AI', 'HNSW分层可导航小世界', 'IVF倒排索引/聚类', 'Product Quantization/PQ量化', '实时向量更新', 'DeepMatch深度匹配召回', 'Two-Tower双塔模型', 'Query塔/Item塔', '向量索引/Annoy/ScaNN', 'MILvus/Qdrant向量库', 'Graph召回/图神经网络', 'GNN图神经网络召回', 'GraphSAGE/采样聚合', 'GAT注意力召回', '序列召回/Sequence Modeling', 'GRU4Rec/循环网络', 'LSTM4Rec/长短期记忆', 'BERT4Rec/双向Transformer', 'NextItNet/卷积序列', 'MIND多兴趣建模', 'ComiRec多兴趣召回', '异构序列/Heterogeneous', '跨域召回/Cross-Domain', '知识图谱召回/KG Recall', 'TransE/RotatE召回', '意图召回/Query Intent', '标签召回/Tag Recall', '类目召回/Category Recall', '品牌召回/Brand Recall', '实时召回/Online Recall', '离线召回/Offline Recall', '召回评估/Precision@K/Recall@K', '召回去重/Deduplication', '流量分配/Recall Mix', '多业务召回融合']
                },
                '特征工程': {
                    'desc': '构建用户画像和物品特征',
                    'difficulty': 2,
                    'dimensions': ['特征工程概述/Feature Engineering', '用户画像/User Profile', '人口属性/Age/Gender/Location', '用户行为特征/Behavior Features', '统计特征/Statistics', '计数特征/Count Features', '交叉特征/Cross Features', '类别特征编码/Category Encoding', 'One-hot编码/Sparse Vector', 'Label Encoding/标签编码', 'Target Encoding/目标编码', 'Category Embedding', '频率编码/Frequency Encoding', '物品特征/Item Features', '内容特征/Content Features', '文本特征/TF-IDF/BERT', '图像特征/CNN/VGG', '标签特征/Tag Features', '类目特征/Category/品牌', '统计特征/销量/评分/评论', '时间特征/Time Features', '时间衰减/Time Decay', '周期特征/Periodicity/周期性', '行为序列特征/Sequence Features', 'Session行为/会话特征', '点击序列/浏览序列/购买序列', '序列长度/Sequence Length', '序列Pattern/序列模式', 'Graph特征/图特征', 'Node Degree/节点度', 'PageRank/重要性', '社区归属/Community', '交叉特征组合/Feature Crossing', 'FM/Factorization Machine', 'FFM/Field-Aware FM', 'DeepFM/深度分解机', '特征选择/Feature Selection', '过滤法/Filter/方差阈值', '包装法/Wrapper/递归消除', '嵌入法/Embedding/Tree', '特征重要性/Importance', '在线特征计算/实时特征', '离线特征处理/Spark', '特征平台/Feature Store', '特征监控/Feature Monitor', '特征回填/Backfill', '特征一致性/线上线下', '特征变换/Scaling/Normalization', 'Z-score标准化/MinMax', '对数变换/Log Transform', '分桶/Binning/离散化', '缺失值处理/Imputation']
                },
                '矩阵分解': {
                    'desc': 'SVD、ALS等降维技术',
                    'difficulty': 2,
                    'dimensions': ['矩阵分解概述/Matrix Factorization', '用户-物品评分矩阵', '隐向量/Latent Vector', '隐因子/Latent Factor', 'SVD奇异值分解/Singular Value', 'Truncated SVD/截断SVD', '稀疏矩阵/Sparse Matrix', 'sklearn.decomposition', 'ALS交替最小二乘/Alternating Least', '隐式反馈/Implicit Feedback', '置信度加权/Confidence Weighting', '物品偏置/Item Bias', '用户偏置/User Bias', '全局偏置/Global Bias', '正则化项/Regularization', 'L2正则化/Frobenius', '梯度下降求解/Gradient Descent', '随机梯度下降/SGD', '批量梯度下降/BGD', '矩阵补全/Matrix Completion', '协同过滤/MF for CF', '评分预测/Rating Prediction', 'Top-K推荐/K-Item Recommendation', 'SVD++扩展/Implicit', 'TimeSVD++/时序矩阵', 'NMF非负矩阵分解', 'SVD++ Plus/社交增强', 'Slim稀疏线性方法', 'Factorization Machine/FM', '二阶交叉特征', '高阶交叉/FM高阶', 'FFM/Field-Aware FM', '分解机实现/LibFM/LibFFM', 'PyTorch实现MF', 'Spark MLlib/ALS实现', '协同过滤实现/Surprise', 'ALS并行化/分布式', '负采样/Negative Sampling', '正样本/负样本', '采样策略/Sampling Strategy', '评估指标/RMSE/MAE', 'Top-K评估/NDCG/AP', '过拟合问题/Underfitting', '泛化能力/Generalization', '在线更新/Incremental', '增量矩阵分解']
                },
                'A/B测试': {
                    'desc': '评估推荐效果',
                    'difficulty': 3,
                    'dimensions': ['A/B测试概述/AB Test/对照实验', '实验设计/Experimental Design', '假设检验/Hypothesis Testing', '原假设/H0/零假设', '备择假设/H1', '统计显著性/Significance', 'P-value/P值', '置信水平/Confidence Level', '置信区间/Confidence Interval', '95%置信区间', '第一类错误/Type I Error', '第二类错误/Type II Error', '统计功效/Power', '样本量计算/Sample Size', '效应量/Effect Size', '随机分组/Randomization', '分流策略/AA分流', '流量分配/Traffic Split', '分层实验/Layer/Stratified', '正交实验/Orthogonal', 'Contextual Bandit/上下文老虎机', '多臂老虎机/Multi-Armed Bandit', 'Epsilon-Greedy实验', 'Thompson Sampling实验', 'UCB算法实验', '实验分组/Control/Treatment', '对照组/控制组/Control', '实验组/处理组/Treatment', '核心指标/北极星指标', '辅助指标/Guardrail Metrics', '点击率/CTR/Click-Through Rate', '转化率/CVR/Conversion Rate', '停留时长/Duration', 'GMV/成交总额', '人均点击/平均点击数', '覆盖率/Coverage', '多样性/Diversity', '新颖性/Novelty', '短期指标 vs 长期指标', '辛普森悖论/Simpson Paradox', '新奇效应/Novelty Effect', '首日效应/First-Day Effect', 'Seasonality/季节性', '在线评估/Online Evaluation', '离线评估/Offline Evaluation', 'AUC/ROC曲线下面积', 'NDCG归一化折损增益', 'AB平台/AB Test Platform', 'Exp平台/Experiment', '流量调度/Traffic Controller', '分桶/Bucket', '分层隔离/Layer Isolation', '实验引擎/AB Test Engine', '效果评估/Significant Test', 'AA检验/均匀性检验', 'AB结果分析/Report', '下钻分析/Drill Down', '归因分析/Attribution']
                },
                'DIN': {
                    'desc': '深度兴趣网络，建模用户动态兴趣',
                    'difficulty': 3,
                    'dimensions': ['DIN概述/Deep Interest Network', '兴趣建模/Interest Modeling', '注意力机制/Attention/兴趣激活', 'Activation Unit/激活单元', '用户行为序列/User Behavior', '候选商品/Candidate Item', '注意力权重/Attention Weight', 'Weighted Sum/加权求和', 'Dice激活函数/PReLU改进', 'Batch Normalization in DIN', 'Dice/数据自适应激活', 'BI-LSTM/双向兴趣序列', '注意力 GRU/AGRU', '注意力自然计量/ANP', '深度兴趣进化网络/DIEN', '兴趣抽取层/Interest Extractor', '兴趣进化层/Interest Evolution', 'GRU with attentional update gate', 'AUGRU/注意力更新门', '序列建模/Sequence Modeling', '用户点击序列/Click Sequence', '购买序列/Purchase Sequence', '浏览序列/Browse Sequence', 'Session序列/会话序列', '行为特征/Behavior Features', '兴趣特征/Interest Features', '短期兴趣/Short-term Interest', '长期兴趣/Long-term Interest', '多兴趣建模/Multi-Interest', 'MIND多兴趣网络', 'ComiRec多兴趣召回', 'Capsule网络/胶囊网络', 'Memory Network/记忆网络', 'DIN vs DIEN vs DSIN', 'DSIN/深度序列兴趣网络', 'Session兴趣抽取', 'Session间兴趣转移', '注意力分散/Attention Dilution', '多头注意力/Multi-Head', '位置编码/Position Encoding', 'DIN特征输入', '特征交叉/Feature Interaction', 'DeepCTR实现', 'PyTorch实现DIN', '阿里巴巴DIEN/线上部署', '实时预测/Real-time', '特征工程/行为序列化']
                },
                'Wide&Deep': {
                    'desc': 'Google的推荐模型架构',
                    'difficulty': 3,
                    'dimensions': ['Wide&Deep概述/Google 2016', 'Wide侧/线性模型/记忆能力', 'Deep侧/深度神经网络/泛化能力', '联合学习/Joint Learning', '联合训练/Co-Training', 'Memorization/记忆/线性部分', 'Generalization/泛化/DNN部分', 'Wide侧特征/稀疏特征', '交叉特征/Cross Product', 'Wide特征工程/人工特征', 'AND(特征组合)/与门', 'Deep侧特征/稠密特征', 'Embedding层/稀疏转稠密', '全连接层/Hidden Layers', '激活函数/ReLU', 'Wide&Deep模型结构', 'Deep侧塔/Deep Tower', 'Wide侧塔/Wide Tower', '输出层/Softmax/Sigmoid', '损失函数/Log Loss', '优化器/Adam/Adagrad', 'Wide&Deep论文/Google Play', 'TensorFlow WideDeep', 'DeepCTR/WideDeep实现', 'DeepFM/Wide&Deep升级', 'DCN/Deep&Cross Network', 'DCN v2/改进交叉网络', 'Cross Network/显式特征交叉', 'xDeepFM/Compressed Interaction', 'CIN/Compressed Interaction Network', 'AutoInt/自注意力', 'FiBiNet/双线性特征交互', 'SENet双线性', 'FGCNN/特征生成CNN', 'ORPAM/最优局部', '模型融合/Ensemble', '离线训练/Offline Training', '在线Serving/服务', '特征实时更新', 'Wide侧和Deep侧平衡', 'Deep侧层数选择', 'Embedding维度选择']
                },
                '实时推荐': {
                    'desc': '流式计算实现实时个性化',
                    'difficulty': 3,
                    'dimensions': ['实时推荐概述/Real-time Recommendation', '流式计算/Stream Processing', '实时特征/Online Features', '离线特征/Offline Features', '特征实时性/Latency', '毫秒级延迟/Millisecond', '秒级延迟/Second-level', '分钟级更新/Minute-level', 'Flink流处理/Apache Flink', 'Flink DataStream API', 'Flink SQL/流式SQL', 'Flink CEP/复杂事件处理', 'Kafka消息队列/Streaming', 'Kafka Producer/Consumer', 'Kafka Streams/流处理', 'Spark Streaming/微批', 'Structured Streaming', 'Storm实时计算', '实时特征计算/Feature Computing', '滑动窗口/Sliding Window', '滚动窗口/Tumbling Window', '会话窗口/Session Window', '窗口聚合/Aggregation', 'Watermark/水位线/乱序', 'Checkpoint/状态快照', 'Exactly-Once语义', 'At-Least-Once语义', '用户实时行为/Real-time Behavior', '点击实时反馈/Click Feedback', '曝光实时上报', '实时特征更新', 'Redis实时存储/特征缓存', 'Flink+Redis架构', '实时排序/Real-time Ranking', '在线学习/Online Learning', '增量训练/Incremental Training', '实时模型更新/Online Learning', 'FTRL在线学习', '在线特征工程', '流式特征Join', '实时TopK计算', '热榜实时更新', '实时召回/Online Recall', '实时协同过滤', '实时模型推断', 'Triton推理服务器', 'TensorFlow Serving', '特征服务/Feature Server', '推荐服务/Recommendation Service', 'A/B实验/实时监控', '推荐链路/全链路', 'Lambda架构/批流一体', 'Kappa架构/纯流处理', '流批一体/Streaming Batch']
                },
                '排序算法': {
                    'desc': '精排模型，预测用户点击率或转化率',
                    'difficulty': 3,
                    'dimensions': ['排序概述/Ranking/精排', 'CTR预估/Click-Through Rate', 'CVR预估/Conversion Rate', '排序模型/Ranking Model', '粗排/Coarse Ranking/召回后', '精排/Fine Ranking/候选集', '重排/Reranking/最终排序', '点击率预估/CTR Prediction', '转化率预估/CVR Prediction', '二分类问题/Binary Classification', 'LogLoss损失函数', 'AUC评估指标', 'GAUC分组AUC', 'LogAUC/Label Ranking', 'GBDT/LightGBM/XGBoost', 'GBDT特征重要性', 'GBDT在线学习/FTRL', 'GBDT+LR组合/2014', '因子分解机/FM', 'FFM/Field-Aware FM', '深度学习排序/Deep CTR', 'Wide&Deep/记忆+泛化', 'DeepFM/Deep Factorization', 'DCN/Deep&Cross', 'xDeepFM/显式高阶交叉', 'DIN/深度兴趣网络', 'DIEN/深度兴趣进化', 'DSIN/深度序列兴趣', 'ESMM/全空间多任务', 'ESM2/序列建模样本', '多任务学习/Multi-Task', 'MMoE/多门专家', 'PLE/渐进式分离', 'CGC/共享私有专家', 'Share Bottom/硬参数共享', 'Auxiliary Loss/辅助loss', 'CTR&CVR联合建模', '注意力机制排序', '序列建模/GRU/Transformer', '特征交叉/Feature Crossing', '隐式交叉/Implicit Cross', '显式交叉/Explicit Cross', '一阶特征/First Order', '二阶特征/Second Order', '高阶特征交叉/High Order', 'Embedding技术', 'Attention排序', '序列特征处理', '上下文特征/Context', '用户特征/User Features', '物品特征/Item Features', '交叉特征/Cross Features', '特征重要性/Feature Importance', 'Shallow Deep模型', 'DCN v2/改进版', 'AutoInt/自注意力', 'FiBiNet/双线性', 'ONETA/One-Hot to Embedding', '排序模型优化', '模型蒸馏/Distillation', '多目标排序/Multi-Objective', 'LTR学习排序/Learning to Rank', 'Pointwise/逐点学习', 'Pairwise/配对学习', 'Listwise/列表学习', 'BPR/Bayesian Personalized', 'LambdaMART/LambdaRank', 'NDCG优化']
                },
                '深度学习推荐': {
                    'desc': '使用神经网络构建推荐模型',
                    'difficulty': 3,
                    'dimensions': ['深度学习推荐概述/Deep Learning Rec', 'Embedding技术/向量化表示', 'ID Embedding/ID向量化', '特征Embedding/特征嵌入', 'Multi-hot Embedding', 'Pooling聚合/平均/最大', '注意力加权/Aware Pooling', '深度神经网络/DNN', 'MLP多层感知机', '激活函数/ReLU/Sigmoid/Tanh', 'Dropout正则化', 'BatchNorm批归一化', '残差连接/Residual', '特征交叉/Feature Interaction', 'PNN/Product Network', 'IPNN/Inner PNN/外积', 'OPNN/Outer PNN', 'Deep Crossing/残差网络', 'Neural CF/神经协同过滤', 'GMF/广义矩阵分解', 'MLP协同过滤', 'NeuMF/神经矩阵分解', 'NCF/Neural Collaborative', '注意力机制/Attention', '自注意力/Self-Attention', 'Transformer推荐', 'BST/Behavior Sequence', 'BST Transformer编码', 'BST位置编码', '序列推荐/Sequence Rec', 'SASRec/自注意力', 'BERT4Rec/Masked LM', 'MIMN/记忆增强', 'HPM/层次记忆网络', 'KMN/知识驱动', '图神经网络推荐/GNN Rec', 'GCN图卷积', 'GAT注意力图', 'GraphSAGE采样', 'NGCF/神经图协同', 'LightGCN/轻量GCN', 'GNN序列推荐', '知识图谱推荐/KG Rec', 'RippleNet/涟漪网络', 'KGAT/知识图谱注意力', 'MKR/多任务知识', '多模态推荐/Multi-modal', 'MMGCN/多模态GCN', 'GNN-MNAR/模态感知', '对比学习推荐/Contrastive', 'SGL/自监督图', 'NCL/负样本对比', 'MMCL/多模态对比', '强化学习推荐/RL Rec', 'DRN深度强化学习', 'DEERS/对抗强化学习', 'GRU/Policy Gradient', 'DQN/Deep Q-Network', '迁移学习推荐/Transfer', '跨域推荐/Cross-Domain', '元学习推荐/Meta Learning', 'MeLU个性化', 'MAML少量样本', '联邦学习推荐/Federated', '隐私保护推荐', '在线学习/FTRL/Online', '增量学习/Incremental', '模型压缩/Pruning/Quantization', '知识蒸馏/Distillation', '推荐系统公平性/Fairness']
                }
            }
        }
    },
    '网络工程': {
        '网络工程师': {
            'description': '负责企业网络规划、搭建和维护，保障网络稳定运行。',
            'skills': {
                'ACL': {
                    'desc': '访问控制列表，网络安全策略配置',
                    'difficulty': 2,
                    'dimensions': ['ACL概述/Access Control List/访问控制列表', '标准ACL/Standard ACL/基于源IP', '扩展ACL/Extended ACL/多条件', 'ACL编号/1-99标准/100-199扩展', 'ACL规则/Rule/permit/deny', '通配符掩码/Wildcard Mask', '反掩码/通配符计算', 'any/任意主机匹配', 'host/单主机精确匹配', '入站ACL/Inbound ACL', '出站ACL/Outbound ACL', 'ACL方向/应用方向', '接口应用/Interface apply', 'VLAN ACL/VACL/三层交换', '命名ACL/Named ACL', '自反ACL/Reflexive ACL', '动态ACL/Dynamic ACL', '时间ACL/Time-based ACL', 'ACL注释/Remark', 'ACL顺序/隐含deny any', 'ACL日志/Log/记录匹配', '思科ACL配置/IOS', '华为ACL配置/VRP', 'ACL匹配顺序/自上而下', 'ACL优化/减少条目', 'ACL性能影响', 'IPv6 ACL/命名ACL', '基于端口的ACL/PACL', 'VACL应用/VLAN访问映射', '策略路由/PBR/Policy Route', 'ACL与Route Map', '流量过滤/Traffic Filter', '安全策略实施', '网络分段/Security Zone', 'DMZ隔离/隔离区', '内网访问控制', '外网访问控制', '带宽控制/QoS基础']
                },
                'NAT': {
                    'desc': '网络地址转换，实现内外网通信',
                    'difficulty': 2,
                    'dimensions': ['NAT概述/Network Address Translation', '私有IP地址/Private IP', '公有IP地址/Public IP', 'A类私有/10.0.0.0-10.255.255.255', 'B类私有/172.16.0.0-172.31.255.255', 'C类私有/192.168.0.0-192.168.255.255', 'NAT类型/静态NAT/动态NAT', '静态NAT/Static NAT/一对一映射', '动态NAT/Dynamic NAT/地址池', 'PAT/端口地址转换/Overloading', 'NAT Overload/端口复用', 'Easy IP/出口IP直接转换', '内部全局地址/Inside Global', '内部本地地址/Inside Local', '外部全局地址/Outside Global', '外部本地地址/Outside Local', 'NATinside/内部接口', 'NAToutside/外部接口', 'IP地址转换/Translation', '会话表/Session Table', '转换超时/Timeout', 'TCP会话超时/UDP超时', '静态路由/NAT配置', '默认路由/NAT出口', 'NAT Pool/地址池', 'overload/端口复用', '单向NAT/Inside Initiated', '双向NAT/Bidirectional', 'NAT ALG/应用层网关', 'FTP ALG/FTP穿越NAT', 'DNS ALG', 'VoIP ALG/SIP ALG', 'H.323 ALG', 'NAT日志/日志记录', 'NAT穿透/NAT Traversal', 'STUN/TURN/ICE', '对称NAT/Cone NAT/Full Cone', 'NAT设备性能/并发会话', '会话数限制', '华为NAT配置', '思科NAT配置', '防火墙NAT/Server NAT', '源NAT/SNAT/出向转换', '目标NAT/DNAT/入向转换', '目的NAT/端口映射', '负载均衡NAT', '高可用NAT/HA NAT']
                },
                'TCP/IP': {
                    'desc': '网络通信核心协议栈，理解IP寻址和路由原理',
                    'difficulty': 2,
                    'dimensions': ['TCP/IP四层模型/四层/应用传输网际', 'OSI七层模型/七层参考模型', '应用层/Application Layer', '传输层/Transport Layer', '网络层/Network Layer', '数据链路层/Data Link Layer', '物理层/Physical Layer', 'TCP传输控制协议/面向连接', 'TCP三次握手/SYN/SYN-ACK/ACK', 'TCP四次挥手/FIN/ACK', 'TCP状态机/ESTABLISHED/FIN_WAIT', 'TCP可靠性/确认机制/ACK', 'TCP重传机制/Retransmission', 'TCP滑动窗口/Window Size', 'TCP拥塞控制/Congestion Control', '慢启动/Slow Start', '拥塞避免/Congestion Avoidance', '快重传/Fast Retransmit', '快恢复/Fast Recovery', 'TCP流量控制/Flow Control', '窗口大小/Window Scaling', 'UDP用户数据报协议/无连接', 'TCP vs UDP区别', 'IP互联网协议/Network Layer', 'IPv4地址/32位地址', 'IPv6地址/128位地址', 'IP地址分类/A/B/C/D/E类', '子网掩码/Subnet Mask', '默认网关/Gateway', 'CIDR无类域间路由/Classless', 'VLSM可变长子网掩码', '超网/Supernet', '公有IP vs 私有IP', 'NAT网络地址转换', 'ARP地址解析协议/IP-MAC', 'RARP反向ARP', 'ICMP互联网控制消息协议', 'Ping/回显请求', 'Traceroute/路由追踪', '路由/Routing/静态路由/动态路由', '路由表/Routing Table', '直连路由/Connected', '静态路由/Static Route', '默认路由/Default Route', '动态路由协议/Routing Protocol', 'RIP/OSPF/BGP/EIGRP', 'DNS域名系统/Domain Name', 'DHCP动态主机配置/Dynamic Host', 'HTTP超文本传输/Hypertext', 'HTTPS安全HTTP/SSL/TLS', 'FTP文件传输/File Transfer', 'SFTP安全文件传输', 'SMTP/POP3/IMAP邮件协议', 'SSH安全外壳/Secure Shell', 'Telnet远程登录/明文', 'SNMP简单网络管理', 'TCP/IP协议栈封装', '数据封装/Encapsulation', '数据解封装/De-encapsulation', 'MTU最大传输单元', '分片/Fragmentation', '重组/Reassembly', 'TTL生存时间/Time To Live', 'IP地址规划/子网划分', 'VLSM规划/子网设计', '路由聚合/Summarization', '默认网关配置', 'DNS服务器配置', 'DHCP服务器配置', 'TCP优化/参数调优']
                },
                'VLAN': {
                    'desc': '虚拟局域网划分和配置',
                    'difficulty': 2,
                    'dimensions': ['VLAN概述/Virtual LAN/虚拟局域网', 'VLAN作用/广播域隔离', '广播域/Broadcast Domain', '冲突域/Collision Domain', 'VLAN划分/基于端口/基于MAC/基于协议', 'Access端口/接入端口', 'Trunk端口/干道端口', 'Hybrid端口/混合端口', 'PVID/端口VLAN ID', 'VLAN ID/1-4094', 'VLAN 1/默认VLAN', 'VLAN配置/创建VLAN', 'VLAN命名/name', '将端口加入VLAN', 'show vlan brief/查看VLAN', 'VLAN间路由/Inter-VLAN', '单臂路由/Router on a Stick', '子接口/Sub-interface', '802.1Q标签/Tagging', 'Tag标签/4字节/VLAN Tag', 'Native VLAN/本征VLAN', 'VLAN Trunking/中继', '802.1Q Tunnel/隧道', 'QinQ/双层标签/VLAN Tunnel', 'VTP/VLAN Trunking Protocol', 'VTP模式/Server/Client/Transparent', 'VTP裁剪/VTP Pruning', 'VTP版本/v1 v2 v3', 'STP生成树与VLAN', 'PVST每VLAN生成树', 'PVST+/Per VLAN Spanning', 'Rapid-PVST/RSTP+', 'MSTP多实例生成树', 'Voice VLAN/语音VLAN', 'Guest VLAN/访客VLAN', '管理VLAN/Management VLAN', '私有VLAN/PVLAN/隔离VLAN', 'Super VLAN/聚合VLAN', 'VLAN间路由/Router Interface', 'SVI/交换虚拟接口', 'Layer 3 Switch/三层交换', 'MLAG/堆叠/VPC', '堆叠/iStack/CSS', 'VSS虚拟交换系统', 'vPC/虚拟端口通道', '链路聚合+LACP', 'VLAN映射/VLAN Translation', ' Selective Q-in-Q', '华为VLAN配置', '思科VLAN配置', 'VLAN规划/IP地址对应', 'VLAN安全/限制VLAN跳转', 'VMPS/VLAN Management Policy']
                },
                '网络协议': {
                    'desc': 'HTTP、DNS、DHCP、FTP等应用层协议原理',
                    'difficulty': 2,
                    'dimensions': ['HTTP超文本传输协议/Hypertext Transfer', 'HTTP/1.0 vs HTTP/1.1', 'HTTP/2多路复用/ multiplexing', 'HTTP/3/QUIC协议', 'HTTP请求方法/GET/POST/PUT/DELETE', 'HTTP状态码/200/301/302/404/500', 'HTTP请求头/Request Headers', 'HTTP响应头/Response Headers', 'Keep-Alive/长连接', 'Cookie/Session/会话管理', 'HTTP缓存/Cache-Control', 'ETag/Last-Modified', '代理服务器/Proxy', 'HTTPS/TLS/SSL加密', 'SSL握手/TLS Handshake', '证书/Certificate/CA', '对称加密 vs 非对称加密', 'DNS域名系统/Domain Name System', '根域名服务器/Root Server', '顶级域名/TLD/.com/.cn/.org', '权威DNS/Authoritative DNS', '递归查询/Recursive Query', '迭代查询/Iterative Query', 'DNS记录类型/A/AAAA/CNAME/MX/TXT', 'DNS缓存/Caching', 'DNS TTL/生存时间', 'DNS负载均衡', 'DNS安全/DNSSEC', 'DNS-over-HTTPS/DoH', 'DHCP动态主机配置/Dynamic Host', 'DHCP Discover/Offer/Request/ACK', 'DHCP租约/DHCP Lease', 'DHCP续租/Renew', 'DHCP中继/Relay Agent', 'DHCPv6/IPv6 DHCP', 'DHCP地址池/Pool', '保留地址/Reservation', 'FTP文件传输协议/File Transfer', '主动模式/Active Mode/PORT', '被动模式/Passive Mode/PASV', 'FTP命令/PUT/GET/LIST', 'SFTP/SSH文件传输', 'FTPS/FTP over SSL', 'TFTP简单文件传输', 'SMTP简单邮件传输/Simple Mail', 'POP3邮局协议/Post Office', 'IMAP4互联网消息访问/Internet Message', '邮件发送/MUA/MTA/MDA', 'MIME/多用途互联网邮件扩展', 'Base64编码/邮件附件', 'SSH安全外壳/Secure Shell', 'SSH密钥/公钥私钥', 'SCP安全拷贝/Secure Copy', 'SNMP简单网络管理/Simple Network', 'SNMPv1/v2c/v3', 'Get/Set操作', 'Trap告警/通知', 'MIB管理信息库', 'OID对象标识符', 'NTP网络时间协议/Network Time', 'LDAP轻量目录访问/Lightweight', 'RDP远程桌面/Remote Desktop', 'VNC远程桌面', 'Telnet/明文远程登录', 'RADIUS远程认证/Dial-In User Service', 'TACACS+/Terminal Access Controller', 'WebSocket/全双工通信', 'WebRTC/实时通信']
                },
                '网络排障': {
                    'desc': '使用ping、traceroute、Wireshark等工具排查故障',
                    'difficulty': 2,
                    'dimensions': ['网络排障概述/Troubleshooting', '分层排障法/OSI分层', '自顶向下法/Top-Down', '自底向上法/Bottom-Up', '替换法/Divide and Conquer', '分而治之/逐段排查', '物理层排障/Physical Layer', '链路层排障/Data Link', '网络层排障/Network Layer', '传输层排障/Transport Layer', '应用层排障/Application', 'ping命令/ICMP回显', 'ping -t/持续ping', 'ping -l/指定包大小', 'ping -a/解析主机名', 'ping -f/不分片', 'traceroute路由追踪/Windows tracert', 'traceroute原理/TTL递增', 'tracert vs traceroute区别', 'pathping/统计+路由', 'ipconfig/Windows IP配置', 'ifconfig/Linux IP配置', 'ip addr show/查看IP', 'netstat/查看连接状态', 'netstat -an/显示所有', 'netstat -r/路由表', 'ss命令/Linux Socket', 'arp -a/查看ARP表', 'arp -d/清除ARP', 'route/查看路由表', 'route print/Windows', 'ip route/Linux路由', 'nslookup/DNS查询', 'dig/DNS详细查询', 'host/DNS查询', 'dnsenum/DNS枚举', 'nmap端口扫描/Network Mapper', 'nmap -sS/ SYN扫描', 'nmap -sT/TCP扫描', 'nmap -sU/UDP扫描', 'nmap -O/系统识别', 'Wireshark抓包/Protocol Analyzer', '过滤器/Filter/Display Filter', 'BPF过滤器/Capture Filter', 'tcpdump命令行抓包', 'tcpdump -i/指定接口', 'tcpdump -w/保存文件', 'tcpdump -r/读取文件', 'tshark命令行Wireshark', 'Follow TCP Stream/追踪流', 'Expert Info/专家信息', '统计/Statistics/流量分析', 'IO Graph/IO图表', 'TCP三次握手分析', 'TCP四次挥手分析', 'DNS查询分析', 'HTTP请求分析', '排除法/Elimination', '逐一排查/Isolate', '日志分析/Log Analysis', '设备日志/Syslog', '日志级别/Level', '性能基线/Baseline', '对比法/历史对比', 'Sniffer Pro抓包', 'SolarWinds工具', '网络监控系统/Grafana']
                },
                '网络监控': {
                    'desc': 'SNMP、Zabbix等网络监控工具',
                    'difficulty': 2,
                    'dimensions': ['网络监控概述/Monitoring', '监控目标/可用性/性能/安全', '主动监控/Active Monitoring', '被动监控/Passive Monitoring', 'SNMP简单网络管理/Simple Network', 'SNMP架构/Manager-Agent', 'SNMPv1/v2c/v3区别', 'Community字符串/团体名', 'SNMP GET/GETNEXT', 'SNMP SET/写入', 'SNMP TRAP/主动告警', 'SNMP INFORM/确认告警', 'MIB管理信息库/Management', 'OID对象标识符', '标准MIB/MIB-II', '设备MIB/厂商MIB', 'SNMP轮询/Polling', 'SNMP Trap接收', 'MIB Browser/浏览器', 'Zabbix监控/Centum/开源', 'Zabbix Server/Agent架构', 'Zabbix Proxy分布式', '主机/Host/模板/Template', '监控项/Item/键值/Key', '触发器/Trigger/阈值', '告警/Alert/Action', '模板继承/Template Link', '自动发现/Auto Discovery', '网络发现/Network Discovery', 'Zabbix Agent/Linux/Windows', 'Zabbix Sender/主动上报', 'Zabbix API/自动化', 'Prometheus监控系统', 'Prometheus Pull模式', 'Exporter/指标导出', 'node_exporter', 'cAdvisor容器监控', 'Pushgateway/推送网关', 'Grafana可视化/展示', 'PromQL查询语言', 'Alertmanager告警', 'Cacti流量监控/SNMP', 'RRDtool轮询绘图', 'SolarWinds NPM/Orion', 'SolarWinds NPM', 'PRTG/Paessler Router Traffic', 'PRTG传感器/Sensor', 'Nagios监控系统', 'Nagios Core/免费版', 'Nagios XI/商业版', 'Centreon/法国开源', 'OpenNMS/Java监控', 'LibreNMS/PHP SNMP', '网络设备监控/CPU/内存', '接口流量监控/Inbound/Outbound', '带宽监控/Bandwidth', '延迟监控/Latency', '丢包监控/Packet Loss', '抖动监控/Jitter', 'Syslog日志收集', '日志聚合/ELK Stack', 'Grafana+Loki+Promtail', '监控大屏/Dashboard', 'SLA服务等级协议', '可用性报告/Uptime', '告警收敛/Aggregation', '告警抑制/Deduplication', '告警升级/Escalation']
                },
                '防火墙': {
                    'desc': '网络安全边界防护设备配置和管理',
                    'difficulty': 2,
                    'dimensions': ['防火墙概述/Firewall', '防火墙类型/硬件/软件/云', '包过滤防火墙/Packet Filtering', '状态检测防火墙/Stateful Inspection', '应用层防火墙/Proxy/代理', '下一代防火墙/NGFW/Deep Inspection', '防火墙区域/Zone/Security Zone', '信任区/Trust Zone', '不信任区/Untrust Zone', 'DMZ区/隔离区', '本地/Local Zone', '区域优先级/优先级', '安全策略/Security Policy', '默认策略/Deny All', '策略匹配顺序/从上到下', '源地址/Source Address', '目的地址/Destination', '服务/Service/协议端口', '应用控制/Application Control', '用户身份认证/User Identity', '时间计划/Time Schedule', '会话管理/Session', '连接跟踪/Connection Tracking', '状态表/State Table', '会话超时/Session Timeout', '长连接/Keep-Alive', 'NAT与防火墙', '源NAT/ SNAT', '目的NAT/DNAT/端口映射', '双向NAT', 'Server Map/服务器映射', '黑洞路由/Black Hole Route', '攻击防护/Defense', 'DDoS防护/SYN Flood', 'ICMP Flood防护', 'UDP Flood防护', '扫描防护/Port Scan', 'IP欺骗防护/Spoofing', 'Land Attack防护', 'Ping of Death防护', 'IP分片防护', 'ARP防护/ARP欺骗', '应用层防护/WAF', '入侵检测/IPS', '入侵防御/IPS', 'URL过滤/URL Filter', '内容过滤/Content Filter', '病毒防护/Anti-Virus', '僵尸网络防护/Botnet', '威胁情报/Threat Intelligence', '威胁签名/Signature', '行为分析/Behavior Analysis', '沙箱检测/Sandbox', 'SSL解密/Inspection', '证书验证/Certificate', '流量控制/QoS', '带宽限制/Rate Limit', '会话限制/Connection Limit', '负载均衡/FWLB/Active-Active', '高可用/HA/主备/主主', '故障切换/Failover', '会话同步/Session Sync', '接口配置/IP/MTU', 'VLAN接口/子接口', '链路聚合/Redundancy', 'Bypass卡/故障 bypass', '策略路由/PBR', '路由策略/Route Policy', '日志审计/Log/审计', '集中管理/Central Management', '集中配置下发', '策略备份/Configuration Backup', '策略优化/清理冗余策略', '防火墙吞吐/Throughput', '新建连接/Connection Rate', '并发会话/Concurrent Session', '华为防火墙/USG', '思科防火墙/ASA/Firepower', 'Juniper防火墙/SRX', 'Fortinet防火墙/FortiGate', '天融信防火墙/Topsec', '启明星辰防火墙', '绿盟防火墙/NF', 'Palo Alto防火墙/PA']
                },
                'BGP': {
                    'desc': '边界网关协议，互联网核心路由协议',
                    'difficulty': 3,
                    'dimensions': ['BGP概述/Border Gateway Protocol', 'BGP特点/路径矢量/TCP 179', 'BGP邻居关系/Peer', 'IBGP内部BGP/同一AS', 'EBGP外部BGP/不同AS', 'BGP TCP连接/端口179', 'BGP消息类型/Open/Update/Notify', 'BGP状态机/Idle/Connect/Active', 'OpenSent/OpenConfirm/Established', 'BGP路由属性/Attributes', 'AS-Path/AS路径属性', 'Next-Hop/下一跳属性', 'Origin/起源属性', 'Local Preference/本地优先', 'MED/多出口鉴别器/Multi-Exit', 'Weight/思科权重属性', 'Community/团体属性', 'BGP路由选择/8条规则', 'BGP路由优先级/首选本地', 'AS-Path长度/最短AS Path', 'Origin类型/IGP>EGP>Incomplete', 'MED比较/IGP vs EGP', 'BGP路由聚合/Aggregate', 'BGP自动聚合/手动聚合', 'AS-SET/聚合AS路径', 'BGP防环/AS-Path Loop', 'IBGP水平分割/Horizon', 'BGP同步/Synchronization', 'BGP路由反射器/RR', 'Route Reflector/路由反射器', 'Cluster ID/集群ID', 'Originator ID/起源ID', 'BGP联盟/Confederation', '联盟ID/子AS号', 'BGP路由过滤/Filter', 'BGP邻居认证/Authentication', 'MD5认证', 'BGP路由映射/Route Map', 'BGP正则表达式/AS-Path Regex', 'AS路径列表/AS-Path List', '前缀列表/Prefix List', 'BGP团体/Community', 'No-Export团体', 'No-Advertise团体', 'Route Refresh/路由刷新', 'BGP Dampening/路由抖动', '惩罚值/Penalty', '半衰期/Half-life', '重用阈值/Reuse Limit', '抑制阈值/Suppress Limit', 'BGP多宿主/Multi-Homing', '负载均衡/ECMP', 'BGP路径选择/负载', 'BGP GR/Graceful Restart', 'BFD双向转发检测', 'BGP计时器/Holdtime/Keepalive', 'BGP路由优选/Preference', 'BGP路由宣告/Network', 'BGP路由注入', 'BGP路径属性管理', 'BGP性能优化', 'BGP集群间流量优化', '运营商BGP/ISP BGP', 'BGP选路原则详解', 'BGP团体属性应用', 'Route-Target/VPN目标', 'MPLS VPN与BGP', 'IPv6 BGP/MP-BGP', 'BGP安全/BGPsec', 'RPKI/资源公钥基础设施', 'BGP Flowspec/流量规范', 'BGP TTL Security/Hop Limit']
                },
                'Cisco': {
                    'desc': '思科网络设备配置和管理，CCNA/CCNP认证相关技术',
                    'difficulty': 3,
                    'dimensions': ['思科概述/Cisco Systems', 'Cisco IOS操作系统', 'CLI命令行界面', '用户模式/EXEC', '特权模式/Privileged', '全局配置模式/Global Config', '接口配置模式/Interface', '路由配置模式/Router Config', '常用命令/show', 'show version/版本信息', 'show ip interface brief', 'show running-config', 'show startup-config', 'show ip route/路由表', 'show ip protocols', 'show access-lists', 'show vlan brief', 'show interfaces status', 'show mac address-table', 'CDP/Cisco Discovery', 'LLDP链路层发现', 'telnet远程登录', 'SSH配置', 'line vty/虚拟终端', 'enable密码/enable password', 'enable secret/加密密码', 'service password-encryption', 'banner motd/登录提示', 'hostname/主机名', 'ip address/接口IP', 'no shutdown/启用接口', 'description/接口描述', 'speed/duplex/速率双工', 'switchport mode access', 'switchport mode trunk', 'switchport trunk allowed vlan', 'switchport trunk native vlan', 'DTP动态中继协议', 'VLAN创建/vlan id', 'name/ VLAN命名', 'interface range/端口组', 'IP路由配置/ip route', '默认路由/ip route 0.0.0.0', 'RIP路由协议配置', 'network命令/宣告网络', 'passive-interface/被动接口', 'OSPF配置/router ospf', 'router-id/路由ID', 'network area/区域宣告', 'area 0/骨干区域', 'EIGRP配置/router eigrp', 'autonomous-system/AS号', 'network命令/EIGRP宣告', 'BGP配置/router bgp', 'neighbor/邻居配置', 'BGP network宣告', 'ACL配置/access-list', 'ip access-group/应用ACL', 'NAT配置/ip nat inside', 'inside source/源NAT', 'static nat/静态NAT', 'DHCP配置/ip dhcp pool', 'network/地址池', 'default-router/网关', 'dns-server/DNS服务器', 'VPN配置/IPSec', 'crypto isakmp/ISAKMP', 'crypto ipsec/IPSec', 'transform-set/转换集', 'crypto map/密码图', 'interface Tunnel/隧道接口', 'GRE隧道/GRE Tunnel', 'STP生成树配置', 'spanning-tree mode', 'portfast/快速端口', 'bpduguard/BPDU保护', 'root guard/根保护', ' EtherChannel/链路聚合', 'channel-group mode', 'LACP/PAGP协议', 'HSRP热备份路由/Standby', 'VRRP虚拟路由冗余', 'GLBP网关负载均衡', '堆叠/StackWise', 'VSS虚拟交换系统', 'SPAN端口镜像', 'RSPAN远程镜像', 'ERRDISABLE恢复', 'CDP和LLDP配置', 'Cisco CNA/网络助手', 'Cisco PCM/配置管理', 'Cisco Prime', 'Cisco DNA Center', 'SD-Access/软件定义接入', 'SD-WAN/软件定义广域', 'Viptela/SD-WAN方案', 'Meraki云管理', 'ISO镜像升级', '密码恢复/Password Recovery', '配置保存/copy run start', '配置备份/备份恢复', 'TFTP/FTP备份', 'Cisco认证/CCNA/CCNP/CCIE']
                },
                'H3C': {
                    'desc': '华三网络设备配置和管理',
                    'difficulty': 3,
                    'dimensions': ['H3C概述/华三通信/H3C', 'Comware操作系统', 'Comware CLI命令视图', '用户视图/User View', '系统视图/System View', '接口视图/Interface View', '路由视图/Router View', 'display命令/查看信息', 'display version/版本', 'display interface brief', 'display current-configuration', 'display ip routing-table', 'display vlan', 'display mac-address', 'sysname/主机名', 'ip address/接口IP', 'undo shutdown/启用接口', 'description/接口描述', 'vlan/创建VLAN', 'port access/接入端口', 'port trunk/中继端口', 'port hybrid/混合端口', 'port-isolate/端口隔离', 'link-protocol/链路协议', 'loopback/环回接口', 'VLAN配置/vlan batch', 'interface vlan-interface', 'STP生成树/MSTP', 'stp mode/生成树模式', 'stp enable/启用生成树', '端口安全/Port Security', 'dot1x/IEEE 802.1X', 'MAC地址绑定', 'ARP绑定/静态ARP', 'IP路由/静态路由/ip route-static', '默认路由/ip route-static 0.0.0.0', 'RIP配置/rip', 'network/网络宣告', 'version/版本选择', 'OSPF配置/ospf', 'area/区域配置', 'network/区域网络', 'BGP配置/bgp', 'peer/邻居配置', 'BFD双向转发检测', 'BGP联盟/Confederation', '路由反射器/Reflector', '路由策略/route-policy', 'if-match/匹配条件', 'apply/应用动作', 'ACL配置/acl', 'rule/规则配置', 'packet-filter/包过滤', 'Traffic Classifier/流分类', 'Traffic Behavior/流行为', 'Traffic Policy/流策略', 'NAT配置/nat', 'nat address-group/地址池', 'nat outbound/出向NAT', 'nat server/服务器映射', 'easy-ip/出口IP', 'DHCP配置/dhcp enable', 'dhcp server/服务器', 'network/地址池', 'gateway-list/网关', 'dns-list/DNS', 'dhcp relay/中继', 'VPN配置/IPSec', 'ike/ISAKMP配置', 'ipsec/安全联盟', 'proposal/提议', 'tunnel interface/隧道', 'GRE隧道/隧道配置', 'L2TP VPN/Layer 2 Tunnel', 'SSL VPN配置', '防火墙/zone/安全域', 'security-policy/安全策略', 'hrp/双机热备', 'hrp enable/启用热备', 'hrp track/端口跟踪', '堆叠/IRF/Intelligent Resilient', 'MAD/多主检测', '链路聚合/link-aggregation', '静态聚合/手动聚合', 'LACP动态聚合', 'QOS配置/qos', 'CAR/流量监管', 'GTS/通用流量整形', 'WFQ/加权公平队列', 'PQ/优先队列', 'CBQ/基于类的队列', '日志配置/info-center', 'loghost/日志主机', 'NTP配置/ntp-server', 'SNMP配置/snmp-agent', 'syslog/send log', '配置保存/save', '下次启动配置', '配置文件管理', 'H3C认证/H3CNE/H3CSE']
                },
                'OSPF': {
                    'desc': '开放式最短路径优先，内部网关路由协议',
                    'difficulty': 3,
                    'dimensions': ['OSPF概述/Open Shortest Path First', '链路状态路由/Link-State', 'SPF算法/Dijkstra', '最短路径树/SPT', 'OSPF区域/Area', '骨干区域/Area 0/Backbone', '非骨干区域/Non-Backbone', '常规区域/Regular Area', 'Stub区域/末节区域', 'Totally Stub/完全末节', 'NSSA/Not So Stubby Area', 'Totally NSSA', 'OSPF路由器类型/IR/ABR/ASBR', 'Internal Router/内部路由器', 'Backbone Router/骨干路由器', 'Area Border Router/ABR', 'AS Border Router/ASBR', 'LSA类型/LSA 1/2/3/4/5/7', 'Router LSA/LSA Type 1', 'Network LSA/LSA Type 2', 'Summary LSA/LSA Type 3', 'Summary ASBR LSA/LSA Type 4', 'External LSA/LSA Type 5', 'NSSA LSA/LSA Type 7', 'OSPF邻居关系/Neighbor', '邻居状态/Full/2-Way', 'Down/初始状态', 'Attempt/尝试', 'Init/初始化', '2-Way/双向', 'Exstart/交换开始', 'Exchange/交换', 'Loading/加载', 'Full/邻接完成', 'DR/BDR选举/指定路由器', 'DR/Designated Router', 'BDR/Backup DR', 'DR选举规则/Priority', 'OSPF网络类型/Point-to-Point', 'Broadcast/广播多路访问', 'NBMA/非广播多路访问', 'Point-to-Multipoint', 'Hello报文/Hello Interval', 'Dead Interval/死亡间隔', 'Wait计时器', 'Poll Interval/轮询间隔', 'LSA泛洪/Flooding', 'LSA确认/Acknowledgment', '序列号/Sequence Number', '老化时间/Max Age', '路由汇总/Area Summary', 'ABR汇总/Summary', 'ASBR汇总/External Summary', '虚链路/Virtual Link', '隧道/Tunnel穿越', 'OSPF认证/Authentication', '区域认证/Area Auth', '接口认证/Interface Auth', 'Null认证/无认证', 'Plaintext/明文认证', 'MD5认证/加密认证', 'OSPF Cost/链路代价', '带宽参考值/Reference', 'auto-cost reference-bandwidth', '路由优先级/Preference', 'OSPF外部路由/E1/E2', 'NSSA外部路由/N1/N2', 'OSPFv3/IPv6 OSPF', 'OSPFv3实例/Instance', 'OSPFv3链路本地地址', 'OSPF多实例', 'OSPFv2 vs OSPFv3', 'LSA选项/DoNotAge', 'OSPF路由过滤/Filter', 'OSPF路由引入/Import', 'OSPF外部路由引入', '默认路由/Default Route', 'default-information originate', 'OSPF路由重分发', 'OSPF调优/Timing', 'Hello/Dead Timer', '重传间隔/Retransmit', '泛洪间隔/Flood Delay', '攻角/LSA Arrival', 'OSPF路由汇总/区域', 'OSPF路由聚合/ABR', 'OSPF路由聚合/ASBR', 'OSPF路由选择/Intra-Area', 'Inter-Area/区域间', 'External/外部路由', 'OSPF末节区域', 'OSPF完全末节', 'OSPF NSSA区域', 'LSA Filtering/过滤', 'OSPF GR/Graceful Restart', 'OSPF PF/Fast Convergence', 'BFD联动/Failure Detection']
                },
                'STP': {
                    'desc': '生成树协议，防止网络环路',
                    'difficulty': 3,
                    'dimensions': ['STP概述/Spanning Tree Protocol', '广播风暴/Broadcast Storm', 'MAC地址震荡/MAC Address Flapping', '重复帧/Multiple Frame Copies', 'STP树形拓扑/无环', '生成树算法/STA', 'BPDU网桥协议数据单元', 'BPDU类型/Config BPDU', 'BPDU类型/TCN BPDU', 'Bridge ID/网桥ID', 'Priority + MAC/优先级', '默认优先级/32768', '系统ID扩展/SysIDExt', '根桥/Root Bridge', '根桥选举/优先级+MAC', '根端口/Root Port/RP', '指定端口/Designated Port/DP', '阻塞端口/Blocking Port/BP', '端口状态/Blocking/20s', 'Listening/15s', 'Learning/15s', 'Forwarding', 'Disabled/禁用', '端口开销/Port Cost', 'Path Cost/路径开销', '根桥路径开销/Root Path Cost', 'BPDU Hello Time/2s', 'Forward Delay/15s', 'Max Age/20s', '802.1D标准STP', 'RSTP快速生成树/802.1w', 'RSTP端口角色/Backup/Alternate', 'RSTP边缘端口/Edge Port', 'RSTP提案-同意/Proposal-Agreement', 'RSTP同步/P sync', 'RSTP收敛/快收敛', 'RSTP vs STP区别', 'MSTP多实例生成树/802.1s', 'Instance/实例', 'VLAN映射/Mapping', 'IST/内部生成树', 'CST/公共生成树', 'CIST/公共内部生成树', 'CIST根/CIST Root', '区域根/Regional Root', 'MSTP配置/region-name', 'revision-level/修订级别', 'instance vlan/实例VLAN映射', 'MSTP vs RSTP vs STP', 'PVST每VLAN生成树/Cisco', 'PVST+/Per VLAN Spanning+', 'Rapid-PVST+/RSTP+ per VLAN', 'STP防护/BPDU Guard', 'BPDU保护/边缘端口', 'BPDU Filter/过滤BPDU', 'Root Guard/根保护', 'Loop Guard/环路保护', 'UDLD/单向链路检测', 'Storm Control/风暴控制', 'Broadcast/Multicast/Unknown', '一级防护/一级保护', 'TCN防护/TCN Intercept', 'TCN BPDU Protection', 'TC BPDU Guard', '端口角色恢复', 'TCN超时/Max Age', 'STP选举过程', '根桥选举/全网最小BID', '根端口选举/最小RPC', '指定端口选举/最小Sender BID', '根路径开销计算', 'STP拓扑变更', 'TCN通知/TCN', 'TC置位/Topology Change', 'MAC地址表更新', '计时器调整注意', 'uplinkfast/上行链路快', 'backbonefast/骨干快', 'Cisco STP增强', 'HWTACACS/端口安全', '堆叠与STP', 'VSS与STP', 'M-LAG与STP', 'BFD与STP联动', 'P/A机制/Proposal Agreement']
                },
                'VPN': {
                    'desc': '虚拟专用网络，IPSec和SSL VPN配置',
                    'difficulty': 3,
                    'dimensions': ['VPN概述/Virtual Private Network', 'VPN类型/远程访问/站点到站点', '远程访问VPN/Remote Access', '站点到站点/Site-to-Site', '专线/VPN vs 专线', '隧道/Tunnel/隧道协议', '封装/Encapsulation', '加密/Encryption', '认证/Authentication', '数据完整性/Integrity', 'IPSec协议族/IKE/ESP/AH', 'IPSec两种协议/ESP/AH', 'ESP封装安全载荷/Encapsulating', 'ESP加密/Encryption', 'ESP认证/Authentication', 'ESP头部/IP/ESP', 'AH认证头/Authentication Header', 'AH完整性保护', 'AH vs ESP区别', 'IKE互联网密钥交换/v1/v2', 'IKE Phase 1/第一阶段', 'Main Mode/主模式', 'Aggressive Mode/野蛮模式', 'ISAKMP SA/安全关联', 'IKE Phase 2/第二阶段', 'Quick Mode/快速模式', 'IPSec SA/安全关联', 'DH密钥交换/Diffie-Hellman', 'DH组/Group 1/2/5/14', '加密算法/AES/DES/3DES', 'AES-128/AES-192/AES-256', 'DES/3DES淘汰', '哈希算法/MD5/SHA-1/SHA-2', 'SHA-256/SHA-384/SHA-512', '认证方法/预共享密钥/PSK', '证书认证/Digital Certificate', 'RSA签名/数字签名', 'NAT穿越/NAT-T/NAT Traversal', 'IPSec VPN配置步骤', '第一阶段配置/IKE', 'crypto isakmp policy', 'encryption aes', 'hash sha', 'authentication pre-share', 'DH group', '第二阶段配置/IPSec', 'crypto ipsec transform-set', 'mode tunnel/crypto map', 'crypto map/绑定接口', '感兴趣流量/ACL', 'isakmp key/预共享密钥', 'site-to-site VPN/路由器间', ' GRE通用路由封装', 'GRE over IPSec', 'Tunnel mode/传输模式', 'Tunnel mode/隧道模式', 'IPSec隧道模式', 'IPSec传输模式', 'DMVPN动态多点VPN', 'NHRP/下一跳解析', 'mGRE/多点GRE', 'IPSec保护GRE', 'FlexVPN/Cisco解决方案', 'SSL VPN概述/SSL/TLS', 'SSL VPN vs IPSec VPN', 'SSL VPN无客户端', 'Web VPN/无客户端', 'Client VPN/SSL客户端', 'SSL VPN网关', 'SSL VPN门户', '资源访问/内网应用', 'SSL VPN插件/Citrix', 'AnyConnect/Cisco客户端', 'OpenVPN/开源SSL VPN', 'L2TP VPN/第二层隧道', 'L2TP over IPSec', 'L2TP/IPSec组合', 'PPTP VPN/点对点隧道', 'PPTP vs L2TP vs IPSec', 'VxLAN/虚拟可扩展LAN', 'VxLAN隧道/VNI', 'VxLAN网关', 'WireGuard/现代VPN', 'WireGuard密钥对/公钥', 'WireGuard配置简单', 'WireGuard性能高', 'MPLS VPN/运营商VPN', 'MPLS标签/Label', 'LDP标签分发协议', 'VRF/虚拟路由转发', 'RD/路由区分符', 'RT/路由目标', 'MPLS VPN架构/CE/PE/P', 'VPN高可用/HA', 'VPN冗余/Failover', 'VPN性能/Throughput', 'VPN带宽管理']
                },
                'VRRP': {
                    'desc': '虚拟路由冗余协议，实现网关高可用',
                    'difficulty': 3,
                    'dimensions': ['VRRP概述/ Virtual Router Redundancy', 'VRRP作用/网关冗余', 'HSRP热备份路由协议/Cisco', 'HSRP vs VRRP区别', 'GLBP网关负载均衡协议', 'VRRP版本/VRRPv2/v3', 'VRRPv3/IPv6支持', 'VRRP组/Virtual Router', '虚拟IP地址/Virtual IP', '虚拟MAC地址/Virtual MAC', '虚拟路由器/Virtual Router', '主路由器/Master', '备份路由器/Backup', 'VRRP优先级/Priority', '默认优先级/100', 'Priority 255/IP地址拥有者', 'Priority 0/主设备停止', 'VRRP抢占/Preempt', '抢占延迟/Preempt Delay', 'VRRP定时器/Timers', 'Hello间隔/Hello Interval', 'Master Down Interval', 'Backup Master选举', 'VRRP状态/Master/Backup', 'VRRP通告/Advertisement', 'VRRP track/跟踪', 'Track接口/Interface Tracking', 'Track路由/Route Tracking', 'Track优先级下降', 'VRRP认证/Authentication', '明文认证/Plain Text', 'MD5认证', 'VRRP负载均衡', 'VRRP多组/配置多组', 'MSTP+VRRP联动', 'VRRP配置/vrrp group', 'vrrp priority/优先级', 'vrrp preempt/抢占', 'vrrp timers/定时器', 'vrrp track/跟踪', 'VRRP简明配置', '华为VRRP配置', '思科VRRP配置', 'VRRP双主/双活问题', 'VRRP单网关问题', 'VRRP优化/增强功能', 'VRRP关联BFD', 'BFD快速检测', 'VRRP与OSPF联动', 'VRRP备份通道', 'VRRP日志/监控', 'VRRP故障切换', 'VRRP收敛时间', 'VRRP性能指标', '高可用网关方案', '负载均衡VRRP', 'VGMP/华为组管理', 'VGMP组优先级', 'HRP/华为冗余协议', 'HRP主备备份', 'HRP双活组负载', 'NQA+VRRP联动', 'NQA/网络质量分析', 'E-Trunk/以太网聚合', '堆叠+VRRP方案', 'M-LAG+VRRP', 'VXLAN+VRRP', 'SDN与VRRP', '控制器部署']
                },
                '华为设备': {
                    'desc': '华为路由交换设备配置，HCIA/HCIP认证',
                    'difficulty': 3,
                    'dimensions': ['华为概述/Huawei', 'VRP通用路由平台/Versatile', 'VRP5/VRP8版本', '命令行视图/View', '用户视图/User-View', '系统视图/System-View', '接口视图/Interface', '路由协议视图/Protocol', 'display命令族', 'display version/版本', 'display current-configuration', 'display interface/接口信息', 'display ip interface brief', 'display vlan/ VLAN信息', 'display mac-address/ MAC', 'display stp/生成树', 'display ospf/OSPF信息', 'display bgp/BGP信息', 'display ip routing-table', 'sysname/主机名', 'clock datetime/系统时间', 'header login/登录提示', 'ftp server enable/FTP', 'stelnet enable/SSH', 'user-interface/用户接口', 'authentication-mode/认证', 'protocol inbound/协议', 'ip address/接口IP', 'undo shutdown/启用', 'description/描述', 'mtu/最大传输单元', 'combo-port/Combo口', 'vlan batch/批量创建', 'port default vlan/接入', 'port trunk allow-pass', 'port isolate/端口隔离', 'stp enable/启用生成树', 'stp mode/生成树模式', 'stp root/根桥设置', 'stp tc-protection/TC保护', 'loopback/环回接口', '静态路由/ip route-static', '默认路由/ip route-static 0.0.0.0', 'RIP配置/rip', 'ospf/进程号', 'area/区域配置', 'network/网络宣告', 'import-route/路由引入', 'bgp/AS号', 'peer/邻居配置', 'mpls/启用MPLS', 'mpls ldp/标签分发', 'vlanif/三层VLANIF', 'vrrp vrid/VRRP组', 'virtual-ip/虚拟IP', 'priority/优先级', 'preempt/抢占', 'track interface/跟踪', 'acl/访问控制列表', 'rule/规则配置', 'traffic-filter/流量过滤', 'nat/地址转换', 'nat address-group/地址池', 'nat server/服务器映射', 'easy-ip/出口转换', 'dhcp enable/启用DHCP', 'dhcp server/服务器', 'network/地址池', 'gateway-list/网关列表', 'dns-list/DNS服务器', 'dhcp relay/中继', 'qos/服务质量', 'CAR/流量监管', 'GTS/流量整形', 'HQoS/层次化QoS', 'snmp-agent/ SNMP配置', 'info-center enable/日志', 'ntp-server/时间服务器', 'ssh user/SSH用户', 'ssh authentication-type/认证', 'stelnet/安全Telnet', 'sftp enable/SFTP', 'stack/堆叠配置', '成员优先级/Stack Priority', '堆叠ID/Stack ID', 'MAD检测/Multi-Award Detect', '链路聚合/Eth-Trunk', '手工负载分担/Manual', 'LACP模式/LACP', 'BFD双向转发检测', 'bfd/启用BFD', 'if-match/匹配', 'apply/应用', 'route-policy/路由策略', 'filter-policy/过滤策略', '路由聚合/aggregate', 'ISIS配置/IS-IS', 'PIM组播/PIM-SM/PIM-SSM', 'IGMP Snooping', '用户权限级别/Level', 'FTP/TFTP升级', '配置文件备份/save', '下次启动配置文件', '华为认证/HCIA/HCIP/HCIE']
                },
                '负载均衡': {
                    'desc': 'F5、Nginx等负载均衡设备配置',
                    'difficulty': 3,
                    'dimensions': ['负载均衡概述/Load Balancing', '负载均衡器/Load Balancer', '硬件负载均衡/F5/A10/Citrix', '软件负载均衡/Nginx/HAProxy/LVS', '云负载均衡/ALB/NLB/CLB', '四层负载均衡/L4/Transport', 'TCP负载均衡', '七层负载均衡/L7/Application', 'HTTP负载均衡', 'DNS负载均衡', '全局负载均衡/GSLB', '轮询/Round Robin', '加权轮询/Weighted Round Robin', '最少连接/Least Connections', '加权最少连接/Weighted Least', 'IP Hash/IP哈希', 'URL Hash/URL哈希', '一致性哈希/CONSISTENT HASH', '最小响应时间/Least Response', '健康检查/Health Check', 'TCP检查/端口检查', 'HTTP检查/HTTP_GET', 'HTTPS检查', 'HTTPS证书验证', '主动健康检查', '被动健康检查', '故障检测/Failure Detection', '故障转移/Failover', '会话保持/Session Persistence', 'Cookie会话保持/Sticky Cookie', 'Session Cookie', '源IP会话保持/Source IP', 'L7 Cookie', '连接复用/Connection Reuse', 'Keep-Alive复用', 'SSL终止/SSL Termination', 'SSL卸载/SSL Offload', '证书配置/Certificate', 'HTTPS配置', '后端服务器/Real Server', '服务器池/Server Pool', '成员/Server Member', '权重/Weight', '备份服务器/Backup', '主备模式/Active-Passive', '双活模式/Active-Active', 'NAT模式/负载均衡', 'DR直接路由/Direct Routing', 'IP隧道模式/Tunnel', 'TUN模式', '反向代理模式/Proxy', 'F5负载均衡器/Big-IP', 'F5 LTM/本地流量管理', 'F5 VS/Virtual Server', 'F5 Pool/服务器池', 'F5 Node/节点', 'F5 Monitor/健康检查', 'F5 iRule/脚本', 'F5profiles/协议配置', 'F5 Data Group', 'F5 OneConnect/连接复用', 'Nginx负载均衡/upstream', 'nginx upstream/服务器组', 'server/后端服务器', 'ip_hash/会话保持', 'least_conn/最少连接', 'keepalive/长连接', 'proxy_pass/反向代理', 'proxy_set_header/头信息', 'upstream_hash/哈希', 'least_time/最少时间', 'HAProxy负载均衡', 'HAProxy配置/frontend/backend', 'default_backend/默认后端', 'balance/算法', 'option httpchk/健康检查', 'option httpclose', 'cookie/会话保持', 'server/后端配置', 'maxconn/最大连接', 'LVS负载均衡/IPVS', 'LVS NAT模式', 'LVS DR直接路由', 'LVS TUN隧道模式', 'IPVSADM命令', '持续连接/IPVS persistent', '阿里云SLB/Server Load', 'SLB七层/HTTP/HTTPS', 'SLB四层/TCP/UDP', 'CLB传统负载均衡', 'ALB应用负载均衡', 'NLB网络负载均衡', '后端服务器组', '虚拟服务器/VServer', '会话同步/Session Sync', '连接限速/Connection Limit', '带宽限速/Bandwidth Limit', 'WAF防火墙集成', 'DDoS防护集成', '日志记录/Access Log', '监控指标/Metrics', 'QPS/每秒请求', '并发连接数', '响应时间/Latency', '后端响应时间', '上游超时/Upstream Timeout', '负载均衡算法选择', '性能优化', '故障排查']
                }
            }
        },
        '网络安全工程师': {
            'description': '负责网络安全防护，渗透测试和安全漏洞修复。',
            'skills': {
                'Nmap': {
                    'desc': '网络扫描和端口探测工具',
                    'difficulty': 2,
                    'dimensions': ['Nmap概述/Network Mapper/端口扫描', 'Nmap安装/Linux/Windows', '基本扫描/nmap target', '端口状态/Open/Closed/Filtered', '扫描技术类型', 'TCP SYN扫描/-sS/SYN', 'TCP connect扫描/-sT/CONNECT', 'UDP扫描/-sU', 'FIN扫描/-sF', 'NULL扫描/-sN', 'XMAS扫描/-sX', 'Ping扫描/-sn/-sP', '无Ping扫描/-P0/-PN', 'ACK扫描/-sA/路由追踪', 'Window扫描/-sW', 'Maazon扫描/-sM', '协议扫描/-sO/IP协议', '版本检测/-sV/Version', '操作系统检测/-O/OS Detection', '脚本扫描/--script/NSE', '默认脚本/safe/vuln/auth', '全面扫描/-A/OS+Script+Version', '快速扫描/-F/Top端口', '端口范围/-p/1-1000', '指定端口/-p 80,443', '端口列表/-p-全部端口', '排除主机/--exclude', '排除端口/--excludefile', '扫描速度/-T/Timing', 'T1-T5速度级别', '发送原始报文/-send-ip', '输出格式/-oA/-oN/-oX', '详细输出/-v/-vv', '调试模式/-d/-dd', '服务识别/Banner Grab', 'NSE脚本 vulners', 'vulscan漏洞扫描', 'http-enum/目录枚举', 'http-title/网站标题', 'dns-brute/子域名', 'smb-enum-shares', 'mysql-enum/MySQL', 'ms-sql-enum/MSSQL', '常见端口/SMB/SSH/HTTP', '防火墙检测/--script firewall', '分片扫描/-f/-ff', '诱饵扫描/-D/Decoy', '空闲扫描/-sI/Zombie', '源地址欺骗/-S', 'MAC地址伪造/--spoof-mac', '输出文件/nmap.xml/json', 'grep结果/nmap grep', 'Ndiff/差异扫描', 'Zenmap/GUI界面', '批量扫描/Shell脚本', 'Nmap与Python/nmap库', '自动化扫描/CI集成']
                },
                'Web安全': {
                    'desc': 'SQL注入、XSS、CSRF等Web攻击原理和防护',
                    'difficulty': 2,
                    'dimensions': ['OWASP Top 10/应用安全风险', 'SQL注入/SQL Injection', '注入原理/用户输入拼接SQL', '数字型注入', '字符型注入/单引号/双引号', '布尔盲注/Boolean Blind', '时间盲注/Time-based', '报错注入/Error-based', 'UNION注入/UNION Query', '堆叠注入/Stacked Injection', '宽字节注入/GBK编码', '二次注入/Second-order', '自动化SQL注入/SQLMap', 'SQLMap/--dbs/--tables', 'SQLMap/--dump/--os-shell', 'SQLMap/Tamper脚本', 'SQL注入防护/参数化查询', '预编译语句/Prepared Statement', '绑定变量/Bind Variable', '输入验证/Sanitize', '白名单过滤', '存储过程/Safe Procedure', 'ORM框架防注入', 'XSS跨站脚本/Cross-Site', '反射型XSS/Reflected', '存储型XSS/Stored', 'DOM型XSS/DOM-based', 'XSS原理/执行JavaScript', 'XSS payload/脚本标签', 'Cookie窃取/Session Hijacking', '键盘记录器/Keylogger', 'XSS钓鱼/Phishing', 'XSS蠕虫/Worm', 'BeEF框架/XSS框架', 'XSS Filter/过滤器', 'HTML转义/Entity Encoding', 'CSP内容安全策略', 'HttpOnly/Cookie属性', 'X-XSS-Protection头', 'CSRF跨站请求伪造/Cross-Site', 'CSRF原理/用户不知情提交', 'CSRF Token/令牌', 'SameSite Cookie属性', 'Referer检查', '双重提交Cookie', 'CSRF漏洞利用/POC', 'SSRF服务端请求伪造/Server', 'SSRF原理/服务端发起请求', 'SSRF内网探测', 'SSRF协议利用/file:///gopher://', 'SSRF Redis/6379', 'SSRF防御/URL验证', '协议限制白名单', 'XXE外部实体/XML External', 'XXE原理/加载外部实体', 'XXE读文件/File Disclosure', 'XXE Blind盲注', 'XXE防御/禁用外部实体', 'SSRF vs XXE vs CSRF', '文件上传漏洞/Upload', '绕过技术/Content-Type', '文件扩展名绕过', '.htaccess/配置文件', 'Apache解析漏洞', 'Nginx解析漏洞', 'webshell上传', '上传防护/白名单', 'MIME类型验证', '文件重命名', '内容检查/文件头', '文件删除/服务器存储', '文件包含/File Inclusion', '本地文件包含/LFI', '远程文件包含/RFI', 'PHP伪协议/php://input', 'Session包含/日志包含', '防御方法/禁用RFI', '代码执行/Code Execution', '命令执行/Command Execution', 'RCE/PHP eval/system', '命令注入/Command Injection', '反序列化漏洞/Deserialize', 'Java反序列化', 'Python pickle反序列化', 'Ruby YAML反序列化', '业务逻辑漏洞', '验证码绕过/Bypass', '越权访问/IDOR', '水平越权/同级访问', '垂直越权/提权', '支付漏洞/0元购', '并发问题/Race Condition', '接口未授权访问']
                },
                'Wireshark': {
                    'desc': '网络协议分析和抓包工具',
                    'difficulty': 2,
                    'dimensions': ['Wireshark概述/网络协议分析器', 'Wireshark下载安装', '网卡选择/Interface', '混杂模式/Promiscuous Mode', '捕获过滤器/Capture Filter', 'BPF语法/Berkeley Packet Filter', '主机过滤/host 192.168.1.1', '端口过滤/port 80', '协议过滤/tcp/udp/http', '方向过滤/src/dst', '逻辑运算/and/or/not', '显示过滤器/Display Filter', '过滤表达式/Protocol', 'TCP过滤/tcp.flags', 'HTTP过滤/http.request', 'ip.addr/IP地址', 'tcp.port/TCP端口', 'follow TCP Stream/追踪流', 'Follow HTTP Stream', 'Expert Info/专家信息', '错误信息/Error', '警告/Warning', '注意/Note', 'Packet Details/数据包详情', 'Frame/帧', 'Ethernet/以太网头', 'Internet Protocol/IP', 'Transmission Control/TCP', '应用层协议/HTTP/DNS', '数据包列表/Packet List', '时间戳/Timestamp', '相对时间/Relative Time', '首部数据包/Keep Alive', 'Packet Comments/注释', '颜色规则/Coloring Rules', 'Mark Packets/标记', '保存捕获/Save', '导出对象/Export Objects', '导出HTTP对象', '导出 SMB/FTP文件', 'IO Graphs/IO图表', 'Statistics菜单/统计', 'Protocol Hierarchy/协议分层', 'Conversations/会话统计', 'Endpoints/端点统计', 'HTTP Statistics', 'DNS Statistics', '流量图/Flow Graph', '时序图/Sequence Diagram', 'TCP重传分析', 'TCP三次握手', 'TCP四次挥手', 'TCP窗口大小/Window', 'TCP确认机制/ACK', 'TCP重传/Retransmission', 'TCP乱序/Out-of-Order', 'TCP RST重置', 'HTTP请求分析', 'HTTP响应码', 'HTTPS/TLS分析', 'TLS握手过程', '证书信息/Certificate', 'DNS查询分析', 'ARP分析/地址解析', 'ICMP分析/Ping', 'DHCP分析/租约', 'FTP分析/明文', 'Telnet分析/明文', 'SMB分析/共享文件', '蠕虫攻击分析', 'SYN Flood攻击', 'ARP欺骗分析', '恶意流量识别', 'tshark命令行/TShark', 'tshark -r读取文件', 'tshark -w保存', 'tshark -Y过滤', 'editcap裁剪数据包', 'mergecap合并文件', 'capinfos文件信息', 'text2pcap文本转包', 'Reassemble重组', 'TCP Stream Graph', 'Round Trip Time', 'Throughput Time Graph', '过滤器语法/Filters', '正则表达式过滤']
                },
                '等保合规': {
                    'desc': '网络安全等级保护测评和整改',
                    'difficulty': 2,
                    'dimensions': ['等保概述/等级保护/Protection Level', '等保1.0 vs 2.0区别', '五个保护等级/Level 1-5', '第一级/自主保护', '第二级/指导保护', '第三级/监督保护', '第四级/强制保护', '第五级/专控保护', '等保2.0新技术要求', '云计算/大数据/物联网', '移动互联/工控安全', '定级备案/Report Filing', '系统定级/定级报告', '专家评审/Review', '公安机关备案', '建设整改/Remediation', '安全通信网络', '安全区域边界', '安全计算环境', '安全管理中心', '等级测评/Assessment', '测评机构/CNAS', '测评流程/Procedure', '控制点/测评项', '测评指标/Guideline', '高风险判定指引', '测评方法/Interview/Document', '技术检测/Testing', '主机测评/操作系统', '数据库测评/MySQL/Oracle', '网络测评/防火墙/交换机', '应用测评/Web应用', '数据测评/Data', '管理制度测评', '安全管理机构', '安全管理人员', '安全管理制度', '安全建设管理', '安全运维管理', '技术防护体系', '网络安全/通信网络', '区域边界防护', '计算环境安全', '管理中心/集中管理', '入侵防范/IDS/IPS', '恶意代码防范', '数据安全/备份恢复', '身份鉴别/Authentication', '访问控制/ACL', '安全审计/Audit', '数据加密/Encryption', '敏感数据保护', '个人信息保护', '日志审计/Log', '堡垒机/Jump Server', '数据库审计/DAM', '漏洞扫描/Vulnerability', '渗透测试/Penetration', '安全管理制度', '应急响应预案', '灾难恢复计划', 'DRP/BCP', '物理安全/机房', '电磁防护/Environmental', '网络安全等级保护', 'GB/T 22239-2019标准', '通用要求/扩展要求', '安全物理环境', '安全通信网络', '安全区域边界', '安全计算环境', '安全管理中心', '安全管理制度', '安全管理机构', '安全管理人员', '安全建设管理', '安全运维管理', '物联网安全扩展', '云计算安全扩展', '移动互联扩展', '工业控制系统扩展', '等保整改方案', '安全管理平台/SOC', '态势感知/SA', '合规报告/整改报告']
                },
                '防火墙': {
                    'desc': '访问控制策略配置和网络边界防护',
                    'difficulty': 2,
                    'dimensions': ['防火墙概述/Firewall', '防火墙类型/硬件/软件/云', '包过滤/Packet Filtering', '状态检测/Stateful Inspection', '代理防火墙/Proxy', '下一代防火墙/NGFW', '防火墙区域/Zone', '信任区/Trust', '不信任区/Untrust', 'DMZ隔离区', '本地区域/Local', '安全策略/Policy', '默认策略/Deny All', '策略匹配顺序', '源地址/Source', '目的地址/Destination', '服务端口/Service', '用户身份/User', '时间计划/Schedule', '会话管理/Session', '连接跟踪/Connection', '状态表/State Table', 'NAT与防火墙', '源NAT/SNAT', '目标NAT/DNAT', '攻击防护/Defense', 'DDoS防护', 'SYN Flood防护', '扫描防护/Port Scan', 'IP欺骗防护', 'WAF功能/Web应用防火墙', '入侵检测/IPS', 'URL过滤/URL Filter', '内容过滤/Content', '病毒防护/Anti-Virus', 'SSL解密/Inspection', '负载均衡/FWLB', '高可用/HA/双机', '华为防火墙/USG', '思科防火墙/ASA', 'Juniper SRX', 'Fortinet FortiGate', '天融信/启明/绿盟', '策略优化', '日志审计']
                },
                'Burp Suite': {
                    'desc': 'Web应用安全测试平台',
                    'difficulty': 3,
                    'dimensions': ['Burp Suite概述/Web安全测试', 'Burp Suite安装/Java', 'Burp Proxy代理配置', '浏览器代理设置', 'Intercept/拦截请求', 'Forward/Drop/放行丢弃', 'Action/上下文菜单', 'HTTP History/历史记录', 'WebSockets History', 'Target/站点地图', 'Site Map/站点地图', 'Scope/测试范围', 'Scope Include/Exclude', 'Spider/爬虫/Discovery', '被动扫描/Passive Scan', '主动扫描/Active Scan', 'Scanner漏洞扫描', 'Scan issues/漏洞列表', '漏洞分类/SQLi/XSS/CSRF', 'Scanner Options/配置', 'Intruder/攻击器/Payload', 'Sniper/单Payload', 'Battering Ram/重复', 'Pitchfork/交叉', 'Cluster Bomb/组合', 'Payload Types/类型', 'Simple list/简单列表', 'Runtime file/文件', 'Numbers/数字', 'Dates/日期', 'Brute Forcer/暴力', 'Character frobber', 'Bit flipper/位翻转', 'SQLi注入', 'XSS payload', 'Intruder Positions/位置', 'Clusterbomb攻击', 'Payload Processing', 'Payload Encoding', 'Grep Match/标记', 'Extract Grep', 'Comparer/比较器', 'Repeater/重放器', 'Request/请求修改', 'Response/响应查看', 'Decoder/解码器', '编码/Encode/Decode', 'Hash/哈希', 'Plain/原始', 'Smart decode/智能', 'Sequencer/序列器', 'Token分析/随机性', 'Entropy/熵分析', 'Extender/扩展', 'BApp Store/应用商店', 'SQLMap/集成', 'Python脚本/Burp', 'Jython/JRuby支持', 'CSRF PoC生成', 'JSON Web Token攻击', 'JWT攻击/alg:none', 'JWT暴力破解', '路径穿越/../', '命令注入测试', '越权测试/Batch', '验证码识别/插件', 'Burp Collaborator', 'Out-of-Band', '扫描调度/Schedule', '报告生成/Report', 'Scope高级', 'Session处理', '宏/Macro', 'Cookie Jar', 'Target Map过滤', 'Burp API/自动化']
                },
                'IDS/IPS': {
                    'desc': '入侵检测和防御系统部署',
                    'difficulty': 3,
                    'dimensions': ['IDS概述/Intrusion Detection', 'IPS概述/Intrusion Prevention', 'IDS vs IPS区别', 'IDS类型/网络型/主机型', 'NIDS/Network IDS/网络入侵检测', 'HIDS/Host IDS/主机入侵检测', '签名检测/Signature-based', '特征库匹配', '异常检测/Anomaly-based', '统计异常检测', '协议异常检测', '流量异常检测', '混合检测/Hybrid', 'IDS部署位置/Inline/旁路', 'IDS镜像端口/SPAN/RSPAN', 'TAP分光器', 'Snort入侵检测/Snort', 'Snort规则/Rule', 'Snort预处理器', 'Snort输出插件', 'Snort模式/Promiscuous', 'Suricata/高性能IDS', 'Zeek/Bro网络分析', 'Zeek脚本/Policy Script', 'OSSEC/主机入侵检测', 'Samhain/主机完整性', 'Tripwire/文件完整性', 'AIDE/高级入侵检测', 'RKHunter/Rootkit检测', 'Chkrootkit/Rootkit', '签名库/Signature Database', 'Snort规则编写', 'CIDR表示法/规则', '动作/alert/log/pass', '协议/tcp/udp/icmp/ip', '方向/-> /<>', '端口号/any/80/443', '内容匹配/content', 'PCRE正则匹配', '元数据匹配/metadata', '流标记/flow', 'Msg/消息说明', 'Classtype/分类', 'sid/规则ID', 'rev/版本号', 'IPS阻断/Inline Mode', 'DROP vs REJECT vs SDrop', 'fail2ban/联动防火墙', 'Snort inline', 'Suricata IPS模式', 'Snorby/Snorby Web界面', 'BASE告警管理', 'Splunk SIEM集成', 'ELK日志分析', 'IDS告警分析', '误报优化/False Positive', '漏报分析/False Negative', 'IDS性能/TP/Throughput', 'IDS吞吐量', '规则更新/Subscription', 'ET Open/威胁情报', 'Snort规则社区', 'Emerging Threats', '威胁情报/Threat Intel', 'STIX/TAXII/情报标准', 'MISP平台/情报共享', 'IDS与防火墙联动', 'IDS与交换机联动', '蜜罐/Honeypot/诱捕', 'DDoS检测/DDoS Detection', '僵尸网络检测/Botnet', 'APT检测/高级威胁', 'IDS规则调优', 'Baseline建立', '异常阈值设置', '检测规则优化']
                },
                'Kali Linux': {
                    'desc': '专业渗透测试操作系统及工具使用',
                    'difficulty': 3,
                    'dimensions': ['Kali Linux概述/渗透测试OS', 'Kali官网/下载/VMware', 'Kali安装/物理机/虚拟机', 'Kali更新/apt update', 'Kali工具分类/Information', '信息收集/Reconnaissance', '被动信息收集/OSINT', 'whois查询/Domain', 'DNS查询/dig/nslookup', '子域名枚举/sublist3r', '搜索引擎/Shodan/Censys', 'Google Hacking/Dorks', '邮箱收集/theHarvester', '网站克隆/HTTrack', '主动扫描/Active Scan', 'Nmap端口扫描', 'Nikto Web扫描', 'Dirb目录爆破', 'Gobuster/目录枚举', 'WPScan/WordPress', '漏洞扫描/Vulnerability', 'Nikto/Web服务器扫描', 'OpenVAS综合漏洞', 'Nessus漏洞扫描', 'Nexpose漏洞扫描', 'AWVS漏洞扫描', '密码攻击/Password Attack', 'Hashcat/哈希破解', 'John the Ripper/JTR', 'Hydra在线破解', 'Medusa/Hydra', 'CrackMapExec/域内攻击', 'Mimikatz/明文密码', 'Responder/LMNR Poisoning', '社会工程学/Social Engineering', 'SET工具包/Social Engineer', '钓鱼攻击/Phishing', '凭证收集/Credentials', 'Web渗透/Web Application', 'Burp Suite代理', 'SQLMap注入', 'Sqlmap/--dbs/--dump', 'SQL注入测试', 'XSS测试/BeEF', 'CSRF测试', 'SSRF测试', 'XXE测试', '文件上传测试', '命令注入测试', 'Web模糊测试/FFUF', 'Burp Intruder', 'Web漏洞利用', 'Metasploit框架', 'msfconsole/控制台', 'search模块/search', 'use模块/use', 'set载荷/set PAYLOAD', 'exploit/攻击', 'auxiliary辅助模块', 'payload攻击载荷', 'encoder编码器', 'post后渗透模块', 'meterpreter/后门', 'meterpreter命令', '提权/Elevation', '本地漏洞利用', '绕过UAC', '端口转发/Port Forward', '内网穿透/Pivot', '横向移动/Lateral Movement', '令牌窃取/Token', '哈希传递/Pass-the-Hash', 'Kerberos攻击/Golden Ticket', 'PTH/PTK攻击', '维持访问/Persistence', '注册表持久化', '创建服务持久化', '无线攻击/Wireless', 'Aircrack-ng套件', 'WEP/WPA破解', 'WPA握手捕获', 'Fluxion/钓鱼WiFi', 'Wifite自动化', '移动渗透/Mobile', 'Frida动态分析', 'Drozer/Android测试', 'MobSF/移动安全', '逆向工程/Reverse', 'Radare2/Ghidra', '免杀/Evasion/过杀软', 'Veil/免杀载荷', 'Shellter/注入', 'Metasploit混淆', '取证分析/Forensics', 'Autopsy/磁盘镜像', 'Volatility/内存分析', 'Foremost/文件恢复', 'Steghide/隐写', '密码学/Cryptography', 'OpenSSL命令', '数字证书分析']
                },
                'Metasploit': {
                    'desc': '漏洞利用框架和渗透测试工具',
                    'difficulty': 3,
                    'dimensions': ['Metasploit概述/渗透测试框架', 'Metasploit发展历史', 'Metasploit架构/Framework', 'msfconsole/控制台', 'msfdb/数据库初始化', 'msfvenom/载荷生成', 'armitage/GUI界面', 'Metasploit模块/Module', 'Auxiliary辅助模块/扫描/信息', 'Exploit漏洞利用模块', 'Payload攻击载荷', 'Encoder编码模块', 'NOP空指令模块', 'Post后渗透模块', '模块路径/模块搜索', 'search关键字/search', 'search name:/path', 'search platform:', 'search type:', 'info模块信息/info', 'use选择模块/use', 'show options/选项', 'show payloads/载荷', 'show targets/目标', 'set设置选项/set', 'setg全局设置/setg', 'unset取消设置', 'unsetg全局取消', 'run/exploit执行', 'back返回', 'check检测漏洞', 'Sessions会话管理', 'sessions -i/列出会话', 'sessions -i id/接入', 'sessions -k/结束会话', 'background/后台运行', 'meterpreter/高级载荷', 'meterpreter命令/help', 'sysinfo/系统信息', 'getuid/当前用户', 'getpid/PID', 'getsystem/提权', 'ps/进程列表', 'migrate/进程迁移', 'kill/结束进程', 'shell/获取Shell', 'execute/执行命令', 'hashdump/哈希转储', 'mimikatz/明文密码', 'load kiwi/加载kiwi', 'credphish/凭证钓鱼', 'screenshot/截图', 'webcam_snap/摄像头', 'webcam_list/摄像头列表', 'record_mic/录音', 'keyscan_dump/键盘记录', 'keyscan_start', 'upload上传文件', 'download下载文件', 'cd/pwd/lpwd/目录', 'ls/cat/grep/文件', 'timestomp/时间戳', 'webcam_stream/视频', 'search搜索文件', 'pivot/内网穿透', 'portfwd/端口转发', 'autoroute/路由添加', 'run post/后渗透模块', 'post/multi/recon', 'post/linux/gather', 'post/windows/gather', 'post/multi/manage', 'post/windows/escalate', 'run getgui/开启RDP', 'payload类型/shell', 'reverse_tcp/反向Shell', 'bind_tcp/正向Shell', 'meterpreter/reverse', 'meterpreter/bind', ' staged vs unstaged', '架构/x86/x64', 'LinuxMeterpreter', 'WindowsMeterpreter', 'PHPMeterpreter', 'PythonMeterpreter', 'shell_reverse_tcp', 'windows/meterpreter', '编码器/shikata_ga_nai', 'x86/shikata_ga_nai', '迭代编码/Iterations', '规避/Evasive模块', 'exploit模块编写', 'RHOST/RPORT/设置', 'TARGET/目标设置', 'DisablePayloadHandler', 'handler模块/监听', 'multi/handler', 'searchsploit/EDB搜索', '辅助模块/portscan', 'auxiliary/scanner/portscan', 'auxiliary/scanner/smb', 'auxiliary/scanner/ssh', 'auxiliary/scanner/ftp', 'auxiliary/scanner/http', '永恒之蓝/MS17-010', 'BlueKeep/RDP漏洞', 'CVE漏洞利用', 'MSFVenom生成木马', 'msfvenom -p/载荷', '-f format/格式', '-e encoder/编码', '-i iterations/迭代', '-o output/输出', 'Linux后门/Lynx', 'Windows后门/Patch', 'PHP脚本/meterpreter', 'war部署/msfvenom', '永恒之蓝利用', 'BlueKeep利用', 'Weblogic利用', 'Struts2利用', 'Shellshock利用', 'Rails CVE利用', '后渗透信息收集', '内网信息收集', '域渗透/Domain', 'Kerberos攻击', 'Golden Ticket', 'Silver Ticket', 'Pass-the-Hash', 'Pass-the-Ticket', '钻石 Tickets']
                },
                'WAF': {
                    'desc': 'Web应用防火墙配置和规则调优',
                    'difficulty': 3,
                    'dimensions': ['WAF概述/Web Application Firewall', 'WAF工作原理/检测拦截', 'WAF部署模式/透明/反向代理', 'Inline串联部署', '旁路检测/镜像模式', 'WAF vs 防火墙', 'ModSecurity/Apache WAF', 'ModSecurity CRS规则', 'OWASP ModSecurity CRS', 'CRS规则集/Paranoia Level', 'SecRule编写/规则语法', 'SecRule ACTION/vars', 'SecRule CONDITION/phases', 'SecRule变量/RQUEST_URI', 'SecRule匹配操作/block', 'SecRule t:lowercase', 'SecRule ctl:ruleRemove', 'WAF绕过技术/Bypass', '大小写绕过/Case', '编码绕过/Encode/URL', 'Unicode编码绕过', '注释绕过/**/', '空格替代/%0a', '等价替换/and/or', 'SQL注入绕过', '双写绕过/wafwaf', 'SQLMap绕过/Tamper', '绕过技术总结', 'WAF检测原理', '正则匹配/Pattern', '语义分析/Semantic', '机器学习检测', 'WAF规则优化', '误报处理/处理', '规则调整/Rule Tuning', 'Whitelist白名单', 'IP白名单', 'URL白名单', '参数白名单', 'Bypass Whitelist', '黑名单/Blacklist', '自定义规则', '区域封禁/GeoIP', 'Rate Limiting/限速', 'Bot识别/CAPTCHA', 'Bot防护/Cookie Challenge', 'JavaScript Challenge', 'CC攻击防护', 'DDoS防护/层7', '慢速攻击防护/Slowloris', 'HTTP Flood防护', '慢速POST攻击', 'WAF日志分析', '日志存储/Log Storage', '告警阈值/Alert Threshold', 'WAF报表/Report', 'WAF性能影响', '延迟/Latency', '吞吐量/Throughput', '硬件WAF/Imperva', '硬件WAF/F5 ASM', '硬件WAF/绿盟WAF', '软件WAF/ModSecurity', '云WAF/阿里云WAF', '云WAF/腾讯云WAF', '云WAF/AWS WAF', '云WAF/CF Cloudflare', '云WAF/Akamai', 'DevOps WAF/Nginx+ModSec', 'HAProxy WAF', 'OpenResty WAF', '长亭雷池/Safeline', 'OpenRASP/运行时防护', 'RASP vs WAF区别', 'RASP原理/注入防护', 'WAF规则维护', '规则更新频率', '威胁情报联动', '威胁情报源', 'WAF合规性/PCI DSS', 'WAF审计/Logging', 'WAF认证/Certifications', 'Web漏洞防护', 'SQL注入防护', 'XSS防护/过滤', 'CSRF Token', '命令注入防护', '路径穿越防护', '文件上传防护', '敏感信息泄露']
                },
                '代码审计': {
                    'desc': '审查源代码发现安全漏洞',
                    'difficulty': 3,
                    'dimensions': ['代码审计概述/Code Audit', '代码审计流程/Procedure', '信息收集/Source Gathering', '代码获取/Git/SVN', '代码理解/Analysis', '代码审计工具', '静态代码分析/SAST', 'Fortify/静态分析', 'Checkmarx/以色列', 'SonarQube/代码质量', 'PMD/Java代码分析', 'FindBugs/FindSecBugs', 'Bandit/Python安全', 'Brakeman/Rails安全', 'RIPS/PHP代码审计', 'Semgrep/多语言审计', 'VisualCodeGrepper/VCG', 'Understand工具', 'RATS/C扫描', 'OWASP依赖检查', 'Dependency Check', 'npm audit/Node.js', 'Snyk/依赖漏洞', '白盒测试/White Box', '黑盒+白盒结合', '审计方法/Code Review', '污点分析/Taint Analysis', '数据流分析/Data Flow', '控制流分析/Control Flow', '语义分析/Semantic', '模式匹配/Matching', '危险函数追踪', '敏感函数/eval/system', 'PHP危险函数', 'Java危险方法', 'Python危险函数', '输入源识别/Source', '敏感数据/Sink', '传播路径/Propagation', '漏洞验证/POC', 'SQL注入审计', '审计点/$_GET/$_POST', '审计点/Database Query', '审计点/$_REQUEST', 'XSS漏洞审计', 'echo/print输出', 'innerHTML/innerHTML', 'CSRF漏洞审计', 'Token验证点', 'SSRF漏洞审计', 'file_get_contents', 'curl_exec', 'XXE漏洞审计', 'simplexml_load', 'XML解析函数', '文件操作审计', 'include/require', 'file_put_contents', 'unserialize', '反序列化审计', 'Java反序列化', 'Python pickle', 'PHP serialize', '.NET反序列化', '命令注入审计', 'system/exec/popen', 'Runtime.getRuntime', '代码执行审计', 'eval/assert/call', '命令注入绕过', '认证绕过审计', '会话管理审计', 'JWT审计', 'OAuth审计', 'SSO审计', '越权漏洞审计', 'IDOR审计点', '水平越权/垂直越权', '业务逻辑审计', '支付逻辑/0元购', '验证码绕过', '并发问题/Race', '越权测试', '敏感信息泄露', '硬编码密码', 'API密钥/Secret', '日志信息泄露', '调试信息', '安全配置审计', 'CORS配置', 'CSP配置', 'X-Frame-Options', 'HSTS配置', '审计报告编写', '漏洞描述/Description', '风险评级/Severity', '修复建议/Fix', 'POC代码/Proof']
                },
                '安全加固': {
                    'desc': '操作系统和应用的安全配置',
                    'difficulty': 3,
                    'dimensions': ['安全加固概述/Hardening', '安全基线/Baseline', '等保合规加固', 'CIS Benchmark/基准', '安全加固流程', '风险评估/Identify', '加固实施/Remediate', '验证检查/Verify', 'Windows加固/Windows', '账户安全/Administrator重命名', 'Guest禁用', '密码策略/Password Policy', '密码复杂度', '密码长度/Minimum', '密码过期/Expire', '账户锁定/Account Lockout', '审核策略/Audit Policy', '安全选项/Security Options', '本地策略/Local Policy', '禁用不必要的服务', '服务禁用列表', '端口禁用/Telnet/NetBIOS', '防火墙配置/Windows', 'Windows Firewall', '高级安全防火墙', '入站规则/Outbound Rules', '默认拒绝', '共享安全', 'SMBv1禁用', 'PowerShell安全', 'Execution Policy', '脚本签名要求', '更新补丁/Patch', 'WSUS/Windows Update', '自动更新配置', '补丁测试/Staging', '权限加固/ACL', 'NTFS权限', '共享权限', 'Takeown/获取所有权', 'icacls/权限查看', '加密文件系统/EFS', 'BitLocker加密', 'TPM芯片', '启动安全/UEFI Secure Boot', 'Remote Desktop安全', 'RDP NLA要求', 'RDP加密级别', 'IPSec安全', 'Linux加固/Linux', 'SELinux/AppArmor', 'SELinux模式/Enforcing', 'SELinux上下文', 'chcon/restorecon', 'Policy/策略类型', 'sealert日志', 'AppArmor配置', '系统账户/root/PAM', 'passwd/shadow', 'PAM认证模块', 'wheel组/sudo', 'SSH加固/SSH Hardening', 'SSH密钥登录', 'SSH端口修改', 'SSH禁止密码', 'SSH Protocol 2', 'SSH X11Forwarding', 'SSH PermitRootLogin', 'TCPWrappers', 'hosts.allow/deny', '防火墙/iptables', 'firewalld/centos7', 'ufw/ubuntu', 'iptables规则', 'Chain/INPUT/OUTPUT', 'ACCEPT/DROP/REJECT', '默认策略/Default Policy', '服务加固/Apache', 'Apache安全模块', 'Apache禁用目录', 'Apache版本隐藏', 'Apache HTTPS配置', 'Nginx加固', 'Nginx安全模块', 'Nginx SSL配置', 'MySQL加固', 'MySQL_secure', 'MySQL权限最小化', 'MySQL远程访问', 'MySQL SSL连接', 'Redis加固', 'Redis密码认证', 'Redis绑定地址', 'Redis危险命令', '禁用FLUSHALL', 'Tomcat加固', 'Tomcat manager弱口令', 'Tomcat版本隐藏', 'SSL/TLS加固', 'TLS 1.2/1.3', 'SSL证书配置', 'Cipher Suite', 'HSTS头', 'TLS握手优化', '数据库加固/MySQL', 'PostgreSQL加固', 'Oracle加固', 'MongoDB加固', '弱口令检查/Check', '漏洞扫描/Vuln Scan', '基线核查/Compliance', 'CIS扫描', '等保扫描', '渗透测试/Pentest', '安全配置管理', 'Ansible/Puppet加固', '脚本自动化', '加固检查清单', '加固验证']
                },
                '应急响应': {
                    'desc': '安全事件处理和取证分析',
                    'difficulty': 3,
                    'dimensions': ['应急响应概述/Incident Response', 'PDCERF模型/准备/检测', '六个阶段/Containment', '准备阶段/Preparation', '检测分析/Identification', '遏制阶段/Containment', '根除阶段/Eradication', '恢复阶段/Recovery', '事后总结/Lessons', '应急响应团队/CSIRT', '事件分级/Level 1-4', '紧急/严重/一般/轻微', '应急响应预案', 'Playbook/剧本', '事件报告/Report', '事件记录/Document', '时间线/Timeline', 'IOC指标/Malware Hash', 'IP/域名/URL', 'TTP战术技术', '样本获取/Sample', '内存镜像/Memory Dump', 'Winpmem/内存获取', 'LiME/Linux内存', '磁盘镜像/Disk Image', 'dd命令/FTK Imager', '取证工具/Autopsy', 'Autopsy磁盘分析', 'Volatility/内存分析', 'vol.py分析', '进程分析/pslist', '网络连接/netscan', '恶意进程/malfind', '注册表分析/registry', 'MFT分析/Master File', 'Windows事件日志', 'Security.evtx', 'System.evtx', 'Application.evtx', '4624/4625登录日志', '4648/平行提权', '4649/重放攻击', '4697/服务创建', '4698-4702计划任务', 'PowerShell日志', 'Sysmon/系统监控', 'Sysmon配置', 'Sysmon日志分析', 'Linux日志/日志审计', '/var/log/secure', '/var/log/messages', '/var/log/auth.log', '/.bash_history', '/var/log/nginx', 'SSH登录日志', 'Last命令/登录记录', 'W命令/当前用户', '进程分析/ps/top/lsof', '网络分析/netstat', '文件系统分析', 'Rootkit检测', 'chkrootkit检查', 'rkhunter检查', 'Strace/系统调用', 'Ltrace/库调用', '恶意软件分析/Static', '文件哈希/MD5/SHA', 'Strings分析/字符串', 'PE结构/PE Header', '查壳/Packer Detect', 'IDA Pro反汇编', 'Ghidra/反编译', '在线沙箱/VirusTotal', 'Any.Run交互沙箱', 'Hybrid Analysis', 'Cuckoo沙箱', '恶意软件分析/Dynamic', 'Process Monitor', 'Process Explorer', 'Autoruns/启动项', 'TCPView/网络连接', 'Fiddler/HTTP抓包', 'Wireshark/流量分析', '恶意脚本分析/PowerShell', '混淆分析/Deobfuscation', '勒索软件/Ransomware', '勒索软件分析', 'GandCrab/Ryuk', 'WannaCry分析', '后门分析/Backdoor', 'WebShell检测', 'D盾/安全狗', '河马/Hmmer', 'WebShell连接工具', '冰蝎/Behinder', '哥斯拉/Godzilla', '蚁剑/AntSword', '内网应急/横向渗透', '日志分析溯源', '溯源手法/Attribution', '攻击者画像', 'APT攻击/高级威胁', 'APT分析/APT29', 'APT28/沙虫组织', 'Lazarus组织', '威胁情报/TI/Threat', 'MISP平台', 'STIX/TAXII', '威胁情报库', '应急演练/Exercise', '红蓝对抗', '桌面推演/TTX', 'Ransomware处理', '勒索加密排查', '恢复方法/备份', '密钥获取可能', '数据恢复工具', '事件报告编写', '事后复盘']
                },
                '渗透测试': {
                    'desc': '模拟攻击测试系统安全性，发现安全弱点',
                    'difficulty': 3,
                    'dimensions': ['渗透测试概述/Penetration Testing', 'PTES标准/渗透测试执行', 'OWASP测试指南', 'PTES技术Guidelines', 'PTES前期交互', '情报收集/Intelligence', '主动信息收集/DNS', 'DNS区域传输/AXFR', 'DNS字典爆破', '子域名枚举/fierce', 'Shodan/搜索引擎', 'Censys/Certificate', 'Google Hacking/Dorks', 'Github信息收集', 'LinkedIn社工', 'Whois查询', '社工库查询', '资产发现/Recon-ng', '端口扫描/Nmap', 'Nmap脚本/NSE', '服务识别/Version', '操作系统识别/OS', '漏洞扫描/OpenVAS', 'Nessus漏洞扫描', 'Nikto Web扫描', '漏洞验证/Vulnerability', 'CVE漏洞利用', 'Exploit-DB/EDB', 'SearchSploit搜索', 'Metasploit模块', '手动漏洞验证', 'Web渗透测试', '信息收集/Web', '目标指纹/Header', 'Wappalyzer指纹', 'CMS识别/WordPress', '目录扫描/Dirb', 'Gobuster', 'ffuf模糊测试', 'Burp Suite', '代理配置', 'Intruder攻击', 'Repeater重放', 'SQL注入/SQLi', 'Union注入', 'Boolean盲注', '时间盲注', '报错注入', 'SQLMap自动化', 'XSS跨站脚本', '反射型/存储型', 'BeEF框架', 'CSRF跨站请求', 'SSRF服务端请求', 'XXE外部实体', '文件上传/Webshell', '一句话木马', '冰蝎/哥斯拉', '文件包含/LFI/RFI', '命令注入/Command', '代码执行/Code', '业务逻辑漏洞', '越权测试/IDOR', '水平越权/垂直越权', '支付逻辑漏洞', '接口未授权', '密码找回漏洞', 'JWT攻击', '敏感信息泄露', '未授权访问', 'CORS配置错误', 'SSRF/Redis', '内网渗透/Network', '内网信息收集', '本机信息/ifconfig', '内网网段探测', '存活主机扫描', '端口扫描/内网', 'SMB信息收集', 'SMB协议利用', 'MS17-010永恒之蓝', 'CVE-2019-0708', 'Pass-the-Hash', '哈希传递/PTH', '远程管理/WMI', 'PsExec工具', 'WMIExec', 'Impacket套件', '横向移动/Lateral', '票据传递/PTT', 'Kerberos攻击', 'Golden Ticket', 'Silver Ticket', '域管权限获取', '域控权限维持', '内网端口转发', 'FRP/Ngrok穿透', 'MSF session', 'Meterpreter', '权限提升/Elevation', '本地漏洞利用', 'UAC绕过', 'BypassUAC', '内核漏洞利用', 'sudo提权', 'SUID提权', '计划任务/Cron', 'NFS提权', 'MySQL UDF提权', 'mof提权', '第三方服务提权', '域内渗透/AD', '域信息收集', 'BloodHound分析', 'GPP漏洞/MS14-025', 'Kerberoasting', 'AS-REP Roasting', 'ACL滥用', '域持久化/AdminSDHolder', 'Golden Ticket', 'DCSync攻击', '权限维持/Persistence', '注册表自启动', 'WMI持久化', '计划任务', '服务创建', 'WebShell维护', '后门植入', '社工钓鱼攻击', '钓鱼邮件/Phishing', '钓鱼网站克隆', '宏病毒/Lnk', '水坑攻击/Watering Hole', '物理渗透/U盘攻击', 'BadUSB', 'BadUSB攻击', '社会工程学/SET', '报告编写/Report', '渗透测试报告', '漏洞详情', 'POC/复现步骤', '修复建议', '风险评级', '后续跟踪']
                },
                '漏洞扫描': {
                    'desc': 'Nessus、OpenVAS等自动化漏洞扫描工具',
                    'difficulty': 3,
                    'dimensions': ['漏洞扫描概述/Vulnerability Scan', '漏洞分类/系统/应用/配置', 'CVE漏洞库/MITRE', 'CVE编号/CVE-2021', 'CVSS评分/严重程度', 'CVSS向量/AV/AC/PR', '漏洞库/NVD/NIST', '漏洞库/CNVD/CNNVD', '中国国家漏洞库', 'Nessus漏洞扫描/Tenable', 'Nessus安装/专业版/家庭版', 'Nessus Web界面', 'Nessus扫描策略/Policy', '扫描模板/Template', 'Basic Network Scan', 'Advanced Scan/高级', 'Web Applications', 'Credentialed Patch Audit', 'Malware Scan', 'Discovery/发现扫描', 'WannaCry Ransomware', 'Shellshock/破壳', 'Debian Package Audit', 'SMB Signing', 'SSL/TLS扫描', ' poisoning/Safe Checks', 'Nessus插件/Plugin', 'Plugin ID/插件ID', '家庭版限制/免费版', 'Nessus Report/报告', '导出报告/PDF/HTML', '漏洞详情/Details', 'CVE关联/关联CVE', '解决方案/Fix', 'Nessus调度/Schedule', 'Nessus插件更新', 'OpenVAS开源漏洞', 'OpenVAS架构/GSA', 'OpenVAS Manager', 'OSP/OpenVAS Scanner', 'Greenbone Security', 'OpenVAS安装', 'OpenVAS CLI/gvm-cli', 'gvmd/管理进程', 'OpenVAS扫描任务', '创建目标/Target', '创建任务/Task', '配置凭证/Credential', '扫描配置/Config', 'Family-based', 'Full and Fast', 'Discovery', 'Host Discovery', 'Web CVE', 'IACS/工业控制', 'Linux Local Security', 'Windows Local Security', 'Debian/RHEL', 'OpenVAS报告/Report', '导出格式/PDF/HTML', '漏洞过滤/Filter', '绿盟漏扫/NSFOCUS', '启明星辰漏扫/Venus', '安恒信息/M6', 'Rapid7/NeXpose', 'Qualys漏洞扫描', 'Qualys Cloud', 'Tenable.io/云平台', 'Nexpose/VM Console', 'Acunetix/Web扫描', 'Acunetix AWVS', 'Web漏洞扫描/OWASP', 'Nikto/Apache/Nginx', 'Nikto扫描/nmap', 'Nikto evasions', 'Nikto配置', 'WPScan/WordPress', 'wpscan --url', 'wpscan --enumerate', 'CMS指纹/wpscan', '插件扫描', '用户枚举', 'JoomScan/Joomla', 'JoomlaScan', 'CMSmap/Drupal', 'DrupalScan', 'AppScan/IBM', 'AppScan标准版', 'Burp Suite Pro', 'Burp Pro Scanner', 'ZAP自动扫描', 'OWASP ZAP', 'ZAP Spider/爬虫', 'ZAP Active Scan', 'ZAP Passive Scan', 'ZAP Fuzzer', 'SQLMap注入扫描', 'sqlmap -m/批量', 'sqlmap -r/请求包', 'sqlmap --batch', '漏洞验证/POC', 'PoC编写/验证', 'Exp编写/利用', 'Metasploit验证', 'CVE利用/MSF', '漏扫报告分析', '误报识别', '真阳性/假阳性', '漏洞优先级/Priority', '高危漏洞', '中危漏洞', '低危漏洞', '信息级', '漏洞修复/Patch', '修复方案', 'CVSS评分', 'NVD参考', '厂商补丁', 'workaround缓解', '临时修复', '修复验证', '基线扫描/Compliance', 'CIS Benchmark', '等保合规', '漏扫集成/CI', 'Jenkins集成', 'GitLab集成']
                }
            }
        },
        '系统管理员': {
            'description': '负责服务器和系统的日常运维管理工作。',
            'skills': {
                'Python': {
                    'desc': '运维自动化脚本和工具开发',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/list/dict/set/tuple/控制流/循环/函数/类/继承/多态', 'Python环境/Python3/Pip/Anaconda', '虚拟环境/venv/virtualenv/conda', 'NumPy数值计算/数组/矩阵', 'Pandas数据处理/DataFrame/Series', 'Requests HTTP库/API调用', 'Paramiko/SSH连接/SFTP', 'subprocess/执行系统命令', 'os模块/文件目录操作', 'pathlib/路径操作', 're正则表达式', 'JSON/YAML解析', '日志模块/logging', '异常处理/try-except', '线程threading/进程multiprocessing', 'asyncio异步编程', 'Python脚本编写/自动化', 'Shell脚本调用', '配置文件读取/ConfigParser', '数据库连接/pymysql/SQLite', 'Redis连接/redis-py', 'API开发/Flask/FastAPI', 'Web请求处理', 'CLI工具开发/argparse', '定时任务/schedule/APScheduler', 'Celery分布式任务', '日志分析脚本', '服务器巡检脚本', '备份脚本/自动备份', '监控脚本/指标采集', '告警脚本/消息推送', 'Python打包/Docker镜像', 'requirements.txt依赖管理', 'Git版本控制', '代码规范/PEP8', '单元测试/unittest/pytest']
                },
                'Windows Server': {
                    'desc': 'Windows服务器管理和AD域配置',
                    'difficulty': 1,
                    'dimensions': ['Windows Server概述/微软服务器系统', 'Windows Server 2016/2019/2022', 'Windows Server Core/无GUI', 'Windows Server安装/物理机/虚拟机', '远程桌面/RDP/Remote Desktop', '服务器管理器/Server Manager', '角色和功能/Roles and Features', 'Active Directory/AD活动目录', 'AD域控制器/DC/Domain Controller', 'AD DS/域服务', '域/Domain/域账号', '组织单位/OU/Organizational Unit', '组策略/GPO/Group Policy', '用户管理/Users', '计算机管理/Computer Management', '安全策略/Security Policy', '本地策略/Local Policy', '账户策略/Account Policy', '密码策略/Password Policy', '账户锁定/Account Lockout', '审核策略/Audit Policy', 'NTFS权限/ACL', '共享权限/Share Permission', '文件服务器/File Server', 'DFS命名空间/Distributed File System', 'iSCSI存储/iSCSI Target/Initiator', 'DHCP服务器/Dynamic Host', 'DHCP作用域/Scope', 'DHCP中继/Relay Agent', 'DHCP高可用/Split-scope', 'DNS服务器/Domain Name System', 'DNS区域/Zone/Forward/Reverse', 'DNS记录/A/CNAME/MX/TXT', 'DNS转发器/Forwarder', 'DNS递归查询/迭代查询', 'IIS Web服务器/Internet Information', 'IIS网站/Site', 'IIS应用程序池/Application Pool', 'IIS绑定/Binding/HTTPS', 'IIS日志/Logging', 'IIS压缩/Compression', 'IIS身份验证/Basic/Windows', 'IIS URL重写/ARR', 'IIS PHP配置', 'IIS ASP.NET', 'IIS高可用/NLB', 'NLB负载均衡/Network Load', '故障转移集群/Failover Cluster', 'Hyper-V虚拟化', 'Hyper-V管理器', '虚拟机/VM/创建管理', '虚拟交换机/Switch', '虚拟硬盘/VHD/VHDX', '检查点/Checkpoint', '存储空间/Storage Spaces', 'SMB文件共享/SMB3', 'SMB加密', 'Print Server/打印服务器', 'WDS/Windows部署服务', 'MDT/部署工具', 'WSUS/更新服务', 'Windows Update', '补丁管理/Patch', 'Event Viewer/事件查看器', 'Windows日志/Security/System', 'Task Scheduler/任务计划', 'PowerShell管理', 'PowerShell命令/Get-ADUser', 'PowerShell脚本', '远程管理/WinRM', '防火墙/Windows Firewall', '高级安全防火墙', '安全策略/Security Policy', 'BitLocker加密', 'TPM管理', 'Server Core管理', 'sconfig工具', '部署服务/Deployment']
                },
                'Ansible': {
                    'desc': '自动化运维工具，批量配置管理',
                    'difficulty': 2,
                    'dimensions': ['Ansible概述/自动化运维/Agentless', 'Ansible架构/Control Node/Managed', 'Ansible安装/yum/apt/pip', 'Ansible配置文件/ansible.cfg', 'Inventory主机清单/hosts', '主机模式/Pattern', '主机变量/Host Variables', '组变量/Group Variables', 'Inventory动态/Dynamic', 'Ansible模块/Module', 'ad-hoc命令/ansible命令行', 'ansible-doc/模块文档', 'ping模块/连通性测试', 'command模块/执行命令', 'shell模块/Shell脚本', 'script模块/分发脚本', 'raw模块/原始命令', 'file模块/文件管理', 'copy模块/文件复制', 'template模块/模板', 'lineinfile/行修改', 'blockinfile/块操作', 'archive/unarchive/压缩', 'yum/apt包管理', 'service/systemd模块', 'cron模块/定时任务', 'user模块/用户管理', 'group模块/组管理', 'docker模块/容器', 'git模块/Git操作', 'get_url模块/下载', 'uri模块/HTTP请求', 'Playbook/YAML剧本', 'play结构/hosts/tasks', 'tasks任务列表', 'name任务名', 'action执行模块', 'vars变量', 'handlers处理器', 'notify触发', 'tags标签', 'when条件', 'with_items循环', 'loop循环', 'register注册变量', 'changed_when', 'failed_when', '错误处理/ignore_errors', '块/block/rescue', '角色/Role/角色结构', 'roles/目录结构', 'defaults/main.yml', 'vars/main.yml', 'tasks/main.yml', 'handlers/main.yml', 'templates模板', 'files静态文件', 'roles/myrole/tasks', 'roles/myrole/handlers', 'Galaxy/Ansible Galaxy', 'ansible-galaxy init', 'Ansible Vault/加密', 'ansible-vault加密', '敏感信息加密', '条件执行/when', '循环/loop/with_list', 'with_items/with_dict', 'with_fileglob', 'lookup插件', 'filter_plugins', 'Facts系统变量', 'ansible_host', 'ansible_distribution', 'ansible_memtotal_mb', 'set_fact设置变量', 'delegate_to/委托', 'run_once/一次执行', 'serial/批量控制', 'strategy/策略/free', 'async异步任务', 'poll轮询', 'check模式/dry-run', 'diff模式/diff', 'tags标签执行', 'ansible-pull拉取模式', 'ansible-pull -u', '回调插件/callback', '事实缓存/facts caching', 'inventory脚本', '云模块/ec2/vmware', 'docker_container', 'k8s模块', '网络模块/cisco/juniper', '社区角色/Community Role']
                },
                'Linux': {
                    'desc': 'Linux服务器安装配置和日常维护，包括CentOS、Ubuntu等',
                    'difficulty': 2,
                    'dimensions': ['Linux概述/开源操作系统', 'Linux发行版/CentOS/RHEL/Ubuntu/Debian', 'RHEL红帽/CentOS Stream', 'Ubuntu LTS/长期支持', 'Debian稳定版', 'Linux内核/Kernel', 'Linux安装/RHEL/CentOS安装', 'Ubuntu安装/Desktop/Server', 'Kdump崩溃转储', 'LVM逻辑卷管理', '磁盘分区/fdisk/parted', '文件系统/ext4/xfs/btrfs', '挂载/mount/umount', '/etc/fstab自动挂载', '网络配置/IP/子网/网关', 'ifcfg文件/ens33', 'nmcli命令/NetworkManager', 'nmtui图形工具', 'DNS配置/etc/resolv.conf', '主机名配置/etc/hostname', 'hosts文件/etc/hosts', 'Yum/DNF包管理', 'apt-get/Debian包管理', 'apt/aptitude', '软件源/Repository', 'EPEL源/CentOS', '镜像源配置', '系统更新/yum update', '系统服务/systemd', 'systemctl管理', 'service命令/旧版', '启动管理/boot', 'runlevel/target目标', '用户管理/useradd/usermod', 'passwd/用户密码', 'sudo权限/sudoers', 'su切换用户', 'userdel删除用户', '组管理/groupadd', '权限管理/chmod/chown', 'ACL访问控制', '文件查找/find/locate', '文件查看/cat/head/tail', 'grep文本搜索', 'sed文本处理', 'awk文本分析', '文本编辑器/vi/vim/nano', 'vim编辑器/Insert/Normal', 'vim命令/yy/p/dd', 'vim搜索替换', '进程管理/ps/pgrep', 'top/htop进程监控', 'kill/pkill进程终止', 'nice/renice优先级', 'nohup后台运行', 'screen/tmux终端', '磁盘使用/df/du', '磁盘IO/iostat/iotop', '内存使用/free', 'CPU监控/vmstat', '系统负载/uptime/load', 'sar系统性能', '网络命令/ifconfig/ip', 'ip addr/netstat', 'ss命令/Socket', 'route路由表', 'ip route路由', 'traceroute路由追踪', 'ping网络测试', 'nslookup/DNS查询', 'dig/DNS详解', 'telnet远程', 'ssh远程登录', 'scp文件传输', 'sftp安全传输', 'rsync同步', 'tar压缩/tar.gz', 'zip/unzip压缩', 'cron定时任务', 'crontab计划', '日志系统/journalctl', '/var/log日志', 'syslog/rsyslog', 'rsyslog配置', 'logrotate日志轮转', '防火墙/firewalld/iptables', 'firewalld区域/zone', 'firewalld服务/service', 'iptables规则/chain', 'UFW简单防火墙', 'Selinux/AppArmor', 'Selinux状态/Enforcing', 'Selinux上下文', 'SSH服务/sshd', 'sshd_config配置', 'SSH密钥登录', 'SSH免密码', 'Apache/Nginx Web', 'Nginx安装配置', 'Apache安装配置', 'MySQL/PostgreSQL数据库', 'MySQL安装', 'PostgreSQL安装', 'Redis安装', 'Docker安装', 'Kubernetes/k8s', 'Git安装配置', 'Python安装/pip', 'Java安装/JDK', 'Shell脚本/bash', 'bash编程', '正则表达式/Regex', '管道/Pipe/重定向', '环境变量/PATH', 'source配置文件', 'Cron定时任务', '系统备份', '性能优化', '内核参数/sysctl', 'limits.conf资源限制', 'nproc限制', '系统监控/Prometheus']
                },
                'Shell': {
                    'desc': 'Linux自动化运维脚本编写',
                    'difficulty': 2,
                    'dimensions': ['Shell概述/壳层/命令行解释器', 'Bash/Bourne Again Shell', 'Zsh/Z Shell', 'Fish Shell', 'Sh/POSIX Shell', '脚本首行/shebang/#!/bin/bash', '注释/#单行注释', '变量/Variable赋值', '变量引用/$var', '只读变量/readonly', '环境变量/export', '位置参数/$1/$2/$@/$*', '特殊变量/$?/$$/$0', '字符串处理', '单引号/双引号区别', '命令替换/$(cmd)/`cmd`', '算术运算/$((expr))', 'let运算/expr命令', '算术展开', '数组/Array', '关联数组/Associative Array', '条件测试/[ condition ]', 'test命令', '[[ ]]双括号', '字符串比较/==/!=', '数字比较/-eq/-gt/-lt', '文件测试/-f/-d/-e', '-r/-w/-x权限测试', '逻辑操作/-a/-o/!/&&/||', 'if语句/if-then-fi', 'if-else-if嵌套', 'case语句/模式匹配', 'for循环/for...do...done', 'C风格for循环', 'while循环/while...do', 'until循环', 'select菜单', 'break continue', '函数/function', '函数参数/$1/$2', '函数返回值/return', '局部变量/local', '递归函数', '输入读取/read', 'read -p提示', 'read -t超时', 'read -s隐藏输入', 'echo输出/printf', '颜色输出/echo -e', '字体颜色/echo -e', '格式化输出/printf', '重定向/>/>>/2>/dev/null', '管道/|', 'here文档/<<EOF', 'xargs命令/参数传递', '管道组合', 'grep搜索/正则', 'sed流编辑器', 'sed替换/s/SRC/DST/', 'sed删除/d', 'awk文本处理', 'awk-F指定分隔符', 'awk打印/$1/$NF', 'awk条件/if', 'awk计算', 'cut列提取', 'tr字符转换', 'sort排序', 'uniq去重', 'wc统计/wc -l', 'xargs参数构建', 'basename/dirname路径', 'realpath绝对路径', 'dirname取目录', 'basename取文件名', 'test -z/-n', '字符串长度/${#var}', '字符串截取/${var:0:3}', '字符串替换/${var/old/new}', '默认值/${var:-default}', '脚本调试/bash -x', 'set -x调试', 'set -e遇错退出', 'set -u未定义退出', 'trap信号捕获', '信号/SIGTERM/SIGKILL', '后台运行/&/nohup', 'nohup脱离终端', 'disown脱离作业', 'wait等待', 'jobs查看作业', 'fg/bg前后台', 'crontab定时', 'at一次性定时', 'expect自动化交互', 'sshpass非交互SSH', 'wget/curl下载', 'curl发送请求', 'API调用/JSON', '日志输出', '错误处理', '脚本模板', 'Shell脚本规范', 'Shellcheck检查']
                },
                '备份恢复': {
                    'desc': '数据备份策略制定和灾难恢复',
                    'difficulty': 2,
                    'dimensions': ['备份恢复概述/Backup and Recovery', '备份策略/Backup Strategy', '3-2-1原则/三份副本', '备份类型/全备/增备/差备', '全量备份/Full Backup', '增量备份/Incremental', '差异备份/Differential', '备份窗口/Backup Window', 'RPO恢复点目标/Recovery Point', 'RTO恢复时间目标/Recovery Time', '备份频率/频率选择', '每日备份/Daily', '每周备份/Weekly', '每月备份/Monthly', '备份介质/磁盘/磁带/云', '磁盘备份/DAS/SAN', '磁带备份/Tape/LTO', '云备份/Cloud Backup', '阿里云OSS备份', 'AWS S3备份', 'Azure Backup', '本地备份/NAS', 'NAS网络附加存储', '备份软件/Backup Software', 'Veeam备份虚拟机', 'Veritas NetBackup', 'Commvault备份', 'Bacula开源备份', 'Restic/开源', 'Rclone/云同步', 'Rsync增量同步', 'tar+rsync备份', 'dd磁盘镜像', 'Ghost/Clonezilla', 'XtraBackup/MySQL备份', 'mysqldump/MySQL', 'pg_dump/PostgreSQL', 'MongoDB备份/mongodump', 'Redis备份/RDB+AOF', 'Oracle RMAN备份', '备份脚本/shell脚本', '定时备份/cron', '自动化备份', '备份加密/Encryption', '备份压缩/Gzip/Zstd', '备份验证/Verify', '备份恢复测试', '恢复演练/Recovery Test', '灾难恢复/DR/Disaster', 'DR站点/备份站点', '冷备/Cold Standby', '温备/Warm Standby', '热备/Hot Standby', '双活数据中心', '主备切换/Failover', '回切/Failback', '数据复制/Replication', '同步复制/Sync', '异步复制/Async', 'CDP持续数据保护', '快照/Snapshot', '存储快照', 'LVM快照', 'VMware快照', '云快照', '应用一致性快照', '崩溃一致/Crash', '文件级备份', '块级备份/Block', '操作系统备份', '系统镜像', '裸机恢复/Bare Metal', '业务数据备份', '数据库备份', '文件服务器备份', '邮件备份/Exchange', '虚拟机备份/VM', '容器备份/Docker', 'K8s备份/velero', '备份网络/专用网络', '备份带宽', '备份存储容量', '备份生命周期管理', '备份归档/Archive', '长期保留/LTR', '合规保留/Compliance', '备份删除/过期清理', '勒索防护/备份隔离', '3-2-1-1原则', '备份监控', '备份报告', 'RTO/RPO评估']
                },
                '网络配置': {
                    'desc': '服务器网络参数配置和故障排查',
                    'difficulty': 2,
                    'dimensions': ['网络配置概述/Server Network', '网络基础/IP地址/IPv4/IPv6', '子网掩码/Subnet Mask', '默认网关/Gateway', 'DNS服务器/DNS Server', '公有IP/私有IP', 'NAT地址转换', '静态IP配置/Linux', 'RHEL/CentOS网络配置', '/etc/sysconfig/network-scripts', 'ifcfg-eth0配置', 'Ubuntu网络配置', '/etc/netplan配置', 'YAML格式/netplan', 'NetworkManager/nmcli', 'nmcli con show', 'nmcli con mod', 'nmtui图形工具', 'DHCP自动获取', '动态IP配置', '多网卡配置/Bonding', 'Bond模式/主动备份/负载均衡', 'Teaming/Linux Team', 'Teamd配置', 'VLAN配置/子接口', 'ip link add link', '网桥配置/Bridge', 'brctl网桥工具', '网络绑定/Bond', 'Bonding驱动', 'mode=1/主动备份', 'mode=0/负载均衡', '网络别名/alias', 'IP别名/Secondary IP', '隧道/Tunnel/GRE', 'VXLAN隧道', 'Loopback接口/lo', 'MTU配置/巨型帧', ' Jumbo Frame/9000', '网络诊断工具/ping', 'ping -c/次数', 'ping -s/包大小', 'traceroute路由追踪', 'tracert/Windows', 'mtr/路由质量', 'nslookup/DNS查询', 'dig/DNS详解', 'host/DNS查询', 'netstat/网络状态', 'ss命令/Socket统计', 'ss -tulpn/监听端口', 'ip addr/地址', 'ip link/接口', 'ip route/路由', 'route/路由表', 'ip neigh/ARP表', 'arp -a/ARP缓存', 'ethtool网卡', 'ethtool -S/统计', 'iperf3/带宽测试', 'iPerf服务端/客户端', 'tcpdump抓包', 'tcpdump -i/接口', 'tcpdump -c/包数', 'tcpdump -w/保存', 'tcpdump host/主机', 'tcpdump port/端口', 'tcpdump tcp/协议', 'wireshark分析', 'curl网络请求', 'wget下载', 'telnet测试端口', 'nc/netcat网络瑞士刀', 'nc -zv端口扫描', 'DNS排错/DNS故障', '网络不通排错', 'ping不通排错', '路由不通排错', 'DNS解析失败', '网关不通', 'ARP问题', 'DNS配置/etc/resolv.conf', 'hosts文件/etc/hosts', 'hostname配置', '防火墙影响/Firewall', 'Selinux影响', '路由表错误', '路由追踪/mtr', 'MTU问题/分片', 'NAT问题', '端口冲突', '网络服务/network', 'networkmanager服务', '重启网络/systemctl restart', '网络性能/带宽', '网络延迟/Latency', '网络丢包/Packet Loss', '带宽监控/iptraf', 'nethogs进程流量', 'iftop/流量监控']
                },
                'ELK': {
                    'desc': 'Elasticsearch、Logstash、Kibana日志分析',
                    'difficulty': 3,
                    'dimensions': ['ELK概述/Elastic Stack/日志分析', 'Elasticsearch分布式搜索引擎', 'ES安装/Java要求', 'ES单节点安装', 'ES集群安装/Cluster', 'ES节点类型/Master/Data', 'ES分片/Shard/Primary', 'ES副本/Replica', 'ES Index索引', 'ES Document文档', 'ES Mapping映射', 'ES REST API/_cat', 'ES _cluster健康', 'ES _nodes节点', 'ES _indices索引', 'ES写入流程/写入原理', 'ES搜索流程/查询原理', 'ES倒排索引/Inverted Index', 'ES分词器/Analyzer', 'ES IK分词/中文', 'ES Query查询DSL', 'ES聚合/Aggregation', 'ES集群规划', 'ES性能优化', 'ES冷热架构', 'ES ILM索引生命周期', 'ES Curator管理', 'Logstash日志收集', 'Logstash安装/Java', 'Logstash管道/Pipeline', 'Input输入插件', 'file输入/日志文件', 'beats输入/收受', 'tcp/udp输入', 'syslog输入', 'Filter过滤插件', 'grok过滤/正则解析', 'date日期解析', 'mutate字段处理', 'drop丢弃', 'geoip地理位置', 'useragent浏览器', 'ruby自定义', 'Output输出插件', 'elasticsearch输出', 'file输出/文件', 'stdout输出/控制台', 'kafka输出/消息队列', 'redis输出', 'mongodb输出', 'Logstash配置示例', 'Logstash多管道', 'Beat客户端/Beats', 'Filebeat日志收集', 'Filebeat prospectors', 'Filebeat processors', 'Filebeat modules', 'Packetbeat网络', 'Heartbeat心跳', 'Metricbeat指标', 'Auditbeat审计', 'Journalbeat日志', 'Winlogbeat/Windows事件', 'Kibana可视化/Web', 'Kibana安装', 'Kibana连接ES', 'Discover发现', 'Dev Tools开发工具', 'Visualize可视化', 'Dashboard仪表盘', 'Canvas画布', 'Maps地图', 'Machine Learning', 'APM应用性能', 'Alerting告警', 'Canvas自定义', 'Kibana Lens', 'TSVB时序', 'Timelion时序分析', 'Stack Monitoring监控', 'Elasticsearch集群监控', 'Logstash监控', 'Kibana安全/X-Pack', 'Elasticsearch安全', 'RBAC角色', 'API Keys', '字段级安全', '证书配置/TLS', 'HTTPS配置', 'Elasticsearch备份', 'Snapshot备份', '跨集群复制/CCR', '跨集群搜索/CCS', 'Elasticsearch性能调优', 'JVM调优/heap size', 'ES字段容量', 'Index模板', 'ILM索引生命周期', '日志格式规范/JSON', '日志字段标准化', 'Groovy脚本', 'ES DSL查询', 'ES Term查询', 'ES Match查询', 'ES Bool查询', 'ES聚合查询', 'ES故障排查']
                },
                'ITIL': {
                    'desc': 'IT服务管理流程和最佳实践',
                    'difficulty': 3,
                    'dimensions': ['ITIL概述/IT Infrastructure Library', 'ITIL发展/v3 vs v4', 'ITIL 4框架', 'ITIL服务价值系统/SVS', 'ITIL指导原则', 'ITIL 4 Dimension Model', '服务管理四维度', '服务提供商/Practices', 'ITIL服务台/Service Desk', '服务台类型/本地/集中/虚拟', '服务台指标/SLA', '一线支持/First Line', '二线支持/Second Line', '三线支持/Third Line', '事件管理/Incident', '事件优先级/P1-P4/Priority', '事件分类/Category', '事件升级/Escalation', '重大事件/Major Incident', '事件管理流程', '事件记录/Incident Record', '事件解决/Resolution', '事件关闭/Closed', '问题管理/Problem', '问题分类/RCA根本原因', '已知错误/Known Error', 'CAB变更委员会/Change', '变更请求/RFC', '标准变更/Standard Change', '紧急变更/Emergency', '变更评估/Impact', '变更审批/Approval', '变更发布/Release', '发布策略/Big Bang/Phased', '发布管理/Release', '配置管理/CMDB', 'CI配置项/Configuration Item', 'CI关系/Relationship', '资产配置管理', '服务级别管理/SLM', 'SLA服务水平协议', 'SLA指标/Availability', 'SLA报告', '供应商管理/Vendor', '供应商合同/SLM', '财务管理/Service Portfolio', 'IT预算/Budget', '成本核算/Cost Accounting', '服务价值链/Value Chain', '服务设计/Design', '容量管理/Capacity', '可用性管理/Availability', '连续性管理/Continuity', '安全合规/Security', '需求管理/Demand', '服务目录/Service Catalog', '服务请求/Request', '知识管理/KM/Knowledge', '知识库/KB/Articles', 'ITIL流程集成', '流程自动化', '工作流/Workflow', '工单/Ticket', '派单/Dispatch', 'SOP标准操作', '流程审计/Audit', '流程优化/KPI', '服务报告/Report', 'ITOM/AIOps', '监控集成/Alert', 'CMDB同步', 'SOAR自动化', 'Remedy/ServiceNow', 'Jira Service Management', 'ManageEngine', 'Ivanti/HEAT', 'LANDesk/SPD', 'ISO 20000认证', 'ITIL认证/Foundation', 'ITIL Practitioner', 'ITIL Managing Professional', 'ITIL Strategic Leader']
                },
                'KVM': {
                    'desc': '开源虚拟化技术',
                    'difficulty': 3,
                    'dimensions': ['KVM概述/Kernel-based Virtual', '虚拟化基础/硬件辅助', 'VT-x/AMD-VCPU', 'KVM架构/KVM模块', 'qemu-kvm模拟器', 'qemu-system-x86_64', 'KVM安装/yum/apt', 'qemu-kvm安装', 'libvirt管理工具', 'virsh命令行', 'virt-manager/图形', 'virt-install创建', 'virt-clone克隆', 'virt-sparsify精简', 'virt-convert转换', 'VNC远程连接', 'SPICE协议', '虚拟机规格/vCPU', '虚拟机内存/Memory', '磁盘/Disk/qcow2', 'raw格式/镜像格式', 'qcow2快照/Snapshot', 'qcow2覆写/Backing File', '网络模式/桥接/Bridge', 'NAT模式/Network', 'Host-only/仅主机', 'SR-IOV直通', 'PCI直通/Passthrough', 'GPU虚拟化', 'vGPU技术', 'Mdev/Mediated', '虚拟网络/virbr0', 'libvirt网络/XML', '虚拟交换机', '存储池/Storage Pool', 'Storage Pool类型', 'dir目录池', 'lvm卷池', 'iscsi远程池', 'ceph/rbd池', 'nfs网络存储', 'Volume卷/磁盘', 'virsh命令/list', 'virsh start/stop', 'virsh reboot/shutdown', 'virsh destroy强制', 'virsh undefine删除', 'virsh edit修改', 'virsh autostart', 'virsh console', 'virsh migrate迁移', 'virsh snapshot', 'virsh domblklist', 'virsh domiflist', '虚拟机模板/Template', '云镜像/Cloud Image', 'cloud-init初始化', 'NoCloud数据源', 'Config Drive', 'KVM性能优化', 'CPU绑定/pinning', 'NUMA亲和', '大页内存/Hugepages', 'IO调度器', 'Virtio驱动/半虚拟化', 'Virtio-SCSI', 'Virtio-Net', 'Vhost-Net', 'Vhost-User', 'Live Migration/热迁移', '在线迁移/Online', '离线迁移/Offline', 'virsh migrate', '迁移网络/迁移带宽', '共享存储/迁移要求', 'KVM安全/Security', 'SELinux权限', 'AppArmor', '虚拟机隔离', '安全增强', '嵌套虚拟化', 'KVM监控/Libvirt', 'Prometheus导出', 'Grafana可视化', 'KVM日志/日志分析', '排错/Troubleshooting', 'virsh dominfo', 'virsh dommemstat', 'virsh domstats', '资源配额/Limits', 'CPU配额', '内存配额', '磁盘IO配额', '快照管理', '快照恢复', '快照删除', '克隆虚拟机', '链接克隆/Linked', '完整克隆/Full']
                },
                'Nagios': {
                    'desc': '系统和网络监控工具',
                    'difficulty': 3,
                    'dimensions': ['Nagios概述/开源监控', 'Nagios Core/免费版', 'Nagios XI/商业版', 'Nagios架构/Server/Agent', 'Nagios安装/yum/apt', 'Nagios配置目录', 'nagios.cfg主配置', 'objects目录/对象定义', '主机定义/host', '服务定义/service', '联系人定义/contact', '时间段定义/timeperiod', '命令定义/command', '主机组/hostgroup', '服务组/servicegroup', '依赖关系/dependency', '主机检查/check_host', '服务检查/check_service', 'NRPE远程执行', 'NRPE安装/配置', 'check_nrpe命令', 'NSClient++/Windows', 'check_http/URL监控', 'check_ping/存活检测', 'check_ssh/SSH服务', 'check_snmp/设备监控', 'check_mysql/数据库', 'check_postgres/PG', 'check_disk/磁盘', 'check_load/负载', 'check_memory/内存', 'check_procs/进程', 'check_users/用户', 'check_swap/交换', 'check_dns/DNS', 'check_smtp/邮件', 'check_pop/邮件', 'check_imap/邮件', '主动检查/Active', '被动检查/Passive', 'NSCA被动接收', 'OCSP/ODP', 'Nagios插件/Plugin', '官方插件/nagios-plugins', '自定义插件/Shell', '自定义插件/Perl', '自定义插件/Python', '插件返回码/0/1/2/3', '性能数据/Performance', 'PNP4Nagios图表', 'PerfParse数据', 'GrapherViz', 'NagiosQL/GUI配置', 'Thruk/Web界面', 'Centreon界面', 'Icinga监控/分支', 'Icinga2现代版', 'ICINGA配置文件', '状态类型/Hard/Soft', '状态切换/State Flapping', '通知/Notification', '通知命令', '通知类型/Down/Recovery', '通知方式/Email/SMS', '通知周期', '升级/Escalation', '模板/Template', '主机模板/host template', '服务模板/service template', '继承/Inherit', '变量覆盖', 'NagiosGraph', 'PNP数据处理', 'RRDTool绘图', '性能数据格式', 'check_multi', 'NRDP远程', '依赖检查/Dependency', '主机依赖', '服务依赖', '父主机/Parent', '网络拓扑', '树形监控', 'Nagios日志', '事件处理/Event', '事件处理器', '主动抑制/Begin', '被动抑制/End', '宏/Macro', '$HOSTNAME$', '$SERVICEDESC$', '$HOSTADDRESS$', '宏过滤器', '服务映射/Service Map', '网络路径监控', '分布式Nagios', 'DNX/分布式', 'Nagios Fusion', '报告/Report', '可用性报告', '告警报告', 'SLA报告']
                },
                'VMware': {
                    'desc': '虚拟化平台管理和虚拟机部署',
                    'difficulty': 3,
                    'dimensions': ['VMware概述/虚拟化平台', 'VMware产品线/vSphere/Workstation', 'ESXi/ESX裸机虚拟化', 'vCenter Server管理', 'vSphere Client/HTML5', 'VMware vSphere', 'VMware Workstation', 'VMware Fusion/Mac', 'VMware Player/免费版', 'VMware Converter/迁移', 'ESXi安装/引导安装', 'ESXi定制/Image Builder', 'ESXi配置/DCUI', 'DCUI配置网络', 'ESXi主机配置', '主机配置文件/hostd', 'vCenter安装/VCSA', 'Windows vCenter', 'VCSA部署/Appliance', 'vCenter数据库/PostgreSQL', 'vCenter数据库/Oracle', 'vCenter高可用/VCHA', '集群/Cluster', '集群功能/DRS/HA', 'DRS分布式资源调度', 'DRS自动化级别', 'DRS迁移规则', 'DRS负载均衡', 'HA高可用/集群HA', 'HA心跳/datastore', 'HA故障检测', 'HA虚拟机重启', 'HA接入控制/Admission', 'FT容错/Fault Tolerance', 'FT日志/vLockstep', 'FT单核限制', 'EVC增强vMotion', 'EVC模式/Intel/AMD', 'vMotion迁移/热迁移', 'Storage vMotion', '跨vCenter/Motion', 'vSAN分布式存储', 'vSAN集群/全闪存', 'vSAN策略/策略驱动', 'FTT/Failures to Tolerate', 'RAID策略', 'vSAN网络/vmkernel', 'HCI超融合架构', '网络虚拟化/vSphere', '虚拟交换机/vSS', 'vSphere Distributed Switch', 'VDS/分布式交换机', '端口组/Port Group', 'VLAN/VLAN Tagging', 'MTU/Jumbo Frame', 'Uplink/上行链路', 'NIC Teaming/链路聚合', 'LACP协议', '负载均衡/Route', '故障切换/Failover', 'vmnic物理网卡', 'vmklinux驱动', 'N-VDS/NSX', '虚拟机/VM创建', 'VM规格/vCPU/内存', 'VM磁盘/Thin/Thick', '精简置备/Thin', '厚置备延迟置零', '厚置备置零', 'Eager Zeroed', 'VM快照/Snapshot', '快照管理/Snapshot', '快照层次', '快照删除', '模板/Template', '克隆虚拟机', '自定义规范/Customize', 'Sysprep/Windows', 'cloud-init/Linux', 'Guest OS定制', 'VMware Tools', 'Tools安装', 'Tools升级', 'Tools状态', '虚拟机控制台', 'VMRC控制台', '远程控制台', 'RDM裸设备映射', 'RDM物理', 'RDM虚拟', 'NPIV光纤通道', '存储/vMotion存储', 'iSCSI存储', 'FC光纤通道', 'NFS存储', 'Datastore存储', 'Datastore浏览', '存储DRS/SDRS', '存储策略/Policy', '内容库/Content Library', 'OVA/OVF导入导出', 'vSphere Lifecycle', '生命周期管理', '升级/Update', 'ESXi升级', 'vCenter升级', '补丁/Patch', 'Image Profile', 'Baseline基线', 'Scan/扫描', 'Remediate/修复', '安全增强/Security', 'ESXi锁定模式/Lockdown', '证书管理/Cert', '角色权限/RBAC', '权限/Datacenter', '权限/Cluster', '权限/VM', '权限/Host', '审计日志/Audit', 'vSphere认证/Authentication', 'vSphere LDAP', 'vSphere AD集成', '备份/Veeam', '备份/Commvault', '备份/Vembu', '监控/vROps', 'vRealize Operations', '监控告警/Alarm', 'vSphere监控', '性能图表/Performance', '性能分析', '资源池/Resource Pool', '资源分配/Reservation', '资源限制/Limit', '资源shares', 'DR规划/灾难恢复', 'Site Recovery Manager', 'SRM恢复计划', 'DR测试/非生产恢复']
                },
                'Zabbix': {
                    'desc': '开源监控系统',
                    'difficulty': 3,
                    'dimensions': ['Zabbix概述/开源监控', 'Zabbix架构/Server/Agent', 'Zabbix Server/MySQL', 'Zabbix Proxy代理', 'Zabbix Agent', 'Zabbix Web/Frontend', 'Zabbix安装/RPM/YUM', 'Zabbix LAMP/LNMP', 'Zabbix数据库/MySQL', 'Zabbix数据库/PostgreSQL', 'Zabbix配置/前端', 'Zabbix版本/5.x/6.x', 'Zabbix Web界面', 'Dashboard仪表盘', '全局视图/Global View', '主机/Host', '主机群组/Host Group', '模板/Template', '模板继承/Link', '模板覆盖/Inheritance', '监控项/Item', 'Item Key/键值', 'Item类型/Agent/SNMP', 'Zabbix Agent键值', 'system.cpu.load', 'vfs.fs.size', 'net.if.in/out', 'vm.memory.size', 'Item更新间隔/Update', 'Item历史/History', '趋势/Trends', 'Item预处理/Preprocessing', '正则预处理', '乘数/Discard unchanged', '触发器/Trigger', 'Trigger表达式', '严重程度/Severity', 'Disaster/High/Average', 'Warning/Information', 'Trigger函数/avg/count', 'nodata/diff', '表达式编辑器', 'Trigger依赖/Dependency', '触发器恢复', 'Trigger标签/Tag', '宏/Macro', '{$MACRO}用户宏', '{HOST.NAME}', '{ITEM.VALUE}', '图形/Graph', '简单图形/Simple Graph', '自定义图形/Custom', 'Graph原型', '多语言图形', '聚合图形/Aggregate', 'Map拓扑图/Map', 'Map链接/Link', 'Map元素/Element', 'Map触发器', 'Screen屏幕', 'Slide Shows轮播', '告警/Alert', '动作/Action', '条件/Condition', '操作/Operation', '操作类型/Message', '操作类型/Command', '远程命令/Remote', '告警媒介/Mediatype', 'Email邮件告警', 'SMS短信告警', 'Script脚本', 'Webhook集成', '钉钉/Webhook', '飞书告警', '企业微信告警', '告警确认/Acknowledge', '告警升级/Escalation', '维护期/Maintenance', 'Maintenance Type', 'Zabbix Agent安装', 'Zabbix Agent配置', 'Active Check主动', 'Passive Check被动', 'Zabbix Sender', 'Zabbix Get', 'UserParameter/自定义', 'Zabbix Java Gateway', 'JMX监控/Java Gateway', 'JMX应用/Zabbix', 'SNMP配置/SNMPv2', 'SNMPv3配置/认证', 'SNMP Traps接收', 'SNMP Interface', 'IPMI监控/IPMI', 'SSH监控/检查', 'Telnet检查', 'HTTP Agent/HTTP', 'Web监控/Web Scenarios', 'Web步骤/Step', 'Web验证', 'Zabbix API', 'JSON-RPC', '用户/User', '用户群组/User Group', '权限/Permission', '角色/Role', '前端认证/Auth', 'LDAP集成/AD', 'SSO单点登录', '低级别发现/LLD', 'LLD规则/Rule', 'LLD原型/Prototype', '自动发现/Discovery', '网络发现/Network', '主动Agent发现', 'Zabbix Proxy配置', 'Proxy主动/被动', '分布式监控', 'Zabbix Sender/Trapper', 'Trapper监控项', '监控代理/Agent2', 'Zabbix监控Nginx', 'Zabbix监控MySQL', 'Zabbix监控Redis', 'Zabbix监控Docker', 'Zabbix监控K8s', 'Zabbix监控VMware', '监控模板/官方模板', 'Template OS Linux', 'Template App MySQL', '模板编写', '正则表达式/Regexp', 'Value Mapping', '图标映射/Icon Map', '数据采集/Collection', 'Item类型参考', 'Zabbix日志/Log', '日志监控', '日志文件监控', '历史数据/Housekeeping', '趋势数据', '图表/Screens', '模板导入导出', 'Zabbix Agent2/Go', 'Zabbix性能优化', '数据库优化', '预处理队列', 'Escalator队列', 'Poller队列']
                },
                '存储管理': {
                    'desc': 'SAN、NAS存储配置和管理',
                    'difficulty': 3,
                    'dimensions': ['存储概述/Storage Management', '存储类型/DAS/SAN/NAS', 'DAS直连存储/Direct Attach', 'SAN存储区域网络', 'NAS网络附加存储', '存储协议/FC/iSCSI/NFS', 'FC光纤通道/8G/16G', 'Fibre Channel HBA', 'FC交换机/Fabric', 'FC Zoning', 'FC WWN/Port ID', 'FC LUN masking', 'ISCSI协议/Internet SCSI', 'iSCSI Initiator', 'iSCSI Target', 'iSCSI IQN命名', 'iSCSI CHAP认证', 'iSCSI多路径/MPIO', 'NFS网络文件系统', 'NFS v3/v4', 'NFS导出/Exports', 'NFS挂载/mount', 'NFS权限/权限问题', 'CIFS/SMB共享', 'SMB协议/SMB2/SMB3', 'SMB共享权限', 'SMB访问控制', '块存储/Block Storage', '文件存储/File Storage', '对象存储/Object Storage', '存储控制器', 'RAID技术/RAID级别', 'RAID 0/条带化', 'RAID 1/镜像', 'RAID 5/奇偶校验', 'RAID 6/双校验', 'RAID 10/镜像+条带', 'RAID 50/60', '硬件RAID卡', 'RAID BBU/电池', 'RAID重建/Rebuild', 'RAID级别选择', '存储池/Storage Pool', '热备盘/Hot Spare', '全局热备', 'LUN逻辑单元号', 'LUN划分', 'LUN映射/Mapping', '存储多路径/Path', 'ALUA路径选择', '存储网关', '存储网关/iSCSI', '存储网关/FC', 'NAS网关', '存储分层/Tier', '热数据/温数据', '冷数据/归档', 'SSD缓存/Cache', '自动分层存储', '存储QOS', 'IOPS限制/Throughput', '重复数据删除/Dedupe', '数据压缩/Compression', '数据加密/Encryption', '存储快照/Snapshot', '快照类型/RPO', '克隆/Clone', '备份复制/Replication', '同步复制/Sync', '异步复制/Async', 'MetroCluster双活', '存储双活', 'DR/灾难恢复', 'LUN迁移/Migrate', '卷迁移/Volume Move', '存储扩容/Expand', '存储精简配置/Thin', 'Thick Provisioning', '容量监控/Capacity', '存储告警/Threshold', '存储监控/工具', '存储网络/Metro', 'DWDM传输', 'FC网络', '存储性能调优', 'IOPS计算', '吞吐量计算', '延迟监控/Latency', '存储排错/Troubleshooting', '光纤卡故障/HBA', '链路故障', 'LUN不可见', '路径故障', 'Zoning问题', '存储品牌/EMC/戴尔', '存储品牌/NetApp', '存储品牌/HPE/3PAR', '存储品牌/IBM/DSUS', '存储品牌/华为/OceanStor', '存储品牌/宏杉/MACRO', '存储品牌/曙光/DHT', '软件定义存储/SDS', 'Ceph分布式存储', 'Ceph RBD/块', 'Ceph FS/文件系统', 'Ceph RGW/对象', 'GlusterFS分布式', 'MinIO对象存储', 'cephadm安装', 'Ceph OSD', 'Ceph MON', 'Ceph MDS', 'Ceph PG', 'CRUSH Map', 'Ceph块存储/RBD', 'Ceph文件存储/CephFS', 'Ceph对象/RGW', 'Ceph性能/BlueStore', 'SDS超融合/HCI', 'vSAN/超融合', 'Nutanix超融合', '存储即服务/STaaS']
                },
                '高可用': {
                    'desc': 'Keepalived、HAProxy等高可用方案',
                    'difficulty': 3,
                    'dimensions': ['高可用概述/High Availability', 'HA指标/可用性', '99.9%/99.99%/99.999%', 'SLA服务等级协议', 'MTTF平均无故障', 'MTTR平均修复', '停机时间/Downtime', '单点故障/SPOF', '消除单点', '冗余设计/Redundancy', 'N+1冗余', '2N冗余', '负载均衡/Load Balance', '四层负载均衡/L4', '七层负载均衡/L7', 'HAProxy概述/开源负载均衡', 'HAProxy安装配置', 'HAProxy配置/frontend', 'frontend定义', 'backend定义', 'server定义', 'listen定义', 'balance算法/roundrobin', 'balance leastconn', 'balance source', 'balance hdr', 'healthcheck检查', 'check inter/检查间隔', 'rise/fall/检查次数', 'cookie会话保持', 'option httpchk', 'option forwardfor', 'option redispatch', 'compression压缩', 'stats配置/监控', 'stats uri/统计页面', 'stats auth/认证', 'ACL访问控制', 'acl path_end', 'acl hdr_dom', 'use_backend', 'timeout配置', 'timeout connect', 'timeout client', 'timeout server', 'timeout check', 'log格式', '监控端口', 'HAProxy证书/HTTPS', 'HAProxy日志', 'HAProxy性能调优', 'Keepalived概述/VRRP', 'Keepalived安装', 'Keepalived配置/vrrp', 'vrrp_instance定义', 'state状态/Master/Backup', 'interface网卡', 'virtual_router_id', 'priority优先级', 'advert_int通告间隔', 'nopreempt非抢占', 'preempt_delay', 'virtual_ipaddress', 'virtual_server', 'real_server真实服务器', 'weight权重', 'TCP_CHECK', 'HTTP_GET', 'SSL_GET', 'MISC_CHECK', 'notify脚本', 'vrrp_script', 'track_script', 'VRRP原理', 'VRRP选举', 'VIP漂移', '脑裂问题/Split Brain', '脑裂检测', '脑裂预防', '主备切换/Failover', '故障检测/Health', '检测脚本', '双主配置/Dual Master', 'DNS轮询+Keepalived', 'MySQL + Keepalived', 'Nginx + Keepalived', 'LVS + Keepalived', '高可用架构设计', 'nginx upstream', 'nginx + upstream', 'nginx + Keepalived', 'apache + Keepalived', 'Redis Sentinel哨兵', 'Redis Sentinel架构', 'Redis主从复制', 'Redis自动故障转移', 'Redis Sentinel配置', 'sentinel monitor', 'sentinel down-after', 'sentinel failover', 'Redis Cluster集群', 'Redis Cluster分片', 'Redis Slots', 'MySQL MHA高可用', 'MHA Manager', 'MHA Node', 'MHA VIP切换', 'MHA配置', 'MHA自动切换', 'MySQL Galera Cluster', 'MySQL InnoDB Cluster', 'MySQL Router', 'MySQL Group Replication', 'Percona XtraDB Cluster', 'PostgreSQL高可用', 'Patroni/高可用', 'Etcd/分布式', 'Consul/服务发现', 'Pacemaker高可用', 'Corosync集群', 'DRBD双主', 'DRBD配置', 'Fence设备', '资源隔离/Fencing', 'STONITH隔离', 'VIP漂移/IPMI', 'NFS高可用', 'GlusterFS高可用', 'Ceph高可用', 'Zookeeper高可用', 'Zookeeper集群', 'Kafka高可用', 'Kafka集群', 'RabbitMQ高可用', '集群脑裂处理', '高可用测试', '故障演练']
                }
            }
        }
    },
    '数据科学': {
        '数据分析师': {
            'description': '收集、处理和分析数据，制作数据报表和可视化图表。',
            'skills': {
                'Excel': {
                    'desc': '电子表格数据处理和基础分析，包括透视表和函数',
                    'difficulty': 1,
                    'dimensions': ['Excel基础/单元格/工作表/工作簿', '数据类型/文本/数值/日期/货币', '单元格格式/数字/日期/自定义', '行列操作/插入/删除/隐藏', '快速填充/Ctrl+E', '选择性粘贴/数值/格式', '查找替换/Ctrl+F/Ctrl+H', '排序/单列排序/多列排序', '筛选/自动筛选/高级筛选', '条件格式/数据条/色阶/图标集', '公式基础/=开始/运算符', '引用方式/相对引用/绝对引用', '相对引用$A$1', '混合引用$A1/A$1', '函数/SUM/平均值/计数', 'SUM求和函数', 'AVERAGE平均值', 'COUNT计数/COUNTA', 'MAX/MIN最大最小', 'IF条件判断', 'IF嵌套/多层IF', 'AND/OR逻辑函数', 'COUNTIF单条件统计', 'COUNTIFS多条件', 'SUMIF条件求和', 'SUMIFS多条件求和', 'VLOOKUP纵向查找', 'HLOOKUP横向查找', 'VLOOKUP近似匹配', 'VLOOKUP精确匹配', 'INDEX/MATCH组合', 'INDEX+MATCH查找', 'XLOOKUP新函数', 'MATCH位置查找', 'INDIRECT跨表引用', 'OFFSET偏移引用', 'ROW/COLUMN行列号', 'TEXT文本函数', 'CONCATENATE文本合并', 'LEFT/RIGHT/MID截取', 'LEN文本长度', 'TRIM去除空格', 'SUBSTITUTE替换', 'DATE日期函数', 'TODAY/NOW当前日期', 'YEAR/MONTH/DAY', 'DATEDIF日期间差', 'WEEKDAY星期', 'EDATE/EOMONTH', '数据验证/下拉列表', '下拉菜单/序列', '圈释无效数据', '数据保护/工作表保护', '数据保护/工作簿保护', '数据透视表/PivotTable', '字段拖拽/行/列/值/筛选', '值汇总方式/求和/计数', '值显示方式/百分比', '计算字段/计算项', '切片器/切片器联动', '数据透视图', '分类汇总/小计', '合并计算', '模拟分析/单变量求解', '模拟分析/规划求解', '模拟分析/数据表', '规划求解/线性规划', '方案管理器', '宏/VBA入门', '录制宏', 'VBA编辑器', '数据导入/CSV/TXT', '数据导入/其他数据源', 'Power Query数据获取', 'Power Query转换', 'Power Pivot数据模型', 'DAX函数基础', '快捷键汇总/Ctrl', 'Alt键快捷键', '常用技巧/打印设置', '图表创建/柱形图/折线图', '图表创建/饼图/散点图', '图表创建/组合图', '迷你图/Sparkline', '图表美化/配色', '动态图表']
                },
                'Python': {
                    'desc': '数据处理和分析的编程工具',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/list/dict/set/tuple/控制流/循环/函数/类', 'Python环境/Python3/Pip/Anaconda', 'Jupyter Notebook/IPython', 'Anaconda环境管理', 'conda创建环境', 'pip安装包', 'NumPy数值计算', 'numpy.array创建', '数组形状/shape', '数组索引/切片', '数组运算/广播', 'NumPy函数/mean/sum/std', 'Pandas数据处理', 'Series序列', 'DataFrame数据框', 'read_csv读取', 'head/tail查看', 'info/describe', 'dtypes列类型', '列选择/单列/多列', 'loc/iloc索引', '布尔索引/筛选', 'query查询', '新增列/赋值', '删除列/drop', '重命名列/rename', '数据类型转换', 'astype类型转换', 'to_numeric/to_datetime', '缺失值处理/isna/dropna', 'fillna填充', 'ffill/bfill前向后向', '去重/drop_duplicates', '排序/sort_values', '排名/rank', '合并/concat/merge/join', 'concat行合并', 'merge关联', 'join列合并', '分组/groupby', 'agg聚合函数', 'transform分组计算', 'apply自定义函数', 'pivot_table透视', '交叉表/crosstab', '字符串处理/str方法', '正则表达式/re', '时间处理/pandas日期', 'to_datetime解析', 'resample重采样', 'dt访问器/year/month', 'Matplotlib绘图', 'plot绑定数据', 'figure/axes', '折线图/plot', '柱状图/bar', '散点图/scatter', '直方图/hist', '饼图/pie', '子图/subplot', 'subplots多图', '图表美化/标题/标签', '图例/legend', '中文显示/字体', 'Seaborn统计图', 'sns.load_dataset', '关系图/relplot', '分布图/distplot/histplot', '分类图/catplot', '热力图/heatmap', 'PairPlot配对图', '回归图/lmplot', 'Style/Context设置', 'Plotly交互图', 'px.bar/plotly柱状图', 'px.line/plotly折线图', 'px.scatter/散点图', 'px.pie饼图', 'px.scatter_mapbox', 'px.sunburst旭日图', 'Express高速绑定', 'Graph Objects底层', 'Cufflinks/数据绑定', 'Scipy科学计算', 'Pandas_profiling报告', 'Sweetviz可视化分析', 'D-Tale数据探索', '数据探索/EDA', 'Scikit-learn基础', '数据标准化/scale', 'train_test_split', '统计分析/scipy.stats', 'statsmodels回归', 'Python连接数据库', 'pymysql查询', 'sqlalchemy连接', '数据导出/to_csv/excel', '数据导出/to_sql', '脚本自动化/schedule', 'Git版本控制']
                },
                'SQL': {
                    'desc': '数据库查询和数据提取',
                    'difficulty': 1,
                    'dimensions': ['SQL概述/结构化查询', '数据库/DBMS/MySQL', '数据库/PostgreSQL', '数据库/SQLite', '数据库/Oracle', '数据库/SQL Server', '连接数据库/客户端', 'Navicat/DBeaver', '基本查询/SELECT', 'SELECT *全查询', 'SELECT列选择', '列别名/AS', '去重/DISTINCT', 'WHERE条件', '比较运算符/> /< /=/!=', '逻辑运算符/AND/OR/NOT', 'BETWEEN AND范围', 'IN列表匹配', 'LIKE模糊匹配', '%通配符', '_单个匹配', 'IS NULL空值', 'IS NOT NULL非空', 'ORDER BY排序', 'ASC/DESC升序降序', '多列排序', 'LIMIT限制行数', 'TOP/MYSQL LIMIT', '聚合函数/SUM/AVG', 'COUNT计数', 'MAX/MIN最大最小', 'GROUP BY分组', 'HAVING分组筛选', '分组过滤/HAVING', 'WHERE vs HAVING', '子查询/嵌套查询', '标量子查询', '列子查询', '行子查询', '表子查询', 'EXISTS存在判断', 'IN子查询', '关联子查询', 'JOIN连接/内连接', 'INNER JOIN内连接', 'LEFT JOIN左连接', 'RIGHT JOIN右连接', 'FULL JOIN全连接', 'CROSS JOIN笛卡尔', 'ON连接条件', 'USING简化连接', '自然连接/NATURAL JOIN', '多表连接/三表以上', '自连接/SELF JOIN', 'UNION合并查询', 'UNION ALL不过滤', 'INTERSECT交集', 'EXCEPT差集', 'CASE WHEN分支', 'CASE WHEN多条件', 'CASE WHEN聚合', 'COALESCE空值处理', 'NULLIF条件空', 'CAST类型转换', 'CONVERT类型转换', '日期函数/MySQL', 'DATE/NOW/CURDATE', 'YEAR/MONTH/DAY', 'DATE_ADD/日期加减', 'DATEDIFF日期差', '日期格式化/DATE_FORMAT', '字符串函数/CONCAT', 'CONCAT_WS分隔符', 'LENGTH/CHAR_LENGTH', 'UPPER/LOWER大小写', 'TRIM去除空格', 'SUBSTRING截取', 'REPLACE替换', 'INSTR查找位置', 'IF函数/IFNULL', 'IF条件函数', 'WINDOW函数/窗口', 'ROW_NUMBER排名', 'RANK排名并列', 'DENSE_RANK连续', 'LAG/LEAD偏移', 'SUM OVER累计', 'AVG OVER移动平均', 'FIRST_VALUE/LAST_VALUE', 'OVER分区内', 'PARTITION BY分区', 'ORDER BY窗口内', 'WITH CTE公用表', '递归CTE', 'INSERT插入/INSERT INTO', 'UPDATE更新', 'DELETE删除', 'TRUNCATE清空', 'CREATE TABLE创建', 'ALTER TABLE修改', 'DROP TABLE删除', '索引/INDEX', '视图/VIEW', '事务/BEGIN/COMMIT', 'ROLLBACK事务回滚', '约束/PRIMARY KEY', 'FOREIGN KEY外键', 'UNIQUE唯一约束', 'CHECK检查约束', 'DEFAULT默认约束', 'EXPLAIN执行计划', 'SQL优化/索引使用', 'SQL调优']
                },
                'A/B测试': {
                    'desc': '设计实验验证假设，评估产品改动效果',
                    'difficulty': 2,
                    'dimensions': ['A/B测试概述/AB Test', '实验设计/Experiment Design', '假设检验/Hypothesis Testing', '原假设/H0零假设', '备择假设/H1', '单侧检验/双侧检验', 'P值/P-value', '显著性水平/α/Alpha', '置信水平/Confidence Level', '置信区间/Confidence Interval', '95%置信区间', '统计功效/Power/β', '样本量计算/Sample Size', '效应量/Effect Size', 'Cohen d/ES', '最小可检测效应/MDE', '分流策略/Randomization', 'AA分流/均匀性检验', '流量分配/Traffic Split', '分层实验/Layer/Stratified', '正交实验/Orthogonal', '用户分组/User ID', '设备分组/Device ID', 'Cookie分流', 'Session分流', '随机分配/Random', '分层抽样', '控制组/Control Group', '实验组/Treatment Group', '核心指标/北极星', '辅助指标/Guardrail', '点击率/CTR/Click Rate', '转化率/CVR/Conversion', '停留时长/Duration', '跳出率/Bounce Rate', 'GMV/成交总额', 'DAU/日活用户', 'MAU/月活用户', 'ARPU/用户价值', 'LTV/生命周期价值', 'AB平台/Exp Platform', '分流服务/Split', '实验配置', '实验标签', 'AB效果评估/Analysis', '结果统计/Statistical', 't检验/t-test', 'z检验/z-test', '卡方检验/Chi-square', 'Mann-Whitney U检验', 'ANOVA方差分析', '功效分析/Power Analysis', '结果可视化/Plot', '统计显著性/Significant', '非显著/Not Significant', '新奇效应/Novelty Effect', '首日效应/First-Day', 'Seasonality季节性', '节假日效应', '外部因素控制', '辛普森悖论/Simpson', '辛普森逆转', '下钻分析/Drill Down', '归因分析/Attribution', '多变量测试/MVT', 'MVT vs A/B', '全因子实验/Factorial', 'Bandit算法/MAB', 'Thompson Sampling', 'Epsilon-Greedy', 'UCB上置信界', 'Contextual Bandit', 'AB测试报告/Report', 'AB测试文档', '实验结论', '实验建议', 'A/B测试系统', 'ExpEngine实验引擎']
                },
                'FineBI': {
                    'desc': '国产商业智能工具',
                    'difficulty': 2,
                    'dimensions': ['FineBI概述/帆软BI/国产BI', 'FineBI安装/配置', 'FineBI Web管理', 'FineBI登录/用户', '数据连接/数据源', '业务包/数据包', '抽取数据/直连', '实时数据/直连模式', '本地Excel数据', '数据库连接/MySQL', 'SQL数据集/自定义', '表管理/数据表', '创建自助数据集', '自助ETL/数据处理', '过滤/筛选数据', '新增列/计算', '列重命名/类型', '数据合并/上下合并', '数据合并/左右关联', '行列转换', '分组汇总/group', '排序/sort', '交叉表/pivot', '函数计算/SUM/AVG', 'COUNT/去重计数', 'IF条件函数', 'DATE日期函数', 'TEXT文本函数', 'NULL处理/IFNULL', 'COALESCE函数', '时间序列函数', 'LAG/LEAD偏移', '累计计算/累计SUM', '同期计算/环比', '同比计算/YoY', '维度和指标', '指标拆解', '计算字段', '过滤组件/Filter', '下拉筛选/Dropdown', '列表筛选/Table', '日期筛选/Date', '范围筛选/Range', '文本筛选', '筛选交互', '图表类型/柱形图', '图表类型/折线图', '图表类型/饼图', '图表类型/散点图', '图表类型/地图', '图表类型/雷达图', '图表类型/漏斗图', '图表类型/词云图', '图表类型/桑基图', '图表类型/矩形树图', '组合图/双Y轴', '明细表/数据表', '汇总表', '聚合报表/决策报表', '仪表板/Dashboard', '仪表板布局', '组件联动/Linkage', '过滤联动', '跳转/Hyperlink', '数据钻取/Drill', '上下钻', '参数/Parameter', '联动钻取', '样式设置/主题', '配色方案', '字体样式', '图表样式', '标题/图例/轴', '标签/Label', '提示/Tooltip', '分享协作/Share', '定时调度/Schedule', '邮件推送', '移动端/App', '权限管理/Users', '角色权限/Roles', '行级权限', '列级权限', '数据权限', '公共数据/数据中心', '我的数据/个人', 'FineBI仪表板', 'FineBI模板', 'FineBI移动端', 'FineBI报告']
                },
                'Power BI': {
                    'desc': '微软商业智能分析工具',
                    'difficulty': 2,
                    'dimensions': ['Power BI概述/微软BI/PBI', 'Power BI Desktop安装', 'Power BI Pro许可证', 'Power BI Premium', 'Power BI Service云服务', 'Power BI Mobile', '数据获取/Get Data', '导入模式/Import', 'Live Connection', 'DirectQuery直连', 'Composite Model混合', 'Excel导入', 'CSV/TXT导入', 'Web数据获取', '数据库/MySQL/SQL', 'Azure数据源', 'SharePoint数据', '文件夹数据', 'Power Query编辑器', 'M语言/Power Query', '数据转换/Transform', '列操作/类型/重命名', '删除列/保留列', '拆分列/Split Column', '合并列/Merge', '透视列/Pivot', '逆透视/Unpivot', '追加查询/Append', '合并查询/Merge', '条件列/Add Column', '自定义列/Custom', '分组依据/Group By', '数据类型转换', '填充/ Fill Down/Up', '提取/Extract', '日期提取/year/month', '文本提取/left/right', '替换值/Replace', '删除重复项', '删除错误/Delete Error', '行筛选/Filter Rows', '保留行/Keep Rows', '参数/Parameters', '参数表', '查询重用', 'Data Model数据模型', '关系视图/Relationships', '维度表/Dimension', '事实表/Fact', '星型模型/Star Schema', '雪花模型/Snowflake', '维度类型/Type', '主键/Primary Key', '外键/Foreign Key', '关系基数/One-to-One', '基数/一对多', '多对多/Many-to-Many', '交叉筛选方向/Both', '单方向/单箭头', '双向筛选/Bidirectional', 'DAX语言/Data Analysis', 'DAX基础/语法', 'CALCULATE计算', 'SUM/ SUMX聚合', 'AVERAGE/ AVERAGEX', 'COUNT/COUNTA', 'COUNTROWS/ DISTINCTCOUNT', 'FILTER筛选上下文', 'ALL/ALLEXCEPT', 'RELATED关联', 'RELATEDTABLE', '时间智能/Time Intelligence', 'TOTALYTD年度累计', 'TOTALQTD季度累计', 'TOTALMTD月累计', 'PARALLELPERIOD同期', 'SAMEPERIODLASTYEAR', 'PREVIOUSMONTH上月', 'NEXTMONTH下月', 'DATESBETWEEN日期', 'IF条件判断', 'SWITCH多分支', 'DIVIDE安全除法', 'BLANK空值', 'EARLIER上下文', 'MAX/MIN极值', 'RANKX排名', 'TOPN/N', '度量值/Measure', '计算列/Calculated Column', 'Quick Measure快速度量', '行上下文/Row Context', '筛选上下文/Filter Context', '上下文转换', '迭代器/X后缀函数', 'VAR变量', 'RETURN返回值', 'KPI视觉对象', '指标卡/Card', '多行卡', '折线图/Line Chart', '面积图/Area', '堆叠柱形图/Stacked', '簇状柱形图/Clustered', '条形图/Bar Chart', '饼图/Pie Chart', '环形图/Donut', '散点图/Scatter', '气泡图/Bubble', '地图/Map', '填充地图/Filled Map', 'ArcGIS地图', '矩阵/Matrix', '表/Table', '多行卡', '仪表/Gauge', '关键影响因素', '分解树/Decomposition', '智能叙事/Smart Narrative', 'Q&A问答', '筛选器/Filters', '切片器/Slicer', '日期切片器', '同步切片器', '可视化交互/Selection', '钻取/Drillthrough', '书签/Bookmarks', '按钮/Buttons', 'Actions动作', '页面导航', '工具提示/Pages', 'RLS行级安全/Row Level', '角色管理', 'DAX RLS', '用户名函数/USERNAME', '发布Publish', 'Power BI Service', '工作区/Workspace', 'App工作区', '内容打包', '共享/Share', '工作流/Approval', '行级别安全', '数据保护/Sensitivity', '刷新计划/Schedule', '增量刷新', '网关/Gateway', 'On-premises Data Gateway', 'Enterprise Gateway', '内容管理', 'Power BI Mobile', 'DAX Studio调试', 'DAX格式化', '最佳实践', '性能优化', '报表设计', 'Dashboard设计']
                },
                'Tableau': {
                    'desc': '商业智能可视化工具，制作交互式图表和仪表板',
                    'difficulty': 2,
                    'dimensions': ['Tableau概述/可视化BI', 'Tableau Desktop安装', 'Tableau Public免费版', 'Tableau Online云', 'Tableau Server企业版', 'Tableau Prep数据准备', 'Tableau Prep Builder', '连接数据源/Data Source', 'Live连接/Live', 'Extract抽取数据', '多个数据源/Multi', '数据混合/Data Blending', '混合/Blend Relationships', '数据解释/Explain Data', '工作表/Sheet', '功能区/Analytics Pane', '拖拽操作', '维度和度量/Dimension', '度量/Measure', '连续/离散/Continuous', '分类/Discrete', '颜色编码/Color', '快速表计算/Quick Table', '合计/Grand Total', '小计/Subtotal', '聚合/Aggregation', 'SUM/AVG/COUNT', 'MIN/MAX', 'MEDIAN中位数', 'ATTR属性', 'CNTD去重计数', '维度的角色/Role', '维度属性/Attribute', '标记卡/Marks Card', '颜色/Color', '大小/Size', '标签/Label', '详细信息/Detail', '工具提示/Tooltip', '形状/Shape', '路径/Path', '多边形/Polygon', '图表类型/条形图', '标准条形图/Bar', '堆叠条形图/Stacked', '并排条形图/Side-by-side', '视图组合/dual axis', '折线图/Line', '多线图/Multi-line', '连续线/Continuous', '离散线/Discrete', '区域图/Area', '饼图/Pie', '符号地图/Symbol Map', '填充地图/Filled Map', '地图层/Map Layers', '热力地图/Heat Map', '树地图/Treemap', '气泡图/Bubble', '散点图/Scatter', '箱形图/Box Plot', '直方图/Histogram', '甘特图/Gantt', '帕累托图/Pareto', '瀑布图/Waterfall', '子弹图/Bullet', '闪烁图/Packaged', '符号地图/City Map', '路径地图/Path', '流向地图/Flow', '圆圈图/Circle View', '数据点密度/Density', '日历图/Calendar', '斜率图/Slope Chart', '范围图/Range', '标靶图/Bullet Graph', '文字表/Text Table', '突出显示表', '交叉表/Crosstab', '聚合与详细级别/LOD', 'FIXED LOD固定', 'INCLUDE LOD包含', 'EXCLUDE LOD排除', 'LOD表达式', 'FIXED SUM Sales', 'FIXED {ATTR}', 'INCLUDE Profit Ratio', '表计算/Table Calculation', 'Running Total累计', 'Percent of Total总计百分比', 'Percent Difference差异', 'Moving Average移动平均', 'YTD Total年初至今', 'YOY同比', 'MoM环比', 'Rank排名', 'Window Sum', 'Lookup偏移', 'Previous Value', '快速表计算/Quick', '计算类型/Compute using', '表结构/Table Down/Across', '重启间隔/Per Partition', '参数/Parameter', '参数筛选', '参数联动', '计算字段/Calculated Field', 'IIF条件函数', 'IF/THEN/ELSE', 'CASE WHEN', 'ZNP/ZN防空', 'ISNULL空值', 'CONTAINS包含', 'STARTSWITH/BEGINS', 'FLOAT/DATE类型', 'STR/STRING转换', 'PARSE_DATE解析', 'DATETIME/MOD', '筛选器/Filter', '上下文筛选器/Context', '维度筛选器', '度量筛选器', '顶部筛选/Top', '条件筛选', 'Wildcard匹配', '筛选器显示/Show Filter', '多值筛选', '单值筛选', '范围筛选/Range', '日期范围', '筛选器选项/General', '使用所有工作表', 'LIKE匹配', '排序/Sort', '手动排序', '计算排序', '数据排序', '分组/Group', '分组创建', '合并内部数据', '集/Set', '常量集/Constant Set', '计算集/Computed Set', 'IN/OUT成员', '集值/Set Controls', '集交集/Combination', '集差异/Difference', '分层结构/Hierarchy', '展开/Collapse', 'ドリルダウン/Drill Down', '故事/Story', '故事点/Story Points', '仪表板/Dashboard', '仪表板布局', '平铺/Tiled', '浮动/Floating', '大小适应/Size Fit', '设备设计/Device', '移动端布局', '仪表板操作/Action', '筛选器操作', '高亮操作', 'URL操作', '转到工作表', '参数操作', '仪表板主题', '固定列宽', '容器/Container', '垂直/水平布局', '填充/Padding', '边距/Margin', '筛选器窗格', '格式设置/Format', '字体/Colors', '边框/Boarder', '工作簿主题', '工作表主题', '故事主题', '发布/Publish', 'Tableau Server', 'Tableau Online', '用户权限/Permissions', '项目/Project', '工作簿权限', '数据源权限', '刷新计划', '订阅/Subscription', '告警/Alert', '注释/Annotation', '趋势线/Trend Lines', '参考线/Reference Line', '参考区间/Reference Band', '预测/Forecast', '聚类/Cluster', 'Tableau AI/Explain Data', '最佳实践/设计原则', '配色方案', '视觉最佳实践']
                },
                '业务理解': {
                    'desc': '深入理解业务场景，将数据转化为业务洞察',
                    'difficulty': 2,
                    'dimensions': ['业务理解概述/Business', '业务背景/BG', '业务流程/Business Process', '业务场景/Scenario', '业务术语/Glossary', '业务指标/KPI', '北极星指标/One Metric', 'OKR目标管理', '业务流程图/Flow', '泳道图/Swimlane', '价值流图/Value Stream', '业务需求文档/BRD', 'PRD产品需求', '需求分析/Requirement', '功能需求/FR', '非功能需求/NFR', '需求调研/访谈', '需求确认/Approval', '用户故事/User Story', 'As a /I want/So that', '验收标准/AC', 'Definition of Done', '用户画像/Persona', '用户角色/Role', '用户旅程/Journey', '触点/Touchpoint', '用户行为/Behavior', '用户动机/Motivation', '用户痛点/Pain Point', '业务规则/Business Rule', '业务约束/Constraint', '业务边界/Boundary', '业务逻辑/Logic', '异常处理/Exception', '业务场景分析', 'To-Be现状分析', 'As-Is现状分析', '业务现状', '业务痛点', '改进机会', '业务目标/Objective', '业务策略/Strategy', '业务计划/Plan', '业务价值/Business Value', 'ROI投资回报', '成本效益分析', '业务影响力', '数据分析驱动', '数据驱动决策/DDD', '数据指标体系', '指标定义/Metric Def', '指标计算口径', '指标归因/Attribution', '业务指标拆解', 'GMV拆解', '收入拆解', 'DAU拆解', '转化率拆解', '漏斗分析/Funnel', '归因模型/Attribution Model', '首次触点归因', '末次触点归因', '线性归因', '时间衰减归因', '数据驱动业务', '业务问题定义', '问题分析框架', '5W2H分析法', 'SWOT分析', 'PEST分析', '波特五力', '生命周期/Lifecycle', '用户生命周期', '客户生命周期', '产品生命周期', '业务周期/Seasonality', '周期性分析', '趋势分析/Trend', '同期对比/YoY', '环比分析/MoM', '业务理解沟通', '跨部门沟通', '技术沟通/Tech Talk', '业务汇报/Presentation', '金字塔原理', 'SCQA结构', '故事线/Storyline', '业务洞察/Insight', '洞察提炼', '洞察验证', '洞察应用', 'AARRR模型', '获客/Acquisition', '激活/Activation', '留存/Retention', '变现/Revenue', '推荐/Referral', 'RFM模型', 'R-Recency最近', 'F-Frequency频率', 'M-Monetary金额', 'ABM客户分层', '用户分层/User Layer', '用户分群/Segmentation', '用户标签/Tagging', '标签体系', '画像标签', '行为标签', '规则标签', '模型标签', '业务复盘', '业务复盘方法', 'KISS复盘', 'KPT复盘']
                },
                '报表开发': {
                    'desc': '定期生成业务报表，监控关键指标',
                    'difficulty': 2,
                    'dimensions': ['报表概述/Report', '报表类型/管理报表', '业务报表/运营报表', '财务报表/财务表', '数据报表/Analytics', '报表需求/Requirements', '报表设计/Design', '报表模板/Template', '报表开发/Dev', '报表发布/Publish', '报表分发/Distribution', '报表监控/Monitor', '数据来源/Source', '数据表结构', '数据字典/Schema', 'ETL数据处理', '数据仓库/DW', 'ODS贴源层', 'DWD明细层', 'DWS汇总层', 'ADS应用层', '数据分层/DWD/DWS/ADS', '数据域/Data Domain', '业务过程/Business Process', '维度/Dimension', '度量/Measure', '事实表/Fact Table', '事务事实表', '周期快照表', '累计快照表', '维度表/Dim Table', '缓慢变化维/SCD', 'SCD Type1覆盖', 'SCD Type2新增', 'SCD Type3混合', '代理键/Surrogate Key', '自然键/Natural Key', '拉链表/Slowly Change', '数据同步/Sync', '全量同步/Full', '增量同步/Incremental', '实时同步/CDC', 'Kafka CDC', 'Debezium', 'Canal同步', '数据清洗/Cleaning', '空值处理', '异常值处理', '数据标准化', '数据转换', '数据一致性', '数据准确性', 'SQL报表查询', 'Hive查询', 'SparkSQL', 'Presto查询', 'Impala查询', 'ClickHouse查询', 'Doris查询', '报表开发/SQL', 'DQL数据查询', '分层指标计算', '复杂SQL编写', '窗口函数应用', '数据汇总/AGG', '报表BI工具', 'FineReport报表', 'FineBI仪表板', 'Tableau报表', 'PowerBI报表', 'QuickBI报表', 'Apache Superset', 'Metabase', 'ReportBuilder', 'Crystal Reports', 'Excel报表', '固定格式报表', '自适应报表', '报表字段/Columns', '报表指标/Metrics', '报表筛选/Filters', '日期筛选', '下拉筛选', '多选筛选', '报表排序/Sort', '报表分组/Group', '小计合计/Subtotal', '总计/Grand Total', '报表导出/Export', 'Excel导出', 'PDF导出', 'CSV导出', '报表定时任务', 'Cron定时', 'Airflow调度', 'DolphinScheduler', '任务编排', '报表刷新/Refresh', '自动刷新', '手动刷新', '数据更新', '报表质量/QoR', '报表准确性', '报表时效性', '报表完整性', '报表一致性', '报表可读性', '报表审核/Review', '报表审批/Approval', '报表分发/Share', '邮件推送/Push', '自动化推送', '邮件模板', '钉钉推送', '飞书推送', '企业微信', '报表权限/Permission', '行级权限', '列级权限', '用户权限', '部门权限', '报表监控/Monitor', '数据监控', '任务监控', '异常监控', 'SLA监控', '报表管理/Manage', '报表目录', '元数据管理', '报表标签', '报表评价', '报表迭代', '报表优化', '报表归档/Archive', '报表下线', 'BI平台建设', '指标平台', 'OneData体系', '数据治理/Governance', '报表规范/Standard', '命名规范', '开发规范']
                },
                '数据可视化': {
                    'desc': '将数据转化为图表和仪表板展示，设计清晰的数据故事',
                    'difficulty': 2,
                    'dimensions': ['数据可视化概述/Visualization', '可视化目标/Purpose', '受众分析/Audience', '数据故事/Data Story', '图表选择/Chart Selection', '数据关系/Relationship', '比较关系/Comparison', '趋势关系/Trend', '构成关系/Composition', '分布关系/Distribution', '关联关系/Correlation', '位置关系/Location', '数据编码/Data Encoding', '位置编码/Position', '颜色编码/Color', '大小编码/Size', '形状编码/Shape', '角度编码/Angle', '面积编码/Area', '图表类型/柱状图', '垂直柱状图', '水平柱状图', '堆叠柱状图', '百分比堆叠', '分组柱状图', '双向柱状图', '折线图/Line Chart', '多线图', '面积图/Area Chart', '堆叠面积图', '百分比面积图', '饼图/Pie Chart', '环形图/Donut', '旭日图/Sunburst', '树图/Treemap', '瀑布图/Waterfall', '漏斗图/Funnel', '散点图/Scatter', '气泡图/Bubble', '热力图/Heatmap', '日历热力图', '地图可视化/Map', '填充地图', '符号地图', '流向地图', '统计地图', '密度图/Density', '六边形网格/Hexbin', '箱线图/Box Plot', '小提琴图/Violin', '直方图/Histogram', '密度曲线图', '雷达图/Radar', '南丁格尔玫瑰图', '仪表盘/Gauge', '子弹图/Bullet', 'KPI卡片/Card', '数字卡片', '趋势指标卡', '漏斗转化图', '桑基图/Sankey', '和弦图/Chord', '网络图/Network', '力导向图', '关系图', '甘特图/Gantt', '日历图/Calendar', '时间线/Timeline', '流程图/Flowchart', '对比图/Comparison', '蝴蝶图/Butterfly', '哑铃图/Dumbbell', '坡度图/Slope', '标靶图/Target', '配色方案/Color', '分类配色', '连续配色', '发散配色', '色盲友好配色', '品牌配色', '渐变色配色', '单色配色', '图表配色工具', '色轮/Color Wheel', '配色原则', '颜色心理学', '字体选择/Font', '无衬线字体', '中文字体', '数字字体', '标题字体', '正文字体', '字体大小/Hierarchy', '留白/Whitespace', '对齐/Alignment', '网格/Grid', '黄金比例', '图表网格', '响应式设计', '移动端适配', '图表标题/Title', '副标题/Subtitle', '图例/Legend', '坐标轴/Axis', '轴标签/Axis Label', '网格线/Gridline', '数据标签/Label', '提示/Tooltip', '注释/Annotation', '标注/Callout', '引导线/Reference Line', '趋势线/Trendline', '基准线/Baseline', 'ECharts图表库', 'ECharts折线图', 'ECharts柱状图', 'ECharts饼图', 'ECharts散点图', 'ECharts地图', 'ECharts热力图', 'ECharts雷达图', 'ECharts关系图', 'ECharts漏斗图', 'ECharts桑基图', 'ECharts配置项', 'ECharts series', 'ECharts option', 'AntV蚂蚁金服', 'AntV G2图表', 'AntV G6网络图', 'AntV F2移动端', 'AntV L7地理', 'D3.js可视化', 'D3数据驱动', 'SVG绑定', 'D3选择器', 'D3数据JOIN', 'D3比例尺/Scale', 'D3轴/Axis', 'D3路径/Path', 'D3过渡/Transition', 'Vega-Lite声明式', 'Plotly.py交互', 'px折线/line', 'px柱状/bar', 'px饼/pie', 'px散点/scatter', 'px地图/scatter_mapbox', 'px热力/density_mapbox', 'px雷达/radar', 'px旭日/sunburst', 'pyecharts', 'pyecharts配置', 'pyecharts主题', 'pyecharts组合', 'GraphXR/3D可视化', 'Deck.gl/大规模', 'Kepler.gl/地理', 'Mapbox/地图', 'Tableau可视化', 'FineBI可视化', 'PowerBI可视化', '数据仪表板/Dashboard', '仪表板设计', '仪表板布局', '仪表板交互', '仪表板配色', '故事叙述/Storytelling', '数据叙事', '可视化最佳实践', '可访问性/Accessibility', '动效可视化/Animation', '实时可视化', '大数据可视化']
                },
                '数据报告': {
                    'desc': '撰写数据分析报告，提供决策建议',
                    'difficulty': 2,
                    'dimensions': ['数据报告概述/Report', '报告类型/分析报告', '业务报告/战略报告', '周期性报告/日报', '周报/Weekly', '月报/Monthly', '季报/Quarterly', '年报/年度报告', '专题报告/Analysis', '调研报告/Research', '评估报告/Evaluation', '报告受众/Readers', '管理层报告', '业务部门报告', '技术团队报告', '报告结构/Structure', '执行摘要/Executive', '背景/Background', '目的/Objective', '方法/Methodology', '发现/Finding', '结论/Conclusion', '建议/Recommendation', '附录/Appendix', '报告标题/Title', '报告日期/Date', '报告人/Author', '报告版本/Version', '报告规范/Standard', '文档模板/Template', '报告框架/Framework', 'STAR法则/Situation', 'PEST框架', 'SWOT分析报告', '5W2H分析', '问题定义/Problem', '分析问题', '解决问题', '数据收集/Data', '数据来源/Source', '数据时间范围', '数据可靠性', '数据样本量', '数据方法/Methods', '描述性统计', '趋势分析', '对比分析', '归因分析', '预测分析', '假设检验', '分析方法/Techniques', '同比环比分析', '拆解分析/Pyramid', '漏斗分析', '相关性分析', '回归分析', '聚类分析', '因子分析', '分析维度/Dimension', '时间维度', '地区维度', '渠道维度', '用户维度', '产品维度', '业务维度', '分析维度选择', '关键指标/KPI', '核心指标', '先行指标', '滞后指标', '指标计算', '指标定义', '指标口径', '数据图表/Charts', '图表选择', '图表呈现', '图表说明', '数据洞察/Insight', '洞察提炼', '洞察分类', '洞察验证', '洞察优先级', '洞察排序', '发现/Finding', '关键发现', '核心结论', '数据支撑', '分析结论', '结论推导', '结论验证', '建议/Recommendation', '行动建议', '优先级建议', '可行性评估', '风险提示', '成本预估', '收益预估', '预期效果', '实施路径', '下一步行动', '报告写作/Writing', '专业术语', '简洁表达', '逻辑清晰', '数据支撑', '避免偏见', '客观中立', '金字塔写作', 'MECE原则', '报告排版/Layout', '字体字号', '段落格式', '标题层级', '页眉页脚', '目录/TOC', '页码/Page', '图表编号', '表格编号', '报告配色', '报告配图', '数据表格/Table', '数据表设计', '表头设计', '行列合并', '样式美化', '表格解读', '数据引用/Cite', '数据来源标注', '数据时效性', '数据局限性', '报告审核/Review', '数据核查', '逻辑核查', '格式核查', '同行评审', '报告发布/Publish', '报告分发', '报告存档', '报告更新', '报告复盘', '演示技巧/Presentation', 'PPT制作', '演讲技巧', '问答应对', '演示工具/PowerPoint', 'Keynote', 'Google Slides', 'Canva演示', '报告自动化', '报告模板化', '数据自动更新', '定期报告自动化']
                },
                '数据清洗': {
                    'desc': '处理缺失值、异常值、重复数据',
                    'difficulty': 2,
                    'dimensions': ['数据清洗概述/Cleaning', '数据质量/DQ/Data Quality', '数据质量维度', '完整性/Completeness', '准确性/Accuracy', '一致性/Consistency', '及时性/Timeliness', '唯一性/Uniqueness', '有效性/Validity', '数据探索/EDA/Exploratory', '数据预览/head/tail', '数据类型/dtypes', '数据形状/shape', '数据统计/describe', '缺失值分析/isna', '缺失比例/percent', '重复值分析/duplicated', '异常值检测/outlier', '数据清洗流程', '问题识别', '问题处理', '结果验证', '清洗文档/Documentation', '缺失值/Missing Value', '缺失原因/Missing', 'MCAR完全随机', 'MAR随机缺失', 'MNAR非随机', '删除法/Drop', '行删除/Listwise', '列删除/Drop Column', '均值填充/Mean', '中位数填充/Median', '众数填充/Mode', '固定值填充/Constant', '前向填充/ffill', '后向填充/bfill', '插值填充/Interpolate', '线性插值', '多项式插值', 'KNN插补/KNN Imputer', 'MICE多重插补', '回归填充/Regression', '模型预测填充', '标识缺失/Indicator', '缺失值作为特征', '重复数据/Duplicate', '完全重复/Exact', '部分重复/Partial', '重复检测/duplicated', '重复行删除/drop', '保留策略/first/last', '异常值/Outlier', '异常类型/Extreme', '统计方法/Z-score', 'Z-score计算', 'Z-score阈值', 'IQR方法/四分位', 'Q1/Q3/四分位', 'IQR计算', '1.5倍IQR规则', '箱线图检测', '散点图检测', '可视化检测', '3σ原则', '分布检测', '正常范围', '异常值处理', '删除/Delete', '替换/Replace', '缩尾/Winsorize', '盖帽法/Capping', '对数变换/log', '分箱/Binning', 'NA处理/视为缺失', '标记/Flag', '业务规则判定', '逻辑校验', '规则引擎', '数据不一致/Inconsistent', '格式标准化', '大小写统一', '日期格式统一', '数值格式', '编码格式', '数据类型统一', '文本清洗/Text', '去空格/trim', '去除特殊字符', '去除乱码', '大小写转换', '繁简转换', '拼写纠正', '同义词处理', '文本标准化', '数据合并/Cleaning', '主键合并', '字段匹配', '合并冲突', '合并后验证', '数据拆分/Split', '分列/Split', '提取/Extract', '拆分规则', '数据转换/Transform', '类型转换/astype', '编码转换/Encode', '标准化/Scaling', '归一化/Normalization', '正则表达式/re', '模式匹配', '数据验证/Validation', '规则验证', '范围验证', '格式验证', '一致性验证', '跨表验证', '业务规则验证', '清洗脚本/Script', 'Python清洗', 'Pandas清洗', 'SQL清洗', '数据清洗工具', 'OpenRefine', 'Trifacta', 'DataWrangler', 'Kettle/ETL', '数据质量规则', '数据质量检查', '自动化清洗', '清洗流程文档', '清洗日志', '清洗报告', '清洗效果评估', 'ETL清洗/数据清洗', 'ELT清洗', '清洗最佳实践']
                },
                '统计分析': {
                    'desc': '描述统计、推断统计、相关分析、回归分析等方法',
                    'difficulty': 2,
                    'dimensions': ['统计分析概述/Statistics', '描述性统计/Descriptive', '数据类型/定类/定序', '数据类型/定距/定比', '集中趋势/Central Tendency', '均值/Mean/Average', '中位数/Median', '众数/Mode', '截尾均值/Trimmed', '几何均值/Geometric', '离散程度/Dispersion', '极差/Range', '方差/Variance', '标准差/Standard Dev', '变异系数/CV', '偏度/Skewness', '峰度/Kurtosis', '四分位数/Quartile', 'Q1/Q2/Q3分位', '百分位数/Percentile', '五数概括/Min/Q1', '箱线图/Box Plot', '频数分布/Frequency', '频率分布/Relative Freq', '列联表/Contingency', '交叉表/Crosstab', '比例/Proportion', '比率/Ratio', '百分比/Percentage', '数据可视化/Plot', '直方图/Histogram', '密度曲线', 'QQ图/正态性', '茎叶图/Stem-and-Leaf', '点图/Dot Plot', '条形图/Bar Chart', '饼图/Pie Chart', '推断统计/Inferential', '抽样分布/Sampling', '中心极限定理/CLT', '标准误差/SE', '点估计/Point Estimate', '区间估计/Interval', '置信区间/Confidence', '95%置信区间', '99%置信区间', '置信水平/Level', 'Z分数/Z-score', '标准正态分布', '假设检验/Hypothesis', '原假设/H0', '备择假设/H1', '单侧检验/双侧', '检验统计量', 'P值/P-value', '显著性水平/α', '拒绝域/Reject', '临界值/Critical', '第一类错误/Type I', '第二类错误/Type II', '功效/Power', '样本量计算', '效应量/Effect Size', 'Cohen d', '假设检验步骤', 'z检验/z-test', '单样本z检验', '两样本z检验', 't检验/t-test', '单样本t检验', '两独立样本t', '配对样本t检验', '配对设计', '方差齐性检验', 'Welch t检验', '非参数检验', 'Wilcoxon符号秩', 'Mann-Whitney U', 'Kruskal-Wallis H', '卡方检验/Chi-square', '拟合优度/Goodness', '独立性检验', '列联表检验', 'Fisher精确检验', '二项检验/Binomial', '泊松检验/Poisson', '相关性分析/Correlation', 'Pearson相关系数', '皮尔逊相关', 'Spearman等级相关', 'Kendall tau相关', '相关系数解释', '相关强度/Weak/Medium', '正相关/负相关', '强相关/弱相关', '相关不等于因果', '偏相关/Partial Corr', '复相关/Multiple Corr', '协方差/Covariance', '回归分析/Regression', '一元线性回归', '线性回归方程', '回归系数/Slope', '截距/Intercept', '残差/Residual', '最小二乘法/OLS', 'R²决定系数', '调整R²/Adj R²', 'SSR回归平方和', 'SSE残差平方和', 'SST总平方和', 'F检验/F-test', 't检验/系数显著性', '多重共线性/VIF', '异方差性/Heterosced', '自相关/Autocorr', '多元线性回归', '自变量/因变量', '回归诊断', '残差分析', '预测/Prediction', '点预测', '区间预测', 'Logistic回归', 'S曲线/逻辑斯蒂', '优势比/OR', '似然比/LR', '模型评估/AUC', '混淆矩阵/Precision', 'Recall/F1', 'ROC曲线', '岭回归/Ridge', 'Lasso回归', 'ElasticNet', '逐步回归/Stepwise', '主成分回归/PCR', '主成分分析/PCA', '方差分析/ANOVA', '单因素ANOVA', '双因素ANOVA', '多因素ANOVA', 'F统计量', '组间变异/组内变异', '事后比较/Post-hoc', 'Tukey HSD', 'Bonferroni校正', '时间序列分析', '趋势/Trend', '季节性/Seasonal', '周期性/Cyclical', '不规则/Irr', '移动平均/MA', '指数平滑/ES', 'Holt-Winters', 'AR自回归模型', 'MA滑动平均', 'ARMA/ARIMA', 'ACF/PACF', '白噪声/White Noise', '平稳性检验', 'ADF检验', '差分/Differencing', 'Seasonal ARIMA', '预测/Forecast', '点预测', '置信区间', '贝叶斯统计', '先验分布/后验', '贝叶斯估计', 'MCMC/马尔科夫', '贝叶斯回归', '贝叶斯因子', '统计软件/R/Python', 'SPSS操作', 'STATA分析', 'EViews时序']
                }
            }
        },
        '数据工程师': {
            'description': '搭建和维护数据管道，开发ETL流程，处理大规模数据。',
            'skills': {
                'Python': {
                    'desc': '数据管道开发和数据处理脚本',
                    'difficulty': 1,
                    'dimensions': ['Python基础/数据类型/list/dict/set/tuple/控制流/循环/函数/类/继承/多态', 'Python环境/Python3/Pip/Anaconda/venv', 'NumPy数值计算/np.array/矩阵运算/广播/索引切片', 'Pandas数据处理/DataFrame/Series/缺失值/合并/聚合', 'PyArrow处理/Parquet/Arrow格式', 'PySpark数据处理', 'pandas-datareader金融数据', 'requests网络请求/API调用', 'urllibHTTP库', '数据库连接/pymysql/SQLAlchemy', 'psycopg2/PostgreSQL', 'redis连接/redis-py', 'Elasticsearch连接/es-py', '数据读写/read_csv/to_csv', 'read_excel/to_excel', 'read_sql/to_sql', 'Parquet读写/pyarrow', 'JSON处理/json库', 'YAML解析/PyYAML', '正则表达式/re', 'os模块/文件目录', 'pathlib路径操作', 'glob文件匹配', '日志模块/logging', '日志配置/handlers/formatters', 'try-except异常处理', 'logging config', 'subprocess执行命令', 'multiprocessing多进程', 'threading多线程', 'concurrent.futures', 'asyncio异步编程', 'schedule定时任务', 'APScheduler调度', 'Celery分布式任务队列', 'Scala/Java交互/Py4J', 'PySpark RDD/DataFrame', 'pyspark.sql库', 'spark.read/write', '广播变量/Broadcast', '累加器/Accumulator', '自定义函数/UDF', 'Pandas UDF/Arrow', '窗口函数/Window Functions', '列式计算', 'ETL脚本开发', '数据清洗脚本', '数据校验脚本', '数据质量检查', '单元测试/unittest/pytest', 'Git版本控制', 'CI/CD集成', 'Airflow PythonOperator', '数据管道/Pipeline', 'DAG编写/Airflow']
                },
                'SQL': {
                    'desc': '数据仓库查询和优化',
                    'difficulty': 1,
                    'dimensions': ['SQL基础/SELECT/FROM/WHERE/ORDER BY', '聚合函数/SUM/AVG/COUNT/MAX/MIN', 'GROUP BY分组/HAVING筛选', 'JOIN连接/INNER/LEFT/RIGHT/FULL', '子查询/标量/列/表子查询', 'UNION合并查询', 'CASE WHEN条件', '窗口函数/OVER/PARTITION BY', 'ROW_NUMBER/RANK/DENSE_RANK', 'LAG/LEAD偏移窗口', 'SUM/AVG OVER累计', 'FIRST_VALUE/LAST_VALUE', 'WITH CTE公用表表达式', '递归CTE', '数据类型/INT/VARCHAR/DATE/TIMESTAMP', '类型转换/CAST/CONVERT', '字符串函数/CONCAT/SUBSTRING/LENGTH', '日期函数/DATE/NOW/DATEDIFF/YEAR/MONTH', 'NULL处理/IFNULL/COALESCE/NULLIF', 'Hive SQL/HQL', 'Spark SQL', 'Presto查询', 'Impala查询', 'ClickHouse SQL', 'Doris SQL', 'SELECT语法差异', '分区表/Partition Table', '分桶表/Bucket Table', '动态分区/Dynamic Partition', '静态分区/Static Partition', '表类型/Managed/External', '视图/View物化视图', '临时表/Temporary Table', 'WITH子句/CTE', 'Lateral View/UDTF', 'Explode/炸裂函数', 'Array/Struct/Map类型', 'Array函数/排序/去重', 'Map函数/key/value', 'JSON解析/get_json_object', 'JSON_TUPLE', 'Regexp_extract正则', '窗口分析函数', 'OVER子句完整语法', 'RANGE/ROWS帧', 'PRECEDING/FOLLOWING', 'UNBOUNDED无界', 'CURRENT ROW当前行', 'DISTRIBUTE BY分布', 'SORT BY排序', 'CLUSTER BY聚类', 'DISTRIBUTE BY + SORT BY', '执行计划/EXPLAIN', '执行计划分析', 'Map/Reduce Stage', 'Shuffle过程', '数据倾斜/Skew', 'Join优化策略', 'Broadcast Join广播', 'Shuffle Join', 'Sort Merge Join', 'Bucket Join/分桶', 'Join顺序优化', '谓词下推/PPD', '列裁剪/Column Pruning', '分区裁剪/Partition Pruning', '物化视图/Materialized View', '查询优化技巧', 'SQL优化规则', 'Hint提示/强制优化', '索引/Index/Bitmap', '数据仓库建模', '星型模型/Star Schema', '雪花模型/Snowflake', '宽表/Wide Table', '拉链表/Slowly Changing', '维度退化/Dim Degradation', '事实表/Fact Table', '累积快照表', '事务事实表', '周期快照表', '粒度/Granularity', '一致性维度/Conformed Dim', '一致性事实/Conformed Fact', '代理键/Surrogate Key', '自然键/Natural Key', '钻取/Drill Down/Up', '切片/Slice/切块/Dice', '旋转/Pivot']
                },
                'Scala': {
                    'desc': '大数据处理语言，Spark原生支持',
                    'difficulty': 1,
                    'dimensions': ['Scala基础/面向对象/函数式', 'Scala环境/sbt/IDEA', 'Scala REPL/解释器', '数据类型/Int/Long/Double/String', 'Unit/Any/AnyRef/Nothing', 'val常量/immutable', 'var变量/mutable', 'lazy延迟加载', '函数/def/=>匿名', '函数参数/默认参数', '命名参数', '可变参数/*', '高阶函数', '闭包/Closure', '柯里化/Currying', '偏函数/Partial', '部分应用/Partial Applied', '模式匹配/match', '样例类/case class', '模式守卫/guard', 'Option/Some/None', 'Either/Left/Right', 'Try/Success/Failure', '集合/Collections', 'List/ListBuffer', 'Set/Mutable Set', 'Map/Mutable Map', 'Seq/IndexedSeq', 'Vector向量', 'Range/序列', 'for循环/yield', '推导式/Comprehension', '集合操作/map/filter', 'flatMap展平', 'reduce聚合', 'fold折叠', 'groupBy分组', 'partition分割', 'collect收集', 'exists/forall', 'find查找', 'take/drop', 'takeWhile/dropWhile', 'zip拉链', 'unzip解拉链', 'view惰性视图', 'iterator迭代器', 'Stream流', 'LazyList惰性列表', 'Immutability不可变', 'Mutable可变集合', '并行集合/Par', 'Future异步', 'Promise承诺', 'Await等待', 'Try/TryWith', 'Akka Actor', 'Actor消息', 'Supervision监督', 'ActorSystem', 'Actor路径', 'Spark RDD编程', 'Spark DataFrame', 'Spark Dataset', 'Spark SQL', 'Spark Streaming', 'Structured Streaming', 'Spark MLlib', 'Spark GraphX', 'RDD transformations', 'RDD actions', 'map/flatMap/filter', 'reduceByKey/groupByKey', 'join/window', 'coalesce/repartition', 'cache/persist', 'checkpoint', '广播变量', '累加器', 'Scala互操作/Java', 'Java Scala转换', 'implicit隐式转换', 'implicit参数', 'Type class', '泛型/Generics', 'Upper/Lower Bound', 'View Bound', 'Context Bound', '协变逆变', 'Hadoop集成', 'HDFS操作', 'SBT构建/Maven', 'SBT依赖管理', 'SBT任务/sbt compile', 'SBT打包/sbt package', '打包Uber JAR', 'SparkSubmit', 'Spark集群部署', 'Spark配置调优']
                },
                'ETL': {
                    'desc': '数据抽取、转换、加载流程开发',
                    'difficulty': 2,
                    'dimensions': ['ETL概述/Extract/Transform/Load', '数据集成/Data Integration', 'ELT加载转换', '数据管道/Data Pipeline', '数据源/Source', '关系型/MySQL/Oracle', 'NoSQL/MongoDB', '文件源/CSV/JSON', '日志文件/Log', 'API数据源', '流式数据源/Kafka', '数据湖/Data Lake', '数据抽取/Extract', '全量抽取/Full Extract', '增量抽取/Incremental', 'CDC变更捕获', 'Debezium CDC', 'Canal CDC', 'Maxwell CDC', '时间戳增量/Timestamp', '日志增量/BinLog', 'CDC debezium', '数据同步工具/Sqoop', 'DataX同步', 'Kettle/PDI', 'Informatica', 'Talend ETL', 'Apache NiFi', 'StreamSets', 'Airbyte数据集成', '数据转换/Transform', '数据清洗/Cleaning', '空值处理', '异常值处理', '重复值处理', '数据类型转换', '日期格式转换', '编码转换/Encoding', '数据脱敏/Masking', '数据标准化', '数据规范化', '数据拆分/Split', '数据合并/Merge', '数据聚合/Aggregate', '数据关联/Join', '数据排序/Sort', '数据抽样/Sample', '字段映射/Mapping', '字段计算/Derived', '业务规则/Rules', '数据质量规则', 'SCD缓慢变化维', 'SCD Type1覆盖', 'SCD Type2新增', 'Type3混合', '数据加载/Load', '全量加载/Full Load', '增量加载/Incremental', '批量加载/Batch', '实时加载/Streaming', 'Upsert/Merge', 'Delete删除', 'Append追加', '覆盖/Overwrite', '分区加载/Partition', '目标端/Target', '数据仓库/Star Schema', 'Hive/HDFS', 'ClickHouse', 'Doris', 'Greenplum', 'Teradata', 'Vertica', '星型模型加载', '雪花模型加载', '维度表加载', '事实表加载', 'ETL调度/Airflow', '调度/Oozie', '调度/DolphinScheduler', '调度/Azkarra', '调度/Prefect', '任务依赖/DAG', '任务重试/Retry', '任务告警/Alert', 'ETL监控/Monitor', '数据监控', '任务监控', '血缘追踪/Lineage', '数据治理/Governance', '元数据管理/Meta', '数据质量/DQ', '数据标准/Standard', 'ETL日志/Logs', '错误处理/Error Handle', '异常日志', 'ETL性能/Tuning', '并行处理/Parallel', '分区处理', '压缩/Compression', '内存优化', 'ETL最佳实践', '规范化开发', '模块化设计', '配置化管理', '代码审查', '测试/Unit Test', 'ETL文档/Documentation']
                },
                'Flink': {
                    'desc': '实时流处理框架',
                    'difficulty': 2,
                    'dimensions': ['Flink概述/Apache Flink/流处理', 'Flink架构/JobManager', 'TaskManager架构', 'Slot管理', 'Flink部署/Standalone', 'Standalone Cluster', 'YARN Cluster', 'Kubernetes部署', 'Flink on K8s', 'Flink环境配置', 'DataStream API', 'DataStream编程', 'StreamExecutionEnvironment', 'DataStream Source', 'Socket数据源', 'File数据源', 'Kafka数据源', '自定义数据源/SourceFunction', 'ParallelSourceFunction', 'RichParallelSourceFunction', 'DataStream算子/Operator', 'map映射', 'filter过滤', 'flatMap扁平化', 'keyBy分组', 'reduce聚合', 'fold折叠', 'aggregate聚合', 'window窗口', 'windowAll', 'union合流', 'connect连接', 'coMap/coFlatMap', 'split分流/侧输出', '侧输出/Side Output', 'process函数', 'ProcessFunction', 'KeyedProcessFunction', '窗口/Window', 'TimeWindow滚动窗口', 'SlidingWindow滑动窗口', 'SessionWindow会话窗口', 'GlobalWindow全局窗口', 'CountWindow计数窗口', '窗口函数/WindowFunction', 'ReduceFunction', 'AggregateFunction', 'FoldFunction', 'ProcessWindowFunction', '触发器/Trigger', 'Evictor驱逐器', 'Watermark水印', 'Event Time事件时间', 'Processing Time处理时间', 'Ingestion Time摄入时间', 'Watermark策略', 'FixedWatermarkStrategy', 'PeriodicWatermark', 'PunctuatedWatermark', '乱序处理/Late Data', 'allowedLateness延迟', '侧输出迟到数据', '迟到数据处理', '状态管理/State', 'Keyed State键控状态', 'Operator State算子状态', 'Broadcast State广播状态', 'ListState列表状态', 'MapState映射状态', 'ValueState值状态', 'ReducingState聚合状态', 'AggregatingState', 'TTL状态过期', 'StateBackend状态后端', 'FsStateBackend', 'RocksDBStateBackend', 'Incremental Checkpoint', 'Checkpoint机制', 'Checkpoint配置', 'EXACTLY_ONCE语义', 'AT_LEAST_ONCE语义', 'Barrier对齐/Barrier Align', 'Barrier非对齐', 'Savepoint保存点', 'Stop暂停', '重启策略/Restart', 'FixedRestartStrategy', 'FailureRestartStrategy', 'ExponentialDelayRestart', 'Table API', 'TableEnvironment', 'Table转换', 'Table SQL', 'fromDataStream', 'toDataStream', 'Table SQL查询', '注册表/Register Table', '注册DataStream', 'SQL窗口/Over Window', 'GROUP TUMBLE滚动', 'GROUP HOP滑动', 'SESSION会话', 'SQL函数/UDF', 'UDAF聚合函数', 'UDTF表函数', 'Connector连接器', 'Kafka Connector', 'MySQL CDC', 'Postgres CDC', 'Elasticsearch Connector', 'HDFS Connector', 'JDBC Connector', 'Hive Connector', 'DataGen连接器', 'Print连接器', 'Flink CDC Connect', 'Debezium Format', 'CDC Debezium', 'Flink SQL CDC', '异步IO/AsyncIO', 'AsyncFunction', 'Hive Metastore', 'Hive Dialect', 'Flink ML机器学习', 'Flink CEP复杂事件', 'CEP模式/Match', 'CEP NFA', 'CEP状态机', '背压/Back Pressure', '监控/Monitoring', 'Flink Dashboard', 'Flink Metrics', 'REST API', 'Prometheus监控', 'Grafana可视化', '内存模型/Tuning', 'Flink配置优化', '并行度/Parallelism', 'Slot配置', 'Checkpoint间隔', '状态大小优化', '网络缓冲/Buffer', '背压处理']
                },
                'Hadoop': {
                    'desc': '大数据存储和处理生态系统，包括HDFS和MapReduce',
                    'difficulty': 2,
                    'dimensions': ['Hadoop概述/分布式系统', 'Hadoop生态/HDFS/MapReduce/YARN', 'Hadoop发行版/CDH/Cloudera', 'HDP/Hortonworks', 'Apache Hadoop', 'CDP/Data Platform', 'Hadoop架构', '主从架构/Master-Slave', 'HDFS分布式文件系统', 'NameNode名称节点', 'DataNode数据节点', 'Secondary NameNode', 'CheckpointNode', 'BackupNode', 'HDFS架构/Block', 'Block块/128MB/64MB', '副本机制/Replication', '副本放置策略/Rack', '机架感知/Rack Awareness', '数据均衡/Balancer', 'HDFS读写流程', '写数据/Write Pipeline', 'Pipeline写管道', '读数据/Read Data', '短路读取/Short Circuit', 'HDFS命令/hdfs dfs', 'hdfs dfs -put', 'hdfs dfs -get', 'hdfs dfs -ls', 'hdfs dfs -mkdir', 'hdfs dfs -rm', 'hdfs dfs -cat', 'hdfs dfs -chmod', 'hdfs dfs -chown', 'hdfs dfs -du', 'hdfs dfs -df', 'hdfs dfs -setrep', 'fsck检查文件系统', 'HDFS权限/Permission', '用户名权限', 'ACL访问控制', 'HDFS Federation', 'NameNode Federation', 'ViewFS视图', 'HDFS快照/Snapshot', '快照创建/Snapshot', '快照恢复', '快照限制', 'HDFS安全/Kerberos', 'Kerberos认证', 'Spnego认证', 'HDFS加密/Encryption', 'Zone加密', 'HDFSQuota配额', '存储配额/Space Quota', '文件配额/Name Quota', 'Trash垃圾箱', '回收站/Trash', ' Trash配置', 'MapReduce计算', 'MapReduce架构', 'JobTracker任务跟踪', 'TaskTracker任务槽', 'YARN架构', 'ResourceManager资源', 'NodeManager节点', 'ApplicationMaster', 'Container容器', 'YARN调度/FIFO', 'Capacity Scheduler', 'Fair Scheduler', '公平调度器', '队列/Queue', '队列配置', '资源分配', 'YARN命令/yarn', 'yarn application', 'yarn logs', 'yarn node', 'yarn queue', 'MapReduce编程', 'Mapper类', 'Reducer类', 'Driver主类', 'Job提交', 'InputFormat输入格式', 'TextInputFormat', 'KeyValueTextInputFormat', 'NLineInputFormat', 'DBInputFormat', 'SequenceFileInputFormat', 'OutputFormat输出格式', 'TextOutputFormat', 'SequenceFileOutput', 'DBOutputFormat', 'Combiner合并', 'Partitioner分区', 'Shuffle过程', 'Sort排序', 'Partition分区', 'GroupComparator分组', 'RecordReader记录', 'RecordWriter记录', 'Writable序列化', 'WritableComparable', '自定义数据类型', 'IntWritable/Text/Long', 'NullWritable', 'MapReduce优化', 'Combiner优化', 'Partitioner优化', '压缩/Codec', 'Snappy压缩', 'Lzo压缩', 'Gzip压缩', 'Map端优化', 'Reduce端优化', 'Shuffle优化', '小文件处理', 'CombineFileInputFormat', '小文件合并', 'HDFS小文件', 'MapReduce计数器', 'Counter计数器', '分布式缓存/DistributedCache', 'Job History日志', 'YARN JobHistory', 'MapReduce日志', '故障排查', '数据倾斜', '内存溢出/OOM', '推测执行/Speculative', '推测执行关闭', 'Hive on MapReduce', 'HBase数据库', 'HBase架构/Master', 'RegionServer', 'HBase表/RowKey', 'Column Family列族', 'HBase读写', 'ZooKeeper协调', 'Sqoop数据迁移', 'Flume日志收集', 'Oozie工作流', 'Hadoop HA高可用', 'NameNode HA', 'QJM/Quorum', 'ZKFC故障转移', 'YARN HA', '集群扩容/缩容', '节点管理', '滚动升级', 'Hadoop监控', 'Ganglia监控', 'Ambari管理', 'Cloudera Manager', 'Hadoop配置优化']
                },
                'Hive': {
                    'desc': '基于Hadoop的数据仓库工具',
                    'difficulty': 2,
                    'dimensions': ['Hive概述/数据仓库/Hadoop', 'Hive架构/驱动/编译器', 'Hive编译器/Optimizer', 'Hive执行器/Executor', 'Hive Metastore', 'Metastore数据库/MySQL', 'Derby嵌入式', 'HiveServer2/HS2', 'Beeline客户端', 'CLI命令行', 'Hive配置/hive-site.xml', 'Hive on MapReduce', 'Hive on Tez', 'Hive on Spark', 'Hive安装部署', 'CDH/HDP集成', 'Hive数据库/Database', 'CREATE DATABASE', 'SHOW DATABASES', 'USE database', 'DROP DATABASE', 'Hive表/Table', '内部表/Managed Table', '外部表/External Table', '临时表/Temporary', '分区表/Partitioned', '静态分区/Static Partition', '动态分区/Dynamic Partition', '分区表原理', '分桶表/Bucketed', 'CLUSTERED BY', 'SORT BY/ORDER BY', '分桶表采样', '表操作/DDL', 'CREATE TABLE', 'DESCRIBE', 'SHOW PARTITIONS', 'ALTER TABLE', 'DROP TABLE', 'TRUNCATE TABLE', 'RENAME重命名', 'ADD COLUMNS', 'REPLACE COLUMNS', 'CHANGE COLUMN', '表属性修改', 'SerDe序列化', 'LazySimpleSerDe', 'RegexSerDe', 'JSON SerDe', 'ORC SerDe', 'Parquet SerDe', 'AVRO SerDe', '数据加载/LOAD', 'LOAD DATA LOCAL', 'LOAD DATA HDFS', 'INSERT OVERWRITE', 'INSERT INTO', '直接查询创建/CTAS', 'CREATE TABLE AS SELECT', '数据导出/EXPORT', 'IMPORT导入', 'HQL查询/DQL', 'SELECT查询', 'WHERE条件', 'DISTINCT去重', 'ORDER BY排序', 'SORT BY局部排序', 'DISTRIBUTE BY分配', 'CLUSTER BY', 'LIMIT限制', '列选择/Column', '列别名/AS', '算术运算', '字符串函数', 'CONCAT/SUBSTR', 'LENGTH/LOWER/UPPER', 'TRIM/LTRIM/RTRIM', 'SPLIT/REGEXP_EXTRACT', 'JSON解析函数', 'NVL/COALESCE', 'IF条件/CASE', '日期函数/DATE', 'DATE_ADD/SUB', 'DATEDIFF', 'YEAR/MONTH/DAY', 'TO_DATE/CURRENT_DATE', '聚合函数/COUNT', 'SUM/AVG/MAX/MIN', 'GROUP BY分组', 'HAVING分组过滤', 'DISTINCT COUNT', 'COUNT(*) vs COUNT(1)', 'JOIN连接查询', 'INNER JOIN', 'LEFT/RIGHT OUTER', 'FULL OUTER', 'CROSS JOIN', 'LEFT SEMI JOIN', 'MAP JOIN/Broadcast', 'JOIN条件', '多表连接', '子查询/Subquery', '标量子查询', '表子查询', 'LATERAL VIEW', 'UDTF函数/炸裂', 'POSEXPLODE', 'STACK', '窗口函数/OVER', 'PARTITION BY分区', 'ORDER BY排序', 'RANGE/ROWS帧', 'PRECEDING/FOLLOWING', 'UNBOUNDED', 'CURRENT ROW', 'ROW_NUMBER', 'RANK/DENSE_RANK', 'LAG/LEAD偏移', 'FIRST_VALUE/LAST_VALUE', 'SUM_OVER累计', 'AVG_OVER移动平均', 'COUNT_OVER', '窗口框架/Frame', '聚合到窗口', 'WITH CTE公用表', 'UNION合并', 'UNION ALL', 'EXCEPT/MINUS', 'INTERSECT', 'CTE递归', 'Collection函数', 'ARRAY函数', 'MAP函数', 'STRUCT函数', '类型转换/CAST', '隐式转换', 'Hive优化/Hints', 'MAPJOIN广播', 'Bucket Map Join', 'SMB Join', '倾斜优化/SKEW', '并行执行/PARALLEL', '严格模式/Strict', '排序优化', '分区裁剪/PPD', '列裁剪', '合并小文件', '向量化/Vectorization', 'CBT/Tez优化', 'Fetch抓取优化', '执行引擎/Engine', 'Explain执行计划', 'Hive性能调优', 'JVM重用', '内存配置', 'Map端配置', 'Reduce端配置', 'Shuffle配置', '压缩配置', 'Hive安全/Kerberos', '授权/Grant/Revoke', '角色/Role', '行级授权/Column', '视图/View', '物化视图/Materialized', 'Hive函数/UDF', 'UDF用户自定义', 'UDAF聚合函数', 'UDTF表函数', '永久函数/Permanent', '临时函数/TEMPORARY', '注册函数/CREATE FUNCTION', 'Java UDF开发', 'Python UDF/UDAF', 'HiveServer2连接', 'JDBC连接', 'ODBC连接', 'Hive集成/BI工具', 'Hive Metastore服务', 'Metastore配置', 'HiveWarehouse', 'Hive on Spark配置', 'Spark on Hive', 'Hive事务/Transaction', 'ACID特性', 'BEGIN/COMMIT/ROLLBACK', '锁/Lock', '共享锁/排他锁']
                },
                'Kafka': {
                    'desc': '高吞吐量消息队列，数据采集和传输',
                    'difficulty': 2,
                    'dimensions': ['Kafka概述/消息队列/MQ', 'Kafka架构/分布式', 'Kafka核心概念', 'Topic主题/消息分类', 'Partition分区/并行', 'Replication副本/备份', 'Leader/Follower', 'ISR/In-Sync Replicas', 'AR/All Replicas', 'HW/High Watermark', 'LEO/Last End Offset', 'Producer生产者', 'Consumer消费者', 'Consumer Group消费组', 'Offset偏移量', 'Broker代理/服务器', 'ZooKeeper协调', 'KRaft协议/New', 'Kafka安装部署', '单节点安装', '集群安装', 'Docker安装', 'Kafka配置/server.properties', 'Broker配置', 'Topic配置', 'Producer配置', 'Consumer配置', 'Kafka命令行/kafka-topics', 'kafka-topics.sh创建', '--create创建', '--describe查看', '--list列表', '--alter修改', '--delete删除', '分区副本分配', '分区副本因子', 'Kafka生产者/Producer', 'Producer API', '发送方式/同步', '发送方式/异步', 'acks确认/0/1/all', 'retries重试', 'batch.size批次', 'linger.ms延迟', 'compression.type压缩', 'max.in.flight', '序列化/Serializer', 'key/value序列化', 'StringSerializer', 'JSONSerializer', 'AvroSerializer', 'Schema Registry', '自定义分区/Partitioner', '默认分区器/Default', '粘性分区/Sticky', '消息顺序保证', '幂等性/Idempotent', '事务/Transaction', ' Exactly Once语义', 'Kafka消费者/Consumer', 'Consumer API', '手动提交/auto.commit', '手动commitSync', '手动commitAsync', '提交偏移量', '消费者配置', 'bootstrap.servers', 'group.id组ID', 'auto.offset.reset', 'enable.auto.commit', 'max.poll.records', 'session.timeout.ms', 'heartbeat.interval', 'poll拉取数据', 'poll循环', 'Consumer Group', '组内分区分配', 'Range分配策略', 'RoundRobin分配', 'StickyAssignor', 'CooperativeSticky', 'Rebalance重平衡', 'GroupCoordinator', 'JoinGroup', 'SyncGroup', 'Heartbeat心跳', 'Rebalance触发', 'Rebalance避免', '消费者组位移', '__consumer_offsets', 'seek指定消费', 'seekToBeginning', 'seekToEnd', '多线程消费', '独立消费者', 'Kafka Connect', 'Source Connector', 'Sink Connector', 'JDBC Connector', 'ES Connector', 'HDFS Connector', 'S3 Connector', 'FilePulse Connector', 'MQTT Connector', 'Connect配置', 'REST API', 'Connector开发', 'SourceTask', 'SinkTask', 'Kafka Streams', 'Streams API', 'KStream/KTable', 'DSL编程', 'Processor API', '拓扑/Topology', '流/Stream', '表/Table', 'KTable视图', 'GlobalKTable', '状态存储/Store', '窗口/Window', '会话窗口', '滚动窗口', '滑动窗口', '时间窗口', '时间语义', 'Event Time', 'Processing Time', 'Watermark水印', '乱序处理', '容错/Fault Tolerance', 'exactly_once处理', 'Kafka监控/Monitoring', 'JMX监控', 'Prometheus集成', 'Grafana仪表板', 'Kafka Manager', 'Confluent Control', 'Kafka Eagle', 'Kafka性能优化', '吞吐量优化', '延迟优化', '磁盘IO优化', '网络优化', '内存优化', 'JVM优化', 'GC优化', '页缓存/Page Cache', '顺序写入', '零拷贝/Zero Copy', 'Kafka安全/Security', 'SASL/PLAIN', 'SASL/SCRAM', 'Kerberos', 'SSL/TLS加密', 'ACL授权', 'Kafka生态/kafka_', 'Kafka Connect', 'Kafka Streams', 'Kafka SQL/KSQL', 'Confluent Schema', 'Confluent REST', 'Kafka MirrorMaker', '跨集群复制', 'Kafka Streams应用', '实时流处理', '事件驱动架构', 'CDC同步/Debezium', 'Kafka数据集成', 'Flink集成Kafka', 'Spark Streaming', '集成Kafka Connect', 'Kafka可靠性', '副本同步', 'ISR机制', 'Leader选举', '控制器/Controller', 'Broker故障', '分区重分配', 'Preferred Leader', '手动分区平衡', 'Kafka Streams状态', '状态存储/RocksDB', '交互式查询', 'Kafka Streams配置']
                },
                'Spark': {
                    'desc': '大数据分布式计算框架，支持批处理和流处理',
                    'difficulty': 2,
                    'dimensions': ['Spark概述/大数据计算', 'Spark生态/批处理/流处理', 'Spark Core核心', 'Spark SQL', 'Spark Streaming', 'Structured Streaming', 'Spark MLlib', 'Spark GraphX', 'Spark架构/Driver', 'Executor执行器', 'Task任务', 'Stage阶段', 'DAG有向无环图', 'Shuffle过程', 'Spark部署/Standalone', 'Spark on YARN', 'Spark on Kubernetes', 'Spark on Mesos', 'Local模式', 'Cluster模式', 'Client模式', 'Spark Shell/pyspark', 'spark-shell', 'spark-sql', 'Spark Application', 'SparkSubmit提交', '--class主类', '--master集群', '--deploy-mode', '--num-executors', '--executor-cores', '--executor-memory', '--driver-memory', '--conf配置', 'RDD弹性数据集', 'RDD创建/from Parallelize', 'from textFile', '从集合创建', '从HDFS创建', '从Kafka创建', 'RDD操作/transform', 'map映射', 'flatMap扁平', 'filter过滤', 'distinct去重', 'union合并', 'intersection交集', 'subtract差集', 'cartesian笛卡尔', 'zip拉链', 'sample采样', 'take/count/collect', 'first/top/takeOrdered', 'reduce聚合', 'fold折叠', 'aggregate聚合', 'groupByKey', 'reduceByKey', 'sortByKey', 'keys/values', 'join连接', 'leftOuterJoin', 'cogroup分组连接', 'coalesce合并分区', 'repartition重分区', 'partitionBy', 'mapPartitions', 'mapPartitionsWithIndex', 'glom展开分区', 'cartesian笛卡尔积', 'pipe管道', 'checkpoint检查点', 'cache缓存/persist', 'StorageLevel存储', 'RDD lineage谱系', '依赖/窄依赖/宽依赖', 'Stage划分', 'Task执行', 'Spark SQL/DataFrame', 'SparkSession', 'read API读取', 'read.csv/json/parquet', 'read.jdbc', 'read.text', 'write API写入', 'write.csv/json/parquet', 'write.jdbc', 'write.saveAsTable', 'DataFrame操作', 'select选择', 'filter/where过滤', 'withColumn新增', 'withColumnRenamed', 'drop删除列', 'distinct去重', 'dropDuplicates', 'orderBy/sort排序', 'limit限制', 'sample抽样', 'describe统计', 'summary摘要', 'columns列名', 'dtypes类型', 'printSchema', 'show展示', 'take/head/collect', 'as重命名', 'cast类型转换', 'join连接', 'inner/left/right', 'semi/anti join', 'cross join', 'broadcast join', 'join hints', 'union合并', 'intersect交集', 'except差集', 'Window窗口函数', 'groupBy分组', 'agg聚合', 'pivot透视', 'crosstab交叉表', 'na.fill空值填充', 'na.drop空值删除', 'na.replace替换', 'na.handleNull', 'udf用户函数', 'pandas_udf向量化', 'spark udf注册', 'lit常量列', 'col/column列', 'expr表达式', 'array数组列', 'struct结构列', 'map映射列', 'split分解', 'explode炸裂', 'posexplode', 'from_json/to_json', 'to_timestamp', 'to_date日期', 'year/month/day', 'date_add/sub', 'datediff日期差', 'window时间窗口', 'date_trunc截断', 'trunc截断', 'Schema定义', 'StructType', 'StructField', 'DataType类型', 'Spark SQL优化', 'Catalyst优化器', ' Tungsten优化', 'WholeStageCodegen', '列式存储/Columnar', 'BroadcastHashJoin', 'SortMergeJoin', 'ShuffleHashJoin', 'Predicate Pushdown', 'Column Pruning', 'Constant Folding', 'Null Propagation', '代码生成/codegen', 'Spark Streaming', 'StreamingContext', 'DStream编程', 'socketTextStream', 'textFileStream', 'rawSocketStream', 'KafkaStream', 'transformation', 'DStream转换', 'updateStateByKey', 'mapWithState', 'transform转换', 'window窗口', 'countByWindow', 'reduceByWindow', 'countByValueAndWindow', 'foreachRDD', 'output operation', 'print/saveAsText', 'saveAsHadoopFiles', 'foreachBatch', 'checkpoint检查点', 'Driver HA', 'Back Pressure', 'Structured Streaming', 'spark.readStream', 'readStream.format', 'writeStream', 'write.format', 'outputMode/append', 'outputMode/complete', 'outputMode/update', 'trigger触发器', 'trigger.continuous', 'micro-batch', 'Watermark延迟', 'dropDuplicatesWithinWatermark', 'join with watermark', 'StateStore状态', 'StreamingQuery', 'query.start()', 'query.awaitTermination()', 'query.stop()', 'Spark ML/MLlib', 'Spark ML Pipeline', 'VectorAssembler', 'StringIndexer', 'OneHotEncoder', 'StandardScaler', 'MinMaxScaler', 'Imputer填充', 'ChiSqSelector', 'PCA主成分', 'ALS推荐', 'LDA主题', 'DecisionTree', 'RandomForest', 'GBDT/G梯度提升', 'LogisticRegression', 'LinearRegression', 'SVM支持向量', 'KMeans聚类', 'GaussianMixture', 'SVD奇异值', 'ALS协同过滤', 'FPGrowth频繁项', 'PrefixSpan序列', 'FeatureHasher', 'RFormula', 'CrossValidator', 'TrainValidationSplit', 'Hyperparam Tuning', 'Evaluator评估', 'BinaryClassification', 'MulticlassClassification', 'Regression', 'Clustering聚类', 'RecommenderSystem', 'Pipeline模型', 'model.save/load', 'Spark GraphX', 'Graph图', 'VertexRDD', 'EdgeRDD', 'Graph构建', 'Graph operators', 'PageRank算法', 'TriangleCount', 'ConnectedComponents', 'StronglyConnected', 'Aggregation Messages', 'Pregel API', 'GraphX优化']
                },
                '数据仓库': {
                    'desc': '维度建模、事实表设计、星型/雪花模型',
                    'difficulty': 2,
                    'dimensions': ['数据仓库概述/DW/Data Warehouse', '数据仓库特征/Subject', '面向主题/Subject-Oriented', '集成性/Integrated', '相对稳定性/Nonvolatile', '随时间变化/Time-Variant', 'OLAP联机分析', 'OLTP联机事务', 'OLAP vs OLTP', '数据集市/Data Mart', '企业级数据仓库/EDW', 'ODS操作数据存储', '贴源层/Operational', '明细层/DWD', '汇总层/DWS', '应用层/ADS', '数据域/Data Domain', '业务过程/Business Process', '总线架构/Bus Architecture', '一致性维度/Conformed Dim', '一致性事实/Conformed Fact', 'Kimball维度建模', 'Inmon规范化建模', 'Bill Inmon', 'Ralph Kimball', '星型模型/Star Schema', '星型结构/中心事实表', '维度表/Dimension Table', '事实表/Fact Table', '维度建模步骤', '业务需求分析', '选择业务过程', '声明粒度', '确认维度', '确认事实', '雪花模型/Snowflake', '规范化维度', '范式/3NF', '第三范式', '星型vs雪花', '星座模型/Galaxy', '多事实表共享', '维度表设计', '维度属性/Attribute', '代理键/Surrogate Key', '自然键/Natural Key', '业务键/Business Key', '缓慢变化维/SCD', 'SCD Type1覆盖', 'SCD Type2新增', 'Type3混合', 'Type4独立表', 'Type6混合', '拉链表/Slowly Changing', '历史拉链', '全量快照', 'Type2拉链', '维度类型/Type1/Type2', '退化维度/DD/Degenerate', '杂项维度/Junk Dim', '日期维度/Date', '时间维度/Time', '角色扮演维度', '可退款维度', '审计维度/Audit', '影子维度/Shodow', '维度表设计原则', '扁平维度/Flat', '一致性维度', '维度层次/Hierarchy', '位置维度/Role-Playing', '多值维度/Multi-Valued', '事实表设计', '事务事实表', '周期快照表', '累积快照表', '累计快照表', '半累加事实/Semi-additive', '非累加事实/Non-additive', '事实表粒度/Granularity', '原子事实/Atomic Fact', '聚合事实/Aggregate', '合并事实/Consolidated', '一致性事实', '事实类型/Fact Type', '事务事实/Transaction', '周期快照/Periodic', '累计快照/Accumulating', '比例事实/Ratio', '指标/Measure', '可加指标/Fully-additive', '半可加指标', '不可加指标', '度量值计算', 'SUM/COUNT', 'AVG/平均值', 'MIN/MAX', '事实表设计原则', '维度设计原则', '主键设计', '外键设计', '数据分层/DWD/DWS/ADS', 'DWD明细层', 'DWS汇总层', 'DWT宽表层', 'ADS应用层', 'Common DIM公共维度', '维度建模工具', 'ERWin', 'PowerDesigner', 'Navicat', 'DataX/建模', 'Apache Atlas', 'Hive建模', 'ClickHouse建模', 'Doris建模', '星型模型实现', '雪花模型实现', '数仓分层设计', '数据域划分', '主题域划分', '数仓主题', '交易主题', '会员主题', '营销主题', '商品主题', '库存主题', '财务主题', '供应链主题', '实时数仓/Real-time', 'Lambda架构', 'Kappa架构', 'Flink+ClickHouse', 'Flink+Doris', '湖仓一体/Lakehouse', 'Delta Lake', 'Apache Iceberg', 'Hudi数据湖', 'StarRocks', '物化视图/MV', '数据治理/Data Governance', '元数据管理', '数据血缘/Lineage', '数据质量/DQ', '指标体系/Metric', 'OneData体系', '维度设计工具', '建模规范', '命名规范', '分层规范', '开发规范']
                },
                '数据治理': {
                    'desc': '数据质量、元数据管理、数据血缘',
                    'difficulty': 2,
                    'dimensions': ['数据治理概述/Data Governance', '数据治理框架/Framework', '数据治理成熟度', 'DAMA数据管理', 'DMBOK数据知识', '数据治理组织', '数据治理委员会', '数据Owner', '数据管理员/Data Steward', '数据质量管理/DQ', '数据质量维度', '完整性/Completeness', '准确性/Accuracy', '一致性/Consistency', '及时性/Timeliness', '唯一性/Uniqueness', '有效性/Validity', '数据质量评估', '数据质量检测', '数据质量规则', '空值检测', '唯一性检测', '规范性检测', '一致性检测', '准确性检测', '及时性检测', '重复数据检测', '跨系统一致性', '数据质量指标', '数据质量评分', '数据质量报告', '数据质量监控', '数据质量改进', '元数据管理/Meta', '元数据定义', '技术元数据/Technical', '业务元数据/Business', '操作元数据/Operational', '管理元数据/Administrative', '元数据采集', '元数据存储', '元数据交换', '元数据标准', '元数据模型', '元数据架构', '元数据服务/API', '元数据目录/Catalog', '元数据门户', 'Apache Atlas', 'DataHub', 'Datahub架构', 'Atlas类型/Type', 'Atlas实体/Entity', 'Atlas分类/Taxonomy', 'Atlas血缘/Lineage', 'Atlas搜索', 'Atlas集成/Hive', 'Atlas集成/Spark', 'Atlas集成/Kafka', 'Atlas集成/Flink', '数据血缘/Lineage', '字段级血缘', '表级血缘', 'ETL血缘', 'SQL血缘', '系统血缘', '业务血缘', '血缘采集', '血缘存储', '血缘展示', '血缘追溯', '数据血缘图谱', '数据流向追踪', '影响分析/Impact', '根本原因分析', '数据血缘工具', '数据标准/Standard', '数据标准定义', '数据编码标准', '数据命名规范', '数据格式标准', '数据质量标准', '数据交换标准', '数据安全标准', '标准落地', '标准管理', '主数据管理/MDM', '主数据/Master Data', '交易数据/Transactional', '参考数据/Reference', '主数据识别', '主数据建模', '主数据治理', '主数据集成', '客户主数据/Customer', '产品主数据/Product', '供应商主数据', '员工主数据', '主数据平台/MDM', 'ReferenceData参考', '数据安全/Security', '数据分类/Classification', '敏感数据/Sensitive', '数据脱敏/Masking', '数据加密/Encryption', '数据权限/Authorization', '数据访问控制', '行级安全/RLS', '列级安全/CLS', '数据脱敏规则', '静态脱敏/Static', '动态脱敏/Dynamic', '数据水印/Watermark', '数据血缘安全', '数据合规/GDPR/个保法', '数据跨境', '数据生命周期', '数据采集治理', '数据传输治理', '数据存储治理', '数据处理治理', '数据共享治理', '数据销毁治理', '数据资产/Asset', '数据资产目录', '数据资产评估', '数据资产定价', '数据资产变现', '数据资产管理', '数据资产盘点', '数据资产地图', '数据资产报告', '数据资产运营', '数据资产价值', '数据架构/Architecture', '数据模型管理', '概念模型/Conceptual', '逻辑模型/Logical', '物理模型/Physical', '模型版本管理', '模型变更管理', '数据建模规范', '数据集成/Integration', 'ETL开发规范', '数据同步规范', '数据接口规范', '数据交换规范', 'API管理', '服务治理', '数据平台治理', '数据湖治理', '数据仓库治理', '数据质量流程', '数据质量改进', '数据质量文化', '数据治理工具', ' Informatica', 'Talend', 'DataStage', 'Collibra', 'Alation', 'Immuta', 'Privacera', '数据治理平台', '数据治理报告', '数据治理评估', '数据治理成熟度', '数据治理KPI']
                },
                '数据湖': {
                    'desc': '存储原始格式的大规模数据',
                    'difficulty': 2,
                    'dimensions': ['数据湖概述/Data Lake', '数据湖概念/原始数据', '数据湖vs数据仓库', 'ELT/Lakehouse架构', '数据湖设计原则', '原始性原则/Raw', '模式进化/Schema', 'Schema-on-Read', 'Schema-on-Write', '数据湖存储/Storage', 'HDFS存储', '对象存储/S3', '阿里云OSS', 'AWS S3', 'Azure Blob', 'Google GCS', 'MinIO存储', '本地对象存储', '分布式存储', '存储格式/Format', 'Parquet格式', 'Parquet列式存储', 'Parquet压缩', 'Parquet编码', 'Parquet分区', 'ORC格式', 'ORC ACID', 'ORC ZSTD', 'AVRO格式', 'AVRO Schema', 'AVRO序列化', 'JSON格式', 'CSV格式', 'Sequence格式', 'RCFile格式', 'Delta Lake数据湖', 'Delta Lake概述', 'Delta Lake特性', 'ACID事务/ACID', '事务支持', 'Upsert/Merge', 'Delete删除', 'Update更新', 'Time Travel时间旅行', '版本回溯', 'VACUUM清理', 'Optimize优化', 'Z-Ordering优化', 'Change Data Feed', 'CDF变更流', 'Delta Lake API', 'Delta Lake Python', 'Delta Lake Scala', 'Spark Delta', 'Delta Lake配置', 'Delta Lake优化', 'Apache Iceberg', 'Iceberg概述', 'Iceberg特性', 'Iceberg表格式', '表元数据/Metadata', 'Manifest清单', 'Snapshot快照', 'ACID表', '隐藏分区/Hidden', '分区演进/Partition', 'Schema演进', '时间旅行/Snapshot', '表回溯', 'Rollback回滚', '分支/Branch', '标签/Tag', 'Iceberg格式', 'Iceberg Parquet', 'Iceberg ORC', 'Iceberg Avro', 'Iceberg API', 'REST Catalog', 'Hive Catalog', 'Glue Catalog', 'JVM Iceberg', 'Python Iceberg', 'Apache Hudi', 'Hudi概述', 'Hudi表类型/Copy', 'Copy-on-Write/COW', 'Merge-on-Read/MOR', 'Hudi增量处理', 'Upsert写入', 'Bootstrap引导', 'Hudi查询/Query', 'Hudi Timeline', 'Hudi索引/Index', 'Bloom Index', 'Hudi优化', 'Hudi API', '数据湖建设/Building', '数据湖架构设计', '数据湖分层', 'Bronze层/原始', 'Silver层/清洗', 'Gold层/聚合', '数据目录/Catalog', 'Hive Metastore', 'AWS Glue', 'DataHub', 'Apache Atlas', 'LakeFormation', '数据治理/Governance', '数据质量/Quality', '数据安全/Security', '元数据管理/Meta', '数据血缘/Lineage', '数据访问/Access', '权限控制', '行级访问/RLS', '列级访问/CLS', '数据脱敏/Masking', '数据加密/Encryption', '数据湖查询/Query', 'Presto查询', 'Trino查询', 'Spark SQL', 'Hive查询', 'Impala查询', 'Dremio查询', 'Athena查询', 'Flink查询', '数据湖ETL', 'Spark ETL', 'Flink ETL', 'Airflow调度', 'dbt数据转换', 'Spark写入', 'Flink写入', '流式写入/Streaming', '批量写入/Batch', 'Upsert写入', 'CDC写入', '数据湖性能', '分区设计', '文件大小', '小文件问题', 'Compaction合并', '自动优化', 'Z-Ordering', '数据布局', '缓存/Cache', '数据湖最佳实践', 'Lakehouse湖仓一体', 'Databricks Lakehouse', 'StarRocks湖仓', 'Doris湖仓', 'Apache Doris', 'ClickHouse湖仓', 'Trino/Presto', 'Alluxio加速', '数据湖监控', '存储监控', '查询监控', '配额管理/Quota', '成本优化']
                },
                '调度系统': {
                    'desc': 'Airflow、DolphinScheduler等任务调度',
                    'difficulty': 2,
                    'dimensions': ['调度系统概述/Scheduler', '工作流引擎/Workflow', '任务编排/Orchestration', 'DAG/有向无环图', 'Airflow概述', 'Airflow架构/WebServer', 'Scheduler调度器', 'Executor执行器', 'Metadata DB', 'Redis消息队列', 'Celery执行器', 'LocalExecutor本地', 'CeleryExecutor分布式', 'KubernetesExecutor', 'SequentialExecutor', 'Airflow安装/yum/apt', 'pip安装/Airflow', 'Docker安装', 'Docker-Compose', 'Airflow初始化', 'airflow db init', 'airflow webserver', 'airflow scheduler', 'Airflow配置/airflow.cfg', 'executor配置', 'database配置', 'fernet_key', 'Airflow Web UI', 'DAGs列表', '树状视图/Tree', 'Graph视图/Graph', 'Calendar日历', 'Gantt甘特图', 'Landing Times', 'Task Duration', 'DAG编写/Python', 'DAG定义/from_airflow', 'dag_id唯一ID', 'default_args', 'description描述', 'schedule_interval', '@daily/@hourly', 'cron表达式', 'timedelta', '任务/Task', 'Operator操作符', 'BashOperator', 'PythonOperator', 'DummyOperator', 'EmailOperator', 'HttpOperator', 'SqlOperator', 'MySqlOperator', 'HiveOperator', 'S3FileTransform', 'DockerOperator', 'KubernetesPodOperator', 'SageMaker', 'DataXOperator', 'SparkSubmitOperator', 'BranchPython', 'ShortCircuitOperator', '任务依赖/Bitwise', '>>右移/依赖', '<<左移/设置', 'set_upstream', 'set_downstream', 'cross_downstream', '任务触发/Trigger', 'trigger_rule规则', 'all_success/全部成功', 'all_failed/全部失败', 'one_success/一个成功', 'one_failed/一个失败', 'none_failed/无失败', 'none_skipped', 'always总是', 'XCom任务通信', 'xcom_push/xcom_pull', 'Variables变量', 'Connection连接', 'Airflow连接', 'Hook钩子', 'HookBase', 'MySqlHook', 'HiveHook', 'S3Hook', 'HttpHook', '自定义Hook', 'SubDAG子DAG', 'SubDagOperator', 'TaskGroup任务组', '任务组/TaskGroup', 'edge权重/Edge Labeling', '优先级/Priority', 'weight_rule权重', 'pool资源池', 'Slots槽位', 'concurrency并发', 'max_active_tasks', 'dag_concurrency', '任务重试/Retry', 'retry_delay重试', 'retry_exponential', 'max_retry_delay', 'depends_on_past', 'wait_for_downstream', ' sla超时/SLA', 'sla_miss_callback', 'on_failure_callback', 'on_success_callback', 'on_retry_callback', '任务超时/timeout', 'execution_timeout', 'trigger_dag_id', 'unpause/pause', 'dag_bag', 'Airflow CLI', 'airflow dags list', 'airflow tasks list', 'airflow dags backfill', 'airflow dags trigger', 'airflow tasks test', 'airflow connections', 'airflow variables', 'Airflow API', 'REST API', 'Experimental API', 'Airflow Providers', 'Providers安装', 'Kubernetes Provider', 'Amazon Provider', 'Google Provider', 'Databricks Provider', 'Providers贡献', 'DolphinScheduler概述', '海豚调度/Dolphin', 'DS架构/Master/Worker', 'API Server', 'Alert Server', 'Registry注册', 'MySQL数据库', 'DolphinScheduler安装', 'DolphinScheduler部署', 'DS UI界面', '项目管理/Project', '资源中心/Resource', '数据源中心', '安全中心', '租户管理', '用户管理', '告警管理', 'DolphinScheduler任务', 'Shell任务', 'SQL任务', 'Procedure任务', 'Python任务', 'Spark任务', 'Flink任务', 'MapReduce任务', 'HTTP任务', 'DataX任务', '条件分支/Conditional', '子Workflow子流程', '依赖检查', 'DolphinScheduler DAG', '任务定义', '任务类型', '任务参数', '全局参数', '本地参数', '上游参数', '跨dag传参', '定时任务/Cron', '依赖关系', '任务优先级', '失败重试', '超时配置', '告警通知', '钉钉告警', '邮件告警', '飞书告警', '微信告警', 'Slack告警', '工作流监控', '任务监控', '调度日志', '调度优化', 'Azkaban概述', 'Azkaban Web', 'Azkaban Executor', 'Azkaban任务/flow', 'job任务定义', 'dependencies依赖', 'Xmland Properties', 'Oozie概述', 'Oozie工作流', 'Oozie Coordinator', 'Oozie Bundle', 'workflow.xml', 'coordinator.xml', 'bundle.xml', 'action节点', 'control节点', 'start/end/kill', 'fork/join', 'decision', 'Oozie EL函数', 'Prefect概述', 'Prefect Orion', 'Prefect Flow', 'Prefect Task', 'Prefect Deployment', 'Prefect Cloud', 'Prefect Server', 'Dask调度', 'Luigi概述', 'Luigi Task', 'Luigi Target', 'Luigi Parameter', '任务调度选择', '调度系统对比', 'Airflow vs DS', '调度系统选型']
                },
                '大数据技术': {
                    'desc': '分布式系统和大数据架构设计',
                    'difficulty': 3,
                    'dimensions': ['大数据概述/Big Data', '大数据特征/Volume', 'Volume海量', 'Velocity速度', 'Variety多样', 'Value价值', 'Veracity真实', '大数据技术栈', '数据采集层/Collection', '数据存储层/Storage', '数据计算层/Compute', '数据服务层/Service', '数据应用层/Application', '数据采集/Flume', 'Flume架构/Agent', 'Source源', 'Channel通道', 'Sink汇', 'Flume拦截器', 'Flume选择器', 'Flume配置', 'Kafka采集', 'Logstash采集', 'FileBeat采集', 'DataX采集', 'Sync工具采集', 'Sqoop采集', 'Streaming采集', 'CDC采集', 'BinLog采集', 'MaxWell采集', 'Debezium采集', 'Canal采集', '数据存储/HDFS', 'HDFS架构', 'NameNode', 'DataNode', 'Block块', '副本机制', '存储格式/Parquet', 'ORC/Avro/JSON', '列式存储', '压缩/Snappy', 'Gzip/LZO/ZSTD', '数据仓库/Hive', 'Hive表设计', '分区表', '分桶表', '外部表', '数据治理', 'Spark计算', 'Spark Core', 'RDD/DataFrame', 'Spark SQL', 'Spark ML', 'Flink计算', 'Flink DataStream', 'Flink Table', 'Flink SQL', 'CEP复杂事件', '批流一体', '实时计算/Streaming', '流处理框架', 'Storm实时', 'Trident实时', 'Spark Streaming', 'Structured Streaming', 'Flink流处理', '实时ETL', '实时统计', '实时告警', '消息队列/Kafka', 'Kafka架构', 'Topic分区', 'Producer/Consumer', 'Consumer Group', 'Offset', 'Kafka Connect', 'Schema Registry', 'RocketMQ消息', 'RabbitMQ消息', 'Pulsar消息', '数据服务/Service', 'API网关', 'RESTful API', 'GraphQL API', '数据接口', '数据订阅', 'OLAP查询/Presto', 'Presto查询', 'Trino查询', 'Impala查询', 'Kylin多维', 'Druid实时', 'Doris分析', 'ClickHouse分析', 'StarRocks分析', 'MPP架构', '列式存储', '向量化执行', '预聚合', '数据应用/Application', 'BI报表', '数据分析', '数据挖掘', '机器学习', '实时大屏', '推荐系统', '用户画像', '数据资产管理', '元数据', '数据血缘', '数据质量', '数据安全', '数据标准', '主数据', '大数据架构/Architecture', 'Lambda架构', '批处理层/Batch', '速度层/Speed', '服务层/Serving', 'Kappa架构', '流批一体', '湖仓一体/Lakehouse', '实时湖仓', '离线湖仓', '大数据平台/Platform', 'Hadoop集群', 'Spark集群', 'Flink集群', 'Kafka集群', 'ClickHouse集群', '运维管理/Operation', '集群监控', '资源管理', '容量规划', '故障处理', '扩容缩容', '升级迁移', '多租户管理', '资源隔离', '配额管理', '大数据安全/Security', 'Kerberos认证', 'ACL授权', '数据加密', '数据脱敏', '列级权限', '行级权限', ' Ranger权限', 'Sentry权限', '数据湖安全', 'Hadoop HA', 'NameNode HA', 'YARN HA', 'ResourceManager HA', 'Zookeeper HA', 'Kafka HA', '多副本', '故障转移', '容灾备份', 'DR站', '备份恢复', '数据恢复', '单元化架构', '异地多活', '冷备/温备/热备', '性能优化/Tuning', 'Spark调优', 'Flink调优', 'Kafka调优', 'HDFS调优', 'Hive调优', 'SQL优化', 'JVM调优', 'GC优化', '内存优化', '网络优化', 'CPU优化', '磁盘IO优化', 'Shuffle优化', '数据倾斜处理', '小文件处理', '存储优化', '计算优化', '架构选型/Selection', '技术选型', '开源vs商业', '自建vs云服务', '成本评估', '性能评估', '稳定性评估', '生态评估', '团队能力', '发展趋势/Trend', '湖仓一体', '流批一体', 'Serverless', '云原生大数据', '多云大数据', '实时数据湖', 'DataOps', 'AIOps大数据']
                }
            }
        },
        'BI工程师': {
            'description': '开发商业智能报表和仪表板，为业务决策提供数据支持。',
            'skills': {
                'SQL': {'desc': '数据查询和报表数据源配置', 'difficulty': 1, 'dimensions': ['SQL基础/SELECT/FROM/WHERE/ORDER BY/LIMIT', '聚合函数/SUM/AVG/COUNT/MAX/MIN', 'GROUP BY分组/HAVING筛选', 'JOIN连接/INNER/LEFT/RIGHT/FULL/CROSS', '子查询/标量/列/表子查询', 'UNION合并查询', 'CASE WHEN条件分支', '窗口函数/OVER/PARTITION BY/ROW_NUMBER', 'LAG/LEAD偏移/FIRST_VALUE/LAST_VALUE', '日期函数/DATE/NOW/YEAR/MONTH/DATEDIFF', '字符串函数/CONCAT/SUBSTRING/LENGTH/REPLACE', 'NULL处理/IFNULL/COALESCE/NVL', 'WITH CTE公用表表达式', '数据类型转换/CAST/CONVERT', 'Hive SQL/Spark SQL差异', 'ClickHouse SQL', 'Doris SQL', '执行计划/EXPLAIN分析', 'SQL优化/索引使用', 'JOIN优化策略', '分区裁剪/谓词下推', '数据仓库查询']},
                'ETL': {'desc': '简单的数据抽取和转换', 'difficulty': 2, 'dimensions': ['ETL概述/Extract/Transform/Load', '数据抽取/全量/增量/CDC', '时间戳增量/Timestamp', 'BinLog增量', '数据清洗/空值/异常/重复', '数据类型转换', '日期格式转换', '数据脱敏/Masking', '数据合并/Join/Merge', '数据聚合/SUM/COUNT', 'ETL工具/DataX/Sqoop', 'Kettle/PDI工具', 'Airbyte数据集成', '数据加载/INSERT/OVERWRITE', '分区加载/Partition', '目标端/Hive/MySQL', 'ETL调度/Airflow/DolphinScheduler', '任务依赖/DAG', '错误处理/重试', 'ETL日志/监控', 'ETL最佳实践']},
                'FineReport': {
                    'desc': '国产报表开发工具',
                    'difficulty': 2,
                    'dimensions': ['FineReport概述/帆软报表/FR', 'FineReport安装/设计器', 'FineReport服务器/Web', 'FineReport管理平台', '数据连接/数据源', '内置数据集', '数据库查询', '模板/模板设计', '单元格绑定', '列/行/扩展', '父子格/Parent', '关联数据集', '报表类型/简单报表', '复杂报表/主子报表', '汇总报表', '分组报表', '交叉报表', '多源报表', '行式报表', '分页报表', '折叠报表', '树形报表', '报表参数/Parameter', '下拉数据集', '下拉复选框', '日期参数', '多选参数', '参数联动', '参数传递', '条件属性', '显示规则', '颜色规则', '数据过滤/Filter', '行内过滤', '行后过滤', '数据集过滤', '公式/FORMULA', '算术运算符', '日期公式/DATE/TODAY', '逻辑公式/IF/AND/OR', '汇总公式/SUM/AVG/COUNT', '条件汇总/SUMIF/COUNTIF', '跨Sheet取数', '跨报表取数', 'Reportlets/模块化', '图表绑定', '柱形图/条形图', '折线图/面积图', '饼图/环形图', '散点图/气泡图', '地图/地图报表', '组合图/双Y轴', '甘特图', '雷达图', '词云图', '漏斗图', '图表交互', '决策报表/大屏', '决策报表布局', '组件/DashComp', 'Tab块/Tab组件', '参数面板', '地图组件', 'Flash打印', 'PDF导出', 'Excel导出', 'Word导出', '图片导出', '分页预览', '数据分析/Report', '填报预览/Write', '填报属性', '单元格类型', '文本/数字', '下拉框/复选框', '日期控件', '文本域', '插入图片', '自动补全', '填报提交', '数据校验', '提交模板', '事件/事件配置', '加载事件', '点击事件', '单元格编辑事件', 'JS按钮', '服务端事件', 'FineReport函数', 'REPORT函数', 'JasperReports', 'FineBI联动', 'FineBI决策', '权限管理/管理平台', '目录管理', '权限配置', '角色权限', '用户管理', '定时调度/Schedule', '任务管理', '邮件发送', '模板推送', '集群/Cluster', '集群部署', '负载均衡', '配置优化', '性能优化', '日志分析']
                },
                'Power BI': {'desc': '微软商业智能分析工具', 'difficulty': 2, 'dimensions': ['Power BI概述/PBI桌面/Web/Pro/Premium', 'Power BI Desktop安装', '数据获取/Get Data', 'Excel/CSV/SQL数据库', 'Web数据/SharePoint', 'Power Query编辑器', 'M语言基础', '数据类型/类型转换', '列操作/重命名/删除', '合并查询/Merge', '追加查询/Append', '分组依据', '自定义列', '参数/Parameters', '数据模型/关系视图', '维度表/事实表', '星型模型', '关系/基数/方向', 'DAX语言/Data Analysis', '度量值/Measure', '计算列', 'DAX基础/语法', 'CALCULATE/SUMX', 'FILTER/ALL函数', '时间智能函数', 'TOTALYTD/环比/同比', '表和关系/Dim/Fact', '可视化/图表', '柱状图/折线图/饼图', '散点图/地图', '矩阵/表/卡片', '仪表盘/Dashboard', '筛选器/Slicer', '角色权限/RLS', '行级安全', '发布/分享', 'Power BI Service', '工作区/发布', 'App应用', 'Gateway网关', '数据刷新/Schedule', 'DAX Studio', '最佳实践']},
                'Tableau': {'desc': '数据可视化和仪表板开发工具', 'difficulty': 2, 'dimensions': ['Tableau概述/Desktop/Public', 'Tableau Server/Online', '数据连接/连接器', 'Live/Extract抽取', '数据源/多个源', '工作表/Sheet', '维度和度量', '标记卡/Marks', '图表类型/柱状图', '折线图/面积图', '饼图/环形图', '散点图/气泡图', '地图/填充地图', '箱线图/直方图', '甘特图/帕累托', 'LOD表达式/FIXED', 'INCLUDE/EXCLUDE', '表计算/Quick Table', '累计/SUM/AVG', '排名/RANK', '同期/TOTALYTD', '筛选器/Filter', '上下文筛选', '参数/Parameter', '计算字段', 'IF/CASE函数', '分组/Group', '集/Set', '分层结构/Hierarchy', '仪表板/Dashboard', '布局/平铺浮动', '筛选器操作', '高亮操作', 'URL动作', '设备设计', '故事/Story', '发布/Publish', 'Tableau Server', '用户权限', '订阅/Alert', '最佳实践']},
                '报表开发': {
                    'desc': '企业级报表和KPI仪表板制作',
                    'difficulty': 2,
                    'dimensions': ['报表开发概述/Report Development', '报表类型/管理报表', '业务报表/运营报表', '财务报表/数据报表', 'KPI仪表板/KPI Dashboard', '周期性报表/日报', '周报/月报/季报', '报表需求分析', '报表设计/Design', '报表模板/Template', '报表开发流程', '需求调研/确认', '数据准备/ETL', '报表制作/开发', '报表审核/Review', '报表发布/Publish', '报表分发/推送', '报表迭代优化', '数据来源/Source', '数据仓库/DW', 'ODS/DWD/DWS/ADS', '主题域/业务域', '数据模型/星型', '雪花模型', '维度表/Dim', '事实表/Fact', '指标定义/Metric', '指标口径/计算规则', '数据SQL查询', 'Hive SQL', 'Spark SQL', 'Presto查询', 'ClickHouse', 'Doris查询', 'FineReport报表', 'FineBI仪表板', 'Tableau仪表板', 'PowerBI报表', 'QuickBI报表', 'Superset', 'Metabase', '报表字段/Columns', '报表指标/Metrics', '日期筛选', '下拉筛选', '多选筛选', '报表排序/Sort', '报表分组', '小计/合计', '交叉表', '固定格式报表', '自适应报表', '行冻结列冻结', '合并单元格', '条件格式/颜色', '图表绑定', '组合图/双Y轴', '钻取/Drill', '上下钻', '参数报表', '联动报表', '报表导出/Excel', 'PDF导出', 'CSV导出', '定时任务/Cron', 'Airflow调度', 'DolphinScheduler', '自动化推送/邮件', '钉钉推送', '飞书推送', '企业微信', '报表权限/Permission', '行级权限', '列级权限', '用户权限', '部门权限', '数据权限', '报表质量/QoR', '准确性/时效性', '完整性/一致性', '可读性/美观', '报表监控/Monitor', '任务监控', '数据监控', '异常监控', 'SLA监控', '报表目录管理', '元数据管理', '报表规范', '命名规范', '开发规范', 'BI平台建设']
                },
                '指标体系': {
                    'desc': '构建业务指标体系和KPI',
                    'difficulty': 2,
                    'dimensions': ['指标体系概述/Metric System', '指标定义/Definition', '指标分类/Type', '北极星指标/One Metric', '先行指标/Leading', '滞后指标/Lagging', '结果指标/Outcome', '过程指标/Process', '虚荣指标/Vanity', '指标口径/Calculation', '指标计算公式', '指标数据来源', '指标更新频率', '指标层级/Hierarchy', '公司级指标', '部门级指标', '业务线指标', '产品指标', '用户指标', '运营指标', '财务指标', '指标维度/Dimension', '时间维度/日周月季年', '地区维度/国家省市', '渠道维度/线上线下', '用户维度/新老高低', '产品维度/品类SKU', '设备维度/PC/Mobile', '归因维度', 'OKR目标管理', 'OKR定义', 'OKR对齐', 'OKR跟踪', 'KPI关键绩效', 'KPI设计', 'KPI分解', 'KPI监控', 'KPI复盘', '指标字典/元数据', '指标命名规范', '指标分类体系', '指标标签/Tagging', '指标血缘/Lineage', '指标计算', '指标存储', '指标服务', '指标平台/Metric', 'OneData指标', '指标管理平台', '指标开发/Dev', '指标需求', '指标设计', '指标评审', '指标开发', '指标测试', '指标上线', '指标监控', '指标治理/Governance', '指标质量管理', '指标一致性', '指标复用', '指标淘汰', '交易指标/GMV', 'GMV定义', '订单数/Order', '客单价/AOV', '转化率/CVR', 'CTR点击率', 'UV/独立访客', 'PV/页面浏览', '会话/Session', '跳出率', '留存率/Retention', '新用户数', '活跃用户/DAU', 'MAU月活', '用户增长/Growth', '新增用户', '流失用户', '用户留存', 'ARPU/用户价值', 'LTV/生命周期价值', 'CAC/获客成本', 'CAC计算', 'LTV/CAC比值', 'ROI投资回报', 'ROAS广告回报', 'CPM/CPC/CPS', 'CPL线索成本', '付费率', '复购率', '毛利率', '净利率', 'EBITDA', 'DAU/MAU比值', 'PVPUE', '供给指标/Supply', 'SKU数/SPU', '商品数', '动销率', '库存周转', '采购指标', '履约指标', '完单率', '履约时效', '妥投率', '退货率', '投诉率', 'NPS净推荐', 'CSAT满意度', '指标监控/Dashboard', '指标趋势', '指标预警', '指标归因', '指标拆解/Pyramid', 'GMV拆解', '收入拆解', 'DAU拆解', '转化率拆解', '漏斗分析/Funnel', '归因分析/Attribution', '数据字典/DD', '指标字典', '业务字典']
                },
                '数据仓库': {'desc': '理解数据仓库架构和模型', 'difficulty': 2, 'dimensions': ['数据仓库概述/DW/Data Warehouse', 'OLAP vs OLTP', '数据仓库特征/Subject/集成/稳定/时变', '数据集市/Mart', 'ODS贴源层/DWD明细层/DWS汇总层/ADS应用层', 'Kimball维度建模/Inmon规范化', '星型模型/Star Schema/中心事实表+维度表', '雪花模型/Snowflake/规范化维度', '星座模型/Galaxy/多事实表', '维度表/Dimension/描述属性', '事实表/Fact/业务度量', '代理键/自然键/业务键', '缓慢变化维/SCD Type1覆盖Type2新增', '粒度/Granularity/数据细节层次', '一致性维度/一致性事实', '数据分层/DWD/DWS/ADS', '数据域/Data Domain', '业务过程/Business Process', '维度退化/DD/Degenerate', '维度类型/Date/User', '事实类型/事务/周期快照/累计快照', '可加指标/半可加/不可加', '数仓分层设计', 'Hive/HDFS', 'ClickHouse/Doris', '实时数仓/Lambda/Kappa', '湖仓一体/Lakehouse', 'Delta Lake/Iceberg', '指标体系/OneData']},
                '数据建模': {
                    'desc': '维度建模和事实表设计',
                    'difficulty': 2,
                    'dimensions': ['数据建模概述/Data Modeling', '维度建模/Dimensional', 'Ralph Kimball方法', 'Bill Inmon方法', 'ER模型/实体关系', '概念模型/Conceptual', '逻辑模型/Logical', '物理模型/Physical', '模型评审/Review', '模型设计工具', 'ERWin/PowerDesigner', 'Navicat', 'DBeaver', '维度表设计/Dimension', '维度属性/Attribute', '代理键/Surrogate Key', '自然键/Natural Key', '业务键/Business Key', 'SCD缓慢变化维', 'SCD Type1覆盖', 'SCD Type2新增', 'SCD Type3混合', 'Type4独立表', 'Type6混合', '拉链表/Slowly Change', '历史拉链记录', '全量快照表', 'Type2每日快照', '退化维度/DD', '杂项维度/Junk', '日期维度/Date', '时间维度/Time', '审计维度/Audit', '角色扮演维度', '层次维度/Hierarchy', '多值维度/Multi-Valued', '事实表设计/Fact', '事务事实表/Transaction', '周期快照表/Periodic', '累计快照表/Accumulating', '半累加事实/Semi-additive', '非累加事实', '事实表粒度/Granularity', '原子事实/Atomic', '聚合事实/Aggregate', '合并事实/Consolidated', '一致性事实/Conformed', '维度设计原则', '扁平化设计', '一致性维度', '层次设计', '属性设计', '命名规范', '编码规范', '代理键生成', '事实表设计原则', '一致性设计', '可加性设计', '空值处理', '默认值设计', '星型模型实现', '雪花模型实现', '星座模型实现', '宽表设计/Wide', '数据聚合/汇总表', '中间层设计', '应用层设计', 'Hive建模/HQL', 'ClickHouse建模', 'Doris建模', 'StarRocks建模', '模型版本管理', '模型变更', '模型发布', '模型监控', '建模规范', '命名规范', '分层规范', '开发规范']
                },
                '权限管理': {
                    'desc': '报表和数据行级权限控制',
                    'difficulty': 2,
                    'dimensions': ['权限管理概述/Permission', '系统权限/System', '应用权限/Application', '数据权限/Data', '报表权限/Report', 'FineBI权限', 'FineBI用户', '用户组/Users', '角色/Role', '权限分配', '数据权限配置', '行级权限/RLS', '列级权限/CLS', '部门权限', '数据权限绑定', '权限继承', '权限覆盖', 'FineReport权限', '目录权限', '模板权限', '数据权限', '操作权限', 'PowerBI权限', '工作区权限', 'Workspace Roles', 'Admin/Contributor', 'Member/Viewer', '行级安全/RLS', 'RLS DAX表达式', 'RLS角色', 'RLS规则', 'Tableau权限', 'Site权限', 'Project权限', 'Workbook权限', 'Data Source权限', '用户过滤器', 'User Filter', 'Server权限', '用户角色/Admin', 'Publisher/Explorer', 'Viewer权限', '报表权限', '发布权限', '数据连接权限', '指标权限/Metric', '指标行级', '指标列级', '指标维度约束', '数据源权限', '数据连接权限', '数据表权限', 'ETL权限', '调度权限', '平台权限', '超级管理员', '普通用户', '审计用户', '权限体系设计', 'RBAC基于角色', 'ABAC基于属性', 'PBAC基于策略', '权限模型', '权限矩阵', '权限流程', '权限审批', '权限审计', '权限日志', '最小权限原则', '数据分类/敏感', '敏感数据识别', '数据脱敏权限', '权限变更', '离职权限回收', '权限定期审计', '权限合规/GDPR']
                },
                '移动端': {
                    'desc': '移动端报表适配和发布',
                    'difficulty': 2,
                    'dimensions': ['移动端概述/Mobile BI', '移动BI需求', '移动端报表特点', '移动端设计原则', '简单直观设计', '关键指标突出', '触摸交互', '自适应布局', '响应式设计', '移动端适配/Adaptation', '设备适配/iOS', '设备适配/Android', '平板/Pad适配', '手机/Phone适配', '屏幕尺寸', '分辨率/DPI', '横屏/竖屏', '数据可视化移动端', '图表简化', 'KPI卡片', '数字看板', '核心指标展示', '趋势图简化', '交互设计/Touch', '触摸操作/点击', '滑动/Swipe', '缩放/Pinch', '长按/Long Press', '手势交互', '移动端筛选', '下拉刷新', '下拉选择', '日期选择', '移动端仪表板/Dashboard', '移动BI布局', '移动端组件', 'KPI组件', '图表组件', '列表组件', '地图组件', 'Tab切换', '移动端发布/Publish', 'FineBI移动端', 'FineReport移动', 'PowerBI Mobile', 'Tableau Mobile', 'Superset Mobile', 'APP发布/iOS', 'App Store', 'APP发布/Android', '应用市场', '企业分发', 'MDM管理', '移动端分享', '邮件分享', '微信分享', '链接分享', '移动端权限', '移动端登录', '移动端安全', '数据安全', 'SSO单点登录', 'OAuth登录', '移动端性能', '加载速度', '缓存优化', '离线访问', '推送通知', 'Push Notification', '告警推送', '数据推送', '报表刷新', '实时数据', '定时刷新', '手动刷新', '移动端分析', '使用分析', '访问统计', '用户行为', '访问趋势', '最热报表', '移动端监控', '性能监控', '错误监控']
                }
            }
        }
    },
    '信息安全': {
        '安全工程师': {
            'description': '负责企业信息安全体系建设，安全风险评估和防护。',
            'skills': {
                'VPN': {
                    'desc': '虚拟专用网络配置和安全接入',
                    'difficulty': 2,
                    'dimensions': ['VPN概述/Virtual Private Network', 'VPN类型/远程访问', '站点到站点VPN', 'VPN协议/IPSec', 'IPSec体系/IKE/ESP/AH', '隧道模式/传输模式', '加密算法/AES/DES', '哈希算法/SHA/MD5', 'IKEv1/IKEv2', '预共享密钥/PSK', '证书认证/RSA', 'SSL VPN概述', 'SSL/TLS隧道', 'OpenVPN开源', 'VPN部署/配置', '华为VPN配置', '思科VPN配置', 'VPN网关设备', 'VPN客户端', 'VPN高可用/HA', 'VPN性能优化', 'VPN日志审计', 'VPN安全策略', 'VPN穿透NAT', 'VPN加密传输', 'VPN身份认证', 'VPN带宽管理']
                },
                '云安全': {
                    'desc': '云计算环境的安全配置和防护',
                    'difficulty': 2,
                    'dimensions': ['云安全概述/Cloud Security', '云安全责任/Shared', '责任共担模型', 'IaaS安全', 'PaaS安全', 'SaaS安全', '阿里云安全/AliYun', '阿里云RAM', 'AccessKey管理', '资源访问控制', 'VPC安全', '安全组', '网络ACL', '云防火墙', 'WAF云端', 'DDoS防护', 'AWS云安全', 'IAM身份管理', 'S3安全/ACL', 'VPC终端节点', '安全组/NACL', 'Azure云安全', 'Azure AD', 'RBAC角色', '网络安全组', 'Application Gateway', 'GCP云安全', 'IAM管理', 'VPC网络', 'Cloud Armor', '云数据库安全', 'RDS安全配置', '加密存储', '密钥管理/KMS', '云秘钥管理', 'Secret Manager', '云存储安全', 'OSS/S3安全', '访问控制/ACL', '加密传输/HTTPS', '静态加密', '云网络安全', '防火墙/DDoS', '入侵检测/IDS', '入侵防御/IPS', '云安全组', '微分段/Microseg', '零信任/ZTA', '云原生安全', '容器安全/K8s', 'Docker安全', '镜像安全扫描', '运行时安全', 'K8s网络策略', '服务网格安全/Istio', 'mTLS双向认证', '云合规/GDPR', '云等保', 'CSA云安全', '云安全评估', '云安全监控', '云日志审计', 'CASB云访问', 'CWPP云工作负载', 'CSPM云态势', '安全合规']
                },
                '应用安全': {
                    'desc': 'SDL安全开发生命周期',
                    'difficulty': 2,
                    'dimensions': ['SDL概述/Security Development', 'SDL阶段/Phase', '安全培训/Training', '需求阶段/Secure', '设计阶段/Design', '编码阶段/Implementation', '测试阶段/Verification', '上线阶段/Release', '响应阶段/Response', '安全需求分析', '威胁建模/Threat', 'STRIDE威胁', 'DREAD模型', '攻击树/Attack Tree', '消减策略/Mitigation', '安全设计/Design', '最小权限原则', '纵深防御', 'Fail Secure原则', '开放设计', '心理可接受性', '安全架构评审', '代码审计/Code Review', '静态代码分析/SAST', 'Fortify/Checkmarx', 'SonarQube', 'PMD/FindBugs', '敏感信息检测', '硬编码检测', '安全函数使用', '输入验证', '输出编码', 'SQL注入防护', 'XSS防护', 'CSRF防护', 'SSRF防护', 'XXE防护', '安全测试/Penetration', 'Web渗透测试', 'API安全测试', '移动App测试', '模糊测试/Fuzzing', '安全编码规范', 'Java安全编码', 'Python安全编码', 'PHP安全编码', 'JS安全编码', '安全组件/SCA', '第三方组件', '漏洞扫描/DAST', 'OWASP ZAP', 'Burp Suite', 'Nexpose', '安全发布/Release', '代码签名', '安全配置', '安全部署', '安全响应/Response', '漏洞管理', '补丁管理', 'DevSecOps', 'CI/CD安全', '容器安全扫描', '镜像扫描', 'Secret管理', 'IAM集成']
                },
                '数据安全': {
                    'desc': '数据分类分级、加密、脱敏',
                    'difficulty': 2,
                    'dimensions': ['数据安全概述/Data Security', '数据安全法/个保法', 'GDPR/欧盟通用', 'CCPA/加州隐私', 'PCI DSS/支付卡', '数据分类/Classification', '公开数据/内部数据', '敏感数据/机密', '绝密数据', '数据分级/Levels', '一般/重要/核心', '数据资产盘点', '数据识别/Discovery', '敏感数据识别', '数据标签/Labeling', '数据加密/Encryption', '对称加密/AES/DES', '非对称加密/RSA', 'SM国密算法', 'SM2/SM3/SM4', '哈希算法/SHA', 'MD5/不推荐', '数据传输加密/TLS', 'SSL证书', 'HTTPS配置', '数据存储加密', '透明加密/TDE', '列加密/Column', '应用加密', '数据库加密', '磁盘加密/BitLocker', '文件加密/EFS', '全盘加密/FDE', '密钥管理/KMS', 'HSM硬件', '密钥生命周期', '密钥轮换/Rotation', '密钥存储', '密钥备份', '数据脱敏/Masking', '静态脱敏/Static', '动态脱敏/Dynamic', '掩码/Mask/***', '替换脱敏/Substitute', '随机化/Randomize', '泛化/Generalize', '截断/Truncation', '打码/String Mask', '姓名脱敏', '手机号脱敏', '身份证脱敏', '邮箱脱敏', '银行卡脱敏', '数据水印/Watermark', '可见水印/Visible', '不可见水印', '鲁棒水印', '脆弱水印', '数据溯源', '数据血缘/Lineage', '数据访问控制', 'RBAC权限模型', 'ABAC属性', '列级权限', '行级权限/RLS', '数据审计/Audit', '访问日志', '操作日志', '审计分析', '数据备份/Backup', '加密备份', '备份恢复', '数据销毁/Disposal', '安全擦除', '物理销毁', 'NIST 800-88', '数据完整性', '数字签名', 'MAC消息认证', '数据完整性验证']
                },
                '渗透测试': {
                    'desc': '模拟攻击测试系统安全性，发现安全弱点',
                    'difficulty': 2,
                    'dimensions': ['渗透测试概述/Penetration', 'PTES标准', 'OWASP测试指南', '渗透测试流程', '信息收集/Recon', '主动收集/DNS', '被动收集/OSINT', 'Shodan/Censys', 'Google Dorking', '子域名枚举', '端口扫描/Nmap', '服务识别', '漏洞扫描/OpenVAS', 'Nikto/Web扫描', '漏洞验证', 'Web渗透测试', 'SQL注入/SQLi', 'XSS跨站脚本', 'CSRF请求伪造', 'SSRF服务端请求', 'XXE外部实体', '文件上传/Webshell', '文件包含/LFI/RFI', '命令注入/Command', '代码执行/Code', '业务逻辑漏洞', '越权测试/IDOR', '水平越权', '垂直越权', '密码找回漏洞', 'JWT攻击', '敏感信息泄露', '接口未授权', 'CORS错误', 'SSRF/内网探测', '内网渗透/Network', '内网信息收集', '存活主机扫描', '端口扫描/内网', 'SMB利用/MS17-010', 'Pass-the-Hash', '哈希传递/PTH', '横向移动/Lateral', '票据传递/PTT', 'Kerberos攻击', 'Golden Ticket', '权限提升/Elevation', '本地漏洞利用', 'UAC绕过', '内核漏洞', 'sudo提权', 'SUID提权', '计划任务提权', '数据库提权', '域渗透/AD', '域信息收集', 'BloodHound', 'Kerberoasting', 'AS-REP Roasting', '权限维持/Persistence', '注册表自启动', 'WMI持久化', '计划任务', '社工钓鱼', '钓鱼邮件', '钓鱼网站', '水坑攻击', '物理渗透/U盘', '报告编写', '漏洞详情', 'POC编写', '修复建议', '风险评级']
                },
                '等保2.0': {
                    'desc': '网络安全等级保护标准和测评',
                    'difficulty': 2,
                    'dimensions': ['等保概述/等级保护', '等保1.0 vs 2.0', '五个等级/Level', '第一级自主保护', '第二级指导保护', '第三级监督保护', '第四级强制保护', '第五级专控保护', '通用要求/扩展要求', '安全物理环境', '物理访问控制', '防盗防破坏', '防火防水', '温湿度控制', '电力供应', '电磁防护', '安全通信网络', '网络架构', '通信传输安全', '可信验证', '安全区域边界', '边界防护', '访问控制', '入侵防范', '恶意代码防范', '安全审计', '安全计算环境', '身份鉴别', '访问控制', '安全审计', '入侵防范', '恶意代码防范', '数据安全', '备份恢复', '安全管理中心', '系统管理', '审计管理', '安全管理', '安全管理制度', '安全管理制度', '安全管理机构', '安全管理人员', '安全建设管理', '安全运维管理', '云计算安全', '移动互联安全', '物联网安全', '工业控制系统', '定级备案', '专家评审', '公安机关备案', '建设整改', '等级测评', '测评机构', '测评流程', '控制点', '高风险判定', '测评方法', '技术测评', '管理测评', '主机安全测评', '网络安全测评', '应用安全测评', '数据安全测评', '测评报告', '整改建议', 'GB/T 22239-2019', '安全通用要求', '行业扩展要求']
                },
                '网络安全': {
                    'desc': '网络边界防护、入侵检测和流量监控',
                    'difficulty': 2,
                    'dimensions': ['网络安全概述/Network Security', '网络架构安全', '分层设计', '核心层/汇聚层', '接入层安全', '边界防护', '防火墙/Firewall', '网络隔离/VLAN', 'DMZ隔离区', '内网隔离', '访问控制/ACL', '策略配置', '最小权限', '入侵检测/IDS', 'NIDS网络IDS', 'Snort/Suricata', '规则/签名', '告警分析', '入侵防御/IPS', 'IDS vs IPS', '阻断模式', '流量监控', 'NetFlow收集', 'sFlow收集', '流量分析', '异常检测', 'DDoS防护', '流量清洗', '黑洞路由', 'CC攻击防护', 'SYN Flood', 'UDP Flood', 'HTTP Flood', 'DNS防护', '应用层防护', 'WAF/Web应用', 'ModSecurity', 'Web防护规则', 'OWASP Top10', 'SQL注入防护', 'XSS防护', 'CSRF防护', '网络准入/NAC', '802.1X认证', 'Portal认证', 'MAC认证', '设备安全', '路由器安全', '交换机安全', '安全配置', '固件更新', '网络监控', 'Zabbix监控', 'Prometheus', 'Grafana可视化', '日志分析/ELK', 'Splunk', '告警规则', 'SIEM平台', '网络扫描/Nmap', '漏洞扫描', '渗透测试', '网络设备加固', '路由安全', 'STP安全', 'ARP防护', 'DHCP Snooping', 'IP Source Guard', '802.1X端口安全', '网络日志审计', '安全事件', '应急响应', '网络QoS']
                },
                '防火墙': {
                    'desc': '访问控制策略配置和网络边界防护',
                    'difficulty': 2,
                    'dimensions': ['防火墙概述/Firewall', '防火墙类型/硬件', '软件防火墙', '云防火墙', '包过滤/Packet Filter', '状态检测/Stateful', '代理防火墙/Proxy', '下一代防火墙/NGFW', '安全区域/Zone', 'Trust/Untrust', 'DMZ/Local', '安全策略/Policy', '默认策略/Deny', '策略顺序', '源地址/Dst', '目的地址/Src', '服务/端口', '用户/身份', '时间计划', '会话管理/Session', '连接跟踪', '状态表/State', 'NAT功能/SNAT', 'DNAT端口映射', '攻击防护/Defense', 'DDoS防护', 'SYN Flood', 'ICMP Flood', '扫描防护', 'IP欺骗', '应用控制', 'URL过滤', '应用识别', 'IPS联动', '病毒防护', '内容过滤', 'SSL解密/Inspection', '证书检查', '带宽管理/QoS', '会话限制', '负载均衡/FWLB', '高可用/HA', '主备/主主', '会话同步', '故障切换', '部署模式/Inline', '旁路部署', '透明模式', '路由模式', '华为防火墙/USG', '思科ASA/FTD', 'Juniper SRX', 'Fortinet FG', '天融信', '启明星辰', '绿盟', '策略优化', '日志分析', '告警处理', '配置备份']
                },
                '风险评估': {
                    'desc': '安全风险识别和评估报告编写',
                    'difficulty': 2,
                    'dimensions': ['风险评估概述/Risk', '风险评估流程', '资产识别/Asset', '资产分类', '资产赋值', '资产清单', '威胁识别/Threat', '威胁分类', '威胁源/攻击者', '威胁事件', '脆弱性识别/Vuln', '技术脆弱性', '管理脆弱性', '脆弱性评估', '漏洞扫描', '配置核查', '渗透测试', '风险分析/Analysis', '风险值计算', '风险矩阵', '可能性/P/Likelihood', '影响/I/Impact', '风险等级/High', 'Medium/Low', '风险处置/Treatment', '风险规避', '风险降低', '风险转移', '风险接受', '残余风险', '风险应对', '风险监控', '风险沟通', '风险评估方法', '定性分析', '定量分析', '半定量分析', 'GB/T 20984', 'ISO 31000', 'ISO 27005', 'NIST SP 800-30', 'OCTAVE方法', '熵值法', '层次分析法/AHP', '威胁建模/STRIDE', 'DREAD模型', 'CVSS评分', '风险矩阵/Matrix', '风险报告/Report', '评估报告', '整改建议', '风险跟踪', '复测评估', '合规要求/Compliance', '等保风险评估', '行业合规', '资产评估/Inventory', '重要性评估', '敏感性评估', '业务连续性', '影响分析/BIA']
                },
                'ISO27001': {
                    'desc': '信息安全管理体系',
                    'difficulty': 3,
                    'dimensions': ['ISO 27001概述', '信息安全管理/ISMS', 'PDCA循环', 'Plan计划', 'Do做', 'Check检查', 'Act行动', '范围界定/Scope', '适用性声明/SoA', '风险评估/RA', '风险管理', '安全策略/Policy', '信息安全方针', '组织安全/Organization', '内部组织', '移动设备和远程', '信息分类/Classification', '信息标记', '信息处理', '采购管理/Supplier', '供应商关系', 'SLA要求', '资产管理/Asset', '资产清单', '资产责任人', '资产分类', '信息分类', '介质处理/Asset', '设备维护', '安全处置', '人力资源安全/HR', '安全职责', '背景调查', '入职/离职', '安全培训', '纪律处理', '物理安全/Physical', '安全区域', '周边防护', '物理入口', '办公室防护', '设备安全', '通用控制', '操作安全/Ops', '操作规程', '变更管理', '容量管理', '分离环境', '恶意软件', '备份', '日志记录', '通信安全/Comms', '网络安全', '信息传输', '电子公告', '访问控制/Access', '业务需求', '用户访问', '用户职责', '访问控制', '密码策略', '密码管理', '供应商访问', '系统访问', '变更控制', '密码技术/Crypto', '加密控制', '密钥管理', '物理密钥', '安全事件/Incident', '事件管理', '报告事件', '事件响应', '业务连续性/BCP', '业务连续性', '可用性', '冗余', '合规性/Compliance', '法律要求', '知识产权', '保护记录', '隐私保护', '审计/Review', '内部审计', '管理评审', '改进/Improvement', '不符合项', '纠正措施', '持续改进', 'A.5-A.18附录', 'Controls控制项', '实施指南', '认证流程', '认证审核', '证书维护']
                },
                '安全加固': {
                    'desc': '系统安全配置和漏洞修复',
                    'difficulty': 3,
                    'dimensions': ['安全加固概述/Hardening', '安全基线/Baseline', 'CIS Benchmark', '等保合规加固', '加固流程/Process', '风险评估', '加固实施', '验证检查', 'Windows加固', '账户安全/密码', '密码策略', '账户锁定', 'Guest禁用', '审核策略', '服务禁用', '端口管理', '防火墙/WF', 'PowerShell安全', '补丁管理', '权限加固/ACL', 'BitLocker加密', 'Linux加固', 'SELinux/AppArmor', '账号安全', 'SSH加固', 'sudo权限', '防火墙/iptables', '服务加固/Apache', 'Nginx安全', 'MySQL安全', 'Redis安全', 'Tomcat安全', '中间件加固', 'SSL/TLS加固', '协议加固', '弱口令修复', '漏洞扫描', '补丁修复', 'WAF防护', '配置修复', '云安全加固', 'IAM加固', 'VPC加固', '安全组', '数据库加固', '存储加固', 'Docker加固', 'K8s加固', '基线核查/CIS', '自动化脚本/Ansible', '加固验证', '渗透测试', '配置审计']
                },
                '安全审计': {
                    'desc': '日志审计和行为分析',
                    'difficulty': 3,
                    'dimensions': ['安全审计概述/Audit', '审计目标/Purpose', '审计范围/Scope', '审计类型/Type', '内部审计/Internal', '外部审计/External', '合规审计/Compliance', '技术审计/Technical', '管理审计/Management', '审计流程/Process', '审计计划/Plan', '风险评估', '审计范围', '审计准则', '准备阶段', '现场审计', '审计报告', '跟踪验证', '审计标准/Standards', 'ISO 27001审计', 'PCI DSS审计', 'SOX审计', '等保审计', '审计方法/Methods', '访谈/Interview', '文档审核', '技术测试', '漏洞扫描', '渗透测试', '配置核查', '日志分析', '样本抽样', '系统审计/System', '操作系统审计', 'Windows Audit', 'Linux Audit', '网络设备审计', '数据库审计/DAM', '应用审计/App', '中间件审计', '云服务审计', 'Web应用审计', '日志审计/Log', '日志收集', '日志存储', '日志分析', '异常检测', '关联分析', '告警规则', 'SIEM审计', 'Splunk审计', 'ELK审计', '用户行为/UBA', 'UEBA分析', '异常行为检测', '内部威胁', '数据外发', '权限滥用', '审计报告/Report', '审计发现', '不符合项', '整改建议', '风险评级', '审计意见', '管理建议', '审计跟踪', '整改验证', '审计工具/Tools', '日志分析工具', '配置核查工具', '漏洞扫描工具', '渗透测试工具', '代码审计工具', '合规检查工具', '审计管理/Management', '审计计划管理', '审计文档', '审计档案', '独立性保证']
                }
            }
        },
        '渗透测试工程师': {
            'description': '模拟黑客攻击测试系统安全性，发现并报告安全漏洞。',
            'skills': {
                'Nmap': {
                    'desc': '网络扫描和端口探测',
                    'difficulty': 2,
                    'dimensions': ['Nmap概述/Network Mapper', 'Nmap安装/Linux/Windows', '基本扫描/nmap target', '端口状态/Open/Closed', 'TCP SYN扫描/-sS', 'TCP connect/-sT', 'UDP扫描/-sU', 'FIN/NULL/XMAS扫描', 'Ping扫描/-sn/-sP', 'ACK扫描/-sA', '版本检测/-sV', 'OS检测/-O', '脚本扫描/--script', '全面扫描/-A', '快速扫描/-F', '端口范围/-p', '排除主机/--exclude', 'NSE脚本/vuln/safe', 'vulners脚本', 'firewalk脚本', 'http-enum', 'dns-brute', 'smb-enum', '默认脚本/safe', '输出格式/-oA/-oN', '详细输出/-v', '调试模式/-d', '诱饵扫描/-D', '空闲扫描/-sI', '源地址欺骗/-S', 'MAC伪造/--spoof-mac', '分片扫描/-f', 'Zenmap GUI', '批量扫描/shell', '自动化/CI集成']
                },
                'OWASP': {
                    'desc': 'Web安全漏洞标准和测试方法',
                    'difficulty': 2,
                    'dimensions': ['OWASP概述/Open Web', 'OWASP Top 10/2021', 'A01失效访问控制/Broken', 'A02加密失败/Crypto', 'A03注入/Injection', 'SQL注入/SQLi', '命令注入/Command', 'XSS跨站脚本', 'A04设计不安全/Insecure', 'A05安全配置错误/Security', 'A06脆弱组件/Vulnerable', 'A07身份认证失败/Auth', 'A08数据完整性失败/Integrity', 'A09日志监控不足/Logging', 'A10服务器伪造/SMRI', 'OWASP API Top 10', 'API1失效对象授权', 'API2失效认证', 'API3过度数据暴露', 'API4缺乏资源限制', 'API5功能级授权', 'API6批量赋值', 'API7用户伪造', 'API8默认值', 'API9库存管理', 'API10不充分记录', 'OWASP测试指南', '测试方法/Testing', '信息收集/Recon', '配置测试/Config', '身份管理测试', '认证测试/Auth', '授权测试', '会话管理/Session', '输入验证/Input', '错误处理测试', '加密测试/Crypto', '业务逻辑测试', '客户端测试/Client', '报告编写', 'ASVS应用安全', 'ASVS要求', 'Level1-3验证', 'SAML安全测试', 'WebSocket测试', 'GraphQL测试', 'REST API测试', 'OWASP ZAP使用', 'Burp Suite使用', 'DVWA靶场', 'WebGoat靶场', 'Juice Shop靶场', ' VulnHub靶场', '靶场实践']
                },
                'SQLMap': {
                    'desc': '自动化SQL注入检测工具',
                    'difficulty': 2,
                    'dimensions': ['SQLMap概述/自动化注入', 'SQLMap安装/Python', '基本使用/sqlmap -u', 'POST注入/-r request', 'Cookie注入/--cookie', '批量扫描/-m targets', 'Level/Risk等级', '--level等级1-5', '--risk风险1-3', '--batch自动确认', '--random-agentUA', '检测技术/Techniques', '--technique B/E/T/U/S', 'Boolean盲注/B', 'Error-based/E', 'Time-based/T', 'Union联合/U', 'Stacked堆叠/S', '数据库枚举/--dbs', '表枚举/--tables', '列枚举/--columns', '数据导出/--dump', 'OS Shell/--os-shell', 'OS命令/--os-cmd', '注册表/--reg-read', '指纹识别/-f', 'Banner识别', '当前用户/--current-user', '当前数据库/--current-db', '管理员/--is-dba', '密码哈希/--passwords', '文件读取/--file-read', '文件写入/--file-write', 'WebShell上传', 'Tamper脚本/waf', 'space2comment', 'between', 'charencode', 'equaltolike', 'randomcase', 'space2hash', 'sqlmap更新', 'Sqlmap GUI/用户界面', 'Sqlmap API调用', '绕过WAF/Evasion', '混淆/Obfuscation', '编码/Encoding', '注释/Comment', '参数污染', '真实环境', 'Sqlmap防护/Bypass', 'Sqlmap日志分析', 'Sqlmap报告', 'CTF SQL注入', '真实渗透案例']
                },
                '应急响应': {
                    'desc': '协助修复发现的安全漏洞',
                    'difficulty': 2,
                    'dimensions': ['应急响应概述/Incident', 'PDCERF模型/Phase', '准备阶段/Preparation', '检测阶段/Identification', '遏制阶段/Containment', '根除阶段/Eradication', '恢复阶段/Recovery', '事后总结/Lessons', '应急团队/CSIRT', '事件分级/P1-P4', '紧急事件P1', '严重事件P2', '一般事件P3', '轻微事件P4', '应急预案/Plan', '事件上报/Report', '事件记录/Doc', '时间线/Timeline', '漏洞修复/Vuln Fix', '补丁修复/Patch', '配置修复', '代码修复', 'WAF防护', '网络隔离', '访问控制', '修复验证/Verify', '复测/Retest', '漏洞关闭', '漏洞复盘', '修复报告', '漏洞修复建议', '缓解措施', '临时方案', '永久方案', '修复优先级', '紧急修复', '计划修复', '变更管理', '配置变更', '代码发布', '回滚方案', 'DevSecOps', '安全运营', '补丁管理', '漏洞管理', '工单系统', '修复跟踪', '修复确认']
                },
                '渗透测试': {
                    'desc': 'Web应用、网络和系统的安全测试',
                    'difficulty': 2,
                    'dimensions': ['渗透测试概述/Pentest', '渗透测试标准', 'PTES渗透测试', 'OWASP测试指南', '渗透测试流程', '前期交互/Interaction', '情报收集/Recon', '威胁建模/Threat', '漏洞分析/Vuln', '渗透攻击/Exploitation', '后渗透/Post-Exploit', '报告撰写/Report', '信息收集/Intelligence', 'DNS信息收集', '子域名枚举', 'Whois查询', 'Google Hacking', 'Shodan搜索', '端口扫描/Nmap', '服务枚举', '版本检测', '漏洞扫描/OpenVAS', 'Nikto Web扫描', 'Web渗透测试', 'SQL注入测试', 'XSS测试/Reflected', 'Stored/Stored', 'DOM-based', 'CSRF测试', 'SSRF测试', 'XXE测试', '文件上传/Upload', '文件包含/LFI/RFI', '命令注入/Command', '代码执行/Code', '业务逻辑漏洞', '越权测试/IDOR', '弱口令测试', 'JWT测试', 'API测试/Rest', 'GraphQL测试', '移动App测试', '网络渗透测试', '内网信息收集', '存活主机', '端口扫描', 'SMB漏洞/MS17-010', 'RDP漏洞/CVE-2019', 'Pass-the-Hash', '横向移动/Lateral', '权限提升/Elevation', '本地漏洞利用', 'UAC绕过', '域渗透/AD', '系统渗透测试', 'Linux渗透', 'Windows渗透', '数据库渗透', 'CMS渗透/WordPress', 'Joomla/Drupal', '中间件渗透', 'Tomcat/JBoss', 'WebLogic', 'Apache/Nginx', '后渗透维持/Persist', '权限维持', '后门植入', '痕迹清理', '日志清理', '报告编写', '漏洞描述', 'POC/POC', '修复建议', '风险评级']
                },
                '漏洞报告': {
                    'desc': '编写专业的渗透测试报告',
                    'difficulty': 2,
                    'dimensions': ['漏洞报告概述/Report', '报告结构/Structure', '封面/Cover', '目录/Table of', '执行摘要/Executive', '背景/Background', '目标/Scope', '方法/Methodology', '发现/Finding', '结论/Conclusion', '建议/Recommendation', '附录/Appendix', '报告类型/Type', '渗透测试报告', '漏洞扫描报告', '代码审计报告', '安全评估报告', '测试结果摘要', '漏洞总览', '高危漏洞', '中危漏洞', '低危漏洞', '信息级', '漏洞详情/Detail', '漏洞名称/Name', 'CVE编号', '漏洞类型/Type', '风险等级/Severity', '严重/高/中/低', 'CVSS评分', 'CVSS向量', '影响范围/Summary', '漏洞描述/Desc', '环境版本', '复现步骤/Steps', '步骤1截图', '步骤2截图', '验证命令', 'POC代码/POC', 'EXP利用代码', '修复建议/Fix', '临时方案', '永久方案', '参考链接/Reference', 'OWASP指南', 'CVE链接', '厂商补丁', '代码示例', '附录信息', '漏洞证据', '截图证据', '日志证据', '工具输出', '报告格式/PDF', 'Word格式', 'HTML格式', '报告模板', '漏洞分级标准', 'CVSS计算', '风险矩阵', '报告审核/Review', '报告质量', '专业术语', '漏洞分类', '修复优先级', '修复期限/SLA', '报告归档/Archive']
                },
                'Burp Suite': {
                    'desc': 'Web应用安全测试平台',
                    'difficulty': 3,
                    'dimensions': ['Burp Suite概述/Web测试', 'Burp安装/Java环境', 'Burp Pro vs Free', 'Proxy代理配置', '浏览器代理设置', 'Intercept拦截请求', 'Forward放行', 'Drop丢弃', 'Action菜单', 'HTTP History历史', 'WebSockets History', 'Target站点地图', 'Site Map站点', 'Scope范围设置', 'Spider爬虫/Discovery', '被动扫描/Passive', '主动扫描/Active', 'Scanner漏洞扫描', 'Scan issues漏洞', 'SQLi/XSS/CSRF', 'Scanner Options配置', 'Intruder攻击器', 'Sniper单Payload', 'Battering Ram重复', 'Pitchfork交叉', 'Cluster Bomb组合', 'Payload Types类型', 'Simple list简单', 'Runtime file文件', 'Numbers数字', 'Dates日期', 'Brute Forcer暴力', 'Character frobber', 'Bit flipper位翻转', 'SQLi payload', 'XSS payload', 'Intruder Positions位置', 'Clusterbomb攻击', 'Payload Processing处理', 'Payload Encoding编码', 'Grep Match标记', 'Comparer比较器', 'Repeater重放器', 'Request修改', 'Response查看', 'Decoder解码器', 'Encode编码', 'Decode解码', 'Hash哈希', 'Smart decode智能', 'Sequencer序列器', 'Token分析', 'Entropy熵', 'Extender扩展', 'BApp Store商店', 'SQLMap集成', 'Python脚本', 'Jython支持', 'CSRF POC生成', 'JWT攻击/alg:none', 'JWT暴力破解', '路径穿越/../', '命令注入测试', '越权测试/Batch', '验证码识别', 'Burp Collaborator', 'Out-of-Band OOB', '扫描调度', '报告生成/Report', 'Scope高级设置', 'Session处理', 'Macro宏', 'Cookie Jar', 'Target Map过滤', 'Burp API自动化']
                },
                'Kali Linux': {
                    'desc': '专业渗透测试操作系统及工具集',
                    'difficulty': 3,
                    'dimensions': ['Kali Linux概述/渗透OS', 'Kali下载/VMware镜像', 'Kali安装/物理机', 'Kali更新/apt update', 'Kali工具分类', '信息收集/Recon', '被动信息收集/OSINT', 'whois查询', 'DNS查询/dig/nslookup', '子域名枚举/sublist3r', '搜索引擎/Shodan', 'Google Hacking/Dorks', '邮箱收集/theHarvester', '网站克隆/HTTrack', '主动扫描/Active', 'Nmap端口扫描', 'Nikto Web扫描', 'Dirb目录爆破', 'Gobuster', 'WPScan/WordPress', '漏洞扫描/Vuln', 'Nikto服务器扫描', 'OpenVAS综合', 'Nessus漏洞', 'Nexpose漏洞', 'AWVS漏洞', '密码攻击/Password', 'Hashcat哈希破解', 'John the Ripper/JTR', 'Hydra在线破解', 'Medusa/Hydra', 'CrackMapExec', 'Mimikatz明文', 'Responder LLMNR', '社会工程学/SE', 'SET工具包/Social', '钓鱼攻击/Phishing', '凭证收集/Creds', 'Web渗透/Web', 'Burp Suite代理', 'SQLMap注入', 'Sqlmap --dbs/--dump', 'XSS测试/BeEF', 'CSRF测试', 'SSRF/XXE测试', '文件上传测试', '命令注入测试', 'Web模糊测试/FFUF', 'Burp Intruder', 'Web漏洞利用', 'Metasploit框架', 'msfconsole/控制台', 'msfvenom载荷', 'armitage GUI', 'meterpreter后门', '提权/Elevation', '本地漏洞', '绕过UAC', '端口转发/Pivot', '内网穿透', '横向移动/Lateral', '令牌窃取', '哈希传递/PTH', 'Golden Ticket', '维持访问/Persist', '注册表持久化', '无线攻击/Wireless', 'Aircrack-ng套件', 'WEP/WPA破解', 'Wifite自动化', '移动渗透/Mobile', 'Frida动态分析', 'Drozer/Android', 'MobSF移动安全', '逆向工程/Reverse', 'Radare2/Ghidra', '免杀/Evasion', 'Veil/Shellter', '取证分析/Forensics', 'Autopsy磁盘', 'Volatility内存', 'Foremost恢复', 'Steghide隐写']
                },
                'Metasploit': {
                    'desc': '漏洞利用框架和渗透测试工具',
                    'difficulty': 3,
                    'dimensions': ['Metasploit概述/渗透框架', 'msfconsole控制台', 'msfdb数据库初始化', 'msfvenom载荷生成', 'armitage GUI', 'Metasploit模块', 'Auxiliary辅助模块', 'Exploit漏洞利用', 'Payload攻击载荷', 'Encoder编码模块', 'NOP空指令', 'Post后渗透', '模块路径/Module', 'search搜索', 'use选择模块', 'show options', 'set设置选项', 'run/exploit执行', 'sessions会话管理', 'sessions -i接入', 'meterpreter命令', 'sysinfo系统信息', 'getuid用户', 'getsystem提权', 'ps进程', 'migrate进程迁移', 'shell获取', 'hashdump哈希', 'mimikatz明文', 'load kiwi', 'screenshot截图', 'webcam摄像头', 'record_mic录音', 'keyscan键盘', 'upload上传', 'download下载', 'cd/pwd目录', 'timestomp时间戳', 'portfwd端口转发', 'autoroute路由', 'run post后渗透', 'post/windows/gather', 'post/linux/gather', 'run getgui开启RDP', 'payload类型/shell', 'reverse_tcp反向', 'bind_tcp正向', 'meterpreter/reverse', '架构/x86/x64', 'meterpreter分类', '编码器/shikata_ga_nai', '迭代编码/Iterations', '永恒之蓝/MS17-010', 'BlueKeep/RDP', 'CVE漏洞利用', 'msfvenom生成', '-p载荷/-f格式', '-e编码/-i迭代', '-o输出', '后渗透信息收集', '内网信息收集', '域渗透/Domain', 'Kerberos攻击', 'Golden Ticket', 'Pass-the-Hash', 'Metasploit配置', 'handler监听', 'multi/handler', 'searchsploit/EDB', '辅助模块/portscan', 'auxiliary/scanner/smb', '辅助/ssh/ftp', '辅助/http']
                },
                '内网渗透': {
                    'desc': '横向移动、权限提升、域渗透',
                    'difficulty': 3,
                    'dimensions': ['内网渗透概述/Lateral', '内网信息收集', '存活主机发现', 'arp-scan', 'nmap主机发现', 'nbtscan', 'netbios扫描', '端口扫描/内网', '22/SSH', '23/Telnet', '80/HTTP', '445/SMB', '3389/RDP', '3306/MySQL', '1433/SQLServer', '1521/Oracle', '5985/WinRM', '服务识别', '版本检测', 'SMB漏洞/MS17-010', 'CVE-2019-0708', 'CVE-2020-0796', 'SMB协议利用', 'psexec远程', 'smbexec', 'wmic远程', 'winrm远程', 'PsExec工具', 'WMIExec', 'Impacket套件', 'Pass-the-Hash', 'PTH哈希传递', 'PtH攻击', 'PtT票据传递', 'NTLM Relay', 'SMB Relay', 'LLMNR Poisoning', 'NetBIOS Spoofing', '横向移动/Lateral', 'IPC$连接', '计划任务/at', 'schtasks', '服务利用/SC', '令牌窃取/Token', 'Incognito', ' Rotten Potato', 'Hot Potato', 'Print Spooler', 'PrintNightmare', '本地漏洞利用', 'Windows Exploit', 'linux-exploit', 'kernel-exploit', 'UAC绕过/BypassUAC', 'AlwaysInstallElevated', '服务权限/SeImpersonate', 'Rotten Potato', 'Juicy Potato', 'Token Manipulation', '域渗透/Active Directory', 'AD信息收集', 'powerview信息', 'bloodhound信息', '域用户枚举', '域计算机枚举', '域组枚举', 'OU组织单位', 'GPO组策略', ' Trusts信任', 'Kerberoasting', 'AS-REP Roasting', 'LDAP枚举', '域控制器/DC', 'Golden Ticket', 'Silver Ticket', 'Mimikatz票据', 'Mimikatz dcsync', 'DCSync攻击', 'krbtgt hash', 'SID History', 'AdminSDHolder', 'ACL滥用', '约束委派', '资源约束', '域持久化/Persist', 'DSRM密码', 'krbtgt重置', 'Golden Ticket', 'DCShadow', 'Shadow Credentials', '域管理员获取', '域控上线', '内网提权', 'BypassAV', 'BypassAMCI', '权限维持/Privilege', '注册表自启动', 'WMI持久化', '计划任务/Schtasks', '服务创建/SC', 'DLL劫持', 'CLR劫持', 'COM劫持', 'netcat后门', 'PowerShell后门', 'WMI后门', '后门/shell', '内网代理/Proxy', 'frp内网穿透', 'ngrok穿透', 'msf proxy', 'reGeorg WebShell', 'Neo-reGeorg', '冰蝎WebShell', '哥斯拉WebShell', '蚁剑WebShell', '内网扫描/扫描器', 'fscan内网扫描', 'ladon扫描', 'fscan用法', '横向移动检测', '日志分析', '安全监测', '内网防御绕过']
                },
                '漏洞利用': {
                    'desc': '漏洞验证和利用脚本编写',
                    'difficulty': 3,
                    'dimensions': ['漏洞利用概述/Exploitation', '漏洞原理/Principle', '漏洞类型/Type', '缓冲区溢出/Buffer', 'Stack溢出', 'Heap溢出', '格式化字符串/%x', '整数溢出/Int Overflow', 'Use After Free/UAF', 'Double Free', '类型混淆', '命令注入/Command', 'SQL注入/SQLi', 'XSS跨站脚本', 'CSRF请求伪造', '远程代码执行/RCE', '本地提权/EoP', '漏洞利用流程', '漏洞识别/Identify', '漏洞验证/Verify', 'PoC开发/Proof', 'EXP开发/Exploit', '漏洞利用框架', 'Metasploit框架', 'CANVAS利用', 'Core Impact', 'EDB Exploit数据库', 'SearchSploit搜索', 'CVE漏洞查询', 'Exploit-DB', 'GitHub Exploit', '漏洞利用开发', 'Python exp开发', 'Poc编写/Python', 'Python脚本/shell', 'C语言exp开发', '栈溢出exp', 'SEH覆盖', 'Egg Hunter', 'Shellcode编写', 'msfvenom生成', 'x86 shellcode', 'x64 shellcode', '反弹shell', '正向shell', '编码/shikata_ga_nai', 'xor编码', '坏字符/Badchars', ' Immunity Debugger', 'WinDbg调试', 'IDA Pro反汇编', 'Ghidra反编译', '漏洞验证/Vuln Verify', 'Nessus扫描', 'OpenVAS扫描', 'Metasploit验证', 'CVE利用/MSF', '漏洞利用防护', 'DEP数据执行', 'ASLR地址随机', 'Stack Canary', 'SafeSEH', 'SEHOP', 'CFI控制流', '缓解措施/Bypass', '绕过DEP/ROP', '绕过ASLR', '绕过Canary', '漏洞利用模块', '漏洞利用脚本', '渗透工具集成', 'Burp集成', 'SQLMap集成', 'Nmap集成', '自动化利用', 'CTF漏洞利用', 'Pwn/CTF', 'Binary Exploit', '格式字符串', '栈迁移', 'House of Spirit', 'House of Force', 'House of Einherjar', 'Unsorted Bin', 'Fast Bin Attack', 'House of Lore', '堆利用/Unlink', 'IO_FILE利用', 'onegadget', 'DynELF泄密', 'Ret2dlresolve', 'ROP链构造', 'Ret2libc', 'Ret2csu', 'SROP/Sigreturn', 'BROP/Blind ROP', 'JOP/Jump Oriented', 'COP/Call Oriented']
                },
                '社会工程学': {
                    'desc': '钓鱼攻击、物理渗透测试',
                    'difficulty': 3,
                    'dimensions': ['社会工程学概述/SE', '社工攻击类型/Type', '钓鱼攻击/Phishing', '鱼叉钓鱼/Spear', '鲸钓/Whaling', '短信钓鱼/Smishing', '语音钓鱼/Vishing', '邮件钓鱼/Email', '恶意链接', '恶意附件', 'SET工具包/Social', 'Gophish钓鱼框架', 'Blackeye钓鱼', 'SocialFish', '钓鱼页面克隆', '克隆网站', '凭证收割', 'SET工具使用', 'msf钓鱼模块', '钓鱼邮件/Mail', '邮件伪造/Spoof', 'SPF/DKIM/DMARC', '邮件头分析', '社工库查询', '泄漏数据搜索', '信息收集/SE Recon', 'LinkedIn信息', 'Facebook信息', 'Twitter信息', '微博信息', '脉脉信息', 'GitHub信息', '拼凑攻击', '信息验证', '密码字典生成', 'CUPP字典', 'cupp.py用法', 'CeWL爬取字典', '社工密码', '物理渗透/Physical', '门禁 bypass', 'RFID复制', 'NFC复制', '_EM418', 'Proxmark3', '洛阳铲/开锁', '物理社工', '伪装渗透', '尾随/Tailgating', '肩窥/Shoulder', '垃圾桶潜水', '钓鱼WiFi/Evil', 'Hostapd/热点', 'WIFIPhisher', '嗅探/Sniffing', '中间人/MITM', 'SSLStrip', 'DNS欺骗', 'ARP欺骗', 'Session劫持', 'BadUSB/USB攻击', 'Arduino BadUSB', ' Teensy攻击', 'Rubber Ducky', 'U盘投放/Drop', '社会工程心理学', '权威原则', '互惠原则', '承诺一致', '社会认同', '稀缺原则', '喜好原则', '熟悉原则', '紧迫感/FOMO', '恐惧心理', '好奇心利用', '信任建立', '目标选择', '信息信封', '钓鱼模板', '钓鱼话术', '钓鱼邮件模板', '社工报告', '攻击记录', '攻击效果']
                }
            }
        },
        '安全运维工程师': {
            'description': '监控安全事件，进行应急响应和事后分析。',
            'skills': {
                '取证分析': {
                    'desc': '数字取证和攻击溯源',
                    'difficulty': 2,
                    'dimensions': ['取证分析概述/Digital Forensics', '取证原则/依法取证', '电子证据/Evidence', '证据链完整性', '取证流程/Procedure', '证据获取/Acquisition', '内存取证/Memory', 'Winpmem内存获取', 'LiME Linux内存', 'FTK Imager', '磁盘镜像/Disk Image', 'dd命令磁盘复制', 'WinHex十六进制', '证据保存/Preservation', '证据哈希/MD5', 'SHA-1/SHA-256', '证据封存', '取证工具/Forensics Tools', 'Autopsy磁盘分析', 'EnCase取证软件', 'AccessData FTK', 'Volatility内存分析', 'vol.py分析', '进程分析/pslist', '网络连接/netscan', '恶意进程/malfind', '注册表分析/Registry', 'MFT分析/Master File', 'Timeline时间线', 'Windows事件日志', 'Security.evtx', 'System.evtx', 'Application.evtx', '4624登录成功', '4625登录失败', '4648平行提权', '4649重放攻击', '4697服务创建', '4698-4702计划任务', 'PowerShell日志', 'Sysmon系统监控', 'Sysmon日志分析', 'Sysmon配置', 'Linux日志审计', '/var/log/secure', '/var/log/messages', '/.bash_history', 'SSH登录日志', 'Last命令/登录', 'W命令/当前', '进程分析/ps/top', '网络分析/netstat', '文件系统分析', 'Rootkit检测', 'chkrootkit', 'rkhunter', 'Strace系统调用', 'Ltrace库调用', '恶意软件分析/Static', '文件哈希/MD5', 'Strings字符串', 'PE结构/PE Header', '查壳/Packer Detect', 'IDA Pro反汇编', 'Ghidra反编译', '在线沙箱/VirusTotal', 'Any.Run交互沙箱', 'Hybrid Analysis', 'Cuckoo沙箱', '动态分析/Dynamic', 'Process Monitor', 'Process Explorer', 'Autoruns启动项', 'TCPView网络', 'Fiddler抓包', '恶意脚本分析', '混淆分析/Deobfuscation', '勒索软件/Ransomware', 'WannaCry分析', '后门分析/Backdoor', 'WebShell检测/D盾', 'WebShell连接', '冰蝎/Behinder', '溯源分析/Attribution', '攻击者画像', '攻击路径重建', 'IOC指标/MD5/IP', '域名/URL/TTP', '威胁情报/TI', 'MISP情报平台', 'STIX/TAXII', '应急响应/Incident', 'PDCERF模型', '取证报告/Report', '电子证据鉴定']
                },
                '安全监控': {
                    'desc': '安全设备和日志实时监控',
                    'difficulty': 2,
                    'dimensions': ['安全监控概述/Monitoring', '监控目标/可用性', '性能监控/安全', '威胁监控', '主动监控/Active', '被动监控/Passive', '实时监控/Real-time', '日志监控/Log', '流量监控/Flow', '告警监控/Alert', '安全设备监控/设备', '防火墙监控', 'IDS/IPS监控', 'WAF监控', 'SIEM监控', '网络设备监控', '主机监控', '应用监控', '数据库监控', '云安全监控', '监控指标/Metrics', 'CPU使用率', '内存使用率', '磁盘使用率', '网络流量', '连接数', '带宽使用', '延迟/Latency', '丢包率', '攻击事件数', '告警数量', '误报率', '漏报率', 'MTTD检测时间', 'MTTR响应时间', '监控工具/Tools', 'Zabbix监控', 'Prometheus监控', 'Grafana可视化', 'Nagios监控', 'Cacti流量', 'ELK日志分析', 'Splunk日志', 'Loki日志', 'Graylog日志', 'SOC/SIEM', '安全运营平台', '监控数据源/Data Source', '日志收集/Collection', 'Syslog收集', 'Windows Event', 'NetFlow/sFlow', 'IPFIX流数据', 'Snort告警', 'Suricata告警', 'WAF日志', '防火墙日志', 'IDS日志', 'IPS日志', '主机日志', '应用日志', '数据库审计', '云平台日志', 'AWS CloudTrail', '阿里云ActionTrail', '数据归一化/Normalize', '日志格式/JSON', '日志解析/Parser', '正则表达式', 'Grok解析', '字段提取/Extract', '关联分析/Correlation', '规则关联/Rule', '场景关联/Scenario', '用户行为关联', '资产关联', '威胁关联', '告警规则/Alert Rule', '告警级别/严重/高', '中/低/信息', '告警聚合/Aggregation', '告警收敛/Deduplication', '告警抑制/Suppression', '告警升级/Escalation', '告警通知/Notification', '邮件通知', '短信通知', '钉钉通知', '飞书通知', '告警处理流程', '告警确认', '告警响应', '告警关闭', '告警复盘', '监控仪表板/Dashboard', '安全仪表板', '网络仪表板', '主机仪表板', '应用仪表板', '实时大屏', '监控报告/Report', '日报/周报/月报', '安全趋势', '攻击统计', '告警统计', 'SLA报告', '监控优化/Tuning', '监控阈值', '告警阈值', '基线建立', '异常检测', '机器学习', 'UEBA用户行为', '威胁检测/Detection', '异常行为检测', '威胁狩猎/Hunting', '监控团队/SOC Team', '7x24值守', '值班制度', '交接班', '应急响应预案']
                },
                '安全设备': {
                    'desc': '防火墙、IDS/IPS、WAF等设备运维',
                    'difficulty': 2,
                    'dimensions': ['安全设备概述/Security Device', '防火墙/Firewall', '硬件防火墙/F5/思科ASA', '华为防火墙/USG', 'Juniper SRX', 'Fortinet FortiGate', '天融信/启明/绿盟', '防火墙部署/Inline', '旁路部署/Passive', '防火墙配置/Configuration', '安全区域/Zone', 'Trust/Untrust/DMZ', '安全策略/Policy', '源地址/Destination', '服务端口', '用户身份', '时间计划', '策略匹配顺序', '默认策略/Deny All', '会话管理/Session', '状态检测/State', '连接跟踪', 'NAT配置/SNAT/DNAT', '源NAT转换', '目标NAT', '端口映射', '攻击防护/Defense', 'DDoS防护', 'SYN Flood防护', 'ICMP Flood防护', '扫描防护', 'IDS入侵检测/Intrusion', 'IDS类型/NIDS/HIDS', 'NIDS网络IDS', 'HIDS主机IDS', 'Snort IDS', 'Suricata IDS', 'Zeek/Bro网络', 'IDS部署位置/Port Mirror', 'TAP分光器', 'IDS规则/Signature', 'Snort规则编写', '社区规则/ET Open', 'Snort规则/EVENT', '分类/Classtype', 'SID规则ID', '告警分析', 'IPS入侵防御/Intrusion', 'IPS阻断/Inline', 'IPS vs IDS区别', 'IDS签名更新', '误报优化', 'WAF Web应用防火墙', 'ModSecurity', 'WAF规则/OWASP CRS', 'WAF绕过/Bypass', 'WAF部署/Reverse Proxy', '透明部署', 'WAF配置/规则', '防SQL注入', '防XSS攻击', '防CSRF', '防文件上传', 'IPS/IDS联动', '防火墙+IDS', '防火墙+IPS', '安全设备管理', '设备巡检', '设备状态', '健康检查', '性能监控', '日志分析', '设备升级/Patch', '规则库更新', '设备备份/Configuration', '配置变更管理', '设备故障处理', '故障排查', '性能调优', '日志收集', 'Syslog配置', 'SNMP配置', '集中管理/Central', '防火墙集中管理', 'IDS集中管理', 'WAF集中管理', '统一管理平台', '设备监控/Monitor', 'Zabbix监控', 'Prometheus', '设备安全/Hardening', '管理平面安全', '控制平面安全', '数据平面安全', '设备高可用/HA', '防火墙双机主备', '防火墙双机主主', 'IDS HA', 'WAF HA', '会话同步', '配置同步', '故障切换', '设备选型/Selection', '吞吐量/Throughput', '新建连接/Concurrent', '并发会话', '端口密度', '安全功能', '品牌选择', '维保服务']
                },
                '应急响应': {
                    'desc': '安全事件快速响应和处置',
                    'difficulty': 2,
                    'dimensions': ['应急响应概述/Incident Response', 'PDCERF模型/Phase', '六个阶段/准备检测', '遏制恢复/事后', '准备阶段/Preparation', '检测分析/Identification', '遏制阶段/Containment', '根除阶段/Eradication', '恢复阶段/Recovery', '事后总结/Lessons', '应急响应团队/CSIRT', '事件分级/Level', 'P1紧急/P2严重', 'P3一般/P4轻微', '应急响应预案', 'Playbook/剧本', '事件报告/Report', '事件记录/Document', '时间线/Timeline', 'IOC指标/Malware', 'IP/域名/URL', 'TTP战术技术', '应急响应流程', '事件发现/Detection', '事件确认/Confirm', '事件上报/Report', '初步评估/Assess', '预案启动', '应急处置', '事件调查', '遏制控制', '根除清理', '恢复验证', '事件关闭', '事后复盘', '事件类型/Type', '勒索软件/Ransomware', '网络攻击/Network', 'Web攻击/Web', '主机入侵/Host', '数据泄露/Data Breach', 'DDoS攻击', '钓鱼攻击/Phishing', '供应链攻击', '0day漏洞', '社工攻击', 'APT攻击', '应急处置/Sop', '勒索处置', '勒索加密排查', '备份恢复', '密钥获取', '数据恢复', '网络攻击处置', '源IP定位', '流量分析', '攻击阻断', '溯源分析', 'Web攻击处置', '日志分析', '漏洞排查', '攻击路径', '修复验证', '主机入侵处置', '进程排查', '后门排查', '权限排查', '痕迹清理', '系统重装', '数据泄露处置', '泄露评估', '泄露控制', '通知相关方', '溯源分析', '整改措施', 'DDoS处置', '流量清洗', '黑洞路由', '封禁IP', '运营商协助', '应急工具/Tools', '网络分析/Wireshark', 'tcpdump抓包', '进程分析/ps', 'Autoruns启动项', 'Process Monitor', 'Process Explorer', 'Registry分析', 'Memory分析', 'Volatility', '磁盘取证/FTK', '日志分析/Splunk', 'ELK分析', '恶意软件分析', '沙箱分析/VT', '应急报告/Report', '事件报告', '调查报告', '复盘报告', '改进建议', '演练/Exercise', '桌面推演/TTX', '实战演练', '红蓝对抗', 'DDOS演练', '勒索演练']
                },
                '日志分析': {
                    'desc': '安全日志分析和威胁识别',
                    'difficulty': 2,
                    'dimensions': ['日志分析概述/Log Analysis', '日志类型/Log Type', '系统日志/System', '安全日志/Security', '应用日志/Application', '网络日志/Network', 'Web日志/Web Server', '数据库日志/DB', '主机日志/Host', '网络设备日志', '云平台日志', '日志格式/Format', 'Syslog格式', 'Windows Event', 'JSON格式', 'Apache日志', 'Nginx日志', '访问日志/Access', '错误日志/Error', '日志收集/Collection', 'Syslog收集', 'Agent收集', 'Sysmon收集', 'Winlogbeat收集', 'Filebeat收集', '日志存储/Storage', 'Elasticsearch', 'Splunk存储', 'Loki存储', 'Graylog存储', 'HDFS存储', '日志解析/Parsing', '正则表达式', 'Grok解析', 'Logstash解析', '字段提取/Extract', '字段标准化', '字段映射/Mapping', '日志关联/Correlation', '告警规则/Rule', '时间关联', 'IP关联', '用户关联', '资产关联', '攻击关联', '威胁场景/Scenario', '暴力破解/Brute Force', 'SQL注入/SQLi', 'XSS攻击', 'webshell上传', '内网渗透', '横向移动', '权限提升', '数据外发', '隧道通信', '隐蔽通信', '异常行为/Abnormal', '异常登录', '异常访问', '异常流量', '异常进程', '异常网络连接', '告警分析/Alert', '告警确认/Confirm', '告警分类', '告警优先级', '告警聚合', '告警关联', '误报识别', '真实告警', '分析方法/Method', '关键字分析', '统计分析', '关联分析', '机器学习', '异常检测', 'UEBA分析', '用户行为分析', '实体行为分析', 'IOC搜索', 'IP搜索/Domain', 'Hash搜索', 'URL搜索', '日志可视化', '时间线/Timeline', '统计图表', '关系图谱', '地图分布', '热力图', '日志搜索/Search', '全文搜索', '字段搜索', '正则搜索', '模糊搜索', '复合搜索', '日志过滤/Filter', '时间过滤', '字段过滤', '事件过滤', '日志监控/Monitor', '实时监控', '告警监控', '趋势监控', 'SIEM平台/Splunk', 'ELK Stack', 'IBM QRadar', 'Azure Sentinel', '阿里云SLS', '腾讯云SOC', '日志分析工具', 'Splunk搜索', 'Kibana搜索', 'Windows事件查看器', 'Linux journalctl', 'grep搜索', 'awk分析', '日志报告/Report', '日志报表', '安全周报', '威胁分析报告', '合规审计报告', '日志保留/Retention', '日志归档/Archive', '日志合规/GDPR', '日志脱敏/Masking']
                },
                '漏洞管理': {
                    'desc': '漏洞扫描和修复跟踪',
                    'difficulty': 2,
                    'dimensions': ['漏洞管理概述/Vulnerability', '漏洞生命周期/Lifecycle', '漏洞发现/Discovery', '漏洞验证/Validation', '漏洞评级/Severity', '漏洞修复/Remediation', '漏洞验证/Verify', '漏洞关闭/Close', '漏洞扫描/Scanning', '漏洞扫描器/Tool', 'Nessus扫描', 'OpenVAS扫描', 'Qualys扫描', 'Nexpose扫描', '绿盟漏扫', '启明漏扫', '安恒漏扫', 'Acunetix Web', 'AWVS Web扫描', 'Nikto Web扫描', 'WPScan CMS', '漏洞分类/Category', '系统漏洞/OS', '应用漏洞/App', '配置漏洞/Config', '弱口令/Weak Password', '敏感信息泄露', '漏洞评级/CVSS', 'CVSS评分', '严重/High', '高危/Medium', '中危/Medium', '低危/Low', '信息级/Info', 'CVE漏洞库/MITRE', 'CVE编号', 'NVD/NIST', 'CNVD/中国', 'CNNVD/中国', '漏洞库管理', '漏洞库同步', '漏洞报告/Report', '漏洞详情', '影响范围', '修复建议', 'CVE关联', '漏洞跟踪/Tracking', '工单系统', 'JIRA工单', '漏洞处置单', '处置流程', '责任划分', '修复期限/SLA', '紧急漏洞/P1', '高危漏洞/P2', '中危漏洞/P3', '低危漏洞/P4', '漏洞修复/Remediation', '系统补丁/Patch', 'Windows Update', 'Linux yum/apt', '应用升级/Update', '配置修复/Config', 'WAF防护', '网络隔离', '访问控制', '禁用服务', '删除组件', '版本升级', '漏洞验证/Vefification', '复测/Retest', '验证通过', '验证失败', '漏洞关闭', '漏洞复盘', '漏洞统计分析', '漏洞趋势', '漏洞分布', '漏洞闭环率', '平均修复时间', '漏洞管理系统', 'Virbox/CVM', '防漏洞平台', '漏洞管理流程', 'ISO 27001要求', '漏洞合规/Compliance', '等保漏洞', '漏洞响应/VT Response', '0day响应', '紧急响应流程', '补丁管理/Patch', 'WSUS补丁', ' Lansweeper', 'SCCM补丁', '补丁测试', '补丁分发', '补丁回滚', '补丁管理最佳实践']
                },
                'SIEM': {
                    'desc': '安全信息与事件管理系统',
                    'difficulty': 3,
                    'dimensions': ['SIEM概述/Security Information', 'SIEM架构/Architecture', 'SIEM组件/Components', '日志收集/Collection', '数据采集/Acquisition', '数据处理/Processing', '数据存储/Storage', '数据分析/Analytics', '告警管理/Alerting', '报告生成/Reporting', 'SIEM功能/Features', '日志聚合/Aggregation', '日志标准化/Normalize', '实时监控/Real-time', '关联分析/Correlation', '威胁检测/Detection', '用户行为分析/UEBA', '异常检测/Anomaly', '机器学习/ML', 'SIEM产品/Products', 'Splunk企业安全', 'IBM QRadar', 'ArcSight', 'Microsoft Sentinel', 'Azure Sentinel', '阿里云SLS', '腾讯云SOC', '华为云MRS', '绿盟ESM', '启明天机', 'Splunk安装/部署', 'Splunk Forwarder', 'Heavy Forwarder', 'Universal Forwarder', 'Splunk索引/Index', '索引配置', '热温冷索引', 'Splunk搜索/Search', 'SPL搜索语言', '字段提取/Field', 'stats统计', 'chart图表', 'timechart时序', 'transaction事务', 'lookup查找', 'eval计算', 'rex正则', 'Splunk告警/Alert', '实时告警', '保存搜索', '触发动作', '邮件告警', 'Webhook', '脚本动作', 'Splunk仪表板/Dashboard', '可视化/Viz', '图表类型', '权限控制', 'Splunk App/应用', 'ES App企业安全', 'Splunk TA/技术应用', 'Splunk CIM通用信息', '数据模型/Data Model', '加速数据模型', 'Splunk机器学习', 'MLTK', '异常检测', '预测分析', 'SIEM部署/Deployment', '日志源集成', '数据源配置', 'Forwarder部署', '索引规划', '存储规划', '性能规划', '数据源接入/Data Source', 'Windows日志', 'Linux Syslog', '网络设备', '防火墙', 'IDS/IPS', 'WAF', 'Web服务器', '数据库', '应用程序', '云平台/AWS/Azure', '容器/Kubernetes', 'SIEM规则开发', '关联规则/Correlation', '检测规则', '场景规则', 'UEBA规则', 'MITRE ATT&CK', '战术/Techniques', '告警/Tactics', '规则优化', '误报处理', '规则维护', 'SIEM日志源', '日志类型映射', '日志字段映射', 'CIM映射', 'SIEM报告/Report', '合规报告/PCI', 'SOC报告', '安全态势', 'KPI指标', '趋势分析', 'SIEM运营/Operation', '告警分诊/Triage', '告警调查', '告警响应', '告警升级', 'MTTD/MTTR', 'SIEM调优/Tuning', '基线建立', '阈值调整', '规则优化', '场景优化', 'SIEM性能/Performance', '数据量评估', '搜索性能', '告警性能', '存储容量', '扩展性/Scalability', '集群部署/Cluster', '分布式搜索', '高可用/HA', '数据保留/Retention', '数据归档/Archive', '数据删除/Purge', '合规保留期']
                },
                'SOC': {
                    'desc': '安全运营中心建设',
                    'difficulty': 3,
                    'dimensions': ['SOC概述/Security Operations', 'SOC定义/Center', 'SOC目标/Goals', 'SOC范围/Scope', 'SOC成熟度/Capability', 'SOC类型/内部/外包', '自建SOC/内部', '托管SOC/MSSP', '混合SOC/Hybrid', '云SOC/Cloud', 'SOC架构/Architecture', '组织结构/Organization', 'SOC团队/Team', '安全分析师/SOC', '高级分析师/Level 2', '安全专家/Level 3', '安全运营/SO', '安全工程师', '安全管理员', '事件响应/IR', '威胁情报/TI', '安全架构/Architecture', 'SOC流程/Process', '日常运营/Daily', '资产盘点', '漏洞扫描', '日志审计', '告警监控', '事件调查', '报告输出', '变更管理', '应急响应', 'P1紧急事件', 'P2严重事件', 'P3一般事件', 'P4轻微事件', '升级流程/Escalation', '值班制度/Shifts', '7x24值守', '交接班', 'On-call待命', 'KPI指标/SOC KPI', 'MTTD检测时间', 'MTTR响应时间', '告警处理时长', '事件闭环率', '误报率', '漏报率', 'SLA达成率', '安全运营指标', 'SOC技术平台/Tech', 'SIEM平台', '资产管理系统', 'CMDB配置', '漏洞管理平台', '威胁情报平台', '工单系统', '知识库/Knowledge', 'SOSOC平台', 'SOAR平台', 'UEBA平台', 'NDR平台', 'EDR平台', 'XDR平台', '资产发现/Discovery', '资产识别/Identification', '资产分类/Classification', '资产变更/Mange', '资产监控/Monitor', '威胁情报/CTI', 'IOC指标', '威胁情报源', '开源情报/OSINT', '商业情报', '战略情报', '战术情报', '攻击者画像', 'TTP情报', 'MITRE ATT&CK', '情报关联', '情报共享', '数据源/Data Source', '网络流量/NDR', '主机日志/EDR', '端点检测/EDR', '云安全/CWPP', 'CASB云安全', '邮件安全/SEG', 'Web安全/WAF', '身份安全/IAM', '数据库审计/DAM', '网络设备', '安全设备', '应用系统', 'SIEM集成', '告警集成', '告警源/Alert Source', '告警分类/Category', '告警级别/Severity', '告警分诊/Triage', '分诊规则', '优先级判定', '责任划分', '告警调查/Investigation', '调查流程', '调查工具', '调查模板', '告警响应/Response', '响应流程', '响应动作', '响应工具', '剧本/SOAR Playbook', '自动化响应', '告警升级/Escalation', '升级规则', '升级路径', '告警关闭/Close', '关闭原因', '文档记录', 'KPI统计', '报告/Reporting', '日报/Daily', '周报/Weekly', '月报/Monthly', '季报/Quarterly', '年报/Annual', '合规报告', '事件报告', '趋势分析', '安全态势/Situation', '仪表板/Dashboard', '态势感知', '风险评估', 'SOC建设流程', '需求分析', '方案设计', '平台选型', '部署实施', '团队建设', '流程制定', '运营优化', '持续改进', 'SOC评估/Capability', '成熟度评估', '有效性验证', 'Red Team测试', '演练/Exercise', '桌面推演/TTX', '红蓝对抗', '威胁狩猎/Hunting', '主动威胁发现', 'IoC狩猎', 'TTP狩猎', '异常行为', '狩猎流程', '狩猎报告', 'SOC合规/Compliance', 'ISO 27001', 'PCI DSS', 'GDPR', '等保2.0', '分保']
                },
                '威胁情报': {
                    'desc': '收集和应用威胁情报',
                    'difficulty': 3,
                    'dimensions': ['威胁情报概述/Threat Intelligence', '情报分类/Classification', '战略情报/Strategic', '战术情报/Tactical', '运营情报/Operational', '技术情报/Technical', '情报生命周期/Intelligence', '规划指导/Direction', '收集/Collection', '处理/Processing', '分析/Analysis', '传播/Dissemination', '反馈/Feedback', '战略情报/Strategic', '高管简报', '风险评估', '趋势分析', '行业威胁', '攻击趋势', 'APT组织', '运营情报/Operational', '活动跟踪', ' кампания', '攻击者动机', '攻击时机', '目标情报', '战术情报/Tactical', 'TTPs战术技术', 'MITRE ATT&CK', '攻击向量', '漏洞利用', '恶意软件', '攻击工具', '技术情报/Technical', 'IOC指标', 'IP地址/IP', '域名/Domain', 'URL地址', '文件哈希/MD5', 'SHA-1/SHA-256', '文件特征/Signature', 'C2域名', '僵尸网络', '恶意软件家族', 'URL黑名单', 'IP黑名单', '威胁情报源/Sources', '开源情报/OSINT', 'AlienVault OTX', 'VirusTotal', 'URLhaus', 'Malware Bazaar', 'AbuseIPDB', 'ThreatFox', 'Cisco Talos', 'Recorded Future', 'Mandiant', 'CrowdStrike', 'Palo Alto', 'IBM X-Force', '微软威胁情报', '卡巴斯基威胁', '奇安信威胁', '阿里云威胁', '腾讯威胁', '社区情报', 'ISAC信息共享', 'MISP平台/MISP', 'MISP安装/部署', 'MISP事件/Event', 'MISP属性/Attribute', 'MISP Galaxy', 'MISP Tagging', 'MISP分享', '威胁情报平台/TIP', 'AlienVault USM', 'ThreatConnect', 'Anomali', ' Recorded Future', 'ThreatQuotient', '微步在线/TI', '盛邦威胁', '情报关联/Enrichment', 'IP画像', '域名分析', 'URL分析', 'Hash分析', '文件分析', '邮件分析', '关联分析', '团伙分析', 'APT追踪', 'APT组织/APT', 'APT28/Fancy Bear', 'APT29/Cozy Bear', 'Lazarus Group', 'APT41/BARIUM', '海莲花/OceanLotus', 'DarkHotel', 'Patchwork', '蔓灵花/TAPT', 'APT组织战术', '攻击链/CK/Kill Chain', '侦察/Reconnaissance', '武器化/Weaponization', '投递/Delivery', '利用/Exploitation', '安装/Installation', '命令控制/C2', '行动/Action', '钻石模型/Diamond', '对手能力', '对手意图', '基础设施', '受害者', 'ATT&CK框架/MITRE', '战术/Tactics/TA', '技术/Techniques', '子技术/Sub-techniques', '程序/Procedures', '防御规避/Defense', '持久化/Persistence', '权限提升/Privilege', '侦察/Recon', '资源开发/Resource', '初始访问/Initial', '执行/Execution', '收集/Collection', '命令控制/C&C', '数据泄露/Exfiltration', '影响/Impact', '情报应用/Application', 'SIEM集成', '规则编写', '告警关联', 'EDR集成', '检测规则', '响应剧本', '防火墙集成', '封锁规则', 'WAF集成', '防护规则', 'SOAR集成', '自动化响应', '情报订阅', '情报推送', '情报搜索', 'IOC搜索', '批量查询', '追踪监控', '情报评估/Evaluation', '准确性/Accuracy', '及时性/Timeliness', '相关性/Relevance', '完整性/Completeness', '可操作性/Actionable', '情报质量', '情报生产/Production', '情报来源', '采集能力', '分析能力', 'STIX/TAXII标准', 'STIX对象/Object', 'Indicator指标', 'Malware恶意软件', 'Attack Pattern', 'Course of Action', 'Threat Actor', '报告/Report', '威胁报告', 'APT报告', '行业报告', 'IOC报告']
                },
                '安全加固': {
                    'desc': '系统和应用安全配置',
                    'difficulty': 3,
                    'dimensions': ['安全加固概述/Hardening', '安全基线/Baseline', 'CIS Benchmark', '等保合规加固', '加固流程/Process', '风险评估/Risk', '加固实施/Remediation', '验证检查/Verify', '加固文档/Documentation', 'Windows加固/Windows', '账户安全/Account', '密码策略/Password', '复杂度要求', '密码长度', '过期时间', '锁定策略', 'Guest禁用', 'Administrator重命名', '审核策略/Audit', '安全选项/Options', '本地策略', '禁用不必要的服务', '服务列表', '服务权限', '端口管理/Port', 'Telnet禁用', 'NetBIOS禁用', 'SMBv1禁用', '防火墙配置/Windows', 'Windows Firewall', '入站规则', '出站规则', '默认拒绝', 'PowerShell安全', 'Execution Policy', '脚本签名', '系统更新/Patch', 'WSUS更新', '自动更新', '补丁测试', '权限加固/ACL', 'NTFS权限', '共享权限', 'Takeown', 'icacls', '加密/BitLocker', 'EFS加密', 'TPM芯片', '启动安全/UEFI', 'Secure Boot', 'RDP安全', 'NLA要求', '加密级别', 'Linux加固/Linux', 'SELinux/AppArmor', 'SELinux模式', 'SELinux上下文', 'chcon/restorecon', 'Policy/策略', '账号安全/PAM', 'passwd/shadow', 'wheel组/sudo', 'SSH加固/SSH Hardening', 'SSH密钥', 'SSH端口', '禁止密码', 'PermitRootLogin', 'TCPWrappers', 'hosts.allow/deny', '防火墙/iptables', 'firewalld', 'ufw/Ubuntu', 'iptables规则', 'Chain规则', 'INPUT/OUTPUT', 'ACCEPT/DROP', '服务加固/Apache', 'Apache安全', '版本隐藏', '目录禁用', 'HTTPS配置', 'Nginx加固', 'SSL配置', '安全头', 'MySQL加固', '安全安装', '权限最小', '远程访问', 'SSL连接', 'Redis加固', '密码认证', '绑定地址', '危险命令', '禁用命令', 'Tomcat加固', '版本隐藏', 'Manager弱口令', 'SSL配置', '中间件加固/JBoss', 'WebLogic加固', 'WebSphere加固', '数据库加固/MySQL', 'PostgreSQL加固', 'Oracle加固', 'MongoDB加固', 'SSL/TLS加固', 'TLS版本', '证书配置', 'Cipher Suite', 'HSTS头', '协议加固', '漏洞加固/Vuln', '漏洞扫描', '补丁修复', '配置修改', 'WAF防护', '虚拟补丁', '等保测评/Compliance', '等保2.0', '三级系统', '四级系统', '控制点', '测评指标', '弱口令检查', '漏洞扫描', 'CIS扫描', '安全配置/Config', '安全配置核查', '配置基线', '自动化核查', 'Ansible加固', '脚本加固', 'DevSecOps', '镜像安全', '容器安全', 'K8s安全', '云安全加固/AWS', '云安全/Azure', '云安全/GCP', 'IAM安全', 'VPC安全', '安全组', 'NACL', '加固验证/Verify', '基线核查', '配置审计', '渗透测试', '漏洞复查']
                }
            }
        }
    },
    '物联网工程': {
        '嵌入式工程师': {
            'description': '开发嵌入式系统，编写硬件驱动，实现设备功能。',
            'skills': {
                'C': {
                    'desc': '嵌入式开发底层编程语言',
                    'difficulty': 1,
                    'dimensions': ['数据类型(int/float/char/指针/结构体)/sizeof/类型转换', '控制流程(if/switch/for/while/do-while)', '函数定义/参数传递(值传递/指针传递/数组传递)/递归', '指针(一级指针/二级指针/函数指针/指针数组/数组指针)', '数组(一位数组/二维数组/字符串处理)/strlen/strcpy/strcat/strcmp', '内存管理(malloc/free/realloc/calloc)/内存泄漏/段错误', '预处理指令(#define/#include/#ifdef/条件编译)', '位运算(&/|/^/~/<</>>)/位域/字节序/大小端', '关键字(const/volatile/static/extern/register)', '标准库函数(printf/scanf/memcpy/memset/file操作)', '嵌入式C扩展(register/intrinsic/段属性__attribute__)', '代码规范(MISRA-C/编码规范)/编译优化']
                },
                'C++': {
                    'desc': '面向对象嵌入式开发',
                    'difficulty': 1,
                    'dimensions': ['C++基础语法/命名空间namespace/作用域resolution', '类和对象(构造函数/析构函数/拷贝构造/移动构造)', '面向对象特性(封装/继承/多态)/虚函数/纯虚函数/抽象类', '访问控制(public/private/protected)/友元/friend', '运算符重载/类型转换运算符/转换构造函数', '模板(函数模板/类模板)/模板特化/偏特化', '智能指针(auto_ptr/shared_ptr/unique_ptr/weak_ptr)', 'STL容器(vector/list/map/set)/迭代器/算法', '异常处理(try/catch/throw)/异常规格/noexcept', 'C++11新特性(nullptr/auto/范围for/lambda/decltype)', '移动语义(移动构造/移动赋值/std::move)/右值引用', '嵌入式C++优化(RTTI关闭/异常关闭/模板实例化控制)']
                },
                'ADC/DAC': {
                    'desc': '模数/数模转换',
                    'difficulty': 2,
                    'dimensions': ['ADC原理(逐次逼近/双积分/ sigma-delta/并行比较)', '分辨率(8/10/12/16位)/量化误差/LSB计算', '采样定理/奈奎斯特频率/混叠/抗混叠滤波', '采样率/转换时间/吞吐率/单通道/多通道扫描', '参考电压/Vref/基准源/内部基准/外部基准', '输入阻抗/输入类型(单端/差分)/输入范围', 'DMA传输/中断模式/轮询模式/连续转换', '校准(零点校准/满量程校准/自校准)', 'DAC原理(权电阻网络/梯形网络/PWM输出)', 'DAC分辨率/输出范围/建立时间/压摆率', '缓冲输出/无缓冲输出/功率放大', 'ADC/DAC精度指标(INL/DNL/ENOB/SINAD/ SNR/THD)', '实际项目(热敏电阻/称重传感器/音频采集/电压监测)']
                },
                'ESP32': {
                    'desc': '乐鑫WiFi/蓝牙芯片开发',
                    'difficulty': 2,
                    'dimensions': ['ESP32架构(Xtensa dual-core/单核版本)/内存布局', '开发环境(ESP-IDF/VSCode/Arduino)/CMake构建', 'GPIO配置/输入输出/上下拉/开漏/推挽', 'WiFi Station/SoftAP模式/WiFi事件/WiFi配网', '蓝牙BLE广播/扫描/连接/Characteristic/Service', 'MQTT客户端/TCP/UDP/HTTP/OTA升级', 'FreeRTOS任务创建/任务优先级/队列/信号量/互斥量', '定时器(硬件定时器/软件定时器)/PID控制', 'ADC采集(两路ADC)/DAC输出/PWM输出', '存储(NVS/FFS/SPI Flash)/文件系统', '低功耗(浅睡眠/深睡眠/唤醒源/RTC外设)', '外设(I2C/SPI/UART/I2S/LEDC/脉冲计数器)', '错误处理/日志系统/看门狗/调试技巧']
                },
                'GPIO': {
                    'desc': '通用输入输出控制',
                    'difficulty': 2,
                    'dimensions': ['GPIO结构(输入缓冲/输出驱动/施密特触发器)', '工作模式(输入/输出/复用/Analog)', '输入类型(浮空输入/上拉输入/下拉输入)', '输出类型(推挽输出/开漏输出)/线与逻辑', '推挽输出/开漏输出区别/上拉电阻选择', 'GPIO翻转速度(2/10/50MHz)/负载电容', '复用功能(AF0-15)/外设映射/重映射', '外部中断(EXTI)/中断线/边沿触发/电平触发', 'NVIC中断控制器/中断优先级/中断嵌套', 'GPIO读写操作/BSRR寄存器/ODR寄存器', '防抖处理(硬件消抖/软件延时)/滤波', 'GPIO扩展(74HC595/74HC165/IO扩展芯片)', '实际应用(按键/LED/蜂鸣器/继电器/光耦隔离)']
                },
                'I2C/SPI/UART': {
                    'desc': '常用硬件通信协议',
                    'difficulty': 2,
                    'dimensions': ['I2C总线/起始位/停止位/应答位/ACK/NACK', 'I2C地址(7位/10位)/广播地址/从机地址', 'I2C数据传输/主从模式/时钟同步/线与', 'I2C速度(标准100k/快速400k/快速+1M/高速3.4M)', 'I2C重载/重复起始/SCL stretching', 'I2C EEPROM读写(AT24Cxx)/页写入/随机读取', 'I2C传感器(SHT20/MPU6050/ADS1115/BMP280)', 'SPI四线(SCLK/MOSI/MISO/SS)/三线/两线', 'SPI模式(CPOL/CPHA)/模式0/1/2/3/时钟极性相位', 'SPI时钟分频/最高速度/数据传输顺序(MSB/LSB)', 'SPI全双工/半双工/DMA传输/中断模式', 'UART异步/起始位/数据位/校验位/停止位', 'UART波特率(9600/115200/自定义)/误差容忍', 'UART流控(RTS/CTS)/RS232/RS485/TTL电平', 'DMA传输/环形缓冲区/队列处理']
                },
                'PWM': {
                    'desc': '脉冲宽度调制',
                    'difficulty': 2,
                    'dimensions': ['PWM原理/占空比/频率/分辨率', 'PWM定时器结构(计数器/预分频/自动重载)', 'PWM模式(边沿对齐/中心对齐)/计数方式', 'PWM输出通道/输出比较/死区/互补输出', 'PWM频率计算/预分频系数/重装载值', 'PWM分辨率(位数)/精度/频率关系', 'PWM占空比计算/CCR寄存器/Duty Cycle', 'PWM初始化配置/使能/停止', '呼吸灯效果/PWM调光/调速/调压', 'PWM驱动电机(L298N/TB6612)/H桥', 'PWM舵机控制(50Hz/0.5-2.5ms)/角度计算', 'PWM声音输出/蜂鸣器/音频PWM', 'PWM滤波/积分电路/伪DAC输出', 'PWM编码器解码/红外遥控/遥控应用']
                },
                'RTOS': {
                    'desc': '实时操作系统开发和任务调度，如FreeRTOS',
                    'difficulty': 2,
                    'dimensions': ['实时操作系统概念/硬实时/软实时/调度算法', 'FreeRTOS架构/任务/队列/信号量/互斥量', '任务创建(xTaskCreate/vTaskDelete)/任务函数', '任务状态(运行/就绪/阻塞/挂起)/状态转换', '任务优先级/优先级翻转/优先级继承', '时间片轮转/心跳时钟/Tick中断', 'vTaskDelay()/vTaskDelayUntil()/相对延时/绝对延时', '队列(xQueueCreate/发送/接收)/队列长度/数据大小', '信号量(二进制/计数)/xSemaphoreGive/xSemaphoreTake', '互斥量/递归互斥量/优先级继承/锁', '事件组(EventGroup)/事件标志等待/事件触发', '软件定时器/一次性/周期性/回调函数', '任务通知(Task Notify)/直接任务通知', '内存管理/heap_1-5/堆分配策略', '临界段/portENTER_CRITICAL/中断保护', '队列/消息队列/邮箱/互斥锁的选择', '低功耗(idle任务/Tickless模式)']
                },
                'STM32': {
                    'desc': '意法半导体ARM Cortex-M系列开发',
                    'difficulty': 2,
                    'dimensions': ['STM32产品线(F0/F1/F3/F4/F7/H7/L系列)', 'Cortex-M内核(寄存器/堆栈/MSP/PSP)', '启动文件(startup.s)/中断向量表/复位流程', '时钟系统(HSE/LSE/PLL/时钟树)', 'GPIO配置/AFIO复用/EXTI中断', 'NVIC中断控制器/优先级分组/外部中断', 'SysTick定时器/系统滴答/延时函数', 'USART/UART通信/printf重定向/DMA接收', 'SPI/I2C外设/主机从机模式', '定时器(TIM1-15)/输入捕获/输出比较/PWM', 'ADC/DAC配置/多通道/DMA/转换时间', 'DMA控制器/通道/传输模式/循环模式', '看门狗(IWDG/WWDG)/喂狗/复位', 'RTC实时时钟/闹钟/备份寄存器', 'PWR电源管理/睡眠/停机/待机模式', '固件库/HAL库/LL库/CubeMX配置', 'FLash读写/OPTION字节/写保护']
                },
                '调试工具': {
                    'desc': '示波器、逻辑分析仪、JTAG调试器',
                    'difficulty': 2,
                    'dimensions': ['示波器类型(模拟/数字)/带宽/采样率/存储深度', '示波器触发(边沿/脉宽/斜率/I2C/SPI触发)', '示波器探头(1x/10x/电流探头)/接地弹簧/补偿', '时基/垂直灵敏度/触发位置', '示波器测量(幅值/频率/周期/占空比/上升下降沿)', '示波器协议解码(I2C/SPI/UART/解码功能)', '逻辑分析仪采样/协议解码/触发条件', 'Saleae逻辑分析仪/脉宽触发/异步协议解码', 'JTAG接口(TDI/TDO/TCK/TMS/TRST)', 'SWD调试接口(SWDIO/SWCLK/调试接口)', 'ST-Link/J-Link/Debug配置/OpenOCD', 'GDB调试/断点/单步/变量查看/内存查看', '串口调试(Printf重定向/日志输出)', '硬件调试技巧(隔离/分段排除/信号完整性)', '电磁干扰/接地/屏蔽/滤波/去耦电容']
                },
                'ARM': {
                    'desc': 'ARM处理器架构和编程',
                    'difficulty': 3,
                    'dimensions': ['ARM架构版本(ARMv6/7/8/9/10/11)/Cortex-A/R/M', 'ARM指令集(Thumb/Thumb-2/ARM)/32位/16位混合', '工作模式(用户/系统/管理/中止/未定义/IRQ/FIQ)', '寄存器组(R0-R15/CPSR/SPSR)', 'ARM指令格式/数据处理/分支/Load-Store', 'Thumb指令集/条件执行/协处理器指令', '寻址方式(立即数/寄存器/相对/基址偏移)', '流水线(3级/5级/7级/9级)/流水线冲突/分支预测', 'MMU内存管理/页表/虚拟地址/物理地址', 'Cache缓存/I-Cache/D-Cache/缓存一致性', '协处理器/CP15/系统控制', '中断机制(IRQ/FIQ)/向量表/向量地址', 'ARM汇编编程/伪指令/宏/程序结构', 'ATPCS调用规范/参数传递/栈帧', 'NEON SIMD指令/浮点单元VFP', 'TrustZone安全/ARM Trust firmware']
                },
                '嵌入式Linux': {
                    'desc': 'Linux内核裁剪和驱动开发',
                    'difficulty': 3,
                    'dimensions': ['嵌入式Linux构成(Bootloader/Kernel/Rootfs)', 'Bootloader(U-Boot)/启动流程/环境变量', '交叉编译工具链(gcc/ld/objcopy/ar)', 'Makefile/CMake/Kconfig/内核配置menuconfig', 'Linux内核源码结构/子系统', '内核配置裁剪/驱动模块编译/内核编译', '字符设备驱动/设备号/文件操作接口', '块设备/网络设备/平台设备驱动', 'GPIO子系统/LED子系统/按键子系统', '设备树(Device Tree)/.dts/.dtsi/节点属性', 'I2C子系统/适配器/设备驱动分离', 'SPI子系统/Flash驱动/W25Qxx', '文件系统(JFFS2/YAFFS2/UBIFS/EXT4/FAT)', 'BusyBox/根文件系统构建/buildroot', 'Linux内核模块/insmod/rmmod/modprobe/lsmod', 'Misc设备/平台驱动模型/proc/sys文件系统', '中断处理/顶半部/底半部/workqueue/软中断/tasklet', '同步机制(自旋锁/互斥锁/信号量/ Completion)', 'DMA驱动/scatter-gather', '用户空间与内核空间通信(ioctl/netlink)']
                },
                '汇编': {
                    'desc': '底层硬件操作和性能优化',
                    'difficulty': 3,
                    'dimensions': ['汇编语言基础/指令/操作数/寻址模式', 'ARM汇编指令/数据处理/分支/Load-Store', 'Thumb汇编指令/Thumb-2指令集', 'x86汇编基础/寄存器/指令格式', 'AT&T语法/Intel语法/汇编器(AS/GAS/NASM/MASM)', '伪指令(.global/.section/.word/.byte/.align)', '子程序调用/栈帧/参数传递/返回值', 'C语言内联汇编(__asm__)/asm volatile', '混合编程(C调用汇编/汇编调用C)', '汇编优化/指令调度/寄存器分配', 'SIMD指令(SSE/AVX/NEON)/并行计算', 'DSP汇编/信号处理优化', '反汇编/逆向分析/IDA Pro/Ghidra', '固件分析/病毒分析/漏洞挖掘', 'ARM伪指令(LDR/ADR/ADRL)/位置无关代码', '链接脚本/段属性/启动代码']
                },
                '硬件驱动': {
                    'desc': '设备驱动开发和硬件接口编程',
                    'difficulty': 3,
                    'dimensions': ['硬件接口(GPIO/UART/I2C/SPI/CAN/USB)', '硬件时序/信号分析/协议解析', '寄存器操作/位操作/读写时序图', '裸机驱动/轮询/中断/DMA模式', 'Linux字符设备驱动/file_operations', '设备号/自动创建设备节点/devfs', '平台设备驱动/platform_driver', '设备树匹配/OF匹配/compatible属性', 'I2C设备驱动/i2c_driver/i2c_client', 'SPI设备驱动/spi_driver/spi_device', '中断处理程序/request_irq/free_irq', '工作队列/tasklet/软中断/threaded_irq', '同步互斥(自旋锁/互斥锁/信号量)', 'DMA传输/缓存一致性/dmaengine', '电源管理/ suspend/resume/ runtime_pm', '设备驱动调试(printk/dev_err/proc)']
                }
            }
        },
        'IoT开发工程师': {
            'description': '开发物联网应用，实现设备连接、云端数据传输和控制。',
            'skills': {
                'Python': {
                    'desc': '物联网应用层开发语言',
                    'difficulty': 1,
                    'dimensions': ['Python基础语法/数据类型/控制流程', '函数定义/参数传递/返回值/匿名函数lambda', '模块导入/包管理/__name__ == __main__', '文件操作/异常处理/上下文管理器', '网络编程(socket/TCP/UDP/HTTP客户端)', '多线程/多进程/异步IO(asyncio/aiohttp)', 'JSON/XML解析/数据序列化', 'Python标准库(datetime/re/collections)', 'pip包管理/虚拟环境/requirements.txt', 'Micropython/TensorFlow Lite/嵌入式Python', 'GPIO控制(RPi.GPIO/GPIO Zero)/传感器读取', 'MQTT客户端(paho-mqtt)/数据上报', 'REST API调用/云平台SDK/requests库']
                },
                'CoAP': {
                    'desc': '受限应用协议，适用于低功耗设备',
                    'difficulty': 2,
                    'dimensions': ['CoAP协议原理/与HTTP对比/设计目标', 'CoAP消息类型(CON/ NON/ACK/RST)', 'CoAP请求方法(GET/POST/PUT/DELETE)', 'URI路径/Query参数/载荷格式', 'CoAP选项(Content-Format/ETag/If-Match)', '消息ID/令牌(Token)/可靠性保障', 'UDP传输/资源观察(Observe)/订阅', '块传输(Blockwise)/分片传输', '代理/缓存/网关(CoAP-HTTP互转)', 'CoAP安全(DTLS)/预共享密钥/证书', 'AIoT设备应用/轻量化优势', 'Libcoap/Californium/aiocoap库', 'CoAP服务器/客户端实现']
                },
                'HTTP/REST': {
                    'desc': 'Web API通信',
                    'difficulty': 2,
                    'dimensions': ['HTTP协议原理/请求响应模型/状态码', 'HTTP方法(GET/POST/PUT/DELETE/PATCH)', '请求头/响应头/Content-Type', 'URL编码/Query参数/Path参数', 'JSON数据交换/XML数据交换', 'RESTful API设计规范/资源命名', 'API版本管理/错误处理/分页', 'HTTP持久连接/压缩/缓存控制', '身份验证(Bearer Token/API Key)', 'TLS/HTTPS安全传输', '物联网平台API/设备影子/Topic', 'Webhook回调/订阅推送', 'HTTP客户端库(requests/httpx/aiohttp)']
                },
                'MQTT': {
                    'desc': '物联网轻量级消息传输协议',
                    'difficulty': 2,
                    'dimensions': ['MQTT协议原理/发布订阅模式/消息代理', 'MQTT连接流程/Connect报文/心跳', 'QoS等级(QoS0/1/2)/服务质量/消息到达', 'MQTT Topic(主题)/通配符(+/#)', '遗嘱消息(Will)/保留消息(Retained)', '客户端ID/用户名/密码/认证', 'MQTT TLS加密/证书认证', 'MQTT Broker(Mosquitto/EMQX/ActiveMQ)', 'QoS选择策略/网络质量考虑', 'MQTT协议升级(MQTT5.0)/用户属性', '开源协议(RTSP/RTMP对比)', 'MQTT.fx/ MQTT Explorer调试工具', 'MQTT-SN(传感器网络版)/网关转换']
                },
                '云平台': {
                    'desc': '阿里云IoT、AWS IoT、Azure IoT等平台',
                    'difficulty': 2,
                    'dimensions': ['阿里云IoT/Link Platform/设备接入/物模型', '阿里云API/AMQP/微消息队列/规则引擎', 'AWS IoT Core/Device Shadow/Certificate', 'AWS Greengrass/边缘计算/MQTT Bridge', 'Azure IoT Hub/设备预配服务/DPS', 'Azure IoT Edge/模块部署/流分析', '腾讯云IoT/IoT Explorer/规则引擎', '百度天工IoT/时序数据库TSDB', 'OneNET中国移动/设备接入/应用使能', '云平台设备SDK/认证机制/连接协议', '设备影子/状态同步/期望属性', 'OTA升级/远程配置/远程诊断', '规则引擎/SQL处理/数据转发']
                },
                '传感器': {
                    'desc': '温湿度、光照、加速度等各类传感器数据采集',
                    'difficulty': 2,
                    'dimensions': ['传感器分类(模拟/数字/有源/无源)', 'I2C传感器/SPI传感器/UART传感器', '温湿度传感器(DHT11/DHT22/SHT20/BME280)', '光照传感器(BH1750/BH1750/光敏电阻)', '加速度计(MPU6050/ADXL345)/陀螺仪/姿态角', '气压传感器(BMP280/BMP180)', '气体传感器(MQ-2/MQ-135/空气质量)', '称重传感器(HX711/应变片)', '超声波传感器(HC-SR04)/测距', '红外传感器(人体红外/测温/循迹)', '磁传感器(HMC5883L/QMC5883L)', '传感器数据滤波(卡尔曼/一阶低通/滑动平均)', '传感器校准/线性化/温度补偿', '传感器选型/精度/量程/接口']
                },
                '单片机': {
                    'desc': 'Arduino、ESP32、树莓派等开发',
                    'difficulty': 2,
                    'dimensions': ['Arduino基础/IDE安装/Wiring语言', 'Arduino引脚/数字IO/模拟IO/PWM', 'Arduino库/libraries/常用库(Millis/DHT/WiFi)', 'Arduino Shields扩展板/传感器扩展', 'ESP32基础/Arduino Core/开发环境', 'ESP32 WiFi/BLE连接/低功耗', 'ESP32外设(I2C/SPI/UART/ADC/DAC)', '树莓派GPIO/物理引脚/ WiringPi', '树莓派系统安装/SD卡/联网配置', '树莓派I2C/SPI/UART配置', 'GPIO控制/设备驱动/设备树', '树莓派摄像头/CSI/OpenCV', 'Docker on Pi/IoT网关应用', 'STM32基础/标准库/HAL库', '51单片机/定时器/中断/串口']
                },
                '可视化': {
                    'desc': '设备数据可视化和监控',
                    'difficulty': 2,
                    'dimensions': ['数据可视化原理/图表类型选择', '实时数据展示/数据刷新策略', 'ECharts/AntV/G2图表库', 'D3.js数据可视化/自定义图表', 'WebSocket实时推送/数据流展示', '仪表盘设计/仪表盘工具', 'Grafana数据展示/面板配置', 'MQTT数据订阅/Dashboard显示', '大屏展示/响应式设计', '地图可视化/设备位置展示', '数据历史存储/时序数据展示', '告警可视化/阈值告警/实时告警', '移动端适配/H5嵌入', '数据导出/报表生成']
                },
                '数据传输协议': {
                    'desc': 'HTTP、CoAP、LwM2M等协议',
                    'difficulty': 2,
                    'dimensions': ['HTTP协议/请求响应/持久连接', 'CoAP轻量协议/资源受限设备', 'LwM2M(OMA LwM2M)/设备管理协议', 'WebSocket全双工通信/实时推送', 'Socket通信/TCP/UDP传输', 'Modbus协议/RTU/TCP/串口通信', 'CAN总线协议/汽车网络', 'LoRaWAN协议/网关/终端', 'NB-IoT协议/低功耗广域网', 'ZigBee协议/组网/协调器', '协议对比/协议选择策略', '协议转换/网关协议桥接', '数据格式(JSON/二进制/Protobuf)', '安全传输/TLS/DTLS']
                },
                '数据存储': {
                    'desc': '时序数据库如InfluxDB',
                    'difficulty': 2,
                    'dimensions': ['时序数据特点/时间戳/序列', 'InfluxDB安装/InfluxQL/数据写入', 'InfluxDB Telegraf数据收集', 'InfluxDB标签/字段/测量值', 'TSDB时序数据库/数据压缩', 'TDengine时序数据库/超级表', 'MySQL时序数据存储/分表策略', 'MongoDB文档存储/设备数据', 'Redis缓存/最新数据存储', '数据聚合查询/GROUP BY时间', '数据降采样/保留策略/RP', '连续查询/CQ/数据压缩', '数据可视化/ Grafana连接', '数据备份/恢复/迁移']
                },
                '设备管理': {
                    'desc': 'OTA升级、设备注册、生命周期管理',
                    'difficulty': 2,
                    'dimensions': ['设备注册流程/唯一标识/凭证', '设备认证(X.509证书/对称密钥)', '设备影子/状态同步/期望值', 'OTA升级流程/差分升级/全量升级', 'OTA安全/签名验证/回滚机制', '设备分组/批量操作', '设备禁用/启用/注销', '设备生命周期/生产/注册/激活/退役', '固件版本管理/多版本支持', '远程配置/参数下发', '远程诊断/日志获取', '设备告警/阈值监控/异常检测', '设备在线离线状态/心跳', '设备迁移/跨区域/跨平台']
                },
                '边缘计算': {
                    'desc': '边缘网关和本地数据处理',
                    'difficulty': 3,
                    'dimensions': ['边缘计算概念/云边协同/雾计算', '边缘网关架构/硬件选型', '边缘AI/推理加速/NPU', '边缘数据处理/本地过滤/聚合', '边缘存储/本地数据库/缓存', '边缘安全/可信执行环境/TEE', 'Kubernetes Edge/K3s/边缘集群', 'KubeEdge架构/云边消息同步', 'OpenYurt架构/阿里云边缘容器', 'AWS Greengrass/边缘Lambda', 'Azure IoT Edge/边缘模块部署', '边缘推理/TensorFlow Lite/ONNX', '边缘缓存/离线运行/断网续传', '边缘自治/本地决策/弱网适应', '边缘编排/自动化脚本']
                }
            }
        },
        '硬件工程师': {
            'description': '设计硬件电路，绘制PCB，调试硬件样机。',
            'skills': {
                '元器件选型': {
                    'desc': '电阻电容芯片等器件参数选型和成本控制',
                    'difficulty': 2,
                    'dimensions': ['电阻规格(阻值/功率/精度/温度系数)', '电容类型(瓷片/电解/钽/薄膜)/容量/耐压', '电感选型(感值/Q值/饱和电流)', '芯片封装(SOP/TSSOP/QFN/BGA)', 'Datasheet阅读/参数规格表', '品牌选择(原厂/代理商/假冒识别)', '元器件替换/替代料', '采购渠道/交期/成本控制', 'BOM优化/降本方案', '安全裕量/降额设计', '环境适应性(温度/湿度)', '环保要求(RoHS/REACH)']
                },
                '制板工艺': {
                    'desc': 'PCB制造工艺和工厂对接',
                    'difficulty': 2,
                    'dimensions': ['PCB层数(单层/双层/多层)', '板材类型(FR-4/CEM-1/CEM-3/高频板)', '板厚(0.8/1.0/1.2/1.6/2.0mm)', '铜厚(1/2/3oz)/走线宽度与电流', '阻焊颜色/丝印颜色/字符', '过孔类型(通孔/盲孔/埋孔)', '最小线宽/线距/焊盘', '工艺边/定位孔/FPC软板', 'SMT贴片工艺/回流焊/波峰焊', '钢网开口/红胶工艺', 'PCBA工厂对接/工程资料', 'Gerber文件/钻孔文件/坐标文件', '样板交期/批量交期/费用计算']
                },
                '原理图': {
                    'desc': '电路原理图设计和分析',
                    'difficulty': 2,
                    'dimensions': ['原理图符号/元件库创建', '电源符号/地符号/网络标号', '原理图绘制规范/连线', '层次原理图/模块化设计', '电路分析/欧姆定律/基尔霍夫定律', '分压/分流/RC/RL/RLC电路', '滤波电路(低通/高通/带通/带阻)', '放大电路(共射/共集/差分)', '比较器/施密特触发器', '二极管/三极管/MOSFET应用', '运算放大器应用/反馈电路', '电源拓扑(Buck/Boost/Buck-Boost)', '保护电路(过压/过流/防反接)', '原理图检查/DRC检查']
                },
                '焊接': {
                    'desc': 'SMT和手工焊接技术',
                    'difficulty': 2,
                    'dimensions': ['烙铁选择/温度设置/烙铁头保养', '焊锡丝/锡线直径/松香/助焊剂', '贴片焊接/镊子使用/拖焊技巧', 'QFN/BGA封装焊接/热风枪', '芯片拆焊/吸锡线/吸锡器', '虚焊/冷焊/桥连识别', '无铅焊锡/有铅焊锡/熔点', 'BGA植球/钢网/锡球', '回流焊炉温曲线设置', '波峰焊工艺/治具设计', 'SMT不良分析/返修工艺', '焊接辅助工具(放大镜/显微镜/热熔枪)', 'ESD防护/焊接安全']
                },
                '电源设计': {
                    'desc': '开关电源、LDO等电源方案',
                    'difficulty': 2,
                    'dimensions': ['线性电源/开关电源对比', 'LDO原理/压差/效率/散热', 'DC-DC Buck降压拓扑', 'DC-DC Boost升压拓扑', 'DC-DC Flyback反激拓扑', '电感选型/磁芯/饱和电流', '输出电容/输入电容/纹波', '反馈回路/光耦/电压基准', 'PWM控制/频率设置', '效率优化/损耗分析', '保护功能(OCP/OVP/OTP)', 'EMI滤波/π型滤波', '散热设计/PCB铜皮/散热片', '电源测试/负载调整率/线性调整率']
                },
                '电路设计': {
                    'desc': '模拟电路和数字电路设计',
                    'difficulty': 2,
                    'dimensions': ['模拟电路基础/信号调理', '运算放大器电路/比例/加法/积分', '滤波电路设计/截止频率计算', 'ADC前端电路/驱动放大', 'DAC后端电路/缓冲放大', '比较器电路/阈值检测', '数字电路基础/TTL/CMOS电平', '逻辑门电路/组合逻辑/时序逻辑', '时序电路/触发器/寄存器/计数器', '时钟电路/晶振/PLL', '接口电路(USB/ETH/RS485/CAN)', '电平转换电路/电平匹配', '硬件防护(TVS/ESD/共模滤波器)', '功耗分析/休眠设计']
                },
                '硬件调试': {
                    'desc': '示波器、万用表、逻辑分析仪等调试工具',
                    'difficulty': 2,
                    'dimensions': ['万用表使用/电压/电流/电阻测量', '示波器基础/触发/采样/存储', '示波器探头选择/衰减倍数', '时序分析/信号完整性', '逻辑分析仪协议解码/I2C/SPI/UART', '信号发生器/直流电源/电子负载', '焊接调试/飞线/调试线', '上电时序调试/电源时序', '波形分析/噪声分析/纹波测量', '电源完整性测试/PDN', '眼图测试/高速信号测试', '异常排查/干扰定位', '调试报告/问题记录', 'Debug技巧/排除法/替换法']
                },
                'EMC': {
                    'desc': '电磁兼容性设计和整改',
                    'difficulty': 3,
                    'dimensions': ['EMC基础/电磁干扰EMI/电磁敏感EMS', '传导干扰/辐射干扰/空间耦合', 'EMC标准(CE/FCC/CCC)/测试项目', '辐射发射整改/辐射源定位', '传导发射整改/滤波设计', 'CE/RE/CE102/CE106测试', 'CS传导抗扰度/RS辐射抗扰度', 'ESD静电放电整改/防护设计', 'EFT电快速瞬变脉冲群', 'Surge浪涌/雷击测试/防护', 'EMI滤波设计/共模电感/差模电容', '屏蔽设计/金属屏蔽/导电泡棉', 'PCB布局布线EMC注意事项', '接地设计/单点接地/多点接地', 'EMC整改流程/案例分析']
                },
                'PCB设计': {
                    'desc': 'Altium Designer、Cadence等PCB设计软件',
                    'difficulty': 3,
                    'dimensions': ['Altium Designer快捷键/工作环境', '原理图导入/网络表生成', '封装创建/SMD贴片封装/IPC规范', 'PCB层叠设置/叠层设计', '规则设置(线宽/间距/过孔)', '布局原则/模块化布局/接口位置', '布线技巧/45度/圆弧走线/铺铜', '电源平面/地平面/分割平面', '过孔类型/盲埋孔/微孔', 'DRC检查/设计规则检查', 'Gerber输出/钻孔文件/坐标文件', 'BOM输出/装配图/PDF图纸', 'CadenceAllegro基础/OrCAD原理图', '高速PCB设计注意事项', 'PCB检查清单/评审要点']
                },
                '信号完整性': {
                    'desc': '高速信号PCB设计',
                    'difficulty': 3,
                    'dimensions': ['信号完整性基础/反射/串扰', '阻抗控制/特性阻抗/Z0', '微带线/带状线/共面波导', '阻抗计算/线宽/线距/介质厚度', '传输线理论/端接匹配', '源端匹配/终端匹配/戴维南', '串扰分析/近端串扰/远端串扰', '时序分析/建立时间/保持时间', 'S参数/插入损耗/回波损耗', '眼图/抖动/误码率', '高速连接器/同轴连接器', 'DDR布线/等长匹配/蛇形走线', '差分对设计/耦合度/等长', '电源完整性/去耦电容/PDN', 'SI仿真/ADS/HyperLynx仿真']
                }
            }
        }
    },
    '云计算': {
        '云计算工程师': {
            'description': '设计和维护云架构，管理和优化云资源。',
            'skills': {
                'AWS': {
                    'desc': '亚马逊云服务架构设计和部署，EC2、S3、RDS等',
                    'difficulty': 2,
                    'dimensions': ['AWS基础/EC2实例类型/AMI/安全组', 'S3存储/存储类别/生命周期/权限', 'VPC网络/子网/路由表/NAT/Internet Gateway', 'IAM角色/策略/用户组/权限管理', 'RDS数据库/MySQL/PostgreSQL/ Aurora', 'Auto Scaling/弹性伸缩组/启动配置', 'ELB负载均衡/ALB/NLB/目标组', 'CloudWatch监控/日志/告警', 'Lambda无服务器/函数触发器', 'SQS队列/SNS通知/EventBridge', 'EKS容器服务/Kubernetes on AWS', 'CloudFormation模板/基础设施编排', 'AWS成本/Cost Explorer/预算告警']
                },
                'Azure': {
                    'desc': '微软云平台服务管理和开发',
                    'difficulty': 2,
                    'dimensions': ['Azure基础/订阅/资源组/RG', 'Azure VM/虚拟机类型/规模集', 'Azure Storage/Blob/Queue/Table', 'Azure Virtual Network/子网/NSG', 'Azure AD/Entra ID/应用注册', 'Azure SQL/MySQL/PostgreSQL/灵活服务器', 'Azure Kubernetes Service/AKS集群', 'Azure Container Instances/应用服务', 'Azure Functions/ Durable Functions', 'Azure DevOps/管道/工件/Board', 'Azure Monitor/Application Insights', 'ARM模板/Terraform on Azure', 'Azure成本/成本管理/预算']
                },
                'Docker': {
                    'desc': '容器化技术应用部署',
                    'difficulty': 2,
                    'dimensions': ['Docker基础/镜像/容器/仓库', 'Dockerfile编写/指令(FROM/RUN/COPY/ENTRYPOINT)', '镜像构建/分层/缓存优化', 'Docker网络(bridge/host/none/自定义)', 'Docker数据卷/挂载/持久化存储', 'Docker Compose/多容器编排', 'Dockerfile最佳实践/多阶段构建', '镜像安全扫描/漏洞修复', '私有仓库/Docker Hub/Harbor', 'Docker Swarm/集群管理', '容器监控/日志收集', '资源限制/CPU/内存/磁盘IO', 'Docker网络驱动/overlay/Macvlan']
                },
                'Kubernetes': {
                    'desc': '容器编排和集群管理',
                    'difficulty': 2,
                    'dimensions': ['K8s架构/控制平面/工作节点', 'Pod/Deployment/ReplicaSet', 'Service/ClusterIP/NodePort/LoadBalancer', 'Ingress/域名路由/证书', 'ConfigMap/Secret/配置管理', 'PersistentVolume/PersistentVolumeClaim', 'StatefulSet/有状态应用', 'Job/CronJob/定时任务', 'HPA/VPA/自动伸缩', 'RBAC权限/ServiceAccount', '网络策略/命名空间隔离', 'Helm Charts/包管理器', 'Kustomize/配置差异化', '集群升级/版本兼容性', 'Kubeadm/kubespray/集群部署']
                },
                'Serverless': {
                    'desc': '无服务器架构，Lambda、函数计算',
                    'difficulty': 2,
                    'dimensions': ['Serverless概念/事件驱动架构', 'AWS Lambda函数/触发器/事件源', 'Lambda运行时/Python/Node.js/Java', 'Lambda Layers/依赖打包', 'Lambda权限/IAM角色/资源策略', 'API Gateway/ REST API /HTTP API', 'Azure Functions触发器/Binding', '阿里云函数计算FC/触发器', '腾讯云SCF无服务器函数', 'Serverless框架(Serverless Framework)', 'SAM/Claudia.js/无服务器应用', '冷启动优化/预置并发', '成本模型/按调用计费', '无服务器数据库/DynamoDB/CosmosDB']
                },
                'Terraform': {
                    'desc': '基础设施即代码自动化部署',
                    'difficulty': 2,
                    'dimensions': ['Terraform基础/HCL语法/Provider', 'Terraform命令(init/plan/apply/destroy)', '变量定义/variable/输出output', '资源管理/aws_instance/azure_vm', '数据源/data source', '状态管理/remote state/后端', '模块化/module/模块复用', 'Provisioner/远程执行', 'workspace/环境隔离', 'Terraform Cloud/远程运行', 'IAM Policy/最小权限原则', 'Terraform最佳实践/代码审查', 'Terraform升级/版本锁定']
                },
                '云原生': {
                    'desc': '微服务、容器化、DevOps、持续交付',
                    'difficulty': 2,
                    'dimensions': ['云原生概念/12要素应用', '微服务架构/服务拆分/治理', '服务发现/Consul/Eureka', 'API网关/Kong/Envoy', '熔断器/Hystrix/Sentinel', '容器化/Docker/Kubernetes', 'CI/CD流水线/Jenkins/GitLab CI', 'GitOps/ArgoCD/Flux', '配置中心/Apollo/Nacos', '分布式追踪/Jaeger/Zipkin', '服务网格/Istio/Linkerd', '可观测性/日志/监控/链路追踪', '云原生安全/ Secret管理/网络策略']
                },
                '云架构': {
                    'desc': '高可用、高并发、弹性伸缩架构设计',
                    'difficulty': 2,
                    'dimensions': ['高可用架构/多可用区/灾备', '负载均衡/流量分发/健康检查', '水平扩展/垂直扩展/自动伸缩', '缓存架构/Redis Cluster', 'CDN加速/全球分发', '消息队列/异步解耦', '数据库读写分离/分库分表', '分布式存储/Ceph/MinIO', '限流熔断/降级/兜底', '弹性设计/无状态服务', '微服务网关/统一入口', '容灾设计/跨区域部署', '架构评审/架构文档', '成本优化/资源利用率']
                },
                '多云管理': {
                    'desc': '跨云平台的统一管理和迁移',
                    'difficulty': 2,
                    'dimensions': ['多云战略/利弊分析', '跨云迁移/迁移工具', '一致性管理/Terraform/Pulumi', '成本对比/厂商锁定规避', '数据复制/跨云同步', 'DNS管理/Global Traffic Manager', '多云网络/专线/VPN', '跨云备份/灾难恢复', '混合云架构/本地+云', '统一监控/Prometheus/Grafana', '策略即代码/Policy as Code', '多云安全/合规/身份管理', '多云编排/ANSIBLE/Kubernetes']
                },
                '成本优化': {
                    'desc': '云资源成本分析和优化',
                    'difficulty': 2,
                    'dimensions': ['成本模型/按需/预留/竞价实例', '成本分析工具/成本报告', '资源利用率监控/右-sizing', '存储成本/存储类别选择', '网络成本/流量优化', '预留实例/ Savings Plans', 'Spot实例/中断处理', '标签策略/成本归集', '预算告警/成本异常检测', '无服务器成本/按调用优化', '成本可视化/DashBoard', '成本优化实践/案例', 'FinOps实践/云财务管理']
                },
                '网络规划': {
                    'desc': 'VPC、子网、安全组设计',
                    'difficulty': 2,
                    'dimensions': ['VPC设计/ CIDR规划', '子网划分/公有子网/私有子网', '路由表/路由策略', 'Internet Gateway/NAT Gateway', '安全组/NACL/防火墙规则', 'VPN连接/Site-to-Site', '专线连接/Direct Connect', '弹性IP/公网访问控制', 'PrivateLink/服务端点', 'VPC Peering/对等连接', '网络ACL/子网级别控制', '流量监控/VPC Flow Logs', 'DNS设计/Route 53/Private Zone', '网络隔离/环境分离']
                },
                '腾讯云': {
                    'desc': '腾讯云产品架构和部署',
                    'difficulty': 2,
                    'dimensions': ['腾讯云基础/账户/认证', '云服务器CVM/批量计算/竞价实例', '容器服务TKE/Kubernetes集群', '云数据库TDSQL/MySQL/Redis', 'COS对象存储/数据迁移', 'VPC私有网络/子网/路由表', 'CLB负载均衡/ALB/CLB', '无服务器云函数SCF', 'API网关/微服务引擎TSF', '云开发TCB/小程序云开发', '云监控/云审计', '腾讯云DevOps/ CODING', '成本管理/资源包/按量计费']
                },
                '阿里云': {
                    'desc': '国内主流云服务使用',
                    'difficulty': 2,
                    'dimensions': ['阿里云基础/账户/RAM', 'ECS云服务器/弹性裸金属', '容器服务ACK/Kubernetes', 'RDS数据库/MySQL/PostgreSQL/PolarDB', 'OSS对象存储/文件存储NAS', 'VPC专有网络/交换机/路由表', 'SLB负载均衡/ALB/NLB', '函数计算FC/无服务器', 'API网关/微服务/MSF', 'Spring Cloud Alibaba/Nacos', '阿里云DevOps/云效', '云监控/日志服务SLS', '安全产品/WAF/DDoS防护', '成本管理/资源包/节省计划']
                }
            }
        },
        '云运维工程师': {
            'description': '负责云平台运维，保证云服务的高可用性和性能。',
            'skills': {
                'Docker': {
                    'desc': '容器运维和镜像管理',
                    'difficulty': 2,
                    'dimensions': ['Docker守护进程/容器生命周期', '镜像管理/pull/push/tag/构建', '容器操作/start/stop/exec/logs', 'Docker网络/bridge/overlay/host', '数据卷挂载/数据持久化', 'Docker Compose编排多容器', '镜像安全/漏洞扫描/加固', '私有仓库/Harbor/Distribution', '资源限制/CPU/内存配额', '日志驱动/json-file/syslog', '健康检查/HEALTHCHECK', '容器监控/cAdvisor/Stats', 'Docker Swarm集群管理', 'Dockerfile优化/多阶段构建']
                },
                'Kubernetes': {
                    'desc': 'K8s集群运维和故障排查',
                    'difficulty': 2,
                    'dimensions': ['集群架构/控制平面/工作节点', 'kubectl命令/上下文切换', 'Pod调度/亲和性/反亲和性', '滚动更新/回滚/Deployment策略', '资源配额/Request/Limit/Quota', '健康检查/liveness/readiness探针', '存储管理/PV/PVC/StorageClass', '网络策略/命名空间隔离', 'RBAC权限/角色绑定', '日志收集/Fluentd/EFK', '集群升级/版本兼容性', '故障排查/Pod状态/Events', 'HPA自动伸缩/Metrics Server', 'etcd备份/恢复', 'Kubeasz/kubespray部署']
                },
                'Linux': {
                    'desc': 'Linux服务器管理和运维',
                    'difficulty': 2,
                    'dimensions': ['Linux发行版/CentOS/Ubuntu/Debian', '系统服务/systemd/init.d', '用户管理/useradd/usermod/passwd', '磁盘管理/fdisk/df/du/lvm', '网络配置/ifcfg/ip/route', '进程管理/ps/top/htop/kill', '日志管理/ journalctl/rsyslog', '定时任务/cron/anacron/systemd timer', 'SSH密钥/免密登录/跳板机', '系统优化/sysctl/ulimit', '内核参数调优', '安全加固/防火墙(iptables/nftables)/selinux', '性能监控/top/free/iostat/netstat', '故障排查/dmesg/strace/lsof']
                },
                '云计算平台': {
                    'desc': '主流云平台日常运维管理',
                    'difficulty': 2,
                    'dimensions': ['阿里云控制台/日常操作', 'ECS实例管理/远程连接', 'RDS数据库运维/备份/参数调优', 'OSS对象存储/权限/生命周期', 'VPC网络/安全组配置', '云监控/告警规则设置', '运维堡垒机/访问控制', 'AWS控制台/EC2/RDS/S3', 'Azure门户/虚拟机/存储', '腾讯云控制台/CVM/数据库', '云平台CLI/SDK运维', '跨区域运维/多账户管理', '云平台成本控制/资源优化']
                },
                '备份恢复': {
                    'desc': '云数据备份和灾难恢复',
                    'difficulty': 2,
                    'dimensions': ['备份策略/全量/增量/差异', '快照/Snapshot/自动快照策略', '数据库备份/mysqldump/xtrabackup', 'Redis RDB/AOF备份', '备份加密/压缩存储', '异地备份/跨区域复制', '恢复演练/定期测试', 'RTO/RPO目标设定', '灾难恢复计划/DRP', '云存储备份/S3 Glacier', '备份脚本/自动化备份', '备份监控/备份成功告警', 'VMware/物理机迁移', '云迁移工具/迁云服务']
                },
                '安全管理': {
                    'desc': '云安全组、访问控制、密钥管理',
                    'difficulty': 2,
                    'dimensions': ['IAM用户/角色/策略', '安全组/入方向/出方向规则', '网络ACL/子网级别防护', '密钥管理/KMS/对称/非对称密钥', '凭证管理/Secret管理/轮换', '多因素认证/MFA', '安全审计/CloudTrail/操作日志', 'WAF Web应用防火墙', 'DDoS防护/流量清洗', '漏洞扫描/安全评估', '最小权限原则/IAM权限隔离', '网络隔离/VPC对等连接', '安全组规则审计', '合规检查/等保/ISO27001']
                },
                '故障排查': {
                    'desc': '云服务故障诊断和恢复',
                    'difficulty': 2,
                    'dimensions': ['故障分级/P0/P1/P2/P3', '监控告警/异常检测/根因分析', '云平台健康状态/服务状态页', '网络故障排查/ping/telnet/traceroute', 'DNS故障/解析异常', '服务器SSH/远程连接问题', '端口不通/防火墙/Security Group', 'CPU飙高/内存泄漏/进程异常', '磁盘满/IO高/性能瓶颈', '证书过期/SSL/TLS问题', '服务宕机/自动恢复', '故障复盘/Incident Review', '故障报告/时间线/影响范围', '应急响应流程/值班机制']
                },
                '日志管理': {
                    'desc': 'ELK、Loki等日志收集和分析',
                    'difficulty': 2,
                    'dimensions': ['ELK架构/Elasticsearch/Logstash/Kibana', 'Elasticsearch索引/映射/分片', 'Logstash输入/过滤/输出', 'Kibana图表/仪表盘/可视化', 'Loki日志收集/Promtail', 'Grafana Loki展示/日志查询', 'Filebeat轻量日志收集', '日志格式/结构化日志/JSON', '日志采集/容器日志/应用日志', '日志存储策略/生命周期/压缩', '日志查询/DSL/KQL', '日志告警/阈值告警', '日志合规/保留策略', '分布式日志追踪']
                },
                '监控': {
                    'desc': 'Prometheus、Grafana云资源监控和性能调优',
                    'difficulty': 2,
                    'dimensions': ['Prometheus架构/TSDB/拉取模式', 'Exporter指标暴露/Node Exporter', 'PromQL查询/聚合函数/rate/irate', 'Prometheus配置/服务发现', 'Grafana仪表盘/图表/Panel', '告警规则/Alertmanager/PagerDuty', 'Kubernetes监控/cAdvisor/kube-state-metrics', '应用监控/业务指标/APM', '云平台监控/CloudWatch/Azure Monitor', '网络监控/CAdvisor/Weave Scope', '数据库监控/慢查询/连接数', '告警收敛/去重/抑制', 'SLO/SLA目标监控', '性能分析/火焰图/pprof']
                },
                '自动化运维': {
                    'desc': 'Ansible、Puppet等自动化运维工具',
                    'difficulty': 2,
                    'dimensions': ['Ansible基础/YAML/Inventory', 'Ansible模块/command/shell/script', 'Playbook剧本/任务/处理器', 'Ansible Role角色复用', 'Ansible Tower/AWX Web界面', 'Puppet Manifest/资源/类', 'Puppet模块/环境/代码管理', 'SaltStack基础/Master/Minion', '批量执行/命令推送/状态管理', '配置管理/配置文件一致性', '自动部署/应用发布', '堡垒机/审批流程/审计', 'CI/CD集成/Jenkins/GitLab', '配置审计/合规检查']
                }
            }
        },
        '云原生工程师': {
            'description': '构建和维护云原生应用和基础设施。',
            'skills': {
                'ArgoCD': {
                    'desc': 'K8s声明式持续交付工具',
                    'difficulty': 2,
                    'dimensions': ['ArgoCD架构/Application/ApplicationSet', 'GitOps理念/声明式部署', 'ArgoCD安装/配置/Helm参数', 'Application部署/同步策略', '自动同步/Sync Wave', '回滚/History/rollback', '多集群部署/Cluster ADD', 'ArgoCD通知/Webhook集成', 'ArgoCD RBAC/权限控制', 'Argo Rollouts/金丝雀/蓝绿', 'Argo Workflows/工作流引擎', 'Argo CD Image Updater', 'Helm集成/Kustomize集成', '密码管理/Secret集成']
                },
                'CNI': {
                    'desc': '容器网络接口和网络方案',
                    'difficulty': 2,
                    'dimensions': ['CNI规范/接口定义', '容器网络模型/IPAM', 'Bridge网络/网桥插件', 'Flannel网络/VXLAN封装', 'Calico网络/网络策略', 'Weave Net/网络插件', 'Cilium/eBPF数据平面', 'Macvlan/Vlan插件', 'Host-local/IPAM分配', 'CNI插件选择策略', '网络命名空间/netns', 'Veth对/容器网络连接', 'K8s网络策略/隔离', 'Ingress Controller/负载均衡']
                },
                'CSI': {
                    'desc': '容器存储接口和存储方案',
                    'difficulty': 2,
                    'dimensions': ['CSI规范/接口定义', '存储插件架构/Controller/Node', 'PV/PVC绑定机制', 'StorageClass/动态供给', 'NFS存储卷/网络文件系统', 'HostPath/本地存储', 'EmptyDir/临时存储', 'AWS EBS CSI驱动', 'GCE PD CSI驱动', 'Ceph RBD/CephFS存储', 'Longhorn分布式存储', 'Local PV/本地持久化', '存储QoS/IOPS限制', '存储快照/克隆/备份']
                },
                'Docker': {
                    'desc': '容器技术原理和最佳实践',
                    'difficulty': 2,
                    'dimensions': ['Docker架构/容器运行时/runc', '镜像分层/联合文件系统', '容器网络/bridge/overlay', 'Docker存储驱动/overlay2', 'Docker安全/Security Profiles', 'Docker监控/Stats/API', 'Docker日志驱动/ logging driver', 'Docker Daemon配置', 'Containerd独立运行', 'Dockerfile最佳实践', '镜像优化/多阶段构建', 'Docker Registry/镜像分发', 'Docker Compose/本地编排', 'Swarm Mode/集群模式']
                },
                'GitOps': {
                    'desc': '基于Git的持续交付模式',
                    'difficulty': 2,
                    'dimensions': ['GitOps核心原则/声明式', 'Git仓库结构/应用仓库', 'ArgoCD/GitOps引擎', 'Flux CD/自动同步', 'GitOps工作流/开发流程', '环境管理/dev/staging/prod', 'Secrets管理/sealed-secrets', 'Kustomize差异化配置', 'Helm Chart管理', 'Pull Request审核流程', 'GitOps监控/同步状态', '灾难恢复/Git回滚', '多集群GitOps', 'GitOps安全/代码签名']
                },
                'Grafana': {
                    'desc': '监控数据可视化',
                    'difficulty': 2,
                    'dimensions': ['Grafana安装/数据源配置', 'Dashboard创建/面板/Panel', 'Prometheus数据源', 'Graph/Time Series图表', 'Alert规则/Alertmanager', '变量模板/动态仪表盘', '用户管理/组织/团队', 'Grafana Loki日志', 'Explore探索查询', 'Annotations注解', 'Provisioning/自动化配置', 'Grafana Cloud托管服务', '告警渠道/Slack/邮件', '权限控制/Dashboard共享']
                },
                'Helm': {
                    'desc': 'K8s包管理和应用部署',
                    'difficulty': 2,
                    'dimensions': ['Helm架构/Tiller/客户端', 'Helm Chart结构/templates', 'Chart.yaml元数据', 'values.yaml默认值', '模板渲染/Go模板', 'Helm函数/sprig函数库', '条件渲染/with作用域', 'Helm仓库/ChartMuseum/Harbor', 'Helm install/upgrade/rollback', 'Release管理/状态追踪', 'Helm Hooks/生命周期钩子', 'Helm测试/Test Charts', 'Helm安全/签名验证', 'Helm3免Tiller部署']
                },
                'Istio': {
                    'desc': '服务网格，微服务流量管理',
                    'difficulty': 2,
                    'dimensions': ['Istio架构/Control Plane/Data Plane', 'Envoy代理/sidecar注入', 'VirtualService/路由规则', 'DestinationRule/负载均衡策略', 'Gateway/ Ingress Gateway', 'ServiceEntry/外部服务', '流量镜像/Mirror Traffic', '超时重试/熔断/限流', 'Fault Injection/故障注入', 'mTLS双向认证/Security Policy', 'Mixer/Telemetry V2', 'Kiali服务可视化', 'Jaeger链路追踪', 'Istio配置最佳实践']
                },
                'Knative': {
                    'desc': 'K8s无服务器框架',
                    'difficulty': 2,
                    'dimensions': ['Knative架构/Eventing/Serving', 'Knative Serving/服务部署', 'Serverless自动伸缩/KPA', '冷启动优化/预热', 'Revision管理/版本路由', 'Knative Eventing/事件源', 'Trigger/Broker事件订阅', 'CloudEvents事件规范', 'Kafka事件源/绑定', '流量分割/金丝雀发布', ' Knative API/ kubectl', '自动扩缩容/0-N', '服务探测/健康检查', 'Knative与云厂商集成']
                },
                'Kubernetes': {
                    'desc': '深度掌握K8s架构和原理',
                    'difficulty': 2,
                    'dimensions': ['K8s架构/控制平面组件', 'etcd存储/一致性问题', 'API Server认证授权', 'Scheduler调度器/调度算法', 'Controller Manager/控制器', 'Kubelet工作原理', 'Kube-Proxy网络代理', 'Pod生命周期/Init容器', 'ConfigMap/Secret配置', 'Service/Ingress网络', 'Volume/存储管理', 'SecurityContext/PSP/PodSecurity', 'NetworkPolicy网络策略', 'ResourceQuota/LimitRange', '调度亲和性/污点容忍', 'CRD/自定义资源']
                },
                'Prometheus': {
                    'desc': '云原生监控方案',
                    'difficulty': 2,
                    'dimensions': ['Prometheus架构/TSDB存储', '指标类型/Counter/Gauge/Histogram', 'PromQL查询语言', 'Exporter指标暴露', '服务发现/SD机制', 'Prometheus Operator', 'Alertmanager告警', 'Prometheus联邦', 'Remote Write远程存储', 'Recording Rules预计算', 'Grafana集成', 'BlackboxExporter探针', 'APM应用性能监控', 'Prometheus性能调优']
                },
                'etcd': {
                    'desc': '分布式键值存储',
                    'difficulty': 2,
                    'dimensions': ['etcd架构/Raft共识协议', 'etcd数据模型/键值对', 'etcd API/gRPC接口', 'MVCC多版本并发控制', 'Watch机制/事件监听', 'Lease租约/TTL', 'etcd集群/节点发现', 'Raft Leader选举', '一致性问题/脑裂', 'etcd备份/snapshot', 'etcd恢复/disaster recovery', 'etcd性能优化/参数调优', 'etcd监控/metrics', 'etcd安全/TLS/mTLS']
                },
                'Operator': {
                    'desc': 'K8s Operator开发和运维',
                    'difficulty': 3,
                    'dimensions': ['Operator模式/CRD控制器', 'Kubebuilder框架', 'Operator SDK/Golang', 'Custom Resource定义', 'Reconciliation Loop', 'Status Subresource状态更新', 'Finalizer处理资源删除', 'Webhooks验证/变更', 'Owner References层级', 'Leader Election选主', 'Operator测试/suite', 'etcd Operator示例', 'Prometheus Operator示例', 'Operator最佳实践', 'Operator生命周期管理']
                }
            }
        }
    },
    '游戏开发': {
        'Unity开发工程师': {
            'description': '使用Unity引擎开发游戏，实现游戏逻辑和交互功能。',
            'skills': {
                'C#': {
                    'desc': 'Unity主要编程语言，游戏逻辑开发',
                    'difficulty': 1,
                    'dimensions': ['C#基础语法/数据类型/控制流程', 'OOP特性/类/接口/继承/多态', '委托/事件/delegate/event', '协程/IEnumerator/Yield', 'LINQ/Lambda表达式', '泛型/集合/List/Dictionary', '结构体/枚举/可空类型', 'Unity API/MonoBehaviour', '协程/异步编程/Task', '反射/Attribute特性', '内存管理/垃圾回收', 'JsonUtility/序列化', 'File文件操作', '设计模式/单例/观察者']
                },
                'UGUI': {
                    'desc': 'Unity用户界面系统',
                    'difficulty': 2,
                    'dimensions': ['Canvas画布/屏幕空间/世界空间', 'RectTransform/锚点/轴心', 'Image/Sprite/九宫格', 'Text/TextMeshPro字体', 'Button/Button事件', 'Toggle/Checkbox组件', 'Slider/Scrollbar滑动条', 'InputField输入框', 'Dropdown下拉框', 'ScrollView滚动视图', 'VerticalLayoutGroup水平布局', 'GridLayoutGroup网格布局', 'ContentSizeFitter自适应', 'UGUI事件/EventTrigger', 'UGUI优化/批处理']
                },
                'UI设计': {
                    'desc': '游戏界面和交互设计',
                    'difficulty': 2,
                    'dimensions': ['UI布局原则/界面层级', 'HUD设计/血条/小地图', '弹窗设计/确认框/提示', '按钮状态/正常/悬停/点击', '动画过渡/界面切换动画', '动效设计/弹性/缓动', '响应式设计/分辨率适配', '深色模式/主题切换', '无障碍设计/辅助功能', 'UI性能优化/Overdraw', '图集打包/Atlas', '本地化/多语言/Localization', '新手引导/高亮遮罩', 'HUD管理/单例模式']
                },
                'Unity3D': {
                    'desc': '跨平台游戏引擎使用，场景管理和资源管理',
                    'difficulty': 2,
                    'dimensions': ['Unity编辑器界面/快捷键', '场景Scene/GameObject/Component', 'Transform组件/位置旋转缩放', 'Prefab预制体/实例化', '材质Material/Shader/渲染管线', '光照/Light/烘焙/探针', '相机Camera/视野/层/剔除', '输入管理/Input.GetKey', 'Time时间/DeltaTime', '协程/Coroutine', '生命周期/Awake/Start/Update', '场景切换/SceneManager', 'Unity Package Manager', 'ProjectSettings项目配置', '版本控制/Unity Collaborate']
                },
                '动画系统': {
                    'desc': 'Animator、Animation动画控制',
                    'difficulty': 2,
                    'dimensions': ['Animation动画剪辑', 'Animator Controller状态机', 'State状态/Transition过渡', 'BlendTree混合树', '动画层/Avatar Mask', '动画参数/Int/Float/Bool/Trigger', '动画事件/Animation Event', 'IK逆向运动学/Foot IK', 'Root Motion根动画', '人形动画Avatar', '动画片段导入设置', 'AnimationCurve动画曲线', 'Playable API/时间轴', '动画重写/Override Controller', '2D动画/Sprite Sheet']
                },
                '多平台发布': {
                    'desc': 'iOS、Android、PC、WebGL发布',
                    'difficulty': 2,
                    'dimensions': ['Build Settings构建配置', 'Player Settings平台设置', 'iOS Xcode项目生成', 'iOS证书/Provisioning', 'Android APK打包', 'Android SDK/NDK配置', 'Android Manifest权限', 'PC Standalone构建', 'WebGL构建/发布', 'IL2CPP脚本后端', '代码剥离/Stripping', '压缩纹理/ETC2/ASTC', '平台符号解析', '多平台宏/#if UNITY_EDITOR', '热更新方案/ILRuntime']
                },
                '寻路系统': {
                    'desc': 'NavMesh导航网格',
                    'difficulty': 2,
                    'dimensions': ['NavMesh烘焙/Bake设置', 'NavMeshAgent导航代理', 'NavMeshObstacle障碍物', 'OffMeshLink链接', '寻路调用/NavMeshPath', 'NavMeshLink组件', '区域Area设置/成本', '动态寻路/更新NavMesh', '分层NavMesh/Layered', '寻路优先级/优先级队列', 'NavMeshSurface平面', 'A*寻路算法', 'Grid GridGraph网格图', 'NavMesh调试/路径绘制']
                },
                '游戏物理': {
                    'desc': '物理引擎实现碰撞和运动效果',
                    'difficulty': 2,
                    'dimensions': ['物理引擎概述/PhysX', 'Rigidbody刚体/质量/阻力', 'Collider碰撞体/Box/Sphere/Capsule', '碰撞检测/OnCollisionEnter', '触发器/Is Trigger', '碰撞矩阵/Layer Collision', '力施加/AddForce/Torque', '恒定力/Constant Force', 'CharacterController', 'Raycast射线检测', 'SphereCast/CapsuleCast', '关节/Joint/Hinge/Torque', '布料/Cloth Component', '物理材质/Physic Material']
                },
                '物理引擎': {
                    'desc': 'Rigidbody、Collider物理组件使用',
                    'difficulty': 2,
                    'dimensions': ['刚体属性/Mass/Drag/Angular Drag', '运动学刚体/Kinematic', '碰撞层/Layer/矩阵', '碰撞检测模式/Continuous', '物理固定更新/Fixed Timestep', '插值/Interpolation', '碰撞事件/Collision Info', '触发事件/Trigger Events', '复合碰撞体', 'WheelCollider轮子碰撞', 'ConfigurableJoint', 'Spring Joint弹簧关节', 'Hinge Joint铰链关节', '物理材质摩擦力/弹性']
                },
                '粒子系统': {
                    'desc': '特效制作和粒子控制',
                    'difficulty': 2,
                    'dimensions': ['Particle System组件', 'Emission发射模块', 'Shape形状模块/锥形/圆形', 'Velocity over Lifetime速度', 'Color over Lifetime颜色渐变', 'Size over Lifetime大小变化', 'Texture Sheet Animation纹理动画', 'Renderer渲染模块', 'Main Module主模块', 'Limit Velocity Over Lifetime', 'Collision碰撞模块', 'Sub Emitters子发射器', 'Trail拖尾模块', 'Cinemachine配合', 'GPU Instancing粒子优化']
                },
                '资源打包': {
                    'desc': 'AssetBundle资源管理和热更新',
                    'difficulty': 2,
                    'dimensions': ['AssetBundle构建/BuildPipeline', 'AB打包策略/分包', 'AB加载/AssetBundle.LoadAsset', 'AB依赖/Dependencies', 'AB变体/Variants', 'AB卸载/Unload', 'UnityWebRequest下载', 'AssetBundle缓存', '资源引用计数管理', 'MD5校验/版本检测', '热更新流程/增量更新', 'Addressables资源系统', 'Resources.Load优化', '资源释放/Resources.UnloadUnusedAssets']
                },
                'Shader': {
                    'desc': 'ShaderLab编写自定义着色器',
                    'difficulty': 3,
                    'dimensions': ['Shader基础/顶点片元着色器', 'ShaderLab语法/Properties', 'CG/HLSL编程', 'Unity光照模型/BRDF', '法线/Normal/法线贴图', 'Shadow/Caster/Receiver', 'UV动画/滚动纹理', '顶点动画/Displace', 'Bloom后处理效果', 'Depth of Field景深', 'Post Processing Stack', 'Surface Shader表面着色器', 'Unlit无光照着色器', 'Instancing实例化绘制', 'Shader性能优化/ALU']
                },
                '性能优化': {
                    'desc': 'DrawCall优化、资源管理、内存优化',
                    'difficulty': 3,
                    'dimensions': ['Profiler性能分析器', 'CPU性能/GPU性能', 'DrawCall批处理/Batching', '静态批处理/动态批处理', 'GPU Instancing实例化', '纹理图集/Atlas打包', 'LOD Level of Detail', 'Occlusion Culling遮挡剔除', 'Frustum Culling视锥剔除', '内存管理/垃圾回收/GC', '对象池/Object Pooling', 'MipMap优化', '光照探针/Light Probes', '阴影优化/Shadows优化', 'IL2CPP优化/代码剥离']
                }
            }
        },
        'Unreal开发工程师': {
            'description': '使用Unreal引擎开发高质量游戏，负责图形渲染和性能优化。',
            'skills': {
                'C++': {
                    'desc': 'Unreal核心编程语言，高性能开发',
                    'difficulty': 1,
                    'dimensions': ['C++基础/数据类型/指针/引用', '类和对象/继承/多态', '模板/Templates/泛型编程', 'STL容器/迭代器/算法', '智能指针/Unique/Shared', '命名空间/Namespace', '预处理指令/宏定义', 'Unreal UPROPERTY/UCLASS', 'UFUNCTION/UPROPERTY宏', 'FString/FText/文本处理', 'TArray/TMap/TSet容器', '委托/Delegate/Multicast', '协程/Future/Async', '蓝图调用/C++暴露接口', '模块/插件开发']
                },
                'AI行为树': {
                    'desc': '游戏AI设计和实现',
                    'difficulty': 2,
                    'dimensions': ['Behavior Tree行为树', 'Selector选择器/序列', 'Sequence序列/条件检查', 'Task任务节点', 'Decorator装饰器', 'Service服务节点', ' Blackboard黑板', 'AI感知/AIPerception', 'EQS环境查询系统', '导航/Navigation Mesh', 'AIController控制器', 'MoveTo移动任务', '自定义Task', 'AI模块架构', 'Pathfinding寻路']
                },
                'UMG': {
                    'desc': 'Unreal用户界面系统',
                    'difficulty': 2,
                    'dimensions': ['Widget蓝图控件', 'Canvas Panel画布', 'VerticalBox/HorizontalBox', 'SizeBox/Overlay', 'Text/TextBlock', 'Button/CheckBox', 'Image/Slate刷', 'EditableText/TextBox', 'Slider/ProgressBar', 'ComboBox下拉框', 'ListView列表视图', 'TreeView树形视图', '动画/Montage', '样式/Style/主题', 'UMG优化/复杂UI']
                },
                'Unreal Engine': {
                    'desc': 'Unreal游戏引擎深度使用',
                    'difficulty': 2,
                    'dimensions': ['引擎架构/模块系统', 'Actor/Pawn/Character', 'GameMode/GameInstance', 'Level/World/WorldContext', '组件/Component系统', 'GameplayFramework', 'UObject垃圾回收', '反射系统/RTTI', '蓝图可视化脚本', '关卡蓝图/Level BP', '动画蓝图/Anim BP', '材质编辑器/Material', '蓝图通信/接口', '编辑器扩展', '插件开发']
                },
                '光照系统': {
                    'desc': '静态光照、动态光照、Lumen',
                    'difficulty': 2,
                    'dimensions': ['Light Actor/Directional', 'Point Light点光源', 'Spot Light聚光灯', 'Sky Light天空光', 'Static/Stationary/Movable', 'Lightmass全局光照', '光照贴图/UV', '反射/Reflection', 'IBL环境光照', 'Lumen动态光照', 'Ray Tracing光线追踪', 'SSAO屏幕空间AO', '光照函数/Light Function', 'IES配置文件', '体积雾/Volumetric']
                },
                '动画系统': {
                    'desc': '动画蓝图和混合空间',
                    'difficulty': 2,
                    'dimensions': ['Animation Sequence动画', 'Blend Space混合空间', 'State Machine状态机', 'Anim Graph动画图表', 'Event Graph事件图表', 'Notify通知事件', 'Montage蒙太奇', 'IK逆向运动学', '物理动画/Physics Asset', 'Root Motion根动画', 'Anim Layer接口', 'Sync Groups同步组', 'Curves曲线动画', 'Aim Offset瞄准偏移', '布料动画/Cloth']
                },
                '性能分析': {
                    'desc': 'Unreal Insights性能分析工具',
                    'difficulty': 2,
                    'dimensions': ['Unreal Insights/会话', 'CPU Profiler分析', 'GPU Profiler分析', 'Memory内存分析', 'Load Time加载时间', 'Frame Profiler', 'Stats统计系统', 'GPUVisualizer', 'ShaderComplexity着色器', 'Rendering Stats', 'Draw Call统计', 'LOD状态统计', 'Memory Insights', 'Networking Insights', 'Trace/Recording']
                },
                '材质系统': {
                    'desc': 'Material Editor材质编辑',
                    'difficulty': 2,
                    'dimensions': ['Base Material基础材质', 'Material Expression表达式', 'Texture Sample纹理采样', 'UV Coord Coordinates', 'Normal Map法线', 'Roughness/Metallic粗糙度金属度', 'PBR光照模型', 'Material Functions函数', 'Material Layers层', 'Param Collection参数集合', 'Decal贴花', 'Blend Mode混合模式', 'Translucency透明度', 'Subsurface Scattering次表面', '材质实例/Material Instance']
                },
                '游戏物理': {
                    'desc': '物理模拟和角色控制',
                    'difficulty': 2,
                    'dimensions': ['Physics Asset物理资产', 'Rigid Body刚体', 'Collision碰撞频道', 'Physical Material物理材质', 'Constraint约束', 'Hinge Joint铰链关节', 'Physics Handle物理手柄', 'Chaos Physics引擎', 'Destructible可破碎物', 'Cloth布料', 'Vehicle车辆', 'Character Movement', 'Walk/Run/Air', 'NavMeshwalking', 'Flying飞行']
                },
                '网络同步': {
                    'desc': '多人游戏网络架构',
                    'difficulty': 2,
                    'dimensions': ['Replication复制', 'Role/RemoteRole角色', 'Owning Connection', 'Replicated变量', 'RPC远程调用', 'DOREPLIFETIME', 'Multicast广播', 'Net Group网络组', 'Relevancy相关性', 'Net Driver网络驱动', 'Demo Net记录', 'Online Subsystem', 'Session会话', 'Matchmaking匹配', 'Latency Compensation']
                },
                '蓝图': {
                    'desc': 'Unreal可视化脚本编程',
                    'difficulty': 2,
                    'dimensions': ['Blueprint事件图', 'Event BeginPlay/EventTick', 'Variables变量', 'Branch/序列节点', 'ForEach循环', 'Gate/Delay', 'Custom Events自定义事件', 'Functions函数', 'Macros宏', 'Interfaces接口', 'Structs结构体', 'Enums枚举', 'Data Table数据表', 'Blueprint通信', '蓝图优化']
                },
                'Nanite': {
                    'desc': '虚拟几何体系统',
                    'difficulty': 3,
                    'dimensions': ['Nanite概述/虚拟几何体', 'Nanite支持格式/FBX/StaticMesh', '强制Nanite/ForceNanite', 'Nanite质量/Nanite Quality', 'LOD系统/Fallbacl LOD', 'Nanite剔除', 'Nanite与HLOD配合', '性能优化/三角形数量', 'Nanite限制/约束', 'Nanite可视化', 'Nanite兼容性', 'Nanite最佳实践', 'Virtual Shadow Maps', '几何优先级', 'Nanite LOD调整']
                },
                '图形渲染': {
                    'desc': '渲染管线理解和优化',
                    'difficulty': 3,
                    'dimensions': ['渲染管线/Rendering Pipeline', 'Draw Call绘制调用', 'Command List命令列表', 'RHI渲染硬件接口', '延迟渲染/Forward+', 'GBuffer渲染目标', 'Bloom后处理', 'Tone Mapping色调映射', 'Anti-Aliasing抗锯齿', 'Temporal AA/FSR', 'Shadow级联阴影', 'CSM阴影贴图', 'Ray Tracing渲染', 'Lumen全局光照', 'Nanite几何体', 'TSR时间超采样']
                }
            }
        },
        '游戏客户端工程师': {
            'description': '开发游戏客户端，实现游戏玩法和交互体验。',
            'skills': {
                'C++': {
                    'desc': '游戏客户端高性能开发',
                    'difficulty': 1,
                    'dimensions': ['C++基础语法/数据类型/控制流程', '类和对象/构造函数/析构函数', '继承/多态/虚函数', '模板/STL容器', '智能指针/shared_ptr/unique_ptr', '引用/指针/内存管理', '命名空间/作用域', '异常处理/try-catch', '文件IO/序列化', '多线程/互斥锁', '设计模式/单例/工厂', '游戏引擎基础/Cocos2d-x/Unity', '脚本绑定/Lua-bindings', '性能分析工具', '代码规范/MISRA']
                },
                'Lua': {
                    'desc': '游戏脚本语言，热更新支持',
                    'difficulty': 1,
                    'dimensions': ['Lua基础语法/table/函数', '闭包/元表/metatable', '面向对象/LuaOOP', '协同程序/coroutine', 'LuaJIT/FFI调用', 'C++绑定/LuaBridge', 'xLua/tolua++', '热更新流程/脚本加载', '模块化管理/require', '调试/LuaEditor', 'Lua语法糖/metamethod', '错误处理/pcall/xpcall', '序列化/json', 'Lua与C++交互', 'Lua优化tips']
                },
                'UI系统': {
                    'desc': '游戏UI框架和布局',
                    'difficulty': 2,
                    'dimensions': ['UI布局/相对布局/绝对布局', '多分辨率适配', 'UI层级/Z-Order', '控件/Button/Label/Image', '事件/触摸/点击/拖拽', 'UI动效/渐变/位移动画', '弹窗管理/WindowManager', '提示框/Toast', '进度条/ProgressBar', '列表/TableView/ScrollView', '输入框/InputField', '多语言/Localization', 'UI优化/批处理', '皮肤切换/换肤', 'UI框架设计']
                },
                '任务系统': {
                    'desc': '任务流程设计和状态管理',
                    'difficulty': 2,
                    'dimensions': ['任务定义/接取/完成', '任务类型/主线/支线/日常', '任务状态/已接取/进行中/已完成', '任务配置/表驱动', '任务链/前置任务', '任务奖励/经验/道具', '任务进度追踪', '任务追踪/任务指引', '自动寻路接任务', '任务UI/任务面板', '任务条件/杀怪/采集/对话', '任务刷新/重置', '任务限制/次数/时间', '委托任务/组队任务', '任务事件触发']
                },
                '存档系统': {
                    'desc': '游戏数据持久化',
                    'difficulty': 2,
                    'dimensions': ['数据持久化/SaveData', '本地存档/Json/XML', '加密存档/异或/AES', '云存档/服务器同步', '存档槽位/多个存档', '自动存档/断线保护', '存档版本/兼容处理', '用户数据/UserData', '角色数据/背包/装备', '配置表加载', '存档校验/完整性', '快速保存/AutoSave', '存档导出/导入', '存档冲突处理', '回档机制']
                },
                '对象池': {
                    'desc': '游戏对象复用和性能优化',
                    'difficulty': 2,
                    'dimensions': ['对象池原理/复用', 'PoolManager管理', '预加载/Preload', '对象回收/ReturnObject', '对象创建/CreateObject', '对象销毁/Despawn', '池大小/动态扩容', '异步加载对象', '特效池/粒子池', '角色池/NPC池', '子弹池/弹幕池', 'UI池/预制体池', '内存管理/对象生命周期', '性能监控/命中率', '池监控面板']
                },
                '战斗系统': {
                    'desc': '技能系统、伤害计算、碰撞检测',
                    'difficulty': 2,
                    'dimensions': ['战斗流程/回合制/即时', '属性计算/攻防/暴击', '技能配置/技能表', '技能释放/按键触发', 'CD冷却/能量消耗', '状态效果/BUFF/DEBUFF', '伤害公式/attr公式', '护甲/抗性减伤', '属性加成/百分比', '碰撞检测/AABB/Sphere', '碰撞过滤/LayerMask', '射线检测/Raycast', '区域检测/扇形/圆形', '位移/冲锋/闪烁', '无敌帧/i-Frame']
                },
                '游戏框架': {
                    'desc': '游戏循环、状态机、事件系统',
                    'difficulty': 2,
                    'dimensions': ['游戏循环/GameLoop', '状态机/FSM/状态模式', '有限状态机/FinitStateMachine', '层次状态机/HSM', '行为树/BehaviorTree', '事件系统/EventDispatcher', '观察者模式/Observer', '消息机制/MsgCenter', '模块解耦/模块通信', '管理器/Manager单例', '组件化设计/ECS', '更新循环/Update', 'FixedUpdate物理更新', 'LateUpdate后处理', 'Time时间管理']
                },
                '热更新': {
                    'desc': '资源热更新和代码热修复',
                    'difficulty': 2,
                    'dimensions': ['热更新流程/下载/加载', '资源热更/AssetBundle', '代码热修复/Lua', 'ILRuntime热更新', 'xLua热更新', 'ToLua热更新', '热更新检测/版本号', '差异更新/增量更新', 'CDN分发', '热更新回滚', '热更新安全/校验', 'lua脚本加载', 'AB依赖管理', '资源卸载/Unload', '热更新UI/进度条']
                },
                '网络编程': {
                    'desc': 'TCP/UDP、协议设计、网络同步',
                    'difficulty': 2,
                    'dimensions': ['Socket编程/TCP/UDP', '字节序/网络序', '协议设计/自定义协议', 'Protocol Buffer/FlatBuffers', '粘包处理/分包', '心跳机制/KeepAlive', '断线重连/AutoReconnect', '数据加密/AES/RSA', '请求队列/请求池', '超时处理/重试', '网络库/epoll/select', '异步网络/IOCP', 'Protobuf序列化', 'JSON/二进制协议', '网络监控/延迟显示']
                },
                '资源管理': {
                    'desc': '资源加载、缓存、释放策略',
                    'difficulty': 2,
                    'dimensions': ['资源加载/Resources', '异步加载/AsyncLoad', '资源引用计数', '引用树/AssetReference', '依赖管理/依赖打包', '资源缓存/LRU', '资源释放/UnloadUnused', '纹理压缩/ASTC/ETC2', '图集打包/Atlas', 'Prefab实例化', '场景加载/Loading', '按需加载/LazyLoad', '资源预加载/Preload', '资源版本管理', '内存监控']
                },
                '图形学': {
                    'desc': '渲染原理、坐标变换、光照模型',
                    'difficulty': 3,
                    'dimensions': ['坐标系/世界/本地/屏幕', '矩阵变换/SRT', '向量运算/点积/叉积', '光照模型/Blinn-Phong', 'PBR材质', '法线/Normal', 'UV映射', '纹理贴图', '渲染管线', 'Shader编写', '后处理/Bloom', '抗锯齿/AA', '深度测试/ZBuffer', '模板缓冲/Stencil', '混合模式/BlendMode']
                }
            }
        },
        '游戏服务端工程师': {
            'description': '开发游戏服务器，处理游戏逻辑和数据同步。',
            'skills': {
                'C++': {
                    'desc': '高性能游戏服务器开发',
                    'difficulty': 1,
                    'dimensions': ['C++基础语法/数据类型', '类和对象/继承多态', 'STL容器/算法', '智能指针/内存管理', '多线程编程/thread', '网络编程/socket', '异步IO/EPOLL/IOCP', 'Protocol Buffer', '日志系统/log4cplus', '信号处理/Signal', '进程间通信/IPC', '内存映射/mmap', '文件IO/序列化', '性能分析/profiler', '设计模式']
                },
                'Go': {
                    'desc': '高并发游戏服务端开发',
                    'difficulty': 1,
                    'dimensions': ['Go基础语法/数据类型', 'Goroutine协程', 'Channel通道', 'select多路复用', 'Context上下文', 'defer/panic/recover', 'net/http/http服务', 'net/rpc远程调用', 'database/sql连接池', 'Redis客户端/go-redis', 'gRPC框架', 'json解析', '并发控制/sync包', '性能调优/pprof', '微服务架构']
                },
                'Java': {
                    'desc': '企业级游戏服务器开发',
                    'difficulty': 1,
                    'dimensions': ['Java基础语法', 'OOP/继承/接口', '集合框架/List/Map', '多线程/Thread/Executor', '并发/JUC/ReentrantLock', 'NIO/Netty框架', 'Spring生态', 'MyBatis/Hibernate', '数据库连接池/HikariCP', 'Redis/Jedis', '消息队列/Kafka', '微服务/SpringCloud', '性能调优/JVM', 'GC调优', '设计模式']
                },
                '数据库': {
                    'desc': 'MySQL、Redis数据存储',
                    'difficulty': 1,
                    'dimensions': ['MySQL安装配置', 'SQL增删改查', '索引/Index', '事务/ACID', '隔离级别', '慢查询优化', '主从复制', '分库分表', 'Redis数据类型/String/Hash/List/Set', 'Redis持久化/RDB/AOF', 'Redis集群/主从/Sentinel', 'Redis分布式锁', 'Redis缓存策略', 'MongoDB文档存储', '数据库连接池']
                },
                '匹配系统': {
                    'desc': '玩家匹配算法和房间管理',
                    'difficulty': 2,
                    'dimensions': ['匹配算法/规则匹配', 'Elo积分匹配', 'MMR匹配', '等待队列/WaitQueue', '匹配超时处理', '房间/Room管理', '房间状态/状态机', '玩家加入/离开', '房间广播/广播消息', '快速匹配/QuickMatch', '排位匹配/Ranked', '自定义房间', '匹配冷却/CD', 'ELO算法原理', '玩家数据缓存']
                },
                '压测优化': {
                    'desc': '服务器性能测试和优化',
                    'difficulty': 2,
                    'dimensions': ['压测工具/JMeter/wrk', 'Grafana监控', 'Prometheus指标', 'CPU压测', '内存压测', '网络压测', 'QPS/TPS指标', '响应时间/P99/P95', '瓶颈分析/profiler', '代码优化', 'SQL优化', '缓存优化', '连接池优化', '线程池优化', 'JVM调优']
                },
                '并发编程': {
                    'desc': '多线程、协程、锁机制',
                    'difficulty': 2,
                    'dimensions': ['线程/Thread创建', '线程池/Executor', '互斥锁/Mutex', '读写锁/RWLock', '条件变量/Condition', '信号量/Semaphore', '原子操作/Atomic', 'Coroutine协程', 'Goroutine并发', 'Channel同步', '死锁避免', '乐观锁/悲观锁', '无锁编程', '并发安全', '线程安全集合']
                },
                '战斗校验': {
                    'desc': '服务器端战斗逻辑验证',
                    'difficulty': 2,
                    'dimensions': ['战斗日志/replay', '伤害公式校验', '技能CD校验', '属性校验', '状态叠加校验', '战斗结果验证', '反外挂/数据异常', '帧同步校验/帧验证', '状态一致性', '作弊检测', '伤害飘字', '技能效果判定', '属性加成计算', '战斗录像存储', '异常战斗报告']
                },
                '消息队列': {
                    'desc': 'Kafka、RabbitMQ异步处理',
                    'difficulty': 2,
                    'dimensions': ['MQ队列概念', 'Kafka架构/Broker/Topic/Partition', 'Kafka生产者/消费者', 'Kafka分区策略', 'Kafka消费者组', 'Kafka可靠性/acks', 'Kafka性能调优', 'RabbitMQ架构/Exchange/Queue', 'RabbitMQ交换机类型', 'RabbitMQ消息确认', '死信队列/DLQ', '延迟队列', '消息顺序性', '消息幂等性', 'MQ监控']
                },
                '网络编程': {
                    'desc': 'Socket、TCP/UDP、IO多路复用',
                    'difficulty': 2,
                    'dimensions': ['TCP三次握手/四次挥手', 'Socket编程', '粘包处理/协议解析', '心跳机制', '断线重连', '非阻塞IO/NIO', 'IO多路复用/epoll/select', 'IOCP异步IO', 'Protocal Buffer编码', '二进制协议', '数据加密/TLS', '高并发架构', '连接池', '流量控制/窗口', '网络模型']
                },
                '防作弊': {
                    'desc': '外挂检测和数据校验',
                    'difficulty': 2,
                    'dimensions': ['客户端检测/内存扫描', '协议检测/数据分析', '行为检测/异常模式', '机器学习异常检测', '签名校验/完整性', '数据加密/混淆', '服务器校验', '战斗日志记录', '异常数据告警', '封禁机制/Ban', 'IP限制/设备指纹', '举报系统', '反调试/anti-debug', '虚拟机检测', '多开检测']
                },
                '分布式系统': {
                    'desc': '服务拆分、负载均衡、容错',
                    'difficulty': 3,
                    'dimensions': ['微服务架构/SOA', '服务注册发现', '负载均衡/LB', '服务治理', '限流熔断/Sentinel', '降级兜底', '配置中心/Nacos', '网关/Gateway', '分布式事务/2PC/TCC', '消息总线', '服务监控/Skywalking', '链路追踪', '容器化/Docker/K8s', '服务网格/Istio', '高可用/多机房部署']
                },
                '游戏同步': {
                    'desc': '状态同步、帧同步、预测回滚',
                    'difficulty': 3,
                    'dimensions': ['状态同步/State Sync', '帧同步/Lockstep', '输入延迟/Input Lag', '预测回滚/Rollback', '可靠UDP/KCP/ENet', '网络延迟补偿', '服务器权威', '客户端预测', '误差校正/Reconciliation', '帧率同步', '断线重连同步', '录像回放/Replay', '延迟模拟', '带宽优化', '同步协议设计']
                }
            }
        }
    },
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
