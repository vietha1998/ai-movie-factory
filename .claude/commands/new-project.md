---
description: Tạo project mới theo mục E master prompt — /new-project <TÊN> <concept>
argument-hint: <PROJECT_NAME> <ý tưởng hoặc title>
---
Tạo project `$ARGUMENTS` theo CLAUDE.md + MASTER_PROMPT.md mục E/F:
1. Checklist NEW PROJECT: thị trường? ngôn ngữ đầu ra? khán giả? độ dài/tập? — chưa rõ trong CLAUDE.md/argument thì HỎI trước khi tạo (bài học L-01).
2. Tạo `projects/<NAME>/{00_input…12_final,logs}` + `project_state.json`, `production_manifest.json`, `continuity_master.json` (mẫu: projects/SALSU_612) + `output/epN/`.
3. Xác định INPUT MODE (A competitor / B new idea). Mode A → template 01 BƯỚC 1–2 (story DNA + new concept). Mode B → template 02.
4. Viết `02_script/series_foundation.md` (mẫu SALSU_612 §1–§10) rồi DỪNG, báo cáo và chờ duyệt trước khi phóng agent.
