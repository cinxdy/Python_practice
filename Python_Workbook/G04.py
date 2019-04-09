
total_charge = 0
while 1 :
    kind = int(input("1)매매 2)임대 0)계산종료"))
    if kind == 0 : 
        print("지금까지 수수료 총액은 %d원입니다."%(total_charge))
        break
    else :
        money = int(input("거래금액은?"))
        if kind == 1 :
            if money < 50000000 : 
                charge = 0.006 * money
                if charge > 250000 : 
                    charge = 250000
            elif money < 200000000 : 
                charge = 0.005 * money
                if charge > 800000 : 
                    charge = 800000
            else : charge = 0.004 * money
            
        elif kind == 2 :
            if money < 20000000 : 
                charge = 0.005 * money
                if charge > 70000 : 
                    charge = 70000
            elif money < 50000000 : 
                charge = 0.005 * money
                if charge > 200000 : 
                    charge = 200000
            elif money < 100000000 : 
                charge = 0.004 * money
                if charge > 300000 :
                    charge = 300000
            else : charge = 0.003 * money
    
        print("수수료는 %d원 입니다"%(charge))
    total_charge += charge