from random import *

coins = int(input("코인 몇 개를 사용하십니까?"))
number = [0,0,0]

i=0
while coins > 0 :
    dummy = int(input("게임 %d회 Start!!!(아무 숫자나 입력하세요)"%(i+1)))
    i += 1
    coins -= 1
    
    for i in range(3) :
        number[i] = randint(1,9)
    print("게임 결과 : %d %d %d"%(number[0],number[1],number[2]))
    if number[0]==number[1] and number[1]==number[2] :
        print("숫자 3개 일치!...코인 4개 증정")
        coins+=4
    elif number[0]==number[1] or number[1]==number[2] or number[0]==number[2] :
        print("숫자 2개 일치!...코인 2개 증정")
        coins+=2
    else : print("꽝입니다... 아쉽군요...")
    print("남아있는 코인은 %d개 입니다"%coins)

print("게임 종료!!!")
