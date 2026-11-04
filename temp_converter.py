temp = float(input("Enter temperature: "))
temp_unit = input("Enter temperature unit (C or F): ")
if temp_unit == "C":
    print(f"Temperature in Fahrenheit: {temp * 9/5 + 32}")
elif temp_unit == "F":
    print(f"Temperature in Celsius: {(temp - 32) * 5/9}")
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
