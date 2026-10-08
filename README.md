# PulseBand

**STM32F103 wearable health-monitoring prototype**

<div align="center">

[![Keil & HEX checks](https://github.com/FuTseYi/PulseBand/actions/workflows/keil-path-check.yml/badge.svg)](https://github.com/FuTseYi/PulseBand/actions/workflows/keil-path-check.yml)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-STM32F103-red.svg)
![Language](https://img.shields.io/badge/language-C-blue.svg)
![Status](https://img.shields.io/badge/status-prototype-lightgrey.svg)

**An open-source embedded wearable prototype**

[Features](#-features) • [Quick Start](#-quick-start) • [Hardware](#-hardware-description) • [Development](#-development-documentation) • [Contributing](#-contributing)

[中文](README_zh-CN.md) | **English**

</div>

---
![Star History Chart](https://api.star-history.com/svg?repos=FuTseYi/PulseBand&type=Date)

## 📖 Project Overview

PulseBand is an open-source smart health band project based on the **STM32F103C8T6** microcontroller. This project integrates multiple health monitoring functions, including heart rate detection, blood oxygen saturation monitoring, body temperature measurement, pedometer, and fall detection. The device communicates wirelessly with a mobile APP through the ESP8266 WiFi module for real-time health data viewing and remote monitoring.

This project is suitable for embedded system learners, electronics enthusiasts, and engineers interested in wearable device development.

## ✨ Features

### Core Functions
- 🫀 **Heart Rate Monitoring** - Based on MAX30102 sensor using Photoplethysmography (PPG)
- 🩸 **Blood Oxygen Detection** - Real-time SpO2 monitoring
- 🌡️ **Temperature Measurement** - Accurate body temperature monitoring
- 🚶 **Smart Pedometer** - Step counting algorithm based on ADXL345 3-axis accelerometer
- 🚨 **Fall Detection** - Intelligent fall recognition and alarm system
- 📱 **Wireless Connection** - Connect to mobile APP via ESP8266-01S module
- 📺 **Real-time Display** - OLED screen displays health data in real-time
- 🔔 **Audio Alarm** - Buzzer alerts for abnormal conditions

### Technical Features
- ⚡ **Power Management** - Battery-powered design; runtime has not been independently benchmarked
- 🔄 **Real-time Monitoring** - 100ms data acquisition cycle, fast response
- 📊 **Data Storage** - Support for historical data caching
- 🌐 **Wireless Transmission** - WiFi real-time data upload
- 🎯 **Sensor Signal Processing** - Physiological estimates require calibration and evaluation against reference instruments

## 🚀 Quick Start

### Hardware Requirements

#### Essential Components
| Component | Model | Quantity | Description |
|-----------|-------|----------|-------------|
| MCU | STM32F103C8T6 | 1 | ARM Cortex-M3, 72MHz |
| Heart Rate & SpO2 Sensor | MAX30102 | 1 | IIC Interface |
| Accelerometer | ADXL345 | 1 | 3-axis accelerometer |
| Display | OLED 128×64 | 1 | SSD1306 driver |
| WiFi Module | ESP8266-01S | 1 | Wireless communication |
| Buzzer | Passive Buzzer | 1 | Alarm notification |
| Debugger | ST-Link V2 | 1 | Program download & debug |

For detailed hardware list and connection instructions, please refer to [hardware documentation](docs/HARDWARE.md)

### Software Environment

#### Development Tools
- **IDE**: Keil uVision5 (v5.29 or higher recommended)
- **Compiler**: ARM-MDK V5.06+
- **Download Tool**: STM32 ST-LINK Utility or J-Link
- **Serial Tool**: Any serial debugging assistant (Baud rate 115200)

#### Firmware Library
- STM32F10x Standard Peripheral Library (included in the project)

### Compilation & Flashing

1. **Clone the Project**
   ```bash
   git clone https://github.com/FuTseYi/PulseBand.git
   cd PulseBand
   ```

2. **Open Project**
   - Open `firmware/USER/Template.uvprojx` with Keil uVision5

3. **Compile Project**
   - Click `Project` → `Build Target` or press `F7`
   - Ensure no errors or warnings

4. **Flash Program**
   - Connect ST-Link to STM32 development board
   - Click `Flash` → `Download` or press `F8`

**Build outputs:** Keil writes generated objects to `firmware/OBJ/` and listings to `firmware/USER/Listings/`. These build artifacts are intentionally ignored. A previously committed `Template.hex` snapshot is preserved under [`firmware/prebuilt/`](firmware/prebuilt/); its hardware compatibility has not been independently verified. For a reproducible firmware image, rebuild from source in Keil.

For validation and device-build limitations, see [Firmware verification](docs/FIRMWARE-VERIFICATION.md). The retained `firmware/prebuilt/Template.hex` is a historical snapshot, **not a hardware-tested release**.

### Mobile APP Usage

1. **Install APP**
   - Transfer `mobile-app/发布版_手环APP.apk` to Android phone
   - Install APK file (allow installation from unknown sources)

2. **Connect Device**
   - The band will automatically create a WiFi hotspot after power-on
   - Connect phone to device WiFi:
     - **SSID**: `WIFI` / Password: `123456789`
     - Or **SSID**: `www` / Password: `12345678`

3. **View Data**
   - Open the mobile APP to view real-time health data

## 🔧 Hardware Description

### System Architecture

```
┌─────────────────────────────────────────────────┐
│           STM32F103C8T6 Main Controller          │
│            (ARM Cortex-M3, 72MHz)                │
└─────────────────────────────────────────────────┘
         │         │         │         │
    ┌────┴───┐ ┌──┴───┐ ┌──┴───┐ ┌──┴────┐
    │MAX30102│ │ADXL345│ │ OLED │ │ESP8266│
    │HR & SpO2│ │Accel. │ │Display│ │ WiFi  │
    └────────┘ └───────┘ └──────┘ └───────┘
```

### Pin Connections

| STM32 Pin | Connected Device | Function |
|-----------|------------------|----------|
| PB8, PB9 | MAX30102 | IIC (SCL, SDA) |
| PA4, PA5 | ADXL345 | IIC (SCL, SDA) |
| PB6, PB7 | OLED | IIC (SCL, SDA) |
| PA9, PA10 | ESP8266 | UART (TX, RX) |
| PB5 | MAX30102 | Interrupt Input |
| PC13 | Buzzer | GPIO Output |

For hardware notes, see [hardware documentation](docs/HARDWARE.md)

## 📂 Project Structure

```text
PulseBand/
├── firmware/       # Keil uVision project, STM32 drivers and application
│   ├── CORE/
│   ├── FWLIB/
│   ├── HARDWAR/
│   ├── SYSTEM/
│   └── USER/       # Template.uvprojx and main.c
├── hardware/       # PCB, schematics and hardware references
├── mobile-app/     # Companion Android APK and project files
├── docs/           # Hardware, development and contribution guides
├── README.md
├── README_zh-CN.md
└── LICENSE
```

## 💻 Development Documentation

### Core Algorithms

#### Heart Rate Detection Algorithm
Peak detection algorithm analyzes PPG signals from MAX30102 sensor to calculate heart rate:
- Signal preprocessing and filtering
- Peak detection and recognition
- Heart rate calculation (based on RR-Interval)

#### Blood Oxygen Saturation Algorithm
Based on the absorption ratio of red and infrared light:
```
R = (AC_Red / DC_Red) / (AC_IR / DC_IR)
SpO2 = 110 - 25 × R
```

#### Fall Detection Algorithm
Based on 3-axis acceleration data:
```
Total_G = √(X² + Y² + Z²)
Fall Detection: Total_G > 3g or Total_G < 0.5g
```

For detailed development documentation, refer to [development documentation](docs/DEVELOPMENT.md)

### Reported Specifications and Verification Status

The following values are taken from prior project documentation. **No independent measurement dataset or calibration protocol is currently included in this repository.** Accuracy and battery-life claims are therefore not verified benchmarks.

| Specification | Value |
|--------------|-------|
| Heart Rate Range | 60-100 BPM |
| SpO2 Accuracy | Not independently verified |
| Temperature Accuracy | Not independently verified |
| Pedometer Accuracy | Not independently verified |
| Battery Life | Not independently benchmarked |
| WiFi Range | Indoor 10-15 meters |
| Display Refresh Rate | 10Hz |
| Data Acquisition Cycle | 100ms |

## 🤝 Contributing

We welcome all forms of contributions! Whether it's reporting bugs, suggesting new features, or submitting code improvements.

### How to Contribute
1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For detailed contribution guidelines, see [contribution guidelines](docs/CONTRIBUTING.md)

### Code Style
- Function naming: lowercase + underscore `sensor_init()`
- Variable naming: lowercase + underscore `sensor_data`
- Macro definition: uppercase + underscore `MAX_BUFFER_SIZE`
- Comments: Use Doxygen style comments

For vulnerability reporting and hardware-use limitations, see [SECURITY.md](SECURITY.md).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use

With the requirement:
- 📋 Include license and copyright notice

## 👨‍💻 Author

**謝懿Shine** - *Project Creator and Main Maintainer*

## 🙏 Acknowledgments

Thanks to the following open source projects and resources:
- [STM32 Standard Peripheral Library](https://www.st.com/)
- [Keil MDK-ARM](https://www.keil.com/)
- Reference code provided by MAX30102 and ADXL345 sensor manufacturers
- All developers who contributed to this project

## 📞 Contact

- 📧 **Issues**: [Submit Issue](https://github.com/FuTseYi/PulseBand/issues)
- 💬 **Discussions**: [Join Discussion](https://github.com/FuTseYi/PulseBand/discussions)

## 📊 Changelog

### v1.0.0 (2025-01-03)
- ✨ Initial release
- ✅ Implemented heart rate, SpO2, and temperature detection
- ✅ Added pedometer and fall detection features
- ✅ Completed WiFi data transmission
- ✅ Developed companion Android APP
- 📝 Improved project documentation

---

<div align="center">

**⚠️ Disclaimer**

This device is for health monitoring reference and educational purposes only, not for medical diagnosis.  
For health concerns, please consult professional medical institutions.

**An educational embedded systems prototype**

</div>

