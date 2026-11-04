empty_list = []  # initialization-1
empty_list1 = list()  # initialization-2
print(empty_list)
print(empty_list1)
print(type(empty_list))
fruits = ['apple', 'banana', 'cherry']  # initialization-3
print(fruits)
print(type(fruits))
print(len(fruits))
print(len(empty_list))
print(fruits[0])  # postive indexing
print(fruits[-3])  # negative indexing
# print(fruits[3])  # IndexError: list index out of range
# print(fruits[-4])  # IndexError: list index out of range
vegetables = ['carrot', 'potato', 'tomato', 'carrot']  # duplicate values
print(vegetables)
response = ['yes', 'no', 'maybe', 'yes', 50, 06.5]  # duplicate values
print(response)
response[1] = 0  # modifying the list
print(response)
# List Methods
# print(help(list))
empty_list.append('grapes')  # adding a single element to the list
print(empty_list)
empty_list.append('mango')
empty_list.append('banana')
print(empty_list)
# empty_list.append('apple', 'orange', 'kiwi')  #TypeError: list.append() takes exactly one argument (3 given)
empty_list.insert(31, 'kiwi')  # adding an element at a specific index
print(empty_list)
empty_list.insert(0, 'orange')
print(empty_list)
fruits.extend(empty_list)  # adding multiple elements to the list
print(fruits)
