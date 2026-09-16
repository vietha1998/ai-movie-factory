# -*- coding: utf-8 -*-
"""
VEO scene-list builder — SALSU_612 · 4화 「평양」 (v2.1 · 287 SC)
Đọc: full_script_ep4.md (t / type / narration / thoại / [SOUND] — nguyên văn) + continuity_master.json (VISUAL_LOCK nguyên văn)
      + batch_XX.py (dữ liệu hình ảnh do veo-prompt-engineer biên).
Ghi: 04_veo/scene_list_ep4.md · 04_veo/scenes_ep4.json · 04_veo/ep4_asset_usage.md · output/ep4/kich_ban/scene_list.md
     · 02_script/sublocks_ep4.md · 05_references/extra/ref_jobs_ep4_extra.json
Sao chép từ logs/scratch/veo-ep1/build.py (cùng schema/validator), sửa cho 4화.
"""
import json, re, os, sys, glob, importlib.util, collections

ROOT = "/Users/admin/phim han quoc"
PROJ = ROOT + "/projects/SALSU_612"
SCRIPT = PROJ + "/02_script/full_script_ep4.md"
CM = json.load(open(PROJ + "/continuity_master.json", encoding="utf-8"))
OUT_DIR = PROJ + "/04_veo"
HERE = os.path.dirname(os.path.abspath(__file__))
EP = 4
N_SC = 287

STYLE = CM["style_tag"]
NEGATIVE = ("cartoon, anime, video game render, plastic skin, extra limbs, deformed hands, text, watermark, logo, "
            "modern buildings in historical scene, anachronistic clothing")

# ---------------------------------------------------------------- LOCKS (nguyên văn continuity_master.json)
LOCKS = {}
LOCKS.update(CM["character_locks"]); LOCKS.update(CM["vehicle_locks"]); LOCKS.update(CM["prop_locks"])
LOCKS["PROP_004"] = CM["vehicle_locks"]["EQP_001"]  # placeholder → EQP_001
LOC_LOCK = {k.split("_")[0] + "_" + k.split("_")[1]: v for k, v in CM["location_locks"].items()}
# ID mới chưa có trong continuity_master (decisions 'sau QC 5화': VEH_207) → lock tạm theo mô tả proposals P-50 / vehicle_bible §0.4 — LOCK_PENDING
LOCK_PENDING = {
    "VEH_207": "Sui dynasty cavalry: tall warhorses with high wooden saddles, red silk saddle cloths and bronze-studded breast straps, riders in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmets with red tassel crests, red cloaks, long spears and straight swords, red and yellow pennants",
}
LOCKS.update(LOCK_PENDING)

# ---------------------------------------------------------------- REF SHEET IDS (05_references/*/ref_jobs.json + extra ep1) + refs CẦN TẠO 4화
REF_DIR = {}
for d in ("characters", "locations", "vehicles", "props"):
    for j in json.load(open(f"{PROJ}/05_references/{d}/ref_jobs.json", encoding="utf-8")):
        REF_DIR[j["id"]] = d
for j in json.load(open(f"{PROJ}/05_references/extra/ref_jobs_ep1_extra.json", encoding="utf-8")):
    REF_DIR[j["id"]] = j["out_dir"].split("/")[-1]  # đã DUYỆT (decisions) — coi như có job
NEW_REFS = {  # chưa có job → 05_references/extra/ref_jobs_ep4_extra.json (xem ep4_asset_usage.md §5)
    "LOC_007_island_ep4": "locations", "LOC_007_south_camp_ep4": "locations", "LOC_007_fog_ep4": "locations",
    "LOC_007_marsh_night_ep4": "locations", "LOC_008_hills_rain_ep4": "locations", "LOC_008_sui_tent_ep4": "locations",
    "LOC_008_sui_camp_ep4": "locations", "LOC_006_market_ep4": "locations",
    "VEH_207_ref": "vehicles", "PROP_018_ref": "props",
    "EXTRA_village_women_ref": "characters", "EXTRA_rok_wounded_ref": "characters",
    "EXTRA_gog_envoy_ref": "characters", "EXTRA_sui_courier_ref": "characters",
}
REF_DIR.update(NEW_REFS)

def ref_path(rid):
    return f"projects/SALSU_612/05_references/{REF_DIR[rid]}/{rid}_1.png"

# ---------------------------------------------------------------- DERIVED STATES
# (char, ref đính, câu trạng thái). ✔bible = nguyên văn character_bible; ep4* = trạng thái trong tập do veo-prompt-engineer đặt theo bảng
# "Trạng thái theo tập" 4화 của bible + [ACTION-VI] (đề xuất character-designer nhập bible).
DERIVED = {
    # ---- ✔ bible verbatim (ref riêng)
    "CHAR_001_reeds_ep4": ("CHAR_001", "CHAR_001_reeds_ep4",
        "Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy."),
    "CHAR_002_reeds_ep4": ("CHAR_002", "CHAR_002_reeds_ep4",
        "Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw."),
    "CHAR_004_braid_ep4": ("CHAR_004", "CHAR_004_braid_ep4",
        "Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform."),
    "CHAR_005_captive_ep3": ("CHAR_005", "CHAR_005_captive_ep3",
        "Prisoner: no helmet, no body armor, no boots, torn dirty camo uniform and socks, hands bound behind the back with hemp rope, split lip, bruised swollen left eye, mud on face, frightened but defiant."),
    "CHAR_006_night_raid_ep4": ("CHAR_006", "CHAR_006_night_raid_ep4",
        "No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture."),
    "CHAR_102_wall_night_ep4": ("CHAR_102", "CHAR_102_wall_night_ep4",
        "A heavy black wool cloak over the crimson robe, crown unchanged, standing, face lit warm from one side as if by torchlight, faint mist on the shoulders."),
    "CHAR_103_ambush_ep4": ("CHAR_103", "CHAR_103_ambush_ep4",
        "Blood on the spear blade and right forearm, smoke smudges on face and armor, sweat, one plank of the round shield split, red crest frayed, teeth clenched mid-battle."),
    "CHAR_105_radio_ep3": ("CHAR_105", "CHAR_105_radio_ep3",
        "A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather."),
    "CHAR_107_scarf_ep2": ("CHAR_107", "CHAR_107_scarf_ep2",
        "A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips."),
    "CHAR_107_night_trail_ep4": ("CHAR_107", "CHAR_107_night_trail_ep4",
        "Braids hidden under a dark cloth, mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, carrying a small unlit paper lantern, wet from rain."),
    "CHAR_202_tent_ep4": ("CHAR_202", "CHAR_202_tent_ep4",
        "Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, holding a small silk scroll, face flushed red with anger, lamplight warmth on the beard."),
    "CHAR_204_ambush_ep4": ("CHAR_204", "CHAR_204_ambush_ep4",
        "Blood on the dao blade, smoke smudges, helmet brim dented, cloak scorched at the hem, sweat and panic in the eyes, mid-run."),
    "CHAR_205_nvg_ep3": ("CHAR_205", "CHAR_205_nvg_ep3",
        "A modern night-vision monocular device mounted on the front of the fox-fur cap, an empty black rifle magazine hanging from the belt, rain-darkened leather armor, mud on boots."),
    "CHAR_205_night_hunt_ep4": ("CHAR_205", "CHAR_205_night_hunt_ep4",
        "Night-vision monocular flipped down over the right eye, wet dark cloak over the armor, bow in hand with arrow nocked, mud on the knees, a fresh cut on the right forearm."),
    # ---- bible text-only states (không ref riêng → đính ref gần nhất)
    "CHAR_005_rescued_ep4": ("CHAR_005", "CHAR_005_captive_ep3",
        "Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, straw sandals, no helmet, exhausted relief."),
    "CHAR_101_helmet_off_tent": ("CHAR_101", "CHAR_101_ref",
        "Helmet removed, gray topknot exposed, cloak over shoulders, brush in hand."),
    "CHAR_103_helmet_off": ("CHAR_103", "CHAR_103_ambush_ep4",
        "Helmet removed and held at the side, black topknot loosened, smoke-smudged face, calm."),
    "CHAR_204_landing_ep4": ("CHAR_204", "CHAR_204_ref",
        "River spray on the oiled cloak and helmet, wet beard, confident grin, dao drawn."),
    # ---- ep4 in-episode states (veo-prompt-engineer; theo bible 'Trạng thái theo tập' 4화 + [ACTION-VI])
    "CHAR_003_reeds_ep4": ("CHAR_003", "CHAR_003_rain_ep3",
        "Patrol cap soaked and dripping, week-old salt-and-pepper stubble, only a light smear of mud on the face, torn wet mechanic gloves, uniform soaked and muddy to the thighs."),
    "CHAR_005_cage_ep4": ("CHAR_005", "CHAR_005_captive_ep3",
        "Prisoner in a bamboo cage: no helmet, no body armor, no boots, torn dirty camo uniform, hair hacked short, a ragged bare patch on the right shoulder where the flag patch was torn off, rope marks on the wrists, split lip, bruised swollen left eye, mud on face, right foot bare and swollen dark purple, frightened but defiant."),
    "CHAR_005_helmet_ep4": ("CHAR_005", "CHAR_005_goguryeo_helmet_ep5",
        "Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, right lower leg splinted with reed bundles and bandage, a Goguryeo iron plate helmet of vertical riveted plates without a plume on his head, exhausted relief."),
    "CHAR_006_reeds_ep4": ("CHAR_006", "CHAR_006_ref",
        "Boonie hat soaked and dripping, week-old beard, mud smeared on the face, hemp cord bracelet on the left wrist, uniform soaked and muddy, no face paint."),
    "CHAR_006_mudface_ep4": ("CHAR_006", "CHAR_006_ref",
        "Boonie hat soaked, entire face blackened with wet mud except the eyes, fixed-blade knife held reversed in the right hand, hemp cord bracelet on the left wrist, uniform soaked and muddy."),
    "CHAR_006_raid_hemp_ep4": ("CHAR_006", "CHAR_006_night_raid_ep4",
        "No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. Disguised over the uniform in a coarse undyed hemp Goguryeo jacket with a dark cloth tied over the head, straw sandals."),
    "CHAR_101_rain_ep4": ("CHAR_101", "CHAR_101_salsu_rain_ep5",
        "Full armor and cloak soaked with rain, plume feathers heavy and dripping, mud on the boots, water droplets on the beard, mounted on a dark warhorse in iron lamellar barding."),
    "CHAR_102_hall_ep4": ("CHAR_102", "CHAR_102_wall_night_ep4",
        "A heavy black wool cloak over the crimson robe, crown unchanged, seated on the black lacquered throne, face lit warm from one side by oil lamps."),
    "CHAR_103_rain_ep4": ("CHAR_103", "CHAR_103_ref",
        "Armor and blue jacket dark with rain, water running from the red crest, round shield slung on the back, mud on the boots."),
    "CHAR_103_council_ep4": ("CHAR_103", "CHAR_103_ambush_ep4",
        "Helmet carried under one arm, black topknot loosened, smoke smudges on face and armor, right forearm wrapped in a cloth bandage, no shield, wet armor."),
    "CHAR_106_reeds_ep4": ("CHAR_106", "CHAR_106_ref",
        "Hemp clothes and leather apron soaked with rain, mud on sandals and shins, wet wispy white beard, hands trembling slightly with cold."),
    "CHAR_107_reedcutter_ep4": ("CHAR_107", "CHAR_107_scarf_ep2",
        "Braids hidden under a coarse hemp head cloth, the olive scarf wound around the waist and hidden under the skirt, skirt hitched and tied at the knees, a reed sickle in one hand, a woven basket on the back, scratched bleeding hands, wet from rain."),
    "CHAR_107_fog_trail_ep4": ("CHAR_107", "CHAR_107_night_trail_ep4",
        "Braids hidden under a dark cloth, pale mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, a reed sickle in one hand, wet."),
    "CHAR_202_rain_ep4": ("CHAR_202", "CHAR_202_ref",
        "Armor and breast mirrors streaming with rain, red cloak heavy with water, white beard dripping, mud splashed to the thighs."),
    "CHAR_202_tent_plain_ep4": ("CHAR_202", "CHAR_202_tent_ep4",
        "Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, mud on the breast mirrors, face flushed red with anger, lamplight warmth on the beard."),
    "CHAR_203_rain_ep4": ("CHAR_203", "CHAR_203_ref",
        "Cloak soaked with the fur collar wet and matted, mud on the boots, a bundle of bamboo slip records in one hand, tired eyes."),
    "CHAR_205_bareheaded_ep4": ("CHAR_205", "CHAR_205_night_hunt_ep4",
        "Fox-fur cap lost, braid exposed and dripping, wet dark cloak over the armor, mud to the thighs, a fresh cut on the right forearm, the night-vision monocular held in one hand on its strap."),
    "CHAR_205_bandaged_day_ep4": ("CHAR_205", "CHAR_205_nvg_ep3",
        "A modern night-vision monocular device mounted on the front of a fox-fur cap, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud on boots."),
    "CHAR_205_bandaged_night_ep4": ("CHAR_205", "CHAR_205_night_hunt_ep4",
        "Night-vision monocular flipped down over the right eye, wet dark cloak over the armor, bow in hand with arrow nocked, mud on the knees, the right forearm wrapped in a grey cloth bandage."),
    "CHAR_205_fog_ep4": ("CHAR_205", "CHAR_205_ref",
        "No cap, braid loose and wet, bare feet, leather armor worn without the cloak, the right forearm wrapped in a grey cloth bandage, a modern night-vision monocular hanging from a cord around the neck, fog beading on the face."),
    "CHAR_205_retreat_ep4": ("CHAR_205", "CHAR_205_nvg_ep3",
        "Fox-fur cap on, braid wet, a modern night-vision monocular hanging from a cord on the chest, the right forearm wrapped in a grey cloth bandage, rain-darkened leather armor, wet dark cloak, mud to the thighs."),
}

