"""前端开发工程师数据"""
data = {
    '计算机与信息技术': {
        '软件工程': {
            '前端开发工程师': {
                'description': '负责网站和Web应用的前端开发，将UI设计转化为可交互的页面。',
                'skills': {
                    'CSS': {
                        'desc': '层叠样式表，用于控制网页的视觉表现，包括布局、颜色、字体、动画、响应式设计等',
                        'difficulty': 1,
                        'dimensions': [
                            ['选择器与优先级', '基础选择器', '组合器', '伪类与伪元素', '优先级计算', '层叠与继承'],
                            ['盒模型与布局', '盒模型(content-box/border-box)', 'BFC与IFC', '外边距合并', 'display属性', '浮动与清除'],
                            ['现代布局', 'Flexbox容器与项目属性', 'Grid布局与命名区域', '定位(absolute/relative/fixed/sticky)', '响应式布局'],
                            ['视觉与动画', '过渡', '关键帧动画', '2D/3D变换', '阴影与渐变', '滤镜与混合模式', 'clip-path与mask'],
                            ['响应式与单位', '媒体查询与断点', 'rem/vw/vh/dvw单位', 'CSS变量', '容器查询'],
                            ['工程化与组织', '预处理器(SCSS/Less)变量与混合', '@import与@use', 'CSS Modules', 'CSS-in-JS', 'Tailwind等原子类']
                        ]
                    },
                    'Git': {
                        'desc': '分布式版本控制系统，用于代码管理和团队协作',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础与配置', '安装与配置', 'SSH密钥', 'git init', 'clone', '工作区/暂存区/仓库'],
                            ['日常操作', 'add/commit/status', 'git diff', 'log与reflog', 'git reset与revert', 'stash暂存'],
                            ['分支与合并', 'branch与checkout', 'merge与rebase', 'cherry-pick', '冲突解决', '分支策略(Git Flow/Trunk)'],
                            ['远程协作', 'remote/push/pull/fetch', 'Pull Request流程', '标签管理', '子模块'],
                            ['内部原理', '对象模型(blob/tree/commit)', '引用与HEAD', '垃圾回收']
                        ]
                    },
                    'HTML': {
                        'desc': '超文本标记语言，用于定义网页的内容结构和语义，包括标签、属性、表单、多媒体嵌入等',
                        'difficulty': 1,
                        'dimensions': [
                            ['文档结构与语义', 'DOCTYPE与html结构', 'meta/link/script标签', '语义化标签(header/nav/main/article)', '可访问性基础'],
                            ['表单与交互', 'form与input类型', '验证与约束', 'label与fieldset', '新input类型(date/color/range)'],
                            ['多媒体与嵌入', 'img与srcset/sizes', 'video/audio', 'iframe', 'figure与figcaption'],
                            ['SEO与性能', 'meta标签优化', '结构化数据(JSON-LD)', '懒加载', '关键渲染路径优化']
                        ]
                    },
                    'JavaScript': {
                        'desc': '网页脚本语言，用于实现页面交互功能、DOM操作、事件处理、异步请求等动态效果',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础类型与操作', '数据类型', '类型转换', '运算符', '严格模式', 'Symbol/Map/Set/WeakMap等'],
                            ['执行与作用域', 'var/let/const', '作用域链', '闭包', '执行上下文与调用栈'],
                            ['原型与面向对象', '原型与原型链', '类与继承', 'this绑定'],
                            ['异步编程', '事件循环(宏/微任务)', '回调', 'Promise', 'async/await', 'Generator'],
                            ['DOM与事件', 'DOM查询/创建/修改', '事件模型(捕获/冒泡)', '事件委托', 'BOM基础'],
                            ['模块化与工程化', 'ES Module导入导出', 'CommonJS与AMD', '动态导入', '错误处理'],
                            ['其他进阶', 'Proxy与Reflect', '正则表达式', '模板字符串', '可选链与空值合并']
                        ]
                    },
                    'TypeScript': {
                        'desc': 'JavaScript的超集，提供静态类型检查、接口定义和更好的IDE支持',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础类型系统', '基础类型(string/number/boolean等)', '字面量类型', '类型推断', '类型断言', '联合/交叉类型'],
                            ['接口与类型别名', '接口定义与扩展', '类型别名', '索引签名', '元组与枚举'],
                            ['函数与泛型', '函数类型声明', '泛型函数与约束', '泛型工具类型(Partial/Required/Pick/Omit)', '条件类型'],
                            ['类与模块', '类与访问修饰符', '抽象类', '模块解析', '命名空间', '声明文件与三斜线指令'],
                            ['配置与工程', 'tsconfig.json配置', 'strict选项', '模块解析策略', '装饰器(实验性)', '类型声明与全局扩展']
                        ]
                    },
                    'npm/yarn/pnpm': {
                        'desc': 'JavaScript包管理工具，用于安装和管理项目依赖',
                        'difficulty': 1,
                        'dimensions': [
                            ['依赖管理', 'install/add/remove', 'dependencies/devDependencies/peer', '语义化版本(^ ~)', 'lock文件'],
                            ['脚本与运行', 'scripts', 'npx/yarn dlx', '生命周期钩子', '环境变量'],
                            ['工作区与Monorepo', 'yarn workspaces', 'pnpm workspace', '软链接与提升'],
                            ['发布与配置', 'package.json字段', 'npm publish', 'registry与镜像', '安全审计']
                        ]
                    },
                    'ES6+': {
                        'desc': '现代JavaScript语法，包括箭头函数、解构赋值、Promise、async/await等',
                        'difficulty': 2,
                        'dimensions': [
                            ['变量与解构', 'let/const', '解构赋值', '展开运算符', '默认参数'],
                            ['函数与类', '箭头函数', 'class与extends', 'super', '模块导入导出'],
                            ['异步处理', 'Promise', 'async/await', 'for...of与迭代器', '生成器'],
                            ['数据结构扩展', 'Set/Map/Weak', 'Symbol', 'Proxy/Reflect', '可选链?.', '空值合并??'],
                            ['数组与字符串方法', 'find/findIndex/flat/flatMap', 'includes/startsWith/endsWith', 'padStart/padEnd'],
                            ['对象新特性', 'Object.assign/keys/values/entries', 'fromEntries', 'Object.freeze/seal', 'globalThis']
                        ]
                    },
                    'React': {
                        'desc': 'Facebook开发的组件化UI库，使用虚拟DOM和单向数据流构建复杂的单页应用',
                        'difficulty': 2,
                        'dimensions': [
                            ['组件基础', 'JSX', '函数组件与类组件', 'Props与PropTypes', '事件处理'],
                            ['Hooks核心', 'useState/useEffect', 'useContext', 'useReducer', 'useMemo/useCallback', 'useRef', '自定义Hook'],
                            ['状态管理与路由', 'React Context', 'Redux/Zustand', 'React Router v6', '数据流'],
                            ['性能与优化', '虚拟DOM与Diff', 'Fiber架构', 'React.memo', '代码分割与React.lazy', '虚拟列表', 'Profiler'],
                            ['样式与测试', 'CSS Modules', 'styled-components', 'Tailwind CSS', 'Jest与React Testing Library'],
                            ['服务端渲染', 'Next.js基础', 'SSR/SSG/ISR', 'Server Components', '路由文件系统']
                        ]
                    },
                    'Sass/Less': {
                        'desc': 'CSS预处理器，提供变量、嵌套、混合等高级特性',
                        'difficulty': 2,
                        'dimensions': [
                            ['变量与嵌套', '变量定义与作用域', '嵌套规则', '父选择器&', '属性嵌套'],
                            ['混合与继承', '@mixin与@include', '参数混合', '@extend与占位符', '混合vs继承'],
                            ['函数与指令', '内置函数(颜色/数学/列表)', '自定义函数', '@if/@for/@each/@while', 'map与list操作'],
                            ['模块化', '@import与@use/@forward', '命名空间', '配置变量', '与PostCSS集成']
                        ]
                    },
                    'Tailwind CSS': {
                        'desc': '实用优先的CSS框架，通过原子类快速构建自定义设计',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心设计', '实用优先与类名组合', '响应式前缀(sm/md/lg)', '状态变体(hover/focus/group)'],
                            ['布局与定位', 'Flex与Grid', '定位(relative/absolute)', 'display属性', '间距控制(m/p)'],
                            ['样式与定制', '颜色/字体/阴影', '圆角与边框', '动画', '自定义配置(tailwind.config.js)', 'darkMode'],
                            ['性能与优化', 'JIT模式', 'purge/优化配置', '与组件库搭配']
                        ]
                    },
                    'Vite': {
                        'desc': '新一代前端构建工具，提供极速的开发服务器启动和热更新',
                        'difficulty': 2,
                        'dimensions': [
                            ['配置与开发', 'vite.config.js', '环境变量(.env)', 'CSS预处理器', '静态资源处理'],
                            ['开发服务器', '热更新(HMR)', 'TypeScript支持', 'ES模块开发'],
                            ['构建与优化', 'Rollup构建', '代码分割', 'Tree Shaking', '预构建', 'SSR与SSG'],
                            ['插件与扩展', 'Vite插件API', '常用插件', '多页面应用']
                        ]
                    },
                    'Vue': {
                        'desc': '渐进式JavaScript框架，提供响应式数据绑定和组件化开发',
                        'difficulty': 2,
                        'dimensions': [
                            ['模板与指令', '插值', 'v-bind/v-on/v-model', 'v-if/v-show', 'v-for', '计算属性与侦听器'],
                            ['组件基础', 'Props与$emit', '插槽', '组件注册', '生命周期钩子', '组合式API(setup)'],
                            ['响应式与状态', 'ref/reactive', 'computed', 'watch', 'Pinia状态管理', 'Vue Router'],
                            ['进阶特性', 'Teleport', 'Suspense', '过渡动画', '自定义指令', '插件'],
                            ['服务端渲染', 'Nuxt基础', 'SSR/SSG', 'Composition API in SSR']
                        ]
                    },
                    'Webpack': {
                        'desc': '前端模块打包工具，支持代码分割、资源优化和开发服务器',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心概念', 'entry/output/loader/plugin', 'mode(dev/prod)', 'source map'],
                            ['Loader与插件', 'babel-loader', 'css-loader/style-loader', 'HtmlWebpackPlugin', 'MiniCssExtractPlugin'],
                            ['代码分割与缓存', 'splitChunks', '动态导入', 'Tree Shaking', '持久化缓存', '模块联邦'],
                            ['优化与构建', 'resolve别名', 'externals', '多页面应用', '构建速度分析', '生产环境优化']
                        ]
                    },
                    '浏览器兼容性': {
                        'desc': '处理不同浏览器的渲染差异，使用polyfill和特性检测',
                        'difficulty': 2,
                        'dimensions': [
                            ['策略与工具', 'caniuse', 'Browserslist', 'Autoprefixer', 'polyfill与core-js', 'babel-preset-env'],
                            ['CSS兼容', 'CSS Reset/Normalize', '优雅降级与渐进增强', 'hack与条件注释'],
                            ['API Polyfill', 'fetch/Promise polyfill', 'IntersectionObserver', 'CSS变量降级', '特性检测']
                        ]
                    },
                    '移动端适配': {
                        'desc': '响应式布局、rem/vw适配、触摸事件处理等移动端开发技术',
                        'difficulty': 2,
                        'dimensions': [
                            ['视口与单位', 'viewport meta', 'dpr', 'rem/vw/vh', '1px边框问题'],
                            ['触摸与手势', 'touch事件', '300ms延迟与fastclick', '手势库', '滚动穿透'],
                            ['布局与适配', 'Flexbox/Grid', '安全区域(safe-area)', '刘海屏适配', '响应式图片'],
                            ['调试与工具', 'vconsole', '移动端Chrome DevTools', '真机调试', 'webview']
                        ]
                    },
                    '前端性能优化': {
                        'desc': '代码分割、懒加载、缓存策略、资源压缩等性能提升技术',
                        'difficulty': 3,
                        'dimensions': [
                            ['性能度量', 'Core Web Vitals(FCP/LCP/CLS)', 'Lighthouse', 'Performance API', 'PerformanceObserver'],
                            ['加载优化', '资源压缩(Gzip/Brotli)', '图片优化(WebP/AVIF)', 'CDN与HTTP/2', '懒加载与预加载'],
                            ['缓存策略', '强缓存(Cache-Control/Expires)', '协商缓存(ETag/Last-Modified)', 'Service Worker', 'Workbox'],
                            ['渲染与执行优化', '重排与重绘', 'GPU加速', '虚拟列表', '防抖与节流', '代码分割与动态导入'],
                            ['架构优化', 'SSR与SSG', '骨架屏与Loading', '资源预连接(preconnect)', 'Font优化']
                        ]
                    }
                }
            }
        }
    }
}