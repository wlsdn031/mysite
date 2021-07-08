class thailandPackage:
    def detail(self):
        print("태국 여행 야시장 투어")

if __name__ == "__main__":
    print("thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = thailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")