rows = int(input("Enter the no.of rows: "))
columns = int(input("Enter the no.of columns: "))
symbol = input("Enter the Symbol you like to print: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()
