# -*- coding: utf-8 -*-
"""
VEO scene-list builder — SALSU_612 · 1화
Đọc: full_script_ep1.md (t / type / narration / thoại / [SOUND] — nguyên văn) + continuity_master.json (VISUAL_LOCK nguyên văn)
      + batch_XX.py (dữ liệu hình ảnh do veo-prompt-engineer biên).
Ghi: 04_veo/scene_list_ep1.md · 04_veo/scenes_ep1.json · 04_veo/ep1_asset_usage.md · output/ep1/kich_ban/scene_list.md
"""
import json, re, os, sys, glob, importlib.util, collections

ROOT = "/Users/admin/phim han quoc"
PROJ = ROOT + "/projects/SALSU_612"
SCRIPT = PROJ + "/02_script/full_script_ep1.md"
CM = json.load(open(PROJ + "/continuity_master.json", encoding="utf-8"))
OUT_DIR = PROJ + "/04_veo"
HERE = os.path.dirname(os.path.abspath(__file__))

STYLE = CM["style_tag"]
NEGATIVE = ("cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, "
            "modern buildings in historical scene, anachronistic clothing")

# ---------------------------------------------------------------- LOCKS (nguyên văn continuity_master.json)
LOCKS = {}
LOCKS.update(CM["character_locks"]); LOCKS.update(CM["vehicle_locks"]); LOCKS.update(CM["prop_locks"])
LOCKS["PROP_004"] = CM["vehicle_locks"]["EQP_001"]  # continuity_master ghi placeholder → prop_bible: PROP_004 = EQP_001
LOC_LOCK = {k.split("_")[0] + "_" + k.split("_")[1]: v for k, v in CM["location_locks"].items()}  # LOC_001 → lock

# ---------------------------------------------------------------- REF SHEET IDS (05_references/*/ref_jobs.json) + refs CẦN TẠO
REF_DIR = {}
for d in ("characters", "locations", "vehicles", "props"):
    for j in json.load(open(f"{PROJ}/05_references/{d}/ref_jobs.json", encoding="utf-8")):
        REF_DIR[j["id"]] = d
NEW_REFS = {  # chưa có trong ref_jobs.json → glabs-operator/world-designer tạo trước (xem ep1_asset_usage.md)
    "LOC_010_wide": "locations", "LOC_003_steppe_d1": "locations", "LOC_003_hollow_d1": "locations",
    "LOC_008_steppe_ep1": "locations", "LOC_003_ford_night": "locations",
    "WPN_102_ref": "vehicles", "EXTRA_boy_scout_ref": "characters", "EXTRA_sui_vanguard_general_ref": "characters",
}
REF_DIR.update(NEW_REFS)

def ref_path(rid):
    return f"projects/SALSU_612/05_references/{REF_DIR[rid]}/{rid}_1.png"

# ---------------------------------------------------------------- DERIVED STATES (character_bible DERIVED_STATES — câu trạng thái nguyên văn; ✔ = có ref riêng)
DERIVED = {
    # id: (char, ref_id_to_attach, state text)
    "CHAR_006_facepaint_ep1": ("CHAR_006", "CHAR_006_facepaint_ep1",
        "Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim."),
    "CHAR_106_refugee_ep1": ("CHAR_106", "CHAR_106_refugee_ep1",
        "No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, someone else's blood on the right sleeve, walking staff, frightened exhausted face."),
    "CHAR_107_refugee_ep1": ("CHAR_107", "CHAR_107_refugee_ep1",
        "A coarse hemp scarf over the head, yellow dust on clothes and face, tear tracks through the dust, one straw sandal broken, clutching a basket, frightened."),
    "CHAR_205_survivor_ep1": ("CHAR_205", "CHAR_205_survivor_ep1",
        "Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes."),
    "CHAR_201_robe_only_ep3": ("CHAR_201", "CHAR_201_robe_only_ep3",
        "Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged."),
    # text-only states (bible: không ref riêng → đính ref gốc)
    "CHAR_105_dusty_ep1": ("CHAR_105", "CHAR_105_ref",
        "Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent."),
    "CHAR_102_seated_throne": ("CHAR_102", "CHAR_102_ref",
        "Seated on a red-lacquered wooden throne, hands on knees, edict scroll on a low table."),
    # ep1 in-episode states do veo-prompt-engineer đặt (theo bảng "Trạng thái theo tập" 1화 của bible) — không ref riêng
    "CHAR_106_bandaged_ep1": ("CHAR_106", "CHAR_106_refugee_ep1",
        "No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, a clean white modern field bandage wrapped tightly around the right lower leg, moving with a heavy limp, walking staff."),
    "CHAR_107_camp_ep1": ("CHAR_107", "CHAR_107_refugee_ep1",
        "Hemp scarf pushed back off the head, yellow dust on clothes, dried tear tracks, one straw sandal broken, small basket kept close."),
    "CHAR_002_powder_ep1": ("CHAR_002", "CHAR_002_ref",
        "Gunpowder residue smudged on both bare forearms, fine yellow dust on helmet and shoulders."),
    "CHAR_002_smoke_ep1": ("CHAR_002", "CHAR_002_ref",
        "Face smudged black with net smoke, one lens of the goggles cracked, wet mud on sleeves and forearms, sweat cutting lines through the grime."),
    "CHAR_004_gloves_ep1": ("CHAR_004", "CHAR_004_ref",
        "Blue nitrile gloves stained with fresh blood, a few loose strands of hair escaping the bun, fine yellow dust on helmet."),
    "CHAR_003_oil_ep1": ("CHAR_003", "CHAR_003_ref",
        "Mechanic gloves dark with engine oil, trouser hems muddy with crushed grass, fine yellow dust on the patrol cap."),
    "CHAR_003_mud_ep1": ("CHAR_003", "CHAR_003_ref",
        "Wet grey mud on gloves, forearms and chest of the body armor, patrol cap pushed back, grease streak on one cheek."),
    "CHAR_104_dust_ep1": ("CHAR_104", "CHAR_104_ref",
        "Road dust on the grey wool cloak and beard, torch soot on the cheeks, tired watchful eyes."),
}

