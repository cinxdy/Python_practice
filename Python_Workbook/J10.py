def fibonacci(n):
    if n == 1 or n == 2 : return 1
    else : return fibonacci(n-1)+fibonacci(n-2)
        
for i in range(2,18):
    print("%dth Ratio (%d/%d) : %f"%(i,fibonacci(i+1),fibonacci(i),fibonacci(i+1)/fibonacci(i)))
    