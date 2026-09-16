# -*- coding: utf-8 -*-
"""Sinh 02_script/sublocks_ep2.md + 05_references/extra/ref_jobs_ep2_extra.json từ build.py SUBLOC/EXTRAS + scenes_ep2.json."""
import json, collections, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build as B

R = json.load(open(B.OUT_DIR + "/scenes_ep2.json", encoding="utf-8"))
use = collections.defaultdict(list)
for r in R:
    if r["subloc"] and r["subloc"] != "NONE": use[r["subloc"]].append(r["id"][3:])
refcnt = collections.Counter(x for r in R for x in r["refs"])

def rng(ids):
    ids = [int(i) for i in ids]; out = []; s = p = ids[0]
    for i in ids[1:]:
        if i == p + 1: p = i; continue
        out.append(f"{s:03d}" if s == p else f"{s:03d}–{p:03d}"); s = p = i
    out.append(f"{s:03d}" if s == p else f"{s:03d}–{p:03d}")
    return ", ".join(out)

EP1_REUSE = {"LOC_002", "LOC_002_hall", "LOC_003", "LOC_003_k2", "LOC_003_tent", "LOC_003_tent_ext", "LOC_003_medic", "LOC_003_hearth", "LOC_003_ford_northbank", "LOC_003_mouth", "LOC_004", "LOC_004_pavilion_int"}
BIBLE = {"LOC_002", "LOC_002_hall", "LOC_003", "LOC_003_tent", "LOC_004", "LOC_004_pavilion_int"}
DAY_NOTE = {}
L = ["# 살수 612 — SUB-LOCK ĐỊA ĐIỂM 2화 (veo-prompt-engineer · 2026-09-16 · CHỜ DUYỆT — cùng cơ chế sublocks_ep1.md)",
     "> Mỗi sub-lock = 1 đoạn VISUAL_LOCK_EN cố định cho một khu vực/buổi của LOC gốc; đã dán NGUYÊN VĂN vào mọi SC tương ứng trong `04_veo/scene_list_ep2.md`. `(bible)` = nguyên văn REF_PROMPT_EN_DETAIL/INTERIOR hoặc VISUAL_LOCK của location_bible; `(ep1)` = tái dùng sub-lock 1화 (sublocks_ep1.md) đúng id; `(mới)` = tạo cho 2화 → world-designer nhập vào location_bible dưới `REF_PROMPT_EN_<subarea>` của LOC gốc (đặc biệt LOC_002: **mặt bị công nam + đông-nam**, 치 đông-nam cải tạo, cổng đông đục 반 미터, lỗ hổng 80 m — decisions 'sau QC 2화 → v2' P-50). Nguồn máy: `logs/scratch/veo-ep2/build.py` SUBLOC.",
     "> Quy tắc dùng: cảnh wide/aerial → lock gốc LOC_xxx; cảnh medium/cận/nội thất → sub-lock của khu vực; luôn thêm câu Light theo bảng ngày/đêm + câu **Season** (4월 bụi vàng cỏ chớm xanh → 5월 → 6월 cỏ xanh nhạt, đất giẫm nát bụi, khô — chưa mưa); kết bằng style tag §D. Mùa/wear tự động theo ngày D trong build.py (APR ≤D33 · MAY D45–46 · JUN ≥D47; wear A/B/C).",
     "", "| # | id sub-lock | LOC gốc | Ref đính (`reference_images`) | Nguồn | SC 2화 | VISUAL_LOCK_EN (nguyên văn) |", "|---|---|---|---|---|---|---|"]
i = 0
for key, (loc, ref, txt) in B.SUBLOC.items():
    if key == "NONE" or key not in use: continue
    i += 1
    src = "bible" if key in BIBLE else ("ep1" if key in EP1_REUSE else "mới")
    L.append(f"| {i} | `{key}` | {loc} | `{ref}`" + (" **(ref mới)**" if ref in B.NEW_REFS else "") + f" | {src} | {len(use[key])} SC: {rng(use[key])} | {txt} |")
