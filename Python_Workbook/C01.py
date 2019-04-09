birth_year = int(input('Birth year?'))
age = 2018- birth_year +1

if age<7 : print('유아')
elif age<13 : print('어린이')
elif age<20 : print('청소년')
elif age<30 : print('청년')
elif age<60 : print('중년')
else : print('노년')