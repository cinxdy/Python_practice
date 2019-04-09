def save_list(newlist,filename):
    userlist=[]
    file = open(filename,"w")
    for i in range(10):
        userlist = input("%dth ID and PW : "%(i+1)).split()
        file.write("%s %s\n"%(userlist[0],userlist[1]))
        newlist.append(userlist)
        
    print("\nUser list")
    print("------------------------")
    print("No\t ID\t PW")
    print("------------------------")

    for i in range(10):
        print("%d\t %s\t %s"%(i+1,newlist[i][0],newlist[i][1]))
    print("------------------------")
    print("Saved in",filename)
    file.close()

userlist=[]
save_list(userlist,"user.txt")