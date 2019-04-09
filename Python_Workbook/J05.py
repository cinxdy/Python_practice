def CalcParking(start_h,start_m,end_h,end_m):
    fee = 0
    term_m = (end_h - start_h)*60 + end_m - start_m
    if term_m % 10 == 0 :
        fee = (term_m//10) *500
    else : 
        fee = (term_m//10+1) *500
    return fee
sum_fee = 0
i = 0
while 1:
    start_h, start_m = map(int,input("%dth Car Time Started Parking : "%(i+1)).split())
    end_h, end_m = map(int,input("%dth Car Time Started Parking : "%(i+1)).split())
    parkingfee = CalcParking(start_h,start_m,end_h,end_m)
    sum_fee += parkingfee
    print("The Parking Fee : ",parkingfee)
    more = input("Are you insert more? (Y/N) : ")
    if more == 'Y' : i+=1
    else : break

print("Parked Car : ",i+1)
print("Sum of Parking Fee : ",sum_fee)