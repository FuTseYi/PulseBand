# Security and hardware safety

PulseBand is an **educational STM32 wearable prototype**, not a medical device. Its firmware, mobile application, sensor readings, wireless transport and historical HEX snapshot have not undergone a formal security, clinical or electrical safety assessment.

## Important limitations

- Do not rely on heart-rate, SpO2, temperature, fall-detection or other readings for diagnosis or emergency response.
- Verify power connections and board revision before flashing or connecting battery-powered hardware.
- The [firmware verification guide](docs/FIRMWARE-VERIFICATION.md) describes basic integrity checks; these do not prove fitness for a particular board or safety-critical usage.
- Review any Wi-Fi credentials, companion-app network traffic, firmware update paths and third-party licenses before practical deployment.

## Reporting issues

Use GitHub private vulnerability reporting if enabled, or contact the maintainer privately through the GitHub profile contact method. Do not disclose secrets or exploitable details in a public issue. General bugs and documentation defects may be reported through [Issues](https://github.com/FuTseYi/PulseBand/issues).

No formal vulnerability-response SLA or medical safety certification is claimed.
