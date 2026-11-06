print('---------SET-----------')

empty_set = set()
print(f"Type of data: {type(empty_set)}")
print(f"Length of empty set: {len(empty_set)}")
food = {'biriyani', 'curry', 'rice', 'fry', 'dosa'}
print(f"Set: {food}")  # unordered data type
# print(help(set)) to find and understand methods in set
print()
print('---------SET-Methods----------')
s1 = set()
s1.add(10)  # add method adds a value to the set
s1.add(30)
print(f"ADD Method: {s1}")
s2 = {20, 40, 50, 60}
s3 = {10, 80, 90}
s2.update(s3)  # adds a collection to another collection of set
print(f"The update method used:{s2}")
# food.update(s2) update method adds a collection to another collection of set of different data type
# print(f"Updated food set: {food}")
print(f"food set: {food}")
food.pop()  # removes a random value from the set
print(f"Pop method used: {food}")

food.remove('curry')  # removes a specific value from the set
print(f"Remove method used: {food}")
