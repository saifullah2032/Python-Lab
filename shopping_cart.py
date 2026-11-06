foods = []
prices = []
total = 0
while True:
    food = input("Enter the food item (or type 'done' to finish): ")
    if food.lower() == 'done':
        break
    price = float(input(f"Enter the price for {food}: "))
    foods.append(food)
    prices.append(price)
    total += price
print("----------Shopping Cart Summary----------")
print(f"{'Food Item':<20}|{'Price'}")
for food in foods:
    print(f"{food:<20}: ${prices[foods.index(food)]:.2f}")
print()
print(f"Total: ${total:.2f}")
print("Thank you for shopping with us!")
