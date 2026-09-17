---
description: QC soi lỗi + chấm benchmark cho tập N — /qc <N> [script|veo]
argument-hint: <ep> [script|veo]
---
Chạy quy trình "sau MỖI deliverable" (CLAUDE.md) cho tập `$ARGUMENTS`: phóng qc-reviewer (Agent, opus, background) với `logs/QC_BRIEF.md`; đầu ra `logs/qc_epN_<loại>.md` + cột benchmark + lessons. Khi về: coordinator chốt điểm ★ vào `logs/decisions.md` (routine → tự quyết; đổi thị trường/câu chuyện/format → hỏi user), giao agent gốc sửa (SendMessage), vá template/agent/brief nếu có bài học quy trình, commit + push.
