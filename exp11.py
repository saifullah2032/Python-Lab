rows = int(input("Enter the no.of rows: "))
columns = int(input("Enter the no.of columns: "))
symbol = input("Enter the symbol to be used: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    columns -= 1
    print()
