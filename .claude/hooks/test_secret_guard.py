#!/usr/bin/env python3
"""Test secret_guard.py — chạy: python3 .claude/hooks/test_secret_guard.py"""
import json, subprocess, pathlib
guard = pathlib.Path(__file__).with_name("secret_guard.py")
F = "config/glabs" + ".env"  # ghép chuỗi để lệnh chạy test không tự kích hoạt hook
cases = {
    f"cat {F}": "DENY", f"head -2 {F}": "DENY", f"grep KEY {F}": "DENY",
    f"python3 - < {F}": "DENY", f"source {F}": "DENY", f"echo $(cat {F})": "DENY",
    f"cat > .claude/commands/glabs.md <<'EOF'\nKHONG in noi dung {F}\nEOF": "allow",
    "python3 tools/glabs_client.py health": "allow", "ls config/": "allow",
    f"printf 'X=1\\n' > {F}": "allow", "git status": "allow",
}
ok = True
for c, exp in cases.items():
    r = subprocess.run(["python3", str(guard)], input=json.dumps({"tool_name": "Bash", "tool_input": {"command": c}}), capture_output=True, text=True)
    got = "DENY" if "deny" in r.stdout else "allow"
    ok &= got == exp
    print(f"{'✓' if got == exp else '✗'} {got:5} (mong {exp:5}) : {c.splitlines()[0][:60]}")
print("ALL OK" if ok else "CÓ LỖI")
raise SystemExit(0 if ok else 1)
