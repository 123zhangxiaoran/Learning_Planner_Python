"""IoT开发工程师数据"""
data = {
    '计算机与信息技术': {
        '物联网工程': {
            'IoT开发工程师': {
                'description': '开发物联网应用，实现设备连接、云端数据传输和控制。',
                'skills': {
                    'Python': {
                        'desc': '物联网应用层开发语言',
                        'difficulty': 1,
                        'dimensions': [
                            ['核心语法与数据', '数据类型/控制流程/函数/lambda', '文件操作与异常处理', '模块与包管理', '标准库(datetime/re/collections)'],
                            ['网络与并发', 'socket/TCP/UDP/HTTP客户端', '多线程/多进程/异步IO(asyncio/aiohttp)', 'JSON/XML解析与序列化'],
                            ['物联网与嵌入式', 'MicroPython/TensorFlow Lite', 'GPIO控制(RPi.GPIO/GPIO Zero)', '传感器读取', '云平台SDK(requests)'],
                            ['物联网通信', 'MQTT客户端(paho-mqtt)', '数据上报与订阅', 'REST API调用', '虚拟环境与依赖管理(requirements.txt)']
                        ]
                    },
                    'CoAP': {
                        'desc': '受限应用协议，适用于低功耗设备',
                        'difficulty': 2,
                        'dimensions': [
                            ['协议基础', '与HTTP对比/设计目标', '消息类型(CON/NON/ACK/RST)', '请求方法(GET/POST/PUT/DELETE)', 'URI/载荷/选项(Content-Format/ETag)'],
                            ['可靠性与扩展', '消息ID/令牌/重传', '资源观察(Observe)订阅', '块传输(Blockwise)分片', '代理/缓存/CoAP-HTTP网关'],
                            ['安全与实现', 'DTLS/预共享密钥/证书', 'Libcoap/aiocoap/Californium库', '服务器/客户端实现', 'AIoT设备轻量化应用']
                        ]
                    },
                    'HTTP/REST': {
                        'desc': 'Web API通信',
                        'difficulty': 2,
                        'dimensions': [
                            ['HTTP基础', '请求响应模型/状态码', '方法(GET/POST/PUT/DELETE)', '请求头/响应头/Content-Type', '持久连接/压缩/缓存控制'],
                            ['RESTful设计', '资源命名/版本管理', '错误处理/分页/过滤', 'JSON/XML数据交换', 'API文档规范'],
                            ['物联网集成', '物联网平台API/设备影子', 'Webhook回调/订阅推送', '身份验证(Bearer Token/API Key)', 'HTTPS/TLS安全传输'],
                            ['客户端库', 'requests/httpx/aiohttp', '请求构造与解析', '超时与重试机制']
                        ]
                    },
                    'MQTT': {
                        'desc': '物联网轻量级消息传输协议',
                        'difficulty': 2,
                        'dimensions': [
                            ['协议核心', '发布订阅模式/消息代理', '连接流程/心跳', 'QoS等级(0/1/2)与服务质量', 'Topic与通配符(+/#)', '遗嘱消息/保留消息/客户端ID'],
                            ['安全与代理', '用户名密码/认证', 'TLS加密/证书认证', 'Broker(Mosquitto/EMQX/ActiveMQ)'],
                            ['高级与工具', 'MQTT5新特性/用户属性', 'MQTT-SN传感器网络', '调试工具(MQTT.fx/MQTT Explorer)', 'QoS与网络选择策略']
                        ]
                    },
                    '云平台': {
                        'desc': '阿里云IoT、AWS IoT、Azure IoT等平台',
                        'difficulty': 2,
                        'dimensions': [
                            ['主流云平台', '阿里云IoT/物模型/规则引擎', 'AWS IoT Core/Device Shadow/Certificate', 'Azure IoT Hub/设备预配服务/DPS', '腾讯云IoT/百度天工/OneNET'],
                            ['设备与边缘', '设备SDK/认证机制/连接协议', '设备影子/状态同步/期望属性', 'OTA升级/远程配置/诊断', 'AWS Greengrass/Azure IoT Edge边缘计算'],
                            ['数据处理', '规则引擎/SQL处理', '数据转发/时序数据库', 'API/AMQP微消息队列']
                        ]
                    },
                    '传感器': {
                        'desc': '温湿度、光照、加速度等各类传感器数据采集',
                        'difficulty': 2,
                        'dimensions': [
                            ['分类与接口', '模拟/数字/有源/无源', 'I2C/SPI/UART传感器接口'],
                            ['常见传感器', '温湿度(DHT11/SHT20/BME280)', '光照(BH1750/光敏电阻)', '加速度/陀螺仪(MPU6050/ADXL345)', '气压(BMP280)/气体(MQ-2)/称重(HX711)', '超声波(HC-SR04)/红外/磁力计(HMC5883L)'],
                            ['数据处理', '卡尔曼/低通/滑动平均滤波', '传感器校准/线性化/温度补偿', '选型(精度/量程/功耗)']
                        ]
                    },
                    '单片机': {
                        'desc': 'Arduino、ESP32、树莓派等开发',
                        'difficulty': 2,
                        'dimensions': [
                            ['Arduino', 'IDE/Wiring语言', '数字/模拟IO/PWM', '库与Shields扩展板', '常用库(Millis/DHT/WiFi)'],
                            ['ESP32', 'Arduino Core/开发环境', 'WiFi/BLE连接/低功耗', '外设(I2C/SPI/UART/ADC/DAC)', 'GPIO控制'],
                            ['树莓派', 'GPIO/WiringPi/设备树', '系统安装/SD卡/联网配置', 'I2C/SPI/UART配置', '摄像头/OpenCV/Docker网关'],
                            ['其他单片机', 'STM32(HAL/标准库)/定时器/中断/串口', '51单片机基础']
                        ]
                    },
                    '可视化': {
                        'desc': '设备数据可视化和监控',
                        'difficulty': 2,
                        'dimensions': [
                            ['图表与库', 'ECharts/AntV/D3.js', '实时数据刷新策略', 'WebSocket实时推送'],
                            ['仪表盘与展示', 'Grafana面板配置', 'MQTT Dashboard', '大屏/响应式/地图可视化', '移动端H5嵌入'],
                            ['告警与数据', '阈值告警/实时告警', '历史存储/时序展示', '数据导出/报表生成']
                        ]
                    },
                    '数据传输协议': {
                        'desc': 'HTTP、CoAP、LwM2M等协议',
                        'difficulty': 2,
                        'dimensions': [
                            ['应用层协议', 'HTTP/CoAP/LwM2M', 'WebSocket全双工/Socket TCP/UDP'],
                            ['工业与底层', 'Modbus RTU/TCP/串口', 'CAN总线/LoRaWAN/NB-IoT/ZigBee'],
                            ['协议转换与安全', '协议选择策略/网关桥接', '数据格式(JSON/二进制/Protobuf)', '安全传输(TLS/DTLS)']
                        ]
                    },
                    '数据存储': {
                        'desc': '时序数据库如InfluxDB',
                        'difficulty': 2,
                        'dimensions': [
                            ['时序数据库', 'InfluxDB(写入/InfluxQL/Telegraf)', 'TDengine(超级表)', '数据压缩/保留策略(RP)'],
                            ['通用与缓存', 'MySQL分表/时序', 'MongoDB文档/设备数据', 'Redis缓存/最新数据'],
                            ['操作与维护', '聚合查询/GROUP BY时间', '降采样/连续查询(CQ)', '数据备份/恢复/Grafana可视化']
                        ]
                    },
                    '设备管理': {
                        'desc': 'OTA升级、设备注册、生命周期管理',
                        'difficulty': 2,
                        'dimensions': [
                            ['注册与认证', '设备ID/凭证/激活', 'X.509证书/对称密钥', '设备影子/状态同步'],
                            ['OTA与配置', 'OTA差分升级/签名验证/回滚', '远程配置/参数下发/诊断日志', '固件版本管理'],
                            ['生命周期与监控', '注册/激活/退役', '设备告警/阈值/异常检测', '心跳/在线离线状态', '分组/批量操作']
                        ]
                    },
                    '边缘计算': {
                        'desc': '边缘网关和本地数据处理',
                        'difficulty': 3,
                        'dimensions': [
                            ['概念与硬件', '云边协同/雾计算', '边缘网关选型', '边缘AI/NPU推理加速'],
                            ['数据处理与存储', '本地过滤/聚合', '边缘数据库/缓存', '断网续传/离线运行'],
                            ['边缘平台', 'KubeEdge/OpenYurt/K3s', 'AWS Greengrass/边缘Lambda', 'Azure IoT Edge/模块部署', 'TensorFlow Lite/ONNX边缘推理'],
                            ['安全与自治', '可信执行环境(TEE)', '本地决策/自治', '边缘编排/自动化脚本']
                        ]
                    }
                }
            }
        }
    }
}