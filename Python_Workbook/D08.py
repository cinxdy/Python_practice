a,b,c = map(int,input('Input a b c ').split())
x_begin, x_end = map(int,input('Input x_begin,x_end ').split())

for x in range(x_begin,x_end+1) :
    y = a*(x**2) + b*x + c
    print('좌표 (',x,',',y,')')
