# -*- coding: utf-8 -*-
"""
VEO scene-list builder — SALSU_612 · 2화 「요동성」 (copy từ veo-ep1/build.py, sửa cho tập 2)
Đọc: full_script_ep2.md v2 (t / type / narration / thoại / [SOUND] — nguyên văn) + continuity_master.json (VISUAL_LOCK nguyên văn)
      + batch_XX.py (dữ liệu hình ảnh do veo-prompt-engineer biên).
Ghi: 04_veo/scene_list_ep2.md · 04_veo/scenes_ep2.json · 04_veo/ep2_asset_usage.md · output/ep2/kich_ban/scene_list.md
"""
import json, re, os, sys, glob, importlib.util, collections

ROOT = "/Users/admin/phim han quoc"
PROJ = ROOT + "/projects/SALSU_612"
SCRIPT = PROJ + "/02_script/full_script_ep2.md"
CM = json.load(open(PROJ + "/continuity_master.json", encoding="utf-8"))
OUT_DIR = PROJ + "/04_veo"
HERE = os.path.dirname(os.path.abspath(__file__))
EP = 2
N_SC = 287

STYLE = CM["style_tag"]
NEGATIVE = ("cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, "
            "modern buildings in historical scene, anachronistic clothing")

# ---------------------------------------------------------------- LOCKS (nguyên văn continuity_master.json)
LOCKS = {}
LOCKS.update(CM["character_locks"]); LOCKS.update(CM["vehicle_locks"]); LOCKS.update(CM["prop_locks"])
LOCKS["PROP_004"] = CM["vehicle_locks"]["EQP_001"]
LOC_LOCK = {k.split("_")[0] + "_" + k.split("_")[1]: v for k, v in CM["location_locks"].items()}

# ---------------------------------------------------------------- REF SHEET IDS (05_references/*/ref_jobs.json + ep1 extra) + refs CẦN TẠO 2화
REF_DIR = {}
for d in ("characters", "locations", "vehicles", "props"):
    for j in json.load(open(f"{PROJ}/05_references/{d}/ref_jobs.json", encoding="utf-8")):
        REF_DIR[j["id"]] = d
for j in json.load(open(f"{PROJ}/05_references/extra/ref_jobs_ep1_extra.json", encoding="utf-8")):
    REF_DIR[j["id"]] = j["out_dir"].split("/")[-1]  # ep1 extra (đã DUYỆT decisions P-38…45): LOC_003_hollow_d1, LOC_003_ford_night, WPN_102_ref, EXTRA_boy_scout_ref…
NEW_REFS = {  # 2화 — chưa có job → 05_references/extra/ref_jobs_ep2_extra.json (xem ep2_asset_usage.md §5)
    "LOC_002_southwall_ep2": "locations", "LOC_002_south_plain_ep2": "locations", "LOC_002_bastion_se_ep2": "locations",
    "LOC_002_eastgate_chisel_ep2": "locations", "LOC_002_infirmary_ep2": "locations", "LOC_002_tunnel_ep2": "locations",
    "LOC_002_breach_ep2": "locations", "LOC_003_valley_ep2": "locations", "LOC_003_valley_burned_ep2": "locations",
    "LOC_004_platform_ep2": "locations", "VEH_201_mud_ep2": "vehicles", "EXTRA_sui_siege_general_ref": "characters",
}
REF_DIR.update(NEW_REFS)

def ref_path(rid):
    return f"projects/SALSU_612/05_references/{REF_DIR[rid]}/{rid}_1.png"

# ---------------------------------------------------------------- DERIVED STATES (character_bible DERIVED_STATES nguyên văn; ✔ = ref riêng đã có job)
DERIVED = {
    # ---- ✔ ref riêng (character_bible §5 / ref_jobs.json)
    "CHAR_001_dusty_ep2": ("CHAR_001", "CHAR_001_dusty_ep2",
        "Fine yellow-grey stone dust and black soot on helmet, shoulders and cheeks, sweat streaks at the temples, sleeves rolled to the elbow, small field bandage on the back of the left hand, one-day stubble."),
    "CHAR_002_soot_ep2": ("CHAR_002", "CHAR_002_soot_ep2",
        "Black soot and stone dust on face and armor, sweat streaks, right sleeve scorched at the cuff, forearms smudged with gunpowder residue, two-day stubble, goggles still on the helmet."),
    "CHAR_003_soot_ep2": ("CHAR_003", "CHAR_003_soot_ep2",
        "Face and gloves blackened with soot from a vehicle fire, left eyebrow half singed, sweat cutting clean lines through the grime, two-day salt-and-pepper stubble, patrol cap pushed back."),
    "CHAR_004_bloody_sleeves_ep2": ("CHAR_004", "CHAR_004_bloody_sleeves_ep2",
        "Helmet off, hair bun half undone with loose strands, dried blood on both sleeves up to the elbows and on nitrile gloves, pale tired face, headlamp hanging around the neck."),
    "CHAR_006_facepaint_ep1": ("CHAR_006", "CHAR_006_facepaint_ep1",
        "Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim."),
    "CHAR_101_cloak_incognito_ep2": ("CHAR_101", "CHAR_101_cloak_incognito_ep2",
        "A plain black wool cloak with hood drawn over the armor hiding the plume, road dust on the hem and boots, helmet plume removed, face half in shadow of the hood."),
    "CHAR_104_siege_ep2": ("CHAR_104", "CHAR_104_siege_ep2",
        "Helmet worn on the head, a blood-spotted cloth bandage around the forehead under the headband, stone dust in the beard, torch soot on cheeks, cloak scorched with a burnt hole, tired fierce eyes."),
    "CHAR_106_forge_ep2": ("CHAR_106", "CHAR_106_forge_ep2",
        "Leather apron blackened with soot, sweat on the brow, sleeves pushed up showing burn-scarred forearms, hammer in hand."),
    "CHAR_107_scarf_ep2": ("CHAR_107", "CHAR_107_scarf_ep2",
        "A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips."),
    "CHAR_201_robe_only_ep3": ("CHAR_201", "CHAR_201_robe_only_ep3",
        "Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged."),
    # ---- text-only states (bible "–" hoặc "Trạng thái theo tập" 2화) → đính ref gốc / ref biến thể gần nhất
    "CHAR_201_field_dust_ep2": ("CHAR_201", "CHAR_201_ref",
        "Gilded cuirass, fine dust on the yellow hem and red boots, irritated expression, a round silk fan in the left hand."),
    "CHAR_201_robe_fan_ep2": ("CHAR_201", "CHAR_201_robe_only_ep3",
        "Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged, a round silk fan in the left hand."),
    "CHAR_003_helmet_combat": ("CHAR_003", "CHAR_003_ref",
        "Ballistic helmet with camo cover worn instead of the patrol cap, chinstrap fastened."),
    # ---- 2화 in-episode states do veo-prompt-engineer đặt theo bảng "Trạng thái theo tập" 2화 + [ACTION-VI] (đề xuất character-designer nhập bible)
    "CHAR_001_dust_light_ep2": ("CHAR_001", "CHAR_001_ref",
        "Fine grey stone dust on helmet and shoulders after three weeks in the field, sleeves rolled to the elbow, one-day stubble, sweat at the temples."),
    "CHAR_002_dust_ep2": ("CHAR_002", "CHAR_002_ref",
        "Grey stone dust on helmet and shoulders, sleeves rolled, forearms smudged with old gunpowder residue, two-day stubble."),
    "CHAR_003_oil_ep2": ("CHAR_003", "CHAR_003_ref",
        "Mechanic gloves dark with engine oil, grey stone dust on the patrol cap and shoulders, two-day salt-and-pepper stubble, a small green notebook in the chest pocket."),
    "CHAR_003_burned_hands_ep2": ("CHAR_003", "CHAR_003_soot_ep2",
        "Face blackened with soot from a vehicle fire, left eyebrow half singed, both hands red, blistered and shaking, sleeves scorched, patrol cap pushed back."),
    "CHAR_003_bandaged_ep2": ("CHAR_003", "CHAR_003_soot_ep2",
        "Both hands wrapped in clean white bandages to the wrists, left eyebrow half singed, soot smudges still on the face, two-day salt-and-pepper stubble, patrol cap pushed back."),
    "CHAR_003_bandage_thin_ep2": ("CHAR_003", "CHAR_003_ref",
        "Thin white bandages wrapped around both palms, left eyebrow half regrown, grey stone dust on the patrol cap and shoulders, salt-and-pepper stubble."),
    "CHAR_004_headlamp_ep2": ("CHAR_004", "CHAR_004_ref",
        "Headlamp switched on over the helmet, grey stone dust on shoulders, blue nitrile gloves, medic bag on the shoulder."),
    "CHAR_005_ash_ep2": ("CHAR_005", "CHAR_005_ref",
        "Ash and soot on face and uniform, one corner of the hard drone case on his back scorched black, red-rimmed eyes."),
    "CHAR_005_dust_ep2": ("CHAR_005", "CHAR_005_ref",
        "Grey stone dust on helmet and shoulders, sleeves rolled, faint stubble."),
    "CHAR_006_paint_faded_ep2": ("CHAR_006", "CHAR_006_facepaint_ep1",
        "The green and black face paint smeared and fading into grey stone dust, two-day stubble, grass stalks gone from the scrim scarf."),
    "CHAR_101_plain_ep2": ("CHAR_101", "CHAR_101_ref",
        "Helmet plume removed: plain iron lamellar armor without the tall plume or white feathers, a black lacquered bamboo dispatch tube at the belt, road dust on the boots, cloak folded away."),
    "CHAR_101_ash_ep2": ("CHAR_101", "CHAR_101_ref",
        "Full armor with the tall dark plume and two white feathers, a black lacquered bamboo dispatch tube at the belt, light grey ash on the shoulder guards."),
    "CHAR_104_helmet_ep2": ("CHAR_104", "CHAR_104_ref",
        "Iron helmet worn on the head instead of under the arm, grey stone dust in the beard, the heavy gray wool cloak thrown back, iron ring of keys at the belt."),
    "CHAR_104_burnt_cloak_ep2": ("CHAR_104", "CHAR_104_ref",
        "Iron helmet worn on the head, the gray wool cloak scorched with a smoking burnt hole at the hem, stone dust in the beard, sweat, fierce eyes."),
    "CHAR_105_ash_ep2": ("CHAR_105", "CHAR_105_ref",
        "Light grey ash and stone dust on the armor, sweat, the single white feather singed brown at the tip."),
    "CHAR_106_limp_ep2": ("CHAR_106", "CHAR_106_forge_ep2",
        "Leather apron blackened with soot, sleeves pushed up showing burn-scarred forearms, a small hammer at the belt, walking with a slight limp on the right leg."),
    "CHAR_107_hemp_scarf_ep2": ("CHAR_107", "CHAR_107_ref",
        "A coarse hemp scarf over the head and shoulders, small cloth herb pouch at the waist, stone dust on the skirt hem, small smear of blood on the fingertips."),
    "CHAR_205_camp_ep2": ("CHAR_205", "CHAR_205_ref",
        "Fox-fur cap on, a Goguryeo arrowhead on a leather cord at the neck, road dust on the leather armor, calm watchful face."),
    "CHAR_205_fire_ep2": ("CHAR_205", "CHAR_205_ref",
        "Fox-fur cap on, a Goguryeo arrowhead on a leather cord at the neck, soot smudges on the cheek and armor, firelight in the eyes, no torch in hand."),
    "CHAR_205_magazine_ep2": ("CHAR_205", "CHAR_205_ref",
        "Fox-fur cap on, a Goguryeo arrowhead on a leather cord at the neck, an empty black steel rifle magazine hanging from the bronze plaque belt, dust on the leather armor."),
}

