print("---------Arithmetic-------------")
print(f"Add: {5+2}")  # add
print(f"Sub: {5-2}")  # sub
print(f"mul: {5*2}")  # mul
print(f"division (Quotient in float): {5/2}")  # division (Quotient in float )
# floor division (Quotient in int )
print(f"floor division (Quotient in int): {5//2}")
print(f"modulo (rmainder): {5 % 2}")  # modulo (rmainder)
print(f"expon/power: {5**2}")  # expon/power
print("---------Assignment-------------")
a = 5  # variable
b = 2  # variable is assigned with a value using "="
print(f"Assign: {a}")
a = 5
b = 2
a += b
print(f"Add Assign: {a}")  # add
a = 5
b = 2
a -= b
print(f"Sub Assign: {a}")  # sub
a = 5
b = 2
a *= b
print(f"mul Assign: {a}")  # mul
a = 5
b = 2
a /= b
# division (Quotient in float )
print(f"division (Quotient in float) Assign: {a}")
# floor division (Quotient in int )
a = 5
b = 2
a //= b
print(f"floor division (Quotient in int) Assign: {a}")
a = 5
b = 2
a %= b
print(f"modulo (rmainder) Assign: {a}")  # modulo (rmainder)
a = 5
b = 2
a **= b
print(f"expon/power Assign: {a}")  # expon/power
print("---------Relational-------------")
a = 5
b = 2
print(f"Equal to 5,2: {a == b}")
print(f"Not Equal to 5,2: {a != b}")
print(f"Greater to 5,2: {a > b}")
print(f"Lesser to 5,2: {a < b}")
print(f"Greater or Equal to 5,2: {a >= b}")
print(f"Lesser or Equal to 5,2: {a <= b}")
print("------------Logical-------------")
print(f" And Op: {True and True}")
print(f" And Op: {True and False}")
print(f" And Op: {False and True}")
print(f" And Op: {False and False}")
print(f" OR Op: {True or True}")
print(f" OR Op: {True or False}")
print(f" OR Op: {False or False}")
print(f" OR Op: {False or False}")
print(f" NOT Op: {not True}")
print(f" NOT Op: {not False}")
print("------------Membership------------")
# In to check if it's present returns true not in returns false
fruits = ["Apple", "Banana", "Cherry", "Orange", "Fig"]
print(f"In Op (Grape in fruits): {"Grape" in fruits} ")
print(f"In Op (Fig in fruits): {"Fig" in fruits} ")
print(f"Not In Op (Grape not in fruits): {"Grape" not in fruits} ")
print(f"Not In Op (Fig not in fruits): {"Fig" not in fruits} ")
s = "come"
print(' ' in s)
d = {21: "Krishna", 22: "Lakshmi", 23: "Maruthi"}
print(34 in d)
print("krishna" in d)
print("Krishna" in d.values())
print("------------Identity------------")
# Gives Bool val by checking the memory loc is same or not
e = 5
f = e
print(f"IS Op: {e is f}")
g = 10
h = 10
print(f"IS Op: {g is h}")
l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(l1 is l2)
print("------------Bit-Wise----------")
a = 12
# shifts the value by given no.of positions to left side
print(f"Bit wise Left Shift: {a << 2}")
# shifts the value by given no.of positions to right side
print(f"Bit Wise Right Shift: {a >> 2}")
