credit_number = input("Enter your credit number:")
print(credit_number[0])  # 1st element of credit number
print(credit_number[-1])  # last element of credit number
print(credit_number[1])  # 2nd element of credit number
# 1st to 4th element of credit number "4" is exclusive
print(credit_number[0:4])
# 1st to 4th element of credit number, start index is optional
print(credit_number[:4])
# 4th element to last element of credit number, end index is optional
print(credit_number[3:])
# 1st to last element of credit number, step size is 2
print(credit_number[::2])
last_four_digits = credit_number[-4:]  # last 4 digits of credit number
print(last_four_digits)
credit_number_reverse = credit_number[::-1]  # reverse of credit number
print(credit_number_reverse)
