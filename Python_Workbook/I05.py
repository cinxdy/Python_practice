def MaxOfTen():
    print("Max of Ten numbers")
    max = 0
    for i in range(10) :
        number=int(input("insert %dth number : "%(i+1)))
        if number > max : max = number
    return max

print("MAX : %d"%MaxOfTen())
