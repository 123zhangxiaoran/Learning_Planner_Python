"""计算机视觉工程师数据"""
data = {
    '计算机与信息技术': {
        '人工智能': {
            '计算机视觉工程师': {
                'description': '开发图像和视频处理算法，如目标检测、人脸识别、图像分割等。',
                'skills': {
                    'Python': {
                        'desc': '计算机视觉开发的主流语言',
                        'difficulty': 1,
                        'dimensions': [
                            ['核心编程', '数据类型(list/dict)', '控制流与函数', '面向对象(类/继承)', '异常处理', '推导式与生成器'],
                            ['科学计算与图像', 'NumPy数组与广播', 'OpenCV(cv2)基础读写', 'PIL/Pillow图像处理', 'Matplotlib可视化', 'Scikit-image滤波'],
                            ['工程与工具', 'Jupyter Notebook/Colab', '版本控制(Git)', '多线程/多进程', 'GPU加速(CUDA/PyTorch)', '虚拟环境与包管理']
                        ]
                    },
                    'CNN': {
                        'desc': '卷积神经网络，图像特征提取的基础',
                        'difficulty': 2,
                        'dimensions': [
                            ['卷积与池化', 'Conv2D(卷积核/步长/填充)', 'Max/Avg Pooling', '全局平均池化', '1x1卷积降维/升维', '空洞卷积与反卷积'],
                            ['网络组件', '全连接层', '激活函数(ReLU/Sigmoid)', 'Batch Normalization', 'Dropout正则化', '权重初始化(Xavier/He)'],
                            ['经典架构', 'LeNet/AlexNet/VGG', 'ResNet残差连接', '深度可分离卷积(MobileNet)', '分组卷积(ResNeXt)', '特征金字塔(FPN)'],
                            ['注意力与优化', '通道注意力(SE-Net)', '空间注意力(CBAM)', '梯度消失/爆炸', '特征图可视化', '迁移学习']
                        ]
                    },
                    'Keras': {
                        'desc': '高级神经网络API',
                        'difficulty': 2,
                        'dimensions': [
                            ['模型构建', 'Sequential与Functional API', 'Dense/Conv2D层', '激活函数与Dropout', 'compile配置', '多输入多输出模型'],
                            ['训练与回调', 'fit(batch_size/epochs)', 'EarlyStopping/ModelCheckpoint', 'ReduceLROnPlateau', 'TensorBoard', '数据增强(ImageDataGenerator)'],
                            ['迁移与保存', '预训练模型(VGG/ResNet)', '迁移学习与微调', 'load_model/h5保存', '权重保存与加载', 'ONNX导出']
                        ]
                    },
                    'OpenCV': {
                        'desc': '开源计算机视觉库，提供图像处理基础功能',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础操作', 'imread/imwrite/颜色空间转换', '通道分离与合并', 'ROI区域', 'resize/旋转/翻转', '仿射与透视变换'],
                            ['滤波与形态学', '高斯/中值/双边滤波', 'Canny/Sobel边缘检测', '阈值处理(自适应/Otsu)', '膨胀/腐蚀/开闭运算', '结构元素'],
                            ['特征与轮廓', 'findContours/drawContours', '轮廓特征(面积/周长)', '霍夫变换(直线/圆)', '模板匹配', '直方图计算与均衡化'],
                            ['视频与高级', 'VideoCapture/VideoWriter', 'ORB/SIFT特征检测', 'DNN模块推理', '相机标定与去畸变', 'GrabCut/MeanShift']
                        ]
                    },
                    'PIL/Pillow': {
                        'desc': 'Python图像处理库',
                        'difficulty': 2,
                        'dimensions': [
                            ['基础操作', 'Image.open/save/show', '模式(RGB/RGBA/L)', 'resize/thumbnail/rotate', 'crop/paste', '通道分离与合并'],
                            ['增强与滤镜', 'ImageEnhance(亮度/对比度)', 'ImageFilter(模糊/锐化)', 'ImageOps(自动对比度/均衡化)', '色彩空间转换', '像素操作(putpixel/getpixel)'],
                            ['绘图与文字', 'ImageDraw(矩形/圆形)', 'draw.text(字体/字号)', 'ImageFont加载字体', 'GIF动画处理', '与NumPy互转']
                        ]
                    },
                    'PyTorch': {
                        'desc': '研究友好的深度学习框架',
                        'difficulty': 2,
                        'dimensions': [
                            ['张量与计算', 'Tensor创建与运算', 'shape/device/to(device)', '自动求导(requires_grad/backward)', '梯度清零(zero_grad)', 'GPU加速(CUDA)'],
                            ['网络与层', 'nn.Module自定义网络', 'Conv2d/Linear/MaxPool2d', '激活函数与Dropout', 'BatchNorm', 'Sequential容器'],
                            ['数据与训练', 'DataLoader/Dataset', 'transforms预处理', 'ImageFolder加载', '损失函数与优化器(Adam)', 'train/eval模式'],
                            ['保存与部署', '模型保存(state_dict)', 'checkpoint恢复', '预训练模型(torchvision.models)', 'TorchScript/JIT', 'ONNX导出']
                        ]
                    },
                    'TensorFlow': {
                        'desc': '深度学习模型训练和部署',
                        'difficulty': 2,
                        'dimensions': [
                            ['张量与计算', 'Tensor/Variable', 'Eager Execution', 'GradientTape自动求导', 'tf.data.Dataset管道', 'map/prefetch/batch优化'],
                            ['模型与训练', 'Functional/Sequential API', 'Conv2D/Dense层', 'fit训练与回调', 'TensorBoard日志', '数据增强(tf.image)'],
                            ['部署与生态', 'SavedModel/h5保存', '迁移学习(tf.keras.applications)', 'TensorFlow Serving', 'TFLite移动端部署', 'TensorFlow.js']
                        ]
                    },
                    '图像分类': {
                        'desc': '识别图像中的物体类别',
                        'difficulty': 2,
                        'dimensions': [
                            ['任务与数据', '多分类/二分类/多标签', '数据集(CIFAR/ImageNet)', '数据划分(训练/验证/测试)', '数据增强(翻转/旋转/CutMix)', '标签平滑'],
                            ['模型演进', 'AlexNet/VGG/GoogLeNet', 'ResNet/DenseNet', 'MobileNet/EfficientNet', 'ConvNeXt现代架构', '预训练与微调'],
                            ['评估与优化', '交叉熵损失/Softmax', 'Top-1/Top-5准确率', '混淆矩阵/F1/ROC', 'Grad-CAM可视化', 'TTA/模型集成']
                        ]
                    },
                    '图像增强': {
                        'desc': '去噪、超分辨率、风格迁移',
                        'difficulty': 2,
                        'dimensions': [
                            ['去噪', '高斯/椒盐噪声', '均值/中值/高斯滤波', '双边滤波/NLM', 'BM3D', '深度学习去噪(DnCNN/U-Net)'],
                            ['超分辨率', '插值法(双线性/双立方)', 'SRCNN/ESRGAN', 'EDSR/SRGAN', '亚像素卷积', 'Real-ESRGAN真实场景'],
                            ['风格迁移与增强', '神经风格迁移(Gatys)', 'Gram矩阵/风格损失', '快速风格迁移(AdaIN)', 'CLAHE/伽马校正', '白平衡/色彩校正']
                        ]
                    },
                    'OCR': {
                        'desc': '光学字符识别，从图像中提取文字',
                        'difficulty': 3,
                        'dimensions': [
                            ['文本检测', 'CTPN/EAST', 'PixelLink/PSENet', 'DBNet可微二值化', 'CRAFT字符区域感知', '任意形状文本检测'],
                            ['文本识别', 'CRNN+CTC', 'Attention机制(ASTER)', 'SATRN/TrOCR', 'Transformer OCR', '多语言/手写体识别'],
                            ['应用与后处理', 'PaddleOCR/EasyOCR', 'Tesseract', '表格识别', '车牌/身份证/发票OCR', '字典校正与评估(Edit Distance)']
                        ]
                    },
                    'ResNet': {
                        'desc': '残差网络，解决深层网络训练问题',
                        'difficulty': 3,
                        'dimensions': [
                            ['残差学习', '恒等映射(Identity Mapping)', '残差块(F(x)+x)', 'Skip Connection', '1x1降维(Projection Shortcut)', '瓶颈设计(Bottleneck)'],
                            ['架构与变体', 'ResNet-18/34/50/101', 'ResNet-V2预激活', 'ResNeXt分组卷积', 'SE-ResNet注意力', 'Wide ResNet'],
                            ['训练与应用', 'ImageNet预训练与微调', 'ResNet-FPN特征金字塔', '在检测/分割中作为骨干', 'CIFAR实验', '1000层探索']
                        ]
                    },
                    'YOLO': {
                        'desc': '实时目标检测算法',
                        'difficulty': 3,
                        'dimensions': [
                            ['演进与基础', 'YOLOv1网格预测', 'v2/v3 Anchor机制', '多尺度预测(FPN)', 'CSPDarknet53骨干', 'PANet路径聚合'],
                            ['现代版本', 'YOLOv5/Mosaic增强', 'v8 anchor-free/Decoupled Head', 'v9可编程梯度信息', 'v10 NMS-free端到端', 'YOLOX/YOLOR变体'],
                            ['评估与部署', 'IoU/NMS后处理', 'mAP/AP评估', 'TensorRT量化加速', '边缘部署(Jetson/NCNN)', '小目标检测优化']
                        ]
                    },
                    '人脸识别': {
                        'desc': '人脸检测、特征提取、身份验证',
                        'difficulty': 3,
                        'dimensions': [
                            ['人脸检测', 'MTCNN多任务级联', 'RetinaFace多尺度', 'YOLOv5-Face', '轻量检测(FaceBoxes/DBFace)', '关键点(5点/68点)与人脸对齐'],
                            ['特征提取', 'FaceNet三元组损失', 'ArcFace/CosFace角度间隔', 'InsightFace/VGGFace', '度量学习(Center Loss)', '人脸聚类与检索'],
                            ['应用与属性', '活体检测(眨眼/红外)', '年龄/性别/表情识别', '口罩与遮挡处理', '跨姿态/跨年龄识别', 'DeepFake与防伪']
                        ]
                    },
                    '图像分割': {
                        'desc': '像素级图像分割，包括语义分割和实例分割',
                        'difficulty': 3,
                        'dimensions': [
                            ['语义分割', 'FCN编码器-解码器', 'U-Net/UNet++', 'DeepLab(空洞卷积/ASPP)', 'PSPNet金字塔池化', 'SegNet/跳跃连接'],
                            ['实例与全景分割', 'Mask R-CNN(RoI Align)', 'YOLACT实时实例分割', 'SOLOv2动态分割', 'Panoptic FPN全景分割', 'PQ/mIoU评估指标'],
                            ['数据与优化', 'COCO/VOC/Cityscapes数据集', '数据增强与TTA', '医学影像分割(CT/MRI)', '遥感分割', '模型压缩与实时部署']
                        ]
                    },
                    '模型部署': {
                        'desc': '模型转换、量化、边缘设备部署',
                        'difficulty': 3,
                        'dimensions': [
                            ['导出与转换', 'PyTorch/TF模型保存', 'ONNX导出与优化', 'TensorRT推理加速', 'CoreML/TFLite移动端', 'NCNN/MNN嵌入式框架'],
                            ['量化与压缩', 'INT8/FP16量化', 'PTQ静态量化', 'QAT量化感知训练', '结构化/通道剪枝', '知识蒸馏'],
                            ['服务与运维', 'TorchServe/TF Serving', 'REST/gRPC API', 'Docker/K8s部署', '模型监控与灰度发布', '推理延迟与吞吐量优化']
                        ]
                    },
                    '目标检测': {
                        'desc': '定位并识别图像中的多个物体',
                        'difficulty': 3,
                        'dimensions': [
                            ['两阶段检测', 'Faster R-CNN/RPN', 'RoI Pooling与Align', 'Cascade R-CNN', 'FPN多尺度特征', 'NMS后处理'],
                            ['单阶段与Anchor-Free', 'SSD多尺度默认框', 'RetinaNet/Focal Loss', 'FCOS/CenterNet', 'DETR Transformer检测', 'Deformable DETR'],
                            ['损失与评估', 'Smooth L1/CIoU损失', '数据增强(Mosaic/CutMix)', 'COCO mAP/AP50', '小目标/密集/遮挡检测', '旋转目标检测与遥感应用']
                        ]
                    },
                    '视频分析': {
                        'desc': '目标跟踪、行为识别、视频理解',
                        'difficulty': 3,
                        'dimensions': [
                            ['动作识别', 'C3D/I3D 3D卷积', 'SlowFast双路径', 'TSN/TSM时序建模', 'TimeSformer/Video Transformer', 'Kinetics/UCF-101数据集'],
                            ['目标跟踪', 'SiamRPN/DiMP单目标', 'SORT/DeepSORT多目标', 'ByteTrack联合检测', 'ReID行人/车辆重识别', 'FairMOT/JDE'],
                            ['视频理解', '光流(Lucas-Kanade/Farneback)', '异常行为检测', '人数统计与密度估计', '步态/手势识别', '视频摘要与浓缩']
                        ]
                    }
                }
            }
        }
    }
}