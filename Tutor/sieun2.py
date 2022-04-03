def checkPass(p):
    if(len(p)<8): return False

    digit,upper,lower = 0,0,0
    for c in p:
        if(c.isupper()): upper +=1
        if(c.islower()): lower +=1
        if(c.isdigit()): digit +=1

    if(digit==0 or upper ==0 or lower==0): return False

    return True

while True:
    p = input('비밀번호 입력하시오')
    if(checkPass(p)):
        print("통과")
        break;
    else:
        print("틀립니다. 다시 입력하세요")