# ---------------------------------------------------------------- VEHICLE STATES 4화 (câu bổ sung sau lock — không đổi lock)
VEH_STATE = {
    "VEH_001_mud": "Caked in thick wet grey mud and stuck all over with cut reeds so that it looks like a mound of mud, the gun barrel wrapped in reed bundles and lying low, no lights, no antennas visible.",
    "VEH_001_mud_turret": "Caked in thick wet grey mud and stuck all over with cut reeds, mud cracking off the turret ring, reed bundles sliding off the gun barrel, no lights.",
    "VEH_002_captured": "Under a lashed-down cover of dark hides on a heavy wooden ox cart drawn by many oxen, only the boxy shape and one road wheel showing.",
}

# ---------------------------------------------------------------- EXTRAS (không ID trong bible) — lock tạm, dùng NGUYÊN VĂN mọi SC
EXTRAS = {
    "ROK_SOLDIERS": "ROK Army soldiers in soaked mud-smeared granite-pattern digital camo uniforms, helmets wrapped in netting stuck with reed stalks or bare wet heads, faces smeared with mud, week-old stubble, Korean flag patches on right shoulders, faces turned away or hidden under helmet brims",
    "ROK_SOLDIER": "a ROK Army soldier in a soaked mud-smeared granite-pattern digital camo uniform, helmet wrapped in netting stuck with reed stalks, face smeared with mud and turned away or hidden under the helmet brim, Korean flag patch on right shoulder",
    "ROK_SENTRY_NVG": "a ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, a night-vision monocular flipped down over the left eye, a tiny red battery light blinking on it, face mud-smeared and mostly hidden, Korean flag patch on right shoulder",
    "ROK_SENTRY_PLAIN": "a second ROK Army sentry in a soaked mud-smeared granite-pattern digital camo uniform, helmet netted with reed stalks, no night-vision device, face mud-smeared and mostly hidden, Korean flag patch on right shoulder",
    "ROK_RAIDERS_2": "two ROK soldiers disguised in coarse undyed hemp Goguryeo jackets with dark cloths tied over their heads, faces blackened with wet mud except the eyes, straw sandals, bare hands, stooped like old men",
    "ROK_WOUNDED": "a young ROK soldier around 22 with a round face and short black hair, soaked mud-smeared granite-pattern digital camo uniform, Korean flag patch on right shoulder, no helmet, a pressure bandage wrapped around his belly with a cut-short arrow shaft standing from it, face white with sweat",
    "ROK_MORTAR_CREW": "ROK mortar crew in soaked mud-smeared granite-pattern digital camo uniforms and netted helmets, faces down under helmet brims, dropping finned bombs into the tubes",
    "ROK_PZF_GUNNERS": "two ROK soldiers kneeling in the reeds with shoulder-fired anti-tank launchers, faces hidden under netted helmets, a third soldier crouched behind them with a spare launcher tube",
    "ROK_GUNNER_TURRET": "ROK Army tank gunner in granite-pattern digital camo uniform and crew helmet with boom microphone, seen inside a cramped turret lit by a cold blue screen glow, face half in shadow",
    "ROK_RADIOMAN": "young ROK Army radio operator in a soaked mud-smeared granite-pattern digital camo uniform, netted helmet, headset over the helmet, Korean flag patch on right shoulder, face partly hidden by the handset",
    "GOG_INFANTRY": "Goguryeo foot soldiers in iron lamellar armor over brown jackets, iron plate helmets with short plumes, long spears, round wooden shields with iron bosses, black three-legged crow banners on tall poles",
    "GOG_ARCHERS": "Goguryeo archers in iron lamellar armor over brown jackets, iron plate helmets, drawing short composite reflex bows wrapped in dark cherry bark, hip quivers of grey-fletched arrows",
    "GOG_CAVALRYMEN": "Goguryeo cavalrymen in iron lamellar armor with red-plumed iron helmets on horses in iron lamellar barding, four-meter lances, black three-legged crow pennants",
    "GOG_OFFICER": "a Goguryeo officer in iron lamellar armor over a brown jacket, iron plate helmet with a short plume, ring-pommel sword, face wet with rain",
    "GOG_GUARDS": "Goguryeo palace guards in iron lamellar armor holding long spears, faces shadowed under iron helmets",
    "GOG_ENVOY": "Goguryeo envoy around 40, lean build, black topknot under a black silk court cap, dark red-brown silk robe with a black border, no armor, a rolled white cloth flag on a short pole, calm face",
    "GOG_INTERPRETER": "a captured Goguryeo interpreter around 30, thin build, hair loose and tangled, torn brown hemp jacket, hands bound in front with hemp rope, bruised face",
    "GOG_FLAGBEARER": "a mounted Goguryeo flag bearer in iron lamellar armor carrying a tall wet yellow silk banner with a black three-legged crow",
    "VILLAGE_WOMEN": "five middle-aged Goguryeo village women in undyed hemp jackets and pleated skirts hitched and tied at the knees, cloth head wraps, bare feet, carrying woven baskets covered with leaves and reed sickles",
    "VILLAGE_WOMAN_OLD": "an old Goguryeo village woman with a deeply lined face, undyed hemp jacket, cloth head wrap, a woven basket covered with leaves held in both hands",
    "SUI_FEET": "the legs and feet of Sui foot soldiers wading past, torn straw sandals, wet cloth leggings, wooden shield rims dragging in the water, no faces",
    "SUI_SOLDIER_BACK": "a single Sui foot soldier in a wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, straw sandals, seen from behind",
    "SUI_STRAGGLERS": "two Sui stragglers in wet grey-blue padded coats and pointed iron helmets, spears carried reversed, faces turned away",
    "SUI_OFFICER": "a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, straight sword, face weathered and shouting",
    "SUI_OFFICER_MOUNTED": "a Sui officer in mingguang iron lamellar armor with two polished round chest plates, pointed iron helmet with a red tassel, red cloak, on a tall warhorse with a high wooden saddle and red saddle cloth",
    "SUI_MARINES": "Sui marines in wet black lacquered leather lamellar armor with iron chest plates, wide-brimmed iron helmets, round shields and broad dao, faces turned away",
    "SUI_ARCHERS": "hundreds of Sui archers in grey-blue padded coats and pointed iron helmets kneeling in three ranks with drawn bows, seen only as backlit silhouettes",
    "SUI_TORCHBEARERS": "Sui conscript laborers in wet hemp jackets and head cloths wading with burning torches, faces hidden by fire glare",
    "SUI_SENTRY": "a Sui sentry in a wet grey-blue padded coat and pointed iron helmet, spear leaning beside him, face half hidden, dozing",
    "SUI_COURIER": "a Sui mounted courier around 25, mud to the chest, wet grey-blue padded coat and iron lamellar vest, pointed iron helmet, exhausted gasping face",
    "SUI_NAVAL_DEPUTY": "Sui naval deputy commander around 45, thin face with a sparse black beard, dark lacquered leather lamellar armor with iron chest plates, wide-brimmed iron naval helmet, oiled cloak, head bowed",
    "SUI_SOLDIERS_STARVING": "gaunt Sui soldiers in wet grey-blue padded coats and iron helmets, hollow cheeks, sunken eyes, leaning on spears, faces turned away",
    "SUI_SOLDIERS_LOOTING": "Sui soldiers in wet grey-blue padded coats and iron helmets carrying bolts of silk and clay wine jars, faces turned away or hidden under helmets",
    "XIANBEI_RIDERS_FOOT": "Xianbei riders on foot in brown leather lamellar armor over long leather coats, fur-trimmed leather caps, composite bows drawn, wading in a loose double file",
    "XIANBEI_RIDER": "a Xianbei rider in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, composite bow, short curved saber",
    "XIANBEI_DEPUTY": "a Xianbei deputy around 30 in brown leather lamellar armor over a long leather coat, fur-trimmed leather cap, a thin black mustache, listening",
    "XIANBEI_GUARDS_2": "two Xianbei guards in brown leather lamellar armor and fur-trimmed leather caps slumped asleep under a hide awning with bows across their knees",
    "XIANBEI_OFFICER_TORCH": "a Xianbei officer in brown leather lamellar armor and a fur-trimmed leather cap walking behind the ranks with a torch shielded by his hand",
    "DOG": "a lean brown short-haired camp dog",
    "OXEN_CARTS": "two-wheeled wooden ox carts loaded with rope-bound chests, oxen under wooden yokes",
}

