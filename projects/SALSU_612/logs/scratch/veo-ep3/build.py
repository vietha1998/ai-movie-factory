# -*- coding: utf-8 -*-
"""
VEO scene-list builder — SALSU_612 · 3화 「남하」 (copy từ veo-ep1/build.py, sửa cho tập 3)
Đọc: full_script_ep3.md v2 (t / type / narration / thoại / [SOUND] — nguyên văn) + continuity_master.json v3 (VISUAL_LOCK nguyên văn)
      + batch_XX.py (dữ liệu hình ảnh do veo-prompt-engineer biên).
Ghi: 04_veo/scene_list_ep3.md · 04_veo/scenes_ep3.json · 04_veo/ep3_asset_usage.md · output/ep3/kich_ban/scene_list.md
     · 02_script/sublocks_ep3.md · 05_references/extra/ref_jobs_ep3_extra.json
"""
import json, re, os, sys, glob, importlib.util, collections

ROOT = "/Users/admin/phim han quoc"
PROJ = ROOT + "/projects/SALSU_612"
SCRIPT = PROJ + "/02_script/full_script_ep3.md"
CM = json.load(open(PROJ + "/continuity_master.json", encoding="utf-8"))
OUT_DIR = PROJ + "/04_veo"
HERE = os.path.dirname(os.path.abspath(__file__))
EP = 3
N_SC = 287

STYLE = CM["style_tag"]
NEGATIVE = ("cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, "
            "modern buildings in historical scene, anachronistic clothing")

# ---------------------------------------------------------------- LOCKS (nguyên văn continuity_master.json v3)
LOCKS = {}
LOCKS.update(CM["character_locks"]); LOCKS.update(CM["vehicle_locks"]); LOCKS.update(CM["prop_locks"])
LOCKS["PROP_004"] = CM["vehicle_locks"]["EQP_001"]
LOC_LOCK = {k.split("_")[0] + "_" + k.split("_")[1]: v for k, v in CM["location_locks"].items()}
CM_SUB = CM.get("sublocks", {})
CM_DERIVED = CM.get("derived_states", {})

# ---------------------------------------------------------------- REF SHEET IDS (05_references/*/ref_jobs.json + ep1 extra) + refs CẦN TẠO 3화
REF_DIR = {}
for d in ("characters", "locations", "vehicles", "props"):
    for j in json.load(open(f"{PROJ}/05_references/{d}/ref_jobs.json", encoding="utf-8")):
        REF_DIR[j["id"]] = d
for j in json.load(open(f"{PROJ}/05_references/extra/ref_jobs_ep1_extra.json", encoding="utf-8")):
    REF_DIR[j["id"]] = j["out_dir"].split("/")[-1]
NEW_REFS = {  # 3화 — chưa có job → 05_references/extra/ref_jobs_ep3_extra.json (xem ep3_asset_usage.md §5)
    "LOC_003_valley_fire_ep3": "locations", "LOC_001_plain_rain_ep3": "locations",
    "LOC_008_mountain_road_ep3": "locations", "LOC_008_hill_fort_ep3": "locations",
    "LOC_005_south_hill_ep3": "locations", "LOC_005_sui_tent_ep3": "locations",
    "LOC_009_saddle_night_ep3": "locations", "LOC_009_outcrop_ep3": "locations", "LOC_009_xianbei_camp_ep3": "locations",
    "VEH_001_mule_ep3": "vehicles", "EXTRA_xianbei_deputy_ref": "characters",
}
REF_DIR.update(NEW_REFS)

def ref_path(rid):
    return f"projects/SALSU_612/05_references/{REF_DIR[rid]}/{rid}_1.png"

def cm_state(k):
    return CM_DERIVED[k]["prompt_add"]

# ---------------------------------------------------------------- DERIVED STATES (continuity_master v3 derived_states — NGUYÊN VĂN; ✔ = ref riêng đã có job)
DERIVED = {
    # ---- ✔ 3화 (continuity_master.derived_states, ref = job)
    "CHAR_001_rain_ep3": ("CHAR_001", "CHAR_001_rain_ep3", cm_state("CHAR_001_rain_ep3")),
    "CHAR_002_k3_rain_ep3": ("CHAR_002", "CHAR_002_k3_rain_ep3", cm_state("CHAR_002_k3_rain_ep3")),
    "CHAR_003_rain_ep3": ("CHAR_003", "CHAR_003_rain_ep3", cm_state("CHAR_003_rain_ep3")),
    "CHAR_005_captive_ep3": ("CHAR_005", "CHAR_005_captive_ep3", cm_state("CHAR_005_captive_ep3")),
    "CHAR_101_false_surrender_ep3": ("CHAR_101", "CHAR_101_false_surrender_ep3", cm_state("CHAR_101_false_surrender_ep3")),
    "CHAR_101_hall_seated_ep4": ("CHAR_101", "CHAR_101_hall_seated_ep4", cm_state("CHAR_101_hall_seated_ep4")),  # bible: dùng cho 3화 D11 lều
    "CHAR_105_plain_robe_ep3": ("CHAR_105", "CHAR_105_plain_robe_ep3", cm_state("CHAR_105_plain_robe_ep3")),
    "CHAR_105_radio_ep3": ("CHAR_105", "CHAR_105_radio_ep3", cm_state("CHAR_105_radio_ep3")),
    "CHAR_106_rain_south_ep3": ("CHAR_106", "CHAR_106_rain_south_ep3", cm_state("CHAR_106_rain_south_ep3")),
    "CHAR_106_forge_ep2": ("CHAR_106", "CHAR_106_forge_ep2", cm_state("CHAR_106_forge_ep2")),  # bible: 3화 D12–D13 lò rèn
    "CHAR_201_robe_only_ep3": ("CHAR_201", "CHAR_201_robe_only_ep3", cm_state("CHAR_201_robe_only_ep3")),
    "CHAR_202_tent_ep4": ("CHAR_202", "CHAR_202_tent_ep4", cm_state("CHAR_202_tent_ep4")),  # bible: 3화 D9–D10 lều
    "CHAR_205_nvg_ep3": ("CHAR_205", "CHAR_205_nvg_ep3", cm_state("CHAR_205_nvg_ep3")),
    # ---- ✔ ref riêng tập trước, dùng lại đúng bible
    "CHAR_001_dusty_ep2": ("CHAR_001", "CHAR_001_dusty_ep2", cm_state("CHAR_001_dusty_ep2")),
    "CHAR_002_soot_ep2": ("CHAR_002", "CHAR_002_soot_ep2", cm_state("CHAR_002_soot_ep2")),
    "CHAR_003_hands_bandaged_ep2": ("CHAR_003", "CHAR_003_hands_bandaged_ep2", cm_state("CHAR_003_hands_bandaged_ep2")),
    "CHAR_107_scarf_ep2": ("CHAR_107", "CHAR_107_scarf_ep2", cm_state("CHAR_107_scarf_ep2")),
    # ---- prompt_only (continuity_master ref = prompt_only → đính ref gốc / ref biến thể gần nhất)
    "CHAR_107_scarf_burnt_ep3": ("CHAR_107", "CHAR_107_scarf_ep2", cm_state("CHAR_107_scarf_burnt_ep3")),
    "CHAR_205_magazine_ep2": ("CHAR_205", "CHAR_205_ref", cm_state("CHAR_205_magazine_ep2")),
    "CHAR_203_tent_ep4": ("CHAR_203", "CHAR_203_ref", cm_state("CHAR_203_tent_ep4")),
    # ---- 3화 in-episode states do veo-prompt-engineer đặt theo bảng "Trạng thái theo tập" 3화 (character_bible) + [ACTION-VI] — đề xuất character-designer nhập bible
    "CHAR_001_valley_ep3": ("CHAR_001", "CHAR_001_dusty_ep2",
        cm_state("CHAR_001_dusty_ep2") + " The shaft of a Goguryeo arrow protruding from the left chest pocket."),
    "CHAR_001_helmet_ep3": ("CHAR_001", "CHAR_001_rain_ep3",
        cm_state("CHAR_001_rain_ep3") + " A second empty combat helmet with a bare night-vision mount held in the left hand."),
    "CHAR_002_rain_ep3": ("CHAR_002", "CHAR_002_ref",
        "Helmet on with wet cover, rain-soaked uniform, mud to the knees, four-day stubble, right sleeve scorched at the cuff, goggles on the helmet fogged with water."),
    "CHAR_003_valley_ep3": ("CHAR_003", "CHAR_003_hands_bandaged_ep2",
        "Both hands wrapped in dirty white field bandages, no gloves, left eyebrow half singed, soot-streaked tired face, patrol cap, red rag in belt."),
    "CHAR_003_valley_plate_ep3": ("CHAR_003", "CHAR_003_hands_bandaged_ep2",
        "Both hands wrapped in dirty white field bandages, no gloves, left eyebrow half singed, soot-streaked tired face, patrol cap, red rag in belt, a small olive-drab steel vehicle nameplate with a white numeral 3 tied to his backpack strap."),
    "CHAR_004_rain_ep3": ("CHAR_004", "CHAR_004_ref",
        "Helmet on with wet cover, rain-soaked uniform, mud to the knees, hair bun tight, blue nitrile gloves, a small brown hemp herb pouch tied at the belt, medic bag on the shoulder."),
    "CHAR_004_pass_ep3": ("CHAR_004", "CHAR_004_ref",
        "Helmet on with wet cover, rain-soaked uniform, mud to the knees, dried blood on both forearms to the elbows and on the nitrile gloves, a small brown hemp herb pouch tied at the belt, medic bag on the shoulder, pale tired face."),
    "CHAR_005_rain_ep3": ("CHAR_005", "CHAR_005_ref",
        "Helmet on with wet cover, rain-soaked uniform, mud to the knees, faint stubble, the drone controller on the chest harness under a clear rain cover, hard olive drone case on the back."),
    "CHAR_005_valley_ep3": ("CHAR_005", "CHAR_005_ref",
        "Ash and soot on face and uniform, one corner of the hard drone case on his back scorched black, red-rimmed eyes."),
    "CHAR_005_nvg_ep3": ("CHAR_005", "CHAR_005_ref",
        "Helmet on with wet cover and a night-vision monocular flipped up on the helmet mount, rain-soaked uniform, mud to the knees, faint stubble, the drone controller on the chest harness, hard olive drone case on the back, a rope tied around the waist."),
    "CHAR_005_stripped_ep3": ("CHAR_005", "CHAR_005_captive_ep3",
        "No helmet, no body armor, no boots, torn dirty camo uniform and socks, the small Korean flag patch still on the right shoulder, hands bound behind the back with hemp rope, mud on face, frightened."),
    "CHAR_005_captive_patch_ep3": ("CHAR_005", "CHAR_005_captive_ep3",
        "Prisoner: no helmet, no body armor, no boots, torn dirty camo uniform and socks, the small Korean flag patch still sewn on the right shoulder, hands bound behind the back with hemp rope, split lip, bruised swollen left eye, hair hacked short unevenly, mud on face, frightened but defiant."),
    "CHAR_006_valley_ep3": ("CHAR_006", "CHAR_006_ref",
        "Grey stone dust and soot on the boonie hat and shoulders, a night-vision monocular flipped up on a cord over the hat brim, two-day stubble, no face paint."),
    "CHAR_006_rain_ep3": ("CHAR_006", "CHAR_006_ref",
        "Boonie hat soaked with the brim drooping, rain-soaked uniform, wet mud over chest, knees and forearms, five-day stubble, no face paint."),
    "CHAR_006_nvg_ep3": ("CHAR_006", "CHAR_006_ref",
        "Boonie hat soaked with the brim drooping, a night-vision monocular strapped to the front of the hat with cord over the right eye, rain-soaked uniform, wet mud over chest, knees and forearms, five-day stubble, no face paint."),
    "CHAR_006_bare_hands_ep3": ("CHAR_006", "CHAR_006_ref",
        "Boonie hat soaked, no night-vision device, rain-soaked uniform, wet mud over chest and knees, bare hands scraped and bleeding at the knuckles, five-day stubble, no face paint."),
    "CHAR_101_rain_armor_ep3": ("CHAR_101", "CHAR_101_ref",
        "Armor, plume and feathers darkened with rain, water beading on the lamellar plates and running down the short silver beard, mud on boots."),
    "CHAR_105_rain_ep3": ("CHAR_105", "CHAR_105_ref",
        "Rain-soaked armor and jacket, wet feather, mud on boots and skirt, no radio."),
    "CHAR_105_radio_helmet_off_ep3": ("CHAR_105", "CHAR_105_radio_ep3",
        cm_state("CHAR_105_radio_ep3") + " Iron helmet held under the left arm, black topknot bare, head bowed."),
    "CHAR_105_radio_wet_ep3": ("CHAR_105", "CHAR_105_radio_ep3",
        cm_state("CHAR_105_radio_ep3") + " Soaked to the skin after two nights of riding, water streaming from the armor, a bamboo tally tied with red cord in one hand."),
    "CHAR_106_valley_ep3": ("CHAR_106", "CHAR_106_rain_south_ep3",
        "Coarse hemp cloak over the jacket, walking staff, tool roll on the back, mud on sandals, soot smudges from the burning vehicles on the cloak."),
    "CHAR_107_rain_ep3": ("CHAR_107", "CHAR_107_scarf_ep2",
        cm_state("CHAR_107_scarf_ep2") + " Rain-damp braids stuck to the cheeks, mud on the hem of the skirt, a coarse hemp cloak over the shoulders."),
    "CHAR_202_camp_chair_ep3": ("CHAR_202", "CHAR_202_ref",
        "Seated on a folding wooden camp chair, helmet on, the red silk cloak damp at the hem, wet planks underfoot."),
    "CHAR_202_horse_rain_ep3": ("CHAR_202", "CHAR_202_ref",
        "Mounted on a tall war horse with a red silk caparison, the red cloak soaked dark and heavy with rain, straight sword drawn."),
    "CHAR_202_road_tent_ep3": ("CHAR_202", "CHAR_202_ref",
        "Helmet off showing the white topknot, red silk cloak soaked dark with rain, beard wet, mud on the boots."),
    "CHAR_203_rain_ep3": ("CHAR_203", "CHAR_203_ref",
        "Plain dark armor beaded with rain, a bundle of bamboo writing slips in one hand, grey tired face."),
    "CHAR_205_rain_ep3": ("CHAR_205", "CHAR_205_ref",
        "An empty black rifle magazine hanging from a cord on the bronze plaque belt, rain-darkened leather armor, wet fox fur on the cap, mud on boots."),
    "CHAR_205_nvg_hand_ep3": ("CHAR_205", "CHAR_205_ref",
        "An empty black rifle magazine hanging from a cord on the bronze plaque belt, rain-darkened leather armor, mud on boots, a small black night-vision monocular held in both hands."),
    "CHAR_205_nvg_down_ep3": ("CHAR_205", "CHAR_205_nvg_ep3",
        cm_state("CHAR_205_nvg_ep3") + " The monocular swung down over the right eye with a faint green glow at the eyepiece."),
}

