filename = input("Enter the file name to read >> ")
filein = open(filename,'rt')
filename = input("Enter the file name to write >> ")
fileout = open(filename,'wt')

for line in filein :
    sum = 0
    numlist = line.split(' ')
    for num in numlist :
        sum += float(num)
    fileout.write("%f\n"%sum);
    print(sum)

filein.close()
fileout.close()