# ---------------------------------------------------------------- EXTRAS (không ID trong bible) — lock tạm cố định, dùng NGUYÊN VĂN mọi SC; đề xuất character-designer đưa vào bible
EXTRAS = {
    "BOY_SCOUT": "17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large alert dark eyes, cracked lips, black hair tied under a brown cloth headband beneath a plain leather cap, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow on the back, hip quiver, grey stone dust on face and clothes",
    "BOY_SCOUT_FEVER": "17-year-old Goguryeo boy scout, thin small build, sun-browned round face now flushed and sweating, large glassy dark eyes, cracked dry lips, black hair loose from a brown cloth headband, coarse undyed brown hemp jacket open at the collar, lying under a hemp blanket, the right forearm red, swollen and blistered from a burn, shivering",
    "BOY_SCOUT_THIN": "17-year-old Goguryeo boy scout, thin small build gone thinner, sun-browned round face with hollow cheeks, large alert dark eyes, black hair tied under a brown cloth headband beneath a plain leather cap, coarse undyed brown hemp jacket with crossed collar and white border, a cloth bandage wrapped around the right forearm, wide trousers bound at the ankles, straw sandals, short composite bow on the back, hip quiver",
    "GOG_SENTRY": "Goguryeo wall sentry in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, long spear, face turned away or in shadow",
    "SUI_SIEGE_GENERAL": "Chinese man around 45, lean hard build, long weathered face with high cheekbones, narrow black eyes, short black beard trimmed square, black topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors, dark red silk cloak, iron helmet with a black tassel crest, a riding whip in hand, mounted on a dark bay horse. Clearly younger and leaner than any grey- or white-bearded general",
    "SUI_COURIER": "Sui mounted courier in a grey-blue padded coat under a light iron lamellar vest, black head cloth, a red command flag on a short pole, a black lacquered bamboo dispatch tube on a cord, coated in white road dust, on a lathered horse",
    "SUI_SCRIBE": "Sui army scribe in a dark blue silk robe and black gauze cap kneeling at a low folding table with brush, ink stone, a strip of pale silk and a square bronze seal, face turned down",
    "SUI_INTERPRETER": "thin Sui interpreter in a plain grey hemp robe and black cloth cap, clean-shaven, bowing and repeating words, face turned aside",
    "GOG_FARMER": "Goguryeo farmer around 40, kneeling with wrists bound in front by hemp rope, a bruised swollen cheek, undyed hemp jacket and trousers, cloth headband, bare feet, frightened face",
    "XIANBEI_DEPUTY": "Xianbei deputy commander around 30, stocky, round weathered face, thin moustache, single braid, brown leather lamellar armor over a dark felt coat, fur-trimmed leather cap, composite bow and hip quiver, short curved saber",
    "XIANBEI_FIRE_PARTY": "Xianbei warriors on foot in single file, brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows on their backs, soft boots, every third man hugging a lidded clay pot with a red glow leaking at the rim, no torches",
    "XIANBEI_FIRE_ARCHERS": "ten Xianbei archers on foot in brown leather lamellar armor and fur-trimmed leather caps, kneeling in a line, drawing composite bows with burning oil-soaked cloth bound behind the arrowheads, faces lit orange from below",
    "XIANBEI_THREE": "three Xianbei warriors on foot in brown leather lamellar armor and fur-trimmed leather caps crawling low, one hugging a lidded clay pot with a red glow at the rim, one with a drawn knife, faces turned away",
    "XIANBEI_SCOUTS": "Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs",
    "K2_COMMANDER": "ROK Army tank commander in granite-pattern digital camo uniform and crew helmet with boom microphone and goggles, seen from the chest up in the commander's cupola of a tank, face half shadowed by the helmet",
    "K2_GUNNER": "ROK Army tank gunner in granite-pattern digital camo uniform and crew helmet with boom microphone, seen inside a cramped turret pressed to the gunner's sight, face lit only by a screen glow",
    "K2_CREW": "ROK Army tank crew of three in granite-pattern digital camo uniforms and crew helmets with boom microphones, faces turned away or shadowed",
    "K21_CREW": "ROK Army armored vehicle crew in granite-pattern digital camo uniforms and crew helmets with boom microphones, faces turned away or shadowed",
    "MORTAR_GUNNER": "ROK Army mortar gunner in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, kneeling at the mortar sight, face shadowed by the helmet brim",
    "MORTAR_CREW": "ROK Army mortar crew in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims",
    "K3_GUNNER": "ROK Army machine gunner in granite-pattern digital camo uniform, body armor and covered ballistic helmet, Korean flag patch on right shoulder, prone behind a K3 light machine gun with his face hidden behind the weapon, and an assistant gunner beside him feeding the belt with his face turned away",
    "PZF_GUNNER": "ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, kneeling with a Panzerfaust 3 launcher on the shoulder, face hidden behind the sight unit",
    "PZF_GUNNERS": "ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, kneeling at a stone parapet with Panzerfaust 3 launchers on their shoulders, faces hidden behind the sight units",
    "ROK_SENTRY": "ROK Army sentry in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, rifle held muzzle down, face turned away",
    "ROK_SOLDIER": "ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim",
    "ROK_SOLDIERS": "ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims",
    "ROK_SICK": "ROK Army soldier in granite-pattern digital camo uniform, helmet off, pale sweating face turned down, both arms wrapped around the stomach, sitting on the ground",
    "ROK_BURNED": "ROK Army soldier in granite-pattern digital camo trousers and a cut-open uniform shirt, both arms and the neck wrapped in white bandages to the shoulders, helmet off, face turned away",
    "ROK_BURNED_TWO": "two ROK Army soldiers lying on folding stretchers in granite-pattern digital camo trousers, arms and necks wrapped in white bandages to the shoulders, helmets off, faces turned away",
    "GOG_STONEMASONS": "Goguryeo stonemasons in undyed hemp jackets with sleeves tied back, cloth headbands, straw sandals, stone dust on skin and clothes, iron pry bars, wooden mallets and iron chisels, faces turned to the stone",
    "GOG_CIVILIANS": "Goguryeo townspeople in undyed hemp jackets and trousers or pleated skirts, cloth headbands, straw sandals, carrying stone blocks on wooden carriers and baskets of earth on their heads, faces turned away",
    "GOG_WOUNDED": "wounded Goguryeo soldiers lying on straw bedding in brown jackets with the armor removed, burned shoulders and swollen forearms wrapped in cloth, faces turned away",
    "GOG_INFANTRY": "Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles",
    "GOG_ARCHERS": "Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows",
    "GOG_SPEARMEN": "Goguryeo spearmen in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long four-meter spears levelled together in a wall, round wooden shields with iron bosses, faces shadowed under helmets",
    "GOG_CAVALRYMEN": "Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants",
    "GOG_SOLDIER_RUNNER": "young Goguryeo soldier in iron lamellar armor over a brown jacket and an iron plate helmet, face turned up and away",
    "SUI_DIGGERS": "Sui conscript soldiers stripped to the waist with hemp head cloths, mud on skin, swinging mattocks and passing woven baskets of earth hand to hand, faces turned down",
    "SUI_PUSHERS": "hundreds of Sui soldiers in grey-blue padded coats and hemp head cloths straining at pushing beams and tow ropes with backs bent and faces down, oxen under wooden yokes beside them",
    "SUI_CRAFTSMEN": "Sui carpenters and laborers in undyed hemp jackets and head cloths with mallets, adzes, shovels and baskets of wet mud, faces turned to the work",
    "SUI_CROSSBOWMEN": "Sui crossbowmen in grey-blue padded coats and pointed iron helmets crouched behind tall red rectangular shields, spanning heavy wooden crossbows with bronze triggers, faces hidden",
    "SUI_GENERALS": "a row of Sui generals in mingguang lamellar armor with polished round breast mirrors and red cloaks, iron helmets with red tassels, kneeling with heads bowed, faces hidden",
    "SUI_EUNUCH": "Sui court eunuch in a plain grey-blue silk robe and black gauze cap, clean-shaven, head bowed",
    "SUI_OFFICIAL": "Sui court official in a dark blue silk robe and black gauze cap kneeling and holding up a wooden tally with both hands, face turned down",
    "SUI_MARCHERS": "Sui soldiers in grey-blue padded coats under iron lamellar vests marching in a long column under heavy packs of grey grain sacks, rolled tents and spears, backs bent, faces down",
    "SUI_OFFICER_HORSE": "a mounted Sui officer in iron lamellar armor with a red cloak and a leather whip, face shadowed by an iron helmet",
    "SUI_SURVIVORS": "Sui soldiers in grey-blue padded coats and dented iron helmets crawling and staggering out of wreckage, faces turned away",
    "SUI_TOWER_MEN": "Sui soldiers in grey-blue padded coats and pointed iron helmets crowded on the wooden floors of a siege tower, round shields, faces turned away",
    "GOG_TORCH_SQUAD": "four Goguryeo soldiers in iron lamellar armor over brown jackets carrying whitewashed boulders and shielded torches, faces turned away",
}
EXTRA_REF = {  # extra → ref đính (nếu có)
    "BOY_SCOUT": "EXTRA_boy_scout_ref", "BOY_SCOUT_FEVER": "EXTRA_boy_scout_ref", "BOY_SCOUT_THIN": "EXTRA_boy_scout_ref",
    "SUI_SIEGE_GENERAL": "EXTRA_sui_siege_general_ref",
    "GOG_INFANTRY": "WPN_102_ref", "GOG_ARCHERS": "WPN_102_ref", "GOG_SPEARMEN": "WPN_102_ref", "GOG_SENTRY": "WPN_102_ref",
    "GOG_CAVALRYMEN": "VEH_101_ref",
    "XIANBEI_FIRE_PARTY": "VEH_206_ref", "XIANBEI_FIRE_ARCHERS": "VEH_206_ref", "XIANBEI_THREE": "VEH_206_ref", "XIANBEI_SCOUTS": "VEH_206_ref", "XIANBEI_DEPUTY": "VEH_206_ref",
    "SUI_CROSSBOWMEN": "WPN_201_ref", "SUI_TOWER_MEN": "WPN_201_ref", "SUI_MARCHERS": "WPN_201_ref", "SUI_GENERALS": "WPN_201_ref", "SUI_SURVIVORS": "WPN_201_ref",
}

