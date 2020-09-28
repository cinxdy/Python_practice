#전체 element중 중복되는 값이 있으면 “exist duplicate elements” 출력하고 중복되는 2개의 값이 위치하는 index도 출력하기
#작성일자_2019년 04월 09일
#작성자_김은우

import sys # 예외처리를 위해 sys 모듈 가져




while True : #첫번째 수를 입력받음
        try:
                n1 = int(input("첫번째 수 입력: ")) #만약 정수가 들어오면 입력을 받고 브레이크 걸어줌
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.') #만약 정수가 들어오지 않으면 다시 입력하고 함
while True : #2
        try:
                n2 = int(input("두번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #3
        try:
                n3 = int(input("세번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #4
        try:
                n4 = int(input("네번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #5
        try:
                n5 = int(input("다섯번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #6
        try:
                n6 = int(input("여섯번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #7
        try:
                n7 = int(input("일곱번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #8
        try:
                n8 = int(input("여덟번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #9
        try:
                n9 = int(input("아홉번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')

while True : #10
        try:
                n10 = int(input("열번째 수 입력:"))
                break
        except ValueError:
                print('처리할 수 없습니다. 정수로 입력해주세요.')


#3-1 모든 element를 오른쪽으로 한 칸씩 이동하고, 마지막 element는 첫 번째로 옮긴 후 출력한다

n=[n1, n2, n3, n4, n5, n6, n7, n8, n9, n10] #입력 받은 값들은 n이라는 리스트에 저장함

last = n[9]
a = n.pop(9)
new_n = n.insert(0,last)

print('#3-1번 문제입니다')
print(n)

#3-2 10개 중 중간에 위치한 2개의 element를 제거하고 출력하시오.

n.pop(4) #pop를 사용해 n리스트 중 인덱스 중간 값을 제거함
n.pop(4)
print('#3-2번 문제입니다')
print(n) #중간 인덱스가 제거된 n리스트를 출력함

#3-3 전체 element중 제일 큰 수를 찾아서 그 수를 출력하시오.
print('#3-3번 문제입니다')
print('가장 큰 수는 = ', max(n)) #n리스트 중 가장 큰 수를 max를 이용해 출력함

#3-4 전체 element중 중복되는 값이 있으면 “exist duplicate elements” 출력하시오. 또한 중복되는 2개의 값이 위치하는 index도 출력하시오.
if n1 == n2 or n==2 or n2==n3 or n3==n4 or n4==n5 or n5==n6 or n6==n7 or n7==n8 : #n리스트 중에 중복되는 값이 있는지 찾아봄
        print('중복되는 수가 있습니다') #중복되는 수가 있으면 있다고 알려줌

c = 0 #count할 변수를 0으로 설정함
em_list = []
for i in range(1,7) :
    for j in range(0,6) :
        if n[j] == n[j+1] :
            temp = n[j]
            c+=1
            em_list = append(n[j]) # j를 em_list에 추가하고 싶음
            index_num = index.em_list[j] # index_num라는 변수에 em_list의 인덱스를 찾고 싶음
            if c>1 :
                print('중복되는 숫자가 있습니다')
                print('중복갯수 = ', c+1, '중복되는 숫자 = ', em_list)
            else :
                print('중복되는 숫자가 없습니다')