# ---------------------------------------------------------------- SUB-LOCATION LOCKS (cố định — dùng nguyên văn mọi SC; xem 02_script/sublocks_ep4.md)
SUBLOC = {
    # key: (loc_id, ref_id or None, text)
    # ===== LOC_007_SALSU
    "LOC_007_aerial": ("LOC_007", "LOC_007_wide",
        "Wide shallow Cheongcheon River eight hundred meters across in July monsoon rain: long wet grey-brown sandbars, a line of wooden ford-marker stakes crossing the shallows, the north bank buried in dense two-meter grey-green reed beds stretching hundreds of meters, the south bank rising into low green hills, brown water, river mist, heavy grey cloud, no trees on the sandbars"),
    "LOC_007_aerial_night": ("LOC_007", "LOC_007_wide",
        "The wide shallow river at night in rain seen from high above: black water with a faint grey sheen, pale sandbars, the vast dark reed beds of the north bank, low black hills on the south bank with a few scattered orange torch points, no moon"),
    "LOC_007_south_hills": ("LOC_007", "LOC_007_wide",
        "From above the south bank of the shallow river in July monsoon rain: low green hills rolling south under low grey cloud, muddy roads fanning out through wet grass and scrub, the wide grey river and its sandbars behind, rain"),
    "LOC_007_reeds_ford": ("LOC_007", "LOC_007_detail",
        "Inside a dense wet reed bed on the north bank right beside the ford crossing, July monsoon: tall grey-green reeds two meters high with pale feathered tops bending under steady rain, brown river water calf-deep between the stalks, grey-brown mud, trampled reeds along the edge of the crossing path, a grey rain-filled sky barely visible through the reed tops"),
    "LOC_007_island1": ("LOC_007", "LOC_007_island_ep4",
        "A low earth mound rising barely a meter above flooded reed beds on the north bank two kilometers from the ford, July monsoon rain: soldiers' shelters of bundled reeds lashed over shallow scrapes, weapons wrapped in cloth, everything grey-brown and wet, and at the center a head-high mound of wet grey mud stuck with cut reeds hiding a tank with only the reed-wrapped gun barrel lying low, tall grey-green reeds walling in every side, no fire, no smoke"),
    "LOC_007_shelter": ("LOC_007", "LOC_007_island_ep4",
        "Under a low roof of bundled wet reeds on the reed island, July monsoon: rain dripping through the reeds, a grey-brown mud floor, cloth-wrapped rifles, a folded olive poncho, tall grey-green reeds walling in the view, cold grey-green light"),
    "LOC_007_island1_k2": ("LOC_007", "LOC_007_island_ep4",
        "Beside the tank on the reed island: a head-high mound of wet grey mud stuck with cut reeds hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked thick on the side skirts, wooden buckets of wet mud, trampled reeds and grey-brown mud underfoot, tall grey-green reeds walling in every side, steady rain"),
    "LOC_007_island_edge": ("LOC_007", "LOC_007_island_ep4",
        "The edge of the reed island on the north bank, July monsoon: a low mud bank sliding into brown water, tall grey-green reeds parting to show the wide grey river, a long wet sandbar and the low green hills of the south bank far beyond, rain on the water"),
    "LOC_007_stake": ("LOC_007", "LOC_007_detail",
        "The water's edge of the reed bed on the north bank in monsoon rain: brown river water lapping a shelf of grey-brown mud, a wooden stake cut with horizontal notches driven into the sandy bottom, tall grey-green reeds behind, the wide grey river and dark hills upstream under heavy black cloud"),
    "LOC_007_reed_path": ("LOC_007", "LOC_007_detail",
        "A narrow path through flooded reed beds on the north bank, July monsoon: brown water thigh-deep between walls of tall grey-green reeds, trampled stalks marking the way, a slot of grey sky above, rain"),
    "LOC_007_sandbar_mid": ("LOC_007", "LOC_007_south_camp_ep4",
        "A wet grey-brown sandbar in the shallow river with tall reeds growing along its edge, and across a narrow channel of brown water the south bank: a Sui rear-guard camp of grey felt and dark hide tents, two-wheeled ox carts loaded with chests, tethered horses, a large willow tree, red and yellow banners hanging wet, steady rain, low green hills behind"),
    "LOC_007_south_camp": ("LOC_007", "LOC_007_south_camp_ep4",
        "The Sui rear-guard camp on the south bank of the shallow river, July monsoon: rows of grey felt and dark hide tents, two-wheeled ox carts loaded with chests, oxen and tethered horses, cooking fires smoking under hide awnings, a large willow tree dripping rain, red and yellow banners hanging wet, the sandy shore and the grey river beyond, low green hills behind"),
    "LOC_007_cage": ("LOC_007", "LOC_007_south_camp_ep4",
        "Under a dripping willow tree at the edge of the Sui rear-guard camp on the south bank: a man-sized cage of bamboo poles lashed with leather thongs under a sagging wet cloth roof, wet sand and mud, grey felt tents and ox carts behind, steady rain"),
    "LOC_007_south_shore": ("LOC_007", "LOC_007_south_camp_ep4",
        "The sandy south shore of the shallow river in front of the Sui rear-guard camp, July monsoon: wet grey sand at the water's edge, the wide grey river and the dark reed beds of the north bank beyond, grey felt tents and ox carts behind, rain"),
    "LOC_007_south_horses": ("LOC_007", "LOC_007_south_camp_ep4",
        "The horse lines at the edge of the Sui rear-guard camp on the south bank at night in rain: short stocky steppe horses tethered to a rope line, wet sand, dark tents and a few guttering torches behind, the black river beyond"),
    "LOC_007_marsh_night": ("LOC_007", "LOC_007_marsh_night_ep4",
        "The flooded reed marsh of the north bank at night in rain: black water thigh-deep, walls of tall grey-green reeds dripping, no torches, no moon, a faint grey sheen on the water surface, rain streaking the darkness"),
    "LOC_007_outpost": ("LOC_007", "LOC_007_marsh_night_ep4",
        "A company outpost at the edge of the flooded reed marsh at night: a shallow scrape in a reed hummock walled with cut reeds, black water thigh-deep all around, cloth-wrapped rifles, a fixed-blade knife stuck in the mud, dripping reeds, rain, no light"),
    "LOC_007_ford_mouth": ("LOC_007", "LOC_007_wide",
        "The sandbar at the mouth of the ford on the south side of the shallow river at night in rain: wet grey sand, brown water on both sides, a line of wooden ford-marker stakes, the dark reed beds of the north bank across the water, torchlight glowing far off to the east"),
    "LOC_007_torch_line": ("LOC_007", "LOC_007_marsh_night_ep4",
        "The flooded reed beds east of the reed island at night in rain: a curving line of hundreds of burning torches carried by men wading thigh-deep through tall grey-green reeds, orange fire reflected in black water, a large war drum on an ox cart, smoke and rain"),
    "LOC_007_channel_south": ("LOC_007", "LOC_007_marsh_night_ep4",
        "A channel of open black water south of the reed island at night in rain, walls of tall reeds on both sides, bundled-reed rafts drifting on the water carrying burning torches, orange fire reflected in the water"),
    "LOC_007_retreat_path": ("LOC_007", "LOC_007_marsh_night_ep4",
        "A flooded reed path upstream from the reed island at night in rain: brown water waist-deep between walls of tall reeds, trampled stalks, no light except the faint grey sheen of the water, rain"),
    "LOC_007_island2": ("LOC_007", "LOC_007_island_ep4",
        "A low sand mound rising barely a meter above flooded reed beds three kilometers upstream on the north bank, July monsoon: taller reeds closing in on every side, soldiers' shelters of bundled wet reeds, a fresh head-high mound of wet grey mud hiding a tank with only the reed-wrapped gun barrel showing and cut reeds not yet fully covering it, grey-brown mud and sand, no fire, no smoke"),
    "LOC_007_island2_k2": ("LOC_007", "LOC_007_island_ep4",
        "Beside the tank on the second reed island: a fresh head-high mound of wet grey mud hiding the hull and turret, the reed-wrapped gun barrel lying low, mud caked on the side skirts, cut reeds leaning against it, trampled reeds and sand underfoot, tall reeds walling in every side, rain"),
    "LOC_007_aid": ("LOC_007", "LOC_007_island_ep4",
        "The aid station on the reed island: a low roof of bundled wet reeds over a bed of cut reeds and a folded olive poncho, an olive medic bag, rain dripping through the reeds, grey-brown mud, tall reeds walling in the view"),
    "LOC_007_sandtable": ("LOC_007", "LOC_007_island_ep4",
        "A patch of smoothed wet mud between reed shelters on the reed island used as a sand table, cut reed stalks and pebbles laid on it, tall grey-green reeds walling in every side, rain"),
    "LOC_007_island1_abandoned": ("LOC_007", "LOC_007_island_ep4",
        "The abandoned reed island by grey morning light in rain: empty reed shelters collapsing, trampled and flattened reeds, an empty sandbagged mortar pit, a deep pair of tank track ruts filled with brown water leading away into the reeds, no fire"),
    "LOC_007_north_ford": ("LOC_007", "LOC_007_detail",
        "The north-bank shore at the upstream ford: tall grey-green reeds parting onto a strip of wet grey sand, a fighting hole scraped into the reed bank, the wide grey river and a low wet sandbar beyond, rain, river mist"),
    "LOC_007_river_fog": ("LOC_007", "LOC_007_fog_ep4",
        "The wide shallow river at dawn buried in dense white fog: only the tops of the tall reeds rising from the whiteness like islands, the water surface a pale mirror fading into white a few meters out, no far bank visible, flat shadowless white light"),
    "LOC_007_reed_path_fog": ("LOC_007", "LOC_007_fog_ep4",
        "A narrow path through flooded reed beds in dense white dawn fog: brown water thigh-deep between walls of tall grey-green reeds beaded with water, the reeds fading into whiteness within a few meters, flat white light"),
    "LOC_007_east_meadow_fog": ("LOC_007", "LOC_007_fog_ep4",
        "A flat grassy meadow on the north bank east of the reed beds in dense white dawn fog: wet green grass, the shapes of horses and riders fading into whiteness, no horizon, flat white light"),
    "LOC_007_channel_fog": ("LOC_007", "LOC_007_fog_ep4",
        "A channel of open brown water between the south shore and the reed beds in dense white dawn fog: waist-deep water, a wall of tall reeds fading into whiteness on one side, wet sand on the other, no far bank visible"),
    "LOC_007_south_sentry_fog": ("LOC_007", "LOC_007_south_camp_ep4",
        "A Sui sentry post at the water's edge of the rear-guard camp in dense white dawn fog: a hide awning on poles, a spear leaning against it, wet sand, grey felt tents fading into whiteness behind"),
    "LOC_007_water_point": ("LOC_007", "LOC_007_south_camp_ep4",
        "The water point of the Sui rear-guard camp on the south bank: a stone-lined pool of river water, a hide awning on poles, a cold ash fire pit, a large tree with a bamboo cage lashed with leather thongs beneath it, wet sand and mud, grey felt tents behind, dense white dawn fog"),
    "LOC_007_camp_fog": ("LOC_007", "LOC_007_south_camp_ep4",
        "Inside the Sui rear-guard camp in dense white dawn fog: grey felt and dark hide tents fading into whiteness, ox carts, tethered horses, wet sand and mud, flat white light"),
    "LOC_007_tent_tuoba": ("LOC_007", "LOC_007_south_camp_ep4",
        "Inside a small felt tent in the Sui rear-guard camp: a leather sleeping pad, a wooden tent pole hung with a bow and quiver, dim grey fog light through the open flap"),
    "LOC_007_camp_east_fog": ("LOC_007", "LOC_007_south_camp_ep4",
        "The east side of the Sui rear-guard camp in dense white dawn fog: grey felt tents, ox carts, a rough wall of red rectangular shields being raised, arrows flying out of the whiteness, wet grass and mud"),
    "LOC_007_sandbar_north_fog": ("LOC_007", "LOC_007_fog_ep4",
        "A low wet sandbar on the north side of the shallow river in thinning dawn fog: grey sand, a wall of tall reeds behind it, a hundred meters of open brown water to the reed beds of the north bank, fog lifting in ribbons"),
    "LOC_007_channel_north_fog": ("LOC_007", "LOC_007_fog_ep4",
        "The channel of brown water between the north sandbar and the reed beds of the north bank in thinning dawn fog: waist-deep water, tall reeds on the north side, fog lifting, rain beginning"),
    "LOC_007_river_surface": ("LOC_007", "LOC_007_detail",
        "Close on the surface of the shallow river in heavy monsoon rain: brown water pocked by dense raindrops, a wooden stake almost submerged, tall reeds leaning with the current, no far bank"),
    # ===== LOC_006_PYONGYANG
    "LOC_006": ("LOC_006", "LOC_006_wide", LOC_LOCK["LOC_006"]),
    "LOC_006_estuary": ("LOC_006", "LOC_006_wide",
        "Grey sea and a wide river mouth in monsoon rain: low grey waves, mist hiding the horizon, flat marshy shores, rain"),
    "LOC_006_warship_bow": ("LOC_006", "VEH_204_ref",
        "The bow deck of a Sui tower warship under way on a wide grey river in rain: wet dark red-brown planking, a carved beast head at the prow, wooden railings, rows of oars rising and falling below, wooden deckhouses behind, grey water and misty banks"),
    "LOC_006_landing": ("LOC_006", "LOC_006_wide",
        "The sandy landing beach on the north bank of the wide grey-green river below the Goguryeo capital in monsoon rain: wet grey sand, flat-bottomed landing boats pulled up, tower warships anchored close in with square brown sails and red banners, willows dripping, the dry-stacked grey granite outer wall of the fortress with a tiled timber gate tower on the slope above, low grey cloud"),
    "LOC_006_gate_tower": ("LOC_006", "LOC_006_wide",
        "On the two-story timber gate tower of the outer wall of the Goguryeo capital in rain: wet dark tiled roof, wooden railing, dry-stacked grey granite wall below, a black three-legged crow banner hanging wet, the sandy riverbank and the grey-green river with warships far below, rain"),
    "LOC_006_gate_yard": ("LOC_006", "LOC_006_wide",
        "The packed-earth yard inside the outer gate of the Goguryeo capital in rain: a wooden stair climbing to the timber gate tower, dry-stacked grey granite walls, wooden houses with rain-dark tiled roofs beyond, puddles, grey light"),
    "LOC_006_market": ("LOC_006", "LOC_006_market_ep4",
        "An empty market street in the outer town of the Goguryeo capital in monsoon rain, 612 AD: wooden houses with rain-dark grey tiled and thatched roofs, wooden market stalls left standing with bolts of silk and clay wine jars, doors open, an abandoned ox cart, a stone-paved street running uphill toward a closed inner-wall gate, puddles, grey wet light"),
    "LOC_006_alley": ("LOC_006", "LOC_006_market_ep4",
        "A narrow alley between two rows of wooden houses in the outer town of the Goguryeo capital in rain: wet stone paving, rain dripping from grey tiled eaves, wooden walls, and at the end of the alley the closed three-bay wooden doors of a temple hall, grey light"),
    "LOC_006_rooftops": ("LOC_006", "LOC_006_market_ep4",
        "Wet grey tiled rooftops of wooden houses on both sides of a narrow stone-paved alley in the outer town of the Goguryeo capital, rain, grey sky"),
    "LOC_006_temple_int": ("LOC_006", "LOC_006_detail",
        "Inside an empty Goguryeo wooden Buddhist temple hall in rain, 612 AD: thick wooden pillars, a dim gilded wooden Buddha statue, bronze incense burner, a bronze bell, scattered offerings, latticed wooden doors closed with only thin lines of grey light through the cracks, deep shadow"),
    "LOC_006_temple_doors": ("LOC_006", "LOC_006_detail",
        "The three-bay wooden doors of an empty Goguryeo temple hall opening onto a rain-soaked market street with abandoned stalls, bolts of silk, clay wine jars and an abandoned ox cart, wooden houses with rain-dark tiled roofs, grey wet light"),
    "LOC_006_water_gate": ("LOC_006", "LOC_006_wide",
        "The water gate of the outer wall of the Goguryeo capital in rain: a stone gate passage through dry-stacked grey granite walls with a timber gate tower above, two-leaf iron-sheathed wooden doors standing open, the stone-paved market street inside, and outside the gate the sandy riverbank sloping down to the wide grey-green river with warships"),
    "LOC_006_river_burning": ("LOC_006", "LOC_006_wide",
        "The wide grey-green river below the Goguryeo capital in rain: flat-bottomed landing boats burning on the water with black smoke mixing into rain, tower warships rowing backward toward midstream with red banners drooping, broken red banners leaning in the wet sand of the beach"),
    "LOC_006_haepo": ("LOC_006", "LOC_006_wide",
        "A grey sea bay in monsoon rain: dozens of tower warships anchored close together with sails furled, low grey waves, mist hiding the horizon, no shore nearby"),
    "LOC_006_hall": ("LOC_006", "LOC_006_interior",
        "Interior of the Goguryeo royal audience hall at Pyongyang at night in monsoon rain, 612 AD: a long timber hall with thick round pillars lacquered deep red, dark wooden floor, a plain black lacquered throne with gold trim on a low two-step dais, a painted silk folding screen behind it, bronze incense burners with rising smoke, clay and bronze oil lamps giving dim warm light, a large black three-legged crow banner on a yellow field hanging behind the throne, latticed wooden doors open onto a rain-soaked stone courtyard and veranda, low tables with a leather map and a rack of composite bows, wet grey-blue light from outside mixing with warm lamplight inside"),
    "LOC_006_hall_corridor": ("LOC_006", "LOC_006_interior",
        "A covered wooden veranda of the palace at the Goguryeo capital at night in monsoon rain: thick round pillars lacquered deep red, dark wooden floor, rain pouring onto a stone courtyard beside it, carved wooden doors opening onto warm oil-lamp light, guards' torches"),
    "LOC_006_river_road_night": ("LOC_006", "LOC_006_wide",
        "A dirt road along the wide grey-green river at night in rain, 612 AD: mud and puddles, willows dripping, the torch-lit walls and gate towers of the Goguryeo capital shrinking in the distance behind, black hills, no other light"),
    # ===== LOC_008_GOGURYEO_VILLAGE (4화 = đồi xanh mưa bắc 평양 / trại Tùy 30리 / đường rút — KHÔNG dùng lock làng núi)
    "LOC_008_hills_rain": ("LOC_008", "LOC_008_hills_rain_ep4",
        "Low green hills north of the Goguryeo capital in July monsoon rain, 612 AD: wet grass and scrub on rolling slopes, a muddy dirt road winding through the valley below churned by countless feet and hooves, low grey cloud on the ridges, mist in the folds, no buildings"),
    "LOC_008_road_column": ("LOC_008", "LOC_008_hills_rain_ep4",
        "A muddy dirt road through low green hills in monsoon rain, 612 AD: mud churned to soup by countless feet, wet grass and scrub on both sides, low grey cloud, an endless column of Sui infantry with wet red and yellow banners filling the road to the horizon"),
    "LOC_008_hilltop": ("LOC_008", "LOC_008_hills_rain_ep4",
        "The crest of a green hill in monsoon rain: wet grass and scrub, low grey cloud, and below in the valley a muddy road filled with an endless column of Sui soldiers under wet red and yellow banners"),
    "LOC_008_hillside_rock": ("LOC_008", "LOC_008_hills_rain_ep4",
        "A wet grey rock on a green hillside in monsoon rain, wet grass, scrub, horses standing with heads down in the rain behind, low grey cloud"),
    "LOC_008_sui_camp_mountain": ("LOC_008", "LOC_008_sui_camp_ep4",
        "A vast Sui camp pitched against the foot of a green forested mountain in monsoon rain, 612 AD: countless grey felt and hemp tents in ragged rows across wet trampled grass and mud, only a few thin threads of cooking smoke, red and yellow banners hanging limp, wooden watchtowers, horse lines, low grey cloud on the mountain"),
    "LOC_008_sui_camp_gate": ("LOC_008", "LOC_008_sui_camp_ep4",
        "The gate of the Sui camp in monsoon rain: a gap in a low earth bank with a wooden barrier, mud churned to soup, rows of grey felt tents beyond, wet red and yellow banners on black lacquered poles, exhausted soldiers leaning on spears"),
    "LOC_008_sui_camp_cook": ("LOC_008", "LOC_008_sui_camp_ep4",
        "A cooking fire in the Sui camp in rain: a clay pot on stones over a smoking fire sheltered by a red rectangular wooden shield, mud, grey felt tents behind"),
    "LOC_008_sui_camp_edge": ("LOC_008", "LOC_008_sui_camp_ep4",
        "The edge of the Sui camp in rain looking out over wet green fields and low hills, grey felt tents behind, an earth bank, mud, low grey cloud"),
    "LOC_008_sui_tent": ("LOC_008", "LOC_008_sui_tent_ep4",
        "Interior of a Sui general's campaign tent pitched on a mountainside in monsoon rain: dark hide walls beaded with water, rain drumming on the roof, a folding wooden camp chair, a low black lacquered table with a leather map painted in ink, a clay oil lamp giving dim warm light, a sword rack, a red and yellow banner, a bronze brazier, mud tracked over reed mats"),
    "LOC_008_sui_tent_door": ("LOC_008", "LOC_008_sui_tent_ep4",
        "The doorway of a Sui general's campaign tent with the hide flap held open: rain falling on a vast camp of grey felt tents on a green mountainside, and far to the south across the rain a low hill with the faint grey line of a fortress wall, low grey cloud"),
    "LOC_008_mud_road_night": ("LOC_008", "LOC_008_hills_rain_ep4",
        "A muddy road through low green hills at night in rain: mud and puddles, wet scrub, a column of Sui soldiers sleeping in the mud along the roadside under wet cloaks, no light except a guttering torch"),
    "LOC_008_gog_camp_hill": ("LOC_008", "LOC_008_hills_rain_ep4",
        "A Goguryeo field camp on a green hill in monsoon rain: hemp tents with wooden poles, a large tent with an awning of oiled cloth, black three-legged crow banners hanging wet, saddled horses in iron lamellar barding waiting in the rain, wet grass, low grey cloud"),
    "LOC_008_gog_tent": ("LOC_008", None,
        "Interior of a Goguryeo commander's field tent at night in rain: oiled hemp walls, rain drumming on the cloth, a low wooden table, a clay oil lamp, a set of iron lamellar armor laid beside the table, a black three-legged crow banner, reed mats"),
    "LOC_008_fields": ("LOC_008", "LOC_008_hills_rain_ep4",
        "Abandoned terraced fields below the Sui camp in monsoon rain: overgrown wet millet plots, mud, low green hills, grey cloud"),
    "LOC_008_road_west": ("LOC_008", "LOC_008_hills_rain_ep4",
        "A muddy road winding west between low green hills in monsoon rain, 612 AD, seen from above: a long train of two-wheeled ox carts, mud, wet scrub, low grey cloud"),
    "LOC_008_square": ("LOC_008", "LOC_008_hills_rain_ep4",
        "A muddy road through low green hills in monsoon rain: an enormous square formation of Sui infantry crawling north along it, four sides of red rectangular shields and long spears, ox carts in the center, wet red and yellow banners, mud churned to soup, low grey cloud"),
    "LOC_008_square_inside": ("LOC_008", "LOC_008_hills_rain_ep4",
        "Inside the marching square of Sui infantry on a muddy road in rain: walls of soldiers with red rectangular shields and spears on every side, ox carts creaking through mud in the center, exhausted men, wet banners, low grey sky"),
    "LOC_008_square_head": ("LOC_008", "LOC_008_hills_rain_ep4",
        "The muddy road at the head of the marching Sui square in rain: churned mud, wet green hills, the front rank of red shields and spears behind, low grey cloud"),
    "LOC_008_knoll": ("LOC_008", "LOC_008_hills_rain_ep4",
        "The top of a green knoll in monsoon rain: wet grass, low grey cloud, and far below in the valley a dark square of tens of thousands of soldiers crawling north along a muddy road"),
    "LOC_008_aerial_north": ("LOC_008", "LOC_008_hills_rain_ep4",
        "From high above in rain: low green hills rolling north under grey cloud, a muddy road, and beyond the last hills a silver band of a wide river, mist"),
}

