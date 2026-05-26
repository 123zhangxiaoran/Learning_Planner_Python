"""Unity开发工程师数据"""
data = {
    '计算机与信息技术': {
        '游戏开发': {
            'Unity开发工程师': {
                'description': '使用Unity引擎开发游戏，实现游戏逻辑和交互功能。',
                'skills': {
                    'C#': {
                        'desc': 'Unity主要编程语言，游戏逻辑开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础语法', '数据类型与变量', '控制流程(if/for/while)', '数组与集合(List/Dictionary)', '结构体与枚举', '可空类型'],
                            ['面向对象与高级特性', '类/接口/继承/多态', '委托与事件(delegate/event)', '泛型与约束', '协程(IEnumerator/Yield)', 'LINQ与Lambda表达式'],
                            ['Unity集成', 'MonoBehaviour生命周期', 'Unity API常用类', '协程与异步编程(Task)', '序列化(JsonUtility)', '反射与Attribute特性'],
                            ['内存与设计模式', '内存管理与垃圾回收', '对象池模式', '单例模式与观察者模式', '文件操作与资源加载']
                        ]
                    },
                    'UGUI': {
                        'desc': 'Unity用户界面系统',
                        'difficulty': 2,
                        'dimensions': [
                            ['Canvas与基础组件', 'Canvas画布(屏幕/世界空间)', 'RectTransform锚点与轴心', 'Image/Sprite/九宫格', 'Text与TextMeshPro', 'Button与事件绑定'],
                            ['交互组件', 'Toggle/Checkbox', 'Slider/Scrollbar', 'InputField输入框', 'Dropdown下拉框', 'ScrollView滚动视图'],
                            ['布局与自适应', 'VerticalLayout/HorizontalLayout', 'GridLayout网格布局', 'ContentSizeFitter自适应', 'AspectRatioFitter', 'SafeArea适配'],
                            ['事件与优化', 'EventTrigger事件系统', 'UGUI批处理与合批', '图集打包(Atlas)', 'Overdraw优化', 'Raycaster与事件穿透']
                        ]
                    },
                    'UI设计': {
                        'desc': '游戏界面和交互设计',
                        'difficulty': 2,
                        'dimensions': [
                            ['布局与层级', 'UI布局原则与界面层级', 'HUD设计(血条/小地图/准星)', '弹窗与确认框设计', '新手引导与高亮遮罩'],
                            ['状态与动效', '按钮状态(正常/悬停/点击/禁用)', '界面切换动画与过渡', '缓动曲线与弹性效果', '粒子与序列帧动画融入'],
                            ['适配与多语言', '多分辨率适配策略', 'Canvas Scaler设置', '本地化与多语言方案', '主题切换与深色模式'],
                            ['性能与工具', 'UI DrawCall优化', '图集与动态图集', 'UI框架设计(如UIManager单例)', 'UI预制体与变体']
                        ]
                    },
                    'Unity3D': {
                        'desc': '跨平台游戏引擎使用，场景管理和资源管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['编辑器与核心概念', '场景/GameObject/Component', 'Transform组件', 'Prefab预制体与实例化', 'SceneManager场景切换', 'Project Settings配置'],
                            ['渲染与光照', '相机Camera与Culling Mask', '光照类型与Lightmapping烘焙', 'Light Probes探针', '材质Material与Shader', '渲染管线(URP/HDRP)'],
                            ['输入与时间', 'Input输入管理(新旧系统)', 'Time.deltaTime与Time.time', 'FixedUpdate与Update', 'Input System Package'],
                            ['生命周期与工具', 'Awake/Start/Update生命周期', '协程与Coroutine', 'Unity Package Manager', '版本控制与Collab/Plastic SCM']
                        ]
                    },
                    '动画系统': {
                        'desc': 'Animator、Animation动画控制',
                        'difficulty': 2,
                        'dimensions': [
                            ['动画剪辑与状态机', 'Animation Clip片段', 'Animator Controller', 'State状态与Transition过渡', '动画参数(Int/Float/Bool/Trigger)'],
                            ['混合与层', 'Blend Tree混合树', '动画层与Avatar Mask', 'Override Controller重写', 'AnimationCurve曲线'],
                            ['高级控制', '动画事件(Animation Event)', 'IK逆向运动学(Foot IK)', 'Root Motion根运动', 'Playable API与Timeline'],
                            ['2D与导入', '2D动画(Sprite Sheet/骨骼)', '动画片段导入设置', 'Avatar人形骨骼配置', 'Muscles & Settings肌肉设置']
                        ]
                    },
                    '多平台发布': {
                        'desc': 'iOS、Android、PC、WebGL发布',
                        'difficulty': 2,
                        'dimensions': [
                            ['构建设置', 'Build Settings场景配置', 'Player Settings平台参数', '分辨率与方向设置', '图标与启动画面'],
                            ['移动平台', 'iOS Xcode导出与证书', 'Android APK/AAB打包', 'Android Manifest权限', 'SDK/NDK与Gradle配置'],
                            ['桌面与Web', 'PC Standalone构建', 'WebGL发布与模板', 'IL2CPP脚本后端', 'Mono与IL2CPP对比'],
                            ['优化与更新', '代码剥离(Managed Stripping)', '纹理压缩格式(ETC2/ASTC)', '平台宏定义(#if UNITY_IOS)', '热更新方案(ILRuntime/HybridCLR)']
                        ]
                    },
                    '寻路系统': {
                        'desc': 'NavMesh导航网格',
                        'difficulty': 2,
                        'dimensions': [
                            ['NavMesh生成', 'NavMeshSurface烘焙', 'NavMeshAgent组件', 'NavMeshObstacle动态障碍', 'OffMeshLink连接', 'NavMeshLink组件'],
                            ['寻路控制', 'NavMeshPath路径计算', '区域(Area)与成本', '动态导航与NavMesh更新', '分层NavMesh(Layered)'],
                            ['算法与调试', 'A*寻路算法基础', 'Grid Graph网格图', '寻路优先级与避障', 'NavMesh路径可视化']
                        ]
                    },
                    '游戏物理': {
                        'desc': '物理引擎实现碰撞和运动效果',
                        'difficulty': 2,
                        'dimensions': [
                            ['刚体与碰撞体', 'Rigidbody属性(Mass/Drag)', 'Collider类型(Box/Sphere/Capsule)', '运动学刚体(Kinematic)', '复合碰撞体', '碰撞矩阵与Layer设置'],
                            ['碰撞与触发', '碰撞检测(OnCollisionEnter)', '触发器(IsTrigger)', '碰撞事件参数(Collision)', 'Trigger事件参数'],
                            ['力与运动', 'AddForce/AddTorque', 'ConstantForce恒定力', 'CharacterController角色控制器', '射线检测(Raycast/SphereCast)'],
                            ['物理材质与关节', 'Physic Material(摩擦力/弹性)', 'Fixed Joint/Spring Joint', 'Hinge Joint铰链', 'ConfigurableJoint可配置关节']
                        ]
                    },
                    '物理引擎': {
                        'desc': 'Rigidbody、Collider物理组件使用',
                        'difficulty': 2,
                        'dimensions': [
                            ['刚体进阶', 'Mass/Drag/Angular Drag属性', 'Interpolation/Extrapolation', 'Collision Detection模式', 'Fixed Timestep设置'],
                            ['碰撞事件与交互', '碰撞回调(Collision/Trigger)', 'Collision相对速度与接触点', 'IgnoreCollision忽略', '层碰撞矩阵设置'],
                            ['关节与约束', 'Hinge Joint铰链', 'Spring Joint弹簧', 'ConfigurableJoint配置', 'WheelCollider车轮碰撞器'],
                            ['物理组件与性能', 'Cloth布料组件', '物理材质(摩擦力/弹力)', '复合碰撞体应用', '物理性能优化']
                        ]
                    },
                    '粒子系统': {
                        'desc': '特效制作和粒子控制',
                        'difficulty': 2,
                        'dimensions': [
                            ['核心模块', 'Main Module主模块(持续时间/循环/预热)', 'Emission发射(速率/爆发)', 'Shape形状(锥形/球形/盒形)'],
                            ['视觉控制', 'Color over Lifetime颜色渐变', 'Size over Lifetime大小曲线', 'Texture Sheet Animation序列帧', 'Renderer渲染模式(拉伸/广告牌)'],
                            ['运动与高级', 'Velocity over Lifetime速度', 'Limit Velocity Over Lifetime限速', 'Collision碰撞模块', 'Sub Emitters子发射器'],
                            ['优化与集成', 'Trail拖尾模块', 'GPU Instancing粒子合批', 'Cinemachine配合', '粒子池管理']
                        ]
                    },
                    '资源打包': {
                        'desc': 'AssetBundle资源管理和热更新',
                        'difficulty': 2,
                        'dimensions': [
                            ['AssetBundle构建', 'BuildPipeline构建', '打包策略与分包', '变体(Variants)', 'AB依赖与哈希'],
                            ['加载与卸载', 'AssetBundle.LoadAsset', '同步/异步加载', 'Unload(True/False)', '资源引用计数管理'],
                            ['热更新流程', 'UnityWebRequest下载', '缓存与MD5校验', '增量更新与版本管理', '热更新资源清单'],
                            ['Addressables系统', 'Addressables配置与打包', '资源位置与标签', '异步加载与内存管理', '与AssetBundle对比']
                        ]
                    },
                    'Shader': {
                        'desc': 'ShaderLab编写自定义着色器',
                        'difficulty': 3,
                        'dimensions': [
                            ['基础与语法', 'Shader结构与Properties', 'SubShader与Pass', 'CG/HLSL语言基础', '顶点片元着色器'],
                            ['光照与纹理', 'Unity光照模型(兰伯特/Blinn-Phong)', '法线与法线贴图', '阴影投射与接收', '表面着色器(Surface Shader)'],
                            ['视觉特效', 'UV动画(流动/旋转)', '顶点动画(波动/偏移)', '溶解效果(dissolve)', '边缘光(Rim Light)'],
                            ['后处理与优化', 'Post Processing Stack', 'Bloom/Depth of Field', 'Shader Variant与Shader Featuring', '性能优化与低端适配']
                        ]
                    },
                    '性能优化': {
                        'desc': 'DrawCall优化、资源管理、内存优化',
                        'difficulty': 3,
                        'dimensions': [
                            ['Profiler分析', 'CPU Usage分析', 'GPU Usage分析', 'Memory Profiler', 'Rendering Profiler'],
                            ['DrawCall与批处理', '静态批处理(Static Batching)', '动态批处理(Dynamic Batching)', 'GPU Instancing', 'SRP Batcher'],
                            ['剔除与LOD', 'Frustum Culling视锥剔除', 'Occlusion Culling遮挡剔除', 'LOD组(Level of Detail)', 'MipMap优化'],
                            ['内存与对象池', '垃圾回收(GC)优化', '对象池(Object Pool)', '资源生命周期管理', 'Resources.UnloadUnusedAssets', '纹理与音频压缩'],
                            ['光照与阴影', 'Light Probe光照探针', 'Reflection Probe反射探针', '阴影距离与级联', '烘焙与实时GI平衡']
                        ]
                    }
                }
            }
        }
    }
}