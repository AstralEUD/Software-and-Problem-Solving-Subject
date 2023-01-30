price = 30000000
for year in range(0,10,1):
    price=price*(104/100)
price = int(price)
print(f'10 년후 연봉 : {price}')
