def save_jumsu(jumsulist,filename) :
    file = open(filename,"w")
    for item in jumsulist:
        file.write("%d\t %d\t %d\t %d\t %.1f\n"%(item[0],item[1],item[2],item[3],item[4]))
    file.close()
    print("Saved in",filename)

jumsu=[]
for i in range(5):
    kor,eng,math = map(int,input("%dth kor,eng,math point : "%(i+1)).split())
    jumsu.append([kor,eng,math,kor+eng+math,(kor+eng+math)/3])

print("number\t kor\t eng\t math\t sum\t average")
for i in range(5):
    print("%d\t %d\t %d\t %d\t %d\t %.1f"%(i+1,jumsu[i][0],jumsu[i][1],jumsu[i][2],jumsu[i][3],jumsu[i][4]))

save_jumsu(jumsu,"jumsu.txt")