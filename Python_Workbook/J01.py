def AskAge(birthyear) :
    age = 2019 - birthyear + 1
    print("Age : ",age)
    if age < 7 : return 0
    elif age < 13 : return 1
    elif age < 20 : return 2
    elif age < 30 : return 3
    elif age < 40 : return 4
    else : return 5

kind = ["유아","어린이","청소년","청년","중년","노년"]
count=[0,0,0,0,0,0]
i = 0
while 1 :
    birthyear = int(input("%dth Year : "%(i+1)))
    if birthyear > 2019 : break
    else :
        count[AskAge(birthyear)]+=1
        i+=1

for i in range(6):
    print("%s count : %d"%(kind[i],count[i]))