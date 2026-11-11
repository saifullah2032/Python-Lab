print('-----DICTIONARY-METHODS--------')
d1 = {}
# Set default is used for seting values into dict by both key and value if no value but key is provided then it's 'NONE' value be default
d1.setdefault(2, 20.4)
d1.setdefault(3)
print(d1)
# Update it adds one dict into another dict
d2 = {1: 10, 2: 20.0}
print(d2)
d3 = {3: 30, 4: 40}
print(d3)
d2.update(d3)
print(f"After Updation: {d2}")
# Get it will return the value based on the key if not present then "NONE"
print(f"Get value at 3: {d2.get(3)}")
print(f"Get value where no key present: {d2.get(6)}")
# pop it removes the key and returns the value
print(f"Pop on key 3: {d2.pop(3)}")
# pop item it removes & returns the last item in form of tuple/ on empty dict it will throw error
d2[6] = 30
print(f"Pop item: {d2.popitem()}")
# Clear it removes all the elements in the dict
d4 = {1: 10, 2: 30, 3: 40, 5: 60}
d4.clear()
print(f"After using Clear: {d4}")
# keys it returns the List of Keys of Dict
print(f"The List of Keys in Dict: {d2.keys()}")
# Values it returns the List of Values of Dict
print(f"The List of Values in Dict: {d2.values()}")
# Items it returns the List of Items of Dict which the items are tuples
print(f"The List of items in Dict: {d2.items()}")
