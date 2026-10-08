"""Check relative paths referenced by the checked-in Keil uVision project.

This is not a firmware compile: it only catches broken source/includes paths
before committing a directory reorganization.
"""
from pathlib import Path
from xml.etree import ElementTree as ET

project_file = Path(__file__).resolve().parents[1] / "firmware" / "USER" / "Template.uvprojx"
root = ET.parse(project_file).getroot()
missing = []
sources = 0
includes = 0

for node in root.iter("FilePath"):
    if not node.text or not node.text.strip():
        continue
    sources += 1
    relative_path = node.text.strip().replace("\\", "/")
    resolved = project_file.parent / relative_path
    if not resolved.is_file():
        missing.append(f"source: {relative_path}")

for node in root.iter("IncludePath"):
    if not node.text or not node.text.strip():
        continue
    for raw_path in node.text.split(";"):
        raw_path = raw_path.strip()
        if not raw_path:
            continue
        includes += 1
        relative_path = raw_path.replace("\\", "/")
        if "$" in relative_path or "%" in relative_path:
            continue  # toolchain-provided variable path
        if not (project_file.parent / relative_path).is_dir():
            missing.append(f"include: {relative_path}")

print(f"Keil project references: {sources} sources, {includes} include paths")
if missing:
    raise SystemExit("Missing referenced paths:\n" + "\n".join(missing))
print("All relative Keil source and include paths exist.")
