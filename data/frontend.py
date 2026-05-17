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
                        ['选择器语法', '优先级计算', '层叠规则', '继承机制'],
                        ['盒模型', 'BFC机制', '外边距合并'],
                        ['Flexbox布局', 'Grid布局'],
                        ['定位', 'absolute', 'fixed', 'relative', 'sticky'],
                        ['display属性', '浮动'],
                        ['响应式设计', '媒体查询', 'rem/vw单位'],
                        ['CSS变量', '阴影效果', '渐变', '滤镜', '混合模式'],
                        ['过渡动画', '关键帧动画', '2D/3D变换'],
                        ['伪类伪元素', 'group-hover', 'first', 'last', 'odd', 'even'],
                        ['CSS新特性']
                    ]
                },
                'Git': {
                    'desc': '分布式版本控制系统，用于代码管理和团队协作',
                    'difficulty': 1,
                    'dimensions': [
                        ['Git安装配置', 'SSH密钥配置'],
                        ['工作区', '暂存区', '仓库', 'git init', 'add', 'commit', 'status'],
                        ['git diff', 'log', 'reflog'],
                        ['git reset', 'revert', 'checkout', 'branch'],
                        ['git merge', 'rebase'],
                        ['git stash', 'pop'],
                        ['远程仓库操作', 'git clone', 'pull', 'push', 'fetch'],
                        ['分支管理策略'],
                        ['冲突解决', 'cherry-pick'],
                        ['标签管理', '子模块'],
                        ['Git内部原理']
                    ]
                },
                'HTML': {
                    'desc': '超文本标记语言，用于定义网页的内容结构和语义，包括标签、属性、表单、多媒体嵌入等',
                    'difficulty': 1,
                    'dimensions': [
                        ['HTML标签与属性', 'DOCTYPE声明', '字符实体'],
                        ['表单', 'input类型', '表单验证'],
                        ['多媒体嵌入', '图片img和srcset', '超链接a'],
                        ['文档结构', 'meta标签', 'link/script标签'],
                        ['语义化标签'],
                        ['SEO优化', '可访问性', 'ARIA属性'],
                        ['HTML5新标签'],
                        ['table表格', '列表ul', 'ol', 'dl'],
                        ['iframe内联框架']
                    ]
                },
                'JavaScript': {
                    'desc': '网页脚本语言，用于实现页面交互功能、DOM操作、事件处理、异步请求等动态效果',
                    'difficulty': 1,
                    'dimensions': [
                        ['数据类型', '值类型', '引用类型', '类型转换', 'Symbol'],
                        ['原型链', '原型继承', '闭包'],
                        ['作用域', 'var', 'let', 'const', '执行上下文', '严格模式'],
                        ['事件循环', '宏任务', '微任务'],
                        ['Promise', 'async', 'await', 'Generator', 'Iterator'],
                        ['Map', 'Set', 'WeakMap', 'WeakSet', 'Proxy', 'Reflect'],
                        ['JSON', '正则表达式', '模板字符串'],
                        ['模块化', 'CommonJS', 'ES Module', '模块导入导出'],
                        ['DOM操作', '事件处理', '事件委托', '冒泡', '捕获'],
                        ['BOM操作', 'AJAX', 'Fetch', 'Web Storage'],
                        ['解构赋值', '展开运算符', '箭头函数', '类', '错误处理']
                    ]
                },
                'TypeScript': {
                    'desc': 'JavaScript的超集，提供静态类型检查、接口定义和更好的IDE支持',
                    'difficulty': 2,
                    'dimensions': [
                        ['基础类型', 'string', 'number', 'boolean', 'null', 'undefined', 'void', 'never', 'any'],
                        ['接口', '类型别名'],
                        ['元组', '枚举', '数组类型'],
                        ['函数类型', '类型推断', '类型断言'],
                        ['泛型', '泛型约束', '泛型工具类型', 'Pick', 'Omit', 'Partial', 'Required', 'Record', 'Exclude', 'Extract'],
                        ['交叉类型', '联合类型', '类型保护', '类型守卫'],
                        ['声明文件', '声明'],
                        ['装饰器', '命名空间', '模块'],
                        ['模块解析', 'tsconfig配置', 'strict模式']
                    ]
                },
                'npm/yarn/pnpm': {
                    'desc': 'JavaScript包管理工具，用于安装和管理项目依赖',
                    'difficulty': 1,
                    'dimensions': [
                        ['包安装', 'npm install', 'yarn add', 'pnpm add', '包卸载', 'npm uninstall', 'remove'],
                        ['版本管理', '语义化版本', '^', '~'],
                        ['package.json配置', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml'],
                        ['npx执行命令', 'npm scripts钩子'],
                        ['依赖类型', 'dependencies', 'devDependencies', 'peerDependencies'],
                        ['Node版本管理', 'nvm', 'n'],
                        ['工作区', 'yarn workspace', '软链接'],
                        ['npm publish', '镜像源配置', '缓存管理'],
                        ['吊装']
                    ]
                },
                'ES6+': {
                    'desc': '现代JavaScript语法，包括箭头函数、解构赋值、Promise、async/await等',
                    'difficulty': 2,
                    'dimensions': [
                        ['let', 'const', '模板字符串', '箭头函数'],
                        ['解构赋值', '展开运算符', '剩余参数', '默认参数'],
                        ['Promise', 'async', 'await', '类', '模块导入导出'],
                        ['Symbol', '迭代器', '生成器', '迭代器协议', 'for...of循环'],
                        ['Set', 'Map', 'WeakSet', 'WeakMap'],
                        ['Proxy', 'Reflect', '可选链?.', '空值合并??'],
                        ['字符串方法', 'includes', 'repeat', 'padStart', 'padEnd'],
                        ['数组方法', 'map', 'filter', 'reduce', 'find', 'some', 'every', 'findIndex', 'flat', 'flatMap'],
                        ['对象方法', 'Object.assign', 'keys', 'values', 'entries', 'fromEntries'],
                        ['BigInt', 'globalThis']
                    ]
                },
                'React': {
                    'desc': 'Facebook开发的组件化UI库，使用虚拟DOM和单向数据流构建复杂的单页应用',
                    'difficulty': 2,
                    'dimensions': [
                        ['JSX语法', '元素渲染'],
                        ['组件定义', 'function', 'class', 'Props', '事件处理'],
                        ['自定义Hook', 'React.memo', 'React.lazy'],
                        ['条件渲染', '列表渲染', '状态提升', '组合', '继承'],
                        ['Context', 'Refs', 'Portal', '错误边界'],
                        ['生命周期', 'componentDidMount', 'componentDidUpdate', 'componentWillUnmount'],
                        ['Hooks', 'useState', 'useEffect', 'useContext', 'useReducer', 'useCallback', 'useMemo', 'useRef'],
                        ['虚拟DOM', 'Diff算法', 'Fiber架构'],
                        ['性能优化', '虚拟列表'],
                        ['React Router', '状态管理', 'Redux', 'Zustand'],
                        ['CSS方案', 'styled-components', 'css modules', 'tailwind'],
                        ['TypeScript配合', '单元测试', 'Jest', 'Testing Library'],
                        ['Next.js', '服务端组件', 'SSR', 'RSC']
                    ]
                },
                'Sass/Less': {
                    'desc': 'CSS预处理器，提供变量、嵌套、混合等高级特性',
                    'difficulty': 2,
                    'dimensions': [
                        ['变量定义', '$', '@', '延迟加载'],
                        ['嵌套规则', '父选择器'],
                        ['混合', '继承', '占位符'],
                        ['运算', '颜色函数', '内置函数'],
                        ['条件指令', '@if', '@for', '@each', '@while'],
                        ['作用域'],
                        ['导入', '@import', '@use'],
                        ['PostCSS配合', '预处理器配置']
                    ]
                },
                'Tailwind CSS': {
                    'desc': '实用优先的CSS框架，通过原子类快速构建自定义设计',
                    'difficulty': 2,
                    'dimensions': [
                        ['颜色', '字体', '间距', '响应式前缀'],
                        ['状态变体', 'hover', 'focus', 'active', 'disabled', 'group-hover'],
                        ['flex布局', 'flex-col', 'flex-wrap'],
                        ['Grid', 'grid-cols', 'gap'],
                        ['m', 'p', 'mt', 'mb', 'mx', 'my'],
                        ['w', 'h', 'min', 'max'],
                        ['定位', 'absolute', 'fixed', 'relative', 'sticky'],
                        ['文本', 'text', 'font', 'italic', 'bold'],
                        ['圆角', '阴影', '动画'],
                        ['自定义配置', 'tailwind.config.js', 'JIT', 'darkMode']
                    ]
                },
                'Vite': {
                    'desc': '新一代前端构建工具，提供极速的开发服务器启动和热更新',
                    'difficulty': 2,
                    'dimensions': [
                        ['项目创建', 'create vite', 'vite.config.js'],
                        ['环境变量', '.env', 'CSS预处理', '静态资源'],
                        ['开发服务器', '热更新', 'HMR'],
                        ['构建', 'rollup', '代码分割', 'Tree Shaking'],
                        ['预构建', '依赖缓存'],
                        ['插件系统'],
                        ['SSR', '多页面应用'],
                        ['TypeScript支持', 'esbuild']
                    ]
                },
                'Vue': {
                    'desc': '渐进式JavaScript框架，提供响应式数据绑定和组件化开发',
                    'difficulty': 2,
                    'dimensions': [
                        ['模板语法', '插值', '指令', 'v-if', 'v-for', 'v-bind', 'v-on', 'v-model'],
                        ['计算属性', '侦听器'],
                        ['生命周期', 'created', 'mounted', 'updated', 'unmounted'],
                        ['组件', 'Props', '$emit', '插槽'],
                        ['响应式', 'Proxy', 'Reactive', 'Ref', 'computed'],
                        ['组件通信', 'Teleport', 'Suspense'],
                        ['Vue Router', 'Pinia'],
                        ['组合式API', 'setup'],
                        ['过渡动画', 'transition'],
                        ['SSR', 'Nuxt']
                    ]
                },
                'Webpack': {
                    'desc': '前端模块打包工具，支持代码分割、资源优化和开发服务器',
                    'difficulty': 2,
                    'dimensions': [
                        ['入口', '输出', '加载器', '插件'],
                        ['模式', 'development', 'production'],
                        ['代码分割', 'splitChunks', '动态导入'],
                        ['Tree Shaking', '压缩', 'source map'],
                        ['resolve', '别名', '扩展名'],
                        ['HtmlWebpackPlugin', 'MiniCssExtractPlugin'],
                        ['babel-loader', 'ts-loader', 'vue-loader'],
                        ['模块联邦', '作用域提升'],
                        ['构建优化', '持久化缓存'],
                        ['工程化', '多页面应用', 'SSR']
                    ]
                },
                '浏览器兼容性': {
                    'desc': '处理不同浏览器的渲染差异，使用polyfill和特性检测',
                    'difficulty': 2,
                    'dimensions': [
                        ['CSS兼容性', 'caniuse'],
                        ['Polyfill', 'Babel', 'core-js'],
                        ['特性检测', '浏览器Hack'],
                        ['CSS Reset', 'Normalize', '前缀'],
                        ['fetch polyfill', 'Promise polyfill'],
                        ['Browserslist', 'Autoprefixer'],
                        ['优雅降级', '渐进增强']
                    ]
                },
                '移动端适配': {
                    'desc': '响应式布局、rem/vw适配、触摸事件处理等移动端开发技术',
                    'difficulty': 2,
                    'dimensions': [
                        ['视口', 'viewport', 'DPI', '像素比'],
                        ['rem适配', 'vw', 'vh'],
                        ['Flexbox', 'Grid'],
                        ['touch事件', 'tap', '300ms延迟', '点透'],
                        ['安全区域', '刘海屏适配'],
                        ['手势', '滑动', '滚动穿透'],
                        ['1px边框'],
                        ['图片适配', 'iconfont'],
                        ['调试', 'vconsole']
                    ]
                },
                '前端性能优化': {
                    'desc': '代码分割、懒加载、缓存策略、资源压缩等性能提升技术',
                    'difficulty': 3,
                    'dimensions': [
                        ['性能指标', 'FCP', 'LCP', 'CLS', 'Web Vitals'],
                        ['网络优化', 'CDN', 'HTTP/2', 'HTTP/3'],
                        ['资源压缩', 'Gzip', 'Brotli', 'WebP'],
                        ['加载策略', '预加载', '懒加载', '首屏渲染'],
                        ['代码分割', '动态导入'],
                        ['缓存', '强缓存', '协商缓存', 'Service Worker'],
                        ['渲染优化', '重排重绘', 'GPU加速'],
                        ['JS优化', '防抖节流', '虚拟列表'],
                        ['SSR', 'SSG', '骨架屏'],
                        ['监控', 'Lighthouse', 'Chrome DevTools']
                    ]
                }
            }
        }
    }
    }
}
