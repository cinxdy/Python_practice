month = int(input('Month?'))
day = int(input('Day?'))
day_count = 0

if month>12 or month<0 : print('Wrong Month!')

if month>11 : day_count += 30
if month>10 : day_count += 31
if month>9 : day_count += 30
if month>8 : day_count += 31
if month>7 : day_count += 31
if month>6 : day_count += 30
if month>5 : day_count += 31
if month>4 : day_count += 30
if month>3 : day_count += 31
if month>2 : day_count += 28
if month>1 : day_count += 31

day_count += day

print(day_count,'th day')