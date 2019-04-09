num1 = int(input('number 1?'))
num2 = int(input('number 2?'))
num3 = int(input('number 3?'))

if num1 > num2 :
    if num1 > num3 : max_num = num1
    else : max_num = num3
else :
    if num2 < num3 : max_num = num3
    else : max_num =  num2

if num1 < num2 :
    if num1 < num3 : min_num = num1
    else : min_num = num3
else :
    if num2 < num3 : min_num = num3
    else : min_num =  num2

print('max : ',max_num,'min : ',min_num)