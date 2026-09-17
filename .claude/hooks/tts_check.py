#!/usr/bin/env python3
"""PostToolUse (Edit|Write): khi kịch bản full_script_epN.md được sửa → chạy tools/tts_budget.py, báo kết quả vào context."""
import json, re, subprocess, sys, pathlib
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
ti = data.get("tool_input", {}) or {}
f = ti.get("file_path") or (data.get("tool_response", {}) or {}).get("filePath") or ""
if not re.search(r"02_script[\\/]full_script_ep\d+\.md$", f):
    sys.exit(0)
root = pathlib.Path(__file__).resolve().parents[2]
tool = root / "tools" / "tts_budget.py"
if not tool.exists():
    sys.exit(0)
r = subprocess.run([sys.executable, str(tool), f], capture_output=True, text=True)
out = (r.stdout or r.stderr).strip()
first = out.splitlines()[0] if out else "tts_budget: no output"
bad = "vượt ngưỡng: 0 SC" not in first
msg = ("⚠️ TTS budget: " if bad else "✅ TTS budget: ") + first
print(json.dumps({"systemMessage": msg, "hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "[hook tts_check] " + out[:1500]}}, ensure_ascii=False))
