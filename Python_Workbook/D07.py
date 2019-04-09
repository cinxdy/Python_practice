a,b = map(int,input('y = ax+b, Input a and b ').split())
x_begin, x_end = map(int,input('Input x_begin and x_end ').split())

for x in range(x_begin,x_end+1) :
    y = a*x + b
    print('좌표 (',x,',',y,')')