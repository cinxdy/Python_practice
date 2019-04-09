count_all = int(input('How many people are there in your family?'))
count_young = 0 

for i in range(0,count_all) :
    birth_year = int(input('Input Birth Year '))
    age = 2019 - birth_year + 1
    if age < 20 : count_young += 1

print('Youth : ',count_young)