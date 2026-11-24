print('--------Conditional - Statements-------')
print('--If-Statement--')
number = int(input("Enter the number:"))
if number > 0:
    print(f"The Entered Number is Positive: {number}")
if number % 2 == 0:
    print(f"The Number is even: {number}")
name = input("Enter your name:")
if name.find('A') >= 0:
    print(f"Name Is Valid: {name}")
    # print(name.find('A'))
print('--If - else - Statement--')
if number % 5 == 0 and number % 7 == 0:
    print(f"The number divisible by 5 & 7: {number}")
else:
    print(f"{number} is not divisible by both 5 & 7")
if name.find('g') == 0 and len(name) > 6:
    print(f"Name Is Valid contains 'g' : {name}")
else:
    print(f"Name Not Is Valid: {name}")
