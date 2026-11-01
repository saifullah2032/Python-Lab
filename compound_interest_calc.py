principle = float(input("Enter the principle amount: "))
time = float(input("Enter the time in years: "))
rate = float(input("Enter the rate of interest: "))
n = int(input("Enter the number of times interest is compounded per year: "))
while principle <= 0 or time <= 0 or rate <= 0 or n < 1 or n > 12:
    if principle <= 0:
        print("Principle amount must be greater than 0.")
        principle = float(input("Enter the principle amount: "))
    elif time <= 0:
        print("Time must be greater than 0.")
        time = float(input("Enter the time in years: "))
    elif rate <= 0:
        print("Rate must be greater than 0.")
        rate = float(input("Enter the rate of interest: "))
    elif n < 1 or n > 12:
        print("Number of times interest is compounded per year must be between 1 and 12.")
        n = int(input("Enter the number of times interest is compounded per year: "))
total_amount = principle * pow((1+(rate/(100*n))), n*time)
print(f"Total amount after {time} years: {total_amount}")
