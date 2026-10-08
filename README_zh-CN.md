# PulseBand｜STM32 智能健康手环

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-STM32F103-red.svg)
![Language](https://img.shields.io/badge/language-C-blue.svg)
![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)

**基于 STM32F103 的开源可穿戴健康监测原型**

[功能特性](#-功能特性) • [快速开始](#-快速开始) • [硬件说明](#-硬件说明) • [开发文档](#-开发文档) • [贡献指南](#-贡献指南)

[English](README.md) | **中文**

</div>

---

![Star History Chart](https://api.star-history.com/svg?repos=FuTseYi/STM32-Health-Band&type=Date)

## 📖 项目简介

**PulseBand** 是一个基于 **STM32F103C8T6** 微控制器的开源智能健康手环项目。该项目集成了多种健康监测功能，包括心率检测、血氧饱和度监测、体温测量、计步器以及跌倒检测等。设备通过 ESP8266 WiFi 模块与手机 APP 实现无线通信，可实时查看健康数据并进行远程监控。

本项目适合嵌入式系统学习者、电子爱好者以及希望了解可穿戴设备开发的工程师。

## ✨ 功能特性

### 核心功能
- 🫀 **心率监测** - 基于 MAX30102 传感器的光电容积脉搏波描记法（PPG）
- 🩸 **血氧检测** - 实时监测血氧饱和度（SpO2）
- 🌡️ **体温测量** - 精确的体温监测功能
- 🚶 **智能计步** - 基于 ADXL345 三轴加速度传感器的计步算法
- 🚨 **跌倒检测** - 智能跌倒识别与报警系统
- 📱 **无线连接** - 通过 ESP8266-01S 模块连接手机 APP
- 📺 **实时显示** - OLED 屏幕实时显示各项健康数据
- 🔔 **声音报警** - 异常情况蜂鸣器提醒

### 技术特性
- ⚡ **低功耗设计** - 优化的电源管理，延长续航时间
- 🔄 **实时监测** - 100ms 数据采集周期，响应迅速
- 📊 **数据存储** - 支持历史数据缓存
- 🌐 **无线传输** - WiFi 实时数据上传
- 🎯 **高精度算法** - 经过校准的传感器算法，确保数据准确性

## 🚀 快速开始

### 硬件准备

#### 必需组件
| 组件 | 型号 | 数量 | 说明 |
|------|------|------|------|
| 主控芯片 | STM32F103C8T6 | 1 | ARM Cortex-M3，72MHz |
| 心率血氧传感器 | MAX30102 | 1 | IIC 接口 |
| 加速度传感器 | ADXL345 | 1 | 三轴加速度计 |
| 显示屏 | OLED 128×64 | 1 | SSD1306 驱动 |
| WiFi 模块 | ESP8266-01S | 1 | 无线通信 |
| 蜂鸣器 | 无源蜂鸣器 | 1 | 报警提示 |
| 调试器 | ST-Link V2 | 1 | 程序下载与调试 |

详细硬件清单和连接说明请参考 [硬件说明文档](docs/HARDWARE.md)

### 软件环境

#### 开发工具
- **IDE**: Keil uVision5（推荐 v5.29 或更高版本）
- **编译器**: ARM-MDK V5.06+
- **下载工具**: STM32 ST-LINK Utility 或 J-Link
- **串口工具**: 任意串口调试助手（波特率 115200）

#### 固件库
- STM32F10x 标准外设库（已包含在项目中）

### 编译与烧录

1. **克隆项目**
   ```bash
   git clone https://github.com/FuTseYi/STM32-Health-Band.git
   cd STM32-Health-Band
   ```

2. **打开工程**
   - 使用 Keil uVision5 打开 `firmware/USER/Template.uvprojx`

3. **编译项目**
   - 点击 `Project` → `Build Target` 或按 `F7`
   - 确保编译无错误和警告

4. **烧录程序**
   - 连接 ST-Link 到 STM32 开发板
   - 点击 `Flash` → `Download` 或按 `F8`

### 手机 APP 使用

1. **安装 APP**
   - 将 `mobile-app/发布版_手环APP.apk` 传输到 Android 手机
   - 安装 APK 文件（需允许安装未知来源应用）

2. **连接设备**
   - 手环上电后会自动创建 WiFi 热点
   - 手机连接到设备 WiFi：
     - **SSID**: `WIFI` / 密码: `123456789`
     - 或 **SSID**: `www` / 密码: `12345678`

3. **查看数据**
   - 打开手机 APP 即可实时查看健康数据

## 🔧 硬件说明

### 系统架构

```
┌─────────────────────────────────────────────────┐
│              STM32F103C8T6 主控                  │
│         (ARM Cortex-M3, 72MHz)                  │
└─────────────────────────────────────────────────┘
         │         │         │         │
    ┌────┴───┐ ┌──┴───┐ ┌──┴───┐ ┌──┴────┐
    │MAX30102│ │ADXL345│ │ OLED │ │ESP8266│
    │心率血氧│ │加速度 │ │ 显示 │ │ WiFi  │
    └────────┘ └───────┘ └──────┘ └───────┘
```

### 引脚连接

| STM32 引脚 | 连接设备 | 功能 |
|-----------|---------|------|
| PB8, PB9 | MAX30102 | IIC (SCL, SDA) |
| PA4, PA5 | ADXL345 | IIC (SCL, SDA) |
| PB6, PB7 | OLED | IIC (SCL, SDA) |
| PA9, PA10 | ESP8266 | UART (TX, RX) |
| PB5 | MAX30102 | 中断输入 |
| PC13 | 蜂鸣器 | GPIO 输出 |

完整硬件说明请查看 [硬件说明文档](docs/HARDWARE.md)

## 📂 项目结构

```
STM32-Health-Band/
├── firmware/                    # 固件源代码
│   ├── CORE/                   # STM32 核心文件
│   ├── FWLIB/                  # STM32 固件库
│   ├── HARDWAR/                # 硬件驱动层
│   │   ├── MAX30102.c/h        # 心率血氧传感器驱动
│   │   ├── adxl345.c/h         # 加速度传感器驱动
│   │   ├── OLED.c/h            # OLED 显示驱动
│   │   ├── timer.c/h           # 定时器驱动
│   │   └── IO_Init.c/h         # GPIO 初始化
│   ├── SYSTEM/                 # 系统层代码
│   │   ├── delay.c/h           # 延时函数
│   │   ├── sys.c/h             # 系统配置
│   │   └── usart.c/h           # 串口通信
│   └── USER/                   # 用户应用层
│       └── main.c              # 主程序
├── hardware/                    # 硬件相关文件
│   ├── pcb/                    # PCB 设计文件
│   ├── schematics/             # 电路原理图
│   └── datasheets/             # 硬件数据手册
├── mobile-app/                  # Android 手机 APP
├── docs/                        # 项目文档
│   ├── CONTRIBUTING.md         # 贡献指南
│   ├── DEVELOPMENT.md          # 开发文档
│   ├── HARDWARE.md             # 硬件说明
├── LICENSE                      # MIT 许可证
├── README.md                    # 英文 README
└── README_zh-CN.md             # 中文 README
```

## 💻 开发文档

### 核心算法

#### 心率检测算法
采用峰值检测算法，通过分析 MAX30102 传感器的 PPG 信号计算心率：
- 信号预处理与滤波
- 峰值检测与识别
- 心率计算（基于峰间间隔 RR-Interval）

#### 血氧饱和度算法
基于红光和红外光的吸收比率：
```
R = (AC_Red / DC_Red) / (AC_IR / DC_IR)
SpO2 = 110 - 25 × R
```

#### 跌倒检测算法
基于三轴加速度数据：
```
Total_G = √(X² + Y² + Z²)
跌倒判定: Total_G > 3g 或 Total_G < 0.5g
```

详细开发文档请参考 [开发文档](docs/DEVELOPMENT.md)

### 性能指标

| 指标 | 规格 |
|------|------|
| 心率检测范围 | 60-100 BPM |
| 血氧检测精度 | ±2% |
| 温度检测精度 | ±0.5°C |
| 计步精度 | ≥95% |
| 电池续航 | 约 6-24 小时 |
| WiFi 传输距离 | 室内 10-15 米 |
| 显示更新频率 | 10Hz |
| 数据采集周期 | 100ms |

## 🤝 贡献指南

我们欢迎任何形式的贡献！无论是报告 Bug、提出新功能建议，还是提交代码改进。

### 如何贡献
1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request

详细贡献指南请查看 [贡献指南](docs/CONTRIBUTING.md)

### 代码规范
- 函数命名：小写字母+下划线 `sensor_init()`
- 变量命名：小写字母+下划线 `sensor_data`
- 宏定义：大写字母+下划线 `MAX_BUFFER_SIZE`
- 注释：使用 Doxygen 风格注释

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

您可以自由地：
- ✅ 商业使用
- ✅ 修改
- ✅ 分发
- ✅ 私人使用

但需要：
- 📋 包含许可证和版权声明

## 👨‍💻 作者

**謝懿Shine** - *项目创建者和主要维护者*

## 🙏 致谢

感谢以下开源项目和资源：
- [STM32 标准外设库](https://www.st.com/)
- [Keil MDK-ARM](https://www.keil.com/)
- MAX30102、ADXL345 传感器厂商提供的参考代码
- 所有为本项目做出贡献的开发者

## 📞 联系方式

- 📧 **Issues**: [提交 Issue](https://github.com/YourUsername/STM32-Health-Band/issues)
- 💬 **Discussions**: [参与讨论](https://github.com/YourUsername/STM32-Health-Band/discussions)

## 📊 更新日志

### v1.0.0 (2025-01-03)
- ✨ 初始版本发布
- ✅ 实现心率、血氧、体温检测功能
- ✅ 添加计步和跌倒检测功能
- ✅ 完成 WiFi 数据传输
- ✅ 配套 Android APP 开发完成
- 📝 完善项目文档

---

<div align="center">

**⚠️ 免责声明**

本设备仅用于健康监测参考和学习研究，不可用于医疗诊断。  
如有健康问题，请咨询专业医疗机构。

**Made with ❤️ by 謝懿Shine**

</div>
