from random import *

score = []
score.append([0,0,0])
score.append([0,0,0])
name = ["가위","바위","보"]

while 1 :
    my_finger = int(input("가위(1) 바위(2) 보(3)를 입력하세요 "))
    if my_finger == 0 : break
    com_finger = randint(1,3)
    print("컴퓨터가 낸 것은 %s입니다!"%(name[com_finger-1]))

    if my_finger == 1 and com_finger == 3:
        score[0][2]+=1
        score[1][0]+=1
        print("사용자 승!")
    elif my_finger == 3 and com_finger == 1 :
        score[0][0]+=1
        score[1][2]+=1
        print("컴퓨터 승!")
    else :
        if com_finger > my_finger :
            score[0][0]+=1
            score[1][2]+=1
            print("컴퓨터 승!")
        elif com_finger < my_finger :
            score[0][2]+=1
            score[1][0]+=1
            print("사용자 승!")
        else :
            score[0][1]+=1
            score[1][1]+=1
            print("비김!")

print("컴퓨터 : 승 %d회 무 %d회 패 %d회 입니다"%(score[0][0],score[0][1],score[0][2]))
print("사용자 : 승 %d회 무 %d회 패 %d회 입니다"%(score[1][0],score[1][1],score[1][2]))