# ---------------------------------------------------------------- LIGHTING theo bảng ngày/đêm 4화 (header script v2.1) — mưa dầm tháng 7
LIGHT = {
    "dawn_rain": "Flat grey dawn in light steady rain, cold grey-green diffused light, no shadows, water beading on every surface",
    "day_rain": "Grey overcast daylight in steady monsoon rain, flat cold grey-green light, low cloud, rain streaks, every surface wet",
    "day_rain_smoke": "Grey monsoon daylight in steady rain, low cloud, black smoke drifting through the rain, flat cold light",
    "dusk_rain": "Grey wet dusk in rain, dim blue-grey light fading, no fire, no lamps",
    "dusk_rain_stopping": "Grey dusk with the rain just stopped, dim blue-grey light, thin white mist beginning to rise off the water",
    "night_rain": "Night in rain, near-black blue darkness, a faint grey sheen on wet reeds and water, no torches, no moon",
    "night_rain_torch": "Night in rain, warm orange torchlight against blue-black darkness, fire reflected in wet surfaces",
    "night_torchline": "Night in rain, hundreds of distant orange torches reflected in black water, deep blue-black darkness beyond, drum smoke",
    "night_fire": "Night in rain, sudden orange-white fire and explosions lighting wet reeds and water, blue-black darkness beyond",
    "night_nvg": "Monochrome green night-vision view with heavy grain and rain streaks, black sky, pale green highlights on wet reeds and warm bodies",
    "night_nvg_white": "A night-vision view blown out to pure white with grain and faint scan noise, no shapes visible",
    "night_lamp": "Night interior, dim warm oil-lamp light, deep shadows, wet grey-blue rain light leaking in from outside",
    "night_lamp_tent": "Night inside a tent, dim warm oil-lamp light, deep shadows, rain drumming on the roof",
    "night_red": "Night, dim red flashlight light shielded by a hand on faces and hands, deep black shadows beyond",
    "night_screen": "Night inside the turret, cold blue-white glow of a screen on hands and metal, deep black shadows",
    "night_thermal": "Night, a thermal sight view in white-hot monochrome, a dense white-hot mass on a grey background",
    "night_aerial_rain": "Night from high above in rain, black land and grey water, a few scattered orange torch points",
    "dawn_fog": "Dawn in dense white river fog, flat white shadowless light, visibility a few meters, every surface glistening wet, no sun",
    "dawn_fog_thinning": "Dawn with the white river fog thinning into ribbons, flat pale light, light rain beginning",
    "morning_rain": "Grey morning in light rain, flat cold grey-green light, thin mist on the water",
    "afternoon_rain": "Flat grey afternoon light in steady rain, low cloud, wet grey-green tones",
    "evening_lamp_tent": "Evening inside a tent, warm oil-lamp light against grey daylight through the hide flap, rain outside",
    "night_pre_dawn": "The dark before dawn, faint blue-grey light, rain, no lamps",
}
WEAR = "Modern soldiers' uniforms soaked and mud-smeared, faces smeared with mud, week-old uneven stubble, dark circles under the eyes, torn sleeves patched with brown Goguryeo cloth, helmets wrapped in netting stuck with reed stalks or removed."
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

