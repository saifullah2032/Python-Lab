s1 = 'fruits mostly are sweet'
s2 = 'Vegies mostly TASTELESS'
print(f"Original String: {s1}")
print(f"Original String: {s2}")
# it capitalizes the 1st character of string
print(f"Capitalization of 1st char: {s1.capitalize()}")
# it capitalizes 1st char of every word of sting
print(f"Title converstion of string: {s1.title()}")
# it changes all char of string to upper case
print(f"Upper Case conversion: {s1.upper()}")
# it changes all char of string to lower case
print(f"Lower case Conversion: {s1.lower()}")
# it checks wether the string is in upper cae and returns bool
print(f"Check wether is upper or not: {s1.isupper()}")
# it checks wether the string is in lower cae and returns bool
print(f"Check wether is lower or not: {s1.islower()}")
# it Converts the upper to lower and lower to upper
print(f"Swaping of case: {s2.swapcase()}")
# it returns the no.of occurences of a substring in main string
print(f"Count of 'Most' in s2: {s2.count('most')}")
print(f"Count of 'S' in s2: {s2.count('s')}")
# it returns the index of the 1st occurence of substring
print(f"Index of 'S' in s2: {s2.index('s')}")
# you can specify both start and end to search as well
print(f"Index of 'S' in s2: {s2.index('s', 6, 15)}")
# print(f"Index of 'S' in s2: {s2.index('s', -1, -15)}") negative doesn't works
# it returns bool value if the main string starts with sub string
print(f"Starts With the sub string 'f': {s1.startswith('f')}")
# you can specify both start and end to search as well
print(f"Starts With the sub string 's': {s1.startswith('s', 9, 15)}")
# it returns bool value if the main string ends with sub string
print(f"Starts With the sub string 't': {s1.endswith('t')}")
# you can specify both start and end to search as well
print(f"Starts With the sub string 's': {s1.endswith('s', 0, 6)}")
s3 = 'WHY'
print(f"Original String s3: {s3}")
# it checks wether there all in string is only aplha or not and returns bool
print(f"Check for Alpha s3: {s3.isalpha()}")
s4 = '7894561230'
print(f"Original String s4: {s4}")
# it checks wether there all in string is only digit or not and returns bool
print(f"Check for Alpha s4: {s4.isdigit()}")
s5 = 'HX5EM48PR'
print(f"Original String s5: {s5}")
# it checks wether there all in string is only digit or only alpha or both alpha & digit  or not and returns bool
print(f"Check for Alpha s5: {s5.isalnum()}")
s6 = '    Oh what is that'
print(f"Original String s6: {s6}")
# it removes Left/Leading Space Removal
print(f"Left/Leading Space Removed s6: {s6.lstrip()}")
s7 = 'Oh what is that      '
print(f"Original String s7: {s7}")
# it removes Right/Trailing Space Removal
print(f"Right/trailing Space Removed s7: {s7.rstrip()}")
s8 = '    Oh that      '
print(f"Original String s8: {s8}")
# it removes Right/Trailing and  Left/Leading Space Removal
print(f"Right/trailing Space Removed s8: {s8.strip()}")
s9 = 'YUYUYUYUYUYUYUYU'
print(f"Original String s9: {s9}")
# it replaces all the ocurence of old sub string with new sub string and returns new string
print(f"Replace 'U' with 'A' s9: {s9.replace('U', 'A')}")
s10 = 'The Longer You Live The More You Realize that this world is mere Oasis of Happines'
print(f"Original String s10: {s10}")
print(f"Replace space with none s10: {s10.replace(' ', '')}")
# it splits the split wherever there's space in string and returns in list form
print(f"After using split: {s10.split()}")
s11 = '456-798-123-795'
print(f"After using split: {s11.split('-')}")
s12 = 'shangchi@gmail.com'
s13 = s12.split('@')
print(s13)
print(len(s13[0]))
# join the collection of strings with a seprator value into 1 string
words = ["Tom", "Jerry", "Ben10"]
s14 = " and ".join(words)
print(f"Usage of Join: {s14}")
dates = ['15', '08', '1947']
date = "-".join(dates)
print(date)
