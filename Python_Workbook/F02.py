score = []
max=0
min=10
total=0
for i in range(10) :
    newnum = float((input("%dth point "%(i+1))))
    score.append(newnum)
    if max<score[i] : max = score[i]
    if min>score[i] : min = score[i]

for i in range(10) :
    if score[i]!=max and score[i]!=min :
        total+=score[i]
average = total/8
print("average without max and min : %.1f"%(average))