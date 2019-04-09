def PrintCharWithBlank(blanks,size,ch) :
    for i in range(1,size) :
        for j in range(1,blanks+size-i) :
            print(" ",end='')
        for j in range(i) :
            print(ch,end='')
        print()

ch = input("Character : ")
size,blanks = map(int,input("Height and Blanks : ").split())
PrintCharWithBlank(blanks,size,ch)