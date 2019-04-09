def load_list(filename):
    list = []
    file = open(filename,"r")
    while 1:
        line = file.readline().strip().split()
        if len(line)==2 :
            list.append(line)
        else : break
    print(filename,"of ten users' info is updated.")
    file.close()
    return list

list = load_list("user.txt")
print("\nUser list")
print("------------------------")
print("No\t ID\t PW")
print("------------------------")

for i in range(10):
    print("%d\t %s\t %s"%(i+1,list[i][0],list[i][1]))
print("------------------------")