# ---------------------------------------------------------------- VEHICLE STATES 2화 (vehicle_bible damage state; veh_ref = ref biến thể nếu có)
VEH_STATE = {
    "K21_2": "White numeral 2 on the turret, black soot around the short muzzle, a few arrow shafts stuck in the stowage.",
    "K21_3": "White numeral 3 on the turret, a crude hand-forged iron pin with hammer marks fitted through the third road wheel on the right side with an oil streak below it.",
    "K21_4": "White numeral 4 on the turret, clean apart from grey dust.",
    "K21_4_BURNED": "The burned-out wreck of the fourth vehicle: hull scorched black and rust-brown, paint blistered, flotation panels burned away, turret dislodged, hatches open, charred camouflage net hanging from the side.",
    "K2_CLEAN": "Muzzle clean and unfired, fine grey dust on the hull, camouflage netting pulled back.",
    "K2_WET_NET": "Camouflage netting over the hull soaked dark with water.",
    "K2_SOOT": "Black soot around the muzzle after firing, several broken crossbow bolts stuck in the stowage rack, net fibers scorched on the left skirt.",
    "TOWER_HIDE": "Fresh raw timber, wet dark ox hide glistening, a red banner on top.",
    "TOWER_MUD": "Front, sides and top covered in mud-soaked straw mats under a thick layer of wet earth, earth-brown instead of black hide, red banner on top.",
    "RAM_MUD": "The turtle-shell roof covered in two thick layers of wet earth over straw mats.",
}

