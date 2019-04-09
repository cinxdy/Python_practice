s1 = input("first string? ")
s2 = input("second string? ")
list1 = list(s1.lower())
list2 = list(s2.lower())

list1.sort(reverse=True)
list2.sort(reverse=True)

print(list1,list2)
ch = 1
i=0
while 1 :
    if list1[i].isalpha() and list2[i].isalpha() :
        break
    if list1[i]!=list2[i] :
        ch = 0
        break
    i+=1

if ch == 1 : print("Anagram")
else : print("Not Anagram")