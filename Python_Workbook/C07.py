mega = int(input('mega byte?'))
byte = mega * 1024 * 1024

kind = int(input('(1) Wi-Fi (2) BlueTooth (3) LTE (4) USB'))

if kind == 1 :
    time = byte / 1500000
elif kind == 2 :
    time = byte / 300000
elif kind == 3 :
    time = byte / 1000000
elif kind == 4 :
    time = byte / 60000000

print('time',time,'s')