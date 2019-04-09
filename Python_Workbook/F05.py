bmilist = []
count = 0

for i in range(10) :
    height,weight = map(int,input("%dth height(cm) and weight(kg) "%(i+1)).split())
    bmi = weight / ((height/100)**2)
    bmilist.append([height,weight,bmi])
    
for i in range(10) :
    if bmilist[i][2]>=25 :
        print("%dth person is obesity"%(i+1))
        count+=1

print("total %d people are obesity"%(count))