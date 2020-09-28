#전체 element중 중복되는 값이 있으면 “exist duplicate elements” 출력하고 중복되는 2개의 값이 위치하는 index도 출력하기
#작성일자_2019년 04월 09일
#작성자_김은우

import sys # 예외처리를 위해 sys 모듈 가져
n=[]
for i in range(10):
    while True : #i 번째 수를 입력받음
            try:
                    n.append( int(input("첫번째 수 입력: ")) ) #만약 정수가 들어오면 입력을 받고 브레이크 걸어줌
                    break
            except ValueError:
                    print('처리할 수 없습니다. 정수로 입력해주세요.') #만약 정수가 들어오지 않으면 다시 입력하고 함
