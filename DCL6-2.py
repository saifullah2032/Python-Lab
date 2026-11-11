print('---------DICTIONARY---------')
# Dictionary is an collection of items where items are pairs of key and values, no.of key=no.of value =no.of items (Must)
empty_dict = {}  # initialization
empty_dict1 = dict()
print(type(empty_dict))
print(f"Length of empty Dictionary: {len(empty_dict)}")
print(type(empty_dict1))
fruits = {1: "Apple", 2: "Banana", 3: "Cherry", 4: "Orange", 5: "Kiwi"}
print(fruits)
# it acces the key based value if key is not present then key error
print(f"Fruit at key value 3 is: {fruits[3]}")
# using this u can modify or new value to dictionary
fruits[6] = "Grape"
fruits[4] = "Mango"
print(f"New value / Modified value: {fruits}")
fruits[7] = "Grape"
print(fruits)
fruits[7] = "Berry"
print(fruits)
