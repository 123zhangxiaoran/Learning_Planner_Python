"""Unreal开发工程师数据"""
data = {
    '计算机与信息技术': {
        '游戏开发': {
            'Unreal开发工程师': {
                'description': '使用Unreal引擎开发高质量游戏，负责图形渲染和性能优化。',
                'skills': {
                    'C++': {
                        'desc': 'Unreal核心编程语言，高性能开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['语言基础', '数据类型/指针/引用', '类和对象/继承/多态', '模板与泛型编程', 'STL容器/迭代器/算法', '智能指针(Unique/Shared)'],
                            ['Unreal宏与类型', 'UPROPERTY/UCLASS/UFUNCTION宏', 'FString/FText文本处理', 'TArray/TMap/TSet容器', '命名空间与预处理指令'],
                            ['高级编程', '委托(Delegate/Multicast)', '协程(Future/Async)', '蓝图调用与C++暴露', '模块/插件开发', '反射与RTTI']
                        ]
                    },
                    'AI行为树': {
                        'desc': '游戏AI设计和实现',
                        'difficulty': 2,
                        'dimensions': [
                            ['行为树节点', 'Selector选择器/Sequence序列', 'Task任务节点', 'Decorator装饰器', 'Service服务节点'],
                            ['黑板与感知', 'Blackboard黑板', 'AI Perception感知系统', 'EQS环境查询系统'],
                            ['导航与控制', 'Navigation Mesh导航网格', 'AIController控制器', 'MoveTo移动任务', 'Pathfinding寻路'],
                            ['自定义与架构', '自定义Task', 'AI模块架构', '行为树与蓝图交互']
                        ]
                    },
                    'UMG': {
                        'desc': 'Unreal用户界面系统',
                        'difficulty': 2,
                        'dimensions': [
                            ['容器与布局', 'Canvas Panel画布', 'VerticalBox/HorizontalBox', 'SizeBox/Overlay'],
                            ['基础控件', 'Text/TextBlock', 'Button/CheckBox', 'Image/Slate刷', 'EditableText/TextBox'],
                            ['高级控件与样式', 'Slider/ProgressBar', 'ComboBox下拉框', 'ListView/TreeView', '动画(Montage)', '样式/主题'],
                            ['优化', 'UMG优化', '复杂UI管理', 'Widget蓝图通信']
                        ]
                    },
                    'Unreal Engine': {
                        'desc': 'Unreal游戏引擎深度使用',
                        'difficulty': 2,
                        'dimensions': [
                            ['架构与核心类', '引擎架构/模块系统', 'Actor/Pawn/Character', 'GameMode/GameInstance', 'Level/World/WorldContext'],
                            ['反射与内存', 'UObject垃圾回收', '反射系统/RTTI', '组件(Component)系统', 'GameplayFramework'],
                            ['蓝图与脚本', '蓝图可视化脚本', '关卡蓝图/Level BP', '动画蓝图/Anim BP', '材质编辑器/Material'],
                            ['扩展与开发', '编辑器扩展', '插件开发', '蓝图通信/接口']
                        ]
                    },
                    '光照系统': {
                        'desc': '静态光照、动态光照、Lumen',
                        'difficulty': 2,
                        'dimensions': [
                            ['光源类型', 'Directional Light定向光', 'Point/Spot Light点/聚光灯', 'Sky Light天空光'],
                            ['光照模式', 'Static/Stationary/Movable', 'Lightmass全局光照', '光照贴图/UV'],
                            ['全局光照与反射', 'Lumen动态光照', 'Ray Tracing光线追踪', 'IBL环境光照', '反射/Reflection'],
                            ['高级特性', 'SSAO屏幕空间AO', '光照函数/Light Function', 'IES配置文件', '体积雾/Volumetric']
                        ]
                    },
                    '动画系统': {
                        'desc': '动画蓝图和混合空间',
                        'difficulty': 2,
                        'dimensions': [
                            ['动画资产', 'Animation Sequence', 'Blend Space混合空间', 'Montage蒙太奇', 'Curves曲线动画'],
                            ['状态机与图表', 'State Machine状态机', 'Anim Graph动画图表', 'Event Graph事件图表', 'Sync Groups同步组'],
                            ['IK与物理动画', 'IK逆向运动学', '物理动画/Physics Asset', 'Root Motion根动画', 'Aim Offset瞄准偏移'],
                            ['高级特性', 'Notify通知事件', 'Anim Layer接口', '布料动画/Cloth']
                        ]
                    },
                    '性能分析': {
                        'desc': 'Unreal Insights性能分析工具',
                        'difficulty': 2,
                        'dimensions': [
                            ['Unreal Insights', '会话与录制', 'Trace/Recording', 'Frame Profiler'],
                            ['CPU/GPU分析', 'CPU Profiler', 'GPU Profiler', 'GPUVisualizer', 'ShaderComplexity着色器复杂度'],
                            ['内存与加载', 'Memory内存分析', 'Load Time加载时间', 'Memory Insights'],
                            ['统计系统', 'Stats统计系统', 'Rendering Stats', 'Draw Call统计', 'LOD状态统计'],
                            ['网络分析', 'Networking Insights', '网络性能追踪']
                        ]
                    },
                    '材质系统': {
                        'desc': 'Material Editor材质编辑',
                        'difficulty': 2,
                        'dimensions': [
                            ['PBR基础', 'Base Material基础材质', 'PBR光照模型', 'Roughness/Metallic', 'Normal Map法线'],
                            ['表达式与函数', 'Material Expression表达式', 'Texture Sample纹理采样', 'UV Coordinates', 'Material Functions函数'],
                            ['实例与参数', '材质实例/Material Instance', 'Param Collection参数集合', 'Material Layers层'],
                            ['混合与特殊效果', 'Blend Mode混合模式', 'Translucency透明度', 'Subsurface Scattering次表面', 'Decal贴花']
                        ]
                    },
                    '游戏物理': {
                        'desc': '物理模拟和角色控制',
                        'difficulty': 2,
                        'dimensions': [
                            ['物理资产与碰撞', 'Physics Asset物理资产', 'Rigid Body刚体', 'Collision碰撞频道', 'Physical Material物理材质'],
                            ['约束与关节', 'Constraint约束', 'Hinge Joint铰链关节', 'Physics Handle物理手柄'],
                            ['Chaos引擎与特殊模拟', 'Chaos Physics引擎', 'Destructible可破碎物', 'Cloth布料', 'Vehicle车辆'],
                            ['角色移动', 'Character Movement组件', 'Walk/Run/Air', 'NavMeshwalking导航行走', 'Flying飞行']
                        ]
                    },
                    '网络同步': {
                        'desc': '多人游戏网络架构',
                        'difficulty': 2,
                        'dimensions': [
                            ['复制基础', 'Replication复制', 'Role/RemoteRole角色', 'Replicated变量', 'DOREPLIFETIME'],
                            ['RPC与调用', 'RPC远程调用', 'Multicast广播', 'Owning Connection'],
                            ['相关性与优化', 'Relevancy相关性', 'Net Group网络组', 'Net Driver网络驱动'],
                            ['在线服务', 'Online Subsystem', 'Session会话', 'Matchmaking匹配', 'Latency Compensation延迟补偿']
                        ]
                    },
                    '蓝图': {
                        'desc': 'Unreal可视化脚本编程',
                        'difficulty': 2,
                        'dimensions': [
                            ['事件与流程控制', 'Blueprint事件图', 'Event BeginPlay/EventTick', 'Branch/序列节点', 'ForEach循环', 'Gate/Delay'],
                            ['变量与数据类型', 'Variables变量', 'Structs结构体', 'Enums枚举', 'Data Table数据表'],
                            ['函数与宏', 'Custom Events自定义事件', 'Functions函数', 'Macros宏', 'Interfaces接口'],
                            ['通信与优化', '蓝图通信', '蓝图调试与优化']
                        ]
                    },
                    'Nanite': {
                        'desc': '虚拟几何体系统',
                        'difficulty': 3,
                        'dimensions': [
                            ['Nanite基础', 'Nanite概述/虚拟几何体', 'Nanite支持格式', '强制Nanite/ForceNanite'],
                            ['设置与限制', 'Nanite质量/Nanite Quality', 'Nanite限制/约束', 'Nanite兼容性'],
                            ['LOD与剔除', 'LOD系统/Fallback LOD', 'Nanite剔除', '几何优先级', 'Nanite LOD调整'],
                            ['阴影与配合', 'Virtual Shadow Maps', 'Nanite与HLOD配合', 'Nanite可视化']
                        ]
                    },
                    '图形渲染': {
                        'desc': '渲染管线理解和优化',
                        'difficulty': 3,
                        'dimensions': [
                            ['渲染管线基础', '渲染管线/Rendering Pipeline', 'Draw Call绘制调用', 'Command List命令列表', 'RHI渲染硬件接口'],
                            ['延迟渲染与后处理', '延迟渲染/Forward+', 'GBuffer渲染目标', 'Bloom后处理', 'Tone Mapping色调映射'],
                            ['抗锯齿与超采样', 'Anti-Aliasing抗锯齿', 'Temporal AA/FSR', 'TSR时间超采样'],
                            ['阴影与全局光照', 'Shadow级联阴影', 'CSM阴影贴图', 'Lumen全局光照', 'Nanite几何体', 'Ray Tracing渲染']
                        ]
                    }
                }
            }
        }
    }
}