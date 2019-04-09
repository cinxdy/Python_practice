from random import *
count = 0
answer = randint(1,100)

while 1:
    number_try = int(input("Try guess number between 1 and 100 "))
    count+=1
    if number_try > answer : print("answer is smaller number")
    elif number_try < answer : print("answer is bigger number")
    else : 
        print("You got it! try count : %d"%count)
        break