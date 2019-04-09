def Max(num):
    max = num[0]
    for i in range(1,10) :
        if num[i] > max : max = num[i]
    return max

def Min(num):
    min = num[0]
    for i in range(1,10) :
        if num[i] < min : min = num[i]
    return min

num = [ 0 for i in range(10) ]
for i in range(10):
    num[i] = float(input("%dth number : "%(i+1)))

Min_num = Min(num)
Max_num = Max(num)
sum = 0
for i in range(10):
    if num[i]!=Min_num and num[i]!=Max_num :
        sum += num[i]

average = sum / 8

print("Average expect max and min : %d"%average)
