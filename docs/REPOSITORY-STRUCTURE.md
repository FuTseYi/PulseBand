# PulseBand — Repository structure

This file documents the **actual source layout** and highlights why the Keil project has not been reorganized blindly.

| Directory | Contents |
| --- | --- |
| `firmware/USER/` | Keil `Template.uvprojx`, MCU application and startup configuration |
| `firmware/CORE/` | Startup code and core support |
| `firmware/FWLIB/` | STM32F10x standard peripheral library |
| `firmware/HARDWAR/` | Sensor and peripheral drivers (MAX30102, ADXL345, OLED and others) |
| `firmware/SYSTEM/` | Board/system support code |
| `firmware/OBJ/` | Existing tracked Keil build outputs; ignored for new files |
| `hardware/` | PCB designs, circuit files and reference materials |
| `mobile-app/` | Android application release and project assets |
| `docs/` | Hardware, development and contribution guides |

Open `firmware/USER/Template.uvprojx` using Keil µVision. Its project settings reference relative source directories; changing firmware folder names can break the build. Firmware paths therefore remain untouched pending a build verification.

The `.gitignore` prevents *new* Keil machine-specific files and build products from being tracked, but does **not** delete already committed files. Existing outputs can be cleaned separately after comparing them with release assets.

This educational prototype is **not a medical diagnostic device**; listed sensor/accuracy claims should be independently validated before clinical use.
