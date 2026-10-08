# PulseBand — 文件与目录结构 / Repository layout

| 路径 / Path | 用途 / Purpose |
| --- | --- |
| `firmware/CORE/` | STM32 核心文件 |
| `firmware/FWLIB/` | STM32 标准外设库 |
| `firmware/HARDWAR/` | 板级传感器与外设驱动 |
| `firmware/SYSTEM/` | 系统支持代码 |
| `firmware/USER/Template.uvprojx` | 原 Keil 工程入口（工程内部相对路径未改动） |
| `firmware/OBJ/` | Keil 编译输出位置，生成文件不再跟踪 |
| `firmware/USER/Listings/` | Keil Listing 输出位置 |
| `firmware/prebuilt/Template.hex` | 原仓库内保留的 HEX 文件，内容未改动 |
| `hardware/` | PCB 与硬件资料 |
| `mobile-app/` | Android 配套应用文件 |
| `docs/` | 原有开发、硬件与贡献文档 |
| `README.md` / `README_zh-CN.md` | 英文、中文项目入口 |

本次仅整理仓库路径和文件归档，不修改固件、PCB、APP 及原有功能逻辑。早期 Keil 构建产物可从 Git 历史中找回。
