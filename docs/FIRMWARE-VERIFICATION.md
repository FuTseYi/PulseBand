# PulseBand — Firmware verification

This is an **educational STM32F103 prototype**, not a validated medical or consumer wearable product. A clean repository and a valid Intel HEX file are only initial checks.

## Source-of-truth

- Keil µVision project: `firmware/USER/Template.uvprojx`
- Core firmware / peripheral drivers: `firmware/CORE/`, `firmware/FWLIB/`, `firmware/HARDWAR/`, `firmware/SYSTEM/`
- Historical compiled firmware snapshot: `firmware/prebuilt/Template.hex`
- Build output (ignored by Git): `firmware/OBJ/` and `firmware/USER/Listings/`

## Automated checks

The repository's pull request workflow runs:

```shell
python scripts/check_keil_paths.py
python scripts/check_hex_snapshot.py
```

The first command checks source/include relative paths referenced by the Keil project. The second verifies Intel HEX record lengths, per-record checksums, end-of-file framing and prints the snapshot's SHA-256 checksum.

**Passing these checks is not an MCU compilation or functional board test.** The prebuilt HEX snapshot should not be assumed suitable for every STM32F103 board.

## Build on a development workstation

1. Install a suitably licensed Keil MDK / µVision toolchain and the compatible STM32F1 device support pack.
2. Open `firmware/USER/Template.uvprojx`.
3. Review chip selection, compiler settings, peripheral pin mappings, clock frequency and flash configuration for the actual hardware revision.
4. Select **Project → Build Target** and review errors/warnings. Rebuild the HEX from current sources if possible.
5. Compare the generated binary and its SHA-256 checksum to the reference only if toolchain, configuration and firmware revision are known to match.
6. Before flashing through ST-Link, confirm supply voltage and pin connections; preserve a backup of the existing firmware where permitted.

## Hardware acceptance checklist

Verify sensor communication, display, wireless protocol, alarm logic and power consumption on actual hardware. Document board revision, test equipment, firmware hash and observed results. Claims about SpO2, heart-rate precision, step-count accuracy and battery life require independent reference measurements.

**No clinical or diagnostic validity is claimed.**