def build_scene(s, sc):
    sid = s["id"]
    day = s.get("day", "D1")
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
        if e in ("GOG_INFANTRY", "GOG_ARCHERS", "GOG_OFFICER"): add_ref("WPN_102_ref")
        if e in ("VILLAGE_WOMEN", "VILLAGE_WOMAN_OLD"): add_ref("EXTRA_village_women_ref")
        if e == "ROK_WOUNDED": add_ref("EXTRA_rok_wounded_ref")
        if e == "GOG_ENVOY": add_ref("EXTRA_gog_envoy_ref")
        if e == "SUI_COURIER": add_ref("EXTRA_sui_courier_ref")
        if e in ("XIANBEI_RIDER", "XIANBEI_RIDERS_FOOT", "XIANBEI_DEPUTY", "XIANBEI_GUARDS_2", "XIANBEI_OFFICER_TORCH") and "VEH_206" not in vehs: add_ref("VEH_206_ref")
        if e in ("SUI_OFFICER", "SUI_OFFICER_MOUNTED", "SUI_SOLDIER_BACK", "SUI_STRAGGLERS", "SUI_ARCHERS", "SUI_SOLDIERS_STARVING", "SUI_SOLDIERS_LOOTING", "SUI_SENTRY") and "WPN_201" not in vehs: add_ref("WPN_201_ref")
    lock_pending = []
    for v in vehs:
        vref = s.get("veh_ref", {}).get(v, f"{v}_ref")
        vst = s.get("veh_state", {}).get(v)
        seg.append(f"{tag_of(vref)}: {LOCKS[v]}" + (f". {VEH_STATE[vst]}" if vst else ""))
        add_ref(vref)
        if v in LOCK_PENDING: lock_pending.append(v)
    for p in props:
        pref = f"{p}_ref" if f"{p}_ref" in REF_DIR else None
        seg.append((f"{tag_of(pref)}: " if pref else "") + LOCKS[p])
        add_ref(pref)
    seg.append(("Setting " + tag_of(loc_ref) + ": " if loc_ref else "Setting: ") + loc_text)
    add_ref(loc_ref)
    seg.append("Action: " + s["action"].rstrip(".") + ".")
    light = LIGHT[s["light"]] if s["light"] in LIGHT else s["light"]
    seg.append("Light: " + light.rstrip(".") + ".")
    if any(c in ROK for c in chars) or any(e.startswith("ROK") for e in extras):
        seg.append(WEAR)
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
        "narration_ko": sc["nar"], "dialogue_ko": sc["dlg"], "sound": sc["sound"],
        "continuity": s.get("cont", ""),
        "chain_from": s.get("chain"), "cut_half": bool(s.get("cut", False)),
        "aerial_quality": bool(s.get("aerial", False)), "ai_risk": s.get("risk", ""),
        "overlay_text": s.get("overlay"),
        "lock_pending": lock_pending,
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
    if r["overlay_text"]:
        L.append(f"OVERLAY (edit): {r['overlay_text']}")
    if r["lock_pending"]:
        L.append(f"LOCK_PENDING: {', '.join(r['lock_pending'])} (lock tạm trong build.py — thay bằng lock continuity_master khi world-designer khóa)")
    if r["ai_risk"]:
        L.append(f"AI_RISK: {r['ai_risk']}")
    if r.get("insert_clip"):
        L.append(f"INSERT_CLIP ({r['insert_clip']['seconds']} s, tách riêng): {r['insert_clip']['prompt']}")
    return "\n".join(L) + "\n"

