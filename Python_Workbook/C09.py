income = int(input('income?'))
if income <10000000 :
    tax = income * 0.095
elif income < 40000000 :
    tax = income * 0.19
elif income < 80000000 :
    tax = income * 0.28
else : tax = income * 0.37

print('tax : ',tax)