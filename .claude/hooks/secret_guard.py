#!/usr/bin/env python3
"""PreToolUse (Bash): chặn lệnh ĐỌC/in nội dung config/glabs.env (API key).
Không chặn lệnh ghi file, lệnh chỉ nhắc tên file trong nội dung heredoc, hay tools/glabs_client.py (đọc trong code)."""
import json, re, sys
try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)
cmd = (data.get("tool_input", {}) or {}).get("command", "") or ""
PATH = r"[\w./\"'~$-]*glabs\.env\b"
patterns = [
    r"\b(cat|head|tail|less|more|bat|strings|base64|source|xxd|od)\s+(?:-\S+\s+)*" + PATH,   # cat config/glabs.env
    r"\b(grep|sed|awk|cut|tr|sort|uniq|python3?|perl|ruby|node)\b[^|;&\n<>]*\s" + PATH,      # grep KEY config/glabs.env
    r"<\s*" + PATH,                                                                          # < config/glabs.env
    r"^\s*\.\s+" + PATH,                                                                     # . config/glabs.env
    r"\$\(\s*cat\s+" + PATH,                                                                 # $(cat config/glabs.env)
]
if any(re.search(p, cmd, re.M) for p in patterns):
    print(json.dumps({
        "hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny",
            "permissionDecisionReason": "secret_guard: không đọc/in config/glabs.env (API key). Dùng tools/glabs_client.py (đọc trong code, không echo)."},
        "systemMessage": "🔒 secret_guard chặn lệnh đọc config/glabs.env"}, ensure_ascii=False))
sys.exit(0)
