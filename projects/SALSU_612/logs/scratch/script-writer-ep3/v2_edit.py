import re,sys
p='/Users/admin/phim han quoc/projects/SALSU_612/02_script/full_script_ep3.md'
s=open(p,encoding='utf-8').read()
head,body,appx = s[:s.index('## [Phần 1]')], s[s.index('## [Phần 1]'):s.index('\n## 부록')], s[s.index('\n## 부록'):]

# ---------- new N lines (full replacement) ----------
N={
'005':"612년 6월. 요동성 동쪽 골짜기였습니다. 석 달 만에 처음으로, 이 부대는 적이 아니라 자기 것을 태우고 있었습니다.",
'007':"탁발흠은 이틀 전 산으로 꺾어 들어갔습니다. 대군이 아니라 이 부대를 따라왔습니다.",
'014':"한 사람 몫이 세 섬이었습니다. 쌀과 갑옷, 창, 천막, 옷. 황제의 명령은 하나. 군량을 버리는 자는 목을 벤다. 사람들은 다른 방법을 찾았습니다.",
'015':"산길은 수레가 갈 수 있는 유일한 길이었습니다. 하루에 삼십 리. 벌판의 대군은 그 두 배를 갔습니다. 짐은 무거웠고, 매는 더 무서웠습니다.",
'017':"장태오, 스물한 살. 삼 년 전에 대학 시험을 봤습니다. 시험에 나온 시 한 수를 아직 외우고 있었습니다.",
'018':"그 시는 아직 쓰이지 않은 시였습니다. 이 땅의 장군이 한 달 뒤에 적장에게 보낼 시였습니다. 소년은 그 결말을 알았습니다.",
'019':"한승우도 들었습니다. 그는 말하지 않았습니다. 이 싸움은 역사가 이미 이겼다. 문제는 그 역사에 아흔네 명의 자리가 없다는 것이었습니다.",
'020':"벌판의 대군에게도 눈이 있었습니다. 옆구리를 도는 기병이었습니다. 해모루는 그것을 알았습니다. 그래서 삼십 기를 언덕 사이에 두었습니다.",
'021':"싸움은 짧았습니다. 산 쪽 언덕은 고구려 기병의 땅이었습니다. 수나라 기병이 본 것은 먼지뿐이었습니다. 먼지는 보고할 것이 못 되었습니다.",
'022':"총소리는 이십 리를 갑니다. 화살 소리는 백 걸음을 갑니다. 오태민이 첫 번째로 금지당한 날이었습니다.",
'023':"그날 밤 부대는 산등성이에 멈췄습니다. 드론은 띄우지 않았습니다. 드론 한 번은 기름이었습니다. 이십 리 아래, 30만의 불이 있었습니다.",
'028':"장교들은 보았습니다. 보지 않은 척했습니다. 벨 목은 하나였고, 묻는 손은 만 개였습니다. 규율도 그날 밤 천막 밑에 묻혔습니다.",
'029':"요동성에서 을지문덕이 한 말이 있었습니다. 저들은 오래 못 버티오. 한승우는 갑옷 이야기인 줄 알았습니다. 배 이야기였습니다.",
'030':"오태민에게 이것은 기회였습니다. 밥을 버리는 군대는 반은 진 군대였습니다. 마저 치는 것이 병법이었습니다. 그의 병법으로는.",
'033':"사흘째 밤. 골짜기에서 떠난 뒤로 두 밤을 자지 못했습니다. 기지는 이제 움직이는 것이었습니다. 천막 하나, 전차 한 대.",
'034':"장갑차 둘, 트럭 둘, 지휘차 하나. 다섯 대의 기름이 한 대에 들어갔습니다. 그 숫자가 이 부대의 남은 길이었습니다.",
'035':"두 번째 기체의 전지는 그날 밤 불 옆에 있었습니다. 열은 전지를 부풀렸습니다. 드론 넷으로 왔습니다. 이제 하나였습니다.",
'037':"야시경 열둘. 무전기. 태블릿. 전부 한 줄로 이어져 있었습니다. 그 줄의 끝은 기름통이었습니다.",
'039':"골짜기에 남은 장갑차의 바퀴에 쇠못을 박은 사람이 을보였습니다. 그 장갑차가 누구 손에 갈지, 그는 아직 몰랐습니다.",
'040':"을지문덕은 사흘 전에 앞서 떠났습니다. 기병 오백과 함께 더 빠른 길로 갔습니다. 편지는 짧았습니다. 그의 편지는 늘 짧았습니다.",
'041':"하늘 눈. 해모루는 드론을 그렇게 불렀습니다. 을지문덕은 그 눈을 압록수에서 쓰려 했습니다.",
'042':"압록수까지 삼백 킬로. 닷새면 하루 육십 킬로였습니다. 골짜기에서 여기까지 삼십 킬로를 사흘에 왔습니다.",
'043':"고구려 기병은 말에서 내리지 않는 사람들이었습니다. 그날 밤 해모루는 말에서 내렸습니다. 삼백 마리의 말이 아흔네 명에게 갔습니다.",
'045':"사흘 전에 군량을 묻고, 이틀 전에 대열에서 빠졌습니다. 밥 냄새가 나는 쪽으로 왔을 뿐이었습니다.",
'046':"해모루가 소리 내어 웃었습니다. 말이 사람을 가르치는 데는 하루가 걸립니다. 그들에게는 하루가 없었습니다.",
'047':"백성민은 강원도 산골 사냥꾼의 아들이었습니다. 말은 그의 손을 알아보았습니다. 그날부터 해모루는 그를 이름으로 불렀습니다.",
'048':"소달구지는 하루 육십 킬로를 못 갑니다. 그래서 짐은 전차 등에 올라갔습니다. 55톤이 짐말이 되었습니다.",
'049':"닷새였습니다. 하루 육십 킬로. 밤에도 갔습니다. 고구려 기병이 자기 말을 남에게 내주고 걷는 것을, 이 땅의 역사는 본 적이 없었습니다.",
'052':"그날 아침 을지문덕은 갑옷을 벗었습니다. 비단옷과 조우관. 칼도 없었습니다. 항복할 생각은 없었습니다. 볼 생각이었습니다.",
'054':"압록수에 이르렀을 때, 백 일치 군량은 거의 남아 있지 않았습니다. 남은 것마저 강가에 묻었습니다. 강을 건너려면 몸이 가벼워야 했습니다.",
'056':"계획은 하나였습니다. 장군이 붙잡히면 전차가 정문에 네 발. 한승우는 쓰고 싶지 않았습니다.",
'059':"우중문. 아홉 군을 이끄는 두 총사령 중 하나. 황제는 결정을 그에게 맡겼습니다. 그의 품에는 밀지가 있었습니다. 을지문덕이 오면 붙잡으라.",
'060':"을지문덕은 한문을 읽고 썼습니다. 말은 해모루가 옮겼습니다. 적장 앞에서 그는 한 마디도 소리 내지 않을 작정이었습니다.",
'061':"필담이었습니다. 붓으로 하는 대화. 왕은 성에 계시다. 신이 대신 왔다. 항복이라는 글자는 쓰지 않았습니다. 옷이 대신 말했습니다.",
'063':"위무사 유사룡. 황제가 항복을 받으라고 보낸 문관이었습니다. 그 한 마디가 30만 5천 명의 운명을 갈랐습니다.",
'064':"을지문덕은 풀려났습니다. 병영에 있었던 시간은 차 한 잔 식을 시간이었습니다. 그 시간에 그는 필요한 것을 다 보았습니다.",
'066':"문이 닫히자 우중문은 후회했습니다. 밀지는 밀지였습니다. 그는 사람을 보냈습니다. 이것도 역사책 그대로입니다.",
'067':"뒤에서 부르는 소리가 났습니다. 돌아보는 순간, 항복하러 온 사람은 도망치는 사람이 됩니다. 그는 끝까지 항복하러 온 사람이었습니다.",
'070':"육십 발이 물에 들어갔습니다. 수나라 기병은 총을 몰랐습니다. 그러나 천둥이라는 말은 알았습니다. 뇌군이 강 건너에 있다고, 그들은 그날 저녁 보고했습니다.",
'076':"이튿날 아침. 두 총사령이 마주 앉았습니다. 우문술은 셈을 하는 사람이었습니다. 군량은 열흘 치도 남지 않았습니다.",
'077':"우중문의 셈에는 황제가 있었습니다. 이 말은 수서에 그대로 남아 있습니다.",
'078':"우문술은 물러섰습니다. 우중문에게는 이유가 하나 더 있었습니다. 황제가 찾는 천둥이 강 건너에 있었습니다. 아홉 군은 군량 없이 강을 건너기로 했습니다.",
'079':"선봉은 하루 만에 건넜습니다. 아홉 군이 다 건너는 데는 사흘이 걸렸습니다. 가슴까지 오는 물이었습니다. 건너는 동안 아무도 막지 않았습니다. 을지문덕이 막지 말라고 했기 때문입니다. 이 결정이 살수까지 가는 첫걸음이었습니다.",
'080':"그날 오후 을지문덕은 첫 번째 싸움을 짰습니다. 이기는 싸움이 아니었습니다. 잘 지는 싸움이었습니다.",
'082':"박격포탄은 육십 발이었습니다. 요동성에서 쉰 발을 썼습니다. 열 발이면 지는 싸움을 진짜처럼 보이게 할 수 있었습니다.",
'094':"적은 배웠습니다. 열 발이 떨어진 자리를 피해 옆으로 퍼졌습니다. 박격포는 이제 쉰 발이었습니다. 배우는 적을 상대로, 쉰 발은 많지 않았습니다.",
'097':"탁발흠이었습니다. 골짜기에서 타지 않은 장갑차를 그가 가져갔습니다. 소 마흔 마리, 하루 팔십 리. 그는 부대를 쫓지 않았습니다. 뇌군은 어차피 압록수로 올 것이었습니다.",
'098':"박기철은 아무 말도 하지 않았습니다. 그가 뗀 명판은 등에 있었습니다. 명판 없는 장갑차 안에는 40밀리 포탄 예순 발이 그대로 있었습니다.",
'099':"첫 번째 패배였습니다. 앞으로 더 여러 번 질 것이었습니다. 을지문덕은 만족한 얼굴이 아니었습니다. 세는 얼굴이었습니다.",
'101':"쇠수레는 소를 따라갔습니다. 하루에 팔십 리. 팔십 리씩, 그것은 황제의 것이 되어 가고 있었습니다.",
'104':"살수. 오늘날의 청천강입니다. 평양에서 북쪽으로 팔십 킬로. 그 자리는 이 부대의 마지막 자리가 될 것이었습니다. 아직 아무도 몰랐습니다.",
'107':"세 번째였습니다. 산길에서 한 번, 압록수에서 한 번. 세 번 다 틀린 말은 아니었습니다. 때가 틀렸을 뿐이었습니다.",
'108':"을지문덕의 셈은 이랬습니다. 굶는 군대는 이기면 더 깊이 들어옵니다. 지면 돌아갑니다. 돌아가면 다시 옵니다.",
'109':"산성 아래 길에 수나라 척후가 있었습니다. 백성민이 나갔습니다. 해모루의 기병 둘이 따랐습니다. 말을 바꿔 탄 날부터 둘은 말 없이도 통했습니다.",
'110':"해모루도 다 알지 못했습니다. 을지문덕은 부하에게도 계책을 나누어 주지 않았습니다. 새는 것은 사람이었기 때문입니다.",
'112':"무전기 하나가 고구려 갑옷에 달렸습니다. 그날부터 이 무전기는 두 시대를 잇는 줄이었습니다. 닿는 거리는 십 킬로. 산이 막으면 그보다 짧았습니다.",
'113':"을지문덕은 묻지 않았습니다. 그는 그것도 셌습니다. 말하는 돌 하나, 십 킬로. 그의 판에 말이 하나 더 놓였습니다.",
'114':"그날 밤 그는 편지를 썼습니다. 받는 사람은 평양의 대왕이었습니다. 적은 굶는다. 적은 건넜다. 신은 살수로 간다. 왕에게도 계책의 전부는 적지 않았습니다.",
'116':"총은 쓰지 않았습니다. 총소리는 산성을 알립니다. 화살은 알리지 않습니다. 이것도 산길에서 배운 것이었습니다.",
'117':"남쪽. 그 말이 그날 밤 모두의 머리에 박혔습니다. 위험은 남쪽에서 올 것이었습니다. 그것은 반만 맞는 생각이었습니다.",
'118':"을보는 쇠를 손으로 읽는 사람이었습니다. 그날 밤 그가 읽은 것을, 박기철은 이튿날 계기판에서 읽었습니다.",
'119':"항생제는 요동성에서 끝났습니다. 이제 약은 을보가 달인 물이었습니다. 스물네 살 의무병이 이 땅의 약초를 배우고 있었습니다.",
'121':"갈대밭에는 갈대를 베는 사람만 아는 길이 있습니다. 그 길이 다음 이야기에서 사람 하나를 살릴 것이었습니다.",
'123':"한승우는 대답을 갖고 있지 않았습니다. 없는 것을 있는 척하지 않았습니다. 그것이 아흔네 명을 여기까지 데려온 방식이었습니다.",
'126':"강을 건넌 날 밤, 강 북쪽. 탁발흠은 쇠수레 안으로 들어갔습니다. 열흘 동안 그는 겉만 보았습니다. 이제 속을 볼 차례였습니다.",
'127':"안에는 40밀리 포탄 예순 발이 남아 있었습니다. 그는 그것이 무엇인지 몰랐습니다. 모르는 것은 건드리지 않는다. 그것이 그가 살아남은 방식이었습니다.",
'128':"그는 산을 알았습니다. 쇠수레는 논을 못 갑니다. 나무다리를 못 건넙니다. 산을 못 넘습니다. 남쪽 길은 요동성 앞에서 잡은 농부에게 미리 물어 두었습니다. 압록수 남쪽에서 쇠수레가 갈 길은 하나뿐이었습니다. 석문령. 돌문 고개였습니다.",
'129':"수나라 총관은 뇌군이 어디로 갔는지 물었습니다. 탁발흠은 지도를 보지 않았습니다. 쇠수레를 보았습니다.",
'130':"요동성 골짜기 위에서 열이틀을 본 것이었습니다. 쇠새는 수레 등에서 밥을 먹었습니다.",
'131':"요하에서 그의 말들은 천둥소리에 미쳤습니다. 세 번째는 없어야 했습니다. 귀를 막은 말은 천둥을 듣지 못합니다. 듣지 못하는 말은 달립니다.",
'132':"닷새 전, 요동성 앞 육합성. 넉 달째였습니다. 황제의 손에는 부서진 쇠새가 있었습니다. 그는 온전한 것을 원했습니다.",
'133':"명령은 삼백 킬로를 닷새에 왔습니다. 산 채로. 죽이면 천둥은 없어집니다. 탁발흠에게 이천 기가 주어졌습니다. 이번에는 사람을 노릴 생각이었습니다.",
'134':"을보가 땀이라 부른 것은 냉각수였습니다. 오르막에서 새는 것이 터졌습니다. 55톤은 물이 없으면 달리지 못합니다.",
'136':"요동성에서 을보는 쇠는 쇠요, 라고 말했습니다. 그때는 바퀴였습니다. 이번에는 물길이었습니다.",
'137':"대열 뒤로 수나라 척후가 붙었습니다. 해모루가 처음으로 말하는 돌을 썼습니다. 돌은 속삭여도 들립니다.",
'138':"척후는 돌아갔습니다. 돌아간 척후는 보고를 합니다. 쇠수레가 고개 밑에 섰다. 그 보고는 그날 저녁 탁발흠에게 닿았습니다.",
'139':"척후 둘이 남아 있었습니다. 그들은 요동성에서 배운 것을 썼습니다. 쇠수레는 탄다. 열다섯 살 소녀가 그 불을 껐습니다. 요동성에서 의무병이 준 수건으로.",
'140':"고개 밑에 마을이 있었습니다. 열다섯 집. 마을 사람들은 도망치지 않았습니다. 삼족오 깃발이 같이 왔기 때문입니다.",
'141':"마을 위가 석문령이었습니다. 두 벼랑 사이의 안장 같은 고개. 남쪽으로 가는 수레 길은 그 고개뿐이었습니다. 이틀. 쇠수레는 그 밑에서 이틀을 서 있어야 했습니다.",
'142':"7세기의 대장간이 21세기의 물길을 고치고 있었습니다. 구리 관을 만들어 끼우고, 송진을 먹인 가죽끈으로 조일 것이었습니다. 을보의 손은 빨랐습니다.",
'143':"전차가 서 있는 동안 보조동력은 돌았습니다. 탁발흠이 요동성 골짜기에서 본 것이 바로 이것이었습니다.",
'144':"수나라 대열은 이틀 뒤에 있었습니다. 소가 끄는 쇠수레는 강 북쪽에 남았습니다. 고치는 데 이틀. 오는 데 이틀.",
'145':"북서쪽 염소 길. 사람 하나가 겨우 지나는 길이었습니다. 거기에 말똥이 있었습니다.",
'146':"그는 물었습니다. 답이 반만 맞았을 뿐입니다.",
'147':"해모루는 셋을 보냈습니다. 그래서 말똥은 해모루의 것이었습니다. 백성민은 그렇게 결론을 내렸습니다. 그것만은 아니었습니다.",
'148':"서 있어도 기름은 줄었습니다. 보조동력은 낮에도 밤에도 돌았습니다. 이틀치 전기를 박기철은 거리로 바꿔 적었습니다.",
'149':"척후의 보고는 정확했습니다. 탁발흠은 직접 보러 왔습니다. 그가 본 것은 서 있는 쇠수레와 꺼지지 않는 대장간 연기였습니다.",
'152':"저녁에 수나라 척후가 마을 밭에 들어왔습니다. 정찰이 아니었습니다. 밥이었습니다.",
'153':"총소리가 골짜기에 울렸습니다. 숨길 것은 이미 없었습니다. 척후는 이미 쇠수레를 보았습니다.",
'154':"자루는 반도 차지 않았습니다. 익지도 않은 조였습니다. 오태민은 처음으로 적을 불쌍하다고 생각했습니다.",
'155':"선택은 둘이었습니다. 전차를 고친다. 그러면 뒤가 따라잡습니다. 전차를 버린다. 그러면 살수에 제때 닿습니다. 둘 다 맞는 답이었습니다.",
'157':"박기철의 답은 숫자였습니다. 아흔 자루. 전차 한 대가 그 숫자를 다른 것으로 만들었습니다.",
'158':"세 사람이 말하는 동안 네 번째 사람은 두드렸습니다. 쇠는 기다리는 사람의 것이 아니었습니다.",
'159':"갈대밭 북쪽 여울. 을지문덕은 사람을 부르지 않았습니다. 쇠수레를 불렀습니다. 이유는 무게였습니다.",
'160':"두 번째 결정이었습니다. 요동 벌판에서 그는 쏘기로 했습니다. 여기서 그는 고치기로 했습니다. 두 번째 값은 첫 번째보다 비쌌습니다.",
'161':"밤에 넘으려면 야시경이, 야시경에는 전기가, 전기에는 서 있는 전차가 필요했습니다. 하나가 하나를 끌고 왔습니다.",
'162':"드론 하나. 한승우가 허락한 충전은 한 번. 나머지 기름은 살수까지의 길이었습니다.",
'165':"병사들은 고구려의 구들 위에서 잤습니다. 천사백 년 뒤에도 이 땅 사람들은 같은 방식으로 방을 데울 것이었습니다.",
'167':"예순여섯 살과 마흔두 살. 한 사람은 쇠를 두드리고, 한 사람은 불을 비췄습니다. 쇠쟁이들에게 말은 필요 없었습니다.",
'168':"백성민은 새벽마다 동쪽 길로 소년을 보냈습니다. 남쪽은 해모루가, 북쪽은 대열이 이틀 뒤. 네 번째 방향은 길이 아니었습니다.",
'170':"해모루의 척후 셋이 염소 길을 내려왔습니다. 위에는 아무도 없었다고, 그들은 믿었습니다. 그들 머리 위에 활 서른 개가 있었습니다. 탁발흠은 손을 내렸습니다.",
'171':"죽은 척후는 돌아가지 않습니다. 돌아가지 않는 척후는 의심을 남깁니다. 쇠수레가 일어나는 밤, 그는 이 길로 내려갈 것이었습니다.",
'174':"시동을 걸었습니다. 흰 연기는 나지 않았습니다. 그 55톤이 이제 고개를 넘어야 했습니다.",
'175':"석문령. 안장처럼 좁은 고개. 양쪽은 삼십에서 육십 미터 벼랑. 남쪽으로 내려가는 길, 동쪽에서 올라오는 길. 북서쪽 벼랑에 염소 길. 동남쪽에 이백 미터 바위.",
'176':"계획은 밤이었습니다. 낮에 넘으면 벼랑 위에서 다 보입니다. 밤에는 야시경을 가진 쪽만 봅니다.",
'177':"화살은 해모루의 척후라는 뜻이었습니다. 척후 셋은 아무도 없다고 했습니다. 그 화살은 그날 밤 잘못 꽂힌 유일한 것이었습니다.",
'178':"같은 새벽, 동쪽 길. 소년 척후가 선비 기병 둘을 만났습니다. 화살 둘. 하나는 안장에 박혔습니다. 소년은 돌아서 달렸습니다.",
'179':"남쪽 입구는 해모루의 삼백이 맡았습니다. 적이 온 곳에서 적이 옵니다. 대개는 그렇습니다.",
'180':"마지막 비행이었습니다. 전지 열네 분 중 십 분. 그 십 분 동안 고개 전체가 보일 것이었습니다.",
'181':"드론과 조종기 사이에는 보이지 않는 줄이 있습니다. 그 줄은 바위에 막힙니다. 높은 곳에 서면 줄이 이어집니다.",
'182':"그동안 전차는 시동을 끄고 보조동력만 돌립니다. 열과 소리를 숨기기 위해서였습니다. 포탑은 줄에 묶입니다.",
'183':"줄에 묶인 전차는 쏘지 못합니다. 줄을 뽑는 데 시간이 걸립니다. 박기철은 그 시간을 알았습니다.",
'185':"전차 옆. 가장 큰 것을 지키는 자리였습니다. 오태민에게는 물러나는 것이었고, 한승우에게는 가장 무거운 것을 맡기는 것이었습니다.",
'186':"야시경은 백성민과 앞에. 장태오는 바위 위에, K3 사수와 소총수 둘이 같이. 해모루는 남쪽. 전차는 맨 뒤. 마흔 분. 모든 눈이 남쪽을 보고 있었습니다.",
'187':"해모루는 정오에 먼저 고개를 넘어 남쪽 입구에 섰습니다. 거기서 수나라 척후 다섯을 만났습니다. 또 남쪽이었습니다.",
'188':"해모루는 이제 돌에 속삭였습니다. 그의 보고는 정확했습니다. 정확한 보고가 틀린 결론을 굳혔습니다.",
'189':"동쪽 길에 척후 둘. 안장에 박힌 화살이 증거였습니다. 백성민은 그것을 뒤따르는 대열의 척후로 읽었습니다. 북서쪽만 비어 있었습니다.",
'191':"신호는 높아야 잡힙니다. 높은 곳은 멀고, 먼 곳은 위험합니다. 드론 하나를 살리는 자리가 사람 하나를 가장 먼 곳에 두었습니다.",
'192':"어깨의 태극기가 떨어지려 하고 있었습니다. 윤서아가 세 바늘로 꿰맸습니다. 그 세 바늘은 하루를 버틸 것이었습니다.",
'194':"열다섯 살에게 스물한 살은 그런 사람이었습니다.",
'195':"구리는 뜨거웠습니다. 새지 않았습니다. 을보가 믿는 것은 손이었습니다.",
'199':"전차는 잠들었습니다. 열도 소리도 숨겼습니다. 보조동력만 깨어 있었습니다. 지금부터 마흔 분.",
'200':"21세기의 줄이 7세기의 돌담 위를 지나갔습니다. 야시경, 무전기. 모두 한 통에서 밥을 먹었습니다.",
'201':"이백 미터. 넷이 올라갔습니다. 조종병 하나, K3 사수 하나, 소총수 둘. 위에서 보면 고개 전체가 손바닥 같을 것이었습니다.",
'202':"마지막 비행이 시작되었습니다. 열네 분 중 십 분. 고개는 조용했습니다.",
'212':"횃불을 쏘면 횃불이 꺼졌습니다. 꺼진 횃불 밑에서 말은 계속 왔습니다. 야시경을 가진 사람은 셋이었습니다. 나머지는 빛을 쏘았습니다.",
'215':"이 분. 야시경 일곱 개가 아직 밥을 먹고 있었습니다. 그날 밤 가장 비싼 이 분이었습니다.",
'240':"동쪽 문은 선비 기병 이백이 막고 있었습니다. 개마무사 삼백이 그 이백을 옆에서 쳤습니다. 이 땅의 기병이 이 땅의 고개를 열었습니다.",
'251':"이름은 여기 적지 않습니다. 스물세 살. 강원도 어느 마을의 아들이었습니다. 그는 이 땅에 묻힌 첫 번째 사람이었습니다. 이 땅은 그때도 이 땅이었습니다.",
'256':"고개 밑에서 해모루는 갈라졌습니다. 그는 을지문덕에게 돌아가야 했습니다. 지는 싸움이 기다리고 있었습니다. 말하는 돌은 십 킬로까지 닿았습니다. 십 킬로 뒤에 그는 다시 혼자였습니다.",
'257':"탁발흠은 밤눈을 손에 넣었습니다. 하나는 조종병의 것, 하나는 사수의 것. 석문령에서 그는 밤을 배웠습니다. 밤눈도 밥을 먹는다는 것을, 그는 아직 몰랐습니다.",
'260':"탁발흠은 말을 걸 수 없었습니다. 말이 달랐습니다. 고구려 말은 이상하게도 이 젊은이에게 통했습니다. 그것을 그는 요동성에서부터 보아 왔습니다.",
'262':"어깨의 깃발이 뜯겼습니다. 어제 세 바늘로 꿰맨 깃발이었습니다. 그는 요동성에서 빈 탄창을 허리에 찼습니다. 이번에는 깃발이었습니다. 그것은 마지막 강까지 그의 품에 있을 것이었습니다.",
'263':"황제의 명은 산 채로였습니다. 쇠수레와 쇠새는 서쪽으로, 이백 기가 호송할 것이었습니다. 밤눈과 포로는 미끼였고, 눈이었습니다.",
'264':"장갑차는 서쪽으로 돌아섰습니다. 요동성까지 삼백 킬로, 하루 팔십 리. 열흘이 넘는 길이었습니다. 그 뒤에는 낙양까지 더 먼 길이 있었습니다.",
'268':"아홉 군이 남쪽으로 갔습니다. 을지문덕은 그들 앞에서 지기 시작했습니다. 이기는 군대는 멈추지 않습니다. 굶어도 멈추지 않습니다.",
'274':"말하는 돌이 살아났습니다. 십 킬로 안이었습니다.",
'279':"한승우는 강을 오래 보았습니다. 요동 벌판에서는 쏘기로, 고개 밑에서는 고치기로 했습니다. 이번에는 아무것도 하지 않아야 했습니다. 그것이 가장 어려운 결정이었습니다.",
}
# ---------- dialogue replacements (sid -> (old_line, new_line)) ----------
D={
'007':("백성민: 산길에 횃불. 선비 기병. 열 분 안에 옵니다.","백성민: 지휘, 여기는 수색. 산길에 횃불. 선비 기병. 열 분 안에 옵니다."),
'066':("우중문: 사람을 보내시오. 더 할 말이 있다 하시오.","우중문: 사람을 보내라. 더 할 말이 있다 하라."),
'111':("한승우: 이걸로 부르시오.","한승우: 이걸로 부르십시오."),
'162':("장태오: 드론 하나. 충전 한 번 남았습니다. 야시경 배터리 40%.","장태오: 드론 하나. 허락된 충전 한 번. 야시경 배터리 40%."),
'174':("박기철: 새지 않습니다. 갑니다.","박기철: 새지 않습니다. 드럼은 비웠습니다. 갑니다."),
'183':("박기철: 마흔 분. 그 사이 전차는 잠듭니다.","박기철: 마흔 분. 그 사이 전차는 줄에 묶입니다."),
'215':("박기철: 충전 중입니다! 이 분!","박기철: 충전 중입니다! 줄 뽑는 데 이 분!"),
}
# ---------- [ACTION]/[SOUND]/header replacements (substring, must be unique in body) ----------
R=[
# SC_003 박기철 reaction off-screen
("[SOUND] lửa cháy, rồi tiếng phóng PZF \"펑\" khô, tiếng nổ dội vách.\n","[SOUND] lửa cháy, rồi tiếng phóng PZF \"펑\" khô, tiếng nổ dội vách; giọng 박기철 off-screen, khàn.\n박기철: 두 발…\n"),
# SC_010 2-BEAT
("[ACTION-VI] K2 bò ra khỏi thung lũng, can dầu và một phuy 200 L buộc dây trên đuôi tháp, cành thông phủ nóc; hàng lính đi bộ hai bên, 을보 chống gậy, 아리 quàng khăn olive nắm tay áo ông; kỵ Goguryeo của 해모루 chờ ở cửa thung. Hai mũi tên từ bóng tối sườn tây cắm \"픽, 픽\" vào bùn sau gót người cuối hàng; lính cuối quay lại bắn một loạt ngắn lên sườn núi rồi chạy tiếp.",
 "[ACTION-VI] 2-BEAT: (a) 1:14–1:18 K2 bò ra khỏi thung lũng, can dầu và một phuy 200 L buộc dây trên đuôi tháp, cành thông phủ nóc; hàng lính đi bộ hai bên, 을보 chống gậy, 아리 quàng khăn olive nắm tay áo ông; kỵ Goguryeo của 해모루 chờ ở cửa thung; (b) 1:18–1:22 cận gót người cuối hàng: hai mũi tên từ bóng tối sườn tây cắm \"픽, 픽\" vào bùn; anh ta quay lại bắn một loạt ngắn lên sườn núi rồi chạy tiếp."),
# SC_015 wounded
("을보 chống gậy, cuộn dụng cụ trên lưng; 아리 khăn olive ướt, bím tóc dính má; sau họ hai xe bò",
 "hai lính băng kín tay (bỏng 2화) đi giữa hàng, súng do người khác vác; 을보 chống gậy, cuộn dụng cụ trên lưng; 아리 khăn olive ướt, bím tóc dính má; sau họ hai xe bò"),
# SC_022 cười → gật
("해모루 phi lên gờ, vệt máu trên lưỡi đao, cười khẽ, quay ngựa đi không nói.","해모루 phi lên gờ, vệt máu trên lưỡi đao, gật một cái, quay ngựa đi không nói."),
# SC_054 chôn bên bờ
("[ACTION-VI] Màn hình drone (góc cao, mưa lấm ống kính): bờ tây — hàng lính Tùy đứng ở mép nước ném bao gai xuống sông; bao nổi rồi chìm; kê vàng loang trên mặt nước xanh; phía sau, trại lều xiêu vẹo kéo dài đến khuất trong mưa. Ngón tay 태오 run trên cần.",
 "[ACTION-VI] Màn hình drone (góc cao, mưa lấm ống kính): bờ bắc — dọc mép trại, hàng trăm lính Tùy đào hố nông trong bùn, hạ bao gai xuống, lấp đất, dẫm lên; kê vàng vãi quanh miệng hố; phía sau, trại lều xiêu vẹo kéo dài đến khuất trong mưa. Ngón tay 태오 run trên cần."),
# SC_057 faces
("giữa lối, 을지문덕 áo lụa đi chậm, hai tay buông, đầu hơi nghiêng nhìn từng mặt; 해모루 nửa bước sau, cờ trắng. Ken-burns trượt theo hàng mặt lính.",
 "giữa lối, 을지문덕 áo lụa đi chậm, hai tay buông, đầu hơi nghiêng nhìn từng mặt; 해모루 nửa bước sau, cờ trắng. Trung cảnh: chỉ 2–3 khuôn mặt lính gần ông nét, hàng sau mờ. Ken-burns đẩy chậm theo bước ông."),
# SC_103 quân cờ
("을지문덕 nói không ngẩng lên khỏi bản đồ — lệnh, không phải thảo luận.","을지문덕 nói không ngẩng lên khỏi bản đồ — lệnh, không phải thảo luận; khi nói, ông đặt một quân cờ gỗ đen lên vạch sông ở 살수."),
# SC_107 (오태민) walk-in
("[ACTION-VI] 오태민 bước một bước lên từ cửa lều, giọng to hơn cần thiết; 해모루 quay đầu nhìn ông; 한승우 không cản.",
 "[ACTION-VI] Walk-in: 오태민 từ cửa lều bước thẳng tới rương bản đồ, ngón tay ấn xuống vạch cột quân Tùy phía bắc, giọng to hơn cần thiết; 해모루 quay đầu nhìn ông; 한승우 không cản."),
# SC_113 second piece
("[ACTION-VI] 을지문덕 ngẩng lên đúng lúc radio kêu; nhìn khối olive trên giáp 해모루 — không hỏi nó là gì; nhìn 한승우 — rồi cúi lại bản đồ. Máy đẩy nhẹ.",
 "[ACTION-VI] 을지문덕 ngẩng lên đúng lúc radio kêu; nhìn khối olive trên giáp 해모루 — không hỏi nó là gì; nhìn 한승우 — rồi cúi lại bản đồ, đặt quân cờ đen thứ hai sát cạnh quân đầu ở 살수. Máy đẩy nhẹ."),
# SC_112 cut xoay
("[ACTION-VI] 해모루 cầm radio, xoay trong tay, đưa lên tai như vỏ ốc;","[ACTION-VI] 해모루 cầm radio, đưa lên tai như vỏ ốc;"),
# SC_124 KB fade note
("Ảnh: lều vải gai có cờ 삼족오 ướt trong mưa đêm, ánh đèn dầu vàng hắt qua vải — rồi (ken-burns kết hợp fade) đèn tắt, lều thành khối đen. Ken-burns đẩy chậm vào cửa lều.",
 "Ảnh: lều vải gai có cờ 삼족오 ướt trong mưa đêm, ánh đèn dầu vàng hắt qua vải — rồi đèn tắt, lều thành khối đen (veo-stage: 2 still 5 s sáng → tắt, hoặc 1 video8s). Ken-burns đẩy chậm vào cửa lều."),
# SC_130 ACTION
("[ACTION-VI] 탁발흠 ngẩng lên, nhìn về phía nam qua sông — nơi hắn đã đứng quan sát ba ngày; hắn nói câu thứ hai chậm hơn, như đọc lại điều đã ghi trong đầu. Sĩ quan Tùy không hiểu; 부장 của hắn hiểu.",
 "[ACTION-VI] 탁발흠 ngẩng lên, nhìn về phía tây — nơi 요동성, nơi hắn đã nằm 12 ngày trên sườn núi nhìn xuống thung lũng xe sắt; hắn nói câu thứ hai chậm hơn, như đọc lại điều đã ghi trong đầu. Sĩ quan Tùy không hiểu; 부장 của hắn hiểu."),
# SC_139 2-BEAT
("[ACTION-VI] K2 lết đoạn cuối lên làng, hơi nước phụt; từ gờ đá bên trên đường, hai kỵ Tùy 척후 còn sót (tách khỏi toán bị đuổi) bắn hai mũi tên quấn vải cháy xuống — một mũi cắm vào cành thông phủ nóc K2, lửa bén nhựa thông; 아리 trên đuôi xe giật khăn olive khỏi cổ đập lửa liên tiếp, 을보 quát; lính đi bên xe bắn một loạt lên gờ — một bóng ngã, bóng kia biến mất. Khăn 아리 cháy sém một góc.\n[SOUND] tên lửa rít, lửa bén cành, khăn đập, K2C1 loạt ngắn, quát.",
 "[ACTION-VI] 2-BEAT: (a) 19:16–19:20 low-angle từ đường: hai mũi tên quấn vải cháy rít xuống từ gờ đá bên trên (2 척후 Tùy còn sót), một mũi cắm vào cành thông phủ nóc K2 đang lết lên dốc, nhựa thông bén lửa; (b) 19:20–19:24 cận đuôi xe: 아리 giật khăn olive khỏi cổ đập lửa liên tiếp, 을보 quát; khăn cháy sém một góc, lửa tắt.\n[SOUND] tên lửa rít, lửa bén cành, khăn đập, quát; off-screen: K2C1 loạt ngắn lên gờ, một tiếng ngã."),
# SC_143 NVG instead of drone
("[ACTION-VI] 태오 cắm dây sạc pin drone vào ổ đuôi K2; APU rì rì sau tháp dù động cơ chính tắt; cậu ngồi xổm nhìn đèn sạc đỏ, nói với 박기철 đi ngang (chỉ thấy chân).",
 "[ACTION-VI] 태오 cắm dây sạc một hàng pin kính đêm vào ổ đuôi K2; hộp drone đóng nắp bên cạnh — không sạc; APU rì rì sau tháp dù động cơ chính tắt; cậu ngồi xổm nhìn đèn sạc đỏ, nói với 박기철 đi ngang (chỉ thấy chân)."),
# SC_149 what he sees
("hắn nhìn xuống thung lũng — làng nhỏ, một chấm sẫm cạnh kho thóc, sợi khói trắng mỏng bốc lên từ chấm đó. Hắn nheo mắt.",
 "hắn nhìn xuống thung lũng — làng nhỏ, một chấm sẫm bất động cạnh kho thóc, và sợi khói lò rèn bốc lên không dứt từ mái che bên suối. Hắn nheo mắt."),
# SC_160/161 already walk-and-talk
# SC_170 direction
("[ACTION-VI] Đường dê trong sương đêm: ba 척후 Goguryeo của 해모루 dắt ngựa đi chậm lên dốc, cung cầm tay, nhìn quanh; máy ngước lên:",
 "[ACTION-VI] Đường dê trong sương đêm: ba 척후 Goguryeo của 해모루 dắt ngựa đi xuống dốc trên đường về, cung đeo lưng, thở phào; máy ngước lên:"),
# SC_173 drum + leather
("bên trong một đoạn ống bọc bằng tấm đồng đỏ gò cong, đóng chốt sắt, mép trám nhựa thông đen; bàn tay băng của 박기철 và bàn tay già của 을보 cùng đặt trên đó; 을보 dốc bát nước lên mối nối — không rỉ. Ken-burns đẩy vào mối đồng.",
 "bên trong một đoạn ống đồng đỏ gò cong lồng vào ống cũ, quấn dây da tẩm nhựa thông đen siết chặt; bàn tay băng của 박기철 và bàn tay già của 을보 cùng đặt trên đó; 을보 dốc bát nước lên mối nối — không rỉ; góc khung: phuy 200 L rỗng nằm nghiêng cạnh lò rèn. Ken-burns đẩy vào mối đồng."),
# SC_178 new content (replace whole ACTION/SOUND of insert)
("### SC_178 · LOC_009_SEOKMUN_PASS (gờ núi tây-bắc trên làng, ngày — insert địch) · 2 척후 Tiên Ti · VEH_206 · video8s · 24:44–24:52\n[ACTION-VI] Insert: trên gờ đá tây-bắc trong mây, hai kỵ Tiên Ti nằm rạp không ngựa, mũ lông ướt, nhìn xuống làng — nhỏ xíu dưới xa: đám người quanh tấm ván bàn cát, K2 cạnh kho thóc, khói lò rèn đã tắt; một tên đếm bằng ngón tay, tên kia bò lùi vào sương. Không thoại.\n[SOUND] gió trên cao, sương; xa xa tiếng nói trầm từ làng.",
 "### SC_178 · LOC_009_SEOKMUN_PASS (đường xe phía đông dưới đèo, rạng sáng D14) · 소년 척후, 2 척후 Tiên Ti · VEH_101, VEH_206, WPN_101 · video8s · 24:44–24:52\n[ACTION-VI] 2-BEAT: (a) 24:44–24:48 소년 척후 phi chậm trên đường xe phía đông trong sương sớm; từ rừng thông bên đường, hai kỵ Tiên Ti mũ lông lao ra; (b) 24:48–24:52 hai mũi tên — một rít qua tai, một cắm \"턱\" vào yên ngựa sau đùi cậu; cậu rạp người xuống cổ ngựa, quay đầu phi ngược về làng, mất hút trong sương. Không thoại.\n[SOUND] vó ngựa, dây cung, tên cắm gỗ yên, tiếng hú ngắn."),
# SC_180 screen 14
("[ACTION-VI] 태오 đặt hộp drone xuống cạnh bàn cát, mở nắp: chiếc cuối, pin đã sạc đầy đèn xanh; cậu giơ một ngón tay — một lần bay.",
 "[ACTION-VI] 태오 đặt hộp drone xuống cạnh bàn cát, mở nắp: chiếc cuối; cậu bật controller — màn hình pin: 14; cậu giơ một ngón tay — một lần bay."),
# SC_183 at K2 already
# SC_189 boy returns
("[ACTION-VI] 한승우 nghe radio, nhìn 백성민; 백성민 gật; 한승우 nói hai chữ rồi ra hiệu đoàn chuẩn bị; sau lưng, lính đang chằng đồ lên K2, 을보 kiểm tra dây.",
 "[ACTION-VI] 소년 척후 phi vào sân, ngựa sùi bọt, xoay yên cho 백성민 xem mũi tên cắm ở yên, giơ hai ngón tay chỉ về đông; 백성민 rút mũi tên, nhìn, gật với 한승우 — kỵ Tiên Ti đi theo đại quân, cột quân ở phía bắc-đông; 한승우 vừa nghe xong radio 해모루, nói hai chữ rồi ra hiệu đoàn chuẩn bị; sau lưng, lính chằng đồ lên K2."),
# SC_193/195 can dầu → hộp đạn
("아리 đã ngồi trên đuôi K2 giữa can dầu, chân đung đưa;","아리 đã ngồi trên đuôi K2 giữa hộp đạn, chân đung đưa;"),
# SC_200 no drone battery
("7 kính đêm đang sạc, đèn đỏ hàng dài (5 chiếc đang dùng: 백성민 + 2 lính đi đầu + 태오 + xạ thủ K3 trên mỏm); pin drone; 4 radio;",
 "7 kính đêm đang sạc, đèn đỏ hàng dài (5 chiếc đang dùng: 백성민 + 2 lính đi đầu + 태오 + xạ thủ K3 trên mỏm); 4 radio (drone đang bay bằng pin 14 phút — không sạc);"),
# SC_202 pin 14 → 10
("[ACTION-VI] Đỉnh mỏm phẳng 10×10 m: 태오 quỳ, drone cất cánh khỏi tay biến vào đêm; màn hình controller: pin 30 → cậu đặt hẹn 10;",
 "[ACTION-VI] Đỉnh mỏm phẳng 10×10 m: 태오 quỳ, drone cất cánh khỏi tay biến vào đêm; màn hình controller: pin 14 → cậu đặt hẹn bay 10, để dành 4 phút quay về (lời 박기철);"),
# SC_231 탁발흠 counts
("[ACTION-VI] Trên đường dê, phía trên đống đá: hàng trăm đuốc dồn cục, ngựa quay ngang, không xuống được; dưới yên, số kỵ Tiên Ti đã vào (vài trăm) ngoái lại nhìn đường về bị bịt — họ bị cắt. High-angle.\n[SOUND] hú, ngựa, đá lăn rải rác.",
 "[ACTION-VI] Trên đường dê, phía trên đống đá: hàng trăm đuốc dồn cục, ngựa quay ngang, không xuống được; dưới yên, số kỵ Tiên Ti đã vào (vài trăm) ngoái lại nhìn đường về bị bịt — họ bị cắt. Cận: 탁발흠 trên nhánh trên, quay sang 부장, giơ bốn ngón tay — đếm sấm. High-angle.\n[SOUND] hú, ngựa, đá lăn rải rác.\n탁발흠: 넷."),
# SC_238 RTH reserved
("drone tự hạ xuống từ đêm — không ai điều khiển — đèn nhấp nháy, đáp đúng chỗ nó cất cánh;",
 "drone tự hạ xuống từ đêm — hết 10 phút bay, nó tự quay về bằng 4 phút pin 태오 để dành, không ai điều khiển — đèn nhấp nháy, đáp đúng chỗ nó cất cánh;"),
# SC_262 keep ACTION
]
# ---------- apply ----------
def find_block(sid):
    m=re.search(r'^### SC_%s .*?(?=^### SC_|\Z)'%sid, body, flags=re.M|re.S)
    return m
