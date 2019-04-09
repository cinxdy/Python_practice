num1 = int(input('number 1?'))
num2 = int(input('number 2?'))
operator = input('operator?(+,-,*,/) ')

if operator == '+' :
    result = num1 + num2
elif operator == '-' :
    result = num1 - num2
elif operator == '*' :
    result = num1 * num2
elif operator == '/' :
    result = num1 / num2

print(num1,operator,num2,'=',result)