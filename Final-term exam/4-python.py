
person = int(input("사람의 수를 입력하시오 : "))
dpee=0
if (person>=20):
    dpee = person*1500
    print(f'20% 할인, 할인 금액 : {dpee}원')
elif (person>=10):
    dpee = person*750
    print(f'10% 할인, 할인 금액 : {dpee}원')
print(f'총비용: {person*7500-dpee}원')
