jumsu=[]
sum=[0,0,0,0,0]
average=[0,0,0,0,0]

for i in range(5) :
    kor,eng,mat = map(int,input("%dth kor,eng,math point"%(i+1)).split())
    jumsu.append([kor,eng,mat])
    for j in range(3) :
        sum[i]+=jumsu[i][j]

for i in range(5) :
    average[i] = sum[i]/3
    print("%dth student sum = %d, average = %.1f"%(i+1,sum[i],average[i]))