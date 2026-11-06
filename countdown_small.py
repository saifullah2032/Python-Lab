import time
my_time = int(input("enter the time in seconds: "))
for x in range(0, my_time):
    print(x)
    time.sleep(1)
print(my_time)
print("time's up")
