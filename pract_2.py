# Factorial Numbers, the product of all positive integers less than or equal to a given number.
factorial_number = int(input("Enter a number to calculate its factorial: "))

if factorial_number < 0:
    print("Factorial is not defined for negative numbers.")
elif factorial_number == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, factorial_number + 1):
        factorial *= i
    print(f"The factorial of {factorial_number} is {factorial}.")

# Armstrong Numbers, a number that is equal to the sum of its own digits raised to the power of the number of digits.
armstrong_number = int(
    input("Enter a number to check if it's an Armstrong number: "))

# Convert the number to a string to easily access each digit
num_str = str(armstrong_number)
num_digits = len(num_str)

# Calculate the sum of each digit raised to the power of the number of digits
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)

# Check if the sum is equal to the original number
if sum_of_powers == armstrong_number:
    print(f"{armstrong_number} is an Armstrong number.")
else:
    print(f"{armstrong_number} is not an Armstrong number.")
