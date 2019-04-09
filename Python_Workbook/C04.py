m2_area = float(input('Area(m2)?'))
pyung_area = m2_area / 3.305

if pyung_area < 15 : print('소형 아파트')
elif pyung_area < 30 : print('중소형 아파트')
elif pyung_area < 50 : print('중형 아파트')
else : print('대형 아파트')