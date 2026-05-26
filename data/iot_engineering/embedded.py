"""嵌入式工程师数据"""
data = {
    '计算机与信息技术': {
        '物联网工程': {
            '嵌入式工程师': {
                'description': '开发嵌入式系统，编写硬件驱动，实现设备功能。',
                'skills': {
                    'C': {
                        'desc': '嵌入式开发底层编程语言',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础与数据类型', '基本数据类型(int/float/char)', '指针与结构体', 'sizeof与类型转换', '关键字(const/volatile/static/extern)', '位运算与字节序'],
                            ['控制与函数', '条件与循环(if/switch/for/while)', '函数定义与参数传递(值/指针/数组)', '递归', '标准库函数(printf/scanf/memcpy)', '代码规范(MISRA-C)'],
                            ['数组与字符串', '一维/二维数组', '字符串处理(strlen/strcpy/strcat/strcmp)', '指针与数组关系', '数组指针与指针数组'],
                            ['内存与预编译', '动态内存(malloc/free/realloc)', '内存泄漏与段错误', '预处理(#define/#include/#ifdef)', '条件编译', '编译优化与段属性'],
                            ['嵌入式C扩展', '寄存器操作与intrinsic', '__attribute__', '函数指针与回调', '中断服务函数编写', '裸机程序结构']
                        ]
                    },
                    'C++': {
                        'desc': '面向对象嵌入式开发',
                        'difficulty': 1,
                        'dimensions': [
                            ['基础与面向对象', '命名空间与作用域', '类与对象(构造/析构/拷贝/移动)', '封装/继承/多态', '虚函数/纯虚函数/抽象类', '访问控制与友元'],
                            ['高级特性', '运算符重载', '模板(函数/类/特化)', '智能指针(shared_ptr/unique_ptr/weak_ptr)', '异常处理(try/catch/noexcept)', 'STL容器与算法(vector/list/map)'],
                            ['现代C++', 'C++11/14/17新特性', 'auto/范围for/lambda/decltype', '移动语义与右值引用', 'nullptr与constexpr', '嵌入式优化(RTTI/异常关闭/模板控制)']
                        ]
                    },
                    'ADC/DAC': {
                        'desc': '模数/数模转换',
                        'difficulty': 2,
                        'dimensions': [
                            ['ADC基础', '工作原理(逐次逼近/Σ-Δ)', '分辨率(8/10/12/16位)', '量化误差与LSB', '采样定理与奈奎斯特频率', '混叠与抗混叠滤波'],
                            ['ADC配置', '采样率与转换时间', '参考电压(Vref/内部/外部)', '输入类型(单端/差分)', 'DMA/中断/轮询模式', '校准(零点/满量程)'],
                            ['DAC基础', '工作原理(权电阻/梯形/PWM)', '分辨率与输出范围', '建立时间与压摆率', '缓冲与无缓冲输出'],
                            ['精度与应用', 'INL/DNL/ENOB/SINAD/SNR/THD', '热敏电阻/称重传感器采集', '音频采集与电压监测', '实际项目调试']
                        ]
                    },
                    'ESP32': {
                        'desc': '乐鑫WiFi/蓝牙芯片开发',
                        'difficulty': 2,
                        'dimensions': [
                            ['开发环境与基础', 'ESP-IDF/Arduino/VSCode', 'CMake构建与工程结构', 'GPIO配置(输入/输出/上下拉)', 'FreeRTOS任务与队列', '日志系统与看门狗'],
                            ['无线通信', 'WiFi STA/SoftAP模式', 'WiFi配网与事件处理', 'BLE广播/扫描/连接', 'GATT/Characteristic/Service', 'MQTT/TCP/UDP/HTTP'],
                            ['外设与存储', 'ADC/DAC/PWM/LEDC', 'I2C/SPI/UART/I2S', 'NVS/SPIFFS/FAT文件系统', 'OTA升级', '定时器与脉冲计数器'],
                            ['功耗与调试', '睡眠模式(浅睡/深睡)', 'RTC唤醒源', '低功耗外设配置', '调试技巧与错误处理', '实际项目实践']
                        ]
                    },
                    'GPIO': {
                        'desc': '通用输入输出控制',
                        'difficulty': 2,
                        'dimensions': [
                            ['结构与模式', 'GPIO内部结构(施密特触发器)', '输入模式(浮空/上拉/下拉)', '输出模式(推挽/开漏)', '复用功能(AF)', '模拟模式'],
                            ['电气特性', '推挽与开漏区别', '上拉电阻选择', '翻转速度(2/10/50MHz)', '负载电容与驱动能力', '防抖处理(硬件/软件)'],
                            ['中断与控制', '外部中断(EXTI)与NVIC', '边沿/电平触发', '中断优先级与嵌套', 'BSRR/ODR寄存器操作', 'GPIO扩展芯片(74HC595)'],
                            ['应用实践', '按键与LED驱动', '蜂鸣器与继电器', '光耦隔离', '实际项目调试']
                        ]
                    },
                    'I2C/SPI/UART': {
                        'desc': '常用硬件通信协议',
                        'difficulty': 2,
                        'dimensions': [
                            ['I2C总线', '起始/停止/应答位', '7/10位地址与广播', '主从模式与时钟同步', '速度(100k/400k/1M)', 'SCL stretching与重复起始'],
                            ['I2C设备与实战', 'EEPROM读写(AT24Cxx)', '页写入与随机读取', '传感器(SHT20/MPU6050/ADS1115)', 'BMP280'],
                            ['SPI总线', '四线(SCLK/MOSI/MISO/SS)', '模式(CPOL/CPHA)0-3', '时钟分频与数据顺序', '全双工/半双工/DMA传输', 'Flash驱动(W25Qxx)'],
                            ['UART通信', '异步帧格式(起始/数据/校验/停止)', '波特率与误差容忍', '流控(RTS/CTS)', 'RS232/RS485/TTL电平', 'DMA环形缓冲区与队列']
                        ]
                    },
                    'PWM': {
                        'desc': '脉冲宽度调制',
                        'difficulty': 2,
                        'dimensions': [
                            ['原理与配置', '占空比/频率/分辨率', '定时器结构(预分频/重载)', '边沿对齐/中心对齐', '互补输出与死区', 'CCR寄存器计算'],
                            ['电机与舵机', 'H桥驱动(L298N/TB6612)', 'PWM调压调速', '舵机控制(50Hz/0.5-2.5ms)', '角度计算'],
                            ['高级应用', '呼吸灯与调光', '声音输出与蜂鸣器', '伪DAC与滤波电路', '红外遥控编码', '编码器解码']
                        ]
                    },
                    'RTOS': {
                        'desc': '实时操作系统开发和任务调度，如FreeRTOS',
                        'difficulty': 2,
                        'dimensions': [
                            ['任务与调度', '硬实时/软实时概念', '任务创建与删除', '任务状态(运行/就绪/阻塞/挂起)', '优先级与时间片轮转', 'Tick中断与心跳时钟'],
                            ['任务间通信', '队列(xQueueCreate/Send/Receive)', '信号量(二进制/计数)', '互斥量/递归互斥量/优先级继承', '事件组(EventGroup)', '任务通知(Task Notify)'],
                            ['定时器与内存', '软件定时器(一次性/周期性)', '内存管理(heap_1-5)', '堆分配策略', '临界段与中断保护'],
                            ['高级特性', '低功耗(Tickless模式)', '延时函数(vTaskDelay/DelayUntil)', '队列/信号量/互斥量选择', '实际项目应用']
                        ]
                    },
                    'STM32': {
                        'desc': '意法半导体ARM Cortex-M系列开发',
                        'difficulty': 2,
                        'dimensions': [
                            ['平台与内核', '产品线(F0/F1/F4/H7/L系列)', 'Cortex-M内核(寄存器/堆栈)', '启动文件与中断向量表', '时钟树(HSE/LSE/PLL)', 'SysTick定时器'],
                            ['外设与接口', 'GPIO/EXTI/NVIC', 'USART/UART/DMA', 'SPI/I2C通信', '定时器(输入捕获/输出比较/PWM)', 'ADC/DAC多通道'],
                            ['系统与存储', 'DMA控制器(通道/循环)', '看门狗(IWDG/WWDG)', 'RTC实时时钟与备份寄存器', 'PWR电源管理(睡眠/停机/待机)', 'Flash读写与写保护'],
                            ['开发库', 'HAL/LL/标准库', 'CubeMX配置', 'printf重定向', '调试技巧', '实际项目']
                        ]
                    },
                    '调试工具': {
                        'desc': '示波器、逻辑分析仪、JTAG调试器',
                        'difficulty': 2,
                        'dimensions': [
                            ['示波器', '带宽/采样率/存储深度', '触发类型(边沿/脉宽/I2C/SPI)', '探头(1x/10x)与接地', '测量(幅值/频率/周期/占空比)', '协议解码功能'],
                            ['逻辑分析仪', '采样与协议解码', '触发条件设置', 'I2C/SPI/UART解码', 'Saleae逻辑分析仪'],
                            ['调试器', 'JTAG接口(TDI/TDO/TCK/TMS)', 'SWD接口(SWDIO/SWCLK)', 'ST-Link/J-Link/OpenOCD', 'GDB调试(断点/单步/内存查看)'],
                            ['硬件调试', '串口日志输出', '分段排除与隔离', '信号完整性与电磁干扰', '去耦电容与滤波', '屏蔽与接地']
                        ]
                    },
                    'ARM': {
                        'desc': 'ARM处理器架构和编程',
                        'difficulty': 3,
                        'dimensions': [
                            ['架构与指令', 'ARMv6/7/8/9与Cortex-A/R/M', 'ARM/Thumb/Thumb-2指令集', '数据处理与Load-Store', '条件执行', 'NEON SIMD与VFP'],
                            ['编程模型', '工作模式(用户/系统/IRQ/FIQ)', '寄存器组(R0-R15/CPSR/SPSR)', '异常与中断向量表', 'ATPCS调用规范', 'ARM汇编伪指令与宏'],
                            ['系统控制', 'MMU与页表', 'Cache(I-Cache/D-Cache)一致性', '协处理器CP15', 'TrustZone安全', '启动代码与链接脚本']
                        ]
                    },
                    '嵌入式Linux': {
                        'desc': 'Linux内核裁剪和驱动开发',
                        'difficulty': 3,
                        'dimensions': [
                            ['系统构建', 'Bootloader(U-Boot)/Kernel/Rootfs', '交叉编译工具链', 'Makefile/CMake/Kconfig', '内核配置与裁剪', 'BusyBox/buildroot根文件系统'],
                            ['驱动开发', '字符设备驱动(file_operations)', '设备号与设备节点', '平台设备驱动(platform_driver)', '设备树(.dts/.dtsi)与compatible'],
                            ['内核机制', '中断处理(顶半部/底半部)', 'workqueue/tasklet/软中断', '同步机制(自旋锁/互斥量/信号量)', 'DMA驱动(scatter-gather)', 'ioctl/netlink通信'],
                            ['子系统', 'GPIO/LED/Input子系统', 'I2C子系统(适配器/设备分离)', 'SPI子系统与Flash驱动', '文件系统(JFFS2/UBIFS/EXT4)'],
                            ['调试与模块', '内核模块(insmod/rmmod)', 'printk/dev_err调试', 'proc/sys文件系统', 'Misc设备', '电源管理']
                        ]
                    },
                    '汇编': {
                        'desc': '底层硬件操作和性能优化',
                        'difficulty': 3,
                        'dimensions': [
                            ['ARM汇编', 'ARM数据处理/Load-Store指令', 'Thumb指令集', 'ARM伪指令(LDR/ADR/ADRL)', '位置无关代码(PIC)', '启动代码与向量表'],
                            ['x86汇编', 'x86寄存器与指令格式', 'AT&T/Intel语法', '汇编器(GAS/NASM/MASM)', '伪指令(.global/.section/.word)'],
                            ['混合编程', 'C内联汇编(__asm__)', 'C调用汇编/汇编调用C', '子程序调用与栈帧', '参数传递与返回值'],
                            ['优化与逆向', '汇编优化(指令调度/寄存器分配)', 'SIMD指令(SSE/AVX/NEON)', 'DSP汇编优化', '反汇编(IDA Pro/Ghidra)', '固件分析与漏洞挖掘']
                        ]
                    },
                    '硬件驱动': {
                        'desc': '设备驱动开发和硬件接口编程',
                        'difficulty': 3,
                        'dimensions': [
                            ['裸机驱动', '寄存器操作与位操作', '读写时序图', '轮询/中断/DMA模式', 'GPIO/UART/I2C/SPI/CAN/USB'],
                            ['Linux设备驱动', '字符设备驱动(file_operations)', '设备号与devfs自动创建设备节点', '平台设备驱动(platform_driver)', '设备树匹配与OF compatible'],
                            ['内核驱动框架', 'I2C驱动(i2c_driver/i2c_client)', 'SPI驱动(spi_driver/spi_device)', '中断处理(request_irq/threaded_irq)', '同步互斥(自旋锁/互斥锁/信号量)'],
                            ['高级主题', 'DMA传输(dmaengine)', '缓存一致性', '电源管理(suspend/resume/runtime_pm)', '驱动调试(printk/dev_err)', '实际驱动开发实践']
                        ]
                    }
                }
            }
        }
    }
}