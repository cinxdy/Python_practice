str = input("Enter the string : ")
list1 = list(str.lower())
list2 = list(str.lower())
list2.reverse()

i=0
j=0
ch=1
while 1 :
    while 1 :
        if not list1[i].isalpha() :
            i+=1
        if not list2[j].isalpha() :
            j+=1
        
        if list1[i].isalpha() and list2[j].isalpha() :
            break
    if list1[i] != list2[j] :
        ch = 0
        break
    else : 
        i+=1
        j+=1
    if i==len(str)-1 or j==len(str)-1 :
        break

if ch==1 : print("Palindrome")
else : print("Not Palindrome")