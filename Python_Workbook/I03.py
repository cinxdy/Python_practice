def AskBiman(height,weight) :
    bmi = weight/((height/100)**2)
    if bmi < 18.5 : print("저체중입니다.")
    elif bmi < 23 : print("정상체중입니다.")
    elif bmi < 25 : print("과체중입니다.")
    elif bmi < 30 : print("경도비만입니다.")
    else : print("고도비만입니다.")

i=0
while i!=10 :
    height, weight = map(int,input("%dth height(cm) and weight(kg) "%(i+1)).split())
    AskBiman(height,weight)
    i+=1