def ShowMenu() :
    price = [15000,10000,7000,2000]
    print("1. 피자(15,000원) 2. 스파게티(10,000원) 3. 샐러드(7,000원) 4. 음료수(2,000원)")
    menu = int(input("메뉴를 선택해주세요.(종료:5)"))
    if menu == 5 : return -1
    else : return price[menu-1]

sum = 0
while 1:
    price = ShowMenu()
    if price == -1 : break
    else :
        sum += price
        print("현재까지의 주문 금액은 %d원입니다.\n"%sum)
print("\n")
print("총 주문 금액은 %d원입니다."%sum)