digit=int(input("큰 수를 입력하세요"))

a=digit
i=0
b=0
Sum=0

while a > 1 :
    a/=10 #a=a/10
    i+=1

a=digit
plus = i
while plus != 0 :
    b= a//(10**plus)
    print (b,"+",end='')
    a=a-(10**plus*b)
    plus-=1
    Sum+=b
    #print(Sum)

print("=",Sum)
