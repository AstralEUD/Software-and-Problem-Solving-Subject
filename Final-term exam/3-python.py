birthage = int(input("출생 연도를 입력하세요: "))
pbt = birthage%10
if (2022-birthage) >= 65:
    print("65세 이상이므로 언제든지 구매가 가능합니다.")
elif (pbt == 1) or (pbt==6):
    print("월요일에 구매가 가능합니다")
elif (pbt == 2) or (pbt==7):
    print("화요일에 구매가 가능합니다")
elif (pbt == 3) or (pbt==8):
    print("수요일에 구매가 가능합니다")
elif (pbt == 4) or (pbt==9):
    print("목요일에 구매가 가능합니다")
elif (pbt == 5) or (pbt==0):
    print("금요일에 구매가 가능합니다")
