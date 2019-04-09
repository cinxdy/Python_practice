number = []
count = 0
dup = 0

print("input number between 1 and 100")

while count!=10 :
    newnum = int(input("%dth number : "%(count+1)))
    for i in range(count) :
        dup = 0
        if newnum == number[i] :
            dup = 1
            break

    if newnum < 1 or newnum >100 or dup ==1 : 
        print("Wrong number!")
    else :
        number.append(newnum)
        count+=1

for i in range(10):
    print("%dth number : %d"%(i+1,number[i]))