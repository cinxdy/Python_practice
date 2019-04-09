from random import *

def GetRandom() :
        number = randint(1,100)
        print("random number :",number)
        if number < 40 : return 2
        elif number < 70 : return 1
        else : return 0

count = [0,0,0]

print("Make Ten Random numbers")
for i in range(10) :
    count[GetRandom()] += 1
print("1.대 (70이상) : %d회 생성"%(count[0]))
print("2.중 (40이상) : %d회 생성"%(count[1]))
print("3.소 (40미만) : %d회 생성"%(count[2]))