HEADER = """# 살수 612 — 4화 「평양」 · SCENE LIST (VEO3 / G-Labs) · v1 · 2026-09-16 · veo-prompt-engineer
> Nguồn: `02_script/full_script_ep4.md` v2.1 (287 SC · 40:00 · 239 video8s + 48 still) · `continuity_master.json` (LOCKED) · character/location/vehicle/prop bible · template 04 §C–§H · decisions.md (sau QC 4화 → v2; sau QC 5화: VEH_207) · 04_veo/VEO_BRIEF.md.
> Format §C như 1화. Mỗi SC: IMAGE_PROMPT (ảnh keyframe 16:9, nano_banana_pro, ref ≤10) → VIDEO_PROMPT (veo_31_fast, mode start_image, 8 s, 1080p). still_kenburns = chỉ ảnh, ken-burns ở khâu edit.
> **Quy ước prompt:** tag `@<ref_id>` đứng trước lock (`@CHAR_001_reeds_ep4`, `@CHAR_205_night_hunt_ep4`, `@LOC_007_island_ep4`) — tag = đúng `name` trong `reference_images`. VISUAL_LOCK dán NGUYÊN VĂN từ continuity_master.json; derived state ✔ = câu nguyên văn character_bible (ref biến thể đính thay ref gốc); trạng thái trong tập (`*_ep4` do veo đặt theo bảng "Trạng thái theo tập" 4화) đính ref gần nhất — xem ep4_asset_usage.md §1. Không tên riêng; không chữ trong ảnh: sổ 박기철/sổ 서아/màn hình trưởng xe/bài thơ/end card → `OVERLAY (edit)`; Hangul trên xe KHÔNG vẽ (decisions #1); 태극기 vai PHẢI (P-38).
> **Hai track 4화:** (a) LOC_006_PYONGYANG (cửa biển 패수 → bãi đổ bộ → phố chợ/chùa trống/ngõ → cổng thủy → nội điện 평양 = REF_PROMPT_EN_INTERIOR) + LOC_008 4화 (đồi xanh mưa bắc 평양, trại Tùy 30리 dựa núi, lều 우중문, 방진 đường rút — KHÔNG dùng lock làng núi LOC_008); (b) LOC_007_SALSU (bãi lau sát đường lội → đảo lau 1 → đầm đêm/chốt gác → bờ nam trại hậu quân + cũi → cửa bãi cạn → đảo lau 2 → sương D7 → bãi bắc/cọc). Sub-lock cố định trong `logs/scratch/veo-ep4/build.py` SUBLOC → `02_script/sublocks_ep4.md`.
> **Mưa dầm toàn tập** (tháng 7): mọi Light = mưa/sương; nước tới gối (D1) → đùi (D2–D4) → thắt lưng (D7) → ngực trong lối lau (P10) — ghi trong Action. Lính Hàn: mũ tháo/bọc lưới + lau, mặt bùn, râu 1 tuần, áo vá vải nâu (WEAR §0.3). K2 = mô bùn phủ lau (VEH_STATE `VEH_001_mud`), chỉ 2 phát đêm D4.
> **Quy tắc 8 s (§F):** 1 SC = 1 địa điểm, 1 hành động chính, ≤2 người nói (ngoại lệ SC_128 통역+태오 — 2 beat trong clip, decisions), 1 chuyển động camera. `CUT_HALF: yes` = hook 0–30 s + khối trận/contact (P2 013–015, P3 039–040, P4 053/062–074, P5 076–092, P6 116–117, P7 130–147, P8 162, P9 181, P10 207–245, P11–12 260–261/272) → edit cắt 2 shot 4 s. `2-BEAT` ×12 (SC_001/003 hook · 139/140/143/144 P7 · 209/215/226/231/240/241 P10): beat A/B ghi trong VIDEO_PROMPT; beat là góc máy khác → `INSERT_CLIP` tách riêng (3–4 s). Đại quân = aerial wide (⚑ AERIAL/QUALITY → veo_31_quality; ảnh nano_banana_pro + upscale 2K).
> **CHAIN_FROM:** chỉ khi SC trước là video8s, cùng địa điểm + nhân vật, hành động nối tiếp → glabs-operator lấy tail-frame làm start_image (`--chain`). Không chain quá 3 clip liên tiếp.
> **POV kính đêm** (SC_062/066/131/217): prompt "monochrome green night-vision view", không HUD; SC_217 = trắng lóa. **Màn hình trưởng xe** (SC_143b/144/145/153/279): "cold blue screen with a small blank readout" — số 잔탄 08→07→06 và 위성 0개 = OVERLAY ở edit.
> **LOCK_PENDING:** `VEH_207` (kỵ Tùy trên ngựa — decisions sau QC 5화) chưa có trong continuity_master → lock tạm theo proposals P-50/vehicle_bible §0.4 (build.py LOCK_PENDING); ref `VEH_207_ref` trong ref_jobs_ep4_extra.json. Thay lock nguyên văn khi world-designer khóa.
> **Style tag (§D, cuối mọi image prompt):** `{style}`
> **Negative (§E, ghi 1 lần):** `{neg}`
> **QC ảnh §G / QC video §H** áp dụng trước khi tạo video; ảnh fail → regenerate ≤3 lần (đổi seed / đơn giản hoá prompt), vẫn fail → giảm số nhân vật trong khung.

"""

PART_TITLES = {
    1: "[Phần 1] 콜드 오픈 — 「숨 쉬는 것도 작게」 (0:00–1:30) · hook, không narrator 0–32 s · D1 rạng sáng bãi lau",
    2: "[Phần 2] 발견 — 「하루 일곱 번」 (1:30–4:30) · [史] 7 trận giả thua · hạm đội 내호아 vào 패수 · đảo lau 1 · 아리 cắt lau",
    3: "[Phần 3] 재고 조사 — 「우린 이제 장님입니다」 (4:30–7:00) · sổ 박기철 · lính Tùy lạc hàng · cọc nước · cũi · MID-ROLL 1 @7:00",
    4: "[Phần 4] 첫 접촉 — 「밤눈을 가진 자」 (7:00–10:30) · [史] 내호아 đổ bộ, 고건무 bỏ trống 나곽 · đêm D2 đánh dao trong lau",
    5: "[Phần 5] 빈 절 (10:30–14:00) · [史] 4만 vào 나곽, cửa chùa mở · narrator im 11:20–12:08 · trại 우중문 30리 · MID-ROLL 2 @14:00",
    6: "[Phần 6] 누구의 군대인가 (14:00–17:30) · nội điện 평양 đêm D3 · thư vua → 해모루 → 한승우 · tên dò lau · mâu thuẫn",
    7: "[Phần 7] 북과 횃불 (17:30–21:00) · cũi mồi · 200 đuốc lùa về bãi cạn · cối 20, PZF 3, K2 2 viên · narrator im 19:39–20:11 · MID-ROLL 3 @21:00",
    8: "[Phần 8] 여섯 발, 이게 답니다 (21:00–24:00) · đảo lau 2 · 잔탄 06 · 탁발흠 đếm vỏ đạn · kế cứu 태오",
    9: "[Phần 9] 여수장우중문시 (24:00–27:30) · [史] thơ → 우중문 · 방진 · 해모루 kể thơ · kế sương · 「반이 건널 때까지」 · MID-ROLL 4 @27:30",
    10: "[Phần 10] 안개 속의 칼 (27:30–34:30) · 6 phase · narrator im 31:24–33:00 · CUT_HALF toàn khối",
    11: "[Phần 11] 여울 북쪽 (34:30–37:30) · chết vì nhiễm trùng · 91명 · mũ trụ Goguryeo · 방진 rút · 탁발흠 quỳ",
    12: "[Phần 12] 물은 오르고, 포탄은 여섯 발 (37:30–40:00) · 방진 về bắc · cọc nước · 잔탄 06 · 오태민 một mình · end card",
}

NAMES = ("한승우", "오태민", "Han ", "Tae-min", "Eulji", "Tuoba", "Yang Guang", "Ki-cheol", "Seo-ah", "Tae-oh", "Seong-min",
         "Hae Mo", "Jeong-su", "Eul-bo", "A-ri", "Lai Huer", "Yu Zhongwen", "Yuwen", "Geon-mu", "Yeongyang", "Seung-woo",
         "Zhou Fashang", "Pyongyang", "Salsu", "Cheongcheon")

def validate(recs):
    errs = []
    ids = [r["id"] for r in recs]
    exp = [f"SC_{i:03d}" for i in range(1, N_SC + 1)]
    if ids != exp:
        missing = sorted(set(exp) - set(ids)); extra = sorted(set(ids) - set(exp))
        errs.append(f"ID mismatch: missing={missing[:10]} extra={extra[:10]} n={len(ids)}")
    t = 0
    chain_run = 0
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
            for tok in NAMES:
                if tok in r["image_prompt"] or tok in r["video_prompt"] or (r.get("insert_clip") and tok in r["insert_clip"]["prompt"]):
                    errs.append(f"{r['id']} proper name '{tok}' in prompt")
            if r["type"] == "video8s" and len(r["chars"]) > 3: errs.append(f"{r['id']} >3 named chars in a clip")
        if r["chain_from"]:
            prev = recs[ids.index(r["chain_from"])]
            if prev["type"] != "video8s": errs.append(f"{r['id']} chain_from {r['chain_from']} is not video8s")
            if ids.index(r["chain_from"]) != ids.index(r["id"]) - 1: errs.append(f"{r['id']} chain_from not previous SC")
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
    recs.sort(key=lambda r: r["id"])
    errs = validate(recs)
    if errs:
        print("VALIDATION ERRORS:"); print("\n".join(errs))
        if "--force" not in sys.argv: sys.exit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    md = [HEADER.replace("{style}", STYLE).replace("{neg}", NEGATIVE)]
    nv = sum(1 for r in recs if r["type"] == "video8s"); ns = len(recs) - nv
    md.append(f"**Tổng:** {len(recs)} SC · {nv} video8s · {ns} still_kenburns · {sum(r['seconds'] for r in recs)} s · chain_from: {sum(1 for r in recs if r['chain_from'])} · cut_half: {sum(1 for r in recs if r['cut_half'])} · aerial/quality: {sum(1 for r in recs if r['aerial_quality'])} · insert_clip: {sum(1 for r in recs if r['insert_clip'])} · overlay: {sum(1 for r in recs if r['overlay_text'])} · lock_pending: {sum(1 for r in recs if r['lock_pending'])}\n\n---\n")
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
    print(f"OK {len(recs)} SC · video {nv} · still {ns} · chain {sum(1 for r in recs if r['chain_from'])} · cut_half {sum(1 for r in recs if r['cut_half'])} · aerial {sum(1 for r in recs if r['aerial_quality'])} · insert {sum(1 for r in recs if r['insert_clip'])} · overlay {sum(1 for r in recs if r['overlay_text'])}")

