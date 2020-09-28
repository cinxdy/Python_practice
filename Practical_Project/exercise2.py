#I don't know about repetition

#doing = 1
#while doing == 1 : 
#    doint = 0
start = int(input("Enter the start day (0~6) >> "))
#    if start < 0 or start > 6 :
#        print("Wrong!")
#        doing = 1
amount = int(input("Enter the amount of days (28~31) >> "))
#    if start < 28 or start > 31 :
#        print("Wrong!")
#        doing = 1

day = ("Sun","Mon","Tue","Wed","Thu","Fri","Sat")

for j in range(7):
    print(day[j],end='\t')

print()

for j in range(start):
    print(" ",end='\t')

for j in range(1,32):
    print(j,end='\t');
    if j % 7 == 7-start :
        print()
        
print()