# ---------------------------------------------------------------- SUB-LOCATION LOCKS 2화 (cố định, dùng nguyên văn mọi SC) → sublocks_ep2.md
SUBLOC = {
    # key: (loc_id, ref_id or None, text)
    "LOC_002": ("LOC_002", "LOC_002_wide", LOC_LOCK["LOC_002"]),
    "LOC_002_southwall_fog": ("LOC_002", "LOC_002_detail",
        "On top of the south wall of the Goguryeo fortress at dawn in thick white fog: dry-stacked grey granite blocks without mortar, a low stone parapet with narrow arrow slits, a rectangular protruding bastion, a wooden rack of arrows, clay water jars, a large hide war drum on a wooden stand, a black three-legged crow banner hanging limp, fog hiding everything beyond the parapet"),
    "LOC_002_southwall": ("LOC_002", "LOC_002_southwall_ep2",
        "On top of the south wall of the Goguryeo fortress under siege: dry-stacked grey granite blocks without mortar, a low stone parapet with narrow arrow slits, rectangular protruding bastions, racks of arrows, clay water jars, iron cauldrons, a hide war drum on a wooden stand, black three-legged crow banners, and beyond the parapet a trampled plain with a filled moat, a line of Sui siege towers and an ocean of grey felt tents"),
    "LOC_002_south_plain": ("LOC_002", "LOC_002_south_plain_ep2",
        "The trampled plain south of the Goguryeo fortress under siege: a moat filled with earth sacks and brushwood into a wide causeway, churned bare earth and yellow dust, lines of Sui eight-wheeled siege towers and ladder carts, red and yellow banners, grey felt tents behind them to the horizon, and the dry-stacked grey granite wall with rectangular bastions and a timber gate tower rising above"),
    "LOC_002_tunnel": ("LOC_002", "LOC_002_tunnel_ep2",
        "Inside a Sui mine tunnel dug under the plain toward the fortress wall: a low earthen passage shored with raw timber posts and beams, clay oil lamps hanging from the posts, damp walls seeping water, woven baskets of loose earth, a cramped ceiling of packed soil"),
    "LOC_002_drawing": ("LOC_002", None,
        "A military treatise drawing in brown ink on aged ivory silk, faint grid lines, brush-drawn side views and cross-sections, no readable characters anywhere"),
    "LOC_002_sui_lines": ("LOC_002", "LOC_002_south_plain_ep2",
        "The Sui siege lines behind the filled moat south of the Goguryeo fortress: a general's position under red and yellow banners on black lacquered poles, grey felt tents, huge red war drums in red lacquered frames, horse lines, siege towers waiting in a line, trampled yellow ground, and the dry-stacked grey granite fortress wall with rectangular bastions in the distance"),
    "LOC_002_sui_yard": ("LOC_002", "LOC_002_south_plain_ep2",
        "The Sui siege-engine yard on the plain south-west of the fortress: raw timber frames of half-built towers and ram carts, stacks of fresh-cut logs from a felled forest, piles of wet ox hides, hemp rope, oxen, straw mats, mud pits, torches on poles, grey felt tents behind"),
    "LOC_002_wall_base_in": ("LOC_002", "LOC_002_detail",
        "Inside the Goguryeo fortress at the foot of the south wall: the inner face of dry-stacked grey granite blocks rising high, a low timber scaffold against a cracked section where fresh pale stones are being fitted between old dark moss-stained ones, stone blocks on wooden carriers, baskets of earth, torches in iron brackets, a packed-earth lane, timber halls with dark tiled roofs behind"),
    "LOC_002_wall_face_out": ("LOC_002", "LOC_002_detail",
        "The outer face of the south wall of the Goguryeo fortress at night: dry-stacked grey granite blocks battered slightly inward, a vertical strip of fresh pale newly-laid stone between old dark moss-stained blocks, the parapet above lit by torches, a white cloth on a spear above a rectangular bastion, the filled moat below"),
    "LOC_002_infirmary": ("LOC_002", "LOC_002_infirmary_ep2",
        "Interior of a dark timber infirmary house against the inner wall of the Goguryeo fortress: plank floor spread with woven reed mats, rows of straw bedding, clay bowls and water basins, bundles of herbs hanging from the rafters, a shuttered wooden lattice window with narrow gaps, thick wooden posts, thin lines of daylight through the shutters, smoke haze"),
    "LOC_002_courtyard": ("LOC_002", "LOC_002_detail",
        "A packed-earth courtyard inside the Goguryeo fortress at the foot of the inner wall: the dry-stacked grey granite wall towering above with a stone stair climbing it and a rectangular bastion at the top, timber halls with dark grey tiled roofs, a black three-legged crow banner, the three-story wooden pagoda beyond the roofs"),
    "LOC_002_hall": ("LOC_002", "LOC_002_interior",
        "Interior of a Goguryeo commander's timber hall at night, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, bronze incense burner, clay oil lamps giving warm yellow light, latticed wooden windows shuttered, a black three-legged crow banner on the wall, smoke haze"),
    "LOC_002_hall_day": ("LOC_002", "LOC_002_interior",
        "Interior of a Goguryeo commander's timber hall by day, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, a low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, a bronze incense burner, a black three-legged crow banner on the wall, morning sun slanting through open latticed wooden doors in bars of light and drifting dust"),
    "LOC_002_veranda": ("LOC_002", "LOC_002_interior",
        "The wooden veranda of the Goguryeo commander's hall: worn dark plank floor, round pillars with faded red lacquer, a low railing, a black three-legged crow banner on a bamboo pole, looking across a packed-earth courtyard and dark tiled roofs toward the distant south wall of dry-stacked grey granite with rectangular bastions, pale daylight and drifting dust"),
    "LOC_002_bastion_se": ("LOC_002", "LOC_002_detail",
        "On the south-east rectangular bastion of the Goguryeo fortress: dry-stacked grey granite blocks without mortar, a low parapet with narrow arrow slits, a black three-legged crow banner on a bamboo pole at the corner, a stone stair down into the fortress, and beyond the parapet the trampled plain to the south with a distant line of Sui siege towers and grey felt tents to the horizon"),
    "LOC_002_bastion_se_k2": ("LOC_002", "LOC_002_bastion_se_ep2",
        "On the south-east rectangular bastion of the Goguryeo fortress with a modern K2 tank parked on top: dry-stacked grey granite parapet with one arrow slit chiselled into a square embrasure the size of a tank gun, a black three-legged crow banner on a bamboo pole beside the tank, a fresh earth ramp descending behind into the fortress, the trampled plain and Sui siege towers beyond the parapet"),
    "LOC_002_ramp": ("LOC_002", "LOC_002_bastion_se_ep2",
        "Inside the Goguryeo fortress behind the south-east bastion: the inner wall dismantled ten courses down, a wide ramp of fresh packed earth rising at twenty degrees from the packed-earth yard to the top of the bastion, stone blocks stacked beside it, baskets, a low timber scaffold, torches in iron brackets, timber halls with dark tiled roofs behind"),
    "LOC_002_ramp_work": ("LOC_002", "LOC_002_bastion_se_ep2",
        "Inside the Goguryeo fortress behind the south-east bastion by day: the inner wall being taken down course by course with iron pry bars, stone blocks stacked on the ground, baskets of earth tipped into a rising ramp, a taut measuring cord on the wall, stone dust, timber halls with dark tiled roofs behind, the dry-stacked grey granite outer wall and bastion above"),
    "LOC_002_eastgate_chisel": ("LOC_002", "LOC_002_eastgate_chisel_ep2",
        "The small east gate of the Goguryeo fortress being widened: a narrow arched passage of dry-stacked grey granite with a low wooden scaffold inside the arch, both walls of the passage freshly chiselled back showing bright pale stone against dark old blocks, stone chips and dust on the ground, two-leaf iron-sheathed wooden doors folded open, a black three-legged crow banner"),
    "LOC_002_eastgate_night_k2": ("LOC_002", "LOC_002_eastgate_chisel_ep2",
        "The widened east gate arch of the Goguryeo fortress at night seen from inside: a narrow stone passage of dry-stacked grey granite with freshly chiselled pale walls, torches in iron brackets, stone dust hanging in the air, the dark hills outside the arch, a packed-earth yard inside"),
    "LOC_002_well_yard": ("LOC_002", "LOC_002_detail",
        "A small well yard inside the Goguryeo fortress: a low round well of grey stone with a wooden bucket and rope, packed-earth ground, a wooden post, timber houses with dark tiled roofs and latticed windows, the dry-stacked grey granite wall in the distance"),
    "LOC_002_granary_fire": ("LOC_002", "LOC_002_detail",
        "Inside the Goguryeo fortress at night: a raised-floor timber granary on thick wooden posts with a dark grey tiled roof, and beside it a small storehouse whose thatched roof is burning, sparks and smoke, clay water jars, a packed-earth yard, a stone well, the dry-stacked grey granite wall with torches behind"),
    "LOC_002_barbican_in": ("LOC_002", "LOC_002_detail",
        "Inside the semicircular stone barbican of the south gate of the Goguryeo fortress: a narrow arched stone passage of dry-stacked grey granite, two-leaf wooden gate doors sheathed with iron plates and studded with large iron nails, a massive oak crossbar in iron brackets, timber props wedged against the doors, stone blocks piled at their feet, dust falling from the vault, torches"),
    "LOC_002_gate_tower": ("LOC_002", "LOC_002_detail",
        "On top of the two-story timber gate tower over the south gate of the Goguryeo fortress: dark grey tiled roof, wooden railing and posts with faded red lacquer, a hide war drum, black three-legged crow banners, the stone barbican below and the causeway across the filled moat, the trampled plain and Sui lines beyond"),
    "LOC_002_causeway": ("LOC_002", "LOC_002_south_plain_ep2",
        "The earth causeway across the filled moat to the south gate of the Goguryeo fortress: packed earth sacks and brushwood, churned mud, the semicircular stone barbican of dry-stacked grey granite ahead with its iron-sheathed gate doors, the timber gate tower above, rectangular bastions either side, arrows stuck in the ground"),
    "LOC_002_breach": ("LOC_002", "LOC_002_breach_ep2",
        "An eighty-meter breach in the south wall of the Goguryeo fortress: the outer face collapsed into a steep slope of tumbled grey granite blocks and earth spilling toward the filled moat, the inner wall still standing behind, dust, intact wall with parapet either side, the fortress yard and timber roofs visible through the gap"),
    "LOC_002_breach_in": ("LOC_002", "LOC_002_breach_ep2",
        "Inside the Goguryeo fortress at the breach in the south wall: a slope of tumbled grey granite blocks rising to the gap in the wall, the inner side of the intact wall either side with its stone stair, a packed-earth yard, stone blocks and baskets, torches, timber halls with dark tiled roofs"),
    "LOC_002_breach_repaired": ("LOC_002", "LOC_002_breach_ep2",
        "The south wall of the Goguryeo fortress near its south-east corner at night: an eighty-meter section rebuilt in fresh pale stone between old dark blocks, a black three-legged crow banner on the new stone, the empty south-east bastion with a soot-blackened square embrasure, moonlight"),
    "LOC_002_northgate": ("LOC_002", "LOC_002_detail",
        "The north gate of the Goguryeo fortress: two-leaf iron-sheathed wooden doors swinging open in a dry-stacked grey granite wall between rectangular bastions, a timber gate tower with dark tiled roof, a beaten track leading out into pale green grass, low oak-scrub hills to the east"),
    "LOC_002_se_corner_out": ("LOC_002", "LOC_002_south_plain_ep2",
        "Outside the south-east corner of the Goguryeo fortress: the dry-stacked grey granite wall with its corner watchtower and a rectangular bastion, a field of trampled grass and bare dust, a line of Sui siege towers, a collapsed tower leaning against the wall, the east hills empty of enemy, the filled moat to the south"),
    "LOC_002_marker_field": ("LOC_002", "LOC_002_south_plain_ep2",
        "The trampled grass field south of the south-east bastion of the Goguryeo fortress at night: bare dust and flattened grass, three whitewashed boulders set in a line at increasing distances from the wall, the dark mass of the dry-stacked granite wall with torches behind, Sui campfires far to the south"),
    "LOC_002_stair": ("LOC_002", "LOC_002_detail",
        "A stone stair climbing the inside of the south wall of the Goguryeo fortress: steep uneven steps of dry-stacked grey granite along the inner face, the parapet and a rectangular bastion above, a packed-earth yard below, a black three-legged crow banner"),
    "LOC_002_eastwall_night": ("LOC_002", "LOC_002_detail",
        "On top of the east wall of the Goguryeo fortress at night: dry-stacked grey granite parapet with arrow slits, a rectangular bastion, a black three-legged crow banner, and beyond the wall the low oak-scrub hills to the east, and far to the south the pale plain under moonlight"),
    "LOC_002_k2_interior": ("LOC_002", None,
        "Inside the cramped turret of a modern K2 tank on the fortress bastion: the gunner's sight with a thermal screen, the commander's station with small glowing instrument panels, an ammunition ready rack, handles, cables and padded steel, dim interior lighting"),
    "LOC_002_pagoda_view": ("LOC_002", "LOC_002_wide",
        "The Goguryeo fortress at night seen from the top floor of its three-story wooden pagoda: dark tiled roofs of timber halls below, torches along the dry-stacked grey granite walls with rectangular bastions, a small thatched roof smouldering beside a raised granary, and outside the walls an ocean of Sui campfires ringing the fortress to the horizon"),
    # ---- LOC_003 (thung lũng, Dạng A — 2화)
    "LOC_003": ("LOC_003", "LOC_003_wide", LOC_LOCK["LOC_003"]),
    "LOC_003_valley_apr": ("LOC_003", "LOC_003_valley_ep2",
        "The hidden company base in a shallow oak-scrub valley three weeks into the siege: a K2 tank under sun-faded green-brown camouflage netting, three K21 infantry fighting vehicles in a row under netting, two 6x6 cargo trucks and a boxy 4x4 command vehicle along the west slope, two olive fuel drums behind a sandbag wall thirty paces from the vehicles, olive-green army tents beside brown hemp Goguryeo tents, ground churned to bare earth, oak scrub in first leaf"),
    "LOC_003_line": ("LOC_003", "LOC_003_valley_ep2",
        "The vehicle line of the hidden company base by day: a K2 tank and three K21 infantry fighting vehicles side by side under sun-faded camouflage netting on bare churned earth, olive ammunition cans, a wooden tally board hung on the command tent, oak-scrub slopes in first leaf either side"),
    "LOC_003_line_night": ("LOC_003", "LOC_003_valley_ep2",
        "The vehicle line of the hidden company base at night: a K2 tank and K21 infantry fighting vehicles under camouflage netting on bare earth, a faint red glow from the command tent, olive ammunition cans, dark oak-scrub slopes, thin moonlight"),
    "LOC_003_drums": ("LOC_003", "LOC_003_valley_ep2",
        "A sandbag wall at the hidden company base thirty paces from the vehicle line: two dark olive 200-liter steel fuel drums standing behind the sandbags under a scrap of camouflage netting, a hand pump and a green jerrycan, bare churned earth, oak scrub on the slope behind"),
    "LOC_003_drums_fire": ("LOC_003", "LOC_003_valley_ep2",
        "The sandbag fuel position of the hidden company base at night on fire: a burning camouflage net over sandbags, a fuel drum engulfed in orange flame, a second drum beside it, burning arrows in the ground, the vehicle line and trucks lit orange thirty paces away, oak scrub"),
    "LOC_003_mortar_day": ("LOC_003", "LOC_003_wide",
        "A sandbagged mortar pit on a small grassy knoll at the south end of the hidden valley base by day: two 81mm mortars on bipods, round baseplates, olive ammunition cans, a range card on a stake, bare earth, oak scrub in leaf, the valley below"),
    "LOC_003_k2": ("LOC_003", "LOC_003_wide",
        "The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond"),
    "LOC_003_k2_day": ("LOC_003", "LOC_003_valley_ep2",
        "The K2 tank of the hidden company base by day with its camouflage netting pulled back: three-tone camouflage hull on bare churned earth, olive ammunition cans, a folding table, oak-scrub slopes in leaf, olive army tents and brown hemp Goguryeo tents beyond"),
    "LOC_003_tent": ("LOC_003", "LOC_003_detail",
        "Inside a modern South Korean army command tent at night, dim red tactical lamplight: a steel folding table with a paper topographic map weighted by a cracked military tablet and a PRC-999K backpack radio with handset, a hand-written tally board of ammunition and fuel numbers on a plank, stacked olive-green ammunition cans, a quadcopter drone battery charging from a cable that runs out under the tent flap, a Goguryeo clay water jar and a bronze oil lamp on the earth floor, faint yellow dust in the air"),
    "LOC_003_tent_ext": ("LOC_003", "LOC_003_wide",
        "Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes"),
    "LOC_003_tent_ext_day": ("LOC_003", "LOC_003_valley_ep2",
        "Outside the olive-green command tent of the hidden company base by day: a wooden tally board with chalk marks hung beside the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents beside the olive army tents, bare churned earth, oak scrub in leaf"),
    "LOC_003_medic": ("LOC_003", "LOC_003_wide",
        "The aid station of the hidden company base at night: a canvas awning off an olive-green army tent, a folding stretcher on olive ammunition cans, a headlamp and a shaded red lamp, camouflage netting, brown hemp Goguryeo tents beside, dry yellow grass, dark oak scrub slopes"),
    "LOC_003_medic_day": ("LOC_003", "LOC_003_wide",
        "The aid station of the hidden company base by day: a canvas awning off an olive-green army tent, folding stretchers on olive ammunition cans, a medic bag, clay pots, brown hemp Goguryeo tents beside, bare earth, oak scrub in leaf"),
    "LOC_003_hearth": ("LOC_003", "LOC_003_wide",
        "A Goguryeo stone hearth fire at the hidden company base: a ring of grey stones, a clay pot over orange flames, brown hemp Goguryeo tents with wooden poles beside olive-green army tents, camouflage netting over dark vehicle shapes behind, bare earth, oak scrub in leaf"),
    "LOC_003_op_west": ("LOC_003", "LOC_003_wide",
        "An observation post on the crest of the west hill above the hidden valley: oak scrub in first leaf, dry grass, a shallow scrape under a poncho, and beyond the crest, across two kilometers of trampled plain, the south wall of the Goguryeo fortress in dry-stacked grey granite with rectangular bastions, Sui siege lines and tents beyond"),
    "LOC_003_trail_night": ("LOC_003", "LOC_003_wide",
        "A narrow dirt trail at night climbing the hillside above the hidden valley through oak scrub in leaf, loose stones, no moon, dark thickets either side, the faint red glow of the valley below"),
    "LOC_003_trail_day": ("LOC_003", "LOC_003_wide",
        "The dirt trail at the mouth of the hidden valley by day: a narrow path climbing through oak scrub in leaf toward the hill crest, a stony stream bed below, bare churned earth on the valley floor, camouflage netting over dark vehicle shapes"),
    "LOC_003_hillside_pov": ("LOC_003", "LOC_003_valley_ep2",
        "The hillside above the hidden valley at night seen through a screen of oak leaves: below in the dark, camouflage netting over vehicle shapes, a single red glow from a tent, and two round drum shapes behind a low sandbag wall thirty paces from the vehicles"),
    "LOC_003_ford_northbank": ("LOC_003", "LOC_003_ford_night",
        "The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north, thin moonlight"),
    "LOC_003_mouth": ("LOC_003", "LOC_003_wide",
        "The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond"),
    "LOC_003_hilltop_enemy": ("LOC_003", "LOC_003_wide",
        "The crest of a hill overlooking the mouth of the hidden valley at dusk: grey boulders, oak scrub in leaf, pale green grass, the dirt trail visible below winding into the dark valley, hills rolling away to the south"),
    "LOC_003_fire_wide": ("LOC_003", "LOC_003_valley_burned_ep2",
        "The hidden valley base at night lit by fire: a K21 infantry fighting vehicle burning beside a cargo truck, a column of fuel fire, burning camouflage netting, sandbags scattered, tents and oak-scrub slopes lit orange, a K2 tank under wet netting at the dark edge"),
    "LOC_003_wreck_dawn": ("LOC_003", "LOC_003_valley_burned_ep2",
        "The hidden valley base at grey dawn after a fire: the burned-out black hull of a K21 infantry fighting vehicle with its turret dislodged and hatches open, thin smoke, a scorched cargo truck beside it, a crater with scattered sandbags where a fuel drum exploded, ash over the ground, tents and netting grey with ash, oak scrub in leaf"),
    "LOC_003_wreck_day": ("LOC_003", "LOC_003_valley_burned_ep2",
        "The hidden valley base by day after the fire: the burned-out black hull of a K21 infantry fighting vehicle with its turret dislodged, a scorched cargo truck, a crater with scattered sandbags, ash over bare earth, a K2 tank with its netting pulled back, two intact K21 vehicles, olive tents and brown hemp Goguryeo tents, oak scrub in leaf"),
    "LOC_003_line_jun": ("LOC_003", "LOC_003_valley_burned_ep2",
        "The vehicle line of the hidden company base in early summer: a K2 tank with a soot-blackened muzzle under half-drawn netting, two K21 infantry fighting vehicles, two cargo trucks and a 4x4 command vehicle, the burned black wreck of a third K21 at the edge, a single fuel drum behind a new sandbag wall, bare earth, oak scrub in full leaf"),
    "LOC_003_hill_south_night": ("LOC_003", "LOC_003_wide",
        "The dark southern hillside beyond the hidden valley at night: oak scrub in full leaf, pale grass under moonlight, a narrow track along the slope, and far below in the valley a single red pinpoint of lamplight"),
    "LOC_003_fork_night": ("LOC_003", "LOC_003_wide",
        "A fork in the track at the foot of the hills at night: one path climbing toward the mouth of the hidden valley through oak scrub, the other running south along the base of the hills, pale green grass under moonlight"),
    # ---- LOC_004 (육합성 / hành doanh / đài quan sát)
    "LOC_004": ("LOC_004", "LOC_004_wide", LOC_LOCK["LOC_004"]),
    "LOC_004_pavilion_day": ("LOC_004", "LOC_004_wide",
        "The Sui emperor's traveling court on the west bank of the Liao River by day: a huge pavilion tent with a golden silk roof and red pillars raised on a wooden dais, yellow and red silk drapes tied back, rows of eunuchs in grey-blue silk robes on the approach, red and yellow banners on black lacquered poles, the wide brown river and an ocean of grey felt tents behind"),
    "LOC_004_pavilion_int": ("LOC_004", "LOC_004_detail",
        "Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack"),
    "LOC_004_hall_day": ("LOC_004", "LOC_004_detail",
        "Interior of the Sui emperor's pavilion inside the mobile fortress by day: a carved wooden throne lacquered red and gilded on a three-step dais, red lacquered pillars, yellow silk drapes with hard sunlight cutting through them in bright stripes across a red carpet, a large bronze incense burner with rising smoke, a silk folding screen, a large silk map, a sword rack"),
    "LOC_004_platform": ("LOC_004", "LOC_004_platform_ep2",
        "A tall timber observation platform newly raised on the plain south of the Goguryeo fortress: raw log posts and a plank deck with a wooden railing, a golden silk canopy on red poles over the deck, yellow imperial banners with red tassels, torches on poles around the base, ranks kneeling below, and across the plain the dry-stacked grey granite fortress wall with rectangular bastions"),
    "LOC_004_gate_night": ("LOC_004", "LOC_004_wide",
        "The red wooden gate of the Sui mobile fortress at night: two-leaf doors with bronze studs in a wall of timber panels faced with grey-painted hemp cloth imitating brick, a red-lacquered watchtower with railings above, lanterns, torches, grey felt tents and campfires beyond"),
    # ---- LOC_001 (요하 — ken-burns sử / trại Tiên Ti)
    "LOC_001_supply_road": ("LOC_001", "LOC_001_wide",
        "A supply road on the flat plain between Zhuojun and the Liao River in spring: deep mud ruts, a two-wheeled ox cart with a broken axle lying on its side, a dead ox bloated in the ditch, torn grain sacks spilling into the mud, a line of stalled carts stretching to the horizon, dry yellow grass, pale grey sky, dust"),
    "LOC_001_xianbei_camp": ("LOC_001", "LOC_001_wide",
        "A Xianbei cavalry camp at the edge of the great Sui camp on the plain: round felt tents, black horse-tail standards on poles, hobbled stocky steppe horses grazing, leather saddles on racks, a smouldering fire, trampled yellow grass and dust, grey felt Sui tents in grid rows behind to the horizon, the low oak hills east of the fortress hazy in the distance"),
    "LOC_001_muster_night": ("LOC_001", "LOC_001_wide",
        "A night muster ground beside the Liao River: nine tall red silk banners with yellow borders in a row on black lacquered poles, torches on poles for miles, long lines of soldiers, stacks of grey hemp grain sacks, officers with bamboo tallies, trampled ground, the black river behind"),
    "LOC_001_march_night": ("LOC_001", "LOC_001_wide",
        "A beaten dirt road across the plain at night under thin moonlight: a long column of soldiers marching east under heavy packs, sparse torches, grass and a shallow ditch beside the road, dust"),
    "NONE": (None, None, ""),
}

