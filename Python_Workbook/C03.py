width = int(input('Width?'))
height = int(input('Height?'))

if width == height : print('정사각형')
elif width*2 > height : print('좌우로 길쭉한 직사각형')
elif height*2 > width : print('위아래로 길쭉한 직사각형')
elif width > height : print('일반적인 가로형 직사각형')
elif height > width : print('일반적인 세로형 직사각형')