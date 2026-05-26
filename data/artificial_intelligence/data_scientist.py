"""数据科学家数据"""
data = {
    '计算机与信息技术': {
        '人工智能': {
            '数据科学家': {
                'description': '通过数据分析挖掘业务价值，建立数据模型支持决策。',
                'skills': {
                    'NumPy': {
                        'desc': '数值计算和矩阵运算',
                        'difficulty': 1,
                        'dimensions': [
                            ['数组基础', 'ndarray创建', '数据类型(int/float/bool)', '形状操作(reshape/flatten)', '索引与切片', '布尔索引与条件筛选'],
                            ['运算与广播', '向量化运算', '矩阵乘法(@/dot)', '广播机制(Broadcast)', '数学函数(sin/cos/exp/log)', '通用函数(ufunc)'],
                            ['聚合与统计', 'sum/mean/std/var', 'max/min/argmax', '排序(sort/argsort)', '条件提取(where/nonzero)', '去重(unique)'],
                            ['线性代数', '特征值/奇异值分解', '范数计算(linalg.norm)', '行列式与逆矩阵', '解线性方程(linalg.solve)', '傅里叶变换(fft)'],
                            ['数据处理', '数组拼接(stack/concatenate)', '分割(split)', '随机数生成(randn/randint)', '文件读写(savetxt/loadtxt)', '性能优化(向量化)']
                        ]
                    },
                    'Pandas': {
                        'desc': '数据清洗、转换和分析',
                        'difficulty': 1,
                        'dimensions': [
                            ['数据结构与IO', 'Series/DataFrame', '读取(read_csv/excel/json)', '查看(head/info/describe)', '保存(to_csv/to_excel)'],
                            ['数据选择与筛选', 'loc/iloc选择', '布尔索引', '条件筛选', '排序(sort_values)', '去重(drop_duplicates)'],
                            ['数据清洗与转换', '缺失值处理(isnull/fillna/dropna)', '替换(replace)', '类型转换(astype)', '映射(map/apply/applymap)', '重命名(rename)'],
                            ['数据合并与重塑', 'concat/merge/join', 'groupby分组聚合', '透视表(pivot_table)', '字符串操作(str)', '日期时间与时间序列(resample/rolling)'],
                            ['索引与性能', 'set_index/reset_index', '层次化索引(MultiIndex)', '窗口函数(rolling/expanding)', '采样(sample)', '性能优化(分类类型)']
                        ]
                    },
                    'Python/R': {
                        'desc': '数据分析和建模的主要工具语言',
                        'difficulty': 1,
                        'dimensions': [
                            ['Python核心', '数据类型与控制流', '推导式', '函数与模块', 'numpy/scipy计算', 'Pandas数据处理'],
                            ['R核心', '向量/矩阵/数据框', 'dplyr/tidyr数据处理', 'ggplot2可视化', 'lm/glm统计建模', 'tidyverse生态'],
                            ['可视化与交互', 'Matplotlib/Seaborn', 'Plotly交互图表', 'Jupyter Notebook', '图表主题与配色'],
                            ['机器学习与模型', 'Scikit-learn建模', 'R建模(caret)', '模型评估', '特征工程基础'],
                            ['环境与协作', 'conda/venv', 'pip/R包管理', '代码规范(PEP8)', '数据科学工作流', 'Python与R互调']
                        ]
                    },
                    'SQL': {
                        'desc': '从数据库中提取和处理数据',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础查询', 'SELECT/FROM/WHERE', '条件(AND/OR/NOT)', '排序(ORDER BY)', '去重(DISTINCT)', '聚合函数(COUNT/SUM/AVG)'],
                            ['高级查询', 'GROUP BY/HAVING', '子查询', '表连接(INNER/LEFT/RIGHT)', 'UNION', '窗口函数(OVER/PARTITION BY)'],
                            ['窗口与排名', 'ROW_NUMBER/RANK/DENSE_RANK', 'LAG/LEAD', 'NTILE', '聚合窗口', '累积计算'],
                            ['数据操作', 'INSERT/UPDATE/DELETE', 'CREATE TABLE', '约束(主键/外键/唯一)', '索引(CREATE INDEX)', '视图(VIEW)'],
                            ['编程对象', '存储过程(PROCEDURE)', '触发器(TRIGGER)', '事务(BEGIN/COMMIT/ROLLBACK)', 'CTE(WITH)', '游标概念'],
                            ['优化与方言', 'EXPLAIN执行计划', '慢查询分析', '索引设计', 'MySQL/PostgreSQL/HiveQL', '查询改写与性能优化']
                        ]
                    },
                    'A/B测试': {
                        'desc': '设计实验评估产品改动效果',
                        'difficulty': 2,
                        'dimensions': [
                            ['实验设计', '对照/实验组', '随机分组', '样本量计算(统计功效)', 'AA测试', '实验周期与指标选择'],
                            ['显著性检验', 't检验/z检验/p值', '置信区间', '方差分析(ANOVA)', '多重比较校正', '辛普森悖论'],
                            ['分流与指标', '哈希分流/分层分流', '北极星指标(OMTM)', '指标构建与归因', '数据埋点', '效果评估(提升度)'],
                            ['效应与因果', '新奇效应', '因果推断概念', '倾向得分匹配(PSM)', '双重差分(DID)', 'AB测试统计陷阱'],
                            ['平台与工程', '在线实验平台', '灰度发布', 'Feature Flag', '实验监控', 'AB测试框架']
                        ]
                    },
                    'Tableau/Power BI': {
                        'desc': '商业智能工具制作交互式仪表板',
                        'difficulty': 2,
                        'dimensions': [
                            ['Tableau基础', '工作表/仪表板', '数据连接(Live/Extract)', '维度与度量', '图表类型(柱状/折线/饼图/散点)', '计算字段与LOD表达式'],
                            ['Tableau交互与发布', '参数与筛选器', '表计算(Window)', '仪表板交互操作', 'Tableau Server/Online发布', '权限管理与数据刷新'],
                            ['Power BI基础', '报表与数据集', 'Power Query数据转换', 'DAX公式', '度量值与计算列', 'Power BI Desktop'],
                            ['Power BI服务', 'Power BI Service', '行级安全(RLS)', '网关与数据刷新', '分享协作', '移动端']
                        ]
                    },
                    '业务理解': {
                        'desc': '将业务问题转化为数据问题',
                        'difficulty': 2,
                        'dimensions': [
                            ['指标体系', 'AARRR海盗模型', '北极星指标(OMTM)', '指标拆解与下钻', 'RFM用户分层', '用户生命周期与漏斗'],
                            ['业务模型与沟通', '商业模式画布', '行业知识(电商/金融/教育)', '需求分析(PRD)', '优先级(RICE/ICE)', '业务需求沟通'],
                            ['数据治理与口径', '数据字典', '数据资产', '数据治理', '指标一致性与口径', '业务指标监控与异常分析'],
                            ['问题定义与实验', '业务问题定义', '数据假设验证', 'AB实验设计', '归因分析', '业务迭代评估']
                        ]
                    },
                    '探索性数据分析': {
                        'desc': '使用统计方法和可视化理解数据分布',
                        'difficulty': 2,
                        'dimensions': [
                            ['数据概览与质量', '数据概览(info/describe)', '缺失值分析', '数据类型检查', '异常值检测(IQR/Z-score)', '数据质量报告'],
                            ['分布与统计', '数值分布(直方图/密度图)', '类别分布(柱状图)', '集中趋势与离散程度', '分布特征(偏度/峰度)', 'QQ图/正态性检验'],
                            ['关系与交叉', '相关性矩阵(heatmap)', '散点图/配对图', '分组分析(groupby)', '交叉表分析', '时间序列趋势分析'],
                            ['可视化工具', 'Matplotlib/Seaborn箱线图', '小提琴图', '热力图', '交互图表', '可视化故事化与业务解读'],
                            ['结论与生成', '假设生成', '探索结论总结', '业务含义解读', '数据故事化', '后续分析建议']
                        ]
                    },
                    '数据可视化': {
                        'desc': '使用Matplotlib、Seaborn、Plotly展示数据洞察',
                        'difficulty': 2,
                        'dimensions': [
                            ['Matplotlib基础', 'figure/axes', '折线/散点/柱状图', '直方图/箱线图/饼图', '子图与坐标轴设置', '样式/颜色/中文配置', '保存图片'],
                            ['Seaborn统计图', '分布图(distplot/kdeplot)', '关系图(relplot)', '分类图(catplot)', '回归图(lmplot)', '热力图(clustermap)', 'set_style主题'],
                            ['Plotly交互', 'Plotly Express快速绘图', 'graph_objects自定', '子图与布局', '导出HTML', 'Dash/动态图表'],
                            ['高级可视化', '地理地图可视化', '动画/动态图表', 'Dashboard制作', '图表配色与主题', '可视化原则与图表选择', '数据故事化']
                        ]
                    },
                    '数据报告': {
                        'desc': '撰写数据分析报告，提供决策建议',
                        'difficulty': 2,
                        'dimensions': [
                            ['报告规划', '报告结构(背景/方法/结论/建议)', '报告类型(周报/专题)', '受众分析', '数据来源与口径说明', '分析方法说明'],
                            ['内容与可视化', '图表选择与数据故事', '结论提炼', '行动建议', '风险提示', '附录与数据字典'],
                            ['自动化与发布', '自动化报告(Python/R)', '邮件/钉钉/飞书推送', '数据门户', '看板/Dashboard', '报告分发与更新'],
                            ['格式与工具', 'PPT制作', 'Word/PDF报告', 'Markdown/Jupyter报告', 'HTML报告', '报告模板与审核']
                        ]
                    },
                    '数据清洗': {
                        'desc': '处理缺失值、异常值、重复数据',
                        'difficulty': 2,
                        'dimensions': [
                            ['缺失值处理', '缺失值识别与分析', '删除法', '填充法(均值/中位数/众数)', '插值法(interpolate)', '模型预测填充'],
                            ['异常值与重复', '异常值识别(Z-score/IQR)', '异常值处理(删除/盖帽)', '重复值检测与删除', '不一致值处理', '缺失/异常指示变量'],
                            ['文本与日期清洗', '文本去空格/大小写', '特殊字符处理', '日期格式标准化', '数据类型转换', '编码乱码处理'],
                            ['高级数据操作', '数据合并与主键对齐', '宽表长表转换', '数据拆分', '数据脱敏', '不平衡数据处理(采样/合成)'],
                            ['工具与流程', 'Python/pandas清洗', 'R/tidyr清洗', 'SQL数据清洗', '数据质量框架', '数据清洗流程自动化']
                        ]
                    },
                    '机器学习': {
                        'desc': '构建预测模型和分类模型',
                        'difficulty': 2,
                        'dimensions': [
                            ['回归与线性模型', '线性回归', '岭回归/Lasso', '逻辑回归', 'SVM(支持向量机)', '朴素贝叶斯分类'],
                            ['树模型与集成', '决策树', '随机森林', 'XGBoost', 'LightGBM', 'CatBoost', 'Stacking/Blending'],
                            ['聚类与降维', 'K-Means', '层次聚类', 'DBSCAN', 'PCA', 't-SNE'],
                            ['模型评估与调优', '交叉验证', '过拟合/欠拟合', '正则化(L1/L2)', 'GridSearch/RandomSearch', 'ROC/AUC', '分类/回归指标'],
                            ['时间序列分析', '时间序列特征', 'ARIMA/SARIMA', '指数平滑', 'Prophet', '时间序列交叉验证']
                        ]
                    },
                    '特征工程': {
                        'desc': '构建和选择对模型有用的特征',
                        'difficulty': 2,
                        'dimensions': [
                            ['数值与转换', '标准化(Z-score/MinMax)', '分箱(等距/等频)', '对数/Box-Cox变换', '交互特征(乘/除)', '多项式特征'],
                            ['类别与编码', 'One-Hot/Label编码', '目标编码(Target Encoding)', '计数编码', '哈希编码', '有序类别编码'],
                            ['时间与序列特征', '年/月/日/星期提取', '滑动窗口统计', '滞后/差分特征', '聚合统计(rolling)', '时间序列特征'],
                            ['文本与高级特征', 'TF-IDF向量', '词向量(Word2Vec)', '主题特征', '图像特征(预训练)', '多模态特征'],
                            ['特征选择与降维', '方差阈值过滤', '相关性分析', '模型重要性', '递归特征消除(RFE)', 'PCA/SVD降维'],
                            ['工程化与监控', '离线/在线特征', '特征回填', '特征版本管理', '特征监控与漂移', '特征存储(Feature Store)']
                        ]
                    },
                    '统计学': {
                        'desc': '假设检验、回归分析、时间序列分析等统计方法',
                        'difficulty': 2,
                        'dimensions': [
                            ['描述统计与分布', '集中趋势(均值/中位数/众数)', '离散程度(方差/标准差)', '分布形状(偏度/峰度)', '常见分布(正态/二项/泊松)', '中心极限定理'],
                            ['推断统计', '置信区间', '假设检验(t/z检验)', 'p值与显著性', '第一/二类错误', '功效分析与样本量计算'],
                            ['回归与相关', 'Pearson/Spearman相关系数', '简单线性回归', '多元线性回归', '回归诊断(残差/共线性)', '逻辑回归'],
                            ['方差分析与非参数', '单因素/双因素方差分析', '协方差分析', '非参数检验(Mann-Whitney/Kruskal-Wallis)', '卡方检验', '多重比较校正'],
                            ['时间序列分析', '时间序列分解(趋势/季节/随机)', '移动平均与指数平滑', 'ARIMA模型', '平稳性检验(ADF)', '协整与Granger因果'],
                            ['贝叶斯与高级', '贝叶斯统计(先验/后验)', '贝叶斯推断', 'MCMC采样概念', 'AB测试统计', '预测置信区间']
                        ]
                    }
                }
            }
        }
    }
}