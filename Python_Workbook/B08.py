num1 = int(input('number 1?'))
num2 = int(input('number 2?'))
num3 = int(input('number 3?'))

if num1==num2 or num2==num3 or num1==num3 :
    print('condition1 satisfied')
if (num1>50 and num2>50) or (num2>50 and num3>50) or (num1>50 and num3>50) :
    print('condition2 satisfied')
if num1+num2 == num3 or num2+num3 == num1 or num1+num3 == num1 :
    print('condition3 satisfied')
if (num2%num1 == 0 and num3%num1 == 0) or (num1%num2 == 0 and num3%num2 == 0) or (num1%num3 == 0 and num2%num3 == 0) :
    print('condition4 satisfied')