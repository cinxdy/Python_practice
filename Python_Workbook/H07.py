from math import *

number = [0 for i in range(10)]
bunsan = [0 for i in range(10)]
total = 0
total_bunsan = 0

number = list(map(int,input("Input 10 numbers between 1 and 100 : ").split()))

for i in range(10) :
    total += number[i]
average = total / 10

for i in range(10) :
    bunsan[i] = pow(number[i]-average,2)
    total_bunsan += bunsan[i]
average_bunsan = total_bunsan/10
std_dev = sqrt(average_bunsan)
print("Sum : %d , Average : %d "%(total,average))
print("Variance : ",bunsan)
print("Average : %.1f, Standard Deviation : %.1f"%(average_bunsan,std_dev))