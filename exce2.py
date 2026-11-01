# shopping cart program, items, quantity, price, total cost
item = input("enter the item name: ")
quantity = int(input("enter the quantity: "))
price = float(input("enter the price of the item: "))
total_cost = quantity * price
print(f"Total cost for {quantity} {item}(s) at ${price} each: ${total_cost}")
