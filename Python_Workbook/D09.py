while 1 :
    dan = int(input('dan?'))
    if dan <2 or dan>9 : print('Wrong!')
    else :
        for i in range(1,10) :
            print(dan,'X',i,'=',dan*i)
        break