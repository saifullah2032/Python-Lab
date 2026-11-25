print('--------Conditional - Statements-------')
# If-elif-else statement
z = int(input("Enter a number for z: "))
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z is zero")
print('-------------------------')
marks = int(input("Enter your marks: "))
if marks >= 90 and marks <= 100:
    print(f"Grade: O, marks: {marks}")
elif marks >= 80 and marks < 90:
    print(f"Grade: A, marks: {marks}")
elif marks >= 65 and marks < 80:
    print(f"Grade: B, marks: {marks}")
elif marks >= 45 and marks < 65:
    print(f"Grade: C, marks: {marks}")
elif marks >= 35 and marks < 45:
    print(f"Grade: D, marks: {marks}")
elif marks > 100 or marks < 0:
    print("Marks Should be in valid range 0 - 100")
else:
    print(f"Grade: F, marks: {marks}")

print('----------Match-Case---------')
food = input("Enter Your Choice of Food (A/B/C/D/E/F) : ")
match food.upper():
    case 'A':
        print("Your Food is Biriyani")
    case 'B':
        print("Your Food is Chikcen Biriyani")
    case 'C':
        print("Your Food is Mutton Biriyani")
    case 'D':
        print("Your Food is Dum Biriyani")
    case 'E':
        print("Your Food is Hydrabadi Biriyani")
    case 'F':
        print("Your Food is Afghani Biriyani")
    case _:
        print("Biriyani completed")
print('----------------')
comnd = input("Enter your command: ")
if len(comnd) == 1:
    match comnd.upper():
        case 'S':
            print('Save Command')
        case 'C':
            print('Copy Command')
        case 'V':
            print('Paste Command')
        case 'X':
            print('Cut Command')
        case 'Z':
            print('Undo Command')
        case 'Y':
            print('Redo Command')
        case _:
            print('Invalid Command')
print('-----Nested-If----------')
username = input("Enter the Username: ")
if len(username) == 12 and username.find('@') >= 0:
    print("User Exists")
    password = input("Enter your Password: ")
    if len(password) == 8 and password.isalnum:
        print("Login Succesful")
    else:
        print("Incorrect Password")
else:
    print("User Doesn't Exist")
print('------------------')
age = int(input("Enter Your age: "))
if age >= 0 and age <= 18:
    print(f"Your Age is {age} and ur Minor")
    if age >= 0 and age <= 12:
        print("Child 👦")
    else:
        print("Teenager ⛹️‍♂️")
elif age > 18 and age <= 100:
    print(f"Your Age is {age} and ur an Adult")
    if age > 18 and age <= 60:
        print("Working Adult ⚒️")
    else:
        print("Senior Citizen 👴")
else:
    print("Incorrect Age Entered 💀")
print('-----------------------')
marks1 = int(input("Enter Your Marks: "))
print(f"You have {'Passed' if marks1 > 35 else 'Failed'} Exam")
