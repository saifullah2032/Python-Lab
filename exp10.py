rows = int(input("Enter the no.of rows: "))
column_start = int(input("Enter the starting column: "))
column_end = int(input("Enter the ending column: "))
for i in range(rows):
    for j in range(column_start, column_end + 1):
        print(j, end="-")
    print()
