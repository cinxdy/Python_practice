jumsu=[]
sum=[0,0,0]
average=[0,0,0]

for i in range(5) :
    kor,eng,mat = map(int,input("%dth kor,eng,math point"%(i+1)).split())
    jumsu.append([kor,eng,mat])
    for j in range(3) :
        sum[j]+=jumsu[i][j]

for j in range(3) :
    average[j] = sum[j]/5

print("kor: sum = %d, average = %.1f"%(sum[0],average[0]))
print("eng: sum = %d, average = %.1f"%(sum[1],average[1]))
print("math: sum = %d, average = %.1f"%(sum[2],average[2]))