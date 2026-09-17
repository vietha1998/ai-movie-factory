---
description: Viết/sửa kịch bản tập N — /script <N> [dense|trim|fix <qc-file>]
argument-hint: <ep> [mode]
---
Kịch bản tập `$ARGUMENTS` của project hiện tại (CLAUDE.md "Project hiện tại"):
- Không mode → phóng agent script-writer (Agent tool, opus, background) với `02_script/SCRIPT_BRIEF.md` + `outline_epN.md` + tập trước; đầu ra `02_script/full_script_epN.md` + copy `output/epN/kich_ban/full_script.md`.
- `dense` → pass narration-dense (≥3.500 어절, không đổi SC). `trim` → pass TTS budget (`tools/tts_budget.py` = 0 vượt). `fix <qc-file>` → áp dụng BLOCK/FIX/NOTE≤1 dòng theo `logs/decisions.md`.
Sau khi agent xong: `python3 tools/tts_budget.py <file>`, `python3 tools/sync_narration.py projects/<P> N` nếu đã có scenes_epN.json, cập nhật `project_state.json`, commit + push.
