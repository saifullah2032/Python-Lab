temp = int(input("Enter temperature: "))
is_raining = False
is_sunny = True

if temp > 35 or temp < 0 or is_raining:
    print("It's not a good day to go outside.")
elif temp >= 28 and is_sunny:
    print("It's not a good day to go outside.")
elif temp <= 26 and temp >= 24 and not is_raining:
    print("It's a good day to go outside.")
else:
    print("It's not a good day to go outside.")
