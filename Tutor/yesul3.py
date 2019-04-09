digit=input("큰 수를 입력하세요")

sum=0
for i in range(len(digit)):
    num = int(digit[i])
    sum += num

    print(num,end='')
    if i!=len(digit)-1 :
        print("+",end='')

print("=",end='')
print(sum)