# ---------------------------------------------------------------- LIGHTING theo bảng ngày/đêm 2화 (header script v2) + mùa
LIGHT = {
    "fog_dawn": "Dawn in thick white fog, cold grey-white diffused light, visibility a few meters, breath fogging",
    "fog_lifting": "Dawn fog thinning in gusts of wind, a low red sun behind it, grey-white light with amber breaking through",
    "apr_morning": "Mid-spring morning, pale silver sun through thin yellow dust haze, cool dry wind, soft shadows",
    "apr_day": "Mid-spring daylight, pale silver sun through drifting yellow dust, soft shadows, dry wind",
    "apr_afternoon": "Late afternoon, low amber sun slanting through thick yellow dust, warm-grey haze, long shadows",
    "apr_dusk": "Dusk, a last band of amber on the western horizon, deep blue shadows, yellow dust settling, first torches lit",
    "night_torch": "Night, warm orange torchlight against deep blue-black darkness, thin moon",
    "night_lamp": "Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows",
    "night_lantern_gold": "Night interior, rich golden silk-lantern light, deep shadows",
    "night_red": "Night, dim red tactical lamplight on faces and hands, deep black shadows beyond",
    "night_moon_dry": "Dry windy night, thin cold moonlight, deep blue-black shadows, dust in the gusts",
    "night_nomoon": "Moonless night, faint starlight only, deep black shadows, shapes barely readable",
    "night_nvg": "Night, monochrome green night-vision view with grain and faint scan noise, black sky, bright green highlights on warm bodies",
    "night_thermal": "Night, a small vehicle screen showing a white-hot thermal view, cold blue-white glow on the operator's face",
    "night_fire": "Night lit by a large fuel fire, hard orange light and hard black shadows, sparks and embers in the wind, smoke",
    "night_fire_far": "Night, orange firelight from a burning vehicle far below, faint on faces, deep black shadows",
    "night_moon_jun": "Warm dry early-summer night, bright moonlight, deep blue shadows, faint dust",
    "dawn_grey": "Cold grey dawn, flat blue-grey light, thin mist, dew on stone and metal",
    "dawn_smoke": "Grey dawn through thin smoke, flat cold light, ash drifting, no wind",
    "dawn_gold_jun": "Early summer dawn, pale gold light low across the plain, dust already rising, cool air",
    "may_day": "Late spring daylight, hard bright sun, yellow dust from trampled ground, dry air",
    "may_afternoon": "Late spring late afternoon, low amber sun through dust, long shadows, dry air",
    "jun_day": "Early summer daylight, hard bright sun, yellow dust from trampled ground, pale green grass on the untrodden slopes, dry hot air",
    "jun_afternoon": "Early summer late afternoon, low amber sun through smoke and dust, long shadows",
    "jun_sunset": "Sunset, low amber sun on the horizon through smoke and dust, long shadows, fires glowing",
    "jun_dusk": "Early summer dusk, a last band of amber in the west, deep blue shadows, warm dry air",
    "sun_stripes": "Hard daylight cutting through yellow silk drapes in bright stripes, dust in the beams, deep shadow between",
    "aerial_dawn": "Aerial at dawn, a low red sun, long shadows, fog and dust haze over the plain",
    "aerial_day": "Aerial in daylight, pale silver sun through dust haze, soft shadows",
    "aerial_night": "Night from high above, thousands of orange campfires and lanterns on a black plain, thin moonlight",
    "aerial_moon_jun": "Night from high above under a bright early-summer moon, pale plain, sparse torches",
}
SEASON = {  # theo bảng ngày/đêm: D25–D33 = 4월 (xuân giữa) · D45–D46 = 5월 đầu · D47–D75 = 5월 giữa–6월 (đầu hè, chưa mưa)
    "APR": "Season: mid-spring, dry yellow grass with the first pale green shoots, drifting yellow dust, no rain.",
    "MAY": "Season: late spring, grass turning pale green on the slopes, trampled ground raising yellow dust, dry air, no rain.",
    "JUN": "Season: early summer before the rains, pale green grass on untrodden ground, the trampled plain bare and dusty, hot dry air, no rain.",
}
WEAR = {  # tình trạng chung lính hiện đại (character_bible §0.3, 2화)
    "A": "Modern soldiers' uniforms worn and faded after three weeks in the field, grey stone dust and torch soot on helmets and shoulders, sleeves rolled, one or two days' stubble, sweat streaks at the temples.",
    "B": "Modern soldiers carry black soot and ash over the grey stone dust, singed net fibers on shoulders, two days' stubble, red tired eyes.",
    "C": "Modern soldiers' uniforms faded and patched, grey dust and old soot, stubble, sunburnt necks, wind-chapped lips.",
}
def day_num(day):
    return int(re.match(r"D(\d+)", day).group(1))
