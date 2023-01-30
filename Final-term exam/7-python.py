arr=[30, 20, 21, 24, 30, 28, 22, 30, 20, 30, 27]
print(f'선수 나이 리스트: {arr}')
count1=0
maxage = 0
cntmax = 0
minage = 200
cntmin = 0
for i in arr:
    if (i<=25):
        count1+=1
    if (maxage < i):
        maxage=i
        cntmax=1
    elif (maxage == i):
        cntmax+=1
    if (minage > i):
        minage=i
        cntmin=1
    elif (minage == i):
        cntmin+=1
print(f'1) 25세 이하 선수 : {count1}명')
print(f'2) 가장 많은 나이 : {maxage}세')
print(f'3) 가장 적은 나이 : {minage}세')
print(f'4) 가장 많은 나이의 갯수 : {cntmax}명')
print(f'5) 가장 적은 나이의 갯수 : {cntmin}명')
