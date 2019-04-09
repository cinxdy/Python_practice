kind = input("Input C or F ")
print(kind)

if kind == 'F' :
    c_degree = int(input("Input C degree "))
    f_degree = c_degree * 1.8 + 32
    print("F degree is ",f_degree,".")

elif kind == 'C' :
    f_degree = int(input("Input F degree "))
    c_degree = (f_degree - 32) / 1.8
    print("C degree is ",c_degree,".")

