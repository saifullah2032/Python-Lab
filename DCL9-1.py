# Slicing variable[start:end:Step] start default "0" , end default "len(variable)", step default "1".
l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
l1 = l[2:5]
l2 = l[-8:-5]
l3 = l[7:9]
l4 = l[-10:-5:2]  # l[0:5:2]
l5 = l[0:5:4]  # l[-10:-5:4]
l6 = l[-4:-7:-1]  # l[6:3:-1]
l7 = l[-2:-9:-3]  # l[8:1:-3]
l8 = l[::-1]
print(l2)
print(l1)
print(l3)
print(l4)
print(l5)
print(l6)
print(l7)
print(l8)
roll_number = "22BQ1A05G8"
stream = roll_number[-4:-2]
print(stream)
pan = 'CIA75GQ3'
last_4 = pan[-4:]
print(last_4)
