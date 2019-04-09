digit=int(input("큰 수를 입력하세요"))
a=digit
sum=0
i=0
b=[]
while a != 0 :
    b.append( a % 10 )
    sum += a % 10
    a //= 10 #a=a/10
    i+=1

for j in range(i):
    print(b[i-j-1],end='')
    if j!=i-1 :
        print("+",end='')
print("=",sum)