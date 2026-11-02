operator = input("Enter the operator (+, -, *, /): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
if operator == "+":
    result = a + b
    print(f"The result of {a} + {b} is: {result:.2f}")
elif operator == "-":
    result = a - b
    print(f"The result of {a} - {b} is: {result:.2f}")
elif operator == "*":
    result = a*b
    print(f"The result of {a} * {b} is : {result:.2f}")
elif operator == "/":
    if b != 0:
        result = a / b
        print(f"The result of {a} / {b} is: {result:.2f}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
