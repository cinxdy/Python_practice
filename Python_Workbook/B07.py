megabyte = int(input('megabytes?'))
bytes = megabyte * 1024 * 1024

usb2 = input('2.0 Y & N?')
if usb2 == 'Y':
    time = bytes / 60000000
elif usb2 == 'N':
    time = bytes / 1500000

print('time : ',int(time))