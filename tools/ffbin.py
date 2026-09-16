#!/usr/bin/env python3
"""Tìm ffmpeg đi kèm dự án theo hệ điều hành (tools/bin/), fallback PATH.
Dùng: from tools.ffbin import ffmpeg_path  hoặc  python3 tools/ffbin.py
"""
import platform, shutil, sys
from pathlib import Path

BIN = Path(__file__).resolve().parent / "bin"

def ffmpeg_path():
    sysname, arch = platform.system(), platform.machine().lower()
    cands = []
    if sysname == "Darwin":
        cands += [BIN / ("ffmpeg-macos-arm64" if arch in ("arm64", "aarch64") else "ffmpeg-macos-x86_64")]
    elif sysname == "Windows":
        cands += [BIN / "ffmpeg-win64.exe"]
    else:
        cands += [BIN / "ffmpeg-linux-x86_64"]
    cands += [BIN / "ffmpeg", BIN / "ffmpeg.exe"]
    for c in cands:
        if c.exists():
            return str(c)
    found = shutil.which("ffmpeg")
    if found:
        return found
    raise FileNotFoundError("Không tìm thấy ffmpeg. Chạy: python3 tools/setup_ffmpeg.py")

if __name__ == "__main__":
    print(ffmpeg_path())
