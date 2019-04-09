count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

while 1 :
    width, height = map(int,input('Width, Height?').split())
    if width<=0 or height<=0 : break

    if width == height : count1 += 1
    elif width >= 2*height : count2 += 1
    elif height >= 2*width : count3 += 1
    elif width > height : count4 += 1
    elif height > width : count5 += 1

print('정사각형 : ',count1)
print('좌우로 길쭉한 직사각형 : ',count2)
print('위아래로 길쭉한 직사각형 : ',count3)
print('일반적인 가로형 직사각형 : ',count4)
print('일반적인 세로형 직사각형 : ',count5)