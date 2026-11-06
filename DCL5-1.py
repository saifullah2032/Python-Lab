print('---------TUPLE-----------')
t = (10, 20, 30, 40, 50, 60, 80, 40, 60, 40)  # tuple created with list
print(t[3])  # acessing the element through index (FBI)
print(t[-2])  # RBI

t2 = (60,)  # if only 1 value then add comma "," at end to specify it as tuple
dt = type(t2)
print(dt)

# print(help(tuple))
print(t.index(40, 6, 8))
count = t.count(40)  # count
index_40 = t.index(40)  # index
index_2_40 = t.index(40, 4, 9)  # index with start and end
print(count)
print(index_40)
print(index_2_40)
