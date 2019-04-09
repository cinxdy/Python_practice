def SelectCan() :
    price = [700,300,1000,500,600]
    print("1. 콜라(700원) 2. 원두커피(300원) 3. 레몬주스(1000원) 4. 홍차(500원) 5. 코코아(600원)")
    menu = int(input("메뉴를 선택해주세요 : "))
    return price[menu-1]

count = 0
sum = 0
while 1:
    price = SelectCan()
    count+=1
    sum += price
    more = input("더 필요하십니까? (Y/N) ")
    if more == 'N' : break

print("총 %d개의 음료를 선택하여 총 %d원입니다."%(count,sum))
