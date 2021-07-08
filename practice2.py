
maple_warrior = True
weapon = "한손검"
jobconstant = 1
dobi = False
while dobi == False :
    try:
        print(dobi)
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

        print(dobi)
    except ValueError :
        print("잘못 입력하셨습니다.")
        dobi = False