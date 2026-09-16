# -*- coding: utf-8 -*-
"""
VEO scene-list builder — SALSU_612 · 5화 「살수」 최종화 (v2.1 · 289 SC)
Đọc: full_script_ep5.md (t / type / narration / thoại / [SOUND] — nguyên văn) + continuity_master.json v3 (VISUAL_LOCK + sublocks + derived_states nguyên văn)
      + batch_XX.py (dữ liệu hình ảnh do veo-prompt-engineer biên).
Ghi: 04_veo/scene_list_ep5.md · 04_veo/scenes_ep5.json · 04_veo/ep5_asset_usage.md · output/ep5/kich_ban/scene_list.md
     · 02_script/sublocks_ep5.md · 05_references/extra/ref_jobs_ep5_extra.json
Sao chép từ logs/scratch/veo-ep1/build.py + veo-ep4/build.py (cùng schema/validator), sửa cho 5화.
Lưu ý 5화: SC_169 đứng TRƯỚC SC_165 trong dòng thời gian (giữ ID) → sắp xếp theo t_start; không mid-roll 5.
"""
import json, re, os, sys, glob, importlib.util, collections

ROOT = "/Users/admin/phim han quoc"
PROJ = ROOT + "/projects/SALSU_612"
SCRIPT = PROJ + "/02_script/full_script_ep5.md"
CM = json.load(open(PROJ + "/continuity_master.json", encoding="utf-8"))
OUT_DIR = PROJ + "/04_veo"
HERE = os.path.dirname(os.path.abspath(__file__))
EP = 5
N_SC = 289

STYLE = CM["style_tag"]
NEGATIVE = ("cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, "
            "modern buildings in historical scene, anachronistic clothing")

# ---------------------------------------------------------------- LOCKS (nguyên văn continuity_master.json v3)
LOCKS = {}
LOCKS.update(CM["character_locks"]); LOCKS.update(CM["vehicle_locks"]); LOCKS.update(CM["prop_locks"])
LOC_LOCK = {k.split("_")[0] + "_" + k.split("_")[1]: v for k, v in CM["location_locks"].items()}
CM_SUB = CM["sublocks"]          # sublocks v3 (LOC_007_* 5화 đã khóa)
CM_DER = CM["derived_states"]    # derived_states v3 (prompt_add nguyên văn)
LOCK_PENDING = {}                # v3 đã có VEH_207 / PROP_024 / PROP_025 → không còn lock tạm cho ID bible
# Lock biến thể đạo cụ theo prop_bible (nguyên văn VISUAL_LOCK_EN_OPEN / _ON_WRECK) — dùng qua prop_state={"PROP_024": "open"}
PROP_LOCK_ALT = {
    "PROP_024:open": "large plain red silk signal banner unfurled and streaming from a four-meter bamboo pole in rain, no emblem, no border, wet silk clinging and snapping",
    "PROP_023:wreck": "a small scorched olive-drab steel nameplate with a scratched white numeral 3 lying on the mud-caked turret edge of a burned tank beside a faded white numeral 1",
    "PROP_023:pocket": "small rectangular olive-drab painted steel vehicle nameplate with a scratched white numeral 3, two bolt holes, scorched edge, a loop of paracord through one hole",
}
# Đạo cụ KHÔNG có ID bible phù hợp (script tag PROP_001 = "bản đồ lụa 을지문덕" ≠ PROP_001 bản đồ giấy ROK; PROP_012 "cờ hiệu nhỏ") → lock tạm, LOCK_PENDING
EXTRA_PROPS = {
    "SILK_MAP": "a Goguryeo silk map painted in black ink brush strokes: a curving river, a line of small stake marks across a ford, a long mid-river sandbar, the north bank hatched thick for reed beds, scale-like strokes for hills on both banks, one small red cinnabar dot at a gap on the north bank, no readable writing",
    "SMALL_CROW_PENNANT": "a small yellow silk hand pennant with a black three-legged crow on a short bamboo stick",
    "K5_PISTOL": "a black South Korean K5 semi-automatic pistol",
    "LACQUER_BOX": "a black lacquered wooden box the size of a small chest, lid tied with yellow silk cord, rain beading on the glossy lacquer",
    "OX_CART_GIANT": "a giant flat wooden cart with eight solid wooden wheels sunk in mud, drawn by rows of oxen under wooden yokes",
    "GOURD_BOTTLE": "a dried gourd water bottle with a hemp cord",
    "MORPHINE": "a small olive autoinjector",
    "WATER_BOWL": "a plain grey Goguryeo pottery bowl of water",
}

# ---------------------------------------------------------------- REF SHEET IDS (05_references/*/ref_jobs.json + extra ep1) + refs CẦN TẠO 5화
REF_DIR = {}
for d in ("characters", "locations", "vehicles", "props"):
    for j in json.load(open(f"{PROJ}/05_references/{d}/ref_jobs.json", encoding="utf-8")):
        REF_DIR[j["id"]] = d
for j in json.load(open(f"{PROJ}/05_references/extra/ref_jobs_ep1_extra.json", encoding="utf-8")):
    REF_DIR[j["id"]] = j["out_dir"].split("/")[-1]  # đã DUYỆT (decisions) — coi như có job
EP4_EXTRA = set()
p4 = f"{PROJ}/05_references/extra/ref_jobs_ep4_extra.json"
if os.path.exists(p4):
    for j in json.load(open(p4, encoding="utf-8")):
        EP4_EXTRA.add(j["id"])
NEW_REFS = {  # chưa có job → 05_references/extra/ref_jobs_ep5_extra.json (xem ep5_asset_usage.md §5)
    "LOC_007_k2_reeds_ep5": "locations", "LOC_007_throat_ep5": "locations", "LOC_007_north_line_ep5": "locations",
    "LOC_007_south_knoll_ep5": "locations", "LOC_007_north_hill_ep5": "locations", "LOC_007_small_bar_ep5": "locations",
    "LOC_007_mid_bar_ep5": "locations", "LOC_007_upstream_bar_ep5": "locations", "LOC_007_aid_ep5": "locations",
    "LOC_007_aftermath_ep5": "locations", "LOC_004_yard_rain_ep5": "locations", "LOC_001_road_west_ep5": "locations",
    "VEH_001_interior_ref": "vehicles",
    "PROP_018_ref": "props", "PROP_023_ref": "props", "EXTRA_silk_map_ref": "props",
    "EXTRA_gog_deputy_ref": "characters", "EXTRA_gog_young_rider_ref": "characters", "EXTRA_k2_driver_ref": "characters",
}
REF_DIR.update(NEW_REFS)

def ref_path(rid):
    return f"projects/SALSU_612/05_references/{REF_DIR[rid]}/{rid}_1.png"

# ---------------------------------------------------------------- DERIVED STATES
# (char, ref đính, câu trạng thái). ✔bible = nguyên văn continuity_master.derived_states[*].prompt_add (ref riêng đã có job);
# ep5* = trạng thái trong tập do veo-prompt-engineer đặt theo bảng "Trạng thái theo tập" 5화 + [ACTION-VI] (đính ref gần nhất; đề xuất character-designer nhập bible).
def B(k):  # bible verbatim
    return CM_DER[k]["prompt_add"]
DERIVED = {
    # ---- ✔ bible verbatim (ref riêng)
    "CHAR_001_reeds_ep4": ("CHAR_001", "CHAR_001_reeds_ep4", B("CHAR_001_reeds_ep4")),
    "CHAR_001_muddy_bloody_ep5": ("CHAR_001", "CHAR_001_muddy_bloody_ep5", B("CHAR_001_muddy_bloody_ep5")),
    "CHAR_001_river_oil_ep5": ("CHAR_001", "CHAR_001_river_oil_ep5", B("CHAR_001_river_oil_ep5")),
    "CHAR_001_final_ep5": ("CHAR_001", "CHAR_001_final_ep5", B("CHAR_001_final_ep5")),
    "CHAR_002_muddy_bloody_ep5": ("CHAR_002", "CHAR_002_muddy_bloody_ep5", B("CHAR_002_muddy_bloody_ep5")),
    "CHAR_003_muddy_ep5": ("CHAR_003", "CHAR_003_muddy_ep5", B("CHAR_003_muddy_ep5")),
    "CHAR_003_crutch_ep5": ("CHAR_003", "CHAR_003_crutch_ep5", B("CHAR_003_crutch_ep5")),
    "CHAR_004_muddy_bloody_ep5": ("CHAR_004", "CHAR_004_muddy_bloody_ep5", B("CHAR_004_muddy_bloody_ep5")),
    "CHAR_005_goguryeo_helmet_ep5": ("CHAR_005", "CHAR_005_goguryeo_helmet_ep5", B("CHAR_005_goguryeo_helmet_ep5")),
    "CHAR_006_horseback_ep5": ("CHAR_006", "CHAR_006_horseback_ep5", B("CHAR_006_horseback_ep5")),
    "CHAR_101_salsu_rain_ep5": ("CHAR_101", "CHAR_101_salsu_rain_ep5", B("CHAR_101_salsu_rain_ep5")),
    "CHAR_101_false_surrender_ep3": ("CHAR_101", "CHAR_101_false_surrender_ep3", B("CHAR_101_false_surrender_ep3")),
    "CHAR_102_hall_night_ep4": ("CHAR_102", "CHAR_102_hall_night_ep4", B("CHAR_102_hall_night_ep4")),
    "CHAR_105_radio_ep3": ("CHAR_105", "CHAR_105_radio_ep3", B("CHAR_105_radio_ep3")),
    "CHAR_105_wounded_ep5": ("CHAR_105", "CHAR_105_wounded_ep5", B("CHAR_105_wounded_ep5")),
    "CHAR_105_bandaged_ep5": ("CHAR_105", "CHAR_105_bandaged_ep5", B("CHAR_105_bandaged_ep5")),
    "CHAR_107_scarf_ep2": ("CHAR_107", "CHAR_107_scarf_ep2", B("CHAR_107_scarf_ep2")),
    "CHAR_201_defeat_news_ep5": ("CHAR_201", "CHAR_201_defeat_news_ep5", B("CHAR_201_defeat_news_ep5")),
    "CHAR_201_rain_k21_ep5": ("CHAR_201", "CHAR_201_rain_k21_ep5", B("CHAR_201_rain_k21_ep5")),
    "CHAR_202_rain_ep5": ("CHAR_202", "CHAR_202_rain_ep5", B("CHAR_202_rain_ep5")),
    "CHAR_202_defeat_ep5": ("CHAR_202", "CHAR_202_defeat_ep5", B("CHAR_202_defeat_ep5")),
    "CHAR_203_retreat_ep5": ("CHAR_203", "CHAR_203_retreat_ep5", B("CHAR_203_retreat_ep5")),
    "CHAR_203_chained_ep5": ("CHAR_203", "CHAR_203_chained_ep5", B("CHAR_203_chained_ep5")),
    "CHAR_205_final_ep5": ("CHAR_205", "CHAR_205_final_ep5", B("CHAR_205_final_ep5")),
    # ---- bible text-only states (không ref riêng → đính ref gần nhất)
    "CHAR_107_scarf_burnt_ep3": ("CHAR_107", "CHAR_107_scarf_ep2", B("CHAR_107_scarf_burnt_ep3")),
    "CHAR_103_helmet_off": ("CHAR_103", "CHAR_103_ref", B("CHAR_103_helmet_off")),
    # ---- ep5 in-episode states (veo-prompt-engineer; theo bible 'Trạng thái theo tập' 5화 + [ACTION-VI])
    "CHAR_001_river_oil_rifle_ep5": ("CHAR_001", "CHAR_001_river_oil_ep5",
        "Helmet off, hair plastered flat, soaked to the chest, uniform and face streaked with the black sheen of fuel oil, water running from the sleeves, exhausted fierce eyes, a black assault rifle in his hands."),
    "CHAR_001_helmet_hand_ep5": ("CHAR_001", "CHAR_001_final_ep5",
        "Helmet held in one hand, hair dry and uncombed, mud dried grey on the uniform, a strip of cloth bandage wrapped around the right hand, empty thigh holster, quiet still face lit by warm sunlight."),
    "CHAR_002_reeds_helmet_ep5": ("CHAR_002", "CHAR_002_muddy_bloody_ep5",
        "Helmet on with chinstrap hanging loose and reed stalks in the band, tactical goggles pushed up on the helmet, mud smeared on the face, a field bandage wrapped around the left upper arm, mud to the thighs, rain-soaked uniform, K3 light machine gun with cloth tape on the stock."),
    "CHAR_002_final_ep5": ("CHAR_002", "CHAR_002_muddy_bloody_ep5",
        "Helmet on with chinstrap hanging loose, goggles missing, blood-soaked field bandage wrapped around the left upper arm, mud drying grey on the uniform, jaw clenched, exhausted eyes, no weapon in hand, warm sunlight."),
    "CHAR_003_capless_ep5": ("CHAR_003", "CHAR_003_muddy_ep5",
        "No cap: wet salt-and-pepper hair plastered to the forehead, mud caked to the hips, engine oil and blood on both forearms, week-old gray stubble, exhausted but calm face, the metal vehicle nameplate still tied to the backpack strap."),
    "CHAR_003_driver_ep5": ("CHAR_003", "CHAR_003_muddy_ep5",
        "No cap and no backpack: wet salt-and-pepper hair plastered to the forehead, mud caked to the hips, engine oil and blood on both forearms, week-old gray stubble, calm face, a small olive-drab steel nameplate showing in the chest pocket of the body armor."),
    "CHAR_003_wounded_ep5": ("CHAR_003", "CHAR_003_crutch_ep5",
        "No cap, wet salt-and-pepper hair, soaked to the chest, an arrow shaft standing from the left thigh with the trouser leg dark with blood, mud and oil on both forearms, week-old gray stubble, face white with pain but calm, teeth clenched."),
    "CHAR_005_helmet_hand_ep5": ("CHAR_005", "CHAR_005_goguryeo_helmet_ep5",
        "Mounted on a Goguryeo warhorse, a plain Goguryeo iron plate helmet without plume held in his hands, hacked short hair, borrowed body armor over a torn camo uniform with no flag patch on the right shoulder, a fading bruise on the left eye, right foot splinted with reeds and bandage, mud drying on the trousers, warm sunlight."),
    "CHAR_006_afoot_ep5": ("CHAR_006", "CHAR_006_horseback_ep5",
        "On foot holding the reins of a Goguryeo warhorse with leather saddle and iron stirrups, boonie hat drying, scrim scarf, K2C1 rifle slung across the chest, mud drying grey on the boots and trousers, warm sunlight."),
    "CHAR_103_court_ep5": ("CHAR_103", "CHAR_103_ref",
        "Helmet removed, black topknot neat, armor cleaned and dry, no shield and no spear, standing at the foot of the dais, face lit warm from one side by oil lamps."),
    "CHAR_105_reeds_ep5": ("CHAR_105", "CHAR_105_radio_ep3",
        "A dead modern olive-green handheld radio with its light off clipped to the chest armor lacing, rain-soaked armor and green jacket, the white feather on the helmet broken and bent, no cloak, mud to the thighs, a black horn trumpet on a leather cord at the hip, quick alert eyes."),
    "CHAR_105_bow_ep5": ("CHAR_105", "CHAR_105_radio_ep3",
        "A dead modern olive-green handheld radio clipped to the chest armor lacing, a composite bow slung across the back, a black horn trumpet on a leather cord at the hip, rain-soaked armor and green jacket, the white feather on the helmet broken and bent, no cloak, mud to the thighs, quick alert eyes."),
    "CHAR_105_charge_ep5": ("CHAR_105", "CHAR_105_radio_ep3",
        "Ring-pommel sword drawn in the right hand, a composite bow slung across the back, a black horn trumpet at the hip, a dead handheld radio clipped to the chest armor, rain-soaked armor and green jacket, the white feather on the helmet broken, no cloak, wading in shallow brown water."),
    "CHAR_106_salsu_ep5": ("CHAR_106", "CHAR_106_ref",
        "Hemp clothes and scorched leather forge apron soaked with rain, mud to the knees, wet wispy white beard, a hand-forged iron pry bar with a hooked end in his hands, no hammer at the belt."),
    "CHAR_106_final_ep5": ("CHAR_106", "CHAR_106_ref",
        "Hemp clothes and leather forge apron drying stiff with mud, wet wispy white beard, a hand-forged iron pry bar with a hooked end planted in the sand beside him, warm sunlight."),
    "CHAR_107_final_ep5": ("CHAR_107", "CHAR_107_scarf_ep2",
        "The olive military scarf with one corner scorched black and frayed, braids damp and stuck with dried blood, dried blood on both hands, the jacket sleeves tied up with strips of cloth, mud on the hem of the skirt, warm sunlight."),
    "CHAR_202_river_ep5": ("CHAR_202", "CHAR_202_defeat_ep5",
        "Thrown into the river: soaked to the skin, helmet lost, white hair loosening from the topknot, beard streaming with muddy water, one breast mirror dented, red cloak torn to half its length, clutching a broken banner pole, chest-deep in brown water, stunned face."),
    "CHAR_203_rain_mounted_ep5": ("CHAR_203", "CHAR_203_retreat_ep5",
        "Mounted on a tall grey Han war horse with a high wooden saddle and a plain leather breast strap, helmet on, the fur collar of the cloak wet and matted, cloak soaked and heavy with rain, face gray with exhaustion, mud on the boots."),
    "CHAR_205_waiting_ep5": ("CHAR_205", "CHAR_205_final_ep5",
        "Mounted on a short stocky steppe horse with white cloth stuffed in its ears, fox-fur cap on and soaked, braid wet, a cracked night-vision device hanging from a cord around the neck, composite bow slung across the back, saber sheathed, right forearm wrapped in a black cloth bandage, rain on the face, calm assessing eyes."),
    "CHAR_205_capless_ep5": ("CHAR_205", "CHAR_205_final_ep5",
        "Fox-fur cap lost, braid loose and wet and swinging, a cracked night-vision device hanging from a cord around the neck, composite bow slung across the back, ring-pommel saber drawn in the right hand with blood on the blade, right forearm wrapped in a black cloth bandage, mud to the thighs, blood on the tunic, rain, fierce calm face."),
    "CHAR_205_bow_ep5": ("CHAR_205", "CHAR_205_final_ep5",
        "Fox-fur cap lost, braid loose and wet, a cracked night-vision device hanging from a cord around the neck, composite recurve bow in the left hand with an arrow nocked, the bandaged right forearm drawing the string, mud to the thighs, blood on the tunic, standing on scorched steel in white smoke."),
}

