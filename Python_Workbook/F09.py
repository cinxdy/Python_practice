monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
day_count = 0

while 1 :
    month = int(input("month? "))
    if month<1 or month>12 : 
        print("Wrong number!")
    else : break

while 1 :
    day = int(input("day? "))
    if day<1 or day>monthdays[month-1] : print("Wrong number!")
    else : break

if month != 1 :
    for i in range(month-1) :
        day_count += monthdays[i]
day_count += day

print("The Date is %dth day in a year"%(day_count))