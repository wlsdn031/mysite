maple_warrior = True
weapon = "한손검"
jobconstant = 1
dobi = False
while dobi == False :
    try:
        job = input("직업명(축약없이, 띄어쓰기 없이, 썬콜 불독 표기)")
        if job == "히어로":
            if weapon in ["한손검", "한손도끼"]:
                jobconstant = 1.0833
                dobi = True
            elif weapon in ["두손검" , "두손도끼"]:
                jobconstant = 1.0746
                dobi = True
        elif job in ["썬콜" , "불독" , "비숍" , "플레임위자드"] :
            jobconstant = 1.2
            dobi = True
        elif job == "제논" :
            jobconstant == 0.875
            dobi = True
        elif job in ["팔라딘" , "다크나이트" , "보우마스터" , "신궁" , "패스파인더" , "나이트로드" , "섀도어" , "듀얼블레이드" , \
            "캐논슈터" ,"캡틴" , "바이퍼" , "소울마스터" , "윈드브레이커" , "나이트워커" , "스트라이커" , "미하일" , "아란" , "에반"\
                 , "메르세데스" , "팬텀" , "루미너스" , "은월" , "배틀메이지" , "와일드헌터" , "메카닉" , "블래스터" , \
                     "데몬슬레이어" , "데몬어벤져" , "카이저" , "앤젤릭버스터" , "카인" , "카데나" , "아크" , "아델" , "일리움" ,\
                          "호영" , "라라" , "제로" , "키네시스"] :
            dobi = True
        else :
            raise ValueError
    except ValueError :
        print("잘못 입력하셨습니다.")
        dobi = False

weaponconstant = 1.0

if weapon in ["스태프" , "완드"]:
    weaponconstant = 1.0
elif weapon in ["한손검" , "한손도끼" , "한손둔기", "ESP리미터", "매직건틀렛", "샤이닝로드"]:
    weaponconstant = 1.2
elif weapon in ["활", "듀얼보우건", "단검", "블레이드", "케인", "데스페라도", "에인션트보우" ,"체인", "부채", "브레스슈터"]:
    weaponconstant = 1.3
elif weapon in ["두손검", "두손도끼", "두손둔기", "튜너", "태도"]:
    weaponconstant = 1.34
elif weapon in ["석궁"]:
    weaponconstant = 1.35
elif weapon in ["창", "폴암", "대검"]:
    weaponconstant = 1.49
elif weapon in ["건", "핸드캐논", "에너지소드"] :
    weaponconstant = 1.5
elif weapon in ["너클", "소울슈터", "건틀릿리볼버"]:
    weaponconstant = 1.7
elif weapon in ["아대"]:
    weaponconstant = 1.75

level = 1
mainstat_percent_skill = 0
mainstat_percent_equip = 0
mainstat_percent_exp = 0
mainstat_percent = mainstat_percent_equip + mainstat_percent_skill + mainstat_percent_exp
mainstat_fixed_hyper = 0
mainstat_fixed_ability = 0
mainstat_fixed_union = 0
mainstat_fixed_symbol = 0
mainstat_fixed_exp = 0
mainstat_fixed = mainstat_fixed_ability + mainstat_fixed_hyper + mainstat_fixed_symbol + mainstat_fixed_union + mainstat_fixed_exp
mainstat_flexible_equip = 0
mainstat_flexible_union = 0
mainstat_flexible_skill = 0
mainstat_flexible_doping = 0
mainstat_flexible_level = (level - 1) * 5 + 4
if maple_warrior == True :
    mainstat_flexible_level == mainstat_flexible_level * 1.15
mainstat_flexible_exp = 0
mainstat_flexible = mainstat_flexible_equip + mainstat_flexible_level + mainstat_flexible_skill + mainstat_flexible_union + mainstat_flexible_doping + mainstat_flexible_exp
mainstat = ( mainstat_flexible * mainstat_percent ) + mainstat_fixed

substat_fixed_hyper = 0
substat_fixed_ability = 0
substat_fixed_union = 0
substat_fixed_exp = 0
substat_fixed = substat_fixed_hyper + substat_fixed_ability + substat_fixed_union + substat_fixed_exp
substat_flexible_equip = 0
substat_flexible_union = 0
substat_flexible_skill = 0
substat_flexible_doping = 0
substat_flexible_exp = 0
substat_flexible = substat_flexible_equip + substat_flexible_skill + substat_flexible_union + substat_flexible_doping + substat_flexible_exp
substat = substat_fixed + substat_flexible + 4

attackpoint_skill = 0
attackpoint_equip = 15
attackpoint_union = 0
attackpoint_hyper = 0
attackpoint_ability = 0
attackpoint_doping = 0
attackpoint_exp = 0
attackpoint = attackpoint_ability + attackpoint_doping + attackpoint_equip + attackpoint_hyper + attackpoint_skill + attackpoint_union + attackpoint_exp

attackpoint_percent_skill = 0
attackpoint_percent_equip = 0
attackpoint_percent_exp = 0
attackpoint_percent = attackpoint_percent_equip + attackpoint_percent_skill + attackpoint_percent_exp

damage_percent_skill = 0
damage_percent_hyper = 0
damage_percent_ability = 0
damage_percent_doping = 0
damage_percent_equip = 0
damage_percent_union = 0
damage_percent_exp = 0
damage_percent = damage_percent_ability + damage_percent_doping + damage_percent_equip + damage_percent_hyper + damage_percent_skill + damage_percent_union

bossdamage_equip = 0
bossdamage_hyper = 0
bossdamage_skill = 0
bossdamage_doping = 0
bossdamage_union = 0
bossdamage_exp = 0
bossdamage = bossdamage_equip + bossdamage_doping + bossdamage_hyper + bossdamage_skill + bossdamage_union + bossdamage_exp
lastdamage_skill = 0
lastdamage_exp = 0
lastdamage = lastdamage_skill + lastdamage_exp

crirate_skill = 0
crirate_hyper = 0
crirate_equip = 0
crirate_union = 0
crirate_ability = 0
crirate_exp = 0
crirate = 5 + crirate_equip + crirate_hyper + crirate_ability + crirate_skill + crirate_union + crirate_exp

cridamage_union = 0
cridamage_equip = 0
cridamage_skill = 0
cridamage_hyper = 0
cridamage_exp = 0
cridamage = 35 + cridamage_equip + cridamage_exp + cridamage_hyper + cridamage_skill + cridamage_union

statattack = (mainstat * 4 + substat) * 0.01 * attackpoint * weaponconstant * jobconstant * ((100 + attackpoint_percent)/100) * ((100 + bossdamage + damage_percent)/100) * ((100+lastdamage)/100)
# (주스탯×4+부스탯)×0.01×총 공격력×무기상수×직업상수×(1+공격력%)×(1+데미지%)×(1+최종 데미지%)
NormalAttackDamage = 1
if crirate >= 100 :
    NormalAttackDamage = statattack * ((100 + cridamage)/100)
elif crirate < 100 :
    NormalAttackDamage = statattack + (statattack * (crirate/100) * (cridamage/100))

print(NormalAttackDamage)
# (주스탯×4+부스탯)×0.01×총 공격력×무기상수×직업상수×(1+공격력%)×(1+데미지%)×(1+최종 데미지%)
