number = []
floor_total = [0 for i in range(5)]
line_total = [0 for j in range(3)]
total = 0


#input
for i in range(5):
    number.append([])
    for j in range(3):
        newnum = int(input("%d0%d-ho person "%(i+1,j+1)))
        number[i].append(newnum)
        total += number[i][j]

#sum
for i in range(5):
    for j in range(3):
        floor_total[i] += number[i][j]
        line_total[j] += number[i][j]

#output
for i in range(5):
    print("%dth floor total member is %d"%(i+1,floor_total[i]))
for j in range(3):
    print("%dth line total member is %d"%(j+1,line_total[j]))
print("total member is %d"%(total))