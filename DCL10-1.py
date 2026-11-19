# print("Start")
name = input("Enter Your Name ")
print(f"Your name is {name}")
# print(type(name))
age = int(input("Enter your age: "))
print(f"Your age is {age}")
# print("Stop")
height = float(input("Enter your Height: "))
print(f"Your Height is {height}")
cmplx = complex(input("Enter complex number: "))
print(f"Your Complex number: {cmplx}")
# print(type(cmplx))
citizen = bool(input("Are You Indian Citizen? "))
status = eval(input("What's Your Maritial Status? "))
print(f"Your Citizen of {citizen} and your marital status is {status}")

a = 10
b = 20
l = [11, 22, 33]
res = eval("a+b+2+len(l)")
print(res)