L += ["", "## Ref mới cần tạo (job: `05_references/extra/ref_jobs_ep2_extra.json`)", "| ref id | thư mục | dùng bởi sub-lock / extra | số SC đính | priority |", "|---|---|---|---|---|"]
for rid, d in B.NEW_REFS.items():
    subs = ", ".join(k for k, v in B.SUBLOC.items() if v[1] == rid and k in use)
    if rid == "VEH_201_mud_ep2": subs = "VEH_201 (veh_ref) từ SC_099"
    if rid == "EXTRA_sui_siege_general_ref": subs = "EXTRAS SUI_SIEGE_GENERAL"
    n = refcnt.get(rid, 0); pr = 1 if n >= 15 else (2 if n >= 5 else 3)
    L.append(f"| `{rid}` | {d} | {subs} | {n} | P{pr} |")
L += ["", "## Ghi chú",
      "- `LOC_002_drawing` / `LOC_002_k2_interior`: không đính ref địa điểm (bản vẽ binh thư trên lụa; nội thất tháp pháo K2) — chỉ style tag + mô tả.",
      "- `LOC_002_southwall_fog` dùng ref `LOC_002_detail` (bible) vì sương che hết hậu cảnh; từ SC_011 (sương tan) → `LOC_002_southwall` (ref mới có hàng tháp).",
      "- `LOC_002_bastion_se` (P4–P5, chưa cải tạo) dùng ref `LOC_002_detail`; `LOC_002_bastion_se_k2` / `_ramp` / `_ramp_work` (P9–P10) dùng ref mới `LOC_002_bastion_se_ep2` (khe đục vuông + dốc đất). QC: 2 trạng thái 치 KHÔNG được lẫn.",
      "- `LOC_003_k2_day` dùng cho cả SC đêm trăng P12 (SC_272–274) — vị trí bãi K2 lưới kéo lên; Light = `night_moon_jun`.",
      "- `LOC_003_valley_ep2` (4월) vs `LOC_003_valley_burned_ep2` (sau hỏa công): ranh giới = SC_146/151. `LOC_003_line_jun` (P11–P12) có xác 천둥 4 + 1 phuy lẻ.",
      "- VEH_201 tháp: ref `VEH_201_ref` (da ướt) SC_003–097 → `VEH_201_mud_ep2` (phủ đất) SC_099–247. VEH_202 xe húc: `RAM_MUD` text từ SC_074 (không ref riêng — 12 SC, ưu tiên thấp; nếu QC thấy AI vẽ da đen → tạo `VEH_202_mud_ep2`).",
      "- 탁발흠 hỏa công (SC_140–150): đi bộ, KHÔNG dán lock VEH_206 (kỵ); chỉ đính `VEH_206_ref` qua EXTRA_REF để giữ trang phục Tiên Ti.",
      "- Aerial 6월 (SC_174, 194, 199, 247, 267, 281–282) dùng lock gốc LOC_002 'yellow steppe… amber low sun through yellow dust' + câu Season JUN (cỏ xanh nhạt, đất giẫm nát bụi) — QC ảnh: chấp nhận cỏ xanh nhạt ngoài vùng giẫm nát; nếu lệch → world-designer thêm VISUAL_LOCK_EN_JUN cho LOC_002 (điểm cần quyết).",
      ]
