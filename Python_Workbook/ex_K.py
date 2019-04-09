EngDic = {}
file = open("word.txt","r")
while 1:
    line = file.readline().strip().split(":")

    if len(line) == 2 :
        EngDic[line[0]]= line[1]
    else : break
file.close()