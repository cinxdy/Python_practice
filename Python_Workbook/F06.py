number = []
total = 0

for i in range(5):
    number.append([])
    for j in range(3):
        newnum = int(input("%d0%d-ho person "%(i+1,j+1)))
        number[i].append(newnum)
        total += number[i][j]
print("total member is %d"%(total))