jumsu = []
class_score = []
class_name = ["kor","eng","math"]
sum = 0

#input
for i in range(5) :
    kor,eng,mat = map(int,input("%dth student kor,eng,math point "%(i+1)).split())
    jumsu.append([kor,eng,mat])

#sum
for j in range(3) :
    for i in range(5) :
        sum += jumsu[i][j]
    average = sum/5
    class_score.append([sum,average])
    sum = 0

for i in range(5) :
    for j in range(3) :
        sum += jumsu[i][j]
    average = sum / 3
    if average >= 90 : grade = 'A'
    elif average >= 80 : grade = 'B'
    elif average >= 70 : grade = 'C'
    elif average >= 60 : grade = 'D'
    else : grade = 'F'
    jumsu[i].append(sum)
    sum =0
    jumsu[i].append(average)
    jumsu[i].append(grade)

#output
print("\n1) subject")
for j in range(3) :
    print("%s subject total : %d, average : %.1f"%(class_name[j],class_score[j][0],class_score[j][1]))

print("\n2) student")
for i in range(5) :
    print("%dth student total : %d, average : %.1f, grade : %s"%(i+1,jumsu[i][3],jumsu[i][4],jumsu[i][5]))