# ---------------------------------------------------------------- EXTRAS (không ID trong bible) — lock tạm cố định, dùng NGUYÊN VĂN mọi SC; đề xuất character-designer đưa vào bible
EXTRAS = {
    "BOY_SCOUT": "17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large alert dark eyes, cracked lips, black hair tied under a brown cloth headband beneath a plain leather cap, coarse undyed brown hemp jacket with crossed collar and white border, rain-soaked, wide trousers bound at the ankles, straw sandals, short composite bow on the back, hip quiver, on a small Goguryeo horse",
    "XIANBEI_DEPUTY": "Xianbei deputy commander around 30, stocky, round weathered face, thin moustache, single braid, brown leather lamellar armor over a dark felt coat, fur-trimmed leather cap, composite bow and hip quiver, short curved saber",
    "XIANBEI_RIDERS": "Xianbei horsemen in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, faces turned away or shadowed",
    "XIANBEI_RIDERS_EARS": "Xianbei horsemen in brown leather lamellar armor and fur-trimmed leather caps on short stocky steppe horses whose ears are stuffed with rolled felt and tied with cord across the cheeks, composite bows drawn, riders bent low over the saddles",
    "XIANBEI_TORCHBEARERS": "hundreds of Xianbei horsemen in brown leather lamellar armor and fur-trimmed leather caps carrying burning pitch torches, strung out in a single file down a cliff path, faces lit orange from below",
    "XIANBEI_CLIMBERS": "Xianbei warriors on foot in brown leather lamellar armor and fur-trimmed leather caps, bows slung on their backs, climbing wet rock hand over hand and sliding down hemp ropes, faces turned to the stone",
    "XIANBEI_ARCHERS_PRONE": "Xianbei archers lying flat on a rock ledge in brown leather lamellar armor and fur-trimmed leather caps, composite bows drawn and aimed downward, faces hidden behind the bows",
    "XIANBEI_WARRIORS_FOOT": "Xianbei warriors on foot in brown leather lamellar armor and fur-trimmed leather caps, short curved sabers and lassos, faces turned away",
    "XIANBEI_CAMP_MEN": "Xianbei warriors around a small campfire in brown leather lamellar armor and fur-trimmed leather caps, faces half lit by the fire and turned away",
    "SUI_ENVOY": "Sui civil official around 50, thin, clean-shaven long face, calm eyes, dark blue silk robe with wide sleeves, black gauze cap with side wings, hands folded in the sleeves",
    "SUI_COURIER": "Sui mounted courier in a grey-blue padded coat under a light iron lamellar vest, black head cloth, a black lacquered bamboo dispatch tube on a cord, coated in mud, kneeling with the tube held up in both hands, face turned down",
    "SUI_CAVALRY_ENVOY": "Sui cavalry officer in mingguang iron lamellar armor with polished round chest plates, pointed iron helmet with a red tassel, a red command pennant, face shadowed by the helmet",
    "SUI_VANGUARD_GENERAL": "Chinese man in his mid-50s, heavy broad build, wide fleshy face with thick black brows, long black beard streaked grey to mid-chest, black topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest, gilt-hilted straight sword",
    "SUI_OFFICER_HORSE": "a mounted Sui officer in iron lamellar armor with a red cloak and a leather whip, face shadowed by an iron helmet",
    "SUI_OFFICER_LANTERN": "a Sui officer in iron lamellar armor and a pointed iron helmet carrying a paper lantern on a short pole, face shadowed",
    "SUI_DESERTER": "Sui deserter in his twenties, gaunt hollow-cheeked face, cracked lips, no armor, a torn grey-blue padded coat soaked through, bare muddy feet, chewing a strip of bark, terrified",
    "SUI_SOLDIER_YOUNG": "young Sui soldier in a grey-blue padded coat under a leather lamellar vest, pointed iron helmet, a grey hemp grain sack tied across the chest, rolled tent and spear on the back, mud to the shins, face straining under the load",
    "SUI_SOLDIERS_STARVING": "Sui soldiers standing in two ragged lines in rain, torn leather lamellar vests over grey-blue padded coats, hollow cheeks, sunken eyes, several leaning on their spears to stay upright, only the two or three nearest faces in focus",
    "SUI_GUARD_STARVING": "a young Sui guard in a grey-blue padded coat and pointed iron helmet with hollow cheeks and cracked lips, hiding a strip of chewed bark in his fist",
    "SUI_GUARDS": "Sui armored guards in mingguang lamellar armor with polished round chest plates and pointed iron helmets standing in two rows with long spears, faces shadowed",
    "SUI_EUNUCH": "Sui court eunuch in a plain grey-blue silk robe and black gauze cap, clean-shaven, head bowed",
    "SUI_MARCHERS": "Sui soldiers in grey-blue padded coats under iron lamellar vests marching in a long column under heavy packs of grey grain sacks, rolled tents and spears, backs bent, faces down",
    "SUI_DIGGERS": "Sui soldiers in grey-blue padded coats crouching in the mud between tents, digging shallow pits with wooden shovels and bare hands, lowering grey hemp grain sacks into them and covering them with earth and straw, faces turned down",
    "SUI_DIGGERS_BANK": "hundreds of Sui soldiers in grey-blue padded coats crouching along a muddy riverbank digging shallow pits, pressing grey hemp grain sacks into them and stamping the earth flat, faces turned down",
    "SUI_VANGUARD_WET": "Sui vanguard infantry in grey-blue padded coats and leather lamellar vests soaked to the chest, pointed iron helmets, long spears and red rectangular shields, forming ragged ranks on wet cobbles, faces turned away",
    "SUI_CROWD_CHARGING": "thousands of Sui soldiers in grey-blue padded coats and pointed iron helmets running in a loose mass with spears and red shields, faces turned away",
    "SUI_SCOUTS_HORSE": "Sui mounted scouts in leather lamellar vests over grey-blue padded coats and pointed iron helmets on tall horses, light spears and small red pennants, faces shadowed",
    "SUI_SCOUTS_FOOT": "two Sui scouts in leather lamellar vests over grey-blue padded coats and pointed iron helmets leading tall horses by the reins, bent over tracks in the mud, faces shadowed",
    "SUI_RAIDERS": "ten Sui horsemen in leather lamellar vests over grey-blue padded coats and pointed iron helmets dismounting in a field, snatching bundles of green millet and throwing grain sacks over their saddles, faces turned away",
    "SUI_ARCHERS_LEDGE": "two Sui scouts in leather lamellar vests and pointed iron helmets crouched on a rock ledge, drawing bows with burning oil-soaked cloth bound behind the arrowheads, faces lit orange",
    "GOG_COURIER": "Goguryeo mounted courier around 25, lean build, soaked through, black topknot under a cloth headband, light leather lamellar vest over a dark brown hemp jacket, kneeling on one knee holding up a bundle of bamboo slips tied with cord",
    "GOG_CAVALRYMEN": "Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants",
    "GOG_CAVALRYMEN_WALKING": "Goguryeo cavalrymen in iron lamellar armor and red-plumed iron helmets walking on foot in rain, leading their armored horses by the reins, faces turned away",
    "GOG_CAVALRYMEN_GRAVE": "Goguryeo cavalrymen in iron lamellar armor with helmets held under their arms, black topknots bare, heads bowed, kneeling to set river cobbles in a ring around a fresh grave mound, faces turned down",
    "GOG_SCOUTS_THREE": "three Goguryeo scouts in light leather lamellar vests over brown hemp jackets and cloth headbands leading small horses down a cliff path, composite bows slung on their backs, unaware",
    "GOG_RIDER_WOUNDED": "a Goguryeo cavalryman with the armor removed lying on a reed mat in a brown jacket, an arrow wound in the thigh being washed, face turned away",
    "GOG_INTERPRETER_CAPTIVE": "Goguryeo prisoner around 35 in a torn undyed hemp jacket, bruised face, cloth headband, wrists bound in front with hemp rope, crouching, speaking with a hoarse tired face",
    "GOG_GATE_GUARD": "Goguryeo gate guard in iron lamellar armor over a brown jacket and an iron plate helmet, lifting a heavy wooden bar from a gate, face turned away",
    "GOG_VILLAGERS": "Goguryeo villagers in undyed hemp jackets and trousers or pleated skirts and cloth headbands standing in doorways and behind wooden fences, children peeking from behind posts, faces turned away",
    "ROK_SOLDIER": "ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim",
    "ROK_SOLDIERS": "ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims",
    "ROK_SOLDIERS_MOUNTED": "ROK Army soldiers in granite-pattern digital camo uniforms, body armor and covered ballistic helmets riding small chestnut Goguryeo horses awkwardly in rain, rifles slung across the saddles, Korean flag patches on right shoulders, faces turned away",
    "ROK_BURNED_HANDS_TWO": "two ROK Army soldiers in granite-pattern digital camo uniforms and covered ballistic helmets walking with both hands wrapped in white bandages to the wrists, no rifles, faces turned away",
    "ROK_RADIOMAN": "young ROK Army radio operator in granite-pattern digital camo uniform, matching body armor, covered ballistic helmet, Korean flag patch on right shoulder, face partly hidden as he bends over a cable",
    "K2_DRIVER": "ROK Army tank driver in granite-pattern digital camo uniform and crew helmet with boom microphone, seen from behind in the driver's hatch, face hidden",
    "K2_GUNNER": "ROK Army tank gunner in granite-pattern digital camo uniform and crew helmet with boom microphone, seen inside a cramped turret pressed to the gunner's sight, face lit only by a screen glow",
    "K3_GUNNER": "ROK Army machine gunner in his early twenties in granite-pattern digital camo uniform, body armor and covered ballistic helmet with a night-vision monocular flipped up on the mount, Korean flag patch on right shoulder, K3 light machine gun in his hands, face turned away or hidden behind the weapon",
    "K3_GUNNER_DEAD": "the body of a young ROK Army machine gunner lying on his side on wet rock in granite-pattern digital camo uniform and body armor, helmet still on, two arrow shafts standing from the shoulder and upper chest, face turned away from the camera",
    "K3_GUNNERS": "ROK Army machine gunners in granite-pattern digital camo uniforms, body armor and covered ballistic helmets prone behind K3 light machine guns on piled stones, faces hidden behind the weapons",
    "PZF_GUNNER": "ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, kneeling with a Panzerfaust 3 launcher on the shoulder, face hidden behind the sight unit",
    "MORTAR_GUNNER": "ROK Army mortar gunner in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, kneeling at the mortar sight, face shadowed by the helmet brim",
    "MORTAR_CREW": "ROK Army mortar crew in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims",
    "ROK_RIFLEMEN_TWO": "two ROK Army riflemen in granite-pattern digital camo uniforms, body armor and covered ballistic helmets without night-vision devices, rifles up, faces turned away",
    "ROK_WOUNDED": "a ROK Army soldier in granite-pattern digital camo uniform lying on his back behind a stone wall with an arrow shaft standing from the shoulder above the body armor, helmet on, face turned away",
    "ROK_WOUNDED_TWO": "two wounded ROK Army soldiers in granite-pattern digital camo uniforms with bandaged shoulders and arms being lifted onto armored Goguryeo horses, helmets on, faces turned away",
    "ROK_SOLDIER_ASLEEP": "ROK Army soldiers in granite-pattern digital camo uniforms sleeping side by side on a warm earth floor with boots off and rifles leaning on the wall, helmets off, faces turned to the wall",
    "ROK_SENTRY_ROOF": "ROK Army soldier in granite-pattern digital camo uniform and covered ballistic helmet standing on the roof of an armored vehicle, face turned away",
    "OX_TEAMS": "two long files of brown oxen under wooden yokes, forty animals, hauling thick hemp tow ropes through deep mud, Sui drovers in grey-blue padded coats and hemp head cloths walking beside them with switches, faces turned away",
    "RADIO_HANDHELD": "an olive-green military handheld VHF radio with a short black rubber antenna and a push-to-talk switch",
}
EXTRA_REF = {  # extra → ref đính (nếu có)
    "BOY_SCOUT": "EXTRA_boy_scout_ref", "XIANBEI_DEPUTY": "EXTRA_xianbei_deputy_ref",
    "SUI_VANGUARD_GENERAL": "EXTRA_sui_vanguard_general_ref",
    "GOG_CAVALRYMEN": "VEH_101_ref", "GOG_CAVALRYMEN_WALKING": "VEH_101_ref", "GOG_CAVALRYMEN_GRAVE": "VEH_101_ref",
    "XIANBEI_RIDERS": "VEH_206_ref", "XIANBEI_RIDERS_EARS": "VEH_206_ref", "XIANBEI_TORCHBEARERS": "VEH_206_ref",
    "XIANBEI_CLIMBERS": "VEH_206_ref", "XIANBEI_ARCHERS_PRONE": "VEH_206_ref", "XIANBEI_WARRIORS_FOOT": "VEH_206_ref", "XIANBEI_CAMP_MEN": "VEH_206_ref",
    "SUI_MARCHERS": "WPN_201_ref", "SUI_DIGGERS": "WPN_201_ref", "SUI_DIGGERS_BANK": "WPN_201_ref", "SUI_VANGUARD_WET": "WPN_201_ref",
    "SUI_CROWD_CHARGING": "WPN_201_ref", "SUI_GUARDS": "WPN_201_ref", "SUI_SOLDIERS_STARVING": "WPN_201_ref",
    "SUI_SCOUTS_HORSE": "VEH_207_ref", "SUI_CAVALRY_ENVOY": "VEH_207_ref", "SUI_RAIDERS": "VEH_207_ref", "SUI_OFFICER_HORSE": "VEH_207_ref",
    "K3_GUNNER": "WPN_003_ref", "K3_GUNNER_DEAD": "WPN_003_ref", "K3_GUNNERS": "WPN_003_ref",
    "PZF_GUNNER": "WPN_005_ref", "MORTAR_GUNNER": "WPN_002_ref", "MORTAR_CREW": "WPN_002_ref",
    "OX_TEAMS": "VEH_002_captured",
}

