def CalcDate(month,day):
    monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    day_count = 0
    while 1 :
        if month<1 or month>12 :
            return -1
        else : break
    while 1 :
        if day<1 or day>monthdays[month-1] :
            return -1
        else : break
    if month != 1 :
        for i in range(month-1) :
            day_count += monthdays[i]
    day_count += day
    return day_count

start_m, start_d = map(int,input("start day (month day) : ").split())
end_m, end_d = map(int,input("end day (month day) : ").split())

start = CalcDate(start_m,start_d)
end = CalcDate(end_m,end_d)
if start > 0 or end > 0 :
    date = end-start
    if date < 0 : date+=365
    print("term : ",date)
else : print("Wrong month or day!")