degrees = []
degree_name = ["냉수","미온수","온수","끓는물"]
count = [0 for i in range(4)]
i=0
while i!=10:
    input_degree = float(input("%dth degree : "%(i+1)))

    if input_degree<0 : print("Wrong!")
    else :
        if input_degree<25 : sel = 0
        elif input_degree<40 : sel = 1
        elif input_degree<80 : sel = 2
        else : sel = 3
        i+=1
        count[sel]+=1
        degrees.append([input_degree,sel])
    
for i in range(10) :
    print("%dth Water degree : %.1f (%s)"%(i+1,degrees[i][0],degree_name[degrees[i][1]]))

for i in range(4) :
    print("%s count : %d"%(degree_name[i],count[i]))