# ---------------------------------------------------------------- VEHICLE STATES 3화 (vehicle_bible damage state 3화; veh_ref = ref biến thể nếu có)
VEH_STATE = {
    "K2_VALLEY": "Camouflage netting removed, cut pine branches lashed over the turret roof, a green 20-liter jerrycan and one dark olive 200-liter fuel drum roped to the rear of the turret, black soot around the muzzle, an extra black whip antenna, fresh mud on the tracks.",
    "K2_DRUM": "Wet mud sprayed over the lower half of the hull, cut pine branches lashed over the turret roof, a green jerrycan and one dark olive 200-liter fuel drum roped to the rear of the turret, black soot around the muzzle, an extra black whip antenna, one skirt plate missing on the left side.",
    "K2_MULE": "Wet mud over the lower half of the hull, cut pine branches over the turret roof, two heavy machine guns, mortar tubes and olive ammunition cans lashed under a net on the engine deck, a green jerrycan and a dark olive 200-liter drum roped to the turret rear, black soot around the muzzle, an extra black whip antenna, one skirt plate missing on the left side.",
    "K2_MULE_STEAM": "Wet mud over the lower half of the hull, cut pine branches over the turret roof, machine guns, mortar tubes and ammunition cans lashed under a net on the engine deck, a green jerrycan and a dark olive drum roped to the turret rear, black soot around the muzzle, one skirt plate missing on the left side, white steam venting from the rear engine grille.",
    "K2_MULE_SCORCH": "Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black where a fire arrow struck, machine guns, mortar tubes and ammunition cans lashed under a net on the engine deck, no fuel drum, black soot around the muzzle, an extra black whip antenna, one skirt plate missing on the left side.",
    "K2_MULE_PATCH": "Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black, the rear engine grille propped open showing a bright red copper sleeve lashed with black pitch-soaked leather cord over a coolant hose, machine guns and ammunition cans lashed on the engine deck, no fuel drum, one skirt plate missing on the left side.",
    "K2_PASS": "Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black, machine guns, mortar tubes and ammunition cans lashed under a net on the engine deck, no fuel drum, a bundle of charging cables running from a socket at the rear of the hull, black soot around the muzzle, one skirt plate missing on the left side, engine silent.",
    "K2_AFTER": "Wet mud over the lower half of the hull, cut pine branches over the turret roof with one branch scorched black, fresh black soot around the muzzle, several broken arrows stuck in the stowage net over the engine deck, machine guns and ammunition cans lashed on the engine deck, no fuel drum, one skirt plate missing on the left side.",
    "K21_3_INTACT": "White numeral 3 on the turret side beside a small Korean flag, camouflage net removed, rear troop ramp lowered and open, a crude hand-forged iron pin with hammer marks through the third road wheel on the right side, wet armor reflecting orange firelight.",
    "K21_3_HOLES": "White numeral 3 on the turret side beside a small Korean flag, camouflage net removed, rear troop ramp lowered and open, a crude hand-forged iron pin through the third road wheel on the right side, two small empty bolt holes on the hull side where a nameplate was removed, wet armor reflecting orange firelight.",
    "K21_2_DRAINED": "White numeral 2 on the turret, rear troop ramp open, camouflage net removed, black soot around the short muzzle, fuel drained, standing dark and empty forty meters away.",
    "K21_2_BURNING": "White numeral 2 on the turret, hull torn open at the side, engulfed in tall orange flame with sparks and intermittent detonations flashing inside the open troop compartment.",
    "K21_3_CAPTURED": "Mud-streaked hull, rear troop ramp open, a red and yellow Sui silk banner with black tassels tied to the turret, thick hemp tow ropes lashed around the hull front leading forward to two files of oxen, two small empty bolt holes on the hull side where a nameplate was removed, a small white arrow mark painted on the ramp, no fuel cans, no camouflage net.",
    "K21_3_PARKED": "Mud-streaked hull, rear troop ramp open, a red and yellow Sui silk banner with black tassels tied to the turret, slack hemp tow ropes lying in the mud in front of the hull, two small empty bolt holes on the hull side, no camouflage net, wet armor reflecting torchlight.",
    "TRUCKS_BURNING": "Two six-wheeled military cargo trucks and a boxy 4x4 command vehicle engulfed in tall orange flame, canvas covers burned away, black smoke rising.",
    "XIANBEI_EARS": "The horses' ears stuffed with rolled felt and tied with cord across the cheeks.",
    "DRONE_WRECK": "The drone with one arm snapped, two propellers broken, the gimbal camera cracked, dried mud on the body.",
}

# ---------------------------------------------------------------- SUB-LOCATION LOCKS 3화 (cố định, dùng nguyên văn mọi SC) → sublocks_ep3.md
def cmsub(k):
    return CM_SUB[k]["lock"]

