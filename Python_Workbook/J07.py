def poweroftwo(n):
    if n== 0 : return 1
    else : return 2*poweroftwo(n-1)
        
while 1 :
    num = int(input("Insert a number : "))
    if num == 0 : break
    else : print("2^%d = %d"%(num,poweroftwo(num)))