"""Validate Intel HEX framing and checksums of the preserved firmware image.

This checks file integrity only, not compatibility with actual hardware.
"""
import hashlib
from pathlib import Path


def validate_hex(path):
    records = 0
    data_bytes = 0
    eof = False
    for lineno, raw in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if eof:
            raise ValueError("Line {}: trailing records after EOF".format(lineno))
        if not line.startswith(":"):
            raise ValueError("Line {}: not an Intel HEX record".format(lineno))
        try:
            payload = bytes.fromhex(line[1:])
        except ValueError as exc:
            raise ValueError("Line {}: invalid hexadecimal bytes".format(lineno)) from exc
        if len(payload) < 5 or len(payload) != payload[0] + 5:
            raise ValueError("Line {}: invalid record length".format(lineno))
        if sum(payload) % 256:
            raise ValueError("Line {}: checksum mismatch".format(lineno))
        typ = payload[3]
        if typ not in (0, 1, 2, 3, 4, 5):
            raise ValueError("Line {}: unsupported record type".format(lineno))
        if typ == 0:
            data_bytes += payload[0]
        if typ == 1:
            if payload[0] != 0 or payload[1] != 0 or payload[2] != 0:
                raise ValueError("Line {}: malformed EOF".format(lineno))
            eof = True
        if typ == 4 and payload[0] != 2:
            raise ValueError("Line {}: malformed extended linear address".format(lineno))
        records += 1
    if not eof or not data_bytes:
        raise ValueError("No data records or terminal EOF record found")
    return records, data_bytes


if __name__ == "__main__":
    target = Path(__file__).resolve().parents[1] / "firmware/prebuilt/Template.hex"
    records, count = validate_hex(target)
    print("Intel HEX: {} valid records, {} data bytes".format(records, count))
    print("SHA-256:", hashlib.sha256(target.read_bytes()).hexdigest())