for sid,newn in N.items():
    m=find_block(sid); assert m, sid
    blk=m.group(0)
    assert re.search(r'^N: ',blk,re.M), ('no N',sid)
    blk2=re.sub(r'^N: .*$', 'N: '+newn, blk, count=1, flags=re.M)
    body=body[:m.start()]+blk2+body[m.end():]
for sid,(old,new) in D.items():
    m=find_block(sid); blk=m.group(0); assert old in blk,(sid,old)
    body=body[:m.start()]+blk.replace(old,new,1)+body[m.end():]
for old,new in R:
    c=body.count(old); assert c==1,(c,old[:60])
    body=body.replace(old,new,1)

# ---------- P6 reorder: old 109 (백성민 out) -> 107 ; old 107 -> 108 ; old 108 -> 109 ----------
b107=find_block('107').group(0); b108=find_block('108').group(0); b109=find_block('109').group(0)
start=find_block('107').start(); end=find_block('109').end()
def retag(blk,new,tnew):
    blk=re.sub(r'^### SC_\d+ ',f'### SC_{new} ',blk,count=1,flags=re.M)
    return re.sub(r'· (video8s|still_kenburns) · \d+:\d+–\d+:\d+',lambda m:f'· {m.group(1)} · {tnew}',blk,count=1)