# ---------------------------------------------------------------- EXTRAS (không ID trong bible) — lock tạm, dùng NGUYÊN VĂN mọi SC; đề xuất world-designer đưa vào bible
EXTRAS = {
    "BOY_SCOUT": "17-year-old Goguryeo boy scout, thin small build, sun-browned round face, large frightened dark eyes, cracked lips, black hair tied under a brown cloth headband, coarse undyed brown hemp jacket with crossed collar and white border, wide trousers bound at the ankles, straw sandals, short composite bow, hip quiver, yellow dust on face and clothes",
    "SUI_VANGUARD_GENERAL": "Chinese man in his mid-50s, heavy broad build, wide fleshy face with thick black brows, long black beard streaked grey to mid-chest, black topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest, gilt-hilted straight sword",
    "SUI_VANGUARD_CMDR_DEAD": "Sui general around 50 with a short black beard, in mingguang iron lamellar armor with two polished round breast mirrors, red silk cloak, iron helmet with red tassel crest",
    "PYONGYANG_COURIER": "Goguryeo courier around 25, lean build, road-dusty face, black topknot under a cloth headband, light leather lamellar vest over a dark brown hemp jacket, wide trousers, straw sandals, holding a black lacquered bamboo tube with red silk cord",
    "SUI_EUNUCH": "Sui court eunuch in a plain grey-blue silk robe and black gauze cap, clean-shaven, head bowed",
    "SUI_EUNUCH_READER": "Sui court official in a dark blue silk robe and black gauze cap with side wings, holding an open pale yellow silk scroll with columns of black brush calligraphy",
    "ROK_SOLDIER": "ROK Army soldier in granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, face turned away or shadowed under the helmet brim",
    "ROK_SOLDIERS": "ROK Army soldiers in granite-pattern digital camo uniforms, matching body armor and covered ballistic helmets, Korean flag patches on right shoulders, faces turned away or shadowed under helmet brims",
    "ROK_RADIOMAN": "young ROK Army radio operator in granite-pattern digital camo uniform, matching body armor, covered ballistic helmet, headset over the helmet, Korean flag patch on right shoulder, face partly hidden by the handset",
    "ROK_GUNNER_TURRET": "ROK Army vehicle gunner in granite-pattern digital camo uniform and crew helmet with boom microphone, seen inside a cramped red-lit turret, face half in shadow",
    "ROK_DRIVER": "ROK Army vehicle driver in granite-pattern digital camo uniform and crew helmet with boom microphone, seen from behind in a cramped driver's seat",
    "GOG_INFANTRY": "Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles",
    "GOG_ARCHERS": "Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows",
    "GOG_CAVALRYMEN": "Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants",
    "XIANBEI_ARCHER": "Xianbei horse archer in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow drawn, hip quiver",
    "XIANBEI_SCOUTS": "Xianbei scouts in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, crawling low with bows slung on their backs",
    "REFUGEES": "Goguryeo refugees in undyed hemp jackets and trousers or pleated skirts, cloth bundles on their backs, children, two-wheeled ox carts loaded with grey hemp grain sacks, oxen under wooden yokes",
    "OX_DRIVER": "Goguryeo ox-cart driver in a coarse undyed hemp jacket and trousers, cloth headband, straw sandals, cracking a leather whip",
    "SUI_LABORERS": "Sui conscript laborers in undyed hemp jackets and head cloths hauling two-wheeled wooden supply carts loaded with grain sacks under cloth covers",
}

