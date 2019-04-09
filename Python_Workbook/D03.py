totalsum = 0
count = 0

while 1 : 
    number = int(input('input number between 0 and 100 '))
    if number <= 0 or number >= 100 : break
    
    totalsum += number
    count+=1

average = totalsum/count
print('total : ',totalsum)
print('average : ',average)