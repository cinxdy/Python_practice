num = []
first = 0
second = 0

for i in range(10) :
    newnum = int(input("%dth number?"%(i+1)))
    num.append(newnum)
    if first<num[i] : first = num[i]

for i in range(10) :
    if first!=num[i] and second<num[i] :
        second = num[i]
        second_index = i

print("두번째로 큰 수는 %d번째 수 %d"%(second_index+1,second))