new=retag(b109,'107','14:54–15:02')+retag(b107,'108','15:02–15:10')+retag(b108,'109','15:10–15:18')
body=body[:start]+new+body[end:]
# N for the moved blocks: N['107'] was written for 오태민 (now 108), N['108'] for 을지문덕 (now 109), N['109'] for 백성민 (now 107) — applied before renumber, so already correct.

# ---------- bờ tây → bờ bắc ; 강 서쪽 (done in N) ----------
body=body.replace('bờ tây','bờ bắc')
# P summaries
body=body.replace("Tùy chưa biết đại đội ở đây (loạt K6 = \"sấm Goguryeo\")","Tùy nhận ra 뇌군 ở bờ nam qua \"sấm\" (우중문 đã nghe ở 육합성 2화) — chưa biết ở đâu")
body=body.replace("9 quân tập kết bờ bắc, lính ném lương xuống sông [史]","9 quân tập kết bờ bắc, lính chôn nốt lương còn lại bên bờ [史: chôn]")
body=body.replace("Hắn đã thấy ở 압록: \"새는 수레에 앉아","Hắn đã thấy ở thung lũng 요동성 (2화, 12 ngày rình): \"새는 수레에 앉아")
body=body.replace("Insert địch: 2 척후 Tiên Ti trên gờ núi nhìn xuống bàn cát.","Rạng sáng: 소년 척후 chạm 2 척후 Tiên Ti trên đường đông (tên cắm yên) → 백성민 đọc là 척후 của cột Tùy phía sau.")
body=body.replace("K2 tắt máy, APU, dây sạc;","K2 tắt máy (giấu nhiệt/tiếng), APU, dây sạc — tháp \"bị cột vào dây\";")
body=body.replace("Xác bọc poncho, chôn kiểu Goguryeo","Xác bọc poncho, chôn kiểu Goguryeo")
body=body.replace("Tiên Ti lên mỏm bằng dây từ đỉnh vách","Tiên Ti lên mỏm bằng dây từ đỉnh vách")
body=body.replace("drone tự hạ về mỏm — tay Tiên Ti nhặt.","drone hết 10 phút tự quay về mỏm bằng 4 phút để dành — tay Tiên Ti nhặt; 탁발흠 đếm \"넷.\"")
body=body.replace("Foreshadow: 태극기 của 태오 trong tay 탁발흠 (5화) · kính đêm → 4화 săn đêm","Foreshadow: 태극기 của 태오 trong tay 탁발흠 (5화) · kính đêm → 4화 săn đêm · \"밤눈도 밥을 먹는다\" → pin kính đêm 4–5화")

