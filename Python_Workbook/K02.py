file = open("menu.txt","r")

print("menu.txt에서 메뉴정보를 읽어들였습니다.")

print("메뉴번호\t 메뉴이름\t 원산지\t 1인분가격")
while 1:
    line = file.readline().strip().split()
    if len(line)==4 :
        print("%5d\t %5s\t %5s\t %5d"%(int(line[0]),line[1],line[2],int(line[3])))
    else : break