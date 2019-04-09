def AskWater(degree) :
    if degree < 25 : return 0
    elif degree < 40 : return 1
    elif degree < 80 : return 2
    else : return 3

kind = ["냉수","미온수","온수","끓는물"]
count = [0 for i in range(4)]
degree = [0 for i in range(10)]
for i in range(10) :
    degree[i] = float(input("%dth degree : "%(i+1)))
    count[AskWater(degree[i])]+=1

for i in range(4) :
    print(kind[i],"degree : ",count[i])