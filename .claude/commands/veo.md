---
description: Chuyển kịch bản tập N thành scene list + prompt ảnh/video + scenes_epN.json — /veo <N>
argument-hint: <ep>
---
Phóng veo-prompt-engineer (Agent, opus, background) cho tập `$ARGUMENTS` theo `04_veo/VEO_BRIEF.md` (lock nguyên văn từ continuity_master, sublocks, derived đúng tập, chain_from, CUT_HALF, overlay). Khi về: `python3 tools/sync_narration.py projects/<P> N`, gộp ref mới vào `05_references/extra/`, ghi decisions, commit + push.
