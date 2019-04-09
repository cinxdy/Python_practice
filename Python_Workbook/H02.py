from random import *

lotto = [0 for i in range(6)]

while 1 :

    i=0
    while i!=6 :
        lotto[i]=randint(1,45)
        bool = 0
        for j in range(i) :
            if lotto[j]==lotto[i] : 
                bool = 1
                break
        if bool == 0:
            i+=1

    print("lotto numbers are %d %d %d %d %d %d"%(lotto[0],lotto[1],lotto[2],lotto[3],lotto[4],lotto[5]))

    onemore = input("more? (Y/N)")
    if onemore == 'N':
        break