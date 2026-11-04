weight = float(input("Enter weight : "))
units = input("Enter units (kg or lb) : ")

if units == "kg":
    print(f"Weight in pounds: {weight * 2.20462}")
elif units == "lb":
    print(f"Weight in kilograms: {weight * 0.453592}")
else:
    print("Invalid units. Please enter 'kg' or 'lb'.")