# ---------- header ----------
head=head.replace("# 살수 612 — 3화 「남하」 대본 v1","# 살수 612 — 3화 「남하」 대본 v2 (QC-fixed)")
head=head.replace("> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 287 (241 video8s + 46 still_kenburns) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer",
 "> **Runtime mục tiêu:** 40:00 (38–42) · **Tổng shot:** 287 (241 video8s + 46 still_kenburns) — xem bảng thống kê cuối file · **Mid-roll:** 7:00 · 14:00 · 21:00 · 27:30 · **Ngày:** 2026-09-16 · script-writer\n> **v2 (QC-fixed, 2026-09-16):** áp dụng logs/qc_ep3_script.md (1 BLOCK + 20 FIX + NOTE ≤1 dòng) theo decisions.md mục \"sau QC 3화 → v2\" + SCRIPT_BRIEF \"Ngân sách đọc TTS\" (video8s ≤22 어절 N+thoại · still ≤45 · toàn tập ≤115 어절/phút). Không đổi SC ID/thời gian/open loop/quotes/mid-roll (trừ đảo thứ tự nội bộ SC_107–109 trong lều). Xem nhật ký v2 ở phụ lục E.")
head=head.replace("bờ tây","bờ bắc")
head=head.replace("Loạt K6 xuống nước (P4) bị Tùy hiểu là \"sấm Goguryeo\".","Loạt K6 xuống nước (P4): kỵ Tùy báo \"천둥\" → 우중문 nhận ra 뇌군 ở bờ nam (đã nghe tên ở 육합성 2화) — động cơ vượt sông.")
head=head.replace("| D2 | ngày | SC_012–022 | Hai cột song song cách 20리; kỵ Tùy cánh sườn bị 30 kỵ 해모루 chặn (mini-combat) |","| D2 | ngày | SC_012–022 | Hai cột song song cách 20리 (đại quân ~70리/ngày, đại đội 30리); kỵ Tùy cánh sườn bị 30 kỵ 해모루 chặn (mini-combat) |")
head=head.replace("| D3 | đêm | SC_033–048 | Trạm dừng (LOC_003 Dạng B): \"400km 딱\"","| D3 | đêm | SC_033–048 | Trạm dừng (LOC_003 Dạng B): \"400km 딱\" (gom ≈430 ở 2화, đã chạy 30 km)")
head=head.replace("| D9 | sáng–chiều [史] | SC_051–075 | 압록수: lính Tùy ném lương xuống sông; 을지문덕 giả hàng","| D9 | sáng–chiều [史] | SC_051–075 | 압록수: lính Tùy chôn nốt lương bên bờ; 을지문덕 giả hàng")
head=head.replace("| D10 | đêm | SC_126–131 | ENEMY (chiếu ở P7, sau P6): 탁발흠 chui vào 천둥 3 bờ bắc; bản đồ bùn → 석문령; bịt tai ngựa |","| D10 | đêm | SC_126–131 | ENEMY (chiếu ở P7, sau P6): 탁발흠 chui vào 천둥 3 bờ bắc; bản đồ bùn → 석문령 (hỏi nông dân 2화); bài học \"chim ăn / mắt đêm đứng yên\" từ 12 ngày rình thung lũng 요동성 (2화); bịt tai ngựa |")
head=head.replace("| D12 | chiều tối–đêm | SC_151–172 | Kỵ Tùy cướp ruộng; quyết vá; \"충전 한 번 / 40%\"; ngủ sau 3 đêm; 을보 gò đồng; 3 척후 해모루 đi qua dưới cung Tiên Ti — 탁발흠 thả |","| D12 | chiều tối–đêm | SC_151–172 | Kỵ Tùy cướp ruộng; quyết vá; \"허락된 충전 한 번 / 40%\"; ngủ sau 3 đêm; 을보 gò đồng; 3 척후 해모루 (đi từ sáng D12) xuống đường dê dưới cung Tiên Ti — 탁발흠 thả |")
head=head.replace("| D14 | rạng sáng–chiều | SC_173–197 | \"사흘째 새벽\" thử máy; bàn cát;","| D14 | rạng sáng–chiều | SC_173–197 | \"사흘째 새벽\" thử máy, đổ nốt phuy; 소년 척후 chạm 2 척후 Tiên Ti đường đông; bàn cát;")
open(p,'w',encoding='utf-8').write(head+body+appx)
print('written')
