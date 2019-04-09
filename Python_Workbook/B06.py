kor = int(input('kor point?'))
eng = int(input('eng point?'))
math = int(input('math point?'))

total = kor + eng + math
average = total / 3.0

print('total?',total)
print('average?',average)

if kor >= 90 :
    print('kor great!')
if eng >= 90 :
    print('eng great!')
if math >= 90 :
    print('math great!')