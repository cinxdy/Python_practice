total_charge = 0
while 1 :
    hour, minute = map(int,input("Input hour and minute ").split())
    if hour == 0 and minute == 0 : break
    charge = hour * 2 * 1000
    if minute > 30 :
        charge += 2 * 1000
    elif minute >0 :
        charge += 1000

    if hour >= 2 and hour < 3 :
        charge *= 0.95
    elif hour >= 3 and hour<5 :
        charge *= 0.90
    elif hour >= 5 :
        charge *= 0.80
    
    print("charge : %d"%(charge))
    total_charge += charge
print("total charge : %d"%(total_charge))