open(B.PROJ + "/02_script/sublocks_ep2.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("sublocks_ep2.md", i, "sub-lock")

# ---------------------------------------------------------------- ref_jobs_ep2_extra.json
STYLE = B.STYLE
LOCS = {
    "LOC_002_southwall_ep2": ("LOC_002_southwall", "Wide establishing reference shot, 16:9, from on top of the wall looking along the parapet and out over the plain. "),
    "LOC_002_south_plain_ep2": ("LOC_002_south_plain", "Wide establishing reference shot, 16:9, from the Sui side looking toward the fortress. "),
    "LOC_002_bastion_se_ep2": ("LOC_002_bastion_se_k2", "Wide establishing reference shot, 16:9, three-quarter view from inside the fortress showing the earth ramp rising to the bastion and the square embrasure in the parapet. "),
    "LOC_002_eastgate_chisel_ep2": ("LOC_002_eastgate_chisel", "Establishing reference shot, 16:9, from inside the fortress looking through the arch. "),
    "LOC_002_infirmary_ep2": ("LOC_002_infirmary", "Interior establishing reference shot, 16:9. "),
    "LOC_002_tunnel_ep2": ("LOC_002_tunnel", "Interior establishing reference shot, 16:9, low camera looking down the tunnel. "),
    "LOC_002_breach_ep2": ("LOC_002_breach", "Wide establishing reference shot, 16:9, from outside the wall at the filled moat. "),
    "LOC_003_valley_ep2": ("LOC_003_valley_apr", "Wide establishing reference shot, 16:9, from the valley mouth by day. "),
    "LOC_003_valley_burned_ep2": ("LOC_003_wreck_day", "Wide establishing reference shot, 16:9, from the valley mouth by day. "),
    "LOC_004_platform_ep2": ("LOC_004_platform", "Wide establishing reference shot, 16:9, low angle from the plain at dawn. "),
}
jobs = []
for rid, (sub, lead) in LOCS.items():
    txt = B.SUBLOC[sub][2]
    prompt = lead + txt + ", no people in frame, no modern structures other than the listed vehicles, no text, " + STYLE
    jobs.append({"id": rid, "type": "image", "priority": 1 if refcnt[rid] >= 15 else (2 if refcnt[rid] >= 5 else 3), "sc_count": refcnt[rid],
                 "out_dir": "05_references/locations", "used_by_sublock": sub,
                 "body": {"prompt": prompt, "model": "nano_banana_pro", "aspect_ratio": "16:9"}})
# VEH_201_mud_ep2 — derived vehicle (vehicle_bible REF_PROMPT_EN + state)
veh_prompt = ("Product-style reference photo of a Sui dynasty eight-wheeled siege tower of 612 AD, three-quarter front view, tall four-story raw timber frame narrowing upward with an internal ladder, "
              "the front, sides and top completely covered in straw mats soaked in mud under a thick layer of wet earth so the tower looks earth-brown and lumpy instead of black hide, mud cracking dry in places, "
              "a hinged drop-bridge at the top also caked with mud, arrow slits on the upper floors, eight solid wooden wheels about one and a half meters tall, towing ropes and pushing beams at the base, a red Sui banner on top, "
              "pure white background, even studio lighting, " + STYLE)
jobs.append({"id": "VEH_201_mud_ep2", "type": "image", "priority": 1, "sc_count": refcnt["VEH_201_mud_ep2"], "out_dir": "05_references/vehicles",
             "used_by_vehicle_state": "VEH_201 TOWER_MUD (SC_099+)", "body": {"prompt": veh_prompt, "model": "nano_banana_pro", "aspect_ratio": "16:9"}})
gen = B.EXTRAS["SUI_SIEGE_GENERAL"].replace(", mounted on a dark bay horse", "")
char_prompt = ("Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. "
               + gen + ". Helmet on, sword sheathed at the hip, cloak thrown back over the shoulders, whip held down at the side, in the full-body view. Must look clearly different from any white-bearded or grey-bearded general: beard short, black, square-trimmed, around 45 years old, lean. "
               "Even studio lighting, no cast shadows, no horse, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look")
jobs.append({"id": "EXTRA_sui_siege_general_ref", "type": "image", "priority": 2, "sc_count": refcnt["EXTRA_sui_siege_general_ref"], "out_dir": "05_references/characters",
             "used_by_extra": "SUI_SIEGE_GENERAL", "body": {"prompt": char_prompt, "model": "nano_banana_pro", "aspect_ratio": "3:4"}})
jobs.sort(key=lambda j: (j["priority"], -j["sc_count"]))
json.dump(jobs, open(B.PROJ + "/05_references/extra/ref_jobs_ep2_extra.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ref_jobs_ep2_extra.json", len(jobs), [(j["id"], j["priority"], j["sc_count"]) for j in jobs])
