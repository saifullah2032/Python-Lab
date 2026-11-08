# prime numbers and fibonacci series
# prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers. A prime number is only divisible by 1 and itself.
# Fibonacci series is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1.
prime_number = int(
    input("Enter a number to check if it's a prime number or not: "))
if prime_number > 1:
    for prime in range(2, prime_number):
        if (prime_number % prime) == 0:
            print(prime_number, "is not a prime number")
            break
    else:
        print(prime_number, "is a prime number")
else:
    print(prime_number, "is not a prime number")

fibonacci_terms = int(
    input("Enter the number of terms for Fibonacci series: "))
n1, n2 = 0, 1
count = 0
while count < fibonacci_terms:
    print(n1, end="")
    nth = n1+n2
    n1 = n2
    n2 = nth
    count += 1
    if count < fibonacci_terms:
        print(", ", end="")
    else:
        print()
