height = int(input('height(cm)?'))
weight = int(input('weight(kg)?'))
bmi = weight/((height/100)**2)

if bmi > 25 :
    print('biman')
else : print('not biman')