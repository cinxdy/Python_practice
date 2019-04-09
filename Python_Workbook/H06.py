number = [0 for i in range(5)]
pow_value = [0 for i in range(20)]

number = list(map(int,input("Input 5 numbers between 2 and 9 ").split()))

max = 0
min = 9**9+1
i=0
for a in range(5) :
    for b in range(5) :
        if a!=b :
            pow_value[i] = number[a] ** number[b]
            if max < pow_value[i] :
                max = pow_value[i]
                max_a = number[a]
                max_b = number[b]
            if min > pow_value[i] :
                min = pow_value[i]
                min_a = number[a]
                min_b = number[b]
            i+=1
        
print("\nmax : %d의 %d승인 %d"%(max_a,max_b,max))
print("min : %d의 %d승인 %d"%(min_a,min_b,min))