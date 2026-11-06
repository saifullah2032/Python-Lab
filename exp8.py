food = input("enter your food (q to Quit):")
food = food.lower()
while not food == "q":
    food = food.upper()
    print(f"your Food is {food}")
    food = input("enter your another food (q to Quit):")
    food = food.lower()
print("Bye! Thanks for using our program.")
