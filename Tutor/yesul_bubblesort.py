num=[]
t=0
count=0
flag=True

while count!=10 :
    t=input("추가할 element 입력 :")

    if t.isdigit() != True :
        print('정수가 아닙니다 다시 입력해주세요')

    else:
        num.append(t)
        count+=1
print(num)



for i in range(0, len(num)):
    for j in range(0, len(num)-i):
        if num[j] < num[j+1]:
            temp = num[j]
            num[j] = num[j+1];
            num[j+1] = temp
            flag=False
        elif flag==True :
            break
        else:
            print(num)