SUBLOC = {
    # key: (loc_id, ref_id, text)
    # ---- LOC_003 Dạng A (thung lũng sau 요동성) — đêm D1 cháy xe
    "LOC_003_valley_fire": ("LOC_003", "LOC_003_valley_fire_ep3",
        "The hidden company valley behind the Goguryeo fortress at night in early summer: a narrow valley of green grass and leafed oak scrub with bare earth churned by tracks, two six-wheeled military cargo trucks and a boxy 4x4 command vehicle burning with tall orange flames that light the rocky valley sides, black smoke rising into low cloud, struck olive-green army tents folded on the ground, one K21 infantry fighting vehicle standing apart with its rear ramp open"),
    "LOC_003_valley_k21": ("LOC_003", "LOC_003_valley_fire_ep3",
        "Beside a K21 infantry fighting vehicle in the hidden valley at night: churned bare earth and wet green grass, olive ammunition cans and green jerrycans on the ground, the orange glow of burning vehicles out of focus behind, black smoke against low cloud, a big oak in leaf overhead"),
    "LOC_003_valley_westledge": ("LOC_003", "LOC_003_valley_fire_ep3",
        "A rocky ledge high on the west side of the hidden valley at night: wet grey rock, leafed oak scrub, below it the valley lit orange by burning vehicles, and to the west a dark mountain trail winding down a black forested slope under low cloud"),
    "LOC_003_valley_mouth": ("LOC_003", "LOC_003_valley_fire_ep3",
        "The mouth of the hidden valley at night: a stony stream bed, wet green grass and leafed oak scrub on the low hills either side, the orange glow of burning vehicles and black smoke behind, armored Goguryeo horsemen waiting in the dark, the first drops of rain"),
    "LOC_003_valley_k21_rain": ("LOC_003", "LOC_003_valley_fire_ep3",
        "A K21 infantry fighting vehicle standing alone under a big leafed oak in the hidden valley at night, rear ramp open, wet armor reflecting orange flames from a burning wreck behind it, the first raindrops speckling the roof, churned bare earth"),
    # ---- LOC_003 Dạng B (di động) — khe núi có suối, đêm D3 mưa (bible REF_PROMPT_EN_MOBILE)
    "LOC_003_ravine": ("LOC_003", "LOC_003_mobile",
        "A single K2 Black Panther tank in mud-smeared three-tone camouflage hidden under cut pine branches and a camouflage net in a narrow rocky ravine with a stream, one olive-green command tent and a few ponchos strung between pine trunks, wet ferns and moss, thick grey mist drifting through the trees, cold grey-green light, no other vehicles, no modern buildings"),
    "LOC_003_ravine_k2rear": ("LOC_003", "LOC_003_mobile",
        "The rear of a K2 tank in a narrow rocky ravine at night in rain: the engine deck under cut pine branches, a green jerrycan and a dark olive fuel drum roped to the turret rear, a tarpaulin on wet stones below with a tangle of charging cables running from a socket in the hull, wet ferns, moss on the rocks, a stream, mist"),
    "LOC_003_ravine_poncho": ("LOC_003", "LOC_003_mobile",
        "Under a dripping olive poncho strung between pine trunks in a narrow rocky ravine at night: wet ferns and moss, a rucksack and an open hard olive case on a flat stone, faint red lamplight from a tent nearby, rain running off the poncho edge"),
    "LOC_003_ravine_hearth": ("LOC_003", "LOC_003_mobile",
        "A small Goguryeo stone hearth under a stretched olive poncho in a narrow rocky ravine at night: a ring of wet grey stones, a clay pot over low orange flames, steel canteen cups, wet ferns and moss, pine trunks, the dark shape of a tank under branches behind, rain"),
    "LOC_003_ravine_mouth": ("LOC_003", "LOC_003_mobile",
        "The mouth of a narrow rocky ravine at night in rain: a shallow stream over grey stones, wet ferns, pine trunks, a line of small chestnut Goguryeo horses with wet saddles being led up, mist, a faint red glow from a tent deeper in the ravine"),
    "LOC_003_ravine_tent": ("LOC_003", "LOC_003_mobile",
        "Inside a small olive-green command tent pitched among pines at night, dim red tactical lamplight: a steel folding table with a folded paper map, a cracked military tablet and a backpack radio, a hand-written tally board on a plank, stacked olive ammunition cans, rain drumming on the tent fabric, mud on the ground sheet"),
    "LOC_003_ravine_stream_nvg": ("LOC_003", "LOC_003_mobile",
        "A shallow stream over grey stones at the edge of a pine ravine at night, wet ferns and moss, pine trunks, mist, seen in monochrome green night vision"),
    # ---- LOC_001 đồng bằng đông 요동성 (tháng 6 — mưa, xanh; KHÔNG dùng lock cỏ vàng 1화)
    "LOC_001_plain_night_aerial": ("LOC_001", "LOC_001_plain_rain_ep3",
        "From very high above at night: a flat black plain under low cloud with a river of orange campfires stretching from one horizon to the other, tiny red banners as specks, and along the right edge a dark silent range of mountains without a single light"),
    "LOC_001_plain_road": ("LOC_001", "LOC_001_plain_rain_ep3",
        "A wide road of deep grey mud across a flat green plain in early summer rain, trampled wet grass either side, cart ruts full of water, low grey cloud, no trees, no buildings"),
    "LOC_001_plain_camp_night": ("LOC_001", "LOC_001_plain_rain_ep3",
        "A Sui army camp on the wet plain at night: rows of sagging grey felt tents with rain running off them, muddy lanes between the rows, small guttering campfires, red and yellow banners hanging limp, low cloud"),
    "LOC_001_plain_camp_tent_edge": ("LOC_001", "LOC_001_plain_rain_ep3",
        "The muddy edge of a sagging grey felt tent in a Sui camp at night: a shallow pit dug in wet dark earth right under the tent skirt, spilled yellow millet on the mud, a wooden shovel, bare footprints filling with rainwater"),
    # ---- LOC_008 (dãy núi giữa Liêu Đông và Áp Lục — đầu hè xanh, mưa phùn) — đường núi D2, sườn núi đêm D2
    "LOC_008_aerial_split": ("LOC_008", "LOC_008_mountain_road_ep3",
        "From very high above on a grey drizzly day: on the left a flat green plain with a huge black column of marching men flowing east without visible head or tail, on the right a range of green forested mountains with a thread of a road along which a tiny line of walkers, riders, ox carts and one dark square vehicle moves, twenty li of low hills between them, low cloud"),
    "LOC_008_mountain_road": ("LOC_008", "LOC_008_mountain_road_ep3",
        "A narrow mountain road of red-brown mud winding along a green early-summer hillside of pine and young oak, wet ferns and moss on the rocks, low cloud on the ridges, steady drizzle, no buildings"),
    "LOC_008_road_pine": ("LOC_008", "LOC_008_mountain_road_ep3",
        "The foot of a big pine beside a muddy mountain road in drizzle: wet roots and moss, ferns, a flat rock, the green hillside dropping away below, low cloud"),
    "LOC_008_road_bend_amnok": ("LOC_008", "LOC_008_mountain_road_ep3",
        "A wet bend of a mountain road in drizzle with low cloud hiding the peaks, green pine and oak slopes, mud sprayed on the rocks, and far to the south-east a dark green ribbon of river showing for the first time between two ranges"),
    "LOC_008_ridge_day": ("LOC_008", "LOC_008_mountain_road_ep3",
        "A grassy ridge crest above rolling green foothills in early summer drizzle: wet knee-high grass and low oak scrub, and far below to the north the flat plain fading into rain haze"),
    "LOC_008_hill_gap": ("LOC_008", "LOC_008_mountain_road_ep3",
        "A grassy gap between two low green hills in drizzle: wet grass churned by hooves, oak scrub on the slopes, the flat plain hazy beyond"),
    "LOC_008_ridge_night": ("LOC_008", "LOC_008_mountain_road_ep3",
        "A rock ledge on a mountainside at night after rain: wet grey rock, low oak scrub, low cloud, and far below the whole plain covered with the orange campfires of a huge army to the horizon"),
    # ---- LOC_008 sơn thành nhỏ trên đỉnh đồi (đêm D11 mưa)
    "LOC_008_hill_fort": ("LOC_008", "LOC_008_hill_fort_ep3",
        "A small Goguryeo hill fort on a wooded hilltop at night in rain: a low dry-stacked grey stone wall three to four meters high following the ridge, a single wooden gate under a small roof with torches, a timber watchtower, inside a packed-earth yard with a raised-floor granary on wooden posts, a large brown hemp tent with a wet black three-legged crow banner, long horse lines, pine trees beyond the wall"),
    "LOC_008_fort_tent": ("LOC_008", "LOC_008_hill_fort_ep3",
        "Interior of a large brown hemp campaign tent on wooden poles at night in rain: clay oil lamps giving warm yellow light, a leather map painted in ink spread over a wooden chest, black wooden game pieces, a rack of spears and bows, woven reed mats on packed earth, rain drumming on the hemp, the tent flap tied open on darkness"),
    "LOC_008_fort_yard": ("LOC_008", "LOC_008_hill_fort_ep3",
        "The packed-earth yard of a small Goguryeo hill fort at night in rain: a raised-floor timber granary on wooden posts with a bark-shingle roof, a K2 tank parked beside it under cut pine branches, torches under small roofs, the low dry-stacked stone wall and a wooden gate, horse lines, puddles"),
    "LOC_008_fort_granary_shed": ("LOC_008", "LOC_008_hill_fort_ep3",
        "Under the roof of a raised-floor Goguryeo granary at night in rain: a woven reed mat on planks, a clay bowl of brown herbal liquid, strips of cloth, a clay oil lamp, thick wooden posts, rain falling in sheets just beyond the eaves"),
    "LOC_008_fort_wall": ("LOC_008", "LOC_008_hill_fort_ep3",
        "On top of the low dry-stacked stone wall of a small Goguryeo hill fort at night in rain: a small timber watch hut with a bark roof, wet stone, a torch guttering under the eaves, black wooded valley below"),
    "LOC_008_fort_gate": ("LOC_008", "LOC_008_hill_fort_ep3",
        "The wooden gate of a small Goguryeo hill fort at night in rain: two plank doors under a small bark-shingle roof with torches in iron brackets, a heavy wooden bar, dry-stacked grey stone wall either side, mud"),
    "LOC_008_fort_trail": ("LOC_008", "LOC_008_hill_fort_ep3",
        "A muddy trail at the foot of a wooded hill at night in rain, tank track marks pressed deep in the mud, dripping oak scrub and pine either side, mist"),
    "LOC_008_fort_tent_ext": ("LOC_008", "LOC_008_hill_fort_ep3",
        "A large brown hemp campaign tent on wooden poles in a fort yard at night in rain, a wet black three-legged crow banner on a pole beside it, warm yellow lamplight glowing through the wet hemp, mud and puddles"),
    "LOC_008_fort_aerial": ("LOC_008", "LOC_008_hill_fort_ep3",
        "From above at night in rain: a small dark hill fort with a low stone wall on a wooded hilltop, two torches at its gate, a dark square vehicle beside a granary inside, and far to the north down in the valley a faint blurred band of enemy campfires"),
    # ---- LOC_008 làng dưới chân đèo (D12–D14, mưa phùn) — lock gốc bible + sub-khu
    "LOC_008": ("LOC_008", "LOC_008_wide", LOC_LOCK["LOC_008"]),
    "LOC_008_village_street": ("LOC_008", "LOC_008_wide",
        "A muddy lane through a Goguryeo mountain village in drizzle: timber houses with dark bark-shingle roofs weighted with stones, a small raised-floor granary on wooden posts, wooden fences, a stone mortar, clay jars, blue hearth smoke, green pine and oak slopes above"),
    "LOC_008_village_k2": ("LOC_008", "LOC_008_wide",
        "Beside a raised-floor Goguryeo granary on wooden posts in a mountain village in drizzle: a K2 tank parked under cut pine branches with a tangle of charging cables running from its rear across the wet yard to the porch of a timber house, wooden fences, bark-shingle roofs, mud"),
    "LOC_008_village_forge": ("LOC_008", "LOC_008_detail",
        "A Goguryeo village forge at night: an open timber shed with bark-shingle roof, a clay furnace glowing orange, a leather bellows, a stone anvil with a hammer, iron tongs, a bucket of dark water, bundles of dried medicinal herbs hanging from the rafters, a clay pot and woven baskets, wet stone path outside with a rocky stream, warm orange forge light against cool blue darkness"),
    "LOC_008_village_forge_day": ("LOC_008", "LOC_008_detail",
        "A Goguryeo village forge on a grey rainy afternoon: an open timber shed with bark-shingle roof, a clay furnace glowing orange, a leather bellows, a stone anvil with a hammer, iron tongs, a bucket of dark water, bundles of dried herbs under the rafters, wet stone path and a rocky stream outside"),
    "LOC_008_village_terraces": ("LOC_008", "LOC_008_wide",
        "Narrow terraced fields of young green millet below a Goguryeo mountain village at dusk in drizzle: low earth banks, a small raised-floor granary at the field edge, a muddy path, timber houses with bark-shingle roofs on the slope above, pine forest, low cloud"),
    "LOC_008_village_edge": ("LOC_008", "LOC_008_wide",
        "The lower edge of a Goguryeo mountain village at dusk: a wooden fence, a mud bank dropping to terraced fields of young green millet below, bark-shingle roofs behind, drizzle, low cloud"),
    "LOC_008_village_porch": ("LOC_008", "LOC_008_wide",
        "The low plank porch of a Goguryeo timber house in a mountain village at night in rain: a bark-shingle roof weighted with stones dripping at the eaves, a row of night-vision monoculars charging on the planks with small red lights, a cable running out into the mud toward a dark tank, a clay jar, wooden fence"),
    "LOC_008_village_house_int": ("LOC_008", "LOC_008_wide",
        "Inside a Goguryeo timber house at night: a warm packed-earth floor heated from below, a small fire in a stone hearth, round wooden posts, plank walls, straw mats, rifles leaning against the wall, boots in a row by the door, rain on the bark roof"),
    "LOC_008_village_granary_floor": ("LOC_008", "LOC_008_wide",
        "The plank floor of a small raised-floor Goguryeo granary at night seen from above: wooden planks, a few grey hemp sacks, a bark-shingle roof close overhead, rain dripping at the eaves, faint orange forge light from outside"),
    "LOC_008_village_night_wide": ("LOC_008", "LOC_008_wide",
        "A Goguryeo mountain village at night in rain, every house dark, bark-shingle roofs shining wet, one orange glow from an open forge shed by the stream lighting the roof beside it and the flank of a tank parked nearby, pine slopes black above"),
    "LOC_008_village_gate": ("LOC_008", "LOC_008_wide",
        "The wooden fence gate of a Goguryeo mountain village at night in rain: rough poles, a muddy path leading east into darkness, dripping pines, no torches"),
    "LOC_008_village_fort_wall": ("LOC_008", "LOC_008_wide",
        "On the low dry-stacked stone wall of a small hill fort above a mountain village at night: wet grey stone, pine tops, and across the valley the black wall of a mountain pass with thick white fog pouring through the saddle between two cliffs"),
    "LOC_008_village_sandtable": ("LOC_008", "LOC_008_wide",
        "A wet yard beside a raised-floor Goguryeo granary on a grey rainy morning: a plank laid on stones carrying a model of a mountain pass built from mud, two high mud ridges for cliffs, a narrow saddle between them with a groove for a road, a long stone standing upright at one corner, a bamboo stick planted on one ridge, boots and a pair of straw sandals around the plank"),
    "LOC_008_village_k2_side": ("LOC_008", "LOC_008_wide",
        "The wet flank of a K2 tank turret in drizzle beside a Goguryeo granary: three-tone camouflage paint, a small Korean flag, white chalk lines drawn on the armor"),
    "LOC_008_village_upward": ("LOC_008", "LOC_008_wide",
        "From the bark-shingle roofs of a mountain village looking up at night: the two blue-grey cliffs of a mountain pass black against low night cloud, the saddle between them filled with white fog, no light anywhere on it"),
    "LOC_008_village_terraces_up": ("LOC_008", "LOC_008_wide",
        "From terraced fields of young green millet looking up in drizzle: a Goguryeo mountain village of timber houses with bark-shingle roofs, a K2 tank parked beside a raised-floor granary under cut pine branches, blue hearth smoke, and high above the village a dirt road winding up into a cleft between two blue-grey cliffs lost in cloud"),
    # ---- LOC_005_AMNOK (D9–D10, D16)
    "LOC_005": ("LOC_005", "LOC_005_wide", LOC_LOCK["LOC_005"]),
    "LOC_005_south_hill": ("LOC_005", "LOC_005_south_hill_ep3",
        "A rocky outcrop under wet pines on the steep south bank above the river: wet moss and ferns, grey rock, a gap in the pines looking down on a wide grey cobble shoal and the dark green river, the far bank crowded with sagging grey tents in drizzle, mist on the peaks"),
    "LOC_005_south_forest": ("LOC_005", "LOC_005_south_hill_ep3",
        "Inside a wet pine forest on the steep south bank of the river in drizzle: dripping pine trunks, ferns, moss, grey rock, mist between the trees, the river a dark green gleam below"),
    "LOC_005_south_forest_edge": ("LOC_005", "LOC_005_south_hill_ep3",
        "The edge of a pine forest on the south bank of the river in drizzle: wet pines, ferns, a slope of grey rock dropping to a wide cobble shoal and the dark green river, the far bank crowded with sagging grey tents, mist"),
    "LOC_005_mortar_pit": ("LOC_005", "LOC_005_south_hill_ep3",
        "A hastily dug mortar pit among wet pines on the south bank hillside: two 81mm mortars on bipods, round baseplates in the mud, ten finned mortar bombs laid in two rows on a poncho, ferns, dripping branches, drizzle"),
    "LOC_005_south_ledge_k3": ("LOC_005", "LOC_005_south_hill_ep3",
        "A rock ledge under pines on the south bank hillside in drizzle: wet grey rock and moss, a clear view down to a wide grey cobble shoal at the river's edge, mist"),
    "LOC_005_shoal_south": ("LOC_005", "LOC_005_wide",
        "A wide shoal of grey cobbles on the south bank of the river in drizzle: the dark green river rushing past, the wooded slope rising behind, mist on the peaks"),
    "LOC_005_ford": ("LOC_005", "LOC_005_wide",
        "The cobble ford of the river in drizzle: knee-deep to chest-deep green water over grey cobbles, the north bank with its sagging grey tents behind, the wooded south bank ahead, mist"),
    "LOC_005_shoal_north": ("LOC_005", "LOC_005_wide",
        "The wide grey cobble shoal on the north bank of the river in drizzle below a sagging grey Sui camp with limp red and yellow banners, the dark green river beyond, mist on the far wooded slope"),
    "LOC_005_camp_edge_pits": ("LOC_005", "LOC_005_detail",
        "The muddy edge of a Sui camp on the north bank in rain: rows of sagging grey felt tents, hundreds of shallow pits dug in the wet dark earth along the bank, grey hemp sacks half buried and trampled, spilled yellow millet, wooden shovels, footprints filling with water, the dark green river below"),
    "LOC_005_camp_lane": ("LOC_005", "LOC_005_detail",
        "A mud lane between rows of sagging grey felt tents in a wet Sui camp on the north bank: puddles, spilled millet trodden into the mud, spears stuck upright, red and yellow banners hanging limp with rain, drizzle, mist"),
    "LOC_005_camp_gate": ("LOC_005", "LOC_005_detail",
        "The gate of a Sui camp on the north bank in drizzle: a gap in a low wet earth bank with a wooden barrier, red and yellow banners on black poles hanging limp, sagging grey tents behind, the grey cobble shoal and dark green river in front"),
    "LOC_005_sui_tent": ("LOC_005", "LOC_005_sui_tent_ep3",
        "Interior of a large Sui field tent on the north bank of the river: a wet plank floor, grey felt walls dripping, a folding wooden camp chair, a low black lacquered table with a brush, an ink stone and strips of pale silk, bronze oil lamps, a red and yellow banner, spears of the guard along the walls, rain drumming on the roof, grey daylight from the open flap"),
    "LOC_005_sui_tent_2": ("LOC_005", "LOC_005_sui_tent_ep3",
        "Interior of a Sui general's field tent on the north bank in the morning: a wet plank floor, grey felt walls, a low black lacquered table covered with bundles of wet bamboo writing slips, a folding camp chair, bronze oil lamps, spears along the wall, rain drumming on the roof, grey light from the flap"),
    "LOC_005_north_road": ("LOC_005", "LOC_005_wide",
        "A muddy road along the north bank of the river between trampled green fields and wet pines: deep ruts full of water, hoofprints, drizzle, the dark green river and misty mountains beyond"),
    "LOC_005_north_road_night": ("LOC_005", "LOC_005_wide",
        "A muddy flat beside the river road on the north bank at night after rain: torches on poles, wet pines, the dark river gleaming, small campfires, mist"),
    "LOC_005_north_fire": ("LOC_005", "LOC_005_wide",
        "Beside a small campfire on a muddy flat by the river at night: a patch of flat wet mud scratched with lines, a few pebbles, firelight on wet leather and pine trunks, steppe horses on a picket line in the dark behind"),
    "LOC_005_north_horses": ("LOC_005", "LOC_005_wide",
        "A Xianbei horse line on a muddy flat by the river at night: short stocky steppe horses tied to a rope between pines, torches, wet mud, mist"),
    "LOC_005_north_horses_dawn": ("LOC_005", "LOC_005_wide",
        "A wide muddy flat by the river at grey dawn: thousands of short stocky steppe horses and riders mounting up in long lines, wet pines, mist on the river, low cloud"),
    "LOC_005_sui_road_tent": ("LOC_005", "LOC_005_sui_tent_ep3",
        "Interior of a Sui general's tent pitched hastily beside a muddy road: a wet plank floor, grey felt walls, a low black lacquered table, a folding camp chair, bronze oil lamps, a red and yellow banner, rain drumming on the roof, the tent flap tied open on a rainy green valley"),
    "LOC_005_aerial_south": ("LOC_005", "LOC_005_wide",
        "From high above on a rainy day: a huge black column of marching men flowing south-east along a valley of green rice paddies and pine hills, red banners drooping with rain, grey hemp sacks scattered along both sides of the road, low cloud"),
    # ---- LOC_004 육합성 (SC_132, sáng, mưa trên mái)
    "LOC_004_pavilion_int": ("LOC_004", "LOC_004_detail", cmsub("LOC_004_pavilion_int")),
    # ---- LOC_009 석문령 (D12–D15)
    "LOC_009": ("LOC_009", "LOC_009_wide", LOC_LOCK["LOC_009"]),
    "LOC_009_east_road": ("LOC_009", "LOC_009_wide",
        "A rough dirt-and-stone road climbing the wet green east slope toward a mountain pass through twisted red pines and young oak, loose stones, low cloud, drizzle"),
    "LOC_009_east_road_ledge": ("LOC_009", "LOC_009_wide",
        "A rock ledge above a rough mountain road on the wet green east slope of a pass, twisted red pines, low cloud, drizzle"),
    "LOC_009_north_ledge": ("LOC_009", "LOC_009_wide",
        "A high rock ledge on a green mountainside north of a village in drizzle: wet grey rock, twisted red pines, and far below to the north a long green valley fading into rain haze"),
    "LOC_009_goat_path": ("LOC_009", "LOC_009_detail",
        "A one-meter goat path scratched along a wet blue-grey cliff face, loose scree below, twisted red pines clinging to the rock, the path winding up into low cloud"),
    "LOC_009_goat_path_fog": ("LOC_009", "LOC_009_detail",
        "A one-meter goat path on a wet blue-grey cliff face at night in thick fog, loose scree, twisted red pines, a rock ledge overhanging the path just above"),
    "LOC_009_far_ridge": ("LOC_009", "LOC_009_wide",
        "A rocky ridge five kilometers from a village at overcast dusk: wet boulders, short grass, twisted red pines, and far below a green valley with a cluster of bark-roofed houses, a thread of smoke rising from a shed by a stream, faint amber light through grey cloud"),
    "LOC_009_xianbei_forest": ("LOC_009", "LOC_009_xianbei_camp_ep3",
        "A Xianbei horse camp hidden in a wet pine forest at dusk: short stocky steppe horses on picket ropes between the trunks, no fires, rain dripping from the needles, mist"),
    "LOC_009_south_gate": ("LOC_009", "LOC_009_wide",
        "The south mouth of a mountain pass at midday in drizzle: a rough stone road dropping away to the south between twisted red pines and wet blue-grey rock, low cloud, armored horsemen waiting on the slope"),
    "LOC_009_east_foot": ("LOC_009", "LOC_009_wide",
        "The east foot of a mountain pass in afternoon drizzle: a rough stone road, wet blue-grey cliffs rising on both sides, twisted red pines, and two hundred meters above a flat-topped rocky outcrop jutting out of the low cloud"),
    "LOC_009_saddle_dusk": ("LOC_009", "LOC_009_wide",
        "The saddle of a mountain pass at overcast dusk: a low ruined dry-stacked Goguryeo stone barrier with a five-meter gap crossing bare wet rock and short grass, a collapsed round stone watch post at its north end, wet blue-grey cliffs either side with faint amber light on their tops, the saddle already in shadow, white mist pouring through from the north-west"),
    "LOC_009_saddle_night": ("LOC_009", "LOC_009_saddle_night_ep3",
        "The saddle of a mountain pass at night: bare wet rock and short grass, a low ruined dry-stacked Goguryeo stone barrier with a five-meter gap crossing the saddle, a collapsed round stone watch post at its north end, wet blue-grey cliffs rising into low cloud on both sides, thin mist, no light except a few faint red charging LEDs"),
    "LOC_009_barrier_gap": ("LOC_009", "LOC_009_saddle_night_ep3",
        "The five-meter gap in a low ruined dry-stacked Goguryeo stone barrier on a mountain pass saddle at night: wet blue-grey stone blocks with moss and yellow lichen, rotten wooden posts, bare wet rock, thin mist, the black cliff wall beyond"),
    "LOC_009_barrier_line": ("LOC_009", "LOC_009_saddle_night_ep3",
        "Along the foot of a low ruined dry-stacked Goguryeo stone barrier on a mountain pass saddle at night: wet blue-grey stone blocks, moss, sandbags, bare wet rock, thin mist, faint red charging lights, the black cliff wall to the north-west"),
    "LOC_009_outcrop_path": ("LOC_009", "LOC_009_outcrop_ep3",
        "A steep stony path climbing the wet blue-grey south-east cliff of a mountain pass toward a flat-topped outcrop: loose scree, twisted red pines, a rope fixed on the rock, the dark saddle far below"),
    "LOC_009_outcrop_top": ("LOC_009", "LOC_009_outcrop_ep3",
        "The flat top of a rocky outcrop ten meters square two hundred meters above a mountain pass saddle at night: bare wet blue-grey rock, a few tufts of grass, a sheer drop on three sides, the cliff continuing up behind, low cloud, the saddle a dark trough far below"),
    "LOC_009_outcrop_top_dawn": ("LOC_009", "LOC_009_outcrop_ep3",
        "The flat top of a rocky outcrop ten meters square high above a mountain pass saddle at grey rainy dawn: bare wet blue-grey rock, extinguished torches, hemp ropes hanging down from the cliff above, low cloud"),
    "LOC_009_nw_cliff": ("LOC_009", "LOC_009_saddle_night_ep3",
        "The north-west cliff of a mountain pass at night seen from the saddle: a black wall of wet blue-grey rock rising into low cloud with a goat path zigzagging down it, twisted red pines, scree at the foot"),
    "LOC_009_nw_cliff_torches": ("LOC_009", "LOC_009_detail",
        "The north-west cliff of a mountain pass at night: a chain of hundreds of burning torches winding down a goat path from the cloud to the saddle, torchlight glowing orange on wet blue-grey rock and thin mist, twisted red pines"),
    "LOC_009_goat_path_foot": ("LOC_009", "LOC_009_saddle_night_ep3",
        "The foot of a goat path where it spills onto a mountain pass saddle at night: loose scree, wet blue-grey rock, torches burning above, thin mist"),
    "LOC_009_goat_path_upper": ("LOC_009", "LOC_009_detail",
        "The upper section of a goat path on a wet blue-grey cliff at night: a narrow rock shelf, a branch path climbing away toward the cliff top, torches passing below, thin mist, across the pass the dark shape of a flat-topped outcrop"),
    "LOC_009_cliff_top_above_outcrop": ("LOC_009", "LOC_009_outcrop_ep3",
        "The cliff top directly above a flat-topped rocky outcrop on a mountain pass at night: wet blue-grey rock, twisted red pines, hemp ropes tied to pine trunks and dropped over the edge, the small flat top of the outcrop faintly lit far below, low cloud"),
    "LOC_009_rockslide": ("LOC_009", "LOC_009_aftermath",
        "A fresh rockslide of wet blue-grey boulders piling up six meters high at the foot of a cliff where a goat path meets a mountain pass saddle, dust and smoke drifting, extinguished torches among the stones, night"),
    "LOC_009_saddle_dawn": ("LOC_009", "LOC_009_aftermath",
        "The saddle of a mountain pass at grey rainy dawn after a night battle: a fresh rockslide of blue-grey boulders six meters high blocking the foot of the north-west cliff, dust and thin smoke still drifting, broken arrows, extinguished torches and a dead steppe horse on the wet stones, a low ruined dry-stacked Goguryeo stone barrier across the saddle, twisted red pines, low cloud, cold grey-blue light"),
    "LOC_009_south_flat": ("LOC_009", "LOC_009_aftermath",
        "A small flat of wet earth at the south end of a mountain pass saddle at grey rainy dawn: short grass, a shallow grave pit, a heap of river cobbles, an upright slab of blue-grey stone, twisted red pines, low cloud"),
    "LOC_009_grave": ("LOC_009", "LOC_009_aftermath",
        "A new Goguryeo-style grave on a small flat at the south end of a mountain pass in rain: a mound of fresh dark earth ringed with grey river cobbles, one upright slab of blue-grey stone at the head, short wet grass, twisted red pines"),
    "LOC_009_south_descent": ("LOC_009", "LOC_009_wide",
        "A rough stone road descending the south side of a mountain pass in rain: wet blue-grey rock, twisted red pines, loose stones, low cloud, green forested slopes below"),
    "LOC_009_south_foot": ("LOC_009", "LOC_009_wide",
        "A muddy fork of roads below the south side of a mountain pass in rain: one track running south into green forested hills, one climbing back north-east, wet grass, twisted red pines, low cloud"),
    "LOC_009_cliff_top_far": ("LOC_009", "LOC_009_wide",
        "The top of the north-west cliff of a mountain pass at grey dawn seen from the saddle far below: a bare rock skyline against pale cloud, twisted red pines, riders as small silhouettes"),
    "LOC_009_xianbei_camp_night": ("LOC_009", "LOC_009_xianbei_camp_ep3",
        "A Xianbei camp on a high plateau north-west of a mountain pass at night in light rain: a small campfire under a big pine, steppe horses on picket ropes with felt in their ears, wet leather saddles, a hard olive case on the ground, low cloud"),
    "LOC_009_xianbei_camp_pine": ("LOC_009", "LOC_009_xianbei_camp_ep3",
        "The foot of a big pine at the edge of a Xianbei camp at night in light rain: wet roots and needles, firelight from a small campfire nearby, a hard olive case on the ground, steppe horses tied in the dark behind"),
    "LOC_009_trail_night": ("LOC_009", "LOC_009_xianbei_camp_ep3",
        "A narrow mountain trail at night in rain: wet stones, dripping pines, low cloud, no torches, total darkness beyond the first few meters"),
    # ---- LOC_007 살수 (D17 chiều, mưa bắt đầu)
    "LOC_007": ("LOC_007", "LOC_007_wide", LOC_LOCK["LOC_007"]),
    "LOC_007_north_sand": ("LOC_007", "LOC_007_wide",
        "A wide wet grey-brown sandflat on the north bank of a wide shallow river in the first rain of a monsoon afternoon: the edge of a dense reed bed two to three meters tall, a line of wooden ford stakes crossing the shallows, long sandbars, low green hills on the far bank, low cloud"),
    "LOC_007_reeds_arrival": ("LOC_007", "LOC_007_detail",
        "Inside a dense wet reed bed on the north bank of a wide shallow river: tall grey-green reeds with pale feathered tops, firm wet grey-brown sand underfoot, old cut reed stumps, brown river water showing between the stalks, light rain, river mist"),
    "LOC_007_water_edge": ("LOC_007", "LOC_007_wide",
        "The water's edge of a wide shallow river on the north bank in light rain: wet grey-brown sand, a line of leaning wooden ford stakes, long sandbars, raindrops dimpling grey water, dense reeds behind, low cloud"),
    "LOC_007_aerial_reeds": ("LOC_007", "LOC_007_wide",
        "From high above in rain: a dense grey-green reed bed hundreds of meters wide on the north bank of a wide shallow grey river, a single faint trail of bent reeds leading into it, long sandbars, low green hills on the far bank, low cloud"),
}

