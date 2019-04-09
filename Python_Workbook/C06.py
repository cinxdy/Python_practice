kor = int(input('kor?'))
eng = int(input('eng?'))
math = int(input('math?'))

total = kor+eng+math
average = total / 3.0

print('total:',total)
print('average:',average)
print('grade:')
if average < 60 : print('가')
elif average < 70 : print('양')
elif average < 80 : print('미')
elif average < 90 : print('우')
else : print('수')