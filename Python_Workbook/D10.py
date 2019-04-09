num1,num2 = map(int,input('Input 2 numbers ').split())

for i in range(1,101) :
    if (i%num1 == 0 or i%num2 == 0) and not (i%num1 == 0 and i%num2 == 0) :
        print(i,end=' ')