# ---------------------------------------------------------------- VEHICLE STATES 5화 (câu bổ sung sau lock — không đổi lock; K2 damage 4 pha theo vehicle_bible)
VEH_STATE = {
    "k2_reeds": "Caked in layers of cracked dry grey mud, wet reed bundles stuck thick over the turret roof and stowage baskets, the gun barrel depressed low and wrapped in reeds, only a corner of the small Korean flag showing under the mud, one headlight smashed, no lights.",
    "k2_after_fire": "Caked in cracked grey mud with the reeds around it burned flat, mud on the gun barrel cracked and fallen in slabs, thin white smoke drifting from the muzzle, the black hull standing exposed like a rock in the flattened reed bed.",
    "k2_arrows": "Caked in cracked grey mud, reeds around it burned flat, dozens of arrows bristling from the turret roof and stowage baskets like quills, the driver's hatch standing open with a smear of blood on its rim, the gun barrel depressed low.",
    "k2_running": "Slabs of dry mud cracking and sliding off the hull, reeds falling from the roof, broken arrow shafts still stuck in the stowage baskets, grey exhaust smoke bursting from the rear grille, tracks throwing wet sand.",
    "k2_stalled": "Stalled broadside in chest-deep brown water, tilted slightly with its tracks sunk in sand, engine silent, arrows bristling over the turret roof, mud cracking off the hull, a rainbow oil slick spreading downstream from the rear of the hull.",
    "k2_burning": "Stalled broadside in chest-deep brown water and burning from the inside: thick white smoke and white-yellow fire jetting from the open commander's hatch, the turret edges glowing dull red, a trickle of white-hot molten metal running down the side skirt, a ring of burning oil on the water around the hull, arrows bristling on the roof.",
    "k2_sunk": "Scorched black, the turret burned out and smoking, the hull sunk tilted into the sand with brown water pouring over the side skirts and across the hull roof, broken arrows on the roof, a broken red Sui banner caught in the track, the ring of oil fire dying.",
    "k2_wreck": "Destroyed: hull tilted ten degrees and sunk to half its height in cracked dry grey-brown river mud, turret scorched black with heat-discolored blue-brown steel around the open commander's hatch, gun depressed low, one side skirt panel missing, broken arrow shafts stuck on the roof and in the stowage basket, one headlight smashed, faded camouflage showing through mud and soot, the small white numeral 1 and the small Korean flag half hidden under dried mud.",
    "k21_captured": "Under a lashed-down cover of mud-caked oiled cloth on a giant flat wooden ox cart with its wheels sunk in mud, one corner of the side skirt and one road wheel showing, a small white arrow mark painted on the rear ramp, a wet red Sui banner planted on the cover, no oxen yoked.",
    "k21_road": "Under a lashed-down cover of oiled cloth on a giant flat wooden cart drawn by forty oxen, only the boxy shape showing, a small wet red Sui banner on the cover.",
    "v207_black": "The general's horse is tall and black with a red silk caparison with a gold border and red tassels under the jaw, high wooden saddle, gilded bronze harness fittings, rain streaming from its trimmed mane.",
    "v207_grey": "The general's horse is tall and grey with a plain leather breast strap and no silk caparison, its wet mane matted, mud to the knees.",
    "v207_chestnut": "The general's horse is a tall chestnut with a red silk caparison and gold border, high wooden saddle, iron stirrups.",
    "v207_troop": "Cavalry horses with simple leather breast straps and no silk, riders in plain iron lamellar armor.",
    "v101_wet": "Iron lamellar barding streaming with rain, mud splashed to the horses' bellies, red plumes heavy with water, a few arrows stuck in the barding.",
    "v101_sun": "Iron lamellar barding streaked with drying mud and river water glittering in sunlight, red plumes heavy, lances raised.",
    "v206_ears": "The steppe horses have white cloth stuffed in their ears and tied with leather cord over the brow, wet leather armor, mud to the belly.",
    "v206_water": "The steppe horses chest-deep in brown water with white cloth in their ears, riders wet to the waist, bows drawn from the saddle.",
}

# ---------------------------------------------------------------- EXTRAS (không ID trong bible) — lock tạm, dùng NGUYÊN VĂN mọi SC
EXTRAS = {
    "SUI_FEET": "the feet and legs of Sui foot soldiers stepping into the water, torn straw sandals, wet cloth leggings, rims of red rectangular wooden shields and spear butts dragging, no faces",
    "SUI_WADERS": "Sui foot soldiers wading chest-deep in brown water in mingguang armor with two polished round chest plates and pointed iron helmets, red rectangular wooden shields held over their heads against the rain, long spears upright, wet red and yellow banners drooping, gaunt hollow-cheeked faces mostly turned away",
    "SUI_WADER_FACE": "one gaunt Sui foot soldier near the camera, hollow cheeks and sunken eyes under a pointed iron helmet, wet grey-blue padded coat under lamellar armor, chest-deep in brown water",
    "SUI_INFANTRY": "Sui foot soldiers in mingguang armor with two polished round chest plates, pointed iron helmets, long spears, red rectangular wooden shields, soaked grey-blue padded coats, faces turned away or hidden under helmets",
    "SUI_INFANTRY_BACKS": "the backs of Sui foot soldiers in mingguang armor and pointed iron helmets, red rectangular shields on their backs, spears upright, soaked and mud-caked, no faces",
    "SUI_SHIELD_WALL": "a wall of Sui foot soldiers advancing shoulder to shoulder behind red rectangular wooden shields with long spears lowered, pointed iron helmets, faces hidden behind the shield rims",
    "SUI_ARCHERS": "Sui archers in soaked grey-blue padded coats and pointed iron helmets loosing volleys from behind a shield line, seen from behind",
    "SUI_ROUT": "Sui foot soldiers running in every direction, shields thrown down, spears dropped, helmets lost, mud to the waist, faces turned away",
    "SUI_STRAGGLERS": "Sui stragglers without shields or banners, barefoot, torn grey-blue padded coats, running through wet grass toward a river, faces turned away",
    "SUI_REAR_GENERAL": "a Sui rear-guard general in his forties, lean weathered face with a short black beard, mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel crest, red cloak soaked dark, straight sword raised, mounted on a tall chestnut Han war horse with a red silk caparison",
    "SUI_DEPUTY": "a Sui deputy officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, mouth open shouting, face streaming with rain, on foot",
    "SUI_STANDARD_BEARER": "a Sui standard bearer in iron lamellar armor and pointed iron helmet holding a tall red silk banner with a yellow border and black tassels on a black lacquered pole, face turned away",
    "SUI_CAVALRYMEN": "Sui cavalrymen in mingguang iron lamellar armor with polished round chest plates and pointed iron helmets with red tassels on tall Han war horses with high wooden saddles and plain leather breast straps, long spears, faces turned away",
    "SUI_EUNUCHS": "Sui court eunuchs in plain grey-blue silk robes and black gauze caps, clean-shaven, bowing low to the floor",
    "SUI_EUNUCH_UMBRELLA": "a Sui court eunuch in a grey-blue silk robe and black gauze cap hurrying with a large red silk umbrella held out too late",
    "SUI_EUNUCH_BOX": "a Sui court eunuch in a grey-blue silk robe and black gauze cap holding a black lacquered wooden box in both hands",
    "SUI_GUARDS_WET": "two Sui guards in soaked grey-blue padded coats and iron lamellar vests with pointed iron helmets standing with spears in the rain, faces hidden under helmet brims",
    "SUI_OX_DRIVER": "a Sui ox-cart driver in a soaked undyed hemp jacket and head cloth, weathered calloused hands, sitting on the cart bench",
    "SUI_SOLDIERS_SILHOUETTE": "silhouettes of Sui soldiers in pointed iron helmets crowding a doorway, spears and lamellar armor catching lantern light, no faces",
    "GOG_SPEARMEN": "Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, four-meter lances with iron heads held level, no shields, soaked with rain, faces mostly hidden under helmets",
    "GOG_SPEARMEN_SUN": "Goguryeo foot soldiers in mud-streaked iron lamellar armor over brown jackets, iron plate helmets with short plumes, four-meter lances raised, standing in warm sunlight",
    "GOG_CAVALRYMEN": "Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants",
    "GOG_CAV_OFFICER": "a Goguryeo cavalry officer in iron lamellar armor with a tall red plume on his iron helmet, on a horse in iron lamellar barding, lance raised, shouting",
    "GOG_ARCHER_OFFICER": "a Goguryeo archer officer in iron lamellar armor and iron helmet with a short plume raising his arm, mouth open shouting",
    "GOG_FIRE_ARCHERS": "a line of Goguryeo archers in iron lamellar armor and iron plate helmets drawing short composite reflex bows with oil-cloth-wrapped fire arrows, small braziers of glowing coals at their feet",
    "GOG_DRUMMERS": "Goguryeo drummers in brown jackets and iron helmets striking large faded red-lacquered war drums on X-shaped wooden stands with thick wooden beaters",
    "GOG_FLAG_BEARER": "a Goguryeo flag bearer in iron lamellar armor over a brown jacket and iron plate helmet, holding a long bamboo pole in both hands, face streaming with rain",
    "GOG_HORN_BLOWER": "a Goguryeo signalman in iron lamellar armor over a brown jacket and iron plate helmet, cheeks puffed, blowing a curved black water-buffalo horn trumpet with a bronze mouthpiece",
    "GOG_DEPUTY": "a Goguryeo deputy commander around 45, broad face with a short black beard and heavy brows, iron lamellar armor laced with red cord over a dark brown jacket, iron plate helmet with a short black plume, ring-pommel sword, soaked with rain",
    "GOG_YOUNG_RIDER": "a young Goguryeo cavalryman around 20, thin face, no beard, iron lamellar armor over a brown jacket, iron helmet with a red plume, on a chestnut horse in iron lamellar barding, soaked with rain",
    "GOG_GUARDS": "Goguryeo palace guards in iron lamellar armor holding long spears, faces shadowed under iron helmets",
    "GOG_FINGER": "the weathered hand of an old Goguryeo general, a single finger with a broken nail resting on the silk, an iron lamellar sleeve at the wrist",
    "ROK_SOLDIERS": "ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, covered helmets stuck with reed stalks, faces smeared with mud, week-old stubble, torn Korean flag patches on right shoulders, K2C1 rifles resting on bent reeds, faces turned away or hidden under helmet brims",
    "ROK_SOLDIER": "a ROK Army soldier in a soaked mud-smeared granite-pattern digital camo uniform, covered helmet stuck with reed stalks, face smeared with mud and turned away or hidden under the helmet brim, Korean flag patch on right shoulder",
    "ROK_SOLDIERS_2": "two ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, covered helmets stuck with reed stalks, faces smeared with mud and mostly hidden under helmet brims, Korean flag patches on right shoulders",
    "ROK_SOLDIERS_SUN": "ROK Army soldiers in mud-caked granite-pattern digital camo uniforms drying grey, helmets off or pushed back, faces streaked with dried mud, K2C1 rifles with bayonets fixed standing beside them, torn Korean flag patches on right shoulders, faces turned away or lowered",
    "ROK_MORTAR_CREW": "two ROK mortar crewmen in soaked mud-smeared granite-pattern digital camo uniforms and reed-stuck helmets, faces down under helmet brims",
    "ROK_K6_CREW": "two ROK gunners in soaked mud-smeared granite-pattern digital camo uniforms and reed-stuck helmets crouched behind a heavy machine gun on a tripod, faces hidden under helmet brims",
    "ROK_K3_GUNNER": "a ROK machine gunner in a soaked mud-smeared granite-pattern digital camo uniform and reed-stuck helmet lying behind a K3 light machine gun in a sandbagged hole, face hidden under the helmet brim",
    "ROK_PZF_GUNNERS": "three ROK soldiers kneeling at the edge of the reeds with shoulder-fired anti-tank launchers, faces hidden under reed-stuck helmets, spare launcher tubes leaning on sandbags",
    "ROK_WOUNDED": "a wounded ROK soldier in a soaked mud-smeared granite-pattern digital camo uniform lying on a reed mat, face turned away, a tourniquet on one thigh",
    "ROK_DRIVER": "the K2 driver, a ROK Army soldier around 28 in a granite-pattern digital camo uniform and crew helmet with boom microphone, square face smeared with mud, half risen out of the open driver's hatch",
    "ROK_GUNNER_TURRET": "the K2 gunner in a granite-pattern digital camo uniform and crew helmet with boom microphone, seen from behind inside the cramped turret lit by a cold blue screen glow",
    "ROK_HAND": "a mud-caked black-gloved hand of a ROK soldier",
    "XIANBEI_SCOUTS_2": "two Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, on short stocky steppe horses with white cloth in their ears, bows slung",
    "XIANBEI_RIDERS": "Xianbei riders in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, on short stocky steppe horses with white cloth stuffed in their ears, short curved sabers drawn, faces turned away",
    "XIANBEI_ARCHER": "a Xianbei horse archer in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, twisting in the saddle with a composite bow drawn",
    "XIANBEI_RIDER_ON_HULL": "a Xianbei rider on foot in soaked brown leather lamellar armor and fur-trimmed leather cap, short curved saber raised in both hands, standing on the steel roof of the tank",
    "XIANBEI_LEADERS_2": "two Xianbei sub-chiefs in brown leather lamellar armor with fur-trimmed leather caps on short steppe horses, listening",
    "VILLAGE_WOMEN_3": "three middle-aged Goguryeo village women in soaked undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, spreading reed mats",
    "VILLAGE_WOMAN": "a middle-aged Goguryeo village woman in a soaked undyed hemp jacket and pleated skirt, cloth head wrap, bare feet",
    "DEAD_HORSE": "a dead Sui war horse lying on its side in the wet sand with arrows in its flank",
}