def season_of(day):
    n = day_num(day)
    return "APR" if n <= 33 else ("MAY" if n <= 46 else "JUN")
def wear_of(day):
    n = day_num(day)
    if day.endswith("f"): return "B"      # D45f = sau khi lửa bùng (SC_142+)
    return "A" if n <= 45 else ("B" if n == 46 else "C")
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
        nar, dlg, sound, action_vi, combat = [], [], "", "", False
        for ln in body.split("\n"):
            ln = ln.strip()
            if ln == "[COMBAT]":
                combat = True; continue
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
                        veh_hdr=veh_hdr, nar=" ".join(nar), dlg=dlg, sound=sound, action_vi=action_vi, combat=combat)
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
    day = s.get("day", "D25")
    chars = s.get("chars", [])
    states = s.get("states", {})
    vehs = s.get("veh", [])
    vstate = s.get("veh_state", {})
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
        add_ref(EXTRA_REF.get(e))
    for v in vehs:
        vref = s.get("veh_ref", {}).get(v, f"{v}_ref")
        vlock = LOCKS[v] if LOCKS[v].rstrip().endswith((".", "!", "?")) else LOCKS[v] + "."
        seg.append(f"{tag_of(vref)}: {vlock}" + (f" {VEH_STATE[vstate[v]]}" if v in vstate else ""))
        add_ref(vref)
    for p in props:
        pref = f"{p}_ref" if f"{p}_ref" in REF_DIR else None
        seg.append((f"{tag_of(pref)}: " if pref else "") + LOCKS[p])
        add_ref(pref)
    if loc_text:
        seg.append((f"Setting {tag_of(loc_ref)}: " if loc_ref else "Setting: ") + loc_text)
        add_ref(loc_ref)
    seg.append("Action: " + s["action"].rstrip(".") + ".")
    light = LIGHT[s["light"]] if s["light"] in LIGHT else s["light"]
    seg.append("Light: " + light.rstrip(".") + ".")
    if not s.get("interior") and loc_text:
        seg.append(SEASON[s.get("season", season_of(day))])
    if any(c in ROK for c in chars) or any(e.startswith(("ROK", "K2_", "K21_", "MORTAR", "K3_", "PZF")) for e in extras):
        seg.append(WEAR[s.get("wear", wear_of(day))])
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
        "type": sc["type"], "loc": loc_id, "subloc": subloc, "day": day.rstrip("f"), "season": s.get("season", season_of(day)),
        "chars": chars, "extras": extras, "vehicles": vehs, "props": props,
        "states": [states[c] for c in chars if c in states],
        "shot": s["shot"],
        "image_prompt": None if edit_only else image_prompt,
        "video_prompt": s["video"],
        "action_start": s["a0"], "action_end": s["a1"],
        "narration_ko": sc["nar"], "dialogue_ko": sc["dlg"], "sound": sc["sound"], "combat": sc["combat"],
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
    loc_line = f"{r['loc']}" + (f" ({r['subloc']})" if r['subloc'] != r['loc'] else "") if r["loc"] else "—"
    chars = ", ".join(r["chars"] + r["extras"]) or "—"
    vehs = ", ".join(r["vehicles"]) or "—"
    props = ", ".join(r["props"]) or "—"
    kb = "video8s" if r["type"] == "video8s" else "still_kenburns"
    L = []
    L.append(f"### {r['id']} | {sc['t']} | {loc_line} | {chars} | {vehs} | PROPS: {props} | TYPE: {kb} | {r['seconds']}s" + ("  · [COMBAT]" if r["combat"] else ""))
    L.append(f"SHOT: {r['shot']}" + ("  · ⚑ AERIAL/QUALITY" if r["aerial_quality"] else ""))
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
    if r["ai_risk"]:
        L.append(f"AI_RISK: {r['ai_risk']}")
    if r.get("insert_clip"):
        L.append(f"INSERT_CLIP ({r['insert_clip']['seconds']} s, tách riêng): {r['insert_clip']['prompt']}")
    return "\n".join(L) + "\n"

