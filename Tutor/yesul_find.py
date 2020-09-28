# find_transfer.py
#다음과 같이 영어 문장과 찾을 단어를 입력 받아서,
#그 단어가 입력된 문장에 몇 번 나타나는지 출력한다.
#또 찾은 단어는 모두 대문자로 바꾼 후 문장을 출력한다
#19/4/1-10
#조예슬


input_str=input("Input a sentence :")
input_find=input("Input a word for search :")

count = input_str.count( input_find )
input_str = input_str.replace( input_find, input_find.upper() )

print(input_str)
print("count : ", count)
