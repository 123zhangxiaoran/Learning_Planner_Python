"""移动端开发工程师数据"""
data = {
    '计算机与信息技术': {
        '软件工程': {
            '移动端开发工程师': {
                'description': '开发iOS和Android移动应用，实现原生或跨平台功能。',
                'skills': {
                    'Java': {
                        'desc': 'Android传统开发语言，生态成熟',
                        'difficulty': 1,
                        'dimensions': [
                            ['语言基础', '数据类型', '控制流', '面向对象(类/继承/多态)', '异常处理(try-catch/finally)'],
                            ['集合与泛型', 'List/Set/Map', 'ArrayList/HashMap', '泛型与装箱拆箱', 'Lambda与函数式接口'],
                            ['并发与IO', 'Thread/Runnable', 'ExecutorService', 'synchronized/volatile', 'IO流与序列化'],
                            ['JVM基础', '内存区域', '类加载', '垃圾回收', 'JVM参数调优'],
                            ['Android核心', '四大组件', 'Activity生命周期', 'Intent与IntentFilter', 'Fragment', 'Service与BroadcastReceiver'],
                            ['UI与布局', 'ConstraintLayout/LinearLayout', '自定义View', '事件分发', 'RecyclerView', 'Handler与消息机制'],
                            ['Jetpack与构建', 'ViewModel/LiveData', 'Room数据库', 'Navigation', 'Gradle与依赖', 'APK打包与混淆']
                        ]
                    },
                    'Kotlin': {
                        'desc': 'Android官方推荐开发语言，与Java完全互操作',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础语法', '变量(var/val)', '空安全', '类型推断', '函数与默认参数', '扩展函数'],
                            ['面向对象与集合', '类/数据类/密封类', '接口与抽象类', '集合操作(filter/map/reduce)', '解构', 'lateinit与lazy'],
                            ['高阶函数与泛型', 'Lambda表达式', '内联函数', '泛型与协变/逆变', '运算符重载', 'DSL'],
                            ['协程并发', 'suspend/async/await', 'CoroutineScope', 'Dispatchers', 'Flow(冷流/热流)', 'Channel与Flow操作符'],
                            ['协程测试与多平台', 'runTest', 'withContext', '协程取消', 'KMM多平台', '与Java互调']
                        ]
                    },
                    'Swift': {
                        'desc': 'Apple开发的iOS应用编程语言，现代、安全、高效',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础与可选值', '变量(let/var)', '可选型与解包(guard/if let)', '函数与闭包', '尾随闭包'],
                            ['类型与协议', '类/结构体/枚举', '协议与扩展', '属性(计算/懒加载)', '下标', '泛型'],
                            ['内存与错误', 'ARC/强引用/弱引用', 'weak/unowned', 'do-catch错误处理', 'Result类型'],
                            ['并发与响应式', 'async/await', 'Actor并发模型', 'TaskGroup', 'Combine框架', 'SwiftUI声明式UI'],
                            ['生态与测试', 'Swift Package Manager', 'XCTest单元测试', 'Copy-on-write', 'String/字符处理']
                        ]
                    },
                    'App发布': {
                        'desc': '应用商店审核流程和发布管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['商店与证书', 'App Store Connect', 'Google Play Console', '证书与Provisioning Profile', '签名密钥与keystore'],
                            ['上架准备', '应用图标与截图', '应用描述与关键词', '隐私政策与权限声明', '年龄分级', '多语言本地化'],
                            ['测试与发布', 'TestFlight/iOS测试', 'Google Play内测/公测', 'AAB与APK打包', '灰度与百分比发布', '版本号管理'],
                            ['审核与优化', '审核指南与常见被拒', 'App Store审核上诉', 'ASO优化', '崩溃报告(Crashlytics)', '应用更新与增量更新'],
                            ['合规与推广', '用户数据收集声明', '热修复政策', '应用下架与重新上架', 'ASA/Google Ads推广', '多平台分发']
                        ]
                    },
                    'Flutter': {
                        'desc': 'Google跨平台UI框架，使用Dart语言，一套代码多端运行',
                        'difficulty': 2,
                        'dimensions': [
                            ['Widget基础', 'StatelessWidget/StatefulWidget', '生命周期', '布局Widget(Row/Column/Stack)', '常用容器(Container/Padding)'],
                            ['列表与滚动', 'ListView/GridView', 'CustomScrollView', 'ScrollController', '下拉刷新与上拉加载'],
                            ['状态管理', 'setState', 'Provider', 'Bloc', 'Riverpod', 'GetX'],
                            ['网络与存储', 'dio/http', 'JSON解析(json_serializable)', 'SharedPreferences/sqflite', '图片缓存'],
                            ['路由与导航', 'Navigator与命名路由', 'go_router', '路由守卫', '嵌套路由'],
                            ['原生交互与插件', 'Platform Channel', '权限管理', '推送/地图/支付插件', '国际化(intl)'],
                            ['构建与测试', 'Hot Reload', 'APK/AAB构建', '混淆(Dart obfuscate)', 'flutter_test单元测试', 'CI/CD(Codemagic)']
                        ]
                    },
                    'React Native': {
                        'desc': '使用React构建原生移动应用的框架',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心组件', 'View/Text/Image', 'TextInput', 'StyleSheet', 'Flexbox布局'],
                            ['列表与滚动', 'FlatList', 'SectionList', 'ScrollView', '下拉刷新/上拉加载', '虚拟列表优化'],
                            ['导航与路由', 'React Navigation', 'Stack/Tab/Drawer', '路由传参', 'Deep Link'],
                            ['状态管理', 'Context与useContext', 'Redux', 'Zustand', 'MobX', '自定义Hook'],
                            ['动画与手势', 'Animated', 'Reanimated', 'Lottie', 'Gesture Handler', 'PanResponder'],
                            ['原生模块与性能', 'Native Modules', 'JSI与TurboModule', 'Hermes引擎', 'JS Bundle打包', '性能优化(FlashList)'],
                            ['测试与部署', 'Jest单元测试', 'Detox E2E测试', 'Fastlane自动化', 'CodePush热更新', 'iOS/Android打包签名']
                        ]
                    },
                    '地图定位': {
                        'desc': 'GPS定位、地图SDK集成',
                        'difficulty': 2,
                        'dimensions': [
                            ['定位技术', 'GPS/基站/WiFi定位', '定位精度与模式', 'Android定位(FusedLocation)', 'iOS定位(CoreLocation)', '前台/后台定位'],
                            ['地图SDK', '高德/百度/腾讯/Google地图', 'MapView初始化', '地图类型与控件', 'Marker与InfoWindow', '自定义标记'],
                            ['坐标与围栏', 'WGS-84/GCJ-02/BD-09坐标', '坐标转换', '逆地理编码', '地理围栏', '室内定位'],
                            ['路径与搜索', '路径规划(步行/驾车)', 'POI搜索', '周边搜索', '导航与路线引导', '地图覆盖物(Polygon/Polyline)'],
                            ['优化与配置', '定位省电策略', '后台定位保活', '离线地图', 'API Key配置', '混淆与权限']
                        ]
                    },
                    '推送服务': {
                        'desc': 'APNs、FCM等推送通知集成',
                        'difficulty': 2,
                        'dimensions': [
                            ['推送原理与平台', '推送原理(长连接)', 'APNs与证书/Auth Key', 'FCM与VAPID Key', '消息类型(通知/数据)', 'Device Token管理'],
                            ['本地与远程推送', '本地推送', '前台/后台/静默推送', '推送Payload(title/body/badge)', 'VoIP推送', 'iOS实时活动(灵动岛)'],
                            ['第三方推送', '极光推送/友盟推送', '华为/小米/OPPO厂商推送', '个推(Getui)', '送达率与点击率统计'],
                            ['交互与策略', '通知渠道(Channel/Category)', '交互式通知(Actions)', '推送点击跳转(Deep Link)', '标签/分群推送', '推送定时与群发'],
                            ['高级与调试', '推送测试', '角标管理', '防打扰/静默期', '推送失败与Token刷新', '主题订阅']
                        ]
                    },
                    '支付集成': {
                        'desc': '微信支付、支付宝、Apple Pay等',
                        'difficulty': 2,
                        'dimensions': [
                            ['支付流程与平台', '支付流程(下单/支付/回调)', '微信支付(商户号/APPID)', '支付宝(商户号/APPID)', 'Apple Pay(Merchant ID)', 'Google Pay API'],
                            ['调起与签名', '微信SDK调起与签名', '支付宝SDK调起与验签', 'Apple Pay支付请求(PKPaymentRequest)', '生物识别支付(指纹/Face ID)'],
                            ['结果与退款', '支付回调(异步通知)', '支付结果轮询', '退款流程与回调', '对账与平账', '风控与异常检测'],
                            ['多支付与安全', '银联/Stripe/PayPal', '聚合支付', 'H5支付/扫码支付', '支付加密与防篡改', '支付日志与统计']
                        ]
                    },
                    '混合开发': {
                        'desc': 'WebView、Cordova、Ionic等混合应用方案',
                        'difficulty': 2,
                        'dimensions': [
                            ['WebView与JSBridge', 'WebView配置与加载', 'JSBridge原理', 'JS调用原生', '原生调JS(evaluateJS)', '离线包与预加载'],
                            ['混合框架', 'Cordova/PhoneGap', 'Ionic(Angular/React)', 'Capacitor', 'React Native/Flutter原生交互'],
                            ['交互与功能', 'H5调用相机/相册', 'H5调用定位/分享', 'H5调起支付', 'H5推送', '微信JS-SDK集成'],
                            ['通信与共享', 'WebSocket实时通讯', 'Cookie/Token共享', 'Native Scheme/URL Scheme', 'App Link/通用链接', '共享登录态'],
                            ['调试与优化', 'H5页面调试(DevTools)', 'Safari远程调试', 'WebView性能优化', '硬件加速', '安全(XSS/HTTPS)']
                        ]
                    },
                    '移动端UI': {
                        'desc': '移动端设计规范、适配不同屏幕尺寸',
                        'difficulty': 2,
                        'dimensions': [
                            ['屏幕与单位', '设计尺寸(pt/dp/sp)', '分辨率与DPI/PPI', '刘海屏/水滴屏/挖孔屏', '安全区域(Safe Area)', '状态栏/导航栏高度'],
                            ['设计规范', 'iOS HIG规范', 'Material Design(MD3)', '颜色系统(主色/辅色)', '字体层级(Typography)', '间距与圆角系统'],
                            ['布局与适配', '响应式布局', 'Flexbox/Grid', 'ConstraintLayout/Auto Layout', 'smallestWidth适配', '图片@1x/@2x/@3x适配'],
                            ['组件与状态', '设计系统与组件库', '按钮状态(正常/按下/禁用)', '空状态/加载/错误状态', '导航设计(Tab/底部导航)', '暗色模式与主题切换'],
                            ['动画与验收', '过渡动画/微交互', '手势(滑动/长按/双击)', '多语言/i18n', 'UI验收与设计还原', 'App Store截图规范']
                        ]
                    },
                    'Android开发': {
                        'desc': 'Android SDK、Jetpack组件、Material Design',
                        'difficulty': 3,
                        'dimensions': [
                            ['架构与组件', 'MVC/MVP/MVVM架构', 'Activity启动模式', 'Service(前台/后台)', 'BroadcastReceiver', 'ContentProvider'],
                            ['View体系', '自定义View(测量/布局/绘制)', 'Canvas/Paint/Bitmap', '属性动画', 'RecyclerView与DiffUtil', 'ViewBinding/DataBinding'],
                            ['Jetpack核心', 'Lifecycle与ViewModel', 'LiveData/Flow', 'Navigation', 'Room数据库', 'Paging分页', 'WorkManager'],
                            ['Jetpack扩展', 'DataStore', 'Hilt依赖注入', 'Startup启动优化', 'Compose声明式UI', 'Material Design组件'],
                            ['进阶与优化', 'Kotlin协程与Flow', 'Clean架构/UseCase', '模块化/组件化', '热修复(Tinker)', '性能优化(启动/内存/布局)'],
                            ['安全与监控', 'APK安全加固', '混淆与反编译', 'Hook与反射', 'APM性能监控', 'LeakCanary/内存泄漏排查']
                        ]
                    },
                    'iOS开发': {
                        'desc': 'UIKit、SwiftUI、Core Data等iOS框架',
                        'difficulty': 3,
                        'dimensions': [
                            ['UIKit基础', 'UIViewController与生命周期', 'UIView与响应链', 'Auto Layout/Masonry/SnapKit', 'Size Class', '安全区域适配'],
                            ['列表与集合视图', 'UITableView/UICollectionView', 'DiffableDataSource', 'Compositional Layout', 'Cell预加载与复用'],
                            ['动画与图形', 'UIView动画', 'Core Animation', 'Core Graphics/Quartz 2D', 'Core Image', '贝塞尔曲线'],
                            ['Web与交互', 'WKWebView与JS交互', '手势识别(UIGestureRecognizer)', 'UINavigationController', 'TabBar与Modal呈现'],
                            ['SwiftUI与响应式', 'SwiftUI声明式语法', '@State/@Binding/@ObservedObject', 'Combine框架', 'List/ForEach/NavigationStack', 'Sheet/FullScreenCover'],
                            ['数据与存储', 'Core Data', 'SQLite/Realm', 'UserDefaults/Keychain', 'FileManager沙盒', 'URLSession网络'],
                            ['系统服务与并发', 'Core Location/MapKit', 'AVFoundation', 'Photos/Contacts', 'Widget/WidgetKit', 'Swift Concurrency(async/await)']
                        ]
                    },
                    '性能优化': {
                        'desc': '启动优化、内存管理、电量优化',
                        'difficulty': 3,
                        'dimensions': [
                            ['启动优化', '冷/热/温启动', '启动流程分析', '二进制重排(Page In)', '懒加载与预加载', '启动窗口与耗时打点'],
                            ['内存与卡顿', '内存泄漏(LeakCanary/Instruments)', '循环引用', '离屏渲染', '卡顿检测(Method Swizzling/Runloop)', '帧率FPS监控'],
                            ['图片与列表', '图片编解码优化', 'WebP/HEIC格式', '大图降采样', '列表Cell复用与预加载', 'DiffUtil/预估高度'],
                            ['网络与IO', '请求合并与缓存', 'Gzip压缩', 'CDN加速', 'Keep-Alive', '磁盘缓存策略(LRU/FIFO)'],
                            ['包体积与功耗', '无用资源清理', '代码混淆', '动态库与资源优化', '电量监控', '后台任务与省电'],
                            ['监控与工具', 'APM性能上报', 'Xcode Instruments', 'Android Profiler', '性能打点', '线上监控与告警']
                        ]
                    },
                    '热更新': {
                        'desc': '动态下发代码修复线上问题',
                        'difficulty': 3,
                        'dimensions': [
                            ['原理与策略', '热更新原理', 'iOS政策限制', '强制更新/静默更新', '语义化版本', '灰度发布/AB测试'],
                            ['Android方案', 'Tinker原理与集成', '差量合成与Patch', '加载流程', 'Robust/Andfix', '资源与So补丁'],
                            ['跨平台方案', 'React Native CodePush', 'JS Bundle分离', 'Flutter热更新/热重启', '小程序热更新', 'H5离线包更新'],
                            ['引擎与安全', 'JS引擎(Hermes/JSCore)', 'Lua脚本更新', 'Wasm更新', '补丁签名与校验', '热更新回退机制'],
                            ['运维与监控', '下载管理与断点续传', '推送与提示', '更新统计', '热更新失败处理', '功能开关/远程配置']
                        ]
                    }
                }
            }
        }
    }
}