str = input("Enter the string : ")
count_all = 0
count_upper = 0
count_lower = 0
count_space = 0
count_digit = 0
count_etc = 0

for ch in str :
    if ch.isalpha() : count_all +=1
    if ch.isupper() : count_upper += 1
    elif ch.islower() : count_lower += 1
    elif ch == ' ' : count_space += 1
    elif ch.isdigit() : count_digit += 1
    else : count_etc += 1

print("총 문자 개수 %d"%count_all)
print("대문자 개수 %d"%count_upper)
print("소문자 개수 %d"%count_lower)
print("공백 개수 %d"%count_space)
print("숫자 개수 %d"%count_digit)
print("기타 문자 개수 %d"%count_etc)
