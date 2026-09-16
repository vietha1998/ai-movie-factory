#!/usr/bin/env python3
"""
Cài ffmpeg TĨNH vào tools/bin/ cho máy hiện tại (Mac arm64/x86_64, Windows x64, Linux x64).
Nguồn: gói PyPI imageio-ffmpeg (đóng gói sẵn binary ffmpeg static). Chỉ cần Python 3 + pip, không cần Homebrew.
Chạy 1 lần trên máy mới:   python3 tools/setup_ffmpeg.py      (Windows: py tools\setup_ffmpeg.py)
"""
import os, platform, stat, subprocess, sys, tempfile, zipfile
from pathlib import Path

BIN = Path(__file__).resolve().parent / "bin"
BIN.mkdir(parents=True, exist_ok=True)

sysname, arch = platform.system(), platform.machine().lower()
if sysname == "Darwin":
    plat = "macosx_11_0_arm64" if arch in ("arm64", "aarch64") else "macosx_10_9_x86_64"
    out = BIN / ("ffmpeg-macos-arm64" if "arm" in plat else "ffmpeg-macos-x86_64")
elif sysname == "Windows":
    plat, out = "win_amd64", BIN / "ffmpeg-win64.exe"
else:
    plat, out = "manylinux2014_x86_64", BIN / "ffmpeg-linux-x86_64"

if out.exists():
    print(f"Đã có: {out}"); sys.exit(0)

with tempfile.TemporaryDirectory() as td:
    cmd = [sys.executable, "-m", "pip", "download", "imageio-ffmpeg", "--only-binary=:all:",
           "--platform", plat, "--python-version", "3.9", "--no-deps", "-d", td]
    print("Tải:", " ".join(cmd[3:]))
    subprocess.run(cmd, check=True)
    whl = next(Path(td).glob("*.whl"))
    with zipfile.ZipFile(whl) as z:
        names = [n for n in z.namelist() if "/binaries/" in n and os.path.basename(n).startswith("ffmpeg") and not n.endswith(".txt")]
        if not names:
            sys.exit("Không thấy binary trong wheel")
        out.write_bytes(z.read(names[0]))
out.chmod(out.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
print(f"OK → {out} ({out.stat().st_size/1e6:.1f} MB)")
subprocess.run([str(out), "-version"], check=False)