# ---------------------------------------------------------------- SUB-LOCATION LOCKS (cố định — dùng nguyên văn mọi SC; xem 02_script/sublocks_ep5.md)
def CS(k):  # continuity_master sublock verbatim
    return CM_SUB[k]["lock"]
SUBLOC = {
    # key: (loc_id, ref_id or None, text)
    # ===== LOC_007_SALSU — continuity_master v3 (nguyên văn)
    "LOC_007": ("LOC_007", "LOC_007_wide", LOC_LOCK["LOC_007"]),
    "LOC_007_reeds": ("LOC_007", "LOC_007_detail", CS("LOC_007_reeds")),
    "LOC_007_throat": ("LOC_007", "LOC_007_throat_ep5", CS("LOC_007_throat")),
    "LOC_007_throat_k2": ("LOC_007", "LOC_007_throat_ep5", CS("LOC_007_throat_k2")),
    "LOC_007_small_bar": ("LOC_007", "LOC_007_small_bar_ep5", CS("LOC_007_small_bar")),
    "LOC_007_mid_bar": ("LOC_007", "LOC_007_mid_bar_ep5", CS("LOC_007_mid_bar")),
    "LOC_007_upstream_bar": ("LOC_007", "LOC_007_upstream_bar_ep5", CS("LOC_007_upstream_bar")),
    "LOC_007_north_flat": ("LOC_007", "LOC_007_north_hill_ep5", CS("LOC_007_north_flat")),
    "LOC_007_south_knoll": ("LOC_007", "LOC_007_south_knoll_ep5", CS("LOC_007_south_knoll")),
    "LOC_007_aftermath": ("LOC_007", "LOC_007_aftermath_ep5", CS("LOC_007_aftermath")),
    # ===== LOC_007_SALSU — sub-lock mới 5화 (veo-prompt-engineer)
    "LOC_007_dawn_aerial": ("LOC_007", "LOC_007_wide",
        "Aerial view at flat grey dawn of a wide shallow river eight hundred meters across, a four-hundred-meter ford marked by a line of leaning wooden stakes, a long tongue-shaped sandbar in mid-river, the north bank buried in dense grey-green reed beds hundreds of meters deep with a narrow gap between the reeds and a steep mud bank, the south bank rising into low green hills, light drizzle, thin river mist, heavy grey cloud"),
    "LOC_007_south_shore": ("LOC_007", "LOC_007_wide",
        "The south shore of the wide shallow river in monsoon rain: wet green grass and churned mud at the water's edge, a line of leaning wooden ford stakes running out into grey-brown water, low green hills behind, the far north bank a dark line of reed beds lost in rain and mist"),
    "LOC_007_south_field": ("LOC_007", "LOC_007_wide",
        "Wet green grassland on the south bank of the wide shallow river in monsoon rain: trampled grass churned to mud, low green hills rising behind, the grey river and its sandbars beyond, low cloud"),
    "LOC_007_ford": ("LOC_007", "LOC_007_wide",
        "Out on the wide shallow ford in monsoon rain: grey-brown water chest-deep on a man, rain pocking the surface, a line of leaning wooden stakes, a long low sandbar in mid-river, the reed beds of the north bank and the low green hills of the south bank both blurred by rain and mist"),
    "LOC_007_ford_surface": ("LOC_007", "LOC_007_detail",
        "The surface of the wide shallow river seen from water level in light drizzle at grey dawn: grey water pocked by raindrops, a leaning wooden ford stake, wet grey-brown sand at the water's edge, the far bank lost in mist"),
    "LOC_007_k2_reeds": ("LOC_007", "LOC_007_k2_reeds_ep5",
        "At the edge of the dense reed bed on the north bank three hundred meters from the throat of the ford, monsoon rain: a K2 tank caked in cracked grey mud and stuck with reed bundles standing among two-meter grey-green reeds, sandbagged fighting holes at the base of the stalks, a mortar pit and a tripod machine gun under reeds nearby, wet grey-brown sand, brown river water showing through the reeds, river mist"),
    "LOC_007_k2_reeds_flat": ("LOC_007", "LOC_007_k2_reeds_ep5",
        "At the edge of the reed bed on the north bank after the guns fired: a K2 tank caked in cracked grey mud standing exposed in a ring of burned and flattened grey-green reeds, sandbagged fighting holes, wet grey-brown sand, thin smoke, the throat of the ford three hundred meters away across wet sand, monsoon rain"),
    "LOC_007_k2_turret_int": ("LOC_007", "VEH_001_interior_ref",
        "Inside the cramped commander's station of a K2 tank: the commander's seat, a periscope sight with a rubber eyecup, a cold blue-white screen with a small blank readout, the autoloader's steel tray beside the breech, switch panels, the open commander's hatch above letting in grey light and rain, mud on the hatch rim, no readable text"),
    "LOC_007_k2_driver_int": ("LOC_007", "VEH_001_interior_ref",
        "Inside the reclined driver's compartment of a K2 tank: a yoke-style steering handle, dark instrument panels with no readable text, three periscope blocks with a slot of grey daylight, the driver's hatch above, steel walls close on every side"),
    "LOC_007_k2_roof": ("LOC_007", "LOC_007_throat_ep5",
        "On the turret roof of a K2 tank stalled in chest-deep brown river water: mud-caked steel, the open commander's hatch, dozens of arrows bristling from the roof and stowage basket, rain running down the arrow shafts, brown water and the heads of thousands of soldiers all around below, the reed bed and a steep mud bank on either side"),
    "LOC_007_north_line": ("LOC_007", "LOC_007_north_line_ep5",
        "The north edge of the dense reed bed where the reeds end and a wide wet grey-brown sandflat begins, monsoon rain: a chain of sandbagged fighting holes along the reed edge, a heavy machine gun on a tripod under reeds at one corner, trampled reeds, the sandflat rising to low bare hills in the distance, grey light"),
    "LOC_007_south_edge": ("LOC_007", "LOC_007_k2_reeds_ep5",
        "The south edge of the reed bed facing the throat of the ford, monsoon rain: a low berm of wet sandbags at the reed line, sharpened reed stakes driven into the sand before it, wet grey-brown sand sloping down to the throat of the ford two hundred meters away, tall grey-green reeds behind"),
    "LOC_007_aid": ("LOC_007", "LOC_007_aid_ep5",
        "Deep inside the dense reed bed on the north bank, monsoon rain: rows of reed mats laid on wet grey-brown sand under a low roof of bundled reeds, an olive medic bag, clay bowls of crushed herbs, rolled bandages, tall grey-green reeds walling in every side, cold grey-green light"),
    "LOC_007_west_reeds": ("LOC_007", "LOC_007_aid_ep5",
        "A patch of higher sand in the western reed bed far from the ford, monsoon rain: reed mats with wounded men laid in rows, reeds propped up as rain screens, an olive medic bag, tall grey-green reeds walling in every side"),
    "LOC_007_mortar_pit": ("LOC_007", "LOC_007_k2_reeds_ep5",
        "A sandbagged mortar pit inside the reed bed, monsoon rain: two 81mm mortars with baseplates sunk in wet sand, rows of mortar bombs laid on an olive poncho, six anti-tank launcher tubes leaning on sandbags, tall grey-green reeds walling in the pit"),
    "LOC_007_reeds_night": ("LOC_007", "LOC_007_detail",
        "Deep inside a dense reed bed on a riverbank at night in light rain: tall grey-green reeds barely visible, wet sand, no fire, no lamps, a faint grey sheen of wet reeds, near-black blue darkness"),
    "LOC_007_east_shore": ("LOC_007", "LOC_007_north_line_ep5",
        "The water's edge on the east side of the reed bed, monsoon rain: a strip of wet grey-brown sand and trampled reeds sloping into shallow brown water, the reed bed behind, the wide grey river to the right, the low bare hills of the north bank far to the left"),
    "LOC_007_north_hill_foot": ("LOC_007", "LOC_007_north_hill_ep5",
        "The foot of the low bare hills north of the river, monsoon rain: knee-high wet reeds and grass on a gentle slope, the wide wet grey-brown sandflat below, the dark reed bed and the grey river beyond, low grey cloud on the hilltops"),
    "LOC_007_east_hill": ("LOC_007", "LOC_007_north_hill_ep5",
        "The crest of a low green hill on the north bank east of the ford, monsoon rain: wet grass, low grey cloud, and below the wide grey-brown sandflat and the grey river crowded with crossing troops"),
    "LOC_007_north_flat_edge": ("LOC_007", "LOC_007_north_line_ep5",
        "The wide wet grey-brown sandflat on the north bank just outside the reed bed, monsoon rain: hoofprints and footprints filling with water, trampled reeds, the dark wall of the reed bed on one side, low bare hills in the distance"),
    "LOC_007_mud_bank": ("LOC_007", "LOC_007_throat_ep5",
        "The steep slick mud bank on the east side of the throat of the ford, monsoon rain: grey-brown mud sliding into chest-deep brown water, the reed bed across the sixty-meter gap, wet sand above, rain streaking the mud"),
    "LOC_007_throat_rim": ("LOC_007", "LOC_007_throat_ep5",
        "The sand rim above the throat of the ford on the north bank, monsoon rain: a low gravel-and-sand lip crowded with Sui soldiers looking down into a sixty-meter gap of chest-deep brown water between a dense reed bed on the west and a steep slick mud bank on the east, the wide grey ford beyond"),
    "LOC_007_ford_sun": ("LOC_007", "LOC_007_finale_light",
        "The wide shallow river after the battle: shafts of yellow sunlight tearing through heavy grey cloud onto brown floodwater, wet sandbars littered with broken spears, fallen red and yellow Sui banners and dead horses, dense reed beds on the north bank flattened and scorched, black smoke drifting, steam rising from the water, rain still falling on one side of the frame"),
    "LOC_007_north_flat_sun": ("LOC_007", "LOC_007_finale_light",
        "The north edge of the flattened reed bed and the wet sandflat in warm late-afternoon sunlight after rain: steam rising from wet reeds and uniforms, mud drying grey, olive ponchos laid in a row, broken arrows in the sand, the grey river beyond with shafts of sun on it"),
    "LOC_007_east_shore_sun": ("LOC_007", "LOC_007_finale_light",
        "The water's edge on the east side of the reed bed in warm late-afternoon sunlight after rain: wet grey-brown sand, reed mats, trampled reeds, steam rising, the burned black shape of a tank far off in the throat of the ford, the river glittering"),
    "LOC_007_small_bar_sun": ("LOC_007", "LOC_007_small_bar_ep5",
        "A small wet grey-brown sandbar beside the throat of the ford in warm late-afternoon sunlight after rain: a dead steppe horse lying on it, broken arrows and a fallen red Sui banner in the wet sand, and thirty meters away in the channel the burned black hull of a tank sunk tilted in the water with thin smoke rising, steam on the river"),
    "LOC_007_throat_sun": ("LOC_007", "LOC_007_finale_light",
        "The throat of the ford in late-afternoon sunlight after the rain: a burned black tank stalled broadside in the sixty-meter channel, its turret charred and tilted, brown water pouring over its side skirts and across the hull roof, broken Sui banners and shields drifting past, a dying ring of oil fire, steam, shafts of sun on the water"),
    "KB_silk_map": ("LOC_007", None,
        "Close on a Goguryeo silk map laid flat, rain-grey light, wet edges of the silk, no readable writing"),
    "KB_notebook": ("LOC_007", None,
        "Close on the open page of a small wet-edged field notebook in a torn plastic bag, pencil lines, rain-grey light"),
    "KB_sand_plan": ("LOC_007", None,
        "Close from above on wet grey-brown river sand scratched with lines by an arrow shaft, raindrops pocking the sand, a few flattened reeds at the edge of frame"),
    # ===== LOC_005_AMNOK
    "LOC_005": ("LOC_005", "LOC_005_wide", LOC_LOCK["LOC_005"]),
    "LOC_005_south_bank": ("LOC_005", "LOC_005_wide",
        "The south bank of the dark green Yalu River in light drizzle: wet green grassland and scrub sloping down to a wide shoal of grey cobbles, steep grey rocky mountains covered in pine and young oak across the river, low cloud on the peaks, mist in the valley, cold grey-green light"),
    # ===== LOC_004_YUKHAPSEONG (5화 D+5 mưa)
    "LOC_004_rain": ("LOC_004", "LOC_004_wide",
        "The Sui emperor's prefabricated mobile fortress in steady rain: six-meter walls of timber panels faced with grey-painted hemp cloth imitating brick darkened by rain, red-lacquered wooden watchtowers at the corners, a central pavilion with a golden silk roof and red pillars, red and yellow banners hanging wet, mud and puddles before the red wooden gate, thousands of grey felt tents to the horizon under low grey cloud, and far off the grey stone walls of a Goguryeo fortress"),
    "LOC_004_pavilion_int": ("LOC_004", "LOC_004_detail", CS("LOC_004_pavilion_int")),
    "LOC_004_pavilion_int_rain": ("LOC_004", "LOC_004_detail",
        "Interior of the Sui emperor's field pavilion by day in rain: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes hanging still and damp, a large bronze incense burner with rising smoke, silk lanterns lit against the grey daylight, a red carpet below the dais, rain heard on the silk roof, grey light through the drapes mixing with warm lantern light"),
    "LOC_004_yard_rain": ("LOC_004", "LOC_004_yard_rain_ep5",
        "The muddy courtyard before the golden pavilion inside the Sui mobile fortress in steady rain: churned mud and standing puddles, timber-and-cloth walls painted grey, red-lacquered watchtowers, wet red and yellow banners, grey felt tents beyond the walls, and in the middle of the yard a giant flat wooden ox cart with its wheels sunk in mud carrying a boxy armored vehicle under a mud-caked oiled cloth cover"),
    "LOC_004_jiangdu_618": ("LOC_004", "LOC_004_detail",
        "Interior of a southern Sui palace hall at night, 618 AD: red lacquered pillars, torn yellow silk drapes hanging loose, overturned silk lanterns, doors thrown wide open onto darkness, a polished dark floor, an ochre-yellow silk robe lying abandoned on the floor, dim lantern light"),
    # ===== LOC_006_PYONGYANG (D+8 đêm mưa)
    "LOC_006_hall": ("LOC_006", "LOC_006_interior", CS("LOC_006_hall")),
    "LOC_006_hall_door": ("LOC_006", "LOC_006_interior",
        "From inside the Goguryeo royal audience hall at Pyongyang at night looking out through open latticed wooden doors: a wet stone veranda and courtyard in pouring rain lit by oil lamps from inside, the dark shape of a fortress wall and a wide grey-black river far below, thick round pillars lacquered deep red framing the doorway, warm lamplight inside against wet grey-blue darkness outside"),
    "KB_poem": ("LOC_006", None,
        "Close on a small ivory silk scroll unrolled on a low black lacquered table under the warm light of a clay oil lamp, dark wooden floor beyond, no other objects"),
    # ===== LOC_001_YOHA (cuối 7월 mưa)
    "LOC_001_retreat_rain": ("LOC_001", "LOC_001_wide",
        "Aerial view of the wide brown Liao River in steady rain at the end of July: three long Sui pontoon bridges of lashed flat boats crossing it, endless columns of Sui soldiers with drooping wet banners and empty two-wheeled carts crossing back west, the east bank a plain of wet green grass with grey felt tents being struck in patches, and on a low rise the grey granite walls of a Goguryeo fortress with black banners still standing, low grey cloud"),
    "LOC_001_road_west": ("LOC_001", "LOC_001_road_west_ep5",
        "A muddy dirt road running west across wet yellow-green grassland in grey rain: ruts filled with water, low grey sky, no trees, no buildings, a giant flat wooden cart drawn by forty oxen far along the road"),
    "LOC_001_cart_bench": ("LOC_001", "LOC_001_road_west_ep5",
        "The driver's bench of a giant wooden ox cart on a muddy road in grey rain: rain-dark wooden planks, a coiled leather whip, the wet backs of oxen ahead, wet yellow-green grassland beyond"),
    # ===== LOC_002_YODONGSEONG (613 KB)
    "LOC_002_siege_613": ("LOC_002", "LOC_002_wide",
        "The Goguryeo plain fortress in a hot summer haze, 613 AD: dry-stacked grey granite walls with rectangular bastions, an enormous ramp of raw earth piled against the wall, a Sui eight-wheeled siege tower of raw timber and wet ox hide lowering its drop-bridge onto the battlements, cloud ladders against the wall, arrows and stones falling from the bastions, red Sui banners, yellow dust, and far off in the dark corner of the frame a Sui column retreating by night with torches put out"),
}

