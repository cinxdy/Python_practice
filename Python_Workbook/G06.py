order = [0,0,0]
total_sale = 0
total_order = 0
price = [10000,6000,3000]

print("세 종류의 제품이 있습니다.\n 1)가죽장갑 1만원, 2)털장갑 6천원, 3)비닐장갑 3천원\n")

while 1 :
    sale = 0
    for i in range(3) :
        order[i] = int(input("%d번 제품은 몇 개 구입하십니까? "%(i+1)))
        sale += order[i]*price[i]
    if sale == 0 : break
    print("판매금액은 %d원 입니다.\n"%sale)
    total_sale += sale
print("지금까지의 총 매출금액은 %d원 입니다."%total_sale)
