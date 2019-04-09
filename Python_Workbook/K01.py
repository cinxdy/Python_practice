num= [0,0,0,0,0]
menu=[0,0,0,0,0]
orgin=[0,0,0,0,0]
price =[0,0,0,0,0]

file = open("menu.txt","w")

for i in range(5):
    num[i],menu[i],orgin[i],price[i] = input("%dth number,menu,orgin,price : "%(i+1)).split()
    
print("메뉴번호\t 메뉴이름\t 원산지\t 1인분 가격")
for i in range(5):
    print("%4d\t %4s\t %4s\t %4d"%(int(num[i]),menu[i],orgin[i],int(price[i])))

print("menu.txt에 저장")
for i in range(5):
    file.write("%d %s %s %d\n"%(int(num[i]),menu[i],orgin[i],int(price[i])))
file.close()