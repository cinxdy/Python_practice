def get_area(x,y):
    if x==0 or y==0 : return 0
    elif x>0 :
        if y>0 : return 1
        else : return 4
    elif x<0 :
        if y>0 : return 2
        else : return 3
    
count=[0,0,0,0,0]
sa=[0 for i in range(10)]
file = open("point.txt","w")

for i in range(10):
    x,y = map(float,input("%dth x,y : "%(i+1)).split())
    file.write("%f %f\n"%(x,y))
    sa[i]= get_area(x,y)
    count[sa[i]]+=1

for i in range(10):
    print("%dth (x,y) is included in %dth area"%(i+1,sa[i]))
    
for i in range(1,5):
    print("%dth area count : %d"%(i,count[i]))

print("point.txt에 저장하였습니다.")