# ---------------------------------------------------------------- LIGHTING theo bảng ngày/đêm 5화 (header script v2.1) — 3 pha LOC_007
LIGHT = {
    "dawn_grey": "Flat grey dawn in light drizzle, silver-grey diffused light, no shadows, thin river mist, water beading on every surface",
    "dawn_grey_aerial": "Flat grey dawn seen from high above, silver-grey light, light drizzle, thin mist on the water",
    "morning_grey": "Early morning under heavy grey cloud in light rain, flat cold grey-green light, thin mist on the water",
    "day_rain": "Grey daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet",
    "day_rain_heavy": "Grey daylight in heavy monsoon rain, big drops pocking the water, flat cold grey-green light, low cloud, mist",
    "day_rain_smoke": "Grey monsoon daylight in steady rain, grey smoke drifting through the rain, flat cold light",
    "day_rain_muzzle": "Grey monsoon daylight in steady rain lit for an instant by a white-orange muzzle flash, flat cold light beyond",
    "day_rain_fire": "Grey monsoon daylight in steady rain, harsh white-yellow fire and glowing red steel throwing hard light and orange reflections on the brown water, white smoke",
    "day_rain_firelight": "Grey monsoon daylight in steady rain, orange firelight from burning oil on the water flickering on wet faces and armor",
    "sun_tearing": "Shafts of yellow sunlight tearing through heavy grey cloud, hard warm light on wet sand and brown water, steam rising, rain still falling at the edge of frame",
    "sun_afternoon": "Warm late-afternoon sunlight after rain, long soft shadows, steam rising from wet ground, a clearing pale sky",
    "sun_clear": "Clear warm daylight under a pale blue sky, dry cracked mud, hard sunlight, a light breeze",
    "turret_screen": "Inside the turret, cold blue-white glow of a screen and grey daylight through the open hatch on the face, deep black shadows",
    "turret_dark": "Inside the turret, dim grey light through the periscope slot and a cold blue screen glow, deep black shadows",
    "turret_fire": "Inside the turret, blinding white-yellow light of burning metal, molten sparks, white smoke",
    "driver_int": "Inside the driver's compartment, dim grey daylight through the periscope blocks, faint instrument glow, deep shadows",
    "night_rain_flashback": "Night in light rain, near-black blue darkness, a faint grey sheen on wet reeds and faces, no fire, no lamps",
    "day_rain_yukhap": "Grey daylight in steady rain, flat cold light, wet red and gold surfaces dulled by rain",
    "pavilion_lamp": "Grey rainy daylight through silk drapes mixing with warm silk-lantern light, deep shadows",
    "night_lamp_rain": "Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in through open doors",
    "night_palace_618": "Night interior, a few overturned lanterns giving dim uneven warm light, deep shadows",
    "summer_haze_613": "Hot summer daylight under a hazy white sky, yellow dust, hard flat light",
    "aerial_rain": "Grey daylight from high above in steady rain, flat cold light, low cloud, mist on the water",
}
WEAR = {
    "rain": "Modern soldiers' helmets covered and stuck with reed stalks, faces smeared with mud, mud caked to the waist, rain-soaked uniforms with sleeves patched in brown Goguryeo cloth, week-old stubble, Korean flag patches on right shoulders still visible through the mud.",
    "sun": "Modern soldiers' uniforms drying grey with caked mud, helmets off or pushed back, faces streaked with dried mud and someone else's blood, exhausted eyes, Korean flag patches on right shoulders visible.",
    "night": "Modern soldiers' uniforms soaked and mud-smeared, helmets off, faces smeared with mud, week-old stubble.",
}
ROK = {"CHAR_001", "CHAR_002", "CHAR_003", "CHAR_004", "CHAR_005", "CHAR_006"}

# ---------------------------------------------------------------- PARSE SCRIPT (nguyên văn)
def parse_script():
    txt = open(SCRIPT, encoding="utf-8").read()
    blocks = re.split(r"\n(?=### SC_\d{3})", txt)
    out = {}
    for b in blocks:
        if not b.startswith("### SC_"):
            continue
        head, _, body = b.partition("\n")
        body = re.split(r"\n(?:---|## 부록)", body)[0]
        parts = head[4:].split(" · ")
        sid = parts[0].strip()
        loc_hdr = parts[1].strip(); chars_hdr = parts[2].strip(); veh_hdr = parts[3].strip()
        typ = parts[-2].strip(); tm = parts[-1].strip()
        m = re.match(r"(\d+):(\d+)[–-](\d+):(\d+)", tm)
        t0 = int(m.group(1)) * 60 + int(m.group(2)); t1 = int(m.group(3)) * 60 + int(m.group(4))
        nar, dlg, sound, action_vi = [], [], "", ""
        for ln in body.split("\n"):
            ln = ln.strip()
            if not ln or ln.startswith("[Kết thúc") or ln.startswith("[MID-ROLL") or ln.startswith("[NARRATOR") or ln.startswith("[END CARD]") or ln.startswith("## ") or ln.startswith("> ") or ln.startswith("### —"):
                continue
            if ln.startswith("[ACTION-VI]"):
                action_vi = ln[len("[ACTION-VI]"):].strip(); continue
            if ln.startswith("[SOUND]"):
                sound = ln[len("[SOUND]"):].strip(); continue
            if ln.startswith("N:"):
                nar.append(ln[2:].strip()); continue
            mm = re.match(r"^([^\[\s:][^:]{0,24}):\s*(.+)$", ln)
            if mm:
                dlg.append(f"{mm.group(1).strip()}: {mm.group(2).strip()}")
        out[sid] = dict(id=sid, t=tm.replace("-", "–"), t0=t0, t1=t1, type=typ, loc_hdr=loc_hdr, chars_hdr=chars_hdr,
                        veh_hdr=veh_hdr, nar=" ".join(nar), dlg=dlg, sound=sound, action_vi=action_vi)
    return out