def write_usage(recs):
    cnt_char, cnt_state, cnt_loc, cnt_sub, cnt_veh, cnt_prop, cnt_ref, cnt_extra = usage_report(recs)
    L = ["# 4화 「평양」 — ASSET USAGE & REF PLAN (veo-prompt-engineer · 2026-09-16)",
         "> Đếm theo `04_veo/scenes_ep4.json` (287 SC). Dùng để glabs-operator chạy ref sheet theo ưu tiên và QC biết SC nào rủi ro.", ""]
    L.append("## 1. Nhân vật (CHAR) — số SC xuất hiện")
    L.append("| CHAR | SC | Derived state trong 4화 (SC) |"); L.append("|---|---|---|")
    for c, n in sorted(cnt_char.items()):
        sts = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_state.items()) if k.startswith(c))
        L.append(f"| {c} | {n} | {sts or '— (base)'} |")
    L.append("")
    L.append("### Trạng thái trong tập do veo đặt (không có trong character_bible — đề xuất character-designer nhập DERIVED_STATES; ref đính = ref gần nhất)")
    L.append("| state_id | CHAR | ref đính | câu trạng thái |"); L.append("|---|---|---|---|")
    bible_ids = {"CHAR_001_reeds_ep4", "CHAR_002_reeds_ep4", "CHAR_004_braid_ep4", "CHAR_005_captive_ep3", "CHAR_006_night_raid_ep4", "CHAR_102_wall_night_ep4", "CHAR_103_ambush_ep4", "CHAR_105_radio_ep3", "CHAR_107_scarf_ep2", "CHAR_107_night_trail_ep4", "CHAR_202_tent_ep4", "CHAR_204_ambush_ep4", "CHAR_205_nvg_ep3", "CHAR_205_night_hunt_ep4", "CHAR_005_rescued_ep4", "CHAR_101_helmet_off_tent", "CHAR_103_helmet_off", "CHAR_204_landing_ep4"}
    for k, (c, rid, txt) in DERIVED.items():
        if k not in bible_ids and cnt_state.get(k):
            L.append(f"| {k} | {c} | {rid} | {txt} |")
    L.append(""); L.append("### Nhân vật phụ không ID (lock tạm trong build.py EXTRAS)")
    L.append("| Extra | SC |"); L.append("|---|---|")
    for e, n in cnt_extra.most_common(): L.append(f"| {e} | {n} |")
    L.append(""); L.append("## 2. Địa điểm (LOC) — số SC")
    L.append("| LOC | SC | Sub-lock (SC) |"); L.append("|---|---|---|")
    for l, n in sorted(cnt_loc.items()):
        subs = ", ".join(f"{k} ({v})" for k, v in sorted(cnt_sub.items()) if k.startswith(l))
        L.append(f"| {l} | {n} | {subs} |")
    L.append(""); L.append("## 3. Khí tài / vũ khí / thiết bị (VEH/WPN/EQP) — số SC")
    L.append("| ID | SC | ghi chú |"); L.append("|---|---|---|")
    for v, n in cnt_veh.most_common(): L.append(f"| {v} | {n} | {'**LOCK_PENDING** — lock tạm build.py, cần world-designer khóa continuity_master' if v in LOCK_PENDING else ''} |")
    L.append(""); L.append("## 4. Đạo cụ (PROP) — số SC")
    L.append("| PROP | SC |"); L.append("|---|---|")
    for p, n in cnt_prop.most_common(): L.append(f"| {p} | {n} |")
    L.append(""); L.append("## 5. REF SHEET CẦN TẠO TRƯỚC — ưu tiên theo số SC đính kèm (image reference_images)")
    L.append("| # | ref id | thư mục | số SC đính | trạng thái |"); L.append("|---|---|---|---|---|")
    for i, (r, n) in enumerate(cnt_ref.most_common(), 1):
        status = "**CHƯA CÓ — job trong ref_jobs_ep4_extra.json**" if r in NEW_REFS else "có job"
        L.append(f"| {i} | {r} | {REF_DIR[r]} | {n} | {status} |")
    L.append("")
    L.append("### Ref CHƯA CÓ (job: `05_references/extra/ref_jobs_ep4_extra.json` — glabs-operator tạo trước lô ảnh cảnh)")
    for rid, meta in REF_JOBS_META.items():
        L.append(f"- `{rid}` ({REF_DIR[rid]}, {meta['ar']}): {meta['vi']}")
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
    L.append("## 7. OVERLAY ở edit (chữ/số KHÔNG vẽ trong ảnh)")
    L.append("| SC | overlay |"); L.append("|---|---|")
    for r in recs:
        if r["overlay_text"]: L.append(f"| {r['id']} | {r['overlay_text']} |")
    L.append("")
    L.append("## 8. 2-BEAT / INSERT_CLIP (clip tách riêng 3–4 s, ghép ở edit)")
    L.append("| SC | insert (s) | nội dung insert |"); L.append("|---|---|---|")
    for r in recs:
        if r["insert_clip"]: L.append(f"| {r['id']} | {r['insert_clip']['seconds']} | {r['insert_clip']['prompt'][:160]}… |")
    L.append("")
    L.append("## 9. SC RỦI RO AI & cách né trong prompt")
    risk = [r for r in recs if r["ai_risk"]]
    L.append("| SC | loại rủi ro | cách né (đã áp dụng trong prompt) |"); L.append("|---|---|---|")
    for r in risk: L.append(f"| {r['id']} | {r['ai_risk'].split('→')[0].strip()} | {r['ai_risk'].split('→')[1].strip() if '→' in r['ai_risk'] else '—'} |")
    L.append("")
    L.append("### Quy tắc né chung (áp dụng toàn tập)")
    L.append("- **Người nằm trong lau + chân lính Tùy đi qua** (P1): máy thấp ngang mặt nước, chỉ chân/dép/vạt khiên của địch, không mặt địch; 1 nhân vật có ID trong khung.")
    L.append("- **Đám đông**: mọi cảnh ≥6 người → aerial/wide hoặc máy sau lưng, mặt phụ quay đi/khuất mũ; 4만/30만/방진 = aerial rất cao, không cận.")
    L.append("- **Chữ/số**: sổ tay, màn hình trưởng xe, bài thơ, thẻ tre, end card → prompt 'blurred pencil lines / small blank readout / columns of brush calligraphy'; số & chữ thật OVERLAY ở edit (decisions #1, #6).")
    L.append("- **Tay cầm súng/dao**: K2C1 luôn bọc vải/đặt xuống; dao găm cận chỉ khi tay KHÔNG làm động tác phức tạp; bắn = chớp lửa đầu nòng hoặc wide, không cận ngón tay trên cò (SC_004/007/011 ngoại lệ có chủ ý: 1 bàn tay, chuyển động chậm).")
    L.append("- **Đánh dao dưới nước** (SC_068–070, 231): 'bodies half under brown water, only backs, arms and churned water visible', không vết thương, không máu cận.")
    L.append("- **Ngựa + nước/sương** (P10): tracking thấp, nước bắn che chân ngựa; số ngựa ≤3 khi cận.")
    L.append("- **POV kính đêm**: 'monochrome green night-vision view with grain' — không HUD; SC_217 trắng lóa toàn khung.")
    L.append("- **K2 = mô bùn**: luôn dán VEH_STATE `VEH_001_mud` sau lock; chỉ SC_143–144 tháp pháo lộ khi xoay/bắn.")
    L.append("- **Hangul trên xe**: KHÔNG vẽ; '천둥' chỉ ở thoại/radio.")
    L.append("- **Nhân vật lịch sử**: diện mạo hư cấu theo lock; 주법상/사자/전령/통역 = lock tạm EXTRAS (1–3 SC), không ref trừ 사자/전령.")
    open(f"{OUT_DIR}/ep{EP}_asset_usage.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

REF_JOBS_META = {
    "LOC_007_island_ep4": dict(ar="16:9", vi="đảo lau (đảo 1 & 2): gò đất thấp giữa lau ngập, mái lau bó tạm, K2 = mô bùn cắm lau — sub-lock `LOC_007_island1`/`_island2`/`_shelter`/`_k2`/`_aid`/`_sandtable` (≈100 SC)."),
    "LOC_007_south_camp_ep4": dict(ar="16:9", vi="trại hậu quân Tùy bờ nam: lều da/nỉ, xe bò chở hòm, ngựa buộc, gốc liễu + cũi tre — sub-lock `LOC_007_south_camp`/`_cage`/`_south_shore`/`_water_point`/`_camp_fog`…"),
    "LOC_007_fog_ep4": dict(ar="16:9", vi="sông 살수 rạng đông D7 sương trắng đặc, chỉ ngọn lau nhô — sub-lock `LOC_007_river_fog`/`_reed_path_fog`/`_channel_fog`/`_sandbar_north_fog` (P10)."),
    "LOC_007_marsh_night_ep4": dict(ar="16:9", vi="đầm lau bờ bắc đêm mưa, nước đen tới đùi, không đuốc — sub-lock `LOC_007_marsh_night`/`_outpost`/`_torch_line`/`_channel_south`/`_retreat_path` (P4, P7)."),
    "LOC_008_hills_rain_ep4": dict(ar="16:9", vi="đồi xanh mưa bắc 평양, đường lầy trong thung — sub-lock `LOC_008_hills_rain`/`_road_column`/`_hilltop`/`_square*`/`_knoll` (P2, P5–P7, P9, P11–P12). KHÔNG phải làng núi LOC_008 gốc."),
    "LOC_008_sui_tent_ep4": dict(ar="16:9", vi="nội thất lều 우중문 dựa núi: vách da, ghế gấp, bàn bản đồ da, đèn dầu, giá kiếm — sub-lock `LOC_008_sui_tent`/`_door` (16 SC)."),
    "LOC_008_sui_camp_ep4": dict(ar="16:9", vi="trại Tùy 30리 dựa núi trong mưa, hàng vạn lều, khói bếp thưa — sub-lock `LOC_008_sui_camp_mountain`/`_gate`/`_cook`/`_edge`."),
    "LOC_006_market_ep4": dict(ar="16:9", vi="phố chợ ngoại thành 평양 bỏ trống trong mưa: sạp lụa, vò rượu, xe bò, ngõ hẹp tới cửa chùa — sub-lock `LOC_006_market`/`_alley`/`_rooftops`."),
    "VEH_207_ref": dict(ar="16:9", vi="**LOCK_PENDING** kỵ binh Tùy (tướng/sĩ quan/전령 trên ngựa Hán, yên cao, giáp 명광개) — decisions sau QC 5화; prompt = lock tạm build.py."),
    "PROP_018_ref": dict(ar="16:9", vi="tù và sừng trâu đen có **7 vạch khắc** trên cán (SC_016/124/193/225/226) — chi tiết nhận diện cần ref."),
    "EXTRA_village_women_ref": dict(ar="16:9", vi="5 bà làng bờ bắc (áo gai, khăn đầu, váy buộc gối, rổ đậy lá, liềm) — 9 SC (P2, P10)."),
    "EXTRA_rok_wounded_ep4": dict(ar="3:4", vi="(xem EXTRA_rok_wounded_ref)"),
    "EXTRA_rok_wounded_ref": dict(ar="3:4", vi="부상병 trúng tên bụng (mặt tròn, ~22) — 6 SC (P7, P8, P11) thấy mặt → cần ref để không drift."),
    "EXTRA_gog_envoy_ref": dict(ar="3:4", vi="사자 Goguryeo (áo bào không giáp, cờ trắng cuộn) — 3 SC (P9)."),
    "EXTRA_sui_courier_ref": dict(ar="3:4", vi="전령 Tùy kỵ mã (bùn tới ngực) — 3 SC (P5, P7)."),
}
REF_JOBS_META.pop("EXTRA_rok_wounded_ep4")

def write_sublocks(recs):
    cnt_sub = collections.Counter(r["subloc"] for r in recs)
    sc_by_sub = collections.defaultdict(list)
    for r in recs: sc_by_sub[r["subloc"]].append(r["id"][3:])
    L = ["# 살수 612 — SUB-LOCK ĐỊA ĐIỂM 4화 (veo-prompt-engineer · 2026-09-16 · chờ DUYỆT như 1화)",
         "> Mỗi sub-lock = 1 đoạn VISUAL_LOCK_EN cố định cho một khu vực/buổi của LOC gốc; đã dán NGUYÊN VĂN vào mọi SC tương ứng trong `04_veo/scene_list_ep4.md`. `(bible)` = nguyên văn REF_PROMPT_EN_INTERIOR/VISUAL_LOCK của location_bible; `(bible, cắt pha)` = lock LOC_007 bỏ mệnh đề 3 pha thời tiết (4화 chỉ có mưa/sương). world-designer nhập vào location_bible dưới mục `REF_PROMPT_EN_<subarea>`; 5화 dùng lại đúng id (đảo lau, cọc, bãi bắc, sương). Nguồn máy: `logs/scratch/veo-ep4/build.py` SUBLOC.",
         "> Quy tắc dùng: aerial → `LOC_007_aerial`/`LOC_006`/`LOC_008_hills_rain`; medium/cận → sub-lock khu vực; luôn thêm câu Light (mưa/sương theo bảng ngày/đêm); kết bằng style tag §D. LOC_008 4화 = đồi xanh mưa bắc 평양 (KHÔNG dùng lock làng núi).", "",
         "| # | id sub-lock | LOC gốc | Ref đính | SC 4화 | VISUAL_LOCK_EN (nguyên văn) |", "|---|---|---|---|---|---|"]
    i = 0
    for k, (loc, ref, txt) in SUBLOC.items():
        if not cnt_sub.get(k): continue
        i += 1
        tag = " (bible)" if k in ("LOC_006", "LOC_006_hall") else (" (bible, cắt pha)" if k == "LOC_007_aerial" else " (mới)")
        ids = sc_by_sub[k]
        idtxt = f"{len(ids)} SC: " + ", ".join(ids[:14]) + ("…" if len(ids) > 14 else "")
        L.append(f"| {i} | `{k}`{tag} | {loc} | `{ref or '—'}` | {idtxt} | {txt} |")
    L.append(""); L.append("## Ref mới cần tạo (job: `05_references/extra/ref_jobs_ep4_extra.json`)")
    L.append("| ref id | dùng cho | số SC đính | priority |"); L.append("|---|---|---|---|")
    cnt_ref = collections.Counter(x for r in recs for x in r["refs"])
    for rid in NEW_REFS:
        n = cnt_ref.get(rid, 0)
        L.append(f"| `{rid}` | {REF_JOBS_META[rid]['vi'].split(' — ')[0][:90]} | {n} | {'P1' if n >= 15 else ('P2' if n >= 5 else 'P3')} |")
    L.append(""); L.append("## Ghi chú")
    L.append("- `LOC_007_aerial`: lock gốc LOC_007 chứa 3 pha thời tiết (bình minh xám → mưa → nắng xé mây) là cấu trúc 5화; 4화 dán bản cắt còn pha mưa. 5화 dùng lock gốc + `LOC_007_finale_light`.")
    L.append("- `LOC_007_island1` / `LOC_007_island2`: cùng ref `LOC_007_island_ep4`; khác nhau ở câu 'fresh mound / cut reeds not yet fully covering' — QC ảnh đảo 2 phải thấy mô bùn mới hơn.")
    L.append("- `LOC_007_stake` dùng cho cả cọc đảo lau 1 (D2) và cọc mới bãi bắc (D6–D8) — CONTINUITY từng SC ghi số vạch nước.")
    L.append("- `LOC_008_*` 4화: đồi xanh mưa bắc 평양 / trại Tùy 30리 / lều 우중문 / 방진 — script header khóa 'không cần LOC mới'; đề xuất world-designer thêm REF_PROMPT_EN_HILLS_RAIN + REF_PROMPT_EN_SUI_TENT vào LOC_008 hoặc tách LOC_011 nếu 5화 cần.")
    L.append("- `LOC_008_gog_tent` (lều 을지문덕, 2 SC) không đính ref địa điểm (nội thất lều Goguryeo chưa có ref) — nano_banana_pro theo text + ref nhân vật.")
    L.append("- POV kính đêm (SC_062/066/131) dùng sub-lock đầm/trại + Light `night_nvg`; SC_217 Light `night_nvg_white`.")
    open(f"{PROJ}/02_script/sublocks_ep{EP}.md", "w", encoding="utf-8").write("\n".join(L) + "\n")

def write_ref_jobs(recs):
    cnt_ref = collections.Counter(x for r in recs for x in r["refs"])
    tail_loc = ", no people in frame, no modern structures, " + STYLE
    tail_char = " Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look"
    def sub(k): return SUBLOC[k][2]
    P = {
        "LOC_007_island_ep4": "Wide establishing reference shot, 16:9. " + sub("LOC_007_island1") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_south_camp_ep4": "Wide establishing reference shot, 16:9. " + sub("LOC_007_south_camp") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_007_fog_ep4": "Wide establishing reference shot, 16:9. " + sub("LOC_007_river_fog") + ". " + LIGHT["dawn_fog"] + tail_loc,
        "LOC_007_marsh_night_ep4": "Wide establishing reference shot, 16:9. " + sub("LOC_007_marsh_night") + ". " + LIGHT["night_rain"] + tail_loc,
        "LOC_008_hills_rain_ep4": "Wide establishing reference shot, 16:9. " + sub("LOC_008_hills_rain") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_008_sui_tent_ep4": "Interior reference shot, 16:9. " + sub("LOC_008_sui_tent") + ". " + LIGHT["night_lamp_tent"] + tail_loc,
        "LOC_008_sui_camp_ep4": "Aerial establishing reference shot, 16:9. " + sub("LOC_008_sui_camp_mountain") + ". " + LIGHT["day_rain"] + tail_loc,
        "LOC_006_market_ep4": "Wide establishing reference shot, 16:9. " + sub("LOC_006_market") + ". " + LIGHT["day_rain"] + tail_loc,
        "VEH_207_ref": "Product-style reference photo of a Sui dynasty cavalry officer of 612 AD mounted on his horse, three-quarter view: " + LOCK_PENDING["VEH_207"] + ", the rider holding a long spear upright, pure white background, even studio lighting, " + STYLE,
        "PROP_018_ref": "Product-style reference photo of a Goguryeo signal horn, three-quarter view: " + LOCKS["PROP_018"] + ", seven short parallel notches freshly carved into the horn near the mouthpiece, pure white background, even studio lighting, " + STYLE,
        "EXTRA_village_women_ref": "Group reference sheet on pure white background, 16:9, full-body front view of " + EXTRAS["VILLAGE_WOMEN"] + ", ages 40 to 65, weathered faces, standing in a row." + tail_char,
        "EXTRA_rok_wounded_ref": "Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. A young ROK soldier around 22 with a round face, short black hair, small eyes and a wide mouth, soaked mud-smeared granite-pattern digital camo uniform, body armor, no helmet, Korean flag patch on right shoulder, private's rank. Empty hands in the full-body view." + tail_char,
        "EXTRA_gog_envoy_ref": "Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. " + EXTRAS["GOG_ENVOY"].capitalize() + ". Flag pole held in the left hand in the full-body view." + tail_char,
        "EXTRA_sui_courier_ref": "Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. " + EXTRAS["SUI_COURIER"][2:].capitalize() + ", a bamboo message tube at the belt." + tail_char,
    }
    jobs = []
    for rid in NEW_REFS:
        n = cnt_ref.get(rid, 0)
        jobs.append({"id": rid, "type": "image", "priority": 1 if n >= 15 else (2 if n >= 5 else 3), "sc_count": n,
                     "out_dir": f"05_references/{NEW_REFS[rid]}", "used_by": REF_JOBS_META[rid]["vi"].split(" — ")[0][:120],
                     "lock_pending": rid == "VEH_207_ref",
                     "body": {"prompt": P[rid], "model": "nano_banana_pro", "aspect_ratio": REF_JOBS_META[rid]["ar"]}})
    jobs.sort(key=lambda j: (j["priority"], -j["sc_count"]))
    json.dump(jobs, open(f"{PROJ}/05_references/extra/ref_jobs_ep{EP}_extra.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
