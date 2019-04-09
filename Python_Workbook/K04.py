def load_point(filename):
    newlist=[]
    file = open(filename,"r")

    while 1 :
        list = file.readline().strip().split()
        if len(list)==2 :
            newlist.append([float(list[0]),float(list[1])])
        else : break
    file.close()
    return newlist

def get_area(x,y):
    if x==0 or y==0 : return 0
    elif x>0 :
        if y>0 : return 1
        else : return 4
    elif x<0 :
        if y>0 : return 2
        else : return 3

list = load_point("point.txt")
print("point.txt에서 좌표 정보를 읽어들였습니다.")

count = [0,0,0,0,0]

for i in range(10):
    x= list[i][0]
    y= list[i][1]
    sa = get_area(x,y)
    count[sa]+=1
    print("%dth (%.1f,%.1f) is included in %dth area"%(i+1,x,y,sa))

for i in range(1,5):
    print("%dth area count : %d"%(i,count[i]))