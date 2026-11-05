fruits = ['apple', 'banana', 'cherry', 'orange']
demo_clr = ['fire', 'earth', 'wind', 'water', 'soul']
# removes last element and returns
print(f'Last Item / Default item: {fruits.pop()}')
print(fruits)
fruits.append('orange')  # adds at last
print('----------------------')
print(f'Index based pop: {fruits.pop(1)}')  # index can also be used
print(fruits)
fruits.insert(1, 'banana')
print('----------------------')
fruits.extend(['cherry', 'kiwi', 'cherry'])
print(fruits)
fruits.remove('cherry')  # removes specific 1st ocurrence of specified object
print(f'1st ocurrence of cherry removed: {fruits}')
print('----------------------')
print(demo_clr)
demo_clr.clear()  # it clears the entire list makes it empty list
print(f'the demo list is cleared: {demo_clr}')
print('----------------------')
print(fruits)
fruits.sort()  # sorts the list elements by default assending order, for strings it's alphabetical order / mixed data types can't be sorted
print(f'the list is sorted: {fruits}')
print('----------------------')
print(fruits)
fruits.reverse()  # reveses the order of the string / any kind of data is can be reversed even mix od diff data types
print(f'the reverse is used: {fruits}')
print('-----------------------')
print(fruits)
# it counts the specified objects occurences
print(f'Count of Cherries present in list: {fruits.count("cherry")}')
print('-----------------------')
print(fruits)
# it returns the index of the specified object
print(f'Index of the first cherry: {fruits.index("cherry")}')
# index can also be used with start and end range
print(f'Index of the other cherry: {fruits.index("cherry", 3, 5)}')
