# OUTPUT — Thư mục giao hàng theo tập

SERIES ĐANG SẢN XUẤT: **살수 612 (SALSU 612)** — thị trường Hàn Quốc, khán giả 50+, mỗi tập ~40 phút, tiếng Hàn.
Project pipeline đầy đủ: `projects/SALSU_612/` · (LẠC HỒNG 1288 tạm dừng, giữ cho kênh Việt.)

Mỗi tập:
```
output/epN/
  tieu_de/      → title.md (제목 KO + gloss VI + EN, thumbnail text, 설명/해시태그)
  kich_ban/     → full_script.md (대본 KO — nội dung + tóm tắt VI mỗi phần), scene_list.md (bảng cảnh 8s)
  canh/         → SC_001.png / SC_001.mp4 ... (ảnh + video từng cảnh đã QC)
  final_video/  → epN_final.mp4 + thumbnail.png
```
Trạng thái: `projects/SALSU_612/project_state.json`
