charge = [5000,10000,15000,3000]
v_count = [ 0 for i in range(4)]
total_count = 0
total_sum = 0
name = ["초등학생","청소년","일반인","경로대상"]

team_count = int(input("오늘 방문한 팀 수를 입력하세요 "))

for i in range(team_count) :
    count = list(map(int,input("%d번팀 인원수(초등학생, 청소년, 일반, 경로대상)를 입력하세요. "%(i+1)).split()))
    membership = int(input("%d번팀 할인카드 종류(카드없음:0, 일반등급:1, VIP등급 :2)를 입력하세요. "%(i+1)))

    sum = 0
    for j in range(4) :
        sum += count[j]*charge[j]
        v_count[j] += count[j]
        total_count += count[j]

    if membership == 1 : sum *= 0.90
    elif membership == 2 : sum *= 0.80

    print("%d번팀 입장료는 %d원입니다."%(i+1,sum))
    total_sum += sum
print()
print("오늘 총 방문자 수는 %d명입니다."%total_count)
for i in range(4) :
    print("%s 수는 %d명입니다."%(name[i],v_count[i]))
print()
print("총 입장료는 %d원입니다."%total_sum)