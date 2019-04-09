from random import *

lotto_com = [0 for i in range(6)]
lotto_user = [0 for i in range(6)]
count = 0

i=0
while i!=6 :
    lotto_user[i]=int(input("%dth lotto number "%(i+1)))
    if lotto_user[i]>45 or lotto_user[i]<1 :
        print("Wrong!")
    else :  
        dup = 0
        for j in range(i) :
            if lotto_user[j] == lotto_user[i] :
                dup = 1
                break
            
        if dup == 1 :
            print("Wrong!")
        else : i+=1

i=0
while i!=6 :
    lotto_com[i]=randint(1,45)
    
    dup = 0
    for j in range(i) :
        if lotto_com[j] == lotto_com[i] :
            dup = 1
            break 
    if dup == 0 : i+=1

for i in range(6) :
    for j in range(6) :
        if lotto_user[i] == lotto_com[j] :
            count+=1

print()
print("This week lotto numbers are %d %d %d %d %d %d"%(lotto_com[0],lotto_com[1],lotto_com[2],lotto_com[3],lotto_com[4],lotto_com[5]))
print()
print("Matched number count is %d"%count)