HEADER = """# 살수 612 — 2화 「요동성」 · SCENE LIST (VEO3 / G-Labs) · v1 · 2026-09-16 · veo-prompt-engineer
> Nguồn: `02_script/full_script_ep2.md` v2 QC-fixed (287 SC · 40:00) · `continuity_master.json` (LOCKED) · character/location/vehicle/prop bible · `02_script/sublocks_ep1.md` (tái dùng) + `sublocks_ep2.md` (mới) · template 04 §C–§H · decisions.md (sau QC 2화 → v2; sau veo 1화 P-38…45).
> Format §C như 1화. Mỗi SC: IMAGE_PROMPT (ảnh keyframe 16:9, nano_banana_pro, ref ≤10) → VIDEO_PROMPT (veo_31_fast, mode start_image, 8 s, 1080p). still_kenburns = chỉ ảnh, ken-burns ở khâu edit. `[COMBAT]` trên header = tag từ script (đếm tỷ lệ combat).
> **Quy ước prompt:** tag `@<ref_id>` đứng trước lock (ví dụ `@CHAR_001_dusty_ep2`, `@CHAR_104_siege_ep2`, `@LOC_002_bastion_se_ep2`) — tag = đúng `name` trong `reference_images`. VISUAL_LOCK dán NGUYÊN VĂN từ continuity_master.json; derived state = câu trạng thái nguyên văn từ character_bible (ref biến thể ✔ đính thay ref gốc; state không có ref → đính ref gốc); state 2화 do veo đặt thêm (dust_light/oil/bandaged/plain/ash/magazine…) ghi trong `logs/scratch/veo-ep2/build.py` DERIVED → đề xuất character-designer nhập bible. Không tên riêng, không chữ trong ảnh; Hangul trên xe KHÔNG vẽ (decisions #1) — chỉ số Ả Rập 1/2/3/4; số trên bảng gỗ / bộ đếm 잔탄 / màn hình nhiệt = **OVERLAY (edit)** (dòng `OVERLAY` + `overlay_text` trong json).
> **Riêng 2화:** mặt bị công = **nam + đông-nam** (tháp/mốc đá/xe húc trên đường đắp cổng nam 옹성/lỗ hổng 80 m tây 치 đông-nam); phía đông = đồi + đường bí mật, không địch. Cổng đông nhỏ có giàn đục (P9 SC_179–183) → K2 chui qua (SC_195). Tháp công thành VEH_201 = da trâu ướt (P1–P5) → **phủ chiếu bùn đất (VEH_201_mud_ep2)** từ SC_099; 충차 VEH_202 phủ đất hai lớp từ SC_074. 천둥 4 cháy (SC_145) → `VEH_002_burned`. 을지문덕: áo choàng đen kín mặt (SC_049–077, `CHAR_101_cloak_incognito_ep2`) → giáp trơn không chỏm (SC_078–127, `CHAR_101_plain_ep2`) → giáp đủ bộ (SC_159+). 탁발흠 hỏa công đêm đi bộ (không đính lock kỵ VEH_206, chỉ đính ref). 아리 khăn olive từ SC_104. 을보 giàn đục + chốt sắt 천둥 3. Mưa CHƯA có: mùa **4월 (bụi vàng, cỏ vàng chớm xanh) → 5월 → 6월 (cỏ xanh nhạt, đất giẫm nát bụi, khô nóng)** — câu `Season:` cuối mỗi prompt ngoại cảnh.
> **Sub-lock địa điểm:** cảnh nội thất/cận dùng sub-lock cố định (`02_script/sublocks_ep2.md`, nguồn máy `build.py` SUBLOC) — DÙNG NGUYÊN VĂN mọi SC. Ref mới cần tạo (12): `LOC_002_southwall_ep2`, `LOC_002_south_plain_ep2`, `LOC_002_bastion_se_ep2`, `LOC_002_eastgate_chisel_ep2`, `LOC_002_infirmary_ep2`, `LOC_002_tunnel_ep2`, `LOC_002_breach_ep2`, `LOC_003_valley_ep2`, `LOC_003_valley_burned_ep2`, `LOC_004_platform_ep2`, `VEH_201_mud_ep2`, `EXTRA_sui_siege_general_ref` → `05_references/extra/ref_jobs_ep2_extra.json`.
> **Nhân vật phụ không ID** (소년 척후, 초병, 수 공성총관, 수 전령, 통역, 농부, 선비 부장, 전차장/포수, 사수, K3 사수, PZF 사수, thợ đá, dân, lính đào hầm…): lock tạm cố định (build.py EXTRAS) — mặt lính phụ luôn quay đi/khuất mũ để né drift; 수 공성총관 PHẢI khác 전군총관 1화 (trẻ hơn, râu đen ngắn) và 우중문 (râu trắng).
> **Quy tắc 8 s (§F):** 1 SC = 1 địa điểm, 1 hành động chính, ≤2 người nói, 1 chuyển động camera. `CUT_HALF: yes` = hook 0–30 s + mọi khối/mini `[COMBAT]` + 2-BEAT (SC_001/003/238) → edit cắt 2 shot 4 s. Đại quân/aerial = ⚑ AERIAL/QUALITY → veo_31_quality cho video, nano_banana_pro + upscale 2K cho ảnh.
> **CHAIN_FROM:** chỉ khi SC trước là video8s, cùng địa điểm + nhân vật, hành động nối tiếp → glabs-operator lấy tail-frame làm start_image (`--chain`). Không chain quá 3 clip liên tiếp.
> **Ánh sáng theo bảng ngày/đêm (header script v2):** D25 sương rạng sáng (001–012) → ngày (013–025) → tối/đêm (026–033) · D26 bình minh–ngày (034–048) → hoàng hôn (049–052) · D27 bình minh (053–054) → ngày trận (055–072) → tối/đêm (073–077) · D28 sáng (078–085) → chiều (086–097) → đêm (098–099) · D29 bình minh (100–103) → chiều tối (104–105) → đêm (106–127) · D33 ngày (128–130) → đêm không trăng (131–133) · D45 bình minh 육합성 (134) → ngày (135–138) → đêm khô gió, hỏa công (139–151) · D46 bình minh tro (152–156) → sáng (157–173) · D47–69 ngày/đêm (174–193) · D70 đêm (194–198) · D71 bình minh → hoàng hôn 3차 공성 (199–249) → đêm (250–255) · D72–74 đêm 육합성 (256–263) · D75 đêm trăng (264–287).
> **Style tag (§D, cuối mọi image prompt):** `{style}`
> **Negative (§E, ghi 1 lần — glabs-operator dán vào field negative nếu model hỗ trợ):** `{neg}`
> **QC ảnh §G / QC video §H** áp dụng trước khi tạo video; ảnh fail → regenerate ≤3 lần (đổi seed / đơn giản hoá prompt), vẫn fail → giảm số nhân vật trong khung.

"""

PART_TITLES = {
    1: "[Phần 1] 안개 속의 탑 (0:00–1:30) · hook sương mù, 0–30 s không narrator · D25 rạng sáng",
    2: "[Phần 2] 항복 깃발의 비밀 (1:30–4:30) · cờ hàng giả thứ 3 [史] · vá tường đêm · D25–D26",
    3: "[Phần 3] 발전기 연료 30일 (4:30–7:00) · kiểm kê D26 · bệnh xá · người áo choàng đen · MID-ROLL 1 @7:00",
    4: "[Phần 4] 충차와 한 발 (7:00–10:30) · D27 1차 공성 thuần cổ + PZF 1 phát vào 충차 · CUT_HALF khối trận",
    5: "[Phần 5] 열 발에 둘 (10:30–14:00) · D28 을지문덕 lộ diện · cối 10 viên → 2 tháp cháy · Tùy lùi 6리 phủ đất · MID-ROLL 2 @14:00",
    6: "[Phần 6] 황제를 죽이면 (14:00–17:30) · D29 khăn olive · đại sảnh đêm · tên lửa vào thành (mini) · 탁군–요하 [史]",
    7: "[Phần 7] 검은 물이 탄다 (17:30–21:00) · D33 ENEMY POV · D45 육합성 · HỎA CÔNG đêm (narrator im 19:34–20:06) · MID-ROLL 3 @21:00",
    8: "[Phần 8] 항생제, 없습니다 (21:00–24:00) · D46 xác 천둥 4 · 2차 공성 Goguryeo tự giữ · 을지문덕 chạm K2 lần 1 · '열 발'",
    9: "[Phần 9] 치 위의 전차 (24:00–27:30) · D47–D70 tháo tường/đắp dốc/đục cổng đông 반 미터 · mốc đá · K2 chui vòm cổng đông · MID-ROLL 4 @27:30",
    10: "[Phần 10] 제3차 공성전 (27:30–34:30) · D71 6월 11 [史] · 6 phase · narrator im 31:30–33:00 · CUT_HALF toàn khối · K2 22→12",
    11: "[Phần 11] 성은 버티오, 문제는 평양이오 (34:30–37:30) · D71 đêm vá lỗ hổng · 육합성 9군 30만 5천 [史] · 9 quân đi qua",
    12: "[Phần 12] 400km (37:30–40:00) · D75 que đo dầu · '전차 한 대 몫' · 탁발흠 bám đuôi · end card",
}

def validate(recs):
    errs = []
    ids = [r["id"] for r in recs]
    exp = [f"SC_{i:03d}" for i in range(1, N_SC + 1)]
    if ids != exp:
        missing = sorted(set(exp) - set(ids)); extra = sorted(set(ids) - set(exp))
        errs.append(f"ID mismatch: missing={missing[:10]} extra={extra[:10]} n={len(ids)}")
    t = 0
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
                        "Hae Mo", "Jeong-su", "Eul-bo", "A-ri", "Yu Zhongwen", "Yuwen", "Mundeok", "Cheondung", "Thunder"):
                if tok in r["image_prompt"] or tok in r["video_prompt"]: errs.append(f"{r['id']} proper name '{tok}' in prompt")
        if r["chain_from"]:
            prev = recs[ids.index(r["chain_from"])]
            if prev["type"] != "video8s": errs.append(f"{r['id']} chain_from {r['chain_from']} is not video8s")
            if ids.index(r["chain_from"]) != ids.index(r["id"]) - 1: errs.append(f"{r['id']} chain_from not previous SC")
    # chain ≤3 liên tiếp
    run = 0
    for r in recs:
        run = run + 1 if r["chain_from"] else 0
        if run > 3: errs.append(f"{r['id']} chain run > 3")
    if t != 2400: errs.append(f"total seconds {t} != 2400")
    return errs

def usage_report(recs):
    C = collections.Counter
    cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra = C(), C(), C(), C(), C(), C(), C(), C()
    for r in recs:
        for c in r["chars"]: cnt_char[c] += 1
        for s in r["states"]: cnt_state[s] += 1
        if r["loc"]: cnt_loc[r["loc"]] += 1; cnt_sub[r["subloc"]] += 1
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
    recs.sort(key=lambda r: r["id"])
    errs = validate(recs)
    if errs:
        print("VALIDATION ERRORS:"); print("\n".join(errs))
        if "--force" not in sys.argv: sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    md = [HEADER.replace("{style}", STYLE).replace("{neg}", NEGATIVE)]
    nv = sum(1 for r in recs if r["type"] == "video8s"); ns = len(recs) - nv
    md.append(f"**Tổng:** {len(recs)} SC · {nv} video8s · {ns} still_kenburns · {sum(r['seconds'] for r in recs)} s · chain_from: {sum(1 for r in recs if r['chain_from'])} · cut_half: {sum(1 for r in recs if r['cut_half'])} · aerial/quality: {sum(1 for r in recs if r['aerial_quality'])} · [COMBAT]: {sum(1 for r in recs if r['combat'])} · overlay: {sum(1 for r in recs if r['overlay_text'])}\n\n---\n")
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
    print(f"OK {len(recs)} SC · video {nv} · still {ns} · chain {sum(1 for r in recs if r['chain_from'])} · cut_half {sum(1 for r in recs if r['cut_half'])} · aerial {sum(1 for r in recs if r['aerial_quality'])} · combat {sum(1 for r in recs if r['combat'])}")

