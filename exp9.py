num = int(input("enter number between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is not a valid number")
    num = int(input("Enter your Number again between 1 - 10: "))
print(f"Your Number lies between 1 - 10 : {num}")
