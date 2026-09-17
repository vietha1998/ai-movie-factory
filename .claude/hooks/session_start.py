#!/usr/bin/env python3
"""SessionStart: nạp tóm tắt trạng thái project hiện tại vào context."""
import json, sys, pathlib, glob
root = pathlib.Path(__file__).resolve().parents[2]
states = sorted(glob.glob(str(root / "projects" / "*" / "project_state.json")))
lines = []
for s in states:
    try:
        d = json.loads(pathlib.Path(s).read_text())
    except Exception:
        continue
    if d.get("status") == "PAUSED":
        lines.append(f"- {d.get('project')}: PAUSED"); continue
    st = d.get("stages", {})
    done = [k for k, v in st.items() if isinstance(v, str) and v.startswith("DONE")]
    lines.append(f"- {d.get('project')} ({d.get('series_name_ko','')}): {len(done)} stage DONE · scripts={st.get('full_script')} · veo={st.get('veo_scenes')}")
    if d.get("blockers"): lines.append("  blockers: " + " | ".join(d["blockers"][:4]))
    if d.get("next"): lines.append("  next: " + " → ".join(d["next"][:4]))
ctx = "[hook session_start] Trạng thái xưởng phim:\n" + ("\n".join(lines) if lines else "(chưa có project)")
print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": ctx}}, ensure_ascii=False))