NEW_REF_NOTES = {
    "LOC_002_southwall_ep2": "(locations, 16:9) mặt tường nam đang bị vây: lan can đá, 치, giá tên, chum, nồi, trống — phía ngoài là đồng bằng giẫm nát, hào lấp, hàng tháp Tùy, biển lều — sub-lock `LOC_002_southwall` (P1–P10, nhiều SC nhất).",
    "LOC_002_south_plain_ep2": "(locations, 16:9) đồng bằng nam thành từ phía Tùy: hào lấp thành đường đắp, hàng tháp 8 bánh + thang, cờ, lều; tường granite + tháp cổng phía sau — sub-lock `LOC_002_south_plain`, `_sui_lines`, `_sui_yard`, `_causeway`, `_se_corner_out`, `_marker_field`.",
    "LOC_002_bastion_se_ep2": "(locations, 16:9) 치 đông-nam SAU khi cải tạo: khe châu mai đục vuông cỡ nòng pháo, dốc đất 20° phía sau (tường trong tháo 10 hàng), K2 trên 치 — sub-lock `LOC_002_bastion_se_k2`, `_ramp`, `_ramp_work` (P9–P10).",
    "LOC_002_eastgate_chisel_ep2": "(locations, 16:9) vòm cổng đông nhỏ có giàn gỗ, hai vách đục lộ đá trắng mới (반 미터) — sub-lock `LOC_002_eastgate_chisel`, `_eastgate_night_k2` (SC_179, 182–183, 195).",
    "LOC_002_infirmary_ep2": "(locations, 16:9) nội thất nhà gỗ bệnh xá cạnh tường: chiếu cói, ổ rơm, chậu, thảo dược treo, cửa chớp lưới — sub-lock `LOC_002_infirmary` (SC_043–047).",
    "LOC_002_tunnel_ep2": "(locations, 16:9) hầm Tùy: cột chống gỗ, đèn dầu, vách rỉ nước, giỏ đất — sub-lock `LOC_002_tunnel` (SC_010, 230).",
    "LOC_002_breach_ep2": "(locations, 16:9) lỗ hổng 80 m tường nam: mặt ngoài đổ thành dốc đá, tường trong còn — sub-lock `LOC_002_breach`, `_breach_in`, `_breach_repaired` (P10–P12).",
    "LOC_003_valley_ep2": "(locations, 16:9) thung lũng 2화 tháng 4: lưới bạc màu, 3 K21 hàng ngang, 2 phuy sau bao cát cách xe 30 bước, sồi chớm lá — sub-lock `LOC_003_valley_apr`, `_line`, `_line_night`, `_drums`, `_drums_fire`, `_k2_day`, `_tent_ext_day`, `_hillside_pov`.",
    "LOC_003_valley_burned_ep2": "(locations, 16:9) thung lũng SAU hỏa công: xác 천둥 4 đen, xe tải cháy sém, hố phuy, tro — sub-lock `LOC_003_fire_wide`, `_wreck_dawn`, `_wreck_day`, `_line_jun` (P7–P12).",
    "LOC_004_platform_ep2": "(locations, 16:9) đài quan sát gỗ của 양제 phía nam thành: lọng vàng, cờ vàng, đuốc chân đài, tường thành phía xa — sub-lock `LOC_004_platform` (SC_200, 213, 221, 248).",
    "VEH_201_mud_ep2": "(vehicles, 16:9, phông trắng) 팔륜누차 PHỦ CHIẾU BÙN ĐẤT (derived VEH_201): mặt trước/hông/đỉnh phủ chiếu rơm ngâm bùn + lớp đất ướt, màu nâu đất thay da đen — dùng cho mọi tháp từ SC_099 (P5 đêm) tới hết tập (~25 SC).",
    "EXTRA_sui_siege_general_ref": "(characters, 3:4) 수 공성총관 ~45 tuổi, gầy rắn, râu đen ngắn vuông, áo choàng đỏ sẫm, chỏm tua ĐEN — PHẢI khác 전군총관 1화 (55, râu đen-xám, chỏm đỏ) và 우중문 (râu trắng) — 12 SC (P2, P4, P5, P7, P10).",
}

def write_usage(recs):
    cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra = usage_report(recs)
    L = ["# 2화 「요동성」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)",
         f"> Đếm theo `04_veo/scenes_ep2.json` ({len(recs)} SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.", ""]
    L.append("## 1. Nhân vật (CHAR) — số SC xuất hiện")
    L.append("| CHAR | SC | Derived state trong 2화 (SC) |"); L.append("|---|---|---|")
    for c, n in sorted(cnt_char.items()):
        sts = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_state.items()) if k.startswith(c))
        L.append(f"| {c} | {n} | {sts or '— (base)'} |")
    L.append(""); L.append("### Derived state text-only của bible (không ref riêng → đính ref gốc/biến thể gần nhất)")
    for k in ("CHAR_201_field_dust_ep2", "CHAR_003_helmet_combat"):
        if k in cnt_state: L.append(f"- `{k}` → ref `{DERIVED[k][1]}` ({cnt_state[k]} SC): {DERIVED[k][2]}")
    L.append(""); L.append("### Derived state 2화 do veo-prompt-engineer đặt thêm (không có trong bible — đề xuất character-designer nhập; đính ref gốc/biến thể gần nhất)")
    for k, (cid, rid, txt) in DERIVED.items():
        if k in cnt_state and rid != k and k not in ("CHAR_201_field_dust_ep2", "CHAR_003_helmet_combat"):
            L.append(f"- `{k}` → ref `{rid}` ({cnt_state[k]} SC): {txt}")
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
    L.append("- VEH_002: 천둥 2/3/4 phân biệt bằng `veh_state` (numeral 2 · numeral 3 + chốt sắt · numeral 4 → `VEH_002_burned`); VEH_201 tháp: `TOWER_HIDE` (P1–P5) → `TOWER_MUD` + ref `VEH_201_mud_ep2` (SC_099+); VEH_202: `RAM_MUD` từ SC_074; VEH_001: `K2_CLEAN` → `K2_WET_NET` (P6–P7) → `K2_SOOT` (SC_249+).")
    L.append(""); L.append("## 4. Đạo cụ (PROP) — số SC")
    L.append("| PROP | SC |"); L.append("|---|---|")
    for p, n in cnt_prop.most_common(): L.append(f"| {p} | {n} |")
    L.append(""); L.append("## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)")
    L.append("| # | ref id | thư mục | số SC đính | trạng thái |"); L.append("|---|---|---|---|---|")
    for i, (r, n) in enumerate(cnt_ref.most_common(), 1):
        status = "**CHƯA CÓ — job trong ref_jobs_ep2_extra.json**" if r in NEW_REFS else ("có job (ep1 extra, DUYỆT)" if r in ("LOC_003_hollow_d1", "LOC_003_ford_night", "LOC_008_steppe_ep1", "LOC_003_steppe_d1", "LOC_010_wide", "EXTRA_boy_scout_ref", "WPN_102_ref", "EXTRA_sui_vanguard_general_ref") else "có job")
        L.append(f"| {i} | {r} | {REF_DIR[r]} | {n} | {status} |")
    L.append("")
    L.append("### Ref CHƯA CÓ trong ref_jobs.json (2화 — job đã ghi `05_references/extra/ref_jobs_ep2_extra.json`; world-designer/character-designer duyệt, glabs-operator tạo trước lô ảnh cảnh)")
    for r, note in NEW_REF_NOTES.items():
        L.append(f"- `{r}` {note} — {cnt_ref.get(r, 0)} SC.")
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
    L.append("## 7. SC có OVERLAY ở edit (số/chữ KHÔNG vẽ bằng AI)")
    L.append("| SC | overlay |"); L.append("|---|---|")
    for r in recs:
        if r["overlay_text"]: L.append(f"| {r['id']} | {r['overlay_text']} |")
    L.append("")
    L.append("## 8. SC RỦI RO AI & cách né trong prompt")
    risk = [r for r in recs if r["ai_risk"]]
    L.append("| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |"); L.append("|---|---|---|")
    for r in risk: L.append(f"| {r['id']} | {r['ai_risk'].split('→')[0].strip()} | {r['ai_risk'].split('→')[1].strip() if '→' in r['ai_risk'] else '—'} |")
    L.append("")
    L.append("### Quy tắc né chung (áp dụng toàn tập — kế thừa 1화 + riêng 2화)")
    L.append("- **Đám đông cận**: mọi cảnh ≥6 người → wide/aerial hoặc máy sau lưng hàng người, mặt lính phụ quay đi/khuất mũ; chỉ nhân vật có ID mới thấy mặt rõ.")
    L.append("- **Chữ**: bảng gỗ phấn, bộ đếm 잔탄, màn hình nhiệt, thẻ lụa/thẻ tre, bản vẽ binh thư, end card → prompt 'chalk marks / blurred figures / no readable characters'; số thật = OVERLAY (edit) — bảng §7.")
    L.append("- **Tay cầm súng**: K2C1 luôn 'muzzle down / slung'; PZF: mặt xạ thủ khuất sau kính ngắm; bắn = wide hoặc chớp lửa đầu nòng, không cận ngón tay trên cò.")
    L.append("- **Tháp công thành + hàng trăm người đẩy**: aerial thấp/wide, người đẩy = 'backs bent, faces down'; tháp = ref VEH_201 (da) hoặc VEH_201_mud_ep2 (đất) đính đúng giai đoạn.")
    L.append("- **Lửa/nổ**: 1 nguồn lửa chính mỗi khung, máy tĩnh hoặc 1 chuyển động; nổ phuy (SC_143) = wide thấp, mọi người nằm rạp; 40mm nổ dây chuyền (SC_146) = chớp qua nắp nóc, không cận.")
    L.append("- **Thương tích/bỏng**: băng trắng, không vết thương hở cận; bỏng = 'red, blistered' trên tay/cẳng tay, không mặt.")
    L.append("- **Chân dung lịch sử (을지문덕/양제/우중문/우문술)**: theo lock hư cấu, không giống người thật; 을지문덕 SC_049–077 KHÔNG lộ mặt (mũ trùm, lưng, bàn tay).")
    L.append("- **K2 trên 치 / chui vòm cổng**: 1 chuyển động xe, máy tĩnh; khe đục/vòm = ref LOC_002_bastion_se_ep2 / LOC_002_eastgate_chisel_ep2 để giữ hình dạng đá.")
    L.append("- **Hangul trên xe**: KHÔNG vẽ (chỉ số Ả Rập 1/2/3/4 + 태극기 nhỏ); '천둥' chỉ ở thoại/radio.")
    open(f"{OUT_DIR}/ep{EP}_asset_usage.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
