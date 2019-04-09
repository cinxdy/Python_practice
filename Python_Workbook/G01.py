agelist = []
kind = ["유아","어린이","청소년","청년","중년","노년"]
count=[0 for i in range (100)]

for i in range(100) :
    birth = int(input("%dth person's birth year : "%(i+1)))
    if birth > 2019 : 
        count_total = i
        break
    age = 2019 - birth + 1
    agelist.append( age )
    
    if age <7 : count[0]+=1
    elif age <13 : count[1]+=1
    elif age <20 : count[2]+=1
    elif age <30 : count[3]+=1
    elif age <60 : count[4]+=1
    else : count[5]+=1

for i in range(count_total) : print("%dth person age : %d"%(i+1,agelist[i]))
for i in range(6) : print("%s count : %d "%(kind[i],count[i]))