# ---------------------------------------------------------------- SUB-LOCATION LOCKS (bible LOC lock hoặc REF_PROMPT_EN_DETAIL/INTERIOR — cố định, dùng nguyên văn mọi SC)
SUBLOC = {
    # key: (loc_id, ref_id, text)
    "LOC_001": ("LOC_001", "LOC_001_wide", LOC_LOCK["LOC_001"]),
    "LOC_001_bank": ("LOC_001", "LOC_001_detail",
        "East bank of the Liao River, early spring 612 AD: the end of a Sui pontoon bridge of flat wooden boats lashed with thick hemp rope and plank decking, wooden mooring stakes driven into grey mud, a red and yellow silk banner with black tassels on a tall pole, hoofprints and cart ruts in the mud, a steep muddy bank rising to dry yellow grass bending in wind, the wide brown river, cold grey diffused light with yellow dust drifting through it"),
    "LOC_001_march": ("LOC_001", "LOC_001_wide",
        "A wide beaten dirt road across the flat North China plain in early spring 612 AD, dry knee-high yellow grass to the horizon bending under constant wind, drifting yellow dust, cold pale grey overcast sky, no trees, no buildings"),
    "LOC_001_canal": ("LOC_001", "LOC_001_wide",
        "A straight man-made canal cutting across the flat yellow plain in early spring 612 AD, packed with flat-bottomed wooden grain barges under cloth covers, a towpath beside it, dry yellow grass, drifting yellow dust, cold pale grey overcast sky"),
    "LOC_001_sui_camp_night": ("LOC_001", "LOC_001_wide",
        "Sui vanguard camp on the east bank of the Liao River at night: grid rows of grey felt tents, lines of burning torches, red and yellow banners with black tassels on black lacquered poles, a large general's tent in the center, wooden watchtowers, horse lines, the three pontoon bridges glittering with torches on the wide black river beyond"),
    "LOC_001_sui_tent": ("LOC_001", "LOC_001_detail",
        "Interior of a Sui vanguard general's campaign tent at night: grey felt walls, a low black lacquered table, silk lanterns giving warm orange light, a silk map painted with rivers and a square fortress hung on a wooden frame, a sword rack, a red and yellow banner, a bronze brazier"),
    "LOC_001_sui_camp_day": ("LOC_001", "LOC_001_wide",
        "Sui camp on the east bank of the Liao River by day: grid rows of grey felt tents to the horizon, red and yellow banners, horse lines, cooking smoke, trampled yellow grass and dust, cold pale grey sky"),
    "LOC_001_north_steppe": ("LOC_001", "LOC_001_wide",
        "Open yellow steppe north of the Goguryeo fortress, dry knee-high yellow grass bending in one direction under constant wind, drifting yellow dust, low grassy rises, cold pale grey sky, early spring, no trees"),
    "LOC_002": ("LOC_002", "LOC_002_wide", LOC_LOCK["LOC_002"]),
    "LOC_002_night_road": ("LOC_002", "LOC_002_wide",
        "Night on the open yellow steppe west of the Goguryeo fortress: dry knee-high yellow grass under thin moonlight, drifting dust, the dark mass of the fortress on its low rise with torches along dry-stacked grey granite walls and a timber gate tower far ahead"),
    "LOC_002_gate": ("LOC_002", "LOC_002_detail",
        "South gate of the Goguryeo fortress at night: a semicircular stone barbican of dry-stacked grey granite, a narrow arched gate passage with two-leaf iron-sheathed wooden doors studded with large iron nails, a two-story timber gate tower with dark grey tiled roof above, rectangular protruding bastions, burning torches along the wall, black three-legged crow banners"),
    "LOC_002_eastwall": ("LOC_002", "LOC_002_detail",
        "On top of the east wall of the Goguryeo fortress: dry-stacked grey granite blocks without mortar forming a rectangular protruding bastion with a low stone parapet and narrow arrow slits, a wooden rack of arrows, clay water jars, a large hide war drum on a wooden stand, a black three-legged crow banner on a pole, the dirt road below running east through dry yellow steppe"),
    "LOC_002_eastroad": ("LOC_002", "LOC_002_wide",
        "The east road: a beaten dirt road through dry knee-high yellow steppe climbing a long gentle slope toward the east gate of the Goguryeo fortress, dry-stacked grey granite walls with rectangular protruding bastions, a timber gate tower with dark tiled roof, torches on the wall"),
    "LOC_002_eastgate": ("LOC_002", "LOC_002_detail",
        "East gate of the Goguryeo fortress at night: two-leaf wooden gate doors sheathed with iron plates and studded with large iron nails, a heavy wooden crossbar, a stone gate passage in dry-stacked grey granite walls flanked by two rectangular protruding bastions, burning torches in iron brackets, black three-legged crow banners"),
    "LOC_002_gateyard": ("LOC_002", "LOC_002_detail",
        "Inside the east gate of the Goguryeo fortress at night: a packed-earth yard behind two-leaf iron-sheathed wooden gate doors, a stone stair climbing the dry-stacked grey granite wall, torches in iron brackets, black three-legged crow banners, timber halls with dark tiled roofs behind"),
    "LOC_002_granary": ("LOC_002", "LOC_002_detail",
        "Inside the Goguryeo fortress at a raised-floor timber granary standing on thick wooden posts with a dark grey tiled roof, wooden steps up to its door, grey hemp grain sacks, a packed-earth street, two-wheeled ox carts, timber halls and a three-story wooden pagoda behind, the dry-stacked grey granite wall in the distance, cold grey daylight"),
    "LOC_002_hall": ("LOC_002", "LOC_002_interior",
        "Interior of a Goguryeo commander's timber hall at night, 612 AD: dark wooden floor, thick round wooden pillars with faded red lacquer, low black lacquered table with a leather map painted in ink, woven reed mats, a rack of spears and composite bows, bronze incense burner, clay oil lamps giving warm yellow light, latticed wooden windows shuttered, a black three-legged crow banner on the wall, smoke haze"),
    "LOC_002_westwall": ("LOC_002", "LOC_002_detail",
        "On a rectangular protruding bastion of the west wall of the Goguryeo fortress: dry-stacked grey granite parapet with arrow slits, a black three-legged crow banner on a tall bamboo pole, and beyond the wall an ocean of grey felt Sui tents with red and yellow banners covering the trampled yellow plain to the horizon under a pale silver sky"),
    "LOC_002_siege_works": ("LOC_002", "LOC_002_wide",
        "The yellow plain west of the Goguryeo fortress: Sui soldiers digging a ditch and raising earth banks, wooden watchtowers going up, the raw timber frames of siege towers being assembled, grey felt tents in grid rows behind, dry-stacked grey granite fortress walls with rectangular bastions and a timber gate tower in the background, cold grey sky"),
    "LOC_003": ("LOC_003", "LOC_003_wide", LOC_LOCK["LOC_003"]),
    "LOC_003_steppe": ("LOC_003", "LOC_003_steppe_d1",
        "Open flat steppe of dry knee-high yellow grass to the horizon under a cold pale grey sky, grass bending in one direction under constant wind, drifting yellow dust, no trees, no hills, no buildings, a fifty-meter stub of modern asphalt road ending abruptly in the grass as if cut with a knife, modern South Korean army vehicles in three-tone green-brown-black camouflage parked on it"),
    "LOC_003_hollow": ("LOC_003", "LOC_003_hollow_d1",
        "A shallow grassy hollow in the open yellow steppe, dry knee-high yellow grass bending under constant wind, a low grassy rise to the east, drifting yellow dust under a cold pale grey sky, modern South Korean army vehicles in three-tone green-brown-black camouflage parked under green-brown camouflage netting, no trees, no buildings"),
    "LOC_003_gully": ("LOC_003", "LOC_003_hollow_d1",
        "A narrow dry gully cutting through the yellow steppe east of the hollow: a bed of pale grey river cobbles, low walls of grey rock and crumbling earth, dry yellow grass along the rim bending in wind, cold grey light, no trees"),
    "LOC_003_ridge_sunset": ("LOC_003", "LOC_003_hollow_d1",
        "The open yellow steppe at sunset: a long low grassy ridge to the east backlit by a low amber sun, dry knee-high yellow grass glowing orange, long shadows, drifting dust lit gold, a shallow hollow below with modern South Korean army vehicles in three-tone green-brown-black camouflage"),
    "LOC_003_trail": ("LOC_003", "LOC_003_wide",
        "A dirt trail at night skirting low hills of bare oak scrub and dry yellow grass into a shallow valley, thin moonlight, dark oak thickets on the slopes above"),
    "LOC_003_tent": ("LOC_003", "LOC_003_detail",
        "Inside a modern South Korean army command tent at night, dim red tactical lamplight: a steel folding table with a paper topographic map weighted by a cracked military tablet and a PRC-999K backpack radio with handset, a hand-written tally board of ammunition and fuel numbers on a plank, stacked olive-green ammunition cans, a quadcopter drone battery charging from a cable that runs out under the tent flap, a Goguryeo clay water jar and a bronze oil lamp on the earth floor, faint yellow dust in the air"),
    "LOC_003_tent_ext": ("LOC_003", "LOC_003_wide",
        "Outside the olive-green command tent of the hidden company base at night: a faint red glow through the tent flap, stacked olive-green ammunition cans, a boxy 4x4 command vehicle with antennas, camouflage netting, brown hemp Goguryeo tents with wooden poles beside the olive army tents, dry yellow grass, bare oak scrub on the dark slopes"),
    "LOC_003_medic": ("LOC_003", "LOC_003_wide",
        "The aid station of the hidden company base at night: a canvas awning off an olive-green army tent, a folding stretcher on olive ammunition cans, a headlamp and a shaded red lamp, camouflage netting, brown hemp Goguryeo tents beside, dry yellow grass, dark oak scrub slopes"),
    "LOC_003_hearth": ("LOC_003", "LOC_003_wide",
        "A Goguryeo stone hearth fire at the hidden company base at night: a ring of grey stones, a clay pot over orange flames, brown hemp Goguryeo tents with wooden poles beside olive-green army tents, camouflage netting over dark vehicle shapes behind, dry yellow grass, bare oak scrub"),
    "LOC_003_mortar": ("LOC_003", "LOC_003_wide",
        "A sandbagged mortar pit on a small grassy knoll at the south end of the hidden valley base at night: two 81mm mortars on bipods, round baseplates, olive ammunition cans, a range card on a stake, dry yellow grass, dark oak scrub slopes, the valley below"),
    "LOC_003_k2": ("LOC_003", "LOC_003_wide",
        "The hidden company base at night: a K2 tank under green-brown camouflage netting in a shallow valley of dry yellow grass, thin moonlight on the netting, bare oak scrub on the dark slopes, olive-green army tents and brown hemp Goguryeo tents beyond"),
    "LOC_003_mouth": ("LOC_003", "LOC_003_wide",
        "The mouth of the hidden valley at night: dry yellow grass, bare oak scrub on low hills either side, a stony stream bed, modern South Korean army vehicles in three-tone green-brown-black camouflage waiting under thin moonlight, the dark steppe and the distant fortress beyond"),
    "LOC_003_ford": ("LOC_003", "LOC_003_ford_night",
        "A shallow stream ford north of the valley mouth at night: a bed of pale grey cobbles under a hand's depth of black water, wide banks of dark grey mud on both sides, dry yellow reeds and grass, a low grassy ridge rising to the north, thin moonlight"),
    "LOC_003_ford_northbank": ("LOC_003", "LOC_003_ford_night",
        "The north bank of the stream ford at night: deep dark grey mud churned and glistening, tufts of dry yellow grass, the cobble ford and black water behind, a low grassy ridge rising to the north under thin moonlight"),
    "LOC_003_northridge": ("LOC_003", "LOC_003_ford_night",
        "A low grassy ridge north of the valley at night: dry knee-high yellow grass under thin moonlight, bare oak scrub, the dark hollow of a valley below with a faint red glow leaking through camouflage netting"),
    "LOC_003_hill_ford": ("LOC_003", "LOC_003_ford_night",
        "A grassy hill above the stream ford at night: dry knee-high yellow grass, bare oak scrub, the pale cobble ford and its dark mud banks visible below, a low ridge to the north, thin moonlight"),
    "LOC_003_westrim": ("LOC_003", "LOC_003_wide",
        "The western rim of the hidden valley at night: dry yellow grass and bare oak scrub on the crest, and beyond it the whole dark plain covered with tens of thousands of Sui campfires like a field of fallen stars to the horizon, the black mass of the Goguryeo fortress in between"),
    "LOC_003_dawn": ("LOC_003", "LOC_003_wide",
        "The hidden company base at cold grey dawn: modern South Korean army vehicles in three-tone green-brown-black camouflage under camouflage netting in a shallow valley of dry yellow grass, thin mist on the ground, dew on the netting, bare oak scrub on the slopes, olive-green army tents beside brown hemp Goguryeo tents, a stony stream bed"),
    "LOC_003_rim_day": ("LOC_003", "LOC_003_wide",
        "The eastern rim of the hidden valley by day: dry yellow grass and bare oak scrub, and in the distance the Goguryeo fortress of dry-stacked grey granite on its low rise with black banners, the yellow plain beyond it covered with grey felt Sui tents to the horizon under a pale grey sky"),
    "LOC_004": ("LOC_004", "LOC_004_wide", LOC_LOCK["LOC_004"]),
    "LOC_004_parade": ("LOC_004", "LOC_004_wide",
        "A vast packed-earth parade ground at dawn, 612 AD: tens of thousands of Sui infantry in mingguang armor with polished round chest plates standing in square blocks to the horizon, huge red-lacquered war drums with gold patterns on wooden frames either side of a red-lacquered timber reviewing platform, red and yellow silk banners with black tassels, low bright sun through dust haze"),
    "LOC_004_pavilion_ext": ("LOC_004", "LOC_004_wide",
        "The Sui emperor's traveling court on the west bank of the Liao River at night: a huge pavilion tent with a golden silk roof and red pillars raised on a wooden dais, yellow and red silk drapes, rows of burning torches on tall poles, hundreds of eunuchs in grey-blue silk robes lining the approach, red and yellow banners, an ocean of grey felt tents with campfires to the horizon"),
    "LOC_004_pavilion_int": ("LOC_004", "LOC_004_detail",
        "Interior of the Sui emperor's field pavilion at night: a carved wooden throne lacquered red and gilded on a three-step dais, a silk folding screen painted with mountains and rivers, red lacquered pillars, yellow silk drapes moving in wind, a large bronze incense burner with rising smoke, silk lanterns giving rich golden light, a red carpet below the dais, a clay sand-table model of a stone fortress on a low table, a large silk map, a sword rack"),
    "LOC_006_hall": ("LOC_006", "LOC_006_interior",
        "Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside"),
    "LOC_008_steppe": ("LOC_008", "LOC_008_steppe_ep1",
        "Open yellow steppe south-east of the Liao River in early spring: dry knee-high yellow grass bending in one direction under constant wind, low rolling grassy hills, drifting yellow dust, a column of black smoke from a burned village far on the horizon, cold pale grey sky, no trees"),
    "LOC_008_hill": ("LOC_008", "LOC_008_steppe_ep1",
        "A low grassy hillside above the open yellow steppe in early spring: dry knee-high yellow grass bending under constant wind, drifting yellow dust, the flat steppe below, cold pale grey sky, no trees"),
    "LOC_010": ("LOC_010", "LOC_010_wide",
        "A frozen dirt road at night between low hills of dark pine forest in the Korean highlands in winter: frost on the ruts, patches of old snow under the pines, bare oak among the pines, a cold blue-grey night sky, no power lines, no buildings, no lights except vehicle headlights"),
}

