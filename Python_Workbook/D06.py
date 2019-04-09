count1 = 0
count2 = 0
count3 = 0
count4 = 0

for i in range(0,10) :
    m2_area = float(input('Area?(m2) '))
    pyung_area = m2_area / 3.305
    print('Area : ',format(pyung_area,".1F"),'평')

    if pyung_area < 15 : count1+=1
    elif pyung_area < 30 : count2+=1
    elif pyung_area < 50 : count3+=1
    else : count4+=1

print('소형 아파트 : ',count1)
print('중소형 아파트 : ',count2)
print('중형 아파트 : ',count3)
print('대형 아파트 : ',count4)