---
description: Vận hành G-Labs — /glabs health | refs [ep] | scenes <ep> | videos <ep> | resume <jobs> <out>
argument-hint: health|refs|scenes|videos|resume …
---
`$ARGUMENTS`:
- `health` → `python3 tools/glabs_client.py health`; lỗi kết nối → báo user mở app G-Labs (tab Webhook, license MAX), KHÔNG retry vô hạn.
- `refs [ep]` → phóng glabs-operator (Agent, sonnet) chạy batch `05_references/*/ref_jobs.json` (+ `extra/ref_jobs_epN_extra.json`) `--parallel 4` → `05_references/<dir>/<id>_1.png`; QC ảnh §G (template 04); cập nhật manifest.
- `scenes <ep>` → từ `04_veo/scenes_epN.json` tạo jobs image (đính ref theo `refs[]`), batch lô 40, QC §G, regenerate ≤3, copy đạt QC → `output/epN/canh/`.
- `videos <ep>` → jobs video mode start_image từ ảnh đạt QC, `chain_from` theo scene JSON, 1080p, QC §H.
- `resume …` → `python3 tools/glabs_client.py resume --jobs … --out …`.
Không bao giờ in nội dung file key trong `config/` (hook secret_guard chặn).