# ---------------------------------------------------------------- LIGHTING theo bảng ngày/đêm (header script v3)
LIGHT = {
    "D0_night_cheorwon": "Winter night, cold blue-grey darkness, vehicle headlights and hooded red flashlights the only light, breath fogging, frost glittering",
    "D0_night_storm": "Winter night, cold blue-grey darkness cut by dry lightning without rain, sharp white flashes, breath fogging",
    "D1_dawn": "Silver-grey dawn, cold diffused light, thin ground mist, dew beading on armor and grass, wind bending the yellow grass",
    "D1_morning": "Cold grey overcast morning, flat diffused light, constant wind bending the yellow grass, thin drifting yellow dust",
    "D1_noon": "Pale silver noon sun filtering through thin cloud and drifting yellow dust, soft shadows, cold wind",
    "D1_afternoon": "Flat grey afternoon light, long soft shadows, wind bending the yellow grass, yellow dust drifting",
    "D3_afternoon": "Late afternoon, low silver sun slanting through thick drifting yellow dust, warm-grey haze, long shadows",
    "D3_sunset": "Sunset, low amber sun on the horizon backlighting drifting yellow dust, long shadows, cold blue in the shadows",
    "D3_dusk": "Dusk, a last thin band of orange on the western horizon, deep blue shadows, yellow dust settling",
    "D3_night_torch": "Night, warm orange torchlight against deep blue-black darkness, thin moon",
    "D3_night_lantern": "Night interior, warm orange silk-lantern light, deep shadows",
    "D3_night_nvg": "Night, monochrome green night-vision view with grain and faint scan noise, black sky, bright green highlights on warm bodies",
    "D3_night_moon": "Night, thin cold moonlight, deep blue-black shadows, dust drifting",
    "D4_dawn": "Cold blue-hour dawn, thin mist on the ground, dew on metal and grass, first grey light without sun",
    "D4_day": "Grey overcast daylight, flat diffused light, cold wind, yellow dust",
    "D4_night_red": "Night, dim red tactical lamplight on faces and hands, deep black shadows beyond",
    "D4_night_moon": "Night, thin cold moonlight, deep blue-black shadows, faint red lamplight leaking from the base",
    "D4_night_nvg": "Night, monochrome green night-vision view with grain and faint scan noise, bright green highlights on warm bodies",
    "D4_night_fire": "Night, orange firelight and torches against deep blue-black darkness, sparks and smoke, thin moon",
    "D4_night_thermal": "Night, a handheld screen showing a white-hot thermal aerial view, cold blue-white glow on the operator's face",
    "D4_night_torch": "Night, warm orange torchlight against deep blue-black darkness",
    "D4_night_aerial": "Night from high above, tens of thousands of orange campfires on a black plain, thin moonlight",
    "D5_dawn": "Cold grey dawn, flat blue-grey light, thin mist, dew on mud and metal",
    "D5_morning": "Flat silver morning light under a pale grey sky, cold wind, yellow dust",
    "D5_evening_lamp": "Night interior, warm yellow light from clay oil lamps, smoke haze, deep shadows",
    "D5_night_lantern": "Night interior, rich golden silk-lantern light, deep shadows",
    "D5_night_moon": "Night, thin cold moonlight, deep blue-black shadows",
}
WEAR = {  # tình trạng chung lính hiện đại (character_bible §0.3, 1화)
    "D0": "Modern soldiers' uniforms clean and crisp, cold-weather breath fogging.",
    "D1": "Modern soldiers' uniforms clean and crisp, a light film of dew on body armor.",
    "D3": "Modern soldiers' uniforms clean but with fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips.",
    "D4": "Modern soldiers carry fine yellow steppe dust on helmets, shoulders and boots, wind-chapped lips, tired eyes.",
    "D5": "Modern soldiers carry fine yellow dust and dried grey mud on uniforms, wind-chapped lips, dark circles under the eyes.",
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
    """s = authored dict; sc = parsed script entry."""
    sid = s["id"]
    day = s.get("day", "D1")
    chars = s.get("chars", [])
    states = s.get("states", {})       # CHAR → derived id
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
    # characters
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
        seg.append(f"{EXTRAS[e]}." if not EXTRAS[e].endswith(".") else EXTRAS[e])
        if e == "BOY_SCOUT": add_ref("EXTRA_boy_scout_ref")
        if e == "SUI_VANGUARD_GENERAL": add_ref("EXTRA_sui_vanguard_general_ref")
        if e in ("GOG_INFANTRY", "GOG_ARCHERS"): add_ref("WPN_102_ref")
    # vehicles / weapons / equipment
    for v in vehs:
        vref = s.get("veh_ref", {}).get(v, f"{v}_ref")
        seg.append(f"{tag_of(vref)}: {LOCKS[v]}")
        add_ref(vref)
    # props
    for p in props:
        pref = f"{p}_ref" if f"{p}_ref" in REF_DIR else None
        seg.append((f"{tag_of(pref)}: " if pref else "") + LOCKS[p])
        add_ref(pref)
    # setting
    seg.append(f"Setting {tag_of(loc_ref)}: {loc_text}")
    add_ref(loc_ref)
    # action, light, wear
    seg.append("Action: " + s["action"].rstrip(".") + ".")
    light = LIGHT[s["light"]] if s["light"] in LIGHT else s["light"]
    seg.append("Light: " + light.rstrip(".") + ".")
    if any(c in ROK for c in chars) or any(e.startswith("ROK") for e in extras):
        seg.append(WEAR[day])
    if s.get("note_prompt"):
        seg.append(s["note_prompt"].rstrip(".") + ".")
    seg.append(STYLE)
    image_prompt = " ".join(seg)
    # extra refs (props/loc) authored
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
        "narration_ko": sc["nar"], "dialogue_ko": sc["dlg"], "sound": sc["sound"],
        "continuity": s.get("cont", ""),
        "chain_from": s.get("chain"), "cut_half": bool(s.get("cut", False)),
        "aerial_quality": bool(s.get("aerial", False)), "ai_risk": s.get("risk", ""),
        "refs": [] if edit_only else refs,
        "image_body": None if edit_only else {
            "prompt": image_prompt, "model": "nano_banana_pro", "aspect_ratio": "16:9",
            "reference_images": [{"path": ref_path(r), "name": r} for r in refs],
        },
        "video_body": None if (not is_video or edit_only) else {
            "prompt": s["video"], "model": "veo_31_quality" if s.get("aerial") else "veo_31_fast",
            "mode": "start_image", "aspect_ratio": "16:9", "resolution": ["1080p"], "video_length": 8,
            "reference_images": [],  # glabs-operator chèn start_image (ảnh cảnh đã QC hoặc tail-frame chain_from); ≤3 tổng
        },
        "video_ref_candidates": [] if (not is_video or edit_only) else refs[:2],
        "edit_only": edit_only,
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
    L.append("DIALOGUE_KO: " + (" / ".join(r["dialogue_ko"]) if r["dialogue_ko"] else "—"))
    L.append(f"SOUND: {r['sound'] or '—'}")
    L.append(f"CONTINUITY: {r['continuity'] or '—'}")
    L.append(f"CHAIN_FROM: {r['chain_from'] or '—'}")
    L.append(f"CUT_HALF: {'yes' if r['cut_half'] else 'no'}")
    L.append(f"REFS: {', '.join(r['refs']) if r['refs'] else '—'}")
    if r["ai_risk"]:
        L.append(f"AI_RISK: {r['ai_risk']}")
    return "\n".join(L) + "\n"

HEADER = """# 살수 612 — 1화 「요하」 · SCENE LIST (VEO3 / G-Labs) · v1 · 2026-09-16 · veo-prompt-engineer
> Nguồn: `02_script/full_script_ep1.md` v3 (291 SC · 40:00) · `continuity_master.json` (LOCKED) · character/location/vehicle/prop bible · template 04 §C–§H · decisions.md.
> Format §C. Mỗi SC: IMAGE_PROMPT (ảnh keyframe 16:9, nano_banana_pro, ref ≤10) → VIDEO_PROMPT (veo_31_fast, mode start_image, 8 s, 1080p). still_kenburns = chỉ ảnh, ken-burns ở khâu edit.
> **Quy ước prompt:** tag `@<ref_id>` đứng trước lock (ví dụ `@CHAR_001_ref`, `@CHAR_006_facepaint_ep1`, `@LOC_002_detail`) — tag = đúng `name` trong `reference_images` để G-Labs bind chính xác (substring `@CHAR_001` vẫn khớp). VISUAL_LOCK dán NGUYÊN VĂN từ continuity_master.json; derived state = câu trạng thái nguyên văn từ character_bible (ref biến thể ✔ đính thay ref gốc; state không có ref → đính ref gốc). Không tên riêng, không chữ trong ảnh; Hangul trên xe KHÔNG vẽ (decisions #1) — chỉ số Ả Rập; số/HUD/chữ trên màn hình & sổ tay = overlay ở edit.
> **Sub-lock địa điểm:** cảnh nội thất/cận dùng đoạn REF_PROMPT_EN_DETAIL/INTERIOR của bible (nguyên văn) thay vì lock wide; khu vực chưa có trong bible (thảo nguyên D1 + đường nhựa cắt, hõm cỏ D1, khe cạn, bến suối đêm, thảo nguyên dân chạy nạn 1화, đêm 철원 LOC_010) dùng sub-lock cố định trong `logs/scratch/veo-ep1/build.py` — DÙNG NGUYÊN VĂN mọi SC → đề xuất world-designer đưa vào location_bible (proposals).
> **Nhân vật phụ không ID** (소년 척후, 전군총관, 전령, 환관, lính Hàn, bộ binh/cung thủ Goguryeo, trinh sát Tiên Ti, dân chạy nạn): lock tạm cố định (build.py EXTRAS) — mặt lính Hàn phụ luôn quay đi/khuất mũ để né drift.
> **Quy tắc 8 s (§F):** 1 SC = 1 địa điểm, 1 hành động chính, ≤2 người nói, 1 chuyển động camera. `CUT_HALF: yes` = hook 0–30 s + khối trận P4/P5/P10 → edit cắt 2 shot 4 s. Đại quân = aerial wide (⚑ AERIAL/QUALITY → dùng veo_31_quality cho video, nano_banana_pro + upscale 2K cho ảnh).
> **CHAIN_FROM:** chỉ khi SC trước là video8s, cùng địa điểm + nhân vật, hành động nối tiếp → glabs-operator lấy tail-frame làm start_image (tools/glabs_client.py `--chain`). Không chain quá 3 clip liên tiếp (drift).
> **Ánh sáng theo bảng ngày/đêm (header script):** D0 đêm 철원 (SC_013–021) · D1 rạng sáng (022–034) → sáng (001–012) → trưa (035–060) → chiều (061–076) · D3 chiều (078–103) → hoàng hôn (104–129) → đêm (130–144) · D4 bình minh (145–152) → ngày (153–154) → đêm (155–253) · D5 bình minh–sáng (254–274) → tối (275–280) → đêm (281–290). Bụi vàng trên lính từ D3; 백성민 sơn mặt (facepaint_ep1) toàn tập trừ flashback.
> **Style tag (§D, cuối mọi image prompt):** `{style}`
> **Negative (§E, ghi 1 lần — glabs-operator dán vào field negative nếu model hỗ trợ):** `{neg}`
> **QC ảnh §G / QC video §H** áp dụng trước khi tạo video; ảnh fail → regenerate ≤3 lần (đổi seed / đơn giản hoá prompt), vẫn fail → giảm số nhân vật trong khung.

"""

PART_TITLES = {
    1: "[Phần 1] 콜드 오픈 — 「있을 수 없는 아침」 (0:00–1:30) · hook, không narrator 0–30 s",
    2: "[Phần 2] 발견 — 「여기가 어디인가」 (1:30–4:30) · flashback 철원 + phát hiện",
    3: "[Phần 3] 재고 조사 (4:30–7:00) · kiểm kê, drone thấy cầu phao · MID-ROLL 1 @7:00",
    4: "[Phần 4] 첫 접촉 (7:00–10:30) · trận cầu phao [史] + cậu bé trinh sát",
    5: "[Phần 5] 첫 방아쇠 (10:30–14:00) · trận Tiên Ti vs K21 · narrator im 11:54–13:14 · MID-ROLL 2 @14:00",
    6: "[Phần 6] 어느 성의 군사요 (14:00–17:30) · 해모루, năm 612, quyết đi đêm",
    7: "[Phần 7] 쇠집은 문을 못 지난다 (17:30–21:00) · trại Tùy, hành quân đêm, 요동성 · MID-ROLL 3 @21:00",
    8: "[Phần 8] 건전지 나흘 (21:00–24:00) · tài nguyên, lều đỏ, cối đăng ký, tên cắm lưới",
    9: "[Phần 9] 동쪽 길, 하룻밤 (24:00–27:30) · sa bàn, kế 7 điểm, drone lần 1 · MID-ROLL 4 @27:30",
    10: "[Phần 10] 동문 야전 (27:30–34:30) · 6 phase · narrator im 31:30–33:00 · CUT_HALF toàn khối",
    11: "[Phần 11] 쇠는 쇠요 (34:30–37:30) · cái giá, kho lương, tường tây",
    12: "[Phần 12] 그 천둥을 가져오라 (37:30–40:00) · chiếu vua, hành doanh 양제, end card",
}

def validate(recs):
    errs = []
    ids = [r["id"] for r in recs]
    exp = [f"SC_{i:03d}" for i in range(1, 292)]
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
            for tok in ("한승우", "오태민", "Han ", "Tae-min", "Eulji", "Tuoba", "Yang Guang", "Ki-cheol", "Seo-ah", "Tae-oh", "Seong-min", "Hae Mo", "Jeong-su", "Eul-bo", "A-ri"):
                if tok in r["image_prompt"] or tok in r["video_prompt"]: errs.append(f"{r['id']} proper name '{tok}' in prompt")
        if r["chain_from"]:
            prev = recs[ids.index(r["chain_from"])]
            if prev["type"] != "video8s": errs.append(f"{r['id']} chain_from {r['chain_from']} is not video8s")
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
        print("VALIDATION ERRORS:"); print("\n".join(errs));
        if "--force" not in sys.argv: sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    # ---- MD
    md = [HEADER.replace("{style}", STYLE).replace("{neg}", NEGATIVE)]
    nv = sum(1 for r in recs if r["type"] == "video8s"); ns = len(recs) - nv
    md.append(f"**Tổng:** {len(recs)} SC · {nv} video8s · {ns} still_kenburns · {sum(r['seconds'] for r in recs)} s · chain_from: {sum(1 for r in recs if r['chain_from'])} · cut_half: {sum(1 for r in recs if r['cut_half'])} · aerial/quality: {sum(1 for r in recs if r['aerial_quality'])}\n\n---\n")
    cur = None
    for r in recs:
        if r["part"] != cur:
            cur = r["part"]; md.append(f"\n## {PART_TITLES[cur]}\n")
        md.append(md_scene(r, sc[r["id"]]))
    open(f"{OUT_DIR}/scene_list_ep1.md", "w", encoding="utf-8").write("\n".join(md))
    # ---- JSON
    json.dump(recs, open(f"{OUT_DIR}/scenes_ep1.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # ---- copy to output
    os.makedirs(ROOT + "/output/ep1/kich_ban", exist_ok=True)
    open(ROOT + "/output/ep1/kich_ban/scene_list.md", "w", encoding="utf-8").write("\n".join(md))
    # ---- usage
    write_usage(recs)
    print(f"OK {len(recs)} SC · video {nv} · still {ns} · chain {sum(1 for r in recs if r['chain_from'])} · cut_half {sum(1 for r in recs if r['cut_half'])} · aerial {sum(1 for r in recs if r['aerial_quality'])}")

def write_usage(recs):
    cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra = usage_report(recs)
    L = ["# 1화 「요하」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)",
         "> Đếm theo `04_veo/scenes_ep1.json` (291 SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.", ""]
    L.append("## 1. Nhân vật (CHAR) — số SC xuất hiện")
    L.append("| CHAR | SC | Derived state trong 1화 (SC) |"); L.append("|---|---|---|")
    for c, n in sorted(cnt_char.items()):
        sts = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_state.items()) if k.startswith(c))
        L.append(f"| {c} | {n} | {sts or '— (base)'} |")
    L.append(""); L.append("### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)")
    L.append("| Extra | SC |"); L.append("|---|---|")
    for e, n in cnt_extra.most_common(): L.append(f"| {e} | {n} |")
    L.append(""); L.append("## 2. Địa điểm (LOC) — số SC")
    L.append("| LOC | SC | Sub-lock (SC) |"); L.append("|---|---|---|")
    for l, n in sorted(cnt_loc.items()):
        subs = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_sub.items()) if k.startswith(l))
        L.append(f"| {l} | {n} | {subs} |")
    L.append(""); L.append("## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/UAV/EQP) — số SC")
    L.append("| ID | SC |"); L.append("|---|---|")
    for v, n in cnt_veh.most_common(): L.append(f"| {v} | {n} |")
    L.append(""); L.append("## 4. Đạo cụ (PROP) — số SC")
    L.append("| PROP | SC |"); L.append("|---|---|")
    for p, n in cnt_prop.most_common(): L.append(f"| {p} | {n} |")
    L.append(""); L.append("## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)")
    L.append("| # | ref id | thư mục | số SC đính | trạng thái trong ref_jobs.json |"); L.append("|---|---|---|---|---|")
    for i, (r, n) in enumerate(cnt_ref.most_common(), 1):
        status = "**CHƯA CÓ — cần thêm job**" if r in NEW_REFS else "có job"
        L.append(f"| {i} | {r} | {REF_DIR[r]} | {n} | {status} |")
    L.append("")
    L.append("### Ref CHƯA CÓ trong ref_jobs.json (đề xuất world-designer/character-designer thêm; glabs-operator tạo trước lô ảnh cảnh)")
    L.append("- `LOC_003_steppe_d1` (locations, 16:9): thảo nguyên cỏ vàng phẳng D1 + đoạn đường nhựa 50 m bị cắt + đoàn xe không lưới — prompt = sub-lock `LOC_003_steppe` trong build.py + style tag.")
    L.append("- `LOC_003_hollow_d1` (locations, 16:9): hõm cỏ trũng D1, xe dưới lưới, gò cỏ phía đông — sub-lock `LOC_003_hollow`.")
    L.append("- `LOC_003_ford_night` (locations, 16:9): bến suối đá cuội đêm, hai bờ bùn, gò bắc — sub-lock `LOC_003_ford` (trận P10).")
    L.append("- `LOC_008_steppe_ep1` (locations, 16:9): thảo nguyên đông-nam, đoàn dân chạy nạn, khói làng cháy chân trời — sub-lock `LOC_008_steppe` (LOC_008 lock gốc là làng núi xanh 3화 → KHÔNG dùng cho 1화).")
    L.append("- `LOC_010_wide` (locations, 16:9): đêm 철원 đường đất đóng băng giữa đồi thông (P-27 đã DUYỆT, bible chưa có) — sub-lock `LOC_010`.")
    L.append("- `WPN_102_ref` (vehicles, 16:9): bộ binh + cung thủ Goguryeo (giáp lamellar, mũ chỏm ngắn, giáo dài, khiên tròn, cung 맥궁) — dùng cho trận cầu phao P4, 치 cổng đông P10, 500 창병 P10 (hiện chỉ có VEH_101 kỵ giáp ngựa và WPN_101 cung).")
    L.append("- `EXTRA_boy_scout_ref` (characters, 3:4): 소년 척후 ~17 tuổi — xuất hiện 13 SC (P4, P6) → cần ref riêng để không drift.")
    L.append("- `EXTRA_sui_vanguard_general_ref` (characters, 3:4): 수 전군총관 (râu đen-xám, ~55 — PHẢI khác CHAR_202 râu trắng) — 6 SC (P7, P12).")
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
    L.append("### Quy tắc né chung (áp dụng toàn tập)")
    L.append("- **Đám đông cận**: mọi cảnh ≥6 người → wide/aerial hoặc máy sau lưng hàng người, mặt lính phụ quay đi/khuất mũ; chỉ nhân vật có ID mới thấy mặt rõ.")
    L.append("- **Chữ**: màn hình GPS/pin/HUD, sổ tay bút chì, chiếu chỉ, end card → prompt chỉ mô tả 'columns of brush calligraphy / blurred pencil figures / empty dark map screen'; số & chữ thật overlay ở edit (decisions #1, #6).")
    L.append("- **Tay cầm súng**: K2C1 luôn 'muzzle down / slung across chest / resting on a rock'; cận tay chỉ khi tay KHÔNG cầm súng (chạm tên, la bàn, bản đồ); bắn = wide hoặc chớp lửa đầu nòng, không cận ngón tay trên cò.")
    L.append("- **Ngựa + kỵ sĩ số đông**: aerial/tracking thấp, bụi che chi tiết chân ngựa; không cận vó.")
    L.append("- **POV kính đêm / màn hình drone**: mô tả 'monochrome green night-vision view with grain' / 'handheld screen showing…' — không vẽ HUD số; overlay ở edit.")
    L.append("- **Xe + nước/bùn** (SC_224–225, 236–241): 1 hành động vật lý rõ (nước bắn / xích quay / dây căng), máy tĩnh, không nhiều vật thể chuyển động.")
    L.append("- **Hangul trên xe**: KHÔNG vẽ (chỉ số Ả Rập 1/2/3 + 태극기 nhỏ); '천둥' chỉ ở thoại/radio.")
    open(f"{OUT_DIR}/ep1_asset_usage.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