# ---------------------------------------------------------------- LIGHTING theo bảng ngày/đêm 3화 (header script v2)
LIGHT = {
    "D1_night_fire": "Night, orange firelight from burning vehicles against deep blue-black darkness, black smoke, low cloud, no moon",
    "D1_night_fire_far": "Night, deep blue-black darkness, a distant orange glow of fire below, low cloud",
    "D1_night_rain_start": "Night, orange firelight on wet steel, the first raindrops falling, low cloud",
    "D2_day_drizzle": "Grey overcast day, steady light drizzle, low cloud on the ridges, flat wet green light, no shadows",
    "D2_night_cloud": "Night after rain, low cloud, deep blue-black darkness, the far glow of thousands of campfires",
    "D2_night_nvg": "Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies",
    "D2_night_lantern": "Night rain, a swinging paper lantern giving weak orange light, deep shadows",
    "D3_night_rain": "Night, steady rain, a hooded flashlight and a faint red glow from a tent, deep blue-black shadows",
    "D3_night_red": "Night interior, dim red tactical lamplight on faces and hands, rain on the tent fabric",
    "D3_night_hearth": "Night rain, low orange hearth light under a poncho, deep shadows",
    "D3_night_nvg": "Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies",
    "D4_dawn_rain": "Grey rainy dawn, cold flat blue-grey light, mist in the ravine",
    "D9_dawn_mist": "Cold grey-green diffused dawn light in drizzle, mist between wet pines, no shadows",
    "D9_day_rain": "Cold grey-green diffused daylight in steady drizzle, mist on the peaks, wet surfaces gleaming",
    "D9_tent": "Grey daylight through a wet tent flap mixed with warm bronze lamplight, rain shadows moving on the felt",
    "D9_drone_screen": "A handheld controller screen showing a live aerial view in drizzle, rain specks on the lens, cold grey-green light",
    "D10_morning_tent": "Grey rainy morning, cold light from the tent flap and warm bronze lamplight",
    "D10_day_rain": "Cold grey-green diffused daylight in steady rain, mist, wet surfaces gleaming",
    "D10_night_torch": "Night after rain, warm orange torchlight and small campfires against deep blue-black darkness, mist",
    "D6_pavilion_morning": "Grey morning light filtering through yellow silk drapes, silk lanterns still lit, rain on the silk roof",
    "D11_dawn_grey": "Cold grey dawn, mist on the river, low cloud, no sun",
    "D11_night_rain_torch": "Night, steady rain, warm orange torchlight under small roofs against deep blue-black darkness",
    "D11_night_lamp": "Night interior, warm yellow light from clay oil lamps, rain on the tent, deep shadows",
    "D11_night_nvg": "Night, monochrome green night-vision view with grain and faint scan noise, rain streaks, bright green highlights on warm bodies",
    "D11_night_rain": "Night, steady rain, faint torchlight, deep blue-black darkness",
    "D12_day_drizzle": "Grey overcast day, light drizzle, low cloud, flat wet green light",
    "D12_dusk_amber": "Overcast dusk, faint amber light through grey cloud on the ridges, the valley in shadow, drizzle",
    "D12_dusk_grey": "Grey dusk in drizzle, the last flat light fading, low cloud",
    "D12_night_forge": "Night, warm orange forge light against cool blue-black rain darkness, sparks",
    "D12_night_rain": "Night, steady rain, faint orange forge glow, deep blue-black darkness",
    "D12_night_fog_nvg": "Night, monochrome green night-vision view blurred into a bright milky mass by thick fog, grain and scan noise",
    "D12_night_fog": "Night, thick fog, no light, wet rock faintly grey",
    "D14_dawn_grey": "Grey rainy dawn, cold flat light, mist, wet surfaces",
    "D14_dawn_fog_road": "Early morning fog on a mountain road, pale grey light, wet pines dripping",
    "D14_morning_rain": "Grey rainy morning, flat cold light, low cloud",
    "D14_noon_drizzle": "Midday under heavy grey cloud, light drizzle, flat light, mist in the pass",
    "D14_afternoon_drizzle": "Grey afternoon drizzle, low cloud hiding the cliff tops, flat cold light",
    "D14_dusk_amber": "Overcast dusk, the last faint amber light on the cliff tops, the saddle already dark, white mist pouring through the gap",
    "D14_night_pass": "Night on the pass, no moon, low cloud, thin mist, near-total darkness broken only by tiny red charging LEDs",
    "D14_night_nvg": "Night, monochrome green night-vision view with grain and faint scan noise, thin mist, bright green highlights on warm bodies",
    "D14_night_thermal": "A handheld controller screen showing a white-hot thermal aerial view of a dark pass, cold blue-white glow on the operator's face",
    "D14_night_torch": "Night, hundreds of orange torches on a black cliff, thin mist glowing orange, deep blue-black darkness elsewhere",
    "D14_night_battle": "Night, orange torchlight on the cliff, red tracer streaks and white muzzle flashes, thin mist, deep blue-black darkness",
    "D14_night_muzzle": "Night, a huge white-orange tank muzzle flash lighting the whole saddle for an instant, dust and smoke, torches on the cliff",
    "D14_night_dust": "Night, orange torchlight through drifting rock dust, deep blue-black darkness",
    "D15_dawn_grey": "Cold grey-blue rainy dawn, thin smoke and dust still drifting, low cloud",
    "D15_morning_rain": "Grey rainy morning, flat cold light, low cloud, wet rock",
    "D15_night_fire": "Night, light rain, warm orange campfire light under a pine against deep blue-black darkness",
    "D15_night_nvg_enemy": "Night, monochrome green night-vision view with grain and faint scan noise, faces and horses glowing pale green around a white-hot fire",
    "D16_day_rain": "Grey rainy day, flat cold light, mist in the valley",
    "D16_night_rain": "Night, steady rain, no torches, near-total darkness with a faint green glow from a night-vision eyepiece",
    "D17_afternoon_rain": "Late monsoon afternoon, flat grey light, the first steady rain dimpling grey water, low cloud, river mist",
    "D17_dusk_rain": "Grey monsoon dusk, steady rain, flat fading light, river mist",
}
WEAR = {  # tình trạng chung lính hiện đại (character_bible §0.3, 3화) — theo ngày
    "D1": "Modern soldiers' uniforms grey with stone dust and black soot from the siege, sweat streaks, two-day stubble, no rain yet.",
    "D2": "Modern soldiers' uniforms rain-soaked and darkened, mud to the knees, three-day stubble, wind-chapped lips.",
    "D3": "Modern soldiers' uniforms rain-soaked and darkened, mud to the knees, three-day stubble, wind-chapped lips.",
    "D4": "Modern soldiers' uniforms rain-soaked and darkened, mud to the knees, three-day stubble, tired eyes.",
    "D9": "Modern soldiers' uniforms rain-soaked and darkened, mud caked to the knees, four-day stubble, hollow cheeks, tired eyes.",
    "D10": "Modern soldiers' uniforms rain-soaked and darkened, mud caked to the knees, four-day stubble, hollow cheeks, tired eyes.",
    "D11": "Modern soldiers' uniforms rain-soaked and darkened, mud caked to the knees, four-day stubble, hollow cheeks, tired eyes.",
    "D12": "Modern soldiers' uniforms rain-soaked and darkened, mud caked to the knees, four-day stubble, hollow cheeks, dark circles under the eyes.",
    "D14": "Modern soldiers' uniforms rain-soaked and fraying at the cuffs, mud caked to the knees, five-day stubble, hollow cheeks, dark circles under the eyes.",
    "D15": "Modern soldiers' uniforms rain-soaked and fraying at the cuffs, mud caked to the knees, five-day stubble, hollow cheeks, dark circles under the eyes.",
    "D16": "Modern soldiers' uniforms rain-soaked and fraying at the cuffs, mud caked to the knees, five-day stubble, hollow cheeks, dark circles under the eyes.",
    "D17": "Modern soldiers' uniforms rain-soaked and fraying at the cuffs, mud caked to the knees, five-day stubble, hollow cheeks, dark circles under the eyes.",
    "D6": "",
}
ROK = {"CHAR_001", "CHAR_002", "CHAR_003", "CHAR_004", "CHAR_005", "CHAR_006"}

# ---------------------------------------------------------------- PARSE SCRIPT (t, type, LOC header, narration, thoại, [SOUND]) — nguyên văn
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

