def Ackermann(i,j):
    if i==0 and j>=0 :
        return j+1
    elif i>0 and j==0 :
        return Ackermann(i-1,1)
    else : return Ackermann(i-1,Ackermann(i,j-1))

for i in range(4):
    for j in range(4):
        print("Ackermann(%d,%d) = %d"%(i,j,Ackermann(i,j)))