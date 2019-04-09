first = 0
second = 0

n1 = int(input('enter a number :'))
n2 = int(input('enter a number :'))
n3 = int(input('enter a number :'))
n4 = int(input('enter a number :'))
n5 = int(input('enter a number :'))
n6 = int(input('enter a number :'))
n7 = int(input('enter a number :'))

n=[n1,n2,n3,n4,n5,n6,n7]

if n1 == n2 == n3 ==n4==n5==n6==n7 :
    print('두 번째로 큰 수가 없습니다')

for i in range(7) :
    if first < n[i] :
        first = n[i]

for i in range(7) :
    if first != n[i] and second < n[i] :
        second = n[i]

if second = 0 :
    print('두 번째로 큰 수가 없습니다')
else 
    print('두 번째로 큰 수는 :', second)