# ---------------------------------------------------------------- LOAD BATCHES
def load_batches():
    scenes = []
    for f in sorted(glob.glob(os.path.join(HERE, "batch_*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
        scenes += mod.SCENES
    return scenes

# ---------------------------------------------------------------- ASSEMBLE
def tag_of(rid):
    return "@" + rid

def build_scene(s, sc):
    sid = s["id"]
    day = s.get("day", "D2")
    chars = s.get("chars", [])
    states = s.get("states", {})
    vehs = s.get("veh", [])
    props = s.get("props", [])
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
        seg.append(EXTRAS[e] if EXTRAS[e].endswith(".") else EXTRAS[e] + ".")
        if e in EXTRA_REF: add_ref(EXTRA_REF[e])
    vstates = s.get("veh_state", {})
    for v in vehs:
        vref = s.get("veh_ref", {}).get(v, f"{v}_ref")
        seg.append(f"{tag_of(vref)}: {LOCKS[v]}" + (f" {VEH_STATE[vstates[v]]}" if v in vstates else ""))
        add_ref(vref)
    for p in props:
        pref = f"{p}_ref" if f"{p}_ref" in REF_DIR else None
        seg.append((f"{tag_of(pref)}: " if pref else "") + LOCKS[p])
        add_ref(pref)
    seg.append(f"Setting {tag_of(loc_ref)}: {loc_text}")
    add_ref(loc_ref)
    seg.append("Action: " + s["action"].rstrip(".") + ".")
    light = LIGHT[s["light"]] if s["light"] in LIGHT else s["light"]
    seg.append("Light: " + light.rstrip(".") + ".")
    if (any(c in ROK for c in chars) or any(e.startswith(("ROK", "K2_", "K3_", "PZF", "MORTAR")) for e in extras)) and WEAR.get(day):
        seg.append(WEAR[day])
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
    rec = {
        "id": sid, "part": s["part"], "t_start": sc["t0"], "t_end": sc["t1"], "seconds": sc["t1"] - sc["t0"],
        "type": sc["type"], "loc": loc_id, "subloc": subloc, "day": day,
        "chars": chars, "extras": extras, "vehicles": vehs, "props": props,
        "states": [states[c] for c in chars if c in states],
        "shot": s["shot"],
        "image_prompt": None if edit_only else image_prompt,
        "video_prompt": s["video"],
        "action_start": s["a0"], "action_end": s["a1"],
        "narration_ko": sc["nar"], "dialogue_ko": "\n".join(sc["dlg"]), "sound": sc["sound"],
        "continuity": s.get("cont", ""),
        "chain_from": s.get("chain"), "cut_half": bool(s.get("cut", False)),
        "aerial_quality": bool(s.get("aerial", False)), "ai_risk": s.get("risk", ""),
        "overlay_text": s.get("overlay"),
        "refs": [] if edit_only else refs,
        "image_body": None if edit_only else {
            "prompt": image_prompt, "model": "nano_banana_pro", "aspect_ratio": "16:9",
            "reference_images": [{"path": ref_path(r), "name": r} for r in refs],
        },
        "video_body": None if (not is_video or edit_only) else {
            "prompt": s["video"], "model": "veo_31_quality" if s.get("aerial") else "veo_31_fast",
            "mode": "start_image", "aspect_ratio": "16:9", "resolution": ["1080p"], "video_length": 8,
            "reference_images": [],
        },
        "video_ref_candidates": [] if (not is_video or edit_only) else refs[:2],
        "edit_only": edit_only,
        "insert_clip": s.get("insert"),
    }
    return rec

# ---------------------------------------------------------------- MD
def md_scene(r, sc):
    loc_line = f"{r['loc']}" + (f" ({r['subloc']})" if r['subloc'] != r['loc'] else "")
    chars = ", ".join(r["chars"] + r["extras"]) or "—"
    vehs = ", ".join(r["vehicles"]) or "—"
    props = ", ".join(r["props"]) or "—"
    kb = "video8s" if r["type"] == "video8s" else "still_kenburns"
    L = []
    L.append(f"### {r['id']} | {sc['t']} | {loc_line} | {chars} | {vehs} | PROPS: {props} | TYPE: {kb} | {r['seconds']}s")
    L.append(f"SHOT: {r['shot']}" + ("  · ⚑ AERIAL/QUALITY" if r["aerial_quality"] else ""))
    if r["edit_only"]:
        L.append("IMAGE_PROMPT: — (EDIT ONLY: end card đen + chữ ở khâu edit, không tạo ảnh AI)")
    else:
        L.append(f"IMAGE_PROMPT: {r['image_prompt']}")
    L.append(f"VIDEO_PROMPT: {r['video_prompt']}")
    L.append(f"ACTION_START: {r['action_start']}")
    L.append(f"ACTION_END: {r['action_end']}")
    L.append(f"NARRATION_KO: {r['narration_ko'] or '—'}")
    L.append("DIALOGUE_KO: " + (r["dialogue_ko"].replace("\n", " / ") if r["dialogue_ko"] else "—"))
    L.append(f"SOUND: {r['sound'] or '—'}")
    L.append(f"CONTINUITY: {r['continuity'] or '—'}")
    L.append(f"CHAIN_FROM: {r['chain_from'] or '—'}")
    L.append(f"CUT_HALF: {'yes' if r['cut_half'] else 'no'}")
    L.append(f"REFS: {', '.join(r['refs']) if r['refs'] else '—'}")
    if r["ai_risk"]:
        L.append(f"AI_RISK: {r['ai_risk']}")
    if r.get("overlay_text"):
        L.append(f"[OVERLAY] (edit): {r['overlay_text']}")
    if r.get("insert_clip"):
        L.append(f"INSERT_CLIP ({r['insert_clip']['seconds']} s, tách riêng): {r['insert_clip']['prompt']}")
    return "\n".join(L) + "\n"

HEADER = """# 살수 612 — 3화 「남하」 · SCENE LIST (VEO3 / G-Labs) · v1 · 2026-09-16 · veo-prompt-engineer
> Nguồn: `02_script/full_script_ep3.md` v2 QC-fixed (287 SC · 40:00) · `continuity_master.json` v3 (LOCKED: +VEH_207, PROP_024–026, LOC_009_SEOKMUN_PASS, LOC_010, 60 sub-lock, 72 derived) · character/location/vehicle/prop bible v3 · template 04 §C–§H · decisions.md.
> Format §C. Mỗi SC: IMAGE_PROMPT (ảnh keyframe 16:9, nano_banana_pro, ref ≤10) → VIDEO_PROMPT (veo_31_fast, mode start_image, 8 s, 1080p). still_kenburns = chỉ ảnh, ken-burns ở khâu edit.
> **Quy ước prompt:** tag `@<ref_id>` đứng trước lock (ví dụ `@CHAR_001_rain_ep3`, `@CHAR_105_radio_ep3`, `@LOC_009_detail`) — tag = đúng `name` trong `reference_images` để G-Labs bind chính xác. VISUAL_LOCK dán NGUYÊN VĂN từ continuity_master.json v3; derived state = `prompt_add` nguyên văn từ continuity_master.derived_states (ref = job → đính ref biến thể thay ref gốc; prompt_only → đính ref gốc/biến thể gần nhất). Trạng thái trong-tập do veo đặt (mưa/bùn/kính đêm trên mũ boonie/tù binh chưa mất patch…) ghi trong `logs/scratch/veo-ep3/build.py` DERIVED → đề xuất character-designer nhập bible. Không tên riêng, không chữ trong ảnh; Hangul trên xe KHÔNG vẽ (decisions #1); số pin/잔탄/giờ bay/bảng gỗ/thơ = `[OVERLAY]` ở edit.
> **Derived 3화 dùng đúng continuity_master:** CHAR_001_rain_ep3 (D2–D17, KHÔNG áo choàng — `rain_cloak_ep3` đã HỦY, script [ACTION-VI] còn ghi "áo choàng gai" → bỏ qua theo lock) · CHAR_002_k3_rain_ep3 (từ SC_246) · CHAR_003_rain_ep3 (D2+, biển "3" trên ba lô; D1 = hands_bandaged_ep2) · CHAR_005_captive_ep3 (từ SC_262 sau khi mất patch; SC_238–261 = biến thể còn patch) · CHAR_101_false_surrender_ep3 (SC_052–075) · CHAR_101_hall_seated_ep4 (lều D11) · CHAR_105_plain_robe_ep3 (giả hàng, cờ trắng) → CHAR_105_radio_ep3 (từ SC_112) · CHAR_106_rain_south_ep3 / forge_ep2 (lò rèn) · CHAR_107_scarf_ep2 → scarf_burnt_ep3 (từ SC_139 beat b) · CHAR_201_robe_only_ep3 (SC_132, cầm xác drone) · CHAR_202_tent_ep4 (D10 lều) · CHAR_205_magazine_ep2 (D1–D14) → CHAR_205_nvg_ep3 (từ SC_258, kính đêm dây quấn mũ lông).
> **Sub-lock địa điểm 3화:** LOC_003 Dạng A đêm cháy xe (`LOC_003_valley_*`) và Dạng B khe núi (`LOC_003_ravine_*`, ref bible `LOC_003_mobile`) · LOC_001 đồng bằng tháng 6 (xanh, mưa — KHÔNG dùng lock cỏ vàng 1화) · LOC_008 đường núi D2 / sơn thành D11 / làng dưới đèo D12–D14 · LOC_005 Áp Lục (đồi bờ nam, lều 우중문, bãi cuội, hố chôn lương, đường lầy bờ bắc) · LOC_009 석문령 (đường dê, mỏm đá, yên đèo đêm, đá lở, mộ, trại Tiên Ti) · LOC_007 살수 P12. Toàn bộ ghi `02_script/sublocks_ep3.md` — DÙNG NGUYÊN VĂN mọi SC.
> **Nhân vật phụ không ID** (소년 척후, 유사룡, 수 전령/기병 사자/총관/낙오병/척후, 고구려 전령/통역 포로/척후, PZF·박격포·K3 사수, 조종수/포수, 무전병, 선비 부장, dân làng, 40 con bò): lock tạm cố định (build.py EXTRAS) — mặt lính phụ luôn quay đi/khuất mũ để né drift. Kỵ Tùy = VEH_207 (rules.sui_cavalry_id), Tiên Ti = VEH_206, 개마무사 = VEH_101. Radio cầm tay của 해모루/한승우 = mô tả trong state/action (`RADIO_HANDHELD`), lock EQP_002 chỉ dán khi là máy đeo lưng.
> **Quy tắc 8 s (§F):** 1 SC = 1 địa điểm, 1 hành động chính, ≤2 người nói, 1 chuyển động camera. `CUT_HALF: yes` = hook 0–32 s + các khối trận (P1 PZF, P2 khe đồi, P4 K6, P5 trận giả thua, P7 hậu vệ/tên lửa, P8 cướp ruộng, P9 소년 척후/cửa nam, P10 Phase 2–4) → edit cắt 2 shot 4 s; 2-BEAT script (SC_001/003/010/070/139/178/228/229) + 12 clip veo-stage P10 (SC_208/210/211/212/216/217/221/223/225/229/231/236) mô tả Beat A/B trong VIDEO_PROMPT. Đại quân = aerial wide (⚑ AERIAL/QUALITY → veo_31_quality cho video, nano_banana_pro + upscale 2K cho ảnh).
> **CHAIN_FROM:** chỉ khi SC trước là video8s, cùng địa điểm + nhân vật, hành động nối tiếp → glabs-operator lấy tail-frame làm start_image (tools/glabs_client.py `--chain`). Không chain quá 3 clip liên tiếp (drift).
> **Ánh sáng theo bảng ngày/đêm (header script):** D1 đêm lửa (001–011) · D2 ngày mưa phùn (012–022) → đêm (023–032) · D3 đêm mưa khe núi (033–045) · D4 rạng sáng (046–050) · D9 Áp Lục sáng sương → chiều mưa (051–075) · D10 sáng lều → ngày mưa (076–101) → đêm bờ bắc (126–131) · D6 육합성 sáng (132) · D11 rạng sáng bờ bắc (133) / đêm sơn thành (102–125) · D12 ngày → hoàng hôn → đêm (134–172) · D14 rạng sáng → trưa → chiều → hoàng hôn (173–198) → đêm đèo (199–238) · D15 rạng đông (239–256) → đêm trại Tiên Ti (257–263, 269–270) · D16 ngày mưa (264–268) · D17 chiều mưa 살수 (271–286). Mưa/bùn/râu 3–5 ngày trên lính từ D2.
> **Style tag (§D, cuối mọi image prompt):** `{style}`
> **Negative (§E, ghi 1 lần — glabs-operator dán vào field negative nếu model hỗ trợ):** `{neg}`
> **QC ảnh §G / QC video §H** áp dụng trước khi tạo video; ảnh fail → regenerate ≤3 lần (đổi seed / đơn giản hoá prompt), vẫn fail → giảm số nhân vật trong khung.

"""

PART_TITLES = {
    1: "[Phần 1] 불타지 않은 3호 (0:00–1:30) · hook, không narrator 0–32 s, đốt xe · 2-BEAT SC_001/003/010",
    2: "[Phần 2] 밥을 묻는 군대 (1:30–4:30) · hai cột song song, kỵ Tùy cánh sườn, lính Tùy chôn lương [史]",
    3: "[Phần 3] 드론 한 번, 전차 600미터 (4:30–7:00) · trạm dừng khe núi, kiểm kê, đổi ngựa · MID-ROLL 1 @7:00",
    4: "[Phần 4] 거짓 항복 (7:00–10:30) · 압록수, 을지문덕 giả hàng [史], 필담, K6 xuống nước · 2-BEAT SC_070",
    5: "[Phần 5] 지는 것도 병법이오 (10:30–14:00) · 우문술/우중문 [史], 9 quân vượt sông, trận giả thua, 천둥 3 bò kéo · narrator im 12:02–13:02 · MID-ROLL 2 @14:00",
    6: "[Phần 6] 이유는 그때 말하겠소 (14:00–17:30) · sơn thành đêm, lều 을지문덕, radio cho 해모루, 척후 phía nam",
    7: "[Phần 7] 쇠수레는 산을 못 넘는다 (17:30–21:00) · ENEMY 탁발흠 trong 천둥 3, bịt tai ngựa, 양제 1 SC, K2 rò nước, tên lửa · 2-BEAT SC_139 · MID-ROLL 3 @21:00",
    8: "[Phần 8] 전차냐, 시간이냐 (21:00–24:00) · cướp ruộng, quyết vá, 40%, ngủ, 을보 gò đồng, 탁발흠 thả 3 척후",
    9: "[Phần 9] 석문령, 마흔 분 (24:00–27:30) · vá xong, bàn cát, 소년 척후 (2-BEAT SC_178), cửa nam, '너무 높다', lên đèo · MID-ROLL 4 @27:30",
    10: "[Phần 10] 고개의 밤 (27:30–34:30) · 6 phase · narrator im 31:32–33:00 · CUT_HALF toàn khối Phase 2–4 · 2-BEAT 12 clip veo-stage",
    11: "[Phần 11] 밤이 낮이 되었다 (34:30–37:30) · chôn KIA kiểu Goguryeo, tách 해모루, ENEMY kính đêm, hỏi cung, patch bị giật, 우중문 tiến [史]",
    12: "[Phần 12] 30만이 지나가게 두시오 (37:30–40:00) · 살수 lần đầu, lệnh '숨으시오', nước lên, end card",
}

def validate(recs):
    errs = []
    ids = [r["id"] for r in recs]
    exp = [f"SC_{i:03d}" for i in range(1, N_SC + 1)]
    if ids != exp:
        missing = sorted(set(exp) - set(ids)); extra = sorted(set(ids) - set(exp))
        errs.append(f"ID mismatch: missing={missing[:10]} extra={extra[:10]} n={len(ids)}")
    t = 0
    run = 0
    for r in recs:
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
            for p in r["props"]:
                if LOCKS[p] not in r["image_prompt"]: errs.append(f"{r['id']} lock {p} not verbatim")
            for tok in ("한승우", "오태민", "Han ", "Tae-min", "Eulji", "Tuoba", "Yang Guang", "Ki-cheol", "Seo-ah", "Tae-oh", "Seong-min",
                        "Hae Mo", "Jeong-su", "Eul-bo", "A-ri", "Zhongwen", "Yuwen", "Salong", "Mundeok"):
                if tok in r["image_prompt"] or tok in r["video_prompt"]: errs.append(f"{r['id']} proper name '{tok}' in prompt")
            if r["type"] == "video8s" and r["cut_half"] is False and r["part"] == 10 and 207 <= int(r["id"][3:]) <= 241:
                errs.append(f"{r['id']} P10 battle clip without cut_half")
        if r["chain_from"]:
            prev = recs[ids.index(r["chain_from"])]
            if prev["type"] != "video8s": errs.append(f"{r['id']} chain_from {r['chain_from']} is not video8s")
            if int(r["chain_from"][3:]) != int(r["id"][3:]) - 1: errs.append(f"{r['id']} chain_from {r['chain_from']} not previous SC")
            run += 1
            if run > 3: errs.append(f"{r['id']} chain run > 3")
        else:
            run = 0
    if t != 2400: errs.append(f"total seconds {t} != 2400")
    return errs

def usage_report(recs):
    cnt_char = collections.Counter(); cnt_state = collections.Counter(); cnt_loc = collections.Counter(); cnt_sub = collections.Counter()
    cnt_veh = collections.Counter(); cnt_prop = collections.Counter(); cnt_ref = collections.Counter(); cnt_extra = collections.Counter()
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
    authored = load_batches()
    recs = []
    for s in authored:
        recs.append(build_scene(s, sc[s["id"]]))
    recs.sort(key=lambda r: r["id"])
    errs = validate(recs)
    if errs:
        print("VALIDATION ERRORS:"); print("\n".join(errs))
        if "--force" not in sys.argv: sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    md = [HEADER.replace("{style}", STYLE).replace("{neg}", NEGATIVE)]
    nv = sum(1 for r in recs if r["type"] == "video8s"); ns = len(recs) - nv
    md.append(f"**Tổng:** {len(recs)} SC · {nv} video8s · {ns} still_kenburns · {sum(r['seconds'] for r in recs)} s · chain_from: {sum(1 for r in recs if r['chain_from'])} · cut_half: {sum(1 for r in recs if r['cut_half'])} · aerial/quality: {sum(1 for r in recs if r['aerial_quality'])} · overlay: {sum(1 for r in recs if r.get('overlay_text'))} · edit_only: {sum(1 for r in recs if r['edit_only'])}\n\n---\n")
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
    print(f"OK {len(recs)} SC · video {nv} · still {ns} · chain {sum(1 for r in recs if r['chain_from'])} · cut_half {sum(1 for r in recs if r['cut_half'])} · aerial {sum(1 for r in recs if r['aerial_quality'])}")

# ---------------------------------------------------------------- SUBLOCKS MD
def write_sublocks(recs):
    cnt_sub = collections.Counter(r["subloc"] for r in recs)
    sc_by_sub = collections.defaultdict(list)
    for r in recs: sc_by_sub[r["subloc"]].append(int(r["id"][3:]))
    def rng(nums):
        nums = sorted(nums); out = []; i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1: j += 1
            out.append(f"{nums[i]:03d}" if i == j else f"{nums[i]:03d}–{nums[j]:03d}"); i = j + 1
        return f"{len(nums)} SC: " + ", ".join(out)
    L = ["# 살수 612 — SUB-LOCK ĐỊA ĐIỂM 3화 「남하」 (veo-prompt-engineer · 2026-09-16 · chờ DUYỆT)",
         "> Mỗi sub-lock = 1 đoạn VISUAL_LOCK_EN cố định cho một khu vực/buổi của LOC gốc; đã dán NGUYÊN VĂN vào mọi SC tương ứng trong `04_veo/scene_list_ep3.md`. Dòng `(bible)` = lấy nguyên văn VISUAL_LOCK / REF_PROMPT_EN_* / sublocks của continuity_master v3 (bỏ đuôi 'no people' + style tag); dòng `(mới)` = veo-prompt-engineer đặt cho 3화 → world-designer nhập vào location_bible + continuity_master.sublocks; các tập sau dùng lại đúng id. Nguồn máy: `logs/scratch/veo-ep3/build.py` SUBLOC.",
         "> Quy tắc dùng: cảnh wide/aerial → lock gốc LOC_xxx; cảnh medium/cận/nội thất → sub-lock của khu vực; luôn thêm câu Light theo bảng ngày/đêm; kết bằng style tag §D. Tháng 6/612: mọi LOC 3화 XANH + mưa — không dùng sub-lock cỏ vàng 1화/2화 (LOC_001/002/003 Dạng A cũ). Ref đính `(mới)` = chưa có job → `05_references/extra/ref_jobs_ep3_extra.json`.",
         "",
         "| # | id sub-lock | LOC gốc | Ref đính (`reference_images`) | Dùng cho (buổi / cảnh) | SC 3화 | VISUAL_LOCK_EN (nguyên văn) |",
         "|---|---|---|---|---|---|---|"]
    bible_keys = {"LOC_005", "LOC_008", "LOC_009", "LOC_007", "LOC_004_pavilion_int", "LOC_003_ravine"}
    i = 0
    for k, (loc, ref, text) in SUBLOC.items():
        if k not in cnt_sub: continue
        i += 1
        tag = "(bible)" if k in bible_keys else "(mới)"
        reftag = f"`{ref}`" + (" (mới)" if ref in NEW_REFS else "")
        L.append(f"| {i} | `{k}` {tag} | {loc} | {reftag} | {SUB_USE.get(k, '—')} | {rng(sc_by_sub[k])} | {text} |")
    L.append("")
    L.append("## Sub-lock KHÔNG dùng trong 3화 nhưng đã định nghĩa (dự phòng)")
    unused = [k for k in SUBLOC if k not in cnt_sub]
    L.append(", ".join(f"`{k}`" for k in unused) if unused else "—")
    open(f"{PROJ}/02_script/sublocks_ep{EP}.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

SUB_USE = {
    "LOC_003_valley_fire": "D1 đêm — thung lũng sau 요동성, xe cháy (wide)", "LOC_003_valley_k21": "D1 đêm — cạnh 천둥 3 (medium/cận)",
    "LOC_003_valley_westledge": "D1 đêm — gờ đá tây, 백성민 nhìn đuốc", "LOC_003_valley_mouth": "D1 đêm — cửa thung, xuất phát",
    "LOC_003_valley_k21_rain": "D1 đêm — 천둥 3 một mình, mưa bắt đầu (still kết P1)",
    "LOC_003_ravine": "D3 đêm — trạm dừng Dạng B (wide)", "LOC_003_ravine_k2rear": "D3 đêm — đuôi K2, sạc 'bạch tuộc'",
    "LOC_003_ravine_poncho": "D3 đêm — dưới poncho (hộp drone)", "LOC_003_ravine_hearth": "D3 đêm — bếp đá, cháo kê",
    "LOC_003_ravine_mouth": "D3 đêm / D4 rạng sáng — cửa khe, ngựa", "LOC_003_ravine_tent": "D3 đêm — lều chỉ huy đèn đỏ",
    "LOC_003_ravine_stream_nvg": "D3 đêm — suối rìa trại (POV kính đêm)",
    "LOC_001_plain_night_aerial": "D1/D2 đêm — aerial dòng sông lửa trại Tùy", "LOC_001_plain_road": "D2 ngày — đường quân Tùy lầy mưa",
    "LOC_001_plain_camp_night": "D2 đêm — trại Tùy, sĩ quan đèn lồng", "LOC_001_plain_camp_tent_edge": "D2 đêm — hố chôn lương cận (still)",
    "LOC_008_aerial_split": "D2 ngày — aerial hai cột song song", "LOC_008_mountain_road": "D2 ngày / D4–D8 — đường núi mưa phùn",
    "LOC_008_road_pine": "D2 — gốc thông bên đường (băng chân)", "LOC_008_road_bend_amnok": "D8 chiều — khúc cua thấy Áp Lục (still)",
    "LOC_008_ridge_day": "D2 ngày — gờ đồi nhìn xuống đồng bằng", "LOC_008_hill_gap": "D2 ngày — khe đồi, kỵ chặn kỵ",
    "LOC_008_ridge_night": "D2 đêm — gờ đá nhìn lửa trại",
    "LOC_008_hill_fort": "D11 đêm mưa — sơn thành nhỏ (wide)", "LOC_008_fort_tent": "D11 đêm — trong lều 을지문덕",
    "LOC_008_fort_yard": "D11 đêm — sân sơn thành, K2 cạnh kho thóc", "LOC_008_fort_granary_shed": "D11 đêm — mái che kho thóc (서아/아리)",
    "LOC_008_fort_wall": "D11 đêm — tường sơn thành, chòi canh (radio)", "LOC_008_fort_gate": "D11 đêm — cổng gỗ",
    "LOC_008_fort_trail": "D11 đêm — đường mòn dưới sơn thành (POV kính đêm)", "LOC_008_fort_tent_ext": "D11 đêm — lều 을지문덕 nhìn ngoài (still)",
    "LOC_008_fort_aerial": "D11 đêm — aerial sơn thành (still)",
    "LOC_008": "D12–D14 — làng dưới chân đèo (lock gốc, wide)", "LOC_008_village_street": "D12 — K2 vào làng",
    "LOC_008_village_k2": "D12–D14 — K2 cạnh kho thóc + dây sạc", "LOC_008_village_forge": "D12 đêm — lò rèn (bible detail)",
    "LOC_008_village_forge_day": "D12 chiều — lò rèn ban ngày", "LOC_008_village_terraces": "D12 chạng vạng — ruộng bậc thang bị cướp",
    "LOC_008_village_edge": "D12 chạng vạng — mép làng nhìn xuống ruộng", "LOC_008_village_porch": "D12 đêm — hiên nhà, kính đêm sạc",
    "LOC_008_village_house_int": "D12 đêm — trong nhà gỗ, sàn 구들", "LOC_008_village_granary_floor": "D12 đêm — sàn kho thóc (한승우 ngủ)",
    "LOC_008_village_night_wide": "D12 đêm — làng đêm, chỉ lò rèn sáng (still)", "LOC_008_village_gate": "D12 đêm — cổng rào, 소년 척후 đi",
    "LOC_008_village_fort_wall": "D12 đêm — tường sơn thành nhỏ trên làng (POV kính đêm sương)", "LOC_008_village_sandtable": "D14 sáng — bàn cát bùn",
    "LOC_008_village_k2_side": "D14 sáng — hông tháp K2 phấn vẽ (still)", "LOC_008_village_upward": "D12 đêm — từ làng ngước lên đèo (still)",
    "LOC_008_village_terraces_up": "D12 — từ ruộng ngước lên làng + đèo (still)",
    "LOC_005": "D9/D10/D16 — Áp Lục (lock gốc, aerial)", "LOC_005_south_hill": "D9 — mỏm đá bờ nam (K6, ống nhòm, drone)",
    "LOC_005_south_forest": "D9/D10 — rừng thông bờ nam (을지문덕 lệnh, kỵ gom)", "LOC_005_south_forest_edge": "D9 rạng sáng — mép rừng (giả hàng)",
    "LOC_005_mortar_pit": "D10 — hố cối 10 viên", "LOC_005_south_ledge_k3": "D10 — gờ đá K3 (오태민 bị cấm)",
    "LOC_005_shoal_south": "D10 — bãi cuội bờ nam (trận giả thua)", "LOC_005_ford": "D9 — bãi cạn (K6 xuống nước, 을지문덕 lội)",
    "LOC_005_shoal_north": "D9 — bãi cuội bờ bắc (50 kỵ đuổi)", "LOC_005_camp_edge_pits": "D9 — hố chôn lương bờ bắc (màn hình drone)",
    "LOC_005_camp_lane": "D9 — lối đi giữa hai hàng lính Tùy", "LOC_005_camp_gate": "D9 — cổng trại Tùy",
    "LOC_005_sui_tent": "D9 — lều 우중문 (필담)", "LOC_005_sui_tent_2": "D10 sáng — lều 우문술 (thẻ tre)",
    "LOC_005_north_road": "D10/D16 — đường lầy bờ bắc (천둥 3 bò kéo)", "LOC_005_north_road_night": "D10 đêm — 천둥 3 đậu bên đường",
    "LOC_005_north_fire": "D10 đêm — đống lửa, bản đồ bùn", "LOC_005_north_horses": "D10 đêm — bãi ngựa bịt tai",
    "LOC_005_north_horses_dawn": "D11 rạng sáng — 2.000 kỵ lên yên", "LOC_005_sui_road_tent": "D16 — lều 우중문 bên đường nam",
    "LOC_005_aerial_south": "D16 — aerial cột quân về nam",
    "LOC_004_pavilion_int": "D6 sáng — lầu vàng 육합성 (양제 cầm xác drone)",
    "LOC_009": "D14 — đèo (lock gốc, aerial hoàng hôn/bình minh)", "LOC_009_east_road": "D12/D14 — đường dốc chân đèo phía đông",
    "LOC_009_east_road_ledge": "D12 — gờ đá trên đường (tên lửa)", "LOC_009_north_ledge": "D12 — gờ núi bắc (백성민 nhìn cột Tùy)",
    "LOC_009_goat_path": "D12 — đường dê (phân ngựa)", "LOC_009_goat_path_fog": "D12 đêm — đường dê sương (3 척후 dưới cung)",
    "LOC_009_far_ridge": "D12 hoàng hôn — gờ núi xa (탁발흠 nhìn làng)", "LOC_009_xianbei_forest": "D12 — bãi ngựa Tiên Ti trong rừng (still)",
    "LOC_009_south_gate": "D14 trưa/đêm — cửa nam (해모루)", "LOC_009_east_foot": "D14 chiều — chân đèo, ngước lên mỏm",
    "LOC_009_saddle_dusk": "D14 hoàng hôn — yên đèo (still)", "LOC_009_saddle_night": "D14 đêm — yên đèo (wide đêm)",
    "LOC_009_barrier_gap": "D14 đêm — K2 trong khoảng hở ải đá", "LOC_009_barrier_line": "D14 đêm — dọc chân ải đá (80 người)",
    "LOC_009_outcrop_path": "D14 đêm — đường mòn lên mỏm", "LOC_009_outcrop_top": "D14 đêm — đỉnh mỏm đá (태오)",
    "LOC_009_outcrop_top_dawn": "D15 rạng đông — đỉnh mỏm trống", "LOC_009_nw_cliff": "D14 đêm — vách tây-bắc (trước đuốc)",
    "LOC_009_nw_cliff_torches": "D14 đêm — vách tây-bắc đuốc", "LOC_009_goat_path_foot": "D14 đêm — chân đường dê vào yên",
    "LOC_009_goat_path_upper": "D14 đêm — đoạn trên đường dê (탁발흠)", "LOC_009_cliff_top_above_outcrop": "D14 đêm — đỉnh vách trên mỏm (dây)",
    "LOC_009_rockslide": "D14 đêm — đá lở", "LOC_009_saddle_dawn": "D15 rạng đông — yên đèo sau trận (bible aftermath)",
    "LOC_009_south_flat": "D15 sáng — nền đất chôn KIA", "LOC_009_grave": "D15 sáng — mộ (still)",
    "LOC_009_south_descent": "D15 sáng — đường xuống phía nam", "LOC_009_south_foot": "D15 — ngã ba dưới đèo (still)",
    "LOC_009_cliff_top_far": "D15 rạng đông — đỉnh vách xa (탁발흠 + 태오)", "LOC_009_xianbei_camp_night": "D15 đêm — trại Tiên Ti cao nguyên",
    "LOC_009_xianbei_camp_pine": "D15 đêm — gốc thông (태오 bị trói)", "LOC_009_trail_night": "D16 đêm — đường mòn, 탁발흠 đi đêm (still)",
    "LOC_007": "D17 — 살수 (lock gốc, aerial)", "LOC_007_north_sand": "D17 — bãi cát bắc mép lau", "LOC_007_reeds_arrival": "D17 — trong bãi lau (아리)",
    "LOC_007_water_edge": "D17 — mép nước, cành đo nước", "LOC_007_aerial_reeds": "D17 — aerial bãi lau (still)",
}

# ---------------------------------------------------------------- REF JOBS (ep3 extra)
REF_JOB_PROMPTS = {
    "LOC_003_valley_fire_ep3": ("locations", "LOC_003_valley_fire", 1),
    "LOC_001_plain_rain_ep3": ("locations", "LOC_001_plain_road", 3),
    "LOC_008_mountain_road_ep3": ("locations", "LOC_008_mountain_road", 2),
    "LOC_008_hill_fort_ep3": ("locations", "LOC_008_hill_fort", 1),
    "LOC_005_south_hill_ep3": ("locations", "LOC_005_south_hill", 1),
    "LOC_005_sui_tent_ep3": ("locations", "LOC_005_sui_tent", 2),
    "LOC_009_saddle_night_ep3": ("locations", "LOC_009_saddle_night", 1),
    "LOC_009_outcrop_ep3": ("locations", "LOC_009_outcrop_top", 2),
    "LOC_009_xianbei_camp_ep3": ("locations", "LOC_009_xianbei_camp_night", 2),
}
def write_ref_jobs(recs):
    cnt_ref = collections.Counter(x for r in recs for x in r["refs"])
    jobs = []
    for rid, (d, subkey, prio) in REF_JOB_PROMPTS.items():
        text = SUBLOC[subkey][2]
        jobs.append({"id": rid, "type": "image", "priority": prio, "sc_count": cnt_ref[rid], "out_dir": f"05_references/{d}",
                     "used_by_sublock": subkey,
                     "body": {"prompt": f"Wide establishing reference shot, 16:9. {text}, no people in frame, no modern structures other than the listed vehicles, {STYLE}",
                              "model": "nano_banana_pro", "aspect_ratio": "16:9"}})
    jobs.append({"id": "VEH_001_mule_ep3", "type": "image", "priority": 1, "sc_count": cnt_ref["VEH_001_mule_ep3"], "out_dir": "05_references/vehicles",
                 "used_by_state": "K2_MULE",
                 "body": {"prompt": f"Product-style reference photo, three-quarter rear-left view, 16:9. {LOCKS['VEH_001']} {VEH_STATE['K2_MULE']} Pure white background, even studio lighting, {STYLE}",
                          "model": "nano_banana_pro", "aspect_ratio": "16:9"}})
    jobs.append({"id": "EXTRA_xianbei_deputy_ref", "type": "image", "priority": 2, "sc_count": cnt_ref["EXTRA_xianbei_deputy_ref"], "out_dir": "05_references/characters",
                 "used_by_extra": "XIANBEI_DEPUTY",
                 "body": {"prompt": f"Character reference sheet, two views side by side: full body and head-and-shoulders, 3:4. {EXTRAS['XIANBEI_DEPUTY']}, standing, neutral expression, pure white background, even studio lighting, no shadows, {STYLE}",
                          "model": "nano_banana_pro", "aspect_ratio": "3:4"}})
    os.makedirs(f"{PROJ}/05_references/extra", exist_ok=True)
    json.dump(jobs, open(f"{PROJ}/05_references/extra/ref_jobs_ep{EP}_extra.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

def write_usage(recs):
    cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra = usage_report(recs)
    L = ["# 3화 「남하」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)",
         "> Đếm theo `04_veo/scenes_ep3.json` (287 SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro. Lock = continuity_master.json v3.", ""]
    L.append("## 1. Nhân vật (CHAR) — số SC xuất hiện")
    L.append("| CHAR | SC | Derived state trong 3화 (SC) |"); L.append("|---|---|---|")
    for c, n in sorted(cnt_char.items()):
        sts = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_state.items()) if k.startswith(c))
        L.append(f"| {c} | {n} | {sts or '— (base)'} |")
    L.append(""); L.append("### Trạng thái do veo-prompt-engineer đặt cho 3화 (chưa có trong continuity_master → đề xuất character-designer nhập bible)")
    for k, (c, ref, txt) in DERIVED.items():
        if k in CM_DERIVED: continue
        L.append(f"- `{k}` ({c}, đính `{ref}`, {cnt_state.get(k, 0)} SC): {txt}")
    L.append(""); L.append("### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)")
    L.append("| Extra | SC | ref đính |"); L.append("|---|---|---|")
    for e, n in cnt_extra.most_common(): L.append(f"| {e} | {n} | {EXTRA_REF.get(e, '—')} |")
    L.append(""); L.append("## 2. Địa điểm (LOC) — số SC")
    L.append("| LOC | SC | Sub-lock (SC) |"); L.append("|---|---|---|")
    for l, n in sorted(cnt_loc.items()):
        subs = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_sub.items()) if k.startswith(l))
        L.append(f"| {l} | {n} | {subs} |")
    L.append(""); L.append("## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/UAV/EQP) — số SC")
    L.append("| ID | SC |"); L.append("|---|---|")
    for v, n in cnt_veh.most_common(): L.append(f"| {v} | {n} |")
    L.append(""); L.append("### Trạng thái xe 3화 (build.py VEH_STATE — theo vehicle_bible damage state 3화)")
    for k, v in VEH_STATE.items(): L.append(f"- `{k}`: {v}")
    L.append(""); L.append("## 4. Đạo cụ (PROP) — số SC")
    L.append("| PROP | SC |"); L.append("|---|---|")
    for p, n in cnt_prop.most_common(): L.append(f"| {p} | {n} |")
    L.append(""); L.append("## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)")
    L.append("| # | ref id | thư mục | số SC đính | trạng thái |"); L.append("|---|---|---|---|---|")
    for i, (r, n) in enumerate(cnt_ref.most_common(), 1):
        status = "**CHƯA CÓ — job trong ref_jobs_ep3_extra.json**" if r in NEW_REFS else ("có job (ep1 extra)" if r in ("LOC_003_hollow_d1", "LOC_003_ford_night", "LOC_008_steppe_ep1", "LOC_003_steppe_d1", "EXTRA_boy_scout_ref", "WPN_102_ref", "EXTRA_sui_vanguard_general_ref") else "có job (bible)")
        L.append(f"| {i} | {r} | {REF_DIR[r]} | {n} | {status} |")
    L.append("")
    L.append("### Ref CHƯA CÓ (11) — `05_references/extra/ref_jobs_ep3_extra.json` (glabs-operator tạo trước lô ảnh cảnh; world-designer/character-designer duyệt)")
    L.append("- `LOC_003_valley_fire_ep3` (locations): thung lũng sau 요동성 đêm D1, xe cháy, cỏ xanh tháng 6 — sub-lock `LOC_003_valley_fire`.")
    L.append("- `LOC_001_plain_rain_ep3` (locations): đồng bằng đông 요동성 tháng 6 — đường lầy, cỏ xanh, mưa — sub-lock `LOC_001_plain_road` (LOC_001 lock gốc là cỏ vàng đầu xuân → KHÔNG dùng cho 3화).")
    L.append("- `LOC_008_mountain_road_ep3` (locations): đường núi bùn đỏ, thông + sồi non, mưa phùn — sub-lock `LOC_008_mountain_road` (P2/P3, montage D4–D8).")
    L.append("- `LOC_008_hill_fort_ep3` (locations): sơn thành nhỏ đêm mưa, cổng gỗ + đuốc, kho thóc nâng sàn, lều 삼족오 — sub-lock `LOC_008_hill_fort` (P6, 24 SC).")
    L.append("- `LOC_005_south_hill_ep3` (locations): mỏm đá dưới tán thông bờ nam nhìn xuống bãi cuội + trại Tùy — sub-lock `LOC_005_south_hill` (P4/P5).")
    L.append("- `LOC_005_sui_tent_ep3` (locations): lều 우중문 sàn ván ướt, ghế gấp, bàn bút lụa — sub-lock `LOC_005_sui_tent` (P4/P5/P11, 12 SC).")
    L.append("- `LOC_009_saddle_night_ep3` (locations): yên đèo đêm, ải đá hở 5 m, đèn sạc đỏ — sub-lock `LOC_009_saddle_night` (P10 wide; cận dùng bible `LOC_009_detail`).")
    L.append("- `LOC_009_outcrop_ep3` (locations): đỉnh mỏm đá 10×10 m cao 200 m — sub-lock `LOC_009_outcrop_top` (P10 태오, 10 SC).")
    L.append("- `LOC_009_xianbei_camp_ep3` (locations): trại Tiên Ti cao nguyên đêm D15, lửa dưới thông, ngựa bịt tai — sub-lock `LOC_009_xianbei_camp_night` (P11).")
    L.append("- `VEH_001_mule_ep3` (vehicles, 16:9): K2 'con la' — K6 + ống cối + hộp đạn buộc đuôi, cành thông nóc, bùn nửa thân, mất 1 tấm váy xích trái — dùng cho ~70 SC K2 từ D4 (state `K2_MULE*`).")
    L.append("- `EXTRA_xianbei_deputy_ref` (characters, 3:4): 선비 부장 (phó của 탁발흠) — 9 SC ENEMY POV; cần ref riêng để không trộn với 탁발흠 (không sẹo, có ria, ~30).")
    L.append("")
    L.append("### Thứ tự chạy ref đề xuất (P1 → P3)")
    L.append("- **P1 (≥15 SC):** " + ", ".join(r for r, n in cnt_ref.most_common() if n >= 15))
    L.append("- **P2 (5–14 SC):** " + ", ".join(r for r, n in cnt_ref.most_common() if 5 <= n < 15))
    L.append("- **P3 (<5 SC):** " + ", ".join(r for r, n in cnt_ref.most_common() if n < 5))
    L.append("")
    L.append("## 6. SC cần ảnh ĐẠI QUÂN / AERIAL (⚑ → ảnh nano_banana_pro + upscale 2K; video veo_31_quality)")
    aer = [r for r in recs if r["aerial_quality"]]
    L.append("| SC | t | type | nội dung |"); L.append("|---|---|---|---|")
    for r in aer: L.append(f"| {r['id']} | {r['t_start']//60}:{r['t_start']%60:02d} | {r['type']} | {r['shot']} |")
    L.append("")
    L.append("## 7. SC RỦI RO AI & cách né trong prompt")
    risk = [r for r in recs if r["ai_risk"]]
    L.append("| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |"); L.append("|---|---|---|")
    for r in risk: L.append(f"| {r['id']} | {r['ai_risk'].split('→')[0].strip()} | {r['ai_risk'].split('→')[1].strip() if '→' in r['ai_risk'] else '—'} |")
    L.append("")
    L.append("## 8. [OVERLAY] ở edit (số/chữ KHÔNG vẽ trong ảnh)")
    L.append("| SC | overlay |"); L.append("|---|---|")
    for r in recs:
        if r.get("overlay_text"): L.append(f"| {r['id']} | {r['overlay_text']} |")
    L.append("")
    L.append("### Quy tắc né chung (áp dụng toàn tập)")
    L.append("- **Đám đông cận**: mọi cảnh ≥6 người → wide/aerial hoặc máy sau lưng hàng người, mặt lính phụ quay đi/khuất mũ; chỉ nhân vật có ID mới thấy mặt rõ. Trại Tùy/bãi cuội/vượt sông = aerial hoặc trung cảnh 'không thấy điểm cuối'.")
    L.append("- **Chữ**: màn hình drone/tablet/bảng gỗ/lụa 필담/thẻ tre/thơ → prompt chỉ 'brush calligraphy / blurred marker figures / empty dark screen'; số thật overlay ở edit (decisions #1, #6). Biển '3' chỉ số Ả Rập.")
    L.append("- **Tay cầm súng**: K2C1/K3 'muzzle down / slung / resting on stones'; bắn = wide hoặc chớp lửa đầu nòng, không cận ngón tay trên cò. K6 = xạ thủ tì vai, mặt sau thước ngắm.")
    L.append("- **Ngựa + kỵ sĩ số đông**: aerial/tracking thấp, mưa/bụi che chi tiết chân ngựa; không cận vó. 40 con bò = wide, hai hàng, người đánh bò quay lưng.")
    L.append("- **POV kính đêm / màn hình drone / nhiệt**: 'monochrome green night-vision view with grain' / 'white-hot thermal aerial view' — không vẽ HUD số; overlay ở edit.")
    L.append("- **Xe + nước/hơi nước/lửa** (SC_003–004, 134–135, 227–230): 1 hiện tượng vật lý rõ (hơi trắng / chớp nòng / thác đá), máy tĩnh.")
    L.append("- **Mưa**: mọi SC D2+ có 'rain/drizzle' trong Light — không vẽ tia mưa dày che mặt; ướt bề mặt + hạt mưa trên vai/ống kính.")
    L.append("- **Hangul trên xe**: KHÔNG vẽ (chỉ số Ả Rập 1/2/3 + 태극기 nhỏ); '천둥' chỉ ở thoại/radio.")
    open(f"{OUT_DIR}/ep{EP}_asset_usage.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
