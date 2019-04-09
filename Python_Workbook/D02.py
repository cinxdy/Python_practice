max = 0
min = 100

while 1 : 
    number = int(input('input number between 0 and 100 '))
    if number <= 0 or number >= 100 : break
    if max<number : max = number
    if min>number : min = number

print('max : ',max)
print('min : ',min)