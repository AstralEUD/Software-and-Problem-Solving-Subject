price = 30000000
year=0
while(price<=60000000):
    price=price*(104/100)
    year+=1
price = int(price)
print(f'{year} 년후 연봉이 2배 이상이 됩니다. 연봉: : {price}원')
