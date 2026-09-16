# 살수 612 — CHARACTER BIBLE (v1 · 2026-09-16)
> **STATUS: LOCKED 2026-09-16** — đổi ngoại hình/trang bị phải qua logs/proposals.md.

> Nguồn sự thật: `02_script/series_foundation.md` §4 (nhân vật), §5 (khí tài), §7 (arc), §8 (ngôn ngữ), §9 (visual). File này KHÔNG mâu thuẫn với foundation; điểm cần đổi/bổ sung ghi ở `logs/proposals.md`.
> Ngôn ngữ: tài liệu tiếng Việt, tên nhân vật tiếng Hàn + romanization; `VISUAL_LOCK_EN` / `REF_SHEET_PROMPT_EN` / `DERIVED_STATES` prompt tiếng Anh.
> Trạng thái: **DRAFT — chờ user duyệt rồi LOCK** (sau lock: không đổi 22 trường; chỉ thêm derived state).

## 0. QUY ƯỚC SỬ DỤNG

### 0.1 Cách dùng trong pipeline
- Mỗi nhân vật có 22 trường (mục J master prompt) + `Trạng thái theo tập` + `Giọng/ngôn ngữ` + 3 khối tiếng Anh.
- **VISUAL_LOCK_EN**: ≤60 từ, không tên riêng, không giống người thật/người nổi tiếng. **Dán nguyên văn** vào mọi image prompt có nhân vật đó (sau tag `@CHAR_xxx`). Không paraphrase.
- **REF_SHEET_PROMPT_EN**: prompt ảnh reference phông trắng (2 view, 3:4). Chạy qua `05_references/characters/ref_jobs.json` → file `CHAR_xxx_ref_1.png`. Ảnh đã QC được đính `reference_images` vào mọi prompt cảnh (tên `@CHAR_xxx_ref_1`).
- **DERIVED_STATES**: biến thể trạng thái (bụi/mưa/máu/mất mũ). Prompt biến thể = REF_SHEET_PROMPT_EN + câu bổ sung chèn ngay trước "Even studio lighting". Dòng có ✔ = cần ref riêng (đã có trong ref_jobs.json). Khi tạo ảnh cảnh, đính ref biến thể đúng tập thay cho ref gốc.
- Không mô tả lại ngoại hình trong VIDEO prompt (đã có trong ảnh start_image).
- Lịch sử thật (CHAR_101/102/103/201/202/203/204): diện mạo **hư cấu** — giữ đúng tuổi, vai trò, quốc gia, trang phục thời đại. Không mô phỏng chân dung/tượng/diễn viên nào.

### 0.2 Bảng nhận diện nhanh (chống AI drift — mỗi người 1 dấu hiệu KHÔNG ai khác có)
| ID | Tên | Tuổi | Dấu hiệu độc nhất | Phân biệt với |
|---|---|---|---|---|
| CHAR_001 | 한승우 Han Seung-woo | 34 | la bàn đeo dây quanh cổ; 3 kim cương (대위) | 002: dáng gầy hơn, mặt dài, không kính bảo hộ |
| CHAR_002 | 오태민 Oh Tae-min | 27 | kính bảo hộ gác trên mũ; tay áo xắn; lông mày rậm thẳng | 001: to con hơn, mặt chữ nhật |
| CHAR_003 | 박기철 Park Ki-cheol | 42 | mũ lưỡi trai (전투모) thay helmet; thái dương muối tiêu; giẻ đỏ ở thắt lưng | duy nhất tóc hoa râm phía hiện đại |
| CHAR_004 | 윤서아 Yoon Seo-ah | 24 | nữ duy nhất phía hiện đại; băng chữ thập đỏ tay trái; nốt ruồi dưới mắt trái | — |
| CHAR_005 | 장태오 Jang Tae-oh | 21 | controller drone trên ngực; mặt búng ra sữa | 006: gầy nhưng cao lêu nghêu, mặt tròn |
| CHAR_006 | 백성민 Baek Seong-min | 30 | mũ 정글모 (boonie) thay helmet; sẹo xẻ lông mày trái; khăn ngụy trang | 005: mặt hẹp góc cạnh |
| CHAR_101 | 을지문덕 Eulji Mundeok | ~55 | râu bạc ngắn; chỏm lông cao đen + 2 lông trắng; ống đựng thư ở thắt lưng | 103/105: tóc bạc, cao gầy |
| CHAR_102 | 영양왕 King Yeongyang | ~50 | 백라관 (mũ lụa trắng viền vàng); râu cằm dài mảnh đen | duy nhất mặc long bào đỏ thẫm |
| CHAR_103 | 고건무 Go Geon-mu | ~40 | chỏm bờm ngựa đỏ ngắn; râu quai nón ngắn; khiên tròn | 101: đen tóc, đậm người |
| CHAR_104 | 고정수 Go Jeong-su | 45 | râu rậm muối tiêu; áo choàng len xám; chùm chìa khóa cổng | 101/103: thấp mập, mũ cầm tay |
| CHAR_105 | 해모루 Hae Mo-ru | 32 | KHÔNG râu; 1 lông trắng trên mũ; tù và; (3화+) máy radio hiện đại trên giáp | duy nhất Goguryeo không râu |
| CHAR_106 | 을보 Eul-bo | 66 | tạp dề da rèn; búa nhỏ ở thắt lưng; mắt trái nheo; râu cằm trắng lưa thưa | — |
| CHAR_107 | 아리 A-ri | 15 | 2 bím tóc buộc chỉ đỏ; váy xếp ly màu đất; (2화+) khăn quân đội olive | — |
| CHAR_201 | 수 양제 Emperor Yang | ~43 | 통천관 đen cao viền vàng; áo vàng thổ + giáp mạ vàng; râu dê dài mảnh | cao nhất phía Tùy, dáng mảnh |
| CHAR_202 | 우중문 Yu Zhongwen | ~65 | 2 gương ngực tròn bóng (명광개); râu trắng dài đến ngực; áo choàng đỏ | 203: to béo, râu dài |
| CHAR_203 | 우문술 Yuwen Shu | ~65 | giáp sẫm không trang trí; râu xám ngắn gọn; thẻ tre trong tay; cổ lông | 202: gầy, xám, áo choàng xám |
| CHAR_204 | 내호아 Lai Huer | ~50 | mũ sắt vành rộng thủy quân; áo choàng dầu; sống mũi dẹt | — |
| CHAR_205 | 탁발흠 Tuoba Qin | 38 | sẹo dài thái dương→hàm trái; 1 bím tóc dày sau lưng; mũ vành lông cáo; (3화+) kính nhìn đêm trên mũ | duy nhất giáp da + cung |

### 0.3 Bảng hao mòn chung — 천둥 중대 (áp dụng mọi CHAR_001–006 trừ khi ghi khác)
| 화 | Mốc thời gian | Trạng thái chung | Palette (foundation §9) |
|---|---|---|---|
| 1화 요하 | 3/612, ngày 1–5 | Quân phục mới, nếp gấp còn; sáng sương bám; cuối tập bụi vàng mịn trên vai/mũ, môi nứt gió. Cạo râu sạch. | xám-vàng bụi, gió, lạnh |
| 2화 요동성 | 4–5/612 | Bụi đá xám + tro đen công thành; mồ hôi vệt thái dương; tay áo xắn; râu 1–2 ngày (nước hạn chế). Đêm hỏa công: bồ hóng. | bụi + lửa đêm |
| 3화 남하 | 6/612, mưa bắt đầu | Áo sẫm nước, bùn tới gối, râu 3–5 ngày, gò má hóp; bắt đầu mang đồ Goguryeo (áo choàng vải thô, dép rơm thay giày hỏng — chỉ 1–2 người). | xanh mưa, xám |
| 4화 평양 | 7/612 đầu, mưa dầm | Ẩn trong lau sậy: mũ bọc lưới + lau, mặt bôi bùn, râu ~1 tuần (사병 cạo dao Goguryeo → không đều), quầng mắt, áo rách vá vải nâu Goguryeo. | xanh mưa, sương sông |
| 5화 살수 | 7/612 ngày quyết định | Mũ đội lại; bùn tới thắt lưng; máu (của người khác) trên ngực/tay; mưa → cuối: nắng xé mây, bùn khô xám. | mưa + lửa + nắng |

Quy tắc: 태극기 trên vai LUÔN nhìn thấy (kể cả rách/bẩn) — đây là identifier series. Râu chỉ mọc từ 2화; không ai để râu dài kiểu Goguryeo.

### 0.4 Khối trang phục chuẩn (tham chiếu — KHÔNG thay VISUAL_LOCK)
- **ROK Army (hiện đại)**: 디지털 화강암 패턴 전투복 (granite digital camo: pixel nâu-khaki-xanh rêu-đen), 신형 방탄복 cùng hoa văn có MOLLE, 방탄헬멧 bọc vải camo (rail + mount kính đêm), **태극기 patch vai phải**, patch đơn vị vai trái (hư cấu: tia sét trắng trên nền đen — không dùng phù hiệu lữ đoàn thật), băng tên Hangul ngực phải, 계급장 giữa ngực, giày chiến đấu sẫm, găng đen. Súng K2C1: thân đen, ốp tay rail + báng màu tan.
- **Goguryeo 612**: 찰갑 lamellar sắt (miếng sắt nhỏ xâu dây da/dây đỏ), 견갑 vai, 상갑 váy đùi; mũ trụ sắt ghép mảnh dọc (종장판주), ống chỏm cắm lông; áo 저고리 dài tới đùi, cổ chéo, viền 선 màu khác; quần 궁고 ống rộng bó cổ chân; giày da/dép rơm; cờ 삼족오 (quạ ba chân) trên nền đỏ-đen; kiếm 환두대도 (chuôi vòng).
- **Tùy (Hán)**: 명광개 (gương ngực tròn bóng), mũ sắt chỏm tua đỏ, áo choàng đỏ; lính thường: giáp lamellar sắt/da, cờ đỏ-vàng. Hoàng đế: 통천관, áo 자황 (vàng thổ).
- **Tiên Ti (탁발)**: giáp da cứng lamellar nâu, áo felt/len đỏ sẫm, mũ vành lông cáo, cung phức hợp, đao chuôi vòng, thắt lưng miếng đồng hoa văn thú; tóc bím 1 bím dày sau lưng (색두).
- **Dân Goguryeo**: vải gai thô không nhuộm / nhuộm chàm-đất; nam 상투 + khăn 건; nữ 저고리 + 주름치마 (váy xếp ly); dép rơm.

---

## 1. NHÂN VẬT HIỆN ĐẠI — 천둥 중대 (THUNDER Company)

### CHAR_001 — 한승우 (Han Seung-woo)
| Trường | Giá trị |
|---|---|
| ID | CHAR_001 |
| Name | 한승우 (Han Seung-woo) |
| Role | 대위 (Captain), 중대장 — chỉ huy đại đội, người ra quyết định cuối |
| Age | 34 |
| Gender | Nam |
| Ethnicity | Hàn Quốc (hiện đại) |
| Skin tone | Vàng nhạt ấm, má rám gió (light warm beige, wind-tanned) |
| Face shape | Oval dài; hốc mắt hơi sâu; gò má cao vừa |
| Eyes | Một mí, đuôi mắt hơi xuôi — điềm tĩnh; đồng tử nâu sẫm; nếp chân chim mờ; quầng mắt nhẹ (thiếu ngủ mãn tính) |
| Nose | Thẳng, sống mũi cao vừa, đầu mũi hơi vuông |
| Jaw | Hàm vuông nhẹ, **cằm có rãnh mờ** |
| Hair style | Húi cua quân đội, hai bên cạo sát, đỉnh ~2 cm; chân tóc chữ M nhẹ |
| Hair color | Đen |
| Body type | Gầy rắn, vai rộng vừa, lưng luôn thẳng |
| Height impression | Cao trung bình–cao (~178 cm). Đứng cạnh 을지문덕 cao hơn nửa đầu; thấp hơn 오태민 một chút |
| Base outfit | 디지털 화강암 전투복 + 방탄복 cùng hoa văn + 방탄헬멧 bọc camo; 태극기 vai phải; patch tia sét vai trái; băng tên 한승우; **계급장 대위 (3 kim cương) giữa ngực**; găng đen |
| Accessories | **La bàn lensatic đeo dây dù quanh cổ** (chiếc la bàn quay loạn đêm xuyên không — ông giữ như bùa); đồng hồ quân đội mặt đen dây nylon tay trái; tổ hợp radio kẹp dây vai trái; túi bản đồ; sổ tay dã chiến |
| Equipment | Radio PRC-999K (EQP_002), ống nhòm, kính nhìn đêm PVS-11K (EQP_001, giữ đến hết), bản đồ giấy Cheorwon (vô dụng — dùng làm ẩn dụ) |
| Weapon | Súng trường K2C1 (WPN_001) — đeo chéo trước ngực; (súng ngắn sĩ quan → proposals) |
| Personality | Điềm tĩnh, ít lời, quan sát trước khi nói; gánh 94 mạng; không hô hào; ra lệnh bằng câu ngắn; mâu thuẫn nội tâm giữa "đưa tất cả về" và "không đứng nhìn dân bị giết" — giải quyết bằng hành động, không độc thoại |
| Relationship | Cấp trên trực tiếp của 오태민 (đối trọng "bắn hay ẩn"); tin 박기철 làm "người nói thật"; bảo vệ 장태오 như em út; cử 백성민 làm tai mắt; **đối tác bị 을지문덕 thử rồi mới tin**; giao tiếp Goguryeo qua 해모루; 고정수 tin ông đầu tiên; 탁발흠 là đối thủ cá nhân; KHÔNG gặp trực tiếp 영양왕 (qua 해모루) |
| Visual identifiers | (1) la bàn dây cổ; (2) 3 kim cương ngực; (3) cằm rãnh mờ; (4) tổ hợp radio vai trái; (5) tư thế đứng thẳng, hai tay chắp sau lưng khi suy nghĩ |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Sạch → cuối tập bụi vàng mịn; cháy thuốc súng nhẹ trên găng phải sau lần nổ súng đầu. Mũ luôn đội. |
| 2화 | Bụi đá + tro; băng nhỏ mu bàn tay trái (mảnh đá công thành); tay áo xắn; râu 1 ngày. |
| 3화 | Mưa: áo sẫm, bùn tới gối, râu 4 ngày, má hóp; **khoác áo choàng vải gai nâu Goguryeo** (고정수 tặng khi rời thành) trùm ngoài áo giáp; mũ đội. |
| 4화 | **Mũ tháo** (bọc lưới để cạnh); tóc bết, râu 1 tuần; bùn bôi mặt ngụy trang; quầng mắt sâu; tay áo phải rách vá vải nâu. |
| 5화 | Mũ đội lại (vỏ ướt); bùn tới thắt lưng; máu người khác quệt ngang ngực giáp; mưa. Cuối tập: nắng, mũ cầm tay, tóc ướt, đứng cạnh K2 hết đạn. |