def load_batches():
    scenes = []
    for f in sorted(glob.glob(os.path.join(HERE, "batch_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        scenes += mod.SCENES
    return scenes

def tag_of(rid):
    return "@" + rid

EXTRA_REF = {  # extra → ref đính
    "GOG_SPEARMEN": "WPN_102_ref", "GOG_SPEARMEN_SUN": "WPN_102_ref", "GOG_FIRE_ARCHERS": "WPN_102_ref", "GOG_DRUMMERS": "WPN_102_ref",
    "GOG_FLAG_BEARER": "WPN_102_ref", "GOG_HORN_BLOWER": "WPN_102_ref", "GOG_ARCHER_OFFICER": "WPN_102_ref", "GOG_GUARDS": "WPN_102_ref",
    "GOG_CAVALRYMEN": "VEH_101_ref", "GOG_CAV_OFFICER": "VEH_101_ref",
    "GOG_DEPUTY": "EXTRA_gog_deputy_ref", "GOG_YOUNG_RIDER": "EXTRA_gog_young_rider_ref",
    "SUI_WADERS": "WPN_201_ref", "SUI_WADER_FACE": "WPN_201_ref", "SUI_INFANTRY": "WPN_201_ref", "SUI_INFANTRY_BACKS": "WPN_201_ref",
    "SUI_SHIELD_WALL": "WPN_201_ref", "SUI_ARCHERS": "WPN_201_ref", "SUI_ROUT": "WPN_201_ref", "SUI_STRAGGLERS": "WPN_201_ref",
    "SUI_DEPUTY": "WPN_201_ref", "SUI_STANDARD_BEARER": "PROP_021_ref", "SUI_GUARDS_WET": "WPN_201_ref", "SUI_FEET": "WPN_201_ref",
    "SUI_REAR_GENERAL": "VEH_207_ref", "SUI_CAVALRYMEN": "VEH_207_ref",
    "XIANBEI_SCOUTS_2": "VEH_206_ref", "XIANBEI_RIDERS": "VEH_206_ref", "XIANBEI_ARCHER": "VEH_206_ref",
    "XIANBEI_RIDER_ON_HULL": "VEH_206_ref", "XIANBEI_LEADERS_2": "VEH_206_ref",
    "ROK_DRIVER": "EXTRA_k2_driver_ref", "ROK_WOUNDED": "EXTRA_rok_wounded_ref" if "EXTRA_rok_wounded_ref" in REF_DIR else None,
}

def build_scene(s, sc):
    sid = s["id"]
    chars = s.get("chars", [])
    states = s.get("states", {})
    vehs = s.get("veh", [])
    props = s.get("props", [])
    xprops = s.get("xprops", [])
    extras = s.get("extras", [])
    subloc = s["loc"]
    loc_id, loc_ref, loc_text = SUBLOC[subloc]
    refs, seen = [], set()
    def add_ref(r):
        if r and r not in seen:
            seen.add(r); refs.append(r)
    seg = [s["shot"].rstrip(".") + "."]
    for c in chars:
        st = states.get(c)
        if st:
            cid, ref_id, st_text = DERIVED[st]
            assert cid == c, (sid, c, st)
        else:
            ref_id, st_text = f"{c}_ref", ""
        seg.append(f"{tag_of(ref_id)}: {LOCKS[c]}" + (f" {st_text}" if st_text else ""))
        add_ref(ref_id)
    for e in extras:
        et = EXTRAS[e][0].upper() + EXTRAS[e][1:]
        seg.append(et if et.endswith(".") else et + ".")
        r = EXTRA_REF.get(e)
        if r and r in REF_DIR:
            # không đính VEH ref hai lần nếu vehicle đã có
            if not (r.endswith("_ref") and r[:-4] in vehs): add_ref(r)
    lock_pending = []
    for v in vehs:
        vref = s.get("veh_ref", {}).get(v, f"{v}_ref")
        vst = s.get("veh_state", {}).get(v)
        seg.append(f"{tag_of(vref)}: {LOCKS[v]}" + (f". {VEH_STATE[vst]}" if vst else ""))
        add_ref(vref)
        if v in LOCK_PENDING: lock_pending.append(v)
    for p in props:
        pref = f"{p}_ref" if f"{p}_ref" in REF_DIR else None
        pst = s.get("prop_state", {}).get(p)
        ptxt = PROP_LOCK_ALT[f"{p}:{pst}"] if pst else LOCKS[p]
        seg.append((f"{tag_of(pref)}: " if pref else "") + ptxt)
        add_ref(pref)
    for xp in xprops:
        seg.append(EXTRA_PROPS[xp][0].upper() + EXTRA_PROPS[xp][1:])
        if xp == "SILK_MAP": add_ref("EXTRA_silk_map_ref"); lock_pending.append("SILK_MAP(PROP_001?)")
        if xp == "SMALL_CROW_PENNANT": lock_pending.append("SMALL_CROW_PENNANT(PROP_012?)")
    seg.append(("Setting " + tag_of(loc_ref) + ": " if loc_ref else "Setting: ") + loc_text)
    add_ref(loc_ref)
    seg.append("Action: " + s["action"].rstrip(".") + ".")
    light = LIGHT[s["light"]] if s["light"] in LIGHT else s["light"]
    seg.append("Light: " + light.rstrip(".") + ".")
    if any(c in ROK for c in chars) or any(e.startswith("ROK") for e in extras):
        seg.append(WEAR[s.get("wear", "rain")])
    if s.get("note_prompt"):
        seg.append(s["note_prompt"].rstrip(".") + ".")
    seg = [x if x.rstrip().endswith((".", "!", "?")) else x.rstrip() + "." for x in seg]
    seg.append(STYLE)
    image_prompt = " ".join(seg)
    for r in s.get("refs_extra", []): add_ref(r)
    for r in s.get("refs_drop", []):
        if r in seen: refs.remove(r); seen.discard(r)
    refs = refs[:10]
    for r in refs: assert r in REF_DIR, (sid, r)
    is_video = sc["type"] == "video8s"
    edit_only = s.get("edit_only", False)
    quality = bool(s.get("aerial", False)) or bool(s.get("quality", False))
    rec = {
        "id": sid, "part": s["part"], "t_start": sc["t0"], "t_end": sc["t1"], "seconds": sc["t1"] - sc["t0"],
        "type": sc["type"], "loc": loc_id, "subloc": subloc, "phase": s.get("phase", ""),
        "chars": chars, "extras": extras, "vehicles": vehs, "props": props + xprops,
        "states": [states[c] for c in chars if c in states],
        "shot": s["shot"],
        "image_prompt": None if edit_only else image_prompt,
        "video_prompt": s["video"],
        "action_start": s["a0"], "action_end": s["a1"],
        "narration_ko": sc["nar"], "dialogue_ko": sc["dlg"], "sound": sc["sound"],
        "continuity": s.get("cont", ""),
        "chain_from": s.get("chain"), "cut_half": bool(s.get("cut", False)),
        "aerial_quality": quality, "aerial": bool(s.get("aerial", False)), "ai_risk": s.get("risk", ""),
        "overlay_text": s.get("overlay"),
        "two_beat": bool(s.get("two_beat", False)),
        "lock_pending": lock_pending,
        "refs": [] if edit_only else refs,
        "image_body": None if edit_only else {
            "prompt": image_prompt, "model": "nano_banana_pro", "aspect_ratio": "16:9",
            "reference_images": [{"path": ref_path(r), "name": r} for r in refs],
        },
        "video_body": None if (not is_video or edit_only) else {
            "prompt": s["video"], "model": "veo_31_quality" if quality else "veo_31_fast",
            "mode": "start_image", "aspect_ratio": "16:9", "resolution": ["1080p"], "video_length": 8,
            "reference_images": [],
        },
        "video_ref_candidates": [] if (not is_video or edit_only) else refs[:2],
        "edit_only": edit_only,
        "insert_clip": s.get("insert"),
    }
    return rec

def md_scene(r, sc):
    loc_line = f"{r['loc']}" + (f" ({r['subloc']})" if r['subloc'] != r['loc'] else "")
    chars = ", ".join(r["chars"] + r["extras"]) or "—"
    vehs = ", ".join(r["vehicles"]) or "—"
    props = ", ".join(r["props"]) or "—"
    kb = "video8s" if r["type"] == "video8s" else "still_kenburns"
    L = []
    L.append(f"### {r['id']} | {sc['t']} | {loc_line} | {chars} | {vehs} | PROPS: {props} | TYPE: {kb} | {r['seconds']}s" + (f" | {r['phase']}" if r['phase'] else ""))
    L.append(f"SHOT: {r['shot']}" + ("  · ⚑ AERIAL/QUALITY" if r["aerial_quality"] else "") + ("  · 2-BEAT" if r["two_beat"] else ""))
    if r["edit_only"]:
        L.append("IMAGE_PROMPT: — (EDIT ONLY: end card đen + chữ ở khâu edit, không tạo ảnh AI)")
    else:
        L.append(f"IMAGE_PROMPT: {r['image_prompt']}")
    L.append(f"VIDEO_PROMPT: {r['video_prompt']}")
    L.append(f"ACTION_START: {r['action_start']}")
    L.append(f"ACTION_END: {r['action_end']}")
    L.append(f"NARRATION_KO: {r['narration_ko'] or '—'}")
    L.append("DIALOGUE_KO: " + (" / ".join(r["dialogue_ko"]) if r["dialogue_ko"] else "—"))
    L.append(f"SOUND: {r['sound'] or '—'}")
    L.append(f"CONTINUITY: {r['continuity'] or '—'}")
    L.append(f"CHAIN_FROM: {r['chain_from'] or '—'}")
    L.append(f"CUT_HALF: {'yes' if r['cut_half'] else 'no'}")
    L.append(f"REFS: {', '.join(r['refs']) if r['refs'] else '—'}")
    if r["overlay_text"]:
        L.append(f"OVERLAY (edit): {r['overlay_text']}")
    if r["lock_pending"]:
        L.append(f"LOCK_PENDING: {', '.join(r['lock_pending'])} (lock tạm trong build.py EXTRA_PROPS — world-designer khóa ID/prop bible)")
    if r["ai_risk"]:
        L.append(f"AI_RISK: {r['ai_risk']}")
    if r.get("insert_clip"):
        L.append(f"INSERT_CLIP ({r['insert_clip']['seconds']} s, tách riêng): {r['insert_clip']['prompt']}")
    return "\n".join(L) + "\n"

HEADER = """# 살수 612 — 5화 「살수」 (最終話) · SCENE LIST (VEO3 / G-Labs) · v1 · 2026-09-16 · veo-prompt-engineer
> Nguồn: `02_script/full_script_ep5.md` v2.1 TTS-trimmed (289 SC · 40:00 · 249 video8s + 40 still) · `continuity_master.json` v3 (LOCKED: +VEH_207 kỵ Tùy, PROP_024 cờ đỏ hiệu lệnh, PROP_025 nhiệt nhôm, PROP_023 biển "3", PROP_026 nút bầu, sublocks LOC_007 8 sub-địa hình, derived 5화) · character/location/vehicle/prop bible v3 · template 04 §C–§H · decisions.md (sau QC 5화 → v2; TTS-trim; bible v3) · 04_veo/VEO_BRIEF.md.
> Format §C như 1화/4화. Mỗi SC: IMAGE_PROMPT (ảnh keyframe 16:9, nano_banana_pro, ref ≤10) → VIDEO_PROMPT (veo_31_fast, mode start_image, 8 s, 1080p). still_kenburns = chỉ ảnh, ken-burns ở khâu edit. **Không mid-roll 5** (P-46) — mid-roll 1–4 @7:00/14:00/21:00/27:30.
> **Thứ tự dòng thời gian:** SC_169 (22:38–22:46) đứng TRƯỚC SC_165 (dời theo QC, giữ ID) — file này và scenes_ep5.json xếp theo t_start.
> **Quy ước prompt:** tag `@<ref_id>` đứng trước lock (`@CHAR_001_muddy_bloody_ep5`, `@CHAR_205_final_ep5`, `@LOC_007_throat_ep5`) — tag = đúng `name` trong `reference_images`. VISUAL_LOCK dán NGUYÊN VĂN từ continuity_master.json v3; derived state ✔ = `derived_states[*].prompt_add` nguyên văn (ref biến thể đính thay ref gốc); trạng thái trong tập (`*_ep5` do veo đặt theo bảng "Trạng thái theo tập" 5화) đính ref gần nhất — xem ep5_asset_usage.md §1. Không tên riêng; không chữ trong ảnh: màn hình bộ đếm 잔탄 06→04→03→01→00 (SC_008/082/086/093/189/213), sổ 박기철, bản đồ lụa, bài thơ, end card → `OVERLAY (edit)`; Hangul trên xe KHÔNG vẽ (decisions #1) — chỉ số Ả Rập "1" trên tháp K2 và "3" trên biển PROP_023; 태극기 vai PHẢI (P-38).
> **Derived 5화 (đúng tập):** 한승우 muddy_bloody (P1–P9, tháp K2 P10 Ph.1–2) → **river_oil** (SC_222–229, 246–247: tháo mũ, loang dầu) → **final** (P11–P12: băng tay phải, bao K5 rỗng, nắng) · 오태민 reeds_helmet (kính còn trên mũ tới SC_131) → **muddy_bloody** (SC_132+: kính mất, băng tay trái, K3 băng dính) · 박기철 muddy (mũ lưỡi trai tới SC_136 → capless) → driver (SC_197–207) → wounded (SC_219–247 tên đùi TRÁI theo bible/ref) → **crutch** (P11–P12) · 서아 muddy_bloody toàn tập · 태오 **goguryeo_helmet** toàn tập · 백성민 **horseback** (SC_026, P9–P10) → afoot (SC_283–284) · 을지문덕 **salsu_rain** (P1–P11) → false_surrender_ep3 (조우관 + áo lụa, P12 nội điện) · 해모루 radio_ep3 (P2/flashback) → reeds/bow (P6–P9, radio chết còn trên giáp) → **wounded** (SC_234–248 cán tên cắm dưới xương đòn trái) → **bandaged** (SC_255+) · 우중문 **rain** (SC_016–064) → river (SC_081–236 ngã nước, gương ngực móp, cờ gãy) → **defeat** (SC_237–264 trói, quỳ) · 우문술 rain_mounted (ngựa xám) → **retreat** (SC_239) → **chained** (SC_267–269) · 탁발흠 waiting (SC_060–123 cung slung, đao chưa rút, kính vỡ treo cổ, băng tay PHẢI) → **final** (SC_124–127 đao rút) → capless (SC_146–249 mũ mất) → bow (SC_245) · 양제 **defeat_news** (SC_267–269) → **rain_k21** (SC_270–272).
> **K2 damage 4 pha (VEH_STATE sau lock):** `k2_reeds` (P1–P9 mép lau, 300 m) → `k2_after_fire` (SC_084–101) → `k2_arrows` (SC_122–199) → `k2_running` (SC_200–205) → `k2_stalled` (SC_206–224 chết máy chắn khe, xả dầu) → `k2_burning` (SC_225–249 nhiệt nhôm, vòng lửa) → `k2_sunk` (SC_251–265) → `k2_wreck` (SC_281–284, ref `VEH_001_ep5`). 천둥 3 = `VEH_002_captured` + `k21_captured` (SC_270–272) / `k21_road` (SC_286).
> **Sub-lock LOC_007 (8 sub-địa hình v3 nguyên văn + sub-lock mới 5화):** `LOC_007` aerial 3 pha · `_reeds` · `_throat` (cổng họng 60 m) · `_throat_k2` (K2 chắn khe) · `_small_bar` (mô cát nhỏ 30 m, xác ngựa) · `_mid_bar` (mô cát giữa sông, cờ 우중문) · `_upstream_bar` (1,5 km đông) · `_north_flat` (bãi bắc/đồi bắc) · `_south_knoll` (gò nam) · `_aftermath` (nước rút); mới: `_dawn_aerial`, `_south_shore`, `_south_field`, `_ford`, `_ford_surface`, `_k2_reeds`, `_k2_reeds_flat`, `_k2_turret_int`, `_k2_driver_int`, `_k2_roof`, `_north_line`, `_south_edge`, `_aid`, `_west_reeds`, `_mortar_pit`, `_reeds_night`, `_east_shore`, `_north_hill_foot`, `_east_hill`, `_north_flat_edge`, `_mud_bank`, `_throat_rim`, `_ford_sun`, `_north_flat_sun`, `_east_shore_sun`, `_small_bar_sun`, `_throat_sun` + LOC_005_south_bank, LOC_004_rain/_yard_rain/_pavilion_int_rain/_jiangdu_618, LOC_006_hall (bible)/_hall_door, LOC_001_retreat_rain/_road_west/_cart_bench, LOC_002_siege_613 → `02_script/sublocks_ep5.md`.
> **Ánh sáng 3 pha LOC_007 (bảng ngày/đêm):** bình minh xám `dawn_grey` (P1–P2 SC_001–031; flashback SC_027–028 `night_rain_flashback`) → sáng sớm `morning_grey` (P3) → mưa dầm `day_rain`/`day_rain_heavy` (P4–P10 Ph.5, SC_050–249; lửa: `day_rain_fire`/`_firelight`) → nắng xé mây `sun_tearing` (Phase 6 SC_250–251) → `sun_afternoon` (P11 SC_253–265) → `sun_clear` (D+10 SC_281–284). LOC_005 mưa phùn, LOC_004 D+5 mưa, LOC_006 D+8 đêm mưa, LOC_001 cuối 7월 mưa, LOC_002 613 nắng hè.
> **Quy tắc 8 s (§F):** 1 SC = 1 địa điểm, 1 hành động chính, ≤2 người nói, 1 chuyển động camera. `CUT_HALF: yes` = hook 0–32 s + khối trận/contact (P2 017–018 · P3 046–047 · P4 050–051/057–072 · P5 076–100 · P6 114/121–129 · P7 127–147 · P8 169 · P9 190–192 · P10 200–250 · P11 252) → edit cắt 2 shot 4 s. **2-BEAT ×22** (SC_001/002/003/004 hook · 078/080/082/084/085/086 sáu viên · 128 · 204/207/208 · 211 · 215 · 218/220/223/224 · 245/249): beat A/B ghi trong VIDEO_PROMPT; beat là góc máy/địa điểm khác → `INSERT_CLIP` tách riêng (3–4 s). Đại quân = aerial wide (⚑ AERIAL/QUALITY → veo_31_quality; ảnh nano_banana_pro + upscale 2K); ⚑ cũng đánh cho clip climax lửa/nhiệt nhôm (SC_225/227/244/249/250).
> **CHAIN_FROM:** chỉ khi SC trước (theo dòng thời gian) là video8s, cùng địa điểm + nhân vật, hành động nối tiếp → glabs-operator lấy tail-frame làm start_image (`--chain`). Không chain quá 3 clip liên tiếp.
> **[END CARD] SC_288/289:** EDIT ONLY — đen + chữ trắng 「살수 612 — 끝」 / 「다음: 613」 (gieo series 2 「613」, P-18). **[OVERLAY]** 잔탄 06→04→03→01→00 + subtitle 知足願云止 (SC_285) — không vẽ chữ.
> **LOCK_PENDING (prop không có ID bible phù hợp):** bản đồ lụa 을지문덕 (script tag PROP_001 ≠ bản đồ giấy ROK) → lock tạm `SILK_MAP` + ref `EXTRA_silk_map_ref`; cờ hiệu nhỏ 삼족오 (SC_180, script tag PROP_012) → `SMALL_CROW_PENNANT`; K5 (không lock) → mô tả trong Action. Đề xuất world-designer thêm PROP_027 bản đồ lụa / PROP_028 cờ hiệu nhỏ.
> **Style tag (§D, cuối mọi image prompt):** `{style}`
> **Negative (§E, ghi 1 lần):** `{neg}`
> **QC ảnh §G / QC video §H** áp dụng trước khi tạo video; ảnh fail → regenerate ≤3 lần (đổi seed / đơn giản hoá prompt), vẫn fail → giảm số nhân vật trong khung.

"""

PART_TITLES = {
    1: "[Phần 1] 여섯 — 「여섯」 (0:00–1:30) · hook, không narrator 0–32 s · D1 rạng đông xám · 2-BEAT SC_001–004",
    2: "[Phần 2] 마개 — 「마개」 (1:30–4:30) · bàn cờ (bản đồ lụa + aerial) · 방진 [史] · flashback nút bầu · 'nửa dưới nước'",
    3: "[Phần 3] 탄창 넷 — 「탄창 넷」 (4:30–7:00) · điểm danh cuối · phát băng đạn · 을보 'gia슴까지' · hậu quân giao tranh [史] · MID-ROLL 1 @7:00",
    4: "[Phần 4] 붉은 깃발 — 「붉은 깃발」 (7:00–10:30) · tiền quân qua cổng họng · vết xích · 탁발흠 đếm sấm · cờ 우중문 ra mô cát · cờ đỏ, tên lửa, trống",
    5: "[Phần 5] 여섯, 다섯, 넷 — 「여섯, 다섯, 넷」 (10:30–14:00) · 나각 3 hồi · 6 viên (narrator im 10:38–12:30) · cối 30, PZF 6 · 신세웅 [史] · '조용하다' · MID-ROLL 2 @14:00",
    6: "[Phần 6] 한 명도 북으로 — 「한 명도 북으로」 (14:00–17:30) · 해모루 vào lau · 2.000 kỵ · 을지문덕 không chia quân · 우문술 '뚫어라' · '오십오 톤'",
    7: "[Phần 7] 쇠수레가 벙어리가 됐다 (17:30–21:00) · kỵ Tiên Ti ngựa bịt tai xông lau · K6 câm (narrator im 18:18–18:50) · K5 15→0 · lái xe trúng tên · 91→86 · MID-ROLL 3 @21:00",
    8: "[Phần 8] 마개는 우리다 — 「마개는 우리다」 (21:00–24:00) · chia đạn · radio 5 % · '전차를 여울에 박는다' · biển 천둥 3 · SC_169 trước SC_165",
    9: "[Phần 9] 300미터 — 「300미터」 (24:00–27:30) · kế trên cát · radio chết → 나각/cờ · giới hạn lội 1,2 m · nút bầu cắm mũi xe · MID-ROLL 4 @27:30",
    10: "[Phần 10] 살수 — 「살수」 (27:30–34:30) · 6 phase · Ph.1 300 m/chết máy/xả dầu/나각 · Ph.2 kẻ săn · Ph.3 sai sót/nhiệt nhôm/vòng lửa · Ph.4 NARRATOR IM 31:30–33:22 · Ph.5 nóc xe · Ph.6 nắng xé mây · CUT_HALF toàn khối",
    11: "[Phần 11] 2천 7백 — 「2천 7백」 (34:30–37:30) · truy kích 압록 [史] (LOC_005) · 80 người · 해모루 băng chéo · 을지문덕 xuống mô cát · 경례 · bát nước 우중문 · 육합성 D+5: xiềng 우문술, 양제 chạm K21 '내년'",
    12: "[Phần 12] 이제 우리는 뭡니까 (37:30–40:00) · 613/614/618 [史] · nội điện 평양 D+8 · Salsu D+10 nước rút: biển 3 lên xác K2 · '이제 우리는 뭡니까?' · 知足願云止 · xe bò về 낙양 · [END CARD] 「613」",
}

NAMES = ("한승우", "오태민", "Han Seung", "Tae-min", "Eulji", "Tuoba", "Yang Guang", "Ki-cheol", "Seo-ah", "Tae-oh", "Seong-min",
         "Hae Mo", "Jeong-su", "Eul-bo", "A-ri", "Lai Huer", "Yu Zhongwen", "Yuwen", "Geon-mu", "Yeongyang", "Seung-woo",
         "Shin Se", "Wang In", "Luoyang", "Mundeok", "Zhongwen")

def validate(recs):
    errs = []
    ids = [r["id"] for r in recs]
    exp = sorted(f"SC_{i:03d}" for i in range(1, N_SC + 1))
    if sorted(ids) != exp:
        missing = sorted(set(exp) - set(ids)); extra = sorted(set(ids) - set(exp))
        errs.append(f"ID mismatch: missing={missing[:10]} extra={extra[:10]} n={len(ids)}")
    if len(ids) != len(set(ids)): errs.append("duplicate IDs")
    t = 0
    chain_run = 0
    for i, r in enumerate(recs):
        if r["t_start"] != t: errs.append(f"{r['id']} t_start {r['t_start']} != {t}")
        t = r["t_end"]
        if r["type"] == "video8s" and r["seconds"] != 8: errs.append(f"{r['id']} video not 8s")
        if not r["edit_only"]:
            if not r["image_prompt"].endswith(STYLE): errs.append(f"{r['id']} style tag missing")
            if len(r["refs"]) > 10: errs.append(f"{r['id']} >10 refs")
            for c in r["chars"]:
                if LOCKS[c] not in r["image_prompt"]: errs.append(f"{r['id']} lock {c} not verbatim")
            for v in r["vehicles"]:
                if LOCKS[v] not in r["image_prompt"]: errs.append(f"{r['id']} lock {v} not verbatim")
            for st in r["states"]:
                if DERIVED[st][2] not in r["image_prompt"]: errs.append(f"{r['id']} derived {st} not verbatim")
            for tok in NAMES:
                if tok in r["image_prompt"] or tok in r["video_prompt"] or (r.get("insert_clip") and tok in r["insert_clip"]["prompt"]):
                    errs.append(f"{r['id']} proper name '{tok}' in prompt")
            if r["type"] == "video8s" and len(r["chars"]) > 3: errs.append(f"{r['id']} >3 named chars in a clip")
            if r["type"] == "video8s" and len(r["dialogue_ko"]) > 2: errs.append(f"{r['id']} >2 speakers")
        if r["chain_from"]:
            if r["chain_from"] not in ids: errs.append(f"{r['id']} chain_from unknown"); continue
            prev = recs[ids.index(r["chain_from"])]
            if prev["type"] != "video8s": errs.append(f"{r['id']} chain_from {r['chain_from']} is not video8s")
            if ids.index(r["chain_from"]) != i - 1: errs.append(f"{r['id']} chain_from not previous SC (timeline)")
            chain_run += 1
            if chain_run > 3: errs.append(f"{r['id']} chain run >3")
        else:
            chain_run = 0
    if t != 2400: errs.append(f"total seconds {t} != 2400")
    return errs

def usage_report(recs):
    C = collections.Counter
    cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra = C(), C(), C(), C(), C(), C(), C(), C()
    for r in recs:
        for c in r["chars"]: cnt_char[c] += 1
        for s in r["states"]: cnt_state[s] += 1
        cnt_loc[r["loc"]] += 1; cnt_sub[r["subloc"]] += 1
        for v in r["vehicles"]: cnt_veh[v] += 1
        for p in r["props"]: cnt_prop[p] += 1
        for x in r["refs"]: cnt_ref[x] += 1
        for e in r["extras"]: cnt_extra[e] += 1
    return cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra

def main():
    sc = parse_script()
    assert len(sc) == N_SC, len(sc)
    authored = load_batches()
    recs = [build_scene(s, sc[s["id"]]) for s in authored]
    recs.sort(key=lambda r: (r["t_start"], r["id"]))
    errs = validate(recs)
    if errs:
        print("VALIDATION ERRORS:"); print("\n".join(errs))
        if "--force" not in sys.argv: sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    md = [HEADER.replace("{style}", STYLE).replace("{neg}", NEGATIVE)]
    nv = sum(1 for r in recs if r["type"] == "video8s"); ns = len(recs) - nv
    md.append(f"**Tổng:** {len(recs)} SC · {nv} video8s · {ns} still_kenburns · {sum(r['seconds'] for r in recs)} s · chain_from: {sum(1 for r in recs if r['chain_from'])} · cut_half: {sum(1 for r in recs if r['cut_half'])} · 2-beat: {sum(1 for r in recs if r['two_beat'])} · aerial/quality: {sum(1 for r in recs if r['aerial_quality'])} · insert_clip: {sum(1 for r in recs if r['insert_clip'])} · overlay: {sum(1 for r in recs if r['overlay_text'])} · edit_only: {sum(1 for r in recs if r['edit_only'])} · lock_pending: {sum(1 for r in recs if r['lock_pending'])}\n\n---\n")
    cur = None
    for r in recs:
        if r["part"] != cur:
            cur = r["part"]; md.append(f"\n## {PART_TITLES[cur]}\n")
        md.append(md_scene(r, sc[r["id"]]))
    open(f"{OUT_DIR}/scene_list_ep{EP}.md", "w", encoding="utf-8").write("\n".join(md))
    json.dump(recs, open(f"{OUT_DIR}/scenes_ep{EP}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    os.makedirs(ROOT + f"/output/ep{EP}/kich_ban", exist_ok=True)
    open(ROOT + f"/output/ep{EP}/kich_ban/scene_list.md", "w", encoding="utf-8").write("\n".join(md))
    write_usage(recs)
    write_sublocks(recs)
    write_ref_jobs(recs)
    print(f"OK {len(recs)} SC · video {nv} · still {ns} · chain {sum(1 for r in recs if r['chain_from'])} · cut_half {sum(1 for r in recs if r['cut_half'])} · 2beat {sum(1 for r in recs if r['two_beat'])} · aerial/quality {sum(1 for r in recs if r['aerial_quality'])} · insert {sum(1 for r in recs if r['insert_clip'])} · overlay {sum(1 for r in recs if r['overlay_text'])} · edit_only {sum(1 for r in recs if r['edit_only'])}")

BIBLE_IDS = {k for k, v in DERIVED.items() if k in CM_DER and v[2] == CM_DER[k]["prompt_add"]}

def write_usage(recs):
    cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra = usage_report(recs)
    L = ["# 5화 「살수」 (最終話) — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)",
         "> Đếm theo `04_veo/scenes_ep5.json` (289 SC, xếp theo t_start — SC_169 trước SC_165). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.", ""]
    L.append("## 1. Nhân vật (CHAR) — số SC xuất hiện")
    L.append("| CHAR | SC | Derived state trong 5화 (SC) |"); L.append("|---|---|---|")
    for c, n in sorted(cnt_char.items()):
        sts = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_state.items()) if k.startswith(c))
        L.append(f"| {c} | {n} | {sts or '— (base)'} |")
    L.append("")
    L.append("### Trạng thái trong tập do veo đặt (không có trong continuity_master.derived_states — đề xuất character-designer nhập DERIVED_STATES; ref đính = ref gần nhất)")
    L.append("| state_id | CHAR | ref đính | câu trạng thái |"); L.append("|---|---|---|---|")
    for k, (c, rid, txt) in DERIVED.items():
        if k not in BIBLE_IDS and cnt_state.get(k):
            L.append(f"| {k} | {c} | {rid} | {txt} |")
    L.append(""); L.append("### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)")
    L.append("| Extra | SC | ref đính |"); L.append("|---|---|---|")
    for e, n in cnt_extra.most_common(): L.append(f"| {e} | {n} | {EXTRA_REF.get(e) or '—'} |")
    L.append(""); L.append("## 2. Địa điểm (LOC) — số SC")
    L.append("| LOC | SC | Sub-lock (SC) |"); L.append("|---|---|---|")
    for l, n in sorted(cnt_loc.items()):
        subs = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_sub.items()) if k.startswith(l) or (k.startswith("KB_") and SUBLOC[k][0] == l))
        L.append(f"| {l} | {n} | {subs} |")
    L.append(""); L.append("## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/EQP) — số SC")
    L.append("| ID | SC | ghi chú |"); L.append("|---|---|---|")
    vnote = {"VEH_001": "K2 damage 4 pha (VEH_STATE k2_reeds → after_fire → arrows → running → stalled → burning → sunk → wreck); SC_281–284 đính `VEH_001_ep5`",
             "VEH_002": "천둥 3 bị thu: `VEH_002_captured` + k21_captured/k21_road", "VEH_207": "kỵ Tùy v3 — 우중문 ngựa đen (v207_black), 우문술 ngựa xám (v207_grey), 후군 장수 ngựa hung; KHÔNG đính VEH_205",
             "VEH_101": "개마무사 — kỵ thật; 'giáo 삭' của 창병 → EXTRA GOG_SPEARMEN + WPN_102_ref (không đính VEH_101)", "VEH_206": "kỵ Tiên Ti ngựa bịt tai (v206_ears/v206_water)", "VEH_205": "chỉ SC_273 (cầu phao 요하)"}
    for v, n in cnt_veh.most_common(): L.append(f"| {v} | {n} | {vnote.get(v, '')} |")
    L.append(""); L.append("## 4. Đạo cụ (PROP) — số SC")
    L.append("| PROP | SC | ghi chú |"); L.append("|---|---|---|")
    pnote = {"PROP_024": "cờ đỏ hiệu lệnh — cuộn (SC_004–184) / bung (SC_066+, VISUAL_LOCK_EN_OPEN dán trong Action)", "PROP_025": "nhiệt nhôm — túi ngực (SC_161) → khay nạp (SC_189) → cài áo (SC_213) → thả (SC_224)",
             "PROP_023": "biển '3' — ba lô (P1–P8) → túi ngực (SC_168) → mép tháp K2 cạnh số 1 (SC_282)", "PROP_018": "tù và 3 hồi = hiệu lệnh (SC_076/208) — không ref bible → PROP_018_ref (dup ep4)",
             "SILK_MAP": "**LOCK_PENDING** bản đồ lụa 을지문덕 (script tag PROP_001)", "SMALL_CROW_PENNANT": "**LOCK_PENDING** cờ hiệu nhỏ (script tag PROP_012)", "PROP_026": "nút bầu — không ref (cận cảnh)"}
    for p, n in cnt_prop.most_common(): L.append(f"| {p} | {n} | {pnote.get(p, '')} |")
    L.append(""); L.append("## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)")
    L.append("| # | ref id | thư mục | số SC đính | trạng thái |"); L.append("|---|---|---|---|---|")
    for i, (r, n) in enumerate(cnt_ref.most_common(), 1):
        status = ("**CHƯA CÓ — job trong ref_jobs_ep5_extra.json**" + (" (trùng ep4 extra — chạy 1 lần)" if r in EP4_EXTRA else "")) if r in NEW_REFS else "có job"
        L.append(f"| {i} | {r} | {REF_DIR[r]} | {n} | {status} |")
    L.append("")
    L.append("### Ref CHƯA CÓ (job: `05_references/extra/ref_jobs_ep5_extra.json` — glabs-operator tạo trước lô ảnh cảnh)")
    for rid, meta in REF_JOBS_META.items():
        L.append(f"- `{rid}` ({REF_DIR[rid]}, {meta['ar']}): {meta['vi']}")
    L.append("")
    L.append("### Thứ tự chạy ref đề xuất (P1 → P3)")
    L.append("- **P1 (≥15 SC):** " + ", ".join(r for r, n in cnt_ref.most_common() if n >= 15))
    L.append("- **P2 (5–14 SC):** " + ", ".join(r for r, n in cnt_ref.most_common() if 5 <= n < 15))
    L.append("- **P3 (<5 SC):** " + ", ".join(r for r, n in cnt_ref.most_common() if n < 5))
    L.append("")
    L.append("## 6. SC cần ảnh ĐẠI QUÂN / AERIAL / CLIMAX (⚑ → ảnh nano_banana_pro + upscale 2K; video veo_31_quality)")
    aer = [r for r in recs if r["aerial_quality"]]
    L.append("| SC | t | type | aerial | nội dung |"); L.append("|---|---|---|---|---|")
    for r in aer: L.append(f"| {r['id']} | {r['t_start']//60}:{r['t_start']%60:02d} | {r['type']} | {'aerial' if r['aerial'] else 'climax'} | {r['shot']} |")
    L.append("")
    L.append("## 7. OVERLAY ở edit (chữ/số KHÔNG vẽ trong ảnh) + END CARD")
    L.append("| SC | overlay |"); L.append("|---|---|")
    for r in recs:
        if r["overlay_text"]: L.append(f"| {r['id']} | {r['overlay_text']} |")
    L.append("")
    L.append("## 8. 2-BEAT / INSERT_CLIP (clip tách riêng 3–4 s, ghép ở edit)")
    L.append("| SC | 2-beat | insert (s) | nội dung insert |"); L.append("|---|---|---|---|")
    for r in recs:
        if r["two_beat"] or r["insert_clip"]:
            L.append(f"| {r['id']} | {'yes' if r['two_beat'] else ''} | {r['insert_clip']['seconds'] if r['insert_clip'] else '—'} | {(r['insert_clip']['prompt'][:170] + '…') if r['insert_clip'] else 'beat A/B trong 1 clip (cùng góc máy)'} |")
    L.append("")
    L.append("## 9. CHAIN_FROM (tail-frame → start_image)")
    L.append(", ".join(f"{r['chain_from'][3:]}→{r['id'][3:]}" for r in recs if r["chain_from"]))
    L.append("")
    L.append("## 10. SC RỦI RO AI & cách né trong prompt")
    risk = [r for r in recs if r["ai_risk"]]
    L.append("| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |"); L.append("|---|---|---|")
    for r in risk: L.append(f"| {r['id']} | {r['ai_risk'].split('→')[0].strip()} | {r['ai_risk'].split('→')[1].strip() if '→' in r['ai_risk'] else '—'} |")
    L.append("")
    L.append("### Quy tắc né chung (áp dụng toàn tập)")
    L.append("- **Đại quân trong nước** (방진 30만, trung quân ngang ngực): luôn aerial/wide, 'heads and shields in brown water', mặt phụ quay đi; không cận đám đông; số ngựa ≤3 khi cận.")
    L.append("- **K2 + nước/dầu/lửa** (SC_205–227, 244–251): 1 hành động vật lý rõ mỗi clip (sóng bùn / xích lún / dầu loang / khói trắng / vòng lửa), máy tĩnh hoặc 1 chuyển động; VEH_STATE đúng pha; không vẽ chữ trên tháp ngoài số 1.")
    L.append("- **Nội thất K2** (tháp/khoang lái): sub-lock `_k2_turret_int`/`_k2_driver_int` + ref `VEH_001_interior_ref`; màn hình 'small blank readout' — số 잔탄 overlay.")
    L.append("- **Chữ/số**: bản đồ lụa (brush strokes, no writing), sổ tay (blurred pencil lines), bài thơ (columns of brush calligraphy), biển '3' (chỉ số Ả Rập), end card → overlay.")
    L.append("- **Tay cầm súng/cung**: K2C1 gác bao cát/lau, bắn = chớp lửa hoặc wide; K5 hai tay (SC_137–138) máy vai, không cận ngón tay trên cò; cung 탁발흠/해모루 (SC_245/248) cận mặt + dây cung tới má, tay run mô tả bằng 'trembling'.")
    L.append("- **Ngựa Tùy vs Tiên Ti vs Goguryeo**: VEH_207 (lụa đỏ, gương ngực, ngựa cao) / VEH_206 (ngựa lùn, da nâu, lông cáo, tai nhét vải) / VEH_101 (giáp sắt kín) — QC loại plate armor phương Tây (vehicle_bible C.5).")
    L.append("- **Vết thương**: 해모루 cán tên dưới xương đòn TRÁI (bible), 박기철 tên đùi TRÁI (bible/ref — script ghi bắp chân phải → cần quyết), 탁발흠 băng cẳng tay PHẢI; không gore, không cận vết thương hở.")
    L.append("- **Hangul trên xe**: KHÔNG vẽ; '천둥' chỉ ở thoại/radio.")
    L.append("- **Nhân vật lịch sử**: diện mạo hư cấu theo lock; 수 후군 장수 (신세웅) = EXTRA lock tạm, không ref (P-44).")
    open(f"{OUT_DIR}/ep{EP}_asset_usage.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

REF_JOBS_META = {
    "LOC_007_k2_reeds_ep5": dict(ar="16:9", vi="K2 trát bùn cắm lau ở mép bãi lau bờ bắc cách cổng họng 300 m (P1–P9) — sub-lock `LOC_007_k2_reeds`/`_k2_reeds_flat`/`_south_edge`/`_mortar_pit` (≈80 SC)."),
    "LOC_007_throat_ep5": dict(ar="16:9", vi="cổng họng bãi (여울 목): khe 60 m nước ngang ngực giữa bãi lau (tây) và bờ bùn dốc (đông), cọc gỗ nghiêng, KHÔNG có xe — sub-lock `LOC_007_throat`/`_throat_k2`/`_k2_roof`/`_mud_bank`/`_throat_rim` (P10 ≈45 SC)."),
    "LOC_007_north_line_ep5": dict(ar="16:9", vi="tuyến bắc: mép lau gặp bãi cát bắc, hố bao cát nối nhau, K6 giá ba chân phủ lau — sub-lock `LOC_007_north_line`/`_east_shore`/`_north_flat_edge`."),
    "LOC_007_south_knoll_ep5": dict(ar="16:9", vi="gò nam: cỏ ướt, vài cây thông ngả gió, nhìn xuống sông đầy quân — sub-lock `LOC_007_south_knoll` (v3 nguyên văn; 12 SC 을지문덕/cờ đỏ/나각)."),
    "LOC_007_north_hill_ep5": dict(ar="16:9", vi="bãi cát bắc → đồi thấp bắc trong mưa, lau thấp chân đồi (2.000 kỵ Tiên Ti) — sub-lock `LOC_007_north_flat` (v3)/`_north_hill_foot`/`_east_hill`."),
    "LOC_007_small_bar_ep5": dict(ar="16:9", vi="mô cát nhỏ cạnh cổng họng, xác ngựa Tùy, tên gãy, cờ đỏ ngã — sub-lock `LOC_007_small_bar` (v3)/`_small_bar_sun` (Phase 3–5, P11 ≈16 SC)."),
    "LOC_007_mid_bar_ep5": dict(ar="16:9", vi="mô cát giữa sông đầy lính Tùy + cụm cờ quanh tướng cưỡi ngựa, cát lở — sub-lock `LOC_007_mid_bar` (v3, SC_063–064/079/081/087/098/192/236)."),
    "LOC_007_upstream_bar_ep5": dict(ar="16:9", vi="mô cát thượng lưu 1,5 km đông, nước tới bụng ngựa, kỵ Goguryeo hàng một — sub-lock `LOC_007_upstream_bar` (v3)."),
    "LOC_007_aid_ep5": dict(ar="16:9", vi="trạm cứu thương sâu trong lau: chiếu lau hàng, mái lau, bát thuốc, băng — sub-lock `LOC_007_aid`/`_west_reeds`."),
    "LOC_007_aftermath_ep5": dict(ar="16:9", vi="D+10 nước rút, nắng: bãi cát khô nứt, lạch nông, xác K2 cháy nghiêng — sub-lock `LOC_007_aftermath` (v3; SC_281–284). Khác `LOC_007_finale_light` (còn nước lũ)."),
    "LOC_004_yard_rain_ep5": dict(ar="16:9", vi="sân 육합성 mưa D+5: cỗ xe gỗ khổng lồ lún bùn chở K21 phủ vải dầu, cờ Tùy — sub-lock `LOC_004_yard_rain` (SC_270–272)."),
    "LOC_001_road_west_ep5": dict(ar="16:9", vi="đường đất lầy về tây trong mưa, xe bò 40 con kéo cỗ xe khổng lồ — sub-lock `LOC_001_road_west`/`_cart_bench` (SC_286–287)."),
    "VEH_001_interior_ref": dict(ar="16:9", vi="nội thất K2 (2 panel: ghế trưởng xe + thị kính + khay máy nạp + màn hình trống · khoang lái yoke + kính tiềm vọng) — 12 SC trong xe; né drift nội thất."),
    "PROP_018_ref": dict(ar="16:9", vi="tù và sừng trâu đen ~50 cm, miệng đồng, dây da — hiệu lệnh 3 hồi (SC_076/208) + 해모루 (trùng đề xuất ep4 extra → chạy 1 lần)."),
    "PROP_023_ref": dict(ar="16:9", vi="biển thép ô-liu 10×25 cm số '3' trắng trầy, 2 lỗ bu-lông, mép cháy sém (SC_168/282 cận) — không Hangul."),
    "EXTRA_silk_map_ref": dict(ar="16:9", vi="**LOCK_PENDING** bản đồ lụa 을지문덕 vẽ mực (sông cong, cọc, mô cát, lau tô dày, đồi vảy, chấm son đỏ) — 4 still KB (SC_012/014/029/107)."),
    "EXTRA_gog_deputy_ref": dict(ar="3:4", vi="고구려 부장 (~45, râu ngắn đen, giáp dây đỏ, chỏm lông đen) — 9 SC thấy mặt (P2, P6, P7, P9, P10, P11)."),
    "EXTRA_gog_young_rider_ref": dict(ar="3:4", vi="고구려 전령 trẻ (~20, không râu, chỏm lông đỏ, ngựa hạt dẻ giáp) — SC_117/172/184."),
    "EXTRA_k2_driver_ref": dict(ar="3:4", vi="조종수 K2 phối thuộc (~28, mặt vuông, mũ crew) — SC_139/140 trúng tên vai phải."),
}

def write_sublocks(recs):
    cnt_sub = collections.Counter(r["subloc"] for r in recs)
    sc_by_sub = collections.defaultdict(list)
    for r in recs: sc_by_sub[r["subloc"]].append(r["id"][3:])
    L = ["# 살수 612 — SUB-LOCK ĐỊA ĐIỂM 5화 (veo-prompt-engineer · 2026-09-16 · chờ DUYỆT như 1화/4화)",
         "> Mỗi sub-lock = 1 đoạn VISUAL_LOCK_EN cố định cho một khu vực/buổi của LOC gốc; đã dán NGUYÊN VĂN vào mọi SC tương ứng trong `04_veo/scene_list_ep5.md`. `(v3)` = nguyên văn `continuity_master.sublocks` / location_bible v3 (8 sub-địa hình LOC_007 5화 + LOC_006_hall + LOC_004_pavilion_int); `(mới)` = veo-prompt-engineer đặt cho 5화 → world-designer nhập vào location_bible dưới mục `REF_PROMPT_EN_<subarea>`. Nguồn máy: `logs/scratch/veo-ep5/build.py` SUBLOC.",
         "> Quy tắc dùng: aerial 3 pha → `LOC_007` (lock gốc) / `LOC_007_dawn_aerial`; medium/cận → sub-lock khu vực; luôn thêm câu Light theo 3 pha (dawn_grey → day_rain → sun_tearing/sun_afternoon/sun_clear); kết bằng style tag §D. Ref đính `*_ep5` = ref mới (ref_jobs_ep5_extra.json).", "",
         "| # | id sub-lock | LOC gốc | Ref đính | SC 5화 | VISUAL_LOCK_EN (nguyên văn) |", "|---|---|---|---|---|---|"]
    i = 0
    v3 = set(CM_SUB.keys()) | {"LOC_007", "LOC_005"}
    for k, (loc, ref, txt) in SUBLOC.items():
        if not cnt_sub.get(k): continue
        i += 1
        tag = " (v3)" if k in v3 else " (mới)"
        ids = sc_by_sub[k]
        idtxt = f"{len(ids)} SC: " + ", ".join(ids[:14]) + ("…" if len(ids) > 14 else "")
        L.append(f"| {i} | `{k}`{tag} | {loc} | `{ref or '—'}` | {idtxt} | {txt} |")
    L.append(""); L.append("## Ref mới cần tạo (job: `05_references/extra/ref_jobs_ep5_extra.json`)")
    L.append("| ref id | dùng cho | số SC đính | priority |"); L.append("|---|---|---|---|")
    cnt_ref = collections.Counter(x for r in recs for x in r["refs"])
    for rid in NEW_REFS:
        n = cnt_ref.get(rid, 0)
        L.append(f"| `{rid}` | {REF_JOBS_META[rid]['vi'].split(' — ')[0][:100]} | {n} | {'P1' if n >= 15 else ('P2' if n >= 5 else 'P3')} |")
    L.append(""); L.append("## Ghi chú")
    L.append("- `LOC_007_throat` / `_throat_k2` (v3): ref mới `LOC_007_throat_ep5` (khe trống, không xe) — K2 chắn khe do VEH_001 lock + VEH_STATE `k2_stalled`/`k2_burning` dán sau; bible ghi ref `LOC_007_wide + K2_ep5` → veo dùng ref khe riêng để ảnh cận chính xác hơn.")
    L.append("- `LOC_007_aftermath` (v3): bible đính `LOC_007_finale_light` (còn nước lũ, mưa một bên) — 5화 SC_281–284 là D+10 nước rút, cát khô nứt → ref mới `LOC_007_aftermath_ep5`; `LOC_007_finale_light` dùng cho Phase 6/P11 (`_ford_sun`, `_north_flat_sun`, `_east_shore_sun`, `_throat_sun`).")
    L.append("- `LOC_007_north_flat` (v3, 'dark mass of steppe horsemen on the hill crest') chỉ dùng khi kỵ Tiên Ti còn trên đồi (P6–P7); bãi cát bắc sau khi kỵ xuống → `_north_flat_edge`.")
    L.append("- Nội thất K2 (`_k2_turret_int`, `_k2_driver_int`) là sub-lock của LOC_007 (xe đứng trong bãi lau/khe) — ref `VEH_001_interior_ref` (vehicles).")
    L.append("- `KB_silk_map` / `KB_notebook` / `KB_sand_plan` / `KB_poem`: still cận đạo cụ, không ref địa điểm; bản đồ lụa đính `EXTRA_silk_map_ref` (LOCK_PENDING).")
    L.append("- `LOC_004_jiangdu_618` (SC_275, KB 618 강도): điện Tùy phương nam — dùng ref `LOC_004_detail` (cột son, rèm lụa) vì không có LOC riêng; đề xuất không tạo LOC mới (1 still).")
    L.append("- `LOC_002_siege_613` (SC_274, KB 613): dùng ref `LOC_002_wide` + VEH_201_ref; 1 still.")
    L.append("- `LOC_005_south_bank` (SC_252 truy kích 압록 [史]): ref `LOC_005_wide` (bible) — không tạo ref mới (1 SC).")
    open(f"{PROJ}/02_script/sublocks_ep{EP}.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

def write_ref_jobs(recs):
    cnt_ref = collections.Counter(x for r in recs for x in r["refs"])
    tail_loc = ", no people in frame, no modern structures, " + STYLE
    tail_char = " Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look"
    def sub(k): return SUBLOC[k][2]
    P = {
        "LOC_007_k2_reeds_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_k2_reeds") + ". " + VEH_STATE["k2_reeds"] + " " + LIGHT["day_rain"] + tail_loc.replace("no modern structures", "no modern structures other than the tank"),
        "LOC_007_throat_ep5": "Wide establishing reference shot from the reed edge, 16:9. " + sub("LOC_007_throat") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_north_line_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_north_line") + ". " + LIGHT["day_rain"] + tail_loc.replace("no modern structures", "no modern structures other than the sandbags and the tripod machine gun"),
        "LOC_007_south_knoll_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_south_knoll").replace("Goguryeo armored guards and a banner bearer, ", "") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_north_hill_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_north_flat").replace("a dark mass of steppe horsemen on the hill crest, ", "") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_small_bar_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_small_bar") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_mid_bar_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_mid_bar").replace("crowded with Sui soldiers in mingguang armor and a cluster of tall red and yellow banners around mounted generals, ", "empty, ") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_upstream_bar_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_upstream_bar").replace("Goguryeo cataphracts wading in a long file, ", "") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_aid_ep5": "Interior-style establishing reference shot, 16:9. " + sub("LOC_007_aid") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_aftermath_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_007_aftermath") + ". " + LIGHT["sun_clear"] + tail_loc.replace("no modern structures", "no modern structures other than the burned tank"),
        "LOC_004_yard_rain_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_004_yard_rain") + ". " + LIGHT["day_rain_yukhap"] + tail_loc.replace("no modern structures", "no modern structures other than the covered vehicle"),
        "LOC_001_road_west_ep5": "Wide establishing reference shot, 16:9. " + sub("LOC_001_road_west") + ". " + LIGHT["day_rain"] + tail_loc,
        "VEH_001_interior_ref": "Reference sheet, two panels side by side on one 16:9 image. Left panel: " + sub("LOC_007_k2_turret_int") + ". Right panel: " + sub("LOC_007_k2_driver_int") + ". Cold blue screen glow and grey daylight, no people, no readable text, " + STYLE,
        "PROP_018_ref": "Product-style reference photo of a Goguryeo signal horn, three-quarter view: " + LOCKS["PROP_018"] + ", pure white background, even studio lighting, " + STYLE,
        "PROP_023_ref": "Product-style reference photo, three-quarter view: " + LOCKS["PROP_023"].replace(", tied to a backpack strap with paracord", "") + ", about ten by twenty-five centimeters, a loop of black paracord through one bolt hole, dried mud in the scratches, pure white background, even studio lighting, " + STYLE,
        "EXTRA_silk_map_ref": "Product-style reference photo laid flat, top-down, 16:9: " + EXTRA_PROPS["SILK_MAP"] + ", ivory silk with frayed edges, pure white background, even studio lighting, " + STYLE,
        "EXTRA_gog_deputy_ref": "Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. " + EXTRAS["GOG_DEPUTY"][2:].capitalize().replace(", soaked with rain", "") + "." + tail_char,
        "EXTRA_gog_young_rider_ref": "Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. A young Goguryeo cavalryman around 20, thin face, no beard, black topknot, iron lamellar armor over a brown jacket, iron helmet with a red plume, ring-pommel sword." + tail_char,
        "EXTRA_k2_driver_ref": "Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. A ROK Army tank driver around 28, square face, short black hair, granite-pattern digital camo uniform, body armor, crew helmet with boom microphone held under one arm, Korean flag patch on right shoulder, corporal's rank." + tail_char,
    }
    jobs = []
    for rid in NEW_REFS:
        n = cnt_ref.get(rid, 0)
        jobs.append({"id": rid, "type": "image", "priority": 1 if n >= 15 else (2 if n >= 5 else 3), "sc_count": n,
                     "out_dir": f"05_references/{NEW_REFS[rid]}", "used_by": REF_JOBS_META[rid]["vi"].split(" — ")[0][:120],
                     "lock_pending": rid == "EXTRA_silk_map_ref", "dup_ep4_extra": rid in EP4_EXTRA,
                     "body": {"prompt": P[rid], "model": "nano_banana_pro", "aspect_ratio": REF_JOBS_META[rid]["ar"]}})
    jobs.sort(key=lambda j: (j["priority"], -j["sc_count"]))
    json.dump(jobs, open(f"{PROJ}/05_references/extra/ref_jobs_ep{EP}_extra.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