**Giọng/ngôn ngữ** (foundation §8)
- 다나까체 chuẩn, âm lượng thấp, câu ≤8 어절. Radio: "천둥 지휘, 전 소대 사격 중지." / "천둥 1, 감명도?"
- Với Goguryeo: 하십시오체 kính trọng, gọi 을지문덕 là "장군님", 해모루 là "해 말객". Được gọi: lính → "중대장님"; Goguryeo → "한 대장" (→ proposals xác nhận).
- Câu mẫu: "구십사 명 전원, 살아서 돌아간다. 그게 임무다." / "쏘지 마. 지나가게 둬라."

**VISUAL_LOCK_EN** (59 từ)
> 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 34-year-old Korean man, lean upright build, long oval face, single-lid calm dark eyes with faint crow's feet, straight nose, square jaw with faint chin cleft, black military buzz cut. ROK Army granite-pattern digital camo uniform, matching body armor and covered ballistic helmet, Korean flag patch on right shoulder, captain's three-diamond rank on chest, lensatic compass on cord around neck. Holding a K2C1 assault rifle (black receiver, tan rail handguard) muzzle down in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_001_dusty_ep2 | 2화 P3–P10 | ✔ | Fine yellow-grey stone dust and black soot on helmet, shoulders and cheeks, sweat streaks at the temples, sleeves rolled to the elbow, small field bandage on the back of the left hand, one-day stubble. |
| CHAR_001_rain_cloak_ep3 | 3화 toàn tập | ✔ | Rain-soaked uniform darkened with water, mud caked to the knees, four-day stubble, hollow cheeks, a coarse brown hemp Goguryeo cloak worn over the body armor, helmet on with wet cover. |
| CHAR_001_reeds_ep4 | 4화 P2–P9 | ✔ | Helmet off, wet matted hair, one-week beard, mud smeared across face as camouflage, dark circles under the eyes, right sleeve torn and patched with brown Goguryeo cloth, uniform wet and muddy. |
| CHAR_001_muddy_bloody_ep5 | 5화 P3–P11 | ✔ | Helmet on with soaked cover, mud caked to the waist, someone else's blood smeared across the chest armor and gloves, rain running down the face, exhausted eyes, jaw clenched. |
| CHAR_001_final_ep5 | 5화 P12 | – | Helmet held in one hand, wet hair, mud drying grey on uniform, quiet still face, warm sunlight. |

---

### CHAR_002 — 오태민 (Oh Tae-min)
| Trường | Giá trị |
|---|---|
| ID | CHAR_002 |
| Name | 오태민 (Oh Tae-min) |
| Role | 중위 (First Lieutenant), 부중대장 kiêm 1소대장 — phó đại đội, đối trọng "hỏa lực" |
| Age | 27 |
| Gender | Nam |
| Ethnicity | Hàn Quốc (hiện đại) |
| Skin tone | Rám nắng trung bình (medium warm tan — nắng thao trường) |
| Face shape | Chữ nhật, trán cao, gò má góc cạnh |
| Eyes | Hai mí rõ, mắt to hơi lồi; **lông mày rậm, thẳng, xếch lên** — luôn như sắp gây sự; nâu |
| Nose | Cao, sống mũi có gờ nhẹ (từng va đập) |
| Jaw | Hàm bạnh rõ, cằm nhọn vừa |
| Hair style | Húi cua sát hơn 한승우 (kiểu #2), chân tóc thẳng |
| Hair color | Đen |
| Body type | Vạm vỡ, ngực dày, cổ to, vai rộng (tập gym) |
| Height impression | Cao nhất nhóm sĩ quan (~181 cm); trong khung hình luôn "to" hơn 한승우 |
| Base outfit | Như CHAR_001 nhưng **계급장 중위 (2 kim cương)**; **tay áo xắn tới khuỷu** (phá quy định); mũ có rail, **kính bảo hộ chiến thuật gác trên đỉnh mũ**; quai mũ hay không cài |
| Accessories | Kính bảo hộ trên mũ; dao chiến thuật cán đen trên áo giáp ngực trái; garô cài dây vai; nhiều túi băng đạn hơn bất kỳ ai (mang 8 băng) |
| Equipment | Radio PRC-999K (소대장), PVS-11K, ống nhòm nhỏ |
| Weapon | K2C1 (WPN_001) — luôn trên tay, không đeo lưng |
| Personality | Nóng, tự tin, tin hỏa lực giải quyết tất cả ("30만이든 뭐든 다 쓸어버립니다"); dũng cảm thật; giọng to; học bài học đau: hỏa lực không thay được chiến lược; 4화 gần như nổ súng phá kế 을지문덕 |
| Relationship | Phó của 한승우 — cãi công khai, phục tùng khi lệnh chốt; ma sát ngầm với 백성민 (người thận trọng); 장태오 ngưỡng mộ anh; 해모루 nể sức mạnh nhưng thấy anh "trẻ"; 5화 giữ bờ bắc — nơi 탁발흠 đánh vào |
| Visual identifiers | (1) kính bảo hộ trên mũ; (2) 2 kim cương; (3) tay áo xắn; (4) lông mày rậm thẳng; (5) cầm súng hai tay kể cả khi nói chuyện |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Sạch; sau trận đầu: muội thuốc súng trên hai cẳng tay trần. |
| 2화 | Tro đen, mồ hôi; **tay áo phải cháy xém** (đêm hỏa công, anh lao vào kéo phuy dầu); râu 2 ngày. |
| 3화 | Mưa, bùn; râu 4 ngày; kính bảo hộ vẫn trên mũ, kính mờ nước. |
| 4화 | **Mũ tháo**, tóc ướt; mặt căng, môi nứt chảy máu; bùn ngụy trang; tay áo rách hẳn, cẳng tay bầm. |
| 5화 | Bùn + máu trên hai cẳng tay; **băng quấn bắp tay trái** (tên sượt); **kính bảo hộ mất** (vỡ trong cận chiến) → identifier thay bằng băng tay; mũ đội, quai không cài. |

**Giọng/ngôn ngữ**
- 다나까체 to, dứt khoát; với lính dưới quyền đôi lúc 반말 ngắn ("가!", "엎드려!"). Gọi 한승우 "중대장님", 박기철 "박 상사", 백성민 "백 중사".
- Với Goguryeo: 하십시오체 gượng, hay bỏ kính ngữ khi nóng.
- Câu mẫu: "중대장님, 화력으로 밀면 끝납니다." / "숨으라니요? 우리가 왜 숨습니까?" / (5화) "북안은 제가 맡습니다. 한 명도 못 건넙니다."

**VISUAL_LOCK_EN** (58 từ)
> 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 27-year-old Korean man, tall muscular build, rectangular face, straight thick eyebrows, large double-lid eyes, high nose with slight bridge bump, strong flared jaw, short black buzz cut. ROK Army granite-pattern digital camo uniform, sleeves rolled, matching body armor, ballistic helmet with tactical goggles pushed up on top, Korean flag patch on right shoulder, lieutenant's two-diamond rank on chest. Holding a K2C1 assault rifle (black receiver, tan rail handguard) across the chest with both hands in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_002_soot_ep2 | 2화 P5–P11 | ✔ | Black soot and stone dust on face and armor, sweat streaks, right sleeve scorched at the cuff, forearms smudged with gunpowder residue, two-day stubble, goggles still on the helmet. |
| CHAR_002_reeds_ep4 | 4화 P2–P9 | ✔ | Helmet off, wet short hair, one-week beard, split bleeding lip, mud smeared on face, both sleeves torn off at the elbow, bruised forearms, uniform soaked and muddy, tense jaw. |
| CHAR_002_muddy_bloody_ep5 | 5화 P3–P11 | ✔ | Helmet on with chinstrap hanging loose, goggles missing, blood-soaked field bandage wrapped around the left upper arm, mud and blood on both forearms, rain-soaked uniform, teeth bared. |

---

### CHAR_003 — 박기철 (Park Ki-cheol)
| Trường | Giá trị |
|---|---|
| ID | CHAR_003 |
| Name | 박기철 (Park Ki-cheol) |
| Role | 상사 (Sergeant First Class), 정비반장 — trưởng ban bảo dưỡng, "đồng hồ nhiên liệu" của series |
| Age | 42 |
| Gender | Nam |
| Ethnicity | Hàn Quốc (hiện đại) |
| Skin tone | Rám trung bình, phong sương; dầu mỡ ăn vào nếp da tay |
| Face shape | Tròn–vuông rộng, má đầy, nếp cười sâu hai bên miệng |
| Eyes | Hẹp, một mí, đuôi mắt nheo cười thường trực; nâu sẫm; nhìn thấu người |
| Nose | To, bè, đầu mũi tròn |
| Jaw | Rộng, cằm đôi nhẹ |
| Hair style | Húi cua; **hai bên thái dương muối tiêu** |
| Hair color | Đen pha bạc thái dương |
| Body type | Đậm chắc, bụng hơi to, cánh tay to thợ máy, bàn tay to ngón ngắn |
| Height impression | Thấp hơn trung bình (~170 cm), chắc nịch; thấp nhất nhóm nam hiện đại |
| Base outfit | Quân phục 화강암; **전투모 (mũ lưỡi trai camo) thay helmet** khi ở căn cứ, helmet chỉ khi giao tranh; áo giáp mở khóa ngực; tay áo xắn; **găng thợ máy đen dính dầu**; 태극기 vai phải; 계급장 상사 (3 chevron) |
| Accessories | **Giẻ đỏ nhét thắt lưng**; sổ tay bìa xanh + bút chì trong túi ngực (bảng đếm dầu/đạn — viết tay); đa năng kìm ở thắt lưng; nút bịt tai treo cổ |
| Equipment | Bộ dụng cụ cuộn da, can dầu 20L, que thăm dầu K21, đèn quay tay |
| Weapon | K2C1 (WPN_001) — đeo sau lưng, hiếm khi bắn |
| Personality | Hài khô, nói bằng con số, thực tế đến tàn nhẫn; yêu xe như con; "bố" của đại đội; 3화 bỏ chính xe mình — không khóc, chỉ tháo biển tên xe mang theo |
| Relationship | Cố vấn "nói thật" cho 한승우; cãi vui với 오태민; thương 태오; **kết bạn với 을보 — hai người thợ giao tiếp bằng tay và kim loại, không cần chung ngôn ngữ** (cặp cross-era quan trọng); 을지문덕 hỏi ông về "쇠수레" |
| Visual identifiers | (1) mũ lưỡi trai camo; (2) thái dương bạc; (3) giẻ đỏ thắt lưng; (4) găng dầu; (5) sổ tay xanh + bút chì |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Sạch nhưng găng đã dầu; ống quần dính bùn cỏ. |
| 2화 | Bồ hóng đen (dập lửa xe K21 cháy); lông mày trái cháy xém một nửa; râu muối tiêu 2 ngày. |
| 3화 | Mưa, bùn; **biển kim loại "천둥 3" tháo từ K21 buộc vào ba lô** (identifier từ đây); găng rách. |
| 4화 | Râu muối tiêu 1 tuần; mũ lưỡi trai ướt nhẹp; ít bùn mặt hơn người khác (ở lại với K2). |
| 5화 | Bùn tới hông (đẩy K2 lún); dầu + máu trên cẳng tay; cuối tập ngồi trên thân K2 với sổ tay. |

**Giọng/ngôn ngữ**
- 다나까체 nhưng chậm, ngắt nhịp; hay lặp con số hai lần. Gọi 한승우 "중대장님", lính "야, 태오".
- Với 을보: nửa 반말 nửa cử chỉ ("영감님, 이거. 이거 봐요.").
- Câu mẫu: "연료, 한 통입니다. 딱 한 통." / "여기서 청천강까지 400km. 연료는 전차 한 대 몫뿐입니다." (foundation) / (5화) "여섯 발. 이게 답니다."
- (Đề xuất phương ngữ 경상도 nhẹ → proposals.)

**VISUAL_LOCK_EN** (59 từ)
> 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 42-year-old Korean man, short stocky build, broad round face, narrow single-lid eyes, deep smile lines, wide round nose, heavy jaw, close-cropped black hair with salt-and-pepper temples. ROK Army granite-pattern digital camo uniform, matching patrol cap, body armor open at chest, black mechanic gloves, red shop rag in belt, Korean flag patch on right shoulder, three-chevron sergeant rank on chest. Holding a small green field notebook and pencil in one hand, K2C1 assault rifle slung on his back, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_003_soot_ep2 | 2화 P7–P11 | ✔ | Face and gloves blackened with soot from a vehicle fire, left eyebrow half singed, sweat cutting clean lines through the grime, two-day salt-and-pepper stubble, patrol cap pushed back. |
| CHAR_003_rain_ep3 | 3화 toàn tập | ✔ | Rain-soaked uniform, mud to the knees, torn mechanic gloves, a small painted metal vehicle nameplate tied to his backpack strap, four-day gray stubble, patrol cap dripping. |
| CHAR_003_muddy_ep5 | 5화 P3–P12 | ✔ | Mud caked to the hips, engine oil and blood on both forearms, soaked patrol cap, week-old gray stubble, exhausted but calm face. |
| CHAR_003_helmet_combat | 2화/5화 giao tranh | – | Ballistic helmet with camo cover worn instead of the patrol cap, chinstrap fastened. |

---

### CHAR_004 — 윤서아 (Yoon Seo-ah)
| Trường | Giá trị |
|---|---|
| ID | CHAR_004 |
| Name | 윤서아 (Yoon Seo-ah) |
| Role | 하사 (Staff Sergeant), 의무병 — quân y đại đội; cầu nối với dân Goguryeo |
| Age | 24 |
| Gender | Nữ |
| Ethnicity | Hàn Quốc (hiện đại) |
| Skin tone | Sáng, tông lạnh; má ửng khi lạnh |
| Face shape | Trái xoan nhỏ, cằm thon |
| Eyes | Hai mí mỏng, mắt to sáng, lông mày thẳng mảnh; **nốt ruồi nhỏ dưới đuôi mắt trái** |
| Nose | Nhỏ, thẳng |
| Jaw | Mềm, cằm thon hơi nhọn |
| Hair style | Tóc đen dài **búi thấp chặt** (quy định) dưới mũ; từ 4화 **tết bím kiểu Goguryeo** do 아리 tết, buộc dây gai |
| Hair color | Đen |
| Body type | Nhỏ gọn, dẻo dai, vai hẹp |
| Height impression | Thấp (~162 cm); trong khung hình luôn nhỏ hơn lính nam — dùng làm tỷ lệ cảm xúc |
| Base outfit | Quân phục 화강암 + áo giáp + helmet có **đèn đội đầu** gắn trước; **băng chữ thập đỏ trên nền trắng tay trái**; 태극기 vai phải; 계급장 하사 (1 chevron); găng nitrile trong túi ngực |
| Accessories | Kéo cắt băng cài giáp; 2 garô cài vai; đèn bút; ống nghe trong túi; từ 3화: **túi vải nhỏ đựng thảo dược Goguryeo** buộc thắt lưng + sổ tay vẽ cây thuốc |
| Equipment | **Ba lô quân y lớn màu olive có chữ thập đỏ** (MED_001: kháng sinh/morphine/băng — giảm dần: 2화 hết kháng sinh); túi truyền dịch; nẹp |
| Weapon | K2C1 (WPN_001) đeo chéo, nòng chúc xuống; hầu như không bắn |
| Personality | Kiên định, dịu nhưng không yếu; đếm thuốc như 박기철 đếm dầu; học nhanh; 2화 tự quyết dùng kháng sinh cuối cho thương binh Goguryeo → cãi với 한승우; 5화 cứu 해모루 trong bùn |
| Relationship | "Chị" của 아리 (dạy nhau: thuốc thảo dược ↔ chữ, băng bó); được 을보 tin; 태오 xem như chị; xung đột đạo đức với 한승우 (thuốc cho ai); 해모루 → kính trọng sau 5화; Goguryeo gọi cô là "의녀" |
| Visual identifiers | (1) băng chữ thập đỏ tay trái; (2) ba lô quân y lớn; (3) nốt ruồi dưới mắt trái; (4) đèn đội đầu; (5) dáng nhỏ giữa lính to; (4화+) bím tóc Goguryeo |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Sạch; sau cứu dân: máu trên găng nitrile, vài sợi tóc xổ. |
| 2화 | **Máu khô trên hai tay áo tới khuỷu** (thương binh Goguryeo); mặt tái; búi tóc xổ nửa; mũ tháo trong lều quân y. |
| 3화 | Mưa; mệt; túi thảo dược xuất hiện; giày ngập bùn; tóc vẫn búi. |
| 4화 | **Tóc tết bím kiểu Goguryeo buộc dây gai**; mũ tháo; tay áo xắn, cẳng tay có máu khô; băng chữ thập sờn. |
| 5화 | Quỳ trong bùn bên 해모루: máu tới khuỷu, mưa, bím tóc ướt, băng chữ thập rách một góc; mũ đội (giao tranh bờ bắc). |

**Giọng/ngôn ngữ**
- 다나까체 với đồng đội; **해요체** mềm với dân/아리/thương binh; dứt khoát khi cấp cứu.
- Với Goguryeo: 하십시오체; gọi 해모루 "말객님". Được gọi: "윤 하사", Goguryeo → "의녀".
- Câu mẫu: "항생제, 마지막 한 병입니다. 누구한테 씁니까?" / (với 아리) "이 풀, 이름이 뭐야? 다시 한번." / (5화) "말객님, 눈 뜨세요. 보세요, 저예요."

**VISUAL_LOCK_EN** (59 từ)
> 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 24-year-old Korean woman, petite slim build, small oval face, bright double-lid eyes, small mole under left eye, small straight nose, soft pointed chin, long black hair in tight low bun. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet with headlamp, red cross armband on left arm, olive medical backpack, Korean flag patch on right shoulder. Trauma shears clipped to the armor, K2C1 assault rifle slung muzzle down, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_004_bloody_sleeves_ep2 | 2화 P6–P11 | ✔ | Helmet off, hair bun half undone with loose strands, dried blood on both sleeves up to the elbows and on nitrile gloves, pale tired face, headlamp hanging around the neck. |
| CHAR_004_braid_ep4 | 4화–5화 | ✔ | Helmet off, hair in a single long Goguryeo-style braid tied with hemp cord, sleeves rolled, dried blood on forearms, small cloth herb pouch at belt, worn red cross armband, wet muddy uniform. |
| CHAR_004_muddy_bloody_ep5 | 5화 P4–P11 | ✔ | Helmet on with soaked cover, long braid dripping, blood to the elbows, mud on knees and thighs, red cross armband torn at one corner, rain on face, focused expression. |

---

### CHAR_005 — 장태오 (Jang Tae-oh)
| Trường | Giá trị |
|---|---|
| ID | CHAR_005 |
| Name | 장태오 (Jang Tae-oh) |
| Role | 일병 (Private First Class), 드론 운용병 — "mắt trên trời"; bị bắt 3화 |
| Age | 21 |
| Gender | Nam |
| Ethnicity | Hàn Quốc (hiện đại) |
| Skin tone | Sáng, mịn, trẻ con; má hồng khi lạnh |
| Face shape | Tròn, má phính nhẹ — mặt búng ra sữa |
| Eyes | To, hai mí, hồn nhiên, hay ngước lên trời; nâu nhạt |
| Nose | Nhỏ, hơi hếch |
| Jaw | Mềm, cằm tròn |
| Hair style | Húi cua quy định, gáy cạo |
| Hair color | Đen |
| Body type | Gầy, cao lêu nghêu, vai xuôi, tay dài; khom lưng khi nhìn màn hình |
| Height impression | Cao (~176 cm) nhưng trông nhỏ vì gầy và khom |
| Base outfit | Quân phục 화강암 + áo giáp; helmet **đẩy ra sau gáy**; 태극기 vai phải; 계급장 일병 (2 gạch ngang); kính bảo hộ trong gác trán |
| Accessories | **Máy điều khiển drone (tablet + 2 cần, có tấm che nắng) treo dây ngực**; ăng-ten; **4 pin drone dán băng keo ghi số 1/2/3/4** trên túi giáp (đếm pin nhìn thấy được) |
| Equipment | Drone quadcopter xám sẫm (UAV_001, 4 → 0), **hộp cứng olive đựng drone sau lưng**, dây sạc, PVS-11K (mất 3화) |
| Weapon | K2C1 (WPN_001) đeo lưng vụng về, hay vướng |
| Personality | Trẻ, sợ nhưng có trách nhiệm; hay báo "배터리 ○○퍼센트"; bị bắt → bị 탁발흠 "nghiên cứu" → trưởng thành; 5화 chiến đấu như lính thường |
| Relationship | Em út: 한승우 bảo vệ, 오태민 nạt yêu, 박기철/윤서아 chăm; 백성민 + 아리 cứu; **đối thoại không lời với 탁발흠** qua drone (Tuoba hỏi bằng cử chỉ, cậu không trả lời); 아리 coi là anh |
| Visual identifiers | (1) controller trên ngực; (2) hộp drone lưng; (3) mặt tròn trẻ con; (4) pin dán số; (5) helmet đẩy ra sau |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Sạch; 4 pin; drone #1 rơi — cậu ôm xác drone gãy cánh. |
| 2화 | Tro; 2 pin; hộp drone cháy xém một góc. |
| 3화 | Mưa, bùn; 1 pin; **BỊ BẮT**: tay trói dây gai sau lưng, mũ + áo giáp + giày bị lột, môi rách, mắt trái bầm, chỉ còn áo quân phục rách và tất. |
| 4화 | Tù binh: như 3화 + bẩn hơn, cổ tay trầy dây trói; sau khi được cứu: **áo 저고리 vải gai Goguryeo khoác ngoài quân phục**, dép rơm. |
| 5화 | **Đội mũ trụ sắt Goguryeo** (mũ mình bị lấy) + áo giáp mượn của đồng đội tử trận, K2C1 trên tay — hình ảnh "lính hiện đại đội mũ cổ" (→ proposals). Bùn, mưa. |

**Giọng/ngôn ngữ**
- 다나까체 hồi hộp, hay lặp; báo số. Gọi mọi người bằng cấp bậc + 님. Được gọi "태오야" (박기철/윤서아), "장 일병" (사관).
- Với 탁발흠: im lặng; chỉ nói "모릅니다" (không biết).
- Câu mẫu: "배터리 40퍼센트… 아니, 38입니다." / "끝이 안 보입니다. 다리… 끝이 안 보입니다." / (5화) "제가 봅니다. 제가 눈입니다."

**VISUAL_LOCK_EN** (59 từ)
> 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 21-year-old Korean man, tall thin build, sloping shoulders, round boyish face, large double-lid eyes, small upturned nose, soft round chin, black crew cut. ROK Army granite-pattern digital camo uniform, matching body armor and ballistic helmet pushed back, Korean flag patch on right shoulder, private's two-bar rank, drone ground-control tablet with sunshade on chest harness, hard drone case on back. Both hands resting on the drone controller, a dark gray quadcopter drone on the floor beside his boots, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_005_captive_ep3 | 3화 P10–4화 P8 | ✔ | Prisoner: no helmet, no body armor, no boots, torn dirty camo uniform and socks, hands bound behind the back with hemp rope, split lip, bruised swollen left eye, mud on face, frightened but defiant. |
| CHAR_005_rescued_ep4 | 4화 P9–P12 | – | Rope marks on wrists, coarse hemp Goguryeo jacket worn open over the torn camo uniform, straw sandals, no helmet, exhausted relief. |
| CHAR_005_goguryeo_helmet_ep5 | 5화 | ✔ | Wearing a Goguryeo iron plate helmet instead of a modern one, borrowed body armor, K2C1 rifle held ready, rain-soaked, mud to the knees, bruise fading on the left eye, determined face. |

---

### CHAR_006 — 백성민 (Baek Seong-min)
| Trường | Giá trị |
|---|---|
| ID | CHAR_006 |
| Name | 백성민 (Baek Seong-min) |
| Role | 중사 (Sergeant), 수색분대장 — trưởng tiểu đội trinh sát; liên lạc thực địa với 해모루 |
| Age | 30 |
| Gender | Nam |
| Ethnicity | Hàn Quốc (hiện đại) — con nhà săn núi Gangwon |
| Skin tone | Rám sẫm, phong sương |
| Face shape | Hẹp, dài, gò má sắc, má hóp nhẹ |
| Eyes | Hẹp, dài, một mí, nhìn xa; lông mày thưa; **sẹo nhỏ xẻ lông mày trái** |
| Nose | Thẳng, từng gãy (gờ nhẹ, hơi lệch) |
| Jaw | Nhọn, hàm nhỏ |
| Hair style | Hơi dài hơn quy định (giấu dưới mũ) |
| Hair color | Đen |
| Body type | Gầy dẻo, cơ dài, bước nhẹ không tiếng |
| Height impression | Trung bình (~175 cm); dáng khom nhẹ khi di chuyển, thẳng khi đứng yên |
| Base outfit | Quân phục 화강암; **정글모 (boonie hat) camo thay helmet** khi trinh sát; áo giáp; **khăn lưới ngụy trang** quấn vai; miếng đệm gối; 태극기 vai phải; 계급장 중사 (2 chevron); **sơn mặt xanh-đen** khi đi trinh sát (không có trên ref gốc) |
| Accessories | Ống nhòm trước ngực; dao lưỡi cố định trên giáp; máy đo xa; (4화+) **vòng dây gai ở cổ tay** do 아리 tết — dấu hiệu dẫn đường |
| Equipment | PRC-999K cầm tay, **PVS-11K (giữ đến cuối — 1 trong số ít còn lại sau 3화)**, bản đồ vẽ tay, dây thừng |
| Weapon | K2C1 (WPN_001) gắn **kính ngắm phóng đại**; dao |
| Personality | Nói ít, mắt "đọc" đất; bình tĩnh tuyệt đối; kính trọng rừng núi; 을지문덕 để ý anh đầu tiên; 4화 cứu 태오 bằng sương + dao + đường mòn; 5화 dẫn kỵ binh Goguryeo qua bãi cạn |
| Relationship | **Bạn thực địa với 해모루** — hai trinh sát hiểu nhau không cần nhiều lời; dẫn 아리 và được 아리 dẫn; cứu 태오; ma sát nhẹ với 오태민; 한승우 tin anh tuyệt đối |
| Visual identifiers | (1) boonie hat; (2) sẹo lông mày trái; (3) khăn lưới ngụy trang; (4) súng có kính ngắm; (5) sơn mặt khi trinh sát |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Sạch, sơn mặt xanh-đen 2 vệt; cỏ khô găm khăn ngụy trang. |
| 2화 | Bụi, sơn mặt trôi loang; râu 2 ngày. |
| 3화 | Mưa; bùn toàn thân (bò trinh sát); râu 5 ngày; mũ boonie ướt sũng vành cụp. |
| 4화 | **Đêm cứu 태오**: không mũ, tóc ướt, mặt bôi bùn đen hoàn toàn chỉ hở mắt, dao trên tay, vòng dây gai cổ tay. |
| 5화 | **Trên lưng ngựa Goguryeo** (yên da, bàn đạp sắt) dẫn kỵ binh qua bãi cạn — boonie hat, khăn ngụy trang, K2C1 đeo chéo; nước tới bụng ngựa (→ proposals). |

**Giọng/ngôn ngữ**
- 다나까체 tối giản, kiểu điện tín: danh từ + số + thời gian. Gọi 해모루 "말객님" rồi từ 3화 chỉ "해모루" (được phép). Được gọi "백 중사".
- Câu mẫu: "발자국. 기병 스물. 두 시간 전." / "안개 걷히기 전에 갑니다. 셋만." / (với 해모루) "저쪽. 바람이 바뀌었소… 아니, 바뀌었습니다."

**VISUAL_LOCK_EN** (58 từ)
> 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 30-year-old Korean man, lean wiry build, narrow long face, sharp cheekbones, narrow single-lid eyes, small scar splitting left eyebrow, straight nose with old break, pointed jaw, black hair slightly over regulation. ROK Army granite-pattern digital camo uniform and matching boonie hat, body armor, camouflage scrim scarf on shoulders, Korean flag patch on right shoulder, staff sergeant two-chevron rank. Clean face without paint. Holding a K2C1 assault rifle with magnified optic muzzle down, binoculars on chest, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_006_facepaint_ep1 | 1화–2화 trinh sát | ✔ | Two diagonal streaks of green and black camouflage face paint across cheeks and forehead, dry yellow grass stalks tucked into the scrim scarf, fine dust on the hat brim. |
| CHAR_006_night_raid_ep4 | 4화 P8–P9 | ✔ | No hat, wet hair plastered down, entire face blackened with mud camouflage except the eyes, fixed-blade knife in right hand, hemp cord bracelet on left wrist, soaked uniform, crouched posture. |
| CHAR_006_horseback_ep5 | 5화 P9–P11 | ✔ | Mounted on a Goguryeo warhorse with leather saddle and iron stirrups, boonie hat soaked, scrim scarf, K2C1 rifle slung across the chest, mud and river water to the boots, rain. |

---

## 2. GOGURYEO (고구려)

### CHAR_101 — 을지문덕 (Eulji Mundeok)
| Trường | Giá trị |
|---|---|
| ID | CHAR_101 |
| Name | 을지문덕 (Eulji Mundeok) — nhân vật lịch sử thật; diện mạo HƯ CẤU |
| Role | 대장군 — tổng chỉ huy chiến trường Goguryeo; chủ nhân kế Salsu |
| Age | ~55 |
| Gender | Nam |
| Ethnicity | Goguryeo (Hàn cổ) |
| Skin tone | Ô-liu rám phong sương, nếp nắng |
| Face shape | Chữ nhật dài, trán cao, thái dương lõm, gò má nổi |
| Eyes | Hẹp, mí sụp nhẹ, **sắc như dao**; đen; lông mày dày đang bạc |
| Nose | Sống mũi cao, dài, thẳng |
| Jaw | Mạnh; **râu bạc cắt ngắn (2–3 cm) + ria** — bạc đều |
| Hair style | Dài, búi 상투 dưới mũ trụ; vài sợi bạc lòa xòa thái dương |
| Hair color | Bạc xám pha vệt đen |
| Body type | Cao so với thời đại, gầy, thẳng, gân guốc; cử động chậm, có chủ ý |
| Height impression | ~172 cm — cạnh 한승우 thấp hơn nửa đầu nhưng "chiếm khung hình" nhờ tư thế |
| Base outfit | 저고리 dài màu **đỏ nâu sẫm** viền 선 đen, quần 궁고 ống rộng bó cổ chân, giày da; ngoài: **찰갑 sắt xâu dây đỏ** đủ bộ (견갑 vai + 상갑 đùi); **mũ trụ sắt ghép mảnh dọc, ống chỏm cắm lông đen cao + 2 lông trắng dài**; áo choàng đen khi ở ngoài |
| Accessories | Khóa thắt lưng đồng hình 삼족오; **ống da đựng thư/thơ ở thắt lưng** (bài thơ gửi 우중문 — 4화); nhẫn sắt |
| Equipment | Ngựa (bay sẫm), bản đồ lụa vẽ sông; ở triều: 조우관 (mũ lông chim) thay mũ trụ |
| Weapon | 환두대도 (kiếm dài chuôi vòng mạ vàng) — hiếm rút; cung trên yên |
| Personality | Lạnh, kiên nhẫn, mỉa ngầm; thử người trước khi tin; coi đại đội là MỘT quân cờ ("cái nút chai"); không kinh ngạc trước công nghệ — hỏi ngay giới hạn của nó ("쇠수레는 며칠이나 달릴 수 있소?"); quyết định lớn không giải thích |
| Relationship | Phục vụ 영양왕 (kính nhưng giữ ý kiến); trên 해모루 (phó/liên lạc — người ông tin nhất) và 고정수; hiểu 고건무; **đối tác thử thách với 한승우**; để ý 백성민; đối thủ trí tuệ với 우중문 (thơ); 3화 đích thân giả hàng vào trại Tùy |
| Visual identifiers | (1) râu bạc ngắn; (2) chỏm lông đen cao + 2 lông trắng; (3) ống đựng thư thắt lưng; (4) mắt hẹp sụp; (5) áo lót đỏ nâu lộ dưới giáp |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Không xuất hiện trực tiếp (chỉ nhắc tên / cờ hiệu xa). |
| 2화 | **Đến thành bằng đường bí mật**: áo choàng đen trùm kín giáp, không lông chỏm, bụi đường; sau đó giáp đủ bộ trên tường thành, tro nhẹ. |
| 3화 | **Giả hàng**: KHÔNG giáp — áo lụa đỏ nâu, 조우관 lông chim, tay không, đi bộ vào trại Tùy; mưa bụi; sau: giáp, mưa. |
| 4화 | Giáp trận, mưa dầm, bùn giày, áo choàng ướt; viết thơ trong lều (mũ tháo, tóc bạc búi). |
| 5화 | Trên gò cát Salsu: mưa, kiếm rút, chỏm lông rủ nước, bùn tới cẳng; cuối: nắng, đứng nhìn sông. |

**Giọng/ngôn ngữ**
- 사극체 **하오체** ("~하오/~시오/~이오"), câu ngắn, sắc, thỉnh thoảng mỉa. Với vua: 합쇼체 "전하". Gọi 한승우 "한 대장" / gọi đại đội "천둥 군사" (→ proposals); gọi xe tăng "쇠수레".
- Câu mẫu (foundation): "쇠수레는 며칠이나 달릴 수 있소?" / "성은 버티오. 문제는 평양이오." / "숨으시오. 30만이 지나가게 두시오." / "내년에 또 올 것이오."
- Câu mới: "천둥은 아껴 쓰는 법이오. 한 번 울리면 다음은 없소." / "그대들이 마개요. 물은 내가 막소."

**VISUAL_LOCK_EN** (59 từ)
> Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. Mid-50s Korean man, tall lean upright build, long rectangular face, hooded narrow razor-sharp dark eyes, long high-bridged nose, strong jaw with short trimmed silver-gray beard, gray hair in topknot. Goguryeo iron lamellar armor laced with red cord, shoulder guards and thigh skirt, iron plate helmet with tall dark plume and two white feathers, dark red-brown jacket beneath, ring-pommel longsword. Right hand resting on the sword hilt, a small leather scroll tube at the belt, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_101_cloak_incognito_ep2 | 2화 P4–P5 | ✔ | A plain black wool cloak with hood drawn over the armor hiding the plume, road dust on the hem and boots, helmet plume removed, face half in shadow of the hood. |
| CHAR_101_false_surrender_ep3 | 3화 P8–P9 | ✔ | No armor: a dark red-brown silk long jacket with black border, wide trousers, a Goguryeo bird-feather court cap with two white feathers, unarmed, empty hands open, light rain on the shoulders. |
| CHAR_101_salsu_rain_ep5 | 5화 | ✔ | Full armor soaked with rain, plume feathers heavy and dripping, mud to the shins, longsword drawn and held low, water droplets on the beard, eyes fixed on the distance. |
| CHAR_101_helmet_off_tent | 4화 lều | – | Helmet removed, gray topknot exposed, cloak over shoulders, brush in hand. |

---

### CHAR_102 — 영양왕 (King Yeongyang, 고원 Go Won)
| Trường | Giá trị |
|---|---|
| ID | CHAR_102 |
| Name | 영양왕 (King Yeongyang) — tên húy 고원 (Go Won); lịch sử thật, diện mạo HƯ CẤU |
| Role | Vua Goguryeo — câu hỏi chính trị "đội quân này thuộc về ai?" |
| Age | ~50 |
| Gender | Nam |
| Ethnicity | Goguryeo (Hàn cổ) |
| Skin tone | Sáng tái (sống trong cung), mịn |
| Face shape | Rộng, đầy đặn — "khuôn mặt giấu suy nghĩ" |
| Eyes | Mí sụp nặng, điềm tĩnh; đen; bọng mắt nhẹ |
| Nose | Sống mũi rộng, đầu mũi đầy |
| Jaw | Đầy, mềm; **râu cằm dài mảnh đen tới ngực + ria mảnh** |
| Hair style | Búi 상투 dưới 백라관 |
| Hair color | Đen, bạc thái dương |
| Body type | Đậm người, ngực rộng, cử động chậm, uy |
| Height impression | Trung bình (~170 cm); hầu hết ngồi (ngai) — cao hơn tất cả nhờ bệ |
| Base outfit | **백라관** (mũ lụa trắng có khung vàng, 삼족오 vàng trước trán); **long bào lụa đỏ thẫm thêu mây chỉ vàng**, tay áo rộng, lớp trong trắng; **thắt lưng da trắng gắn miếng vàng**; hài đen mũi cong |
| Accessories | Ngọc bội xanh treo thắt lưng; nhẫn vàng; hốt ngọc khi thiết triều |
| Equipment | Ấn vua; **chiếu chỉ cuộn lụa** (1화 "giữ thành đến chết"); ngai gỗ sơn đỏ; đèn dầu đồng |
| Weapon | Kiếm nghi lễ trên giá — không bao giờ rút |
| Personality | Chính trị gia kín; không kinh ngạc mà tính toán; hỏi câu khó ("그 뒤에 그대들은 누구의 군대인가?"); tin 을지문덕 nhưng giữ khoảng cách; nghĩ đến sau chiến tranh |
| Relationship | Anh của 고건무; quân chủ của 을지문덕/고정수/해모루; **KHÔNG gặp trực tiếp 한승우** — hỏi qua 해모루 (4화); kết series: bàn giữ hay giải tán "뇌군" |
| Visual identifiers | (1) 백라관 trắng-vàng; (2) râu cằm dài mảnh; (3) long bào đỏ thẫm; (4) thắt lưng trắng-vàng; (5) mí mắt sụp |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Cuối tập: thiết triều đêm, ánh đèn dầu, ban chiếu chỉ — trang phục đủ bộ, tĩnh. |
| 2화 | Không xuất hiện (chiếu chỉ được đọc). |
| 3화 | Không xuất hiện. |
| 4화 | Bình Nhưỡng: long bào + **áo choàng đen khoác ngoài** khi lên tường thành đêm nhìn lửa thuyền Tùy; mặt có bóng đèn đuốc. |
| 5화 | Kết: trong điện, nhận tin thắng — không đổi trang phục; nét mặt không cười. |

**Giọng/ngôn ngữ**
- 사극체 vương giả: **"과인"**, 하라체 "~하라/~인가/~하겠는가"; chậm, mỗi câu là một cân nhắc. Gọi 을지문덕 "대장군", 고건무 "아우", đại đội "그 군사들".
- Câu mẫu: "요동성은 죽어도 지키라. 이것이 과인의 뜻이다." / "그 뒤에 그대들은 누구의 군대인가?" (foundation) / "이겼다. 그런데 과인은 무엇을 얻었는가."

**VISUAL_LOCK_EN** (57 từ)
> Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. Korean man around 50, heavy-set broad build, broad full face, heavy-lidded calm dark eyes, broad fleshy nose, soft full jaw, long thin black chin beard reaching the chest, thin mustache, graying black topknot. Goguryeo royal white silk crown with gold fittings, deep crimson silk robe with gold cloud embroidery, wide sleeves, white leather belt with gold plaques. Hands clasped before the belt, jade pendant hanging from the belt, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_102_wall_night_ep4 | 4화 P4, P12 | ✔ | A heavy black wool cloak over the crimson robe, crown unchanged, standing, face lit warm from one side as if by torchlight, faint mist on the shoulders. |
| CHAR_102_seated_throne | 1화 P12 / 5화 P12 | – | Seated on a red-lacquered wooden throne, hands on knees, edict scroll on a low table. |

---

### CHAR_103 — 고건무 (Go Geon-mu)
| Trường | Giá trị |
|---|---|
| ID | CHAR_103 |
| Name | 고건무 (Go Geon-mu) — em vua, sau là 영류왕; lịch sử thật, diện mạo HƯ CẤU |
| Role | Chỉ huy phòng thủ Bình Nhưỡng; 4화 phục kích thủy quân 내호아 |
| Age | ~40 |
| Gender | Nam |
| Ethnicity | Goguryeo (Hàn cổ) |
| Skin tone | Rám trung bình |
| Face shape | Vuông, trán rộng, **gờ lông mày nổi** |
| Eyes | Sâu, quan sát, hơi nghi ngờ; đen |
| Nose | Rộng, thẳng, ngắn |
| Jaw | Nặng; **râu quai nón đen cắt gọn sát hàm + ria** |
| Hair style | Búi 상투 |
| Hair color | Đen |
| Body type | Chắc, mạnh, cẳng tay dày — võ tướng thực chiến |
| Height impression | ~175 cm, vai rộng, đứng dạng chân |
| Base outfit | **찰갑 sắt sẫm** xâu dây da nâu (tối hơn của 을지문덕), bọc da ngực; 저고리 **xanh chàm sẫm** bên trong; bao tay da; **mũ trụ sắt chỏm bờm ngựa ĐỎ ngắn**; giày da cao |
| Accessories | Mặt dây đồng 삼족오; dây lụa đỏ quấn gốc mũ (dấu hoàng tộc); nhẫn ngọc |
| Equipment | Ngựa (đen), **khiên tròn gỗ bọc da có núm sắt**, tù và |
| Weapon | **Giáo dài (장창)** + 환두대도 ngắn |
| Personality | Thực dụng, quyết đoán, nghi ngờ đại đội (họ là ai, sau chiến tranh thì sao); tự trọng hoàng tộc; muốn thắng bằng người của mình; lắng nghe 을지문덕 nhưng không phục tùng mù |
| Relationship | Em của 영양왕; ngang hàng chiến lược với 을지문덕; đối thủ trực tiếp của 내호아 (phục kích ngoại thành — thật); nghi 한승우; 해모루 là người truyền tin giữa hai bên |
| Visual identifiers | (1) chỏm bờm ngựa đỏ ngắn; (2) râu quai nón gọn; (3) khiên tròn; (4) gờ lông mày; (5) giáo dài |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1–3화 | Không xuất hiện (có thể nhắc tên). |
| 4화 | **Phục kích ngoại thành**: máu trên lưỡi giáo và cẳng tay, khói, mồ hôi, khiên nứt một mảnh, chỏm đỏ xơ; sau trận: tháo mũ, tóc ướt, mặt lem khói. |
| 5화 | Kết: tại Bình Nhưỡng cạnh vua, giáp sạch hơn, không mũ. |

**Giọng/ngôn ngữ**
- 하오체 với ngang hàng, **하게체** với thuộc hạ; thẳng, cộc. Với vua: 합쇼체 "전하" — "신". Gọi đại đội "그 쇠수레 무리".
- Câu mẫu: "성문을 열어라. 놈들이 시장까지 들어오게 두라." / "저들이 우리 편이라 믿소? 나는 아직이오." / "평양은 고구려 사람이 지키오."

**VISUAL_LOCK_EN** (57 từ)
> Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. Korean man around 40, stocky powerful build, square face, heavy brow ridge, deep-set watchful dark eyes, short broad nose, heavy jaw with short black chinstrap beard and mustache, black topknot. Dark iron lamellar armor over a dark blue long jacket, leather bracers, iron helmet with short red horsehair crest, round wooden shield with iron boss, long spear. Spear held upright in the right hand, shield on the left arm, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_103_ambush_ep4 | 4화 P5–P8 | ✔ | Blood on the spear blade and right forearm, smoke smudges on face and armor, sweat, one plank of the round shield split, red crest frayed, teeth clenched mid-battle. |
| CHAR_103_helmet_off | 4화 sau trận / 5화 | – | Helmet removed and held at the side, black topknot loosened, smoke-smudged face, calm. |

---

### CHAR_104 — 고정수 (Go Jeong-su) — HƯ CẤU
| Trường | Giá trị |
|---|---|
| ID | CHAR_104 |
| Name | 고정수 (Go Jeong-su) |
| Role | 요동성주 — thành chủ Liêu Đông; người tin đại đội đầu tiên |
| Age | 45 |
| Gender | Nam |
| Ethnicity | Goguryeo (Hàn cổ) |
| Skin tone | Hồng hào rám (ruddy tan) |
| Face shape | Tròn, má đầy, mệt nhưng ấm |
| Eyes | Tròn hơn người Goguryeo khác, ấm, nhiều nếp nhăn; đen |
| Nose | Đầu mũi to tròn |
| Jaw | Tròn; **râu đen rậm bù xù có vệt bạc** (khác các tướng râu gọn) |
| Hair style | Búi 상투 + **khăn 건 quấn trán** |
| Hair color | Đen pha bạc |
| Body type | Nặng, ngực thùng, bụng to — "người cha của thành" |
| Height impression | Thấp (~168 cm), bề ngang rộng |
| Base outfit | Quan văn kiêm võ: **찰갑 chỉ phần thân (không 견갑 vai)** mặc ngoài 저고리 **nâu viền trắng**, quần **vàng đất**; **áo choàng len xám dày**; mũ trụ sắt trơn không chỏm — **thường cầm dưới nách** hơn là đội |
| Accessories | **Vòng sắt chùm chìa khóa cổng thành** ở thắt lưng; ấn thành chủ; thẻ tre kiểm kho lương |
| Equipment | Đuốc; sổ tre kiểm lương (luôn lo lương); ngựa (lùn, nâu) |
| Weapon | Kiếm ngắn hiếm rút |
| Personality | Bảo vệ dân trên hết; thực tế; tin đại đội sớm vì họ cứu dân của ông; lo lương thực → ràng buộc chính trị "cho ăn = lệ thuộc"; can đảm âm thầm trên tường thành |
| Relationship | Cấp dưới 을지문덕; **đối tác đầu tiên của 한승우**; "cha" cộng đồng 을보/아리; 2화 chỉ huy phòng thủ cùng đại đội; 3화 tặng 한승우 áo choàng khi rời thành; ở lại giữ thành (không nam hạ) |
| Visual identifiers | (1) râu rậm muối tiêu; (2) áo choàng len xám; (3) chùm chìa khóa; (4) mũ cầm nách; (5) khăn trán |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Bụi đường, áo choàng xám, đón dân chạy nạn ở cổng 옹성; đuốc. |
| 2화 | **Vây thành**: bụi đá, tro đuốc, **băng vải quấn trán dưới khăn** (mảnh đá), râu dính bụi, áo choàng cháy thủng; mũ ĐỘI trong đợt công thành. |
| 3화 | Tiễn đại đội ở cổng: sạch hơn, mệt, áo choàng đã tặng → không có áo choàng. |
| 4–5화 | Không xuất hiện (nhắc: "요동성은 아직 서 있소"). |

**Giọng/ngôn ngữ**
- 하오체 ấm; với dân 하게체 dịu ("어서 들어가게"). Với 을지문덕 합쇼체. Gọi 한승우 "한 대장", đại đội "천둥 군사".
- Câu mẫu: "저들이 우리 백성을 구했소. 나는 그걸로 족하오." / "창고에 곡식이 스무 날 치요. 스무 날." / "성문은 내가 닫소. 나가시오."

**VISUAL_LOCK_EN** (58 từ)
> 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 45-year-old Korean man, short heavy build, round ruddy face, warm round wrinkled dark eyes, bulbous nose, round jaw with bushy black beard streaked gray, black topknot under cloth headband. Iron lamellar cuirass over a brown long jacket with white border, heavy gray wool cloak, plain iron helmet carried under one arm, iron ring of gate keys at belt. Ochre trousers and leather boots, right hand resting on the belt, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_104_siege_ep2 | 2화 P4–P11 | ✔ | Helmet worn on the head, a blood-spotted cloth bandage around the forehead under the headband, stone dust in the beard, torch soot on cheeks, cloak scorched with a burnt hole, tired fierce eyes. |
| CHAR_104_no_cloak_ep3 | 3화 P2–P3 | – | Without the gray cloak, cuirass and brown jacket only, helmet under arm, face washed but exhausted. |

---

### CHAR_105 — 해모루 (Hae Mo-ru) — HƯ CẤU
| Trường | Giá trị |
|---|---|
| ID | CHAR_105 |
| Name | 해모루 (Hae Mo-ru) |
| Role | 말객 (sĩ quan cấp trung), phó tướng liên lạc thực địa của 을지문덕 — thoại nhiều nhất phía Goguryeo |
| Age | 32 |
| Gender | Nam |
| Ethnicity | Goguryeo (Hàn cổ) |
| Skin tone | Rám nắng đều |
| Face shape | Sắc, góc cạnh, gò má cao — mặt "diều hâu" |
| Eyes | Sáng, nhanh, đuôi mắt hơi xếch lên; nâu sẫm; lông mày biểu cảm |
| Nose | Thẳng, hẹp |
| Jaw | Sắc; **KHÔNG râu** (cạo nhẵn / lún phún nhẹ) — duy nhất phía Goguryeo |
| Hair style | Búi 상투 buộc dây da, vài sợi lòa xòa |
| Hair color | Đen |
| Body type | Gầy, thể thao, chân kỵ sĩ; cử động nhanh |
| Height impression | ~176 cm — cao, nhẹ; ngang 백성민 |
| Base outfit | **찰갑 nhẹ: sắt phần ngực + váy da xâu dây** (sĩ quan cơ động); 저고리 **xanh lá sẫm viền đỏ**; bao tay da; **mũ trụ sắt cắm 1 lông trắng**; giày cưỡi ngựa |
| Accessories | Miếng thắt lưng đồng hình chim 삼족오; **tù và (뿔나팔) đeo hông**; cờ hiệu nhỏ sau yên; (3화+) **máy radio PRC-999K cầm tay kẹp trên dây giáp ngực** do 한승우 giao — biểu tượng contrast |
| Equipment | Ngựa (hạt dẻ), cung phức hợp + ống tên trên yên, radio (3화+) |
| Weapon | 환두대도 ngắn hơn, cung, giáo nhẹ |
| Personality | Nhanh, tò mò, học chiến thuật hiện đại nhanh nhất; dũng cảm; kính 을지문덕; sốt ruột với chính trị; "phiên dịch văn hóa"; 5화 bị thương nặng khi gánh phần cuối |
| Relationship | Phó/liên lạc của 을지문덕; **bạn thực địa với 백성민**; cầu nối 한승우 ↔ Goguryeo (kể cả vua); được 윤서아 cứu 5화; truyền tin giữa 고건무 và đại đội |
| Visual identifiers | (1) 1 lông trắng; (2) không râu; (3) tù và; (4) radio hiện đại trên giáp (3화+); (5) áo xanh lá viền đỏ |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Đang thu quân sau chạm trán: bụi vàng, máu khô trên bao tay, ngựa thở dốc. |
| 2화 | Tro trên giáp, mồ hôi; lông trắng cháy sém đầu. |
| 3화 | **Radio kẹp trên giáp ngực** (từ đây); mưa, áo choàng vải dầu; bùn. |
| 4화 | Mưa dầm; đi lại giữa Bình Nhưỡng và Salsu: bùn tới đùi, ngựa ướt; mắt trũng. |
| 5화 | **Bị thương**: mũi tên cắm vai trái/dưới xương đòn, máu loang xanh lá thành đen, mũ rơi, tóc xổ, nằm trong lau sậy; sau: băng trắng hiện đại quấn chéo ngực, nửa ngồi. |

**Giọng/ngôn ngữ**
- 하오체 với lính hiện đại ("대장, 쇠새는 어디까지 보오?"); 합쇼체 với 을지문덕/vua ("장군", "전하"); 하게체 với lính mình. Gọi drone "쇠새" (chim sắt), K2 "쇠수레", radio "말하는 돌".
- Câu mẫu: "영양왕 이십삼 년이오. 그대들은 어디서 왔소?" / "그 쇠새로 강 건너까지 보오? 그럼 내가 길을 내겠소." / (5화, thều thào) "마개는… 아직 서 있소?"

**VISUAL_LOCK_EN** (57 từ)
> 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 32-year-old Korean man, tall lean rider's build, sharp angular hawk-like face, bright quick upturned dark eyes, narrow straight nose, sharp clean-shaven jaw, black topknot. Light Goguryeo iron lamellar chest armor with laced leather skirt over a dark green long jacket with red border, iron helmet with a single white feather, signal horn slung at hip, ring-pommel sword. Leather bracers, composite bow and quiver on the back, left hand on the sword hilt, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_105_dusty_ep1 | 1화 P4–P12 | – | Fine yellow dust on armor and face, dried blood on leather gloves, sweat, feather slightly bent. |
| CHAR_105_radio_ep3 | 3화–4화 | ✔ | A modern olive-green military handheld radio clipped to the chest armor lacing, rain-soaked armor and jacket, oiled dark cloak over one shoulder, mud on boots and skirt, wet feather. |
| CHAR_105_wounded_ep5 | 5화 P9–P12 | ✔ | Helmet gone, topknot loosened, an arrow shaft embedded below the left collarbone, blood soaking the green jacket black, lying half-propped in mud and reeds, face pale, rain on skin. |
| CHAR_105_bandaged_ep5 | 5화 P12 | – | Modern white bandage wrapped diagonally across the bare chest and shoulder, jacket draped over, seated, weak but alert. |

---

## 3. DÂN GOGURYEO (hư cấu)

### CHAR_106 — 을보 영감 (Eul-bo)
| Trường | Giá trị |
|---|---|
| ID | CHAR_106 |
| Name | 을보 (Eul-bo) — gọi "을보 영감" |
| Role | Thợ rèn thành Liêu Đông, chạy nạn 1화; "kỹ sư thời cổ" của đại đội |
| Age | 66 |
| Gender | Nam |
| Ethnicity | Goguryeo (Hàn cổ) — thường dân |
| Skin tone | Nâu sẫm phong sương; **sẹo bỏng cũ loang cẳng tay** |
| Face shape | Hốc hác, nếp nhăn sâu, má hóp, trán cao |
| Eyes | Nhỏ, sâu, sáng; **mắt trái nheo thường trực** (bao năm nhìn lửa lò) |
| Nose | Khoằm, to |
| Jaw | Sắc; **râu cằm trắng dài lưa thưa**, lông mày trắng |
| Hair style | Thưa, búi 상투 nhỏ, **khăn gai quấn trán** |
| Hair color | Trắng |
| Body type | Gầy, lưng còng, nhưng cẳng tay gân guốc, **bàn tay to chai, mất đốt đầu ngón áp út trái** |
| Height impression | Thấp (~165 cm), còng — thấp nhất nhóm nam |
| Base outfit | **저고리 vải gai thô không nhuộm** (xám be), quần gai bó cổ chân, **tạp dề da rèn cháy sém**, thắt lưng dây thừng, dép rơm |
| Accessories | **Búa nhỏ ở thắt lưng**; cuộn da dụng cụ; đá mài; bọc hành lý sau lưng (1화) |
| Equipment | Búa, kìm, đá mài; sau 2화: uốn thanh sắt thành móc kéo, mài xẻng, sửa lưỡi lê |
| Weapon | Không (búa nếu cần) |
| Personality | Ít lời, cứng đầu, tò mò kim loại lạ; sờ giáp xe tăng như sờ ngựa; không sợ lính; nói thẳng với cả 성주 |
| Relationship | Ông của 아리; **bạn của 박기철** (ngôn ngữ chung = kim loại); dân của 고정수; được cứu bởi quyết định 1화 của 한승우 → lý do đại đội "lộ diện"; nam hạ cùng đại đội 3화 (→ proposals) |
| Visual identifiers | (1) tạp dề da; (2) búa thắt lưng; (3) mắt trái nheo; (4) mất đốt ngón tay; (5) râu cằm trắng lưa thưa |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | **Chạy nạn**: bọc hành lý sau lưng, bụi vàng, máu người khác trên tay áo, kéo 아리 chạy; không tạp dề. |
| 2화 | Tại 천둥 기지: tạp dề, bồ hóng, đứng bên xe K21 với 박기철. |
| 3화 | Nam hạ: gậy chống, áo choàng gai, mưa, dép rơm bùn; mang cuộn dụng cụ. |
| 4화 | Lau sậy: ướt, im lặng, giữ 아리; tay run vì lạnh. |
| 5화 | Sau trận: đứng nhìn K2 lún bùn, tay sờ giáp thép; nắng. |

**Giọng/ngôn ngữ**
- **하게체/반말** với tất cả kể cả lính hiện đại (ông già); với 성주 하오체 miễn cưỡng. Gọi 박기철 "쇠쟁이" (thợ sắt), 한승우 "대장 양반".
- Câu mẫu: "이 쇠는 우리 쇠가 아니야. 너무 곱네." / "기름이 없으면 말이 못 뛰지. 이놈도 그렇겠구먼." / "고쳐줄게. 대신 이 쇠 한 조각은 내 거야."

**VISUAL_LOCK_EN** (56 từ)
> 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 66-year-old Korean man, thin stooped build, huge calloused hands, gaunt deeply wrinkled face, small deep-set bright eyes, left eye squinting, large hooked nose, sharp jaw with long wispy white chin beard, thin white hair in small topknot under hemp headband. Coarse undyed hemp jacket and trousers, scorched leather forge apron, straw sandals, small hammer at belt. Rope belt, old burn scars on the forearms, holding a pair of blacksmith tongs in one hand, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_106_refugee_ep1 | 1화 P4–P7 | ✔ | No apron: a large cloth bundle tied on the back, yellow dust over hair and clothes, someone else's blood on the right sleeve, walking staff, frightened exhausted face. |
| CHAR_106_forge_ep2 | 2화–3화 căn cứ | ✔ | Leather apron blackened with soot, sweat on the brow, sleeves pushed up showing burn-scarred forearms, hammer in hand. |
| CHAR_106_rain_south_ep3 | 3화–4화 | – | Coarse hemp cloak over the jacket, rain-soaked, mud on sandals and shins, walking staff, tool roll on the back. |

---

### CHAR_107 — 아리 (A-ri)
| Trường | Giá trị |
|---|---|
| ID | CHAR_107 |
| Name | 아리 (A-ri) |
| Role | Cháu gái 을보; góc nhìn dân thường; 4화 dẫn 백성민 vào trại Tùy |
| Age | 15 |
| Gender | Nữ |
| Ethnicity | Goguryeo (Hàn cổ) — thường dân |
| Skin tone | Sáng rám nhẹ; **má nứt gió ửng hồng** |
| Face shape | Tròn nhỏ, trán cao, trẻ con |
| Eyes | To, tròn, sáng; đen; **lông mày dày thẳng** |
| Nose | Nhỏ, tròn |
| Jaw | Cằm tròn mềm |
| Hair style | **2 bím tóc dài buộc chỉ đỏ**, mái ngắn |
| Hair color | Đen |
| Body type | Nhỏ, gầy, nhanh nhẹn |
| Height impression | ~152 cm — nhỏ nhất dàn nhân vật; đứng cạnh 윤서아 thấp hơn nửa đầu |
| Base outfit | **저고리 vải gai nhuộm chàm bạc màu, viền trắng**; **váy xếp ly (주름치마) màu vàng đất dài tới cổ chân**; dép rơm; khăn gai trùm đầu khi chạy nạn; **(2화+) khăn quân đội màu olive** quàng cổ do 윤서아 tặng |
| Accessories | Chỉ đỏ buộc tóc; **túi vải nhỏ đựng hạt/thảo dược ở thắt lưng**; (4화) đèn lồng nhỏ không thắp |
| Equipment | Giỏ đan; thuộc đường mòn núi; dao nhỏ hái thuốc |
| Weapon | Không |
| Personality | Nhanh, gan, tò mò, ít sợ; hỏi câu người lớn không dám ("돌아갈 수 있어요?"); học chữ Hangul từ 윤서아 (viết lên đất); coi 태오 là anh |
| Relationship | Cháu 을보; **"em gái" của 윤서아**; dẫn đường 백성민 4화; bạn đồng lứa của 태오; 고정수 biết tên cô |
| Visual identifiers | (1) 2 bím chỉ đỏ; (2) áo chàm viền trắng; (3) váy xếp ly vàng đất; (4) khăn olive (2화+); (5) túi thảo dược |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Chạy nạn: khăn gai trùm đầu, bụi, nước mắt vệt bụi, dép rơm đứt một chiếc; ôm giỏ. |
| 2화 | Khăn olive quàng cổ (từ đây); sạch hơn; giúp lều quân y — máu trên ngón tay. |
| 3화 | Mưa: bím tóc ướt, váy bùn gấu, áo choàng gai; đi cạnh 을보. |
| 4화 | **Đêm dẫn đường**: bím giấu dưới khăn tối, mặt bôi bùn (백성민 bôi cho), váy vén buộc gối, chân trần, đèn lồng không thắp trên tay. |
| 5화 | Cùng 윤서아 băng bó thương binh: máu trên hai bàn tay, khăn olive buộc tay áo, mưa rồi nắng. |

**Giọng/ngôn ngữ**
- **해요체** trẻ con; với ông 존댓말 nhẹ ("할아버지, 여기요"); với 윤서아 "언니"; với lính "군사 아저씨"; với 태오 "오라버니" (→ 오빠 quá hiện đại).
- Câu mẫu: "언니, 이 풀은 피를 멎게 해요. 씹어서 붙여요." / "그 길은 제가 알아요. 염소 길이에요." / "돌아갈 수 있어요? 언니네 집으로요."

**VISUAL_LOCK_EN** (59 từ)
> 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 15-year-old Korean girl, small thin build, small round face, large round bright dark eyes, thick straight brows, small button nose, soft round chin, wind-chapped pink cheeks, black hair in two long braids tied with red thread, short fringe. Faded indigo hemp jacket with white border over an ochre pleated ankle-length skirt, straw sandals, small cloth herb pouch at waist. Holding a small woven basket in both hands, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_107_refugee_ep1 | 1화 P4–P7 | ✔ | A coarse hemp scarf over the head, yellow dust on clothes and face, tear tracks through the dust, one straw sandal broken, clutching a basket, frightened. |
| CHAR_107_scarf_ep2 | 2화–5화 mặc định | ✔ | A modern olive-green military scarf tied around the neck over the indigo jacket, braids neat, small smear of blood on the fingertips. |
| CHAR_107_night_trail_ep4 | 4화 P8–P9 | ✔ | Braids hidden under a dark cloth, mud smeared on cheeks, skirt hitched and tied at the knees, bare feet, olive scarf, carrying a small unlit paper lantern, wet from rain. |

---

## 4. TÙY (수나라)

### CHAR_201 — 수 양제 (Emperor Yang of Sui, 양광 Yang Guang)
| Trường | Giá trị |
|---|---|
| ID | CHAR_201 |
| Name | 수 양제 (Emperor Yang of Sui) — tên húy 양광 (Yang Guang); lịch sử thật, diện mạo HƯ CẤU |
| Role | Hoàng đế Tùy, đích thân chỉ huy vây Liêu Đông từ 육합성 |
| Age | ~43 |
| Gender | Nam |
| Ethnicity | Hán (Tùy) |
| Skin tone | Tái sáng, mịn, hơi phù (sống trong cung) |
| Face shape | Dài, hẹp, thanh tú — đẹp kiểu kiêu |
| Eyes | Hạnh nhân, mí sụp nửa, lạnh, ngạo; đen |
| Nose | Dài, cao, thanh |
| Jaw | Hẹp, nhọn; **râu dê dài mảnh đen + ria mảnh rủ qua khóe miệng** |
| Hair style | Búi dưới 통천관 |
| Hair color | Đen |
| Body type | Cao, mảnh, mềm — không phải võ tướng; bàn tay dài |
| Height impression | ~178 cm — cao hơn mọi tướng Tùy; hay đứng trên bậc |
| Base outfit | **통천관** (mũ cao đen sơn mài, khung vàng, thanh vàng); **áo 자황 (vàng thổ) lụa thêu rồng chỉ vàng**; ngoài (khi ra trận): **giáp lamellar nghi lễ mạ vàng**, đai lụa đỏ; hài đỏ; thắt lưng ngọc gắn vàng |
| Accessories | Nhẫn ngọc; hốt ngọc (규) khi thiết triều; quạt tròn lụa (trong lều) |
| Equipment | 육합성 (thành di động); chiếu chỉ; (3화+) **drone bị bắt đặt trên bàn lụa** — ông tự tay xem |
| Weapon | Kiếm chuôi vàng nghi lễ |
| Personality | Kiêu ngạo, cầu toàn, thông minh nhưng nóng; tự ra lệnh chi tiết từng việc (lịch sử: bắt tướng báo cáo mọi việc → vây chậm); coi "뇌군" là vật phải sở hữu; thanh lịch và nguy hiểm — không caricature |
| Relationship | Hoàng đế của 우중문/우문술/내호아; **dùng 탁발흠 báo cáo trực tiếp** (bất thường — lý do Tuoba có quyền hành động); đối thủ vô hình của 한승우 (không gặp mặt); 5화 nhận tin thảm bại |
| Visual identifiers | (1) 통천관 đen-vàng; (2) áo vàng thổ; (3) giáp mạ vàng; (4) râu dê dài mảnh; (5) dáng cao mảnh |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | Đọc chiếu xuất quân: đủ bộ, sạch tuyệt đối; nghe 탁발흠 quỳ báo. |
| 2화 | Tại 육합성 nhìn thành: giáp mạ vàng, **bụi bám gấu áo vàng**, mặt cáu; đêm: áo lụa không giáp. |
| 3화 | Không giáp, áo vàng, xem drone/kính đêm bị bắt — cầm lên ngang mắt; nắng lều. |
| 4화 | Không xuất hiện (lệnh truyền qua sứ). |
| 5화 | Nhận tin: đứng bất động, mặt trắng bệch, mũ hơi lệch, tay bóp nát tờ tấu — không gào. |

**Giọng/ngôn ngữ**
- 사극체 đế vương Trung Hoa: **"짐"**, 하라체; lạnh, chậm, từng chữ. Tướng gọi ông "폐하". Gọi Goguryeo "고구려 놈들", đại đội "뇌군".
- Câu mẫu: "그럼 그 천둥을 가져오라." (foundation) / "천둥을 산 채로 잡아라." (foundation) / "성 하나에 넉 달이라. 짐이 웃어야 하는가."

**VISUAL_LOCK_EN** (57 từ)
> Early-40s Chinese man, tall slender soft build, long narrow refined face, half-lidded cold almond eyes, long high elegant nose, narrow pointed jaw with long thin black goatee and thin mustache, black topknot. Tall black lacquered imperial crown with gold beams, ochre-yellow silk robe embroidered with gold dragons under gilded ceremonial lamellar cuirass, jade belt with gold plaques.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. Early-40s Chinese man, tall slender soft build, long narrow refined face, half-lidded cold almond eyes, long high elegant nose, narrow pointed jaw with long thin black goatee and thin mustache, black topknot. Tall black lacquered imperial crown with gold beams, ochre-yellow silk robe embroidered with gold dragons under gilded ceremonial lamellar cuirass, jade belt with gold plaques. Red silk sash, red boots, right hand resting on a gold-hilted ceremonial sword, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_201_robe_only_ep3 | 1화 đêm / 3화 | ✔ | Without the gilded cuirass: ochre-yellow silk robe with wide sleeves only, crown unchanged, hands holding a small dark gray quadcopter drone at eye level, studying it. |
| CHAR_201_field_dust_ep2 | 2화 | – | Gilded cuirass, fine dust on the yellow hem and red boots, irritated expression, a round silk fan in the left hand. |
| CHAR_201_defeat_news_ep5 | 5화 P11–P12 | ✔ | Standing rigid, face drained white, crown slightly askew, a crushed paper report in the clenched right fist, eyes wide and unblinking, no armor, yellow robe. |

---

### CHAR_202 — 우중문 (Yu Zhongwen)
| Trường | Giá trị |
|---|---|
| ID | CHAR_202 |
| Name | 우중문 (Yu Zhongwen) — lịch sử thật, diện mạo HƯ CẤU |
| Role | Tổng chỉ huy quân đột kích 30만 5천; người nhận bài thơ |
| Age | ~65 |
| Gender | Nam |
| Ethnicity | Hán (Tùy) |
| Skin tone | Hồng đỏ phong sương, đốm đồi mồi |
| Face shape | Vuông rộng, đầy thịt, má xệ |
| Eyes | Nhỏ, dữ, vằn đỏ; **lông mày trắng rậm** |
| Nose | Rộng, đầu mũi đỏ |
| Jaw | Nặng; **râu trắng dài đầy tới ngực**, ria ngả vàng |
| Hair style | Búi 상투 |
| Hair color | Trắng |
| Body type | To, ngực thùng, cổ dày, vẫn khỏe; nặng trên yên |
| Height impression | ~172 cm, bề ngang lớn — "tảng đá" |
| Base outfit | **명광개**: giáp lamellar sắt với **2 gương ngực tròn bóng** viền mạ vàng; **áo choàng lụa đỏ**; mũ sắt **chỏm tua đỏ** + tấm che gáy; giày da sơn đỏ |
| Accessories | Miếng thắt lưng đầu hổ; gậy lệnh ngà ngắn; nhẫn vàng to |
| Equipment | Ngựa (đen to), cờ lệnh; (4화) bài thơ 5 chữ 4 câu trên lụa |
| Weapon | 횡도 (kiếm thẳng dài) mạ vàng; chùy ở yên |
| Personality | Hiếu chiến, kiêu, thiếu kiên nhẫn; muốn công Bình Nhưỡng ngay; tự ái bị bài thơ đâm trúng; ra quyết định rút → thảm bại; không ngu — chỉ mù vì danh dự |
| Relationship | Trên 우문술 (xung đột tiến/lùi — thật); nhận thơ 을지문덕; nghe/không nghe 탁발흠; không phối hợp với 내호아; (outline) có thể bị bắt sống 5화 |
| Visual identifiers | (1) 2 gương ngực; (2) râu trắng dài; (3) áo choàng đỏ; (4) tua đỏ mũ; (5) lông mày trắng rậm |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1–2화 | Không/ít xuất hiện (hội nghị 육합성: đủ bộ, sạch). |
| 3화 | Áp Lục: bụi, rồi mưa; cãi với 우문술 trong lều — mũ tháo, râu dính mưa. |
| 4화 | **Nhận thơ**: trong lều, mũ tháo, áo choàng cởi, đọc lụa dưới đèn; mặt đỏ dần. |
| 5화 | **Thảm bại**: bùn tới ngực, áo choàng rách nửa, một gương ngực móp, tua đỏ đứt, râu bết bùn, mưa; (nếu bị bắt) quỳ trên bãi cát, tay trói. |

**Giọng/ngôn ngữ**
- Với vua: 합쇼체 "폐하" — "신"; với tướng: 하오체 gầm; với 우문술 mỉa ("우 장군은 늙었소"). Gọi 을지문덕 "을지 놈".
- Câu mẫu: "평양은 사흘 거리요. 사흘이면 끝나오." / "이 시가… 나를 비웃는 것이냐?" / (5화) "물이… 물이 왜 이렇게 빠른가."

**VISUAL_LOCK_EN** (57 từ)
> Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. Mid-60s Chinese man, big barrel-chested powerful build, broad square fleshy face, small fierce bloodshot eyes under bushy white brows, broad reddish nose, heavy jaw with long full white beard to the chest, white topknot. Sui mingguang iron lamellar armor with two polished round breast mirrors and gilded edges, red silk cloak, iron helmet with red tassel crest. Helmet with iron neck guard, red lacquered leather boots, holding a sheathed gilt-hilted straight sword, cloak thrown back over the shoulders, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_202_tent_ep4 | 3화–4화 lều | ✔ | Helmet off showing the white topknot, red cloak removed, armor worn open at the throat, holding a small silk scroll, face flushed red with anger, lamplight warmth on the beard. |
| CHAR_202_defeat_ep5 | 5화 P9–P12 | ✔ | Mud caked to the chest, red cloak torn to half its length, one breast mirror dented, red tassel torn off, beard matted with mud and rain, helmet lost, stunned exhausted face. |

---

### CHAR_203 — 우문술 (Yuwen Shu)
| Trường | Giá trị |
|---|---|
| ID | CHAR_203 |
| Name | 우문술 (Yuwen Shu) — lịch sử thật, diện mạo HƯ CẤU |
| Role | Phó tổng chỉ huy — phái thận trọng, muốn rút vì hết lương |
| Age | ~65 |
| Gender | Nam |
| Ethnicity | Hán (Tùy) |
| Skin tone | Vàng tái, mỏng |
| Face shape | Hẹp, dài, má hóp, nếp mũi-miệng sâu |
| Eyes | Mệt, thông minh, đuôi xuôi, mí trĩu; lông mày xám |
| Nose | Mảnh, dài, hơi khoằm |
| Jaw | Hẹp; **râu xám cắt ngắn gọn + ria xám dài mảnh** (đối lập râu dài 우중문) |
| Hair style | Búi 상투; trong lều: khăn đầu đen |
| Hair color | Xám |
| Body type | Gầy, hơi còng, bàn tay dài |
| Height impression | ~168 cm — thấp hơn 우중문, luôn đứng lệch một bước |
| Base outfit | **양당개 (giáp hai mảnh) sắt sẫm sơn đen, không trang trí** ngoài áo bào **xanh sẫm**; **áo choàng xám sẫm cổ lông**; mũ sắt trơn (thường cầm) |
| Accessories | **Thẻ tre ghi lương** trong tay; ống bút; ngọc bội nhỏ |
| Equipment | Ngựa (xám), sổ tre |
| Weapon | Kiếm ít rút |
| Personality | Thận trọng, thực tế, nhìn lương thực và người; "biết mà không được nghe"; nói nhỏ, đúng; giữ thể diện cho 우중문 nhưng ghi lại tất cả |
| Relationship | Phó của 우중문 — xung đột tiến/lùi (enemy POV chính 3–4화); tôn trọng 탁발흠 (người duy nhất nghe Tuoba); 5화 dẫn tàn quân rút |
| Visual identifiers | (1) râu xám ngắn gọn; (2) giáp đen trơn; (3) áo choàng xám cổ lông; (4) thẻ tre trong tay; (5) dáng gầy còng |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1–2화 | Hội nghị 육합성: đủ bộ, đứng sau 우중문. |
| 3화 | Áp Lục: mưa bụi, thẻ tre ướt, mặt lo; thấy lính chôn lương. |
| 4화 | Lều: khăn đầu đen, không giáp, áo bào xanh, viết thẻ tre dưới đèn. |
| 5화 | **Rút**: bùn tới gối, áo choàng ướt nặng, mũ đội, dắt ngựa què, nhìn lại sông. |

**Giọng/ngôn ngữ**
- 합쇼체 cẩn trọng với vua và 우중문 ("장군, 아뢰옵니다"); 하오체 khô với thuộc hạ. Tôn trọng: gọi 탁발흠 "탁발 낭장".
- Câu mẫu: "군량이 열흘 치도 남지 않았습니다." / "적이 일곱 번 졌습니다. 일곱 번 다 뜻대로 졌습니다." / (5화) "돌아갑니다. 살아 있는 자만."

**VISUAL_LOCK_EN** (58 từ)
> Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. Mid-60s Chinese man, thin slightly stooped build, long narrow face with hollow cheeks, tired intelligent downturned eyes, thin long slightly hooked nose, narrow jaw with short trimmed gray beard and long thin gray mustache, gray topknot. Plain dark iron two-piece cuirass with black lacquer over a dark blue robe, dark gray cloak with fur collar, unadorned iron helmet. Helmet carried under the left arm, a bundle of bamboo slip records in the right hand, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_203_tent_ep4 | 3화–4화 lều | – | No armor: dark blue robe and a black cloth head wrap, cloak over the shoulders, brush and bamboo slips in hand, lamplight. |
| CHAR_203_retreat_ep5 | 5화 P9–P12 | ✔ | Helmet on, cloak soaked and heavy with rain, mud to the knees, face gray with exhaustion, leading a limping gray horse by the reins, looking back over his shoulder. |

---

### CHAR_204 — 내호아 (Lai Huer)
| Trường | Giá trị |
|---|---|
| ID | CHAR_204 |
| Name | 내호아 (Lai Huer) — lịch sử thật, diện mạo HƯ CẤU |
| Role | Đô đốc thủy quân Tùy; 4화 đổ bộ 4 vạn vào Bình Nhưỡng, bị phục kích |
| Age | ~50 |
| Gender | Nam |
| Ethnicity | Hán (Tùy) |
| Skin tone | Rám sẫm, nứt gió biển |
| Face shape | Rộng, gò má dẹt, mày nặng |
| Eyes | Hẹp, nheo (chói nắng biển), chân chim sâu; đen |
| Nose | Rộng, **sống mũi dẹt (từng gãy)** |
| Jaw | Vuông; **râu đen-xám ngắn dày** |
| Hair style | Búi, **quấn khăn xanh sẫm** dưới mũ |
| Hair color | Đen pha xám |
| Body type | Rộng, tay chân to, chân vòng kiềng (đứng thuyền) |
| Height impression | ~170 cm, bề ngang lớn, trọng tâm thấp |
| Base outfit | **Giáp da sơn đen lamellar + tấm sắt ngực** (nhẹ để đi thuyền), không váy đùi; **áo choàng dầu sẫm**; **mũ sắt vành rộng thủy quân**; thắt lưng thừng; giày da ngắn |
| Accessories | Ấn đồng chỉ huy; ngọc bội xanh biển; tay sẹo dây thừng |
| Equipment | Chiến thuyền, thuyền đổ bộ, cờ thủy quân |
| Weapon | **Đại đao lưỡi rộng** một lưỡi; giáo |
| Personality | Táo bạo, tham công (lịch sử: tiến quá nhanh để giành công), khinh địch; sau thất bại → rút nhanh, thực dụng |
| Relationship | Độc lập với 우중문 (không phối hợp — thật); bị 고건무 phục kích; báo về Dạng Đế |
| Visual identifiers | (1) mũ vành rộng; (2) áo choàng dầu; (3) sống mũi dẹt; (4) khăn xanh; (5) đại đao |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1–3화 | Không xuất hiện (nhắc: thủy quân đang tới). |
| 4화 | **Đổ bộ**: nước sông bắn ướt, áo choàng dầu bóng; **phục kích**: máu trên đao, khói phố chợ, mũ mất vành móp, chạy về thuyền, áo choàng cháy. |
| 5화 | Không xuất hiện (nhắc: đã rút ra biển). |

**Giọng/ngôn ngữ**
- 하오체 to, thô, khinh; với vua 합쇼체. Gọi Bình Nhưỡng "내 성" trước khi chiếm.
- Câu mẫu: "평양은 비었소. 사만이면 남소." / "시장이 왜 이리 조용한가… 물러나라! 배로!"

**VISUAL_LOCK_EN** (57 từ)
> Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. Chinese man around 50, broad thick-limbed bow-legged build, wide flat-cheeked weathered face, narrow squinting dark eyes, broad nose with flattened bridge, square jaw with short dense black-gray beard, hair wrapped in dark blue head cloth. Black lacquered leather lamellar armor with iron chest plates, oiled dark cloak, wide-brimmed iron naval helmet, rope belt, heavy single-edged broad dao. Dao sheathed at the hip, both hands on the rope belt, short leather boots, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_204_landing_ep4 | 4화 P3–P4 | – | River spray on the oiled cloak and helmet, wet beard, confident grin, dao drawn. |
| CHAR_204_ambush_ep4 | 4화 P5–P8 | ✔ | Blood on the dao blade, smoke smudges, helmet brim dented, cloak scorched at the hem, sweat and panic in the eyes, mid-run. |

---

### CHAR_205 — 탁발흠 (Tuoba Qin) — HƯ CẤU
| Trường | Giá trị |
|---|---|
| ID | CHAR_205 |
| Name | 탁발흠 (Tuoba Qin) |
| Role | 낭장 — đội trưởng trinh sát kỵ binh Tiên Ti; **ENEMY ADAPTATION engine** |
| Age | 38 |
| Gender | Nam |
| Ethnicity | Tiên Ti (탁발, Xianbei — thảo nguyên) |
| Skin tone | Đồng rám, gió mài |
| Face shape | Rộng, **gò má cao rộng**, mặt phẳng mạnh |
| Eyes | Hẹp, **thông minh, điềm tĩnh, hơi giễu**; **nâu hổ phách**; "đọc" người |
| Nose | Thẳng, trung bình, hơi rộng |
| Jaw | Mạnh; **râu dê ngắn sẫm** + ria mảnh |
| Hair style | **Cạo hai bên, tóc sau búi thành 1 bím dày dài xuống lưng** (색두) |
| Hair color | Đen nâu |
| Body type | Chắc, mạnh, dáng kỵ sĩ, hơi vòng kiềng |
| Height impression | ~174 cm; trên ngựa trông cao hơn mọi người |
| Base outfit | **Giáp da cứng lamellar nâu sẫm** xâu gân; **áo felt/len đỏ sẫm viền hoa văn hình học**; quần cưỡi ngựa lót felt; **giày da mềm**; **mũ vành lông cáo có tai che**; thắt lưng miếng đồng hoa văn thú |
| Accessories | **Sẹo dài nhạt từ thái dương trái qua má đến hàm** (cũ); vòng cổ răng sói? — KHÔNG (tránh cliché) → thay bằng **dây da đeo một đầu mũi tên Goguryeo** (chiến lợi phẩm cũ); (2화+) **băng đạn K2C1 rỗng treo thắt lưng**; (3화+) **kính nhìn đêm PVS-11K gắn trên mũ lông** |
| Equipment | Ngựa thảo nguyên (vàng nâu bờm đen), dây thòng lọng, ống tên 30 mũi, dây cung dự phòng; (3화+) K21 thu được, 2 kính đêm, drone cuối + 태오 |
| Weapon | **Cung phức hợp** (chính), **đao chuôi vòng**, giáo ngắn, thòng lọng |
| Personality | Thông minh, kiên nhẫn, tò mò kỹ thuật (nhìn xe "uống nước đen" → hỏa công), không sợ, kính trọng kẻ thù; trung thành với Tùy như chuyên gia — không cuồng tín; hài hước khô; **không xấu xí, không caricature** |
| Relationship | Báo thẳng Dạng Đế; 우문술 là tướng duy nhất nghe ông; **đối thủ cá nhân của 한승우 & 백성민**; bắt và "nghiên cứu" 태오 (đối thoại không lời); 5화 dẫn kỵ Tiên Ti đánh thẳng bãi cạn bờ bắc → phải bị giải quyết |
| Visual identifiers | (1) sẹo mặt; (2) 1 bím dày; (3) mũ lông cáo; (4) cung phức hợp; (5) kính nhìn đêm trên mũ (3화+) |

**Trạng thái theo tập**
| 화 | Trạng thái riêng |
|---|---|
| 1화 | **Sống sót trận đầu**: bụi vàng, máu chảy từ tai trái (sóng nổ), ngựa chết cạnh, mũ lông rơi — tóc bím lộ; sau: quỳ trước Dạng Đế, bụi còn nguyên. |
| 2화 | Đêm hỏa công: bồ hóng, đuốc, mắt sáng; băng đạn rỗng treo thắt lưng (từ đây). |
| 3화 | **Chiếm K21**: đứng trên nóc xe; **kính nhìn đêm gắn trên mũ lông** (từ đây), 2 chiếc — 1 đeo, 1 đưa thuộc hạ; mưa. |
| 4화 | **Săn đêm**: kính đêm hạ xuống mắt, áo choàng ướt, cung trên tay, bùn; sau giao tranh: vết cắt cẳng tay. |
| 5화 | **Xung phong lau sậy**: bùn tới đùi, máu, cung bỏ, đao trên tay, mũ lông mất → bím tóc bay, kính đêm vỡ treo cổ; mưa; kết thúc theo outline. |

**Giọng/ngôn ngữ**
- Với vua: 합쇼체 chuẩn, ngắn; với thuộc hạ: 반말 cộc bằng động từ; phân tích như kỹ sư. Gọi đại đội "뇌군" (ông là người đặt tên), K2 "검은 소", drone "쇠새".
- Câu mẫu: "저들은 손에 천둥을 쥐고 있습니다." (foundation) / "쇠수레는 검은 물을 마십니다. 물을 태우면 됩니다." / "천둥도 셀 수 있습니다. 스물두 번 울렸습니다." / (với 태오, tiếng Hàn để khán giả hiểu) "이 새… 누가 날리나. 너인가."

**VISUAL_LOCK_EN** (59 từ)
> 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow.

**REF_SHEET_PROMPT_EN**
> Character reference sheet, two views on one image against pure white background: left, full-body front view standing straight, arms relaxed at sides; right, close-up of the face at three-quarter angle, neutral expression, looking slightly past camera. 38-year-old Xianbei man, compact rider's build, broad high-cheekboned face, long pale scar from left temple to jaw, narrow steady intelligent amber-brown eyes, straight nose, short dark goatee, sides of head shaved, single thick black braid down the back. Dark brown hardened leather lamellar armor over a dark red felt tunic, fox-fur brimmed cap, bronze plaque belt, composite recurve bow. Cap with ear flaps, soft leather riding boots, bow held in the left hand, ring-pommel saber at the left hip, quiver at the right hip, in the full-body view. Even studio lighting, no cast shadows, no props other than listed, photorealistic, cinematic live-action film still, shot on ARRI Alexa, anamorphic 35mm, shallow depth of field, film grain, pure white background, no text, no watermark, no cartoon, no CGI look

**DERIVED_STATES**
| state_id | Dùng ở | Ref | Prompt bổ sung (EN) |
|---|---|---|---|
| CHAR_205_survivor_ep1 | 1화 P5–P12 | ✔ | Fox-fur cap lost, braid exposed and dusty, yellow dust over armor and face, a line of dried blood from the left ear down the neck, torn tunic sleeve, steady unafraid eyes. |
| CHAR_205_nvg_ep3 | 3화–4화 | ✔ | A modern night-vision monocular device mounted on the front of the fox-fur cap, an empty black rifle magazine hanging from the belt, rain-darkened leather armor, mud on boots. |
| CHAR_205_night_hunt_ep4 | 4화 P6–P9 | ✔ | Night-vision monocular flipped down over the right eye, wet dark cloak over the armor, bow in hand with arrow nocked, mud on the knees, a fresh cut on the right forearm. |
| CHAR_205_final_ep5 | 5화 P7–P10 | ✔ | Cap lost, braid flying loose, mud to the thighs, blood on the saber and tunic, bow discarded, a cracked night-vision device hanging from a cord around the neck, rain, fierce calm face. |

---

## 5. TỔNG HỢP DERIVED_STATES CẦN REF RIÊNG (khớp `ref_jobs.json`)
| # | job id | Tập | Ưu tiên |
|---|---|---|---|
| Base | CHAR_001_ref … CHAR_205_ref (18) | — | P1 |
| 1 | CHAR_001_dusty_ep2 | 2 | P1 |
| 2 | CHAR_001_rain_cloak_ep3 | 3 | P1 |
| 3 | CHAR_001_reeds_ep4 | 4 | P1 |
| 4 | CHAR_001_muddy_bloody_ep5 | 5 | P1 |
| 5 | CHAR_002_soot_ep2 | 2 | P1 |
| 6 | CHAR_002_reeds_ep4 | 4 | P2 |
| 7 | CHAR_002_muddy_bloody_ep5 | 5 | P1 |
| 8 | CHAR_003_soot_ep2 | 2 | P2 |
| 9 | CHAR_003_rain_ep3 | 3 | P1 |
| 10 | CHAR_003_muddy_ep5 | 5 | P2 |
| 11 | CHAR_004_bloody_sleeves_ep2 | 2 | P1 |
| 12 | CHAR_004_braid_ep4 | 4–5 | P1 |
| 13 | CHAR_004_muddy_bloody_ep5 | 5 | P2 |
| 14 | CHAR_005_captive_ep3 | 3–4 | P1 |
| 15 | CHAR_005_goguryeo_helmet_ep5 | 5 | P1 |
| 16 | CHAR_006_facepaint_ep1 | 1–2 | P1 |
| 17 | CHAR_006_night_raid_ep4 | 4 | P1 |
| 18 | CHAR_006_horseback_ep5 | 5 | P2 |
| 19 | CHAR_101_cloak_incognito_ep2 | 2 | P2 |
| 20 | CHAR_101_false_surrender_ep3 | 3 | P1 |
| 21 | CHAR_101_salsu_rain_ep5 | 5 | P1 |
| 22 | CHAR_102_wall_night_ep4 | 4 | P2 |
| 23 | CHAR_103_ambush_ep4 | 4 | P1 |
| 24 | CHAR_104_siege_ep2 | 2 | P1 |
| 25 | CHAR_105_radio_ep3 | 3–4 | P1 |
| 26 | CHAR_105_wounded_ep5 | 5 | P1 |
| 27 | CHAR_106_refugee_ep1 | 1 | P1 |
| 28 | CHAR_106_forge_ep2 | 2–3 | P2 |
| 29 | CHAR_107_refugee_ep1 | 1 | P1 |
| 30 | CHAR_107_scarf_ep2 | 2–5 | P1 |
| 31 | CHAR_107_night_trail_ep4 | 4 | P1 |
| 32 | CHAR_201_robe_only_ep3 | 1/3 | P1 |
| 33 | CHAR_201_defeat_news_ep5 | 5 | P2 |
| 34 | CHAR_202_tent_ep4 | 3–4 | P1 |
| 35 | CHAR_202_defeat_ep5 | 5 | P1 |
| 36 | CHAR_203_retreat_ep5 | 5 | P2 |
| 37 | CHAR_204_ambush_ep4 | 4 | P1 |
| 38 | CHAR_205_survivor_ep1 | 1 | P1 |
| 39 | CHAR_205_nvg_ep3 | 3–4 | P1 |
| 40 | CHAR_205_night_hunt_ep4 | 4 | P1 |
| 41 | CHAR_205_final_ep5 | 5 | P1 |

Tổng: 18 base + 41 biến thể = **59 job**. Chạy: `python3 tools/glabs_client.py batch --jobs projects/SALSU_612/05_references/characters/ref_jobs.json --out projects/SALSU_612/05_references/characters/ --parallel 4`. Gợi ý chạy P1 trước (thêm filter theo trường `priority` nếu cần).

## 6. CHECKLIST QC REF SHEET (trước khi LOCK)
- [ ] 2 view rõ trên 1 ảnh, nền trắng thuần, không bóng đổ, không chữ.
- [ ] Mặt khớp 22 trường (đặc biệt dấu hiệu độc nhất §0.2).
- [ ] 태극기 vai phải nhìn thấy (CHAR_001–006); 계급장 đúng số kim cương/chevron.
- [ ] Không vật lạc thời: Goguryeo/Tùy không có khóa kéo, nút nhựa, đồng hồ; hiện đại không có phù hiệu đơn vị thật.
- [ ] Không giống diễn viên/chính khách/tượng đài (CHAR_101, 102, 201, 202, 203, 204).
- [ ] Biến thể giữ đúng mặt/tóc/vóc của base; chỉ đổi trạng thái.
- [ ] Sau khi user duyệt → cập nhật `continuity_master.json.character_locks` và `derived_states`, đổi header file này thành LOCKED.
