"""
Display a menu with options related to a shopping cart
Implement While loop to keep the menu running (after user has selected options)
Users able to view, add multiple, remove multiple and get total cost for cart
Defensive programming for user error
Provides the user with the option to end the program and 'checkout'
"""

print("-" * 50)
print("Welcome to my shop!")
print("-" * 50)

cat_food_count = 0
dog_food_count = 0
balls_count = 0
treats_count = 0

# Prices added as variable to make easier to change
cat_food_price = 5.00  
dog_food_price = 5.00
balls_price = 2.50
treats_price = 2.00

# Continuous loop for user input until option '4' entered
while True:  
    menu = input("Select one of the following e.g. '1':\n\
    1. Add Item \n\
    2. Remove Item \n\
    3. View Cart\n\
    4. Checkout\n\
Type number option here: ")
    
    # Option 1 - Add item to basket increasing count
    if menu == "1":
        print(f"\nItems available are:\n\
    1. Cat Food - £{"%.2f"%(cat_food_price)}\n\
    2. Dog Food - £{"%.2f"%(dog_food_price)}\n\
    3. Balls - £{"%.2f"%(balls_price)}\n\
    4. Treats - £{"%.2f"%(treats_price)}\n")
        
        # Loop to handle user error and ask user to try again if not 1-4 input
        while True:
            add_item = input("What item would you like to add? e.g '1':\t")
            if add_item.isnumeric():
                add_item = int(add_item)
                if add_item > 0 and add_item <= 4:
                    break
                else:
                    print("Invalid option, must be between 1 and 4. Try again.")
            else:
                    print("Invalid option, must be a positive integer. Try again.")
        
        # Loop to handle user error if not a positive integer
        while True:
            add_quantity = input("How many would you like to add?\t")
            if add_quantity.isnumeric():
                add_quantity = int(add_quantity)
                break
            else:
                print("Invalid input, must be a positive integer. Try again.")

        if add_item == 1:
            cat_food_count += (add_quantity)
            print(f"\n{add_quantity}x Cat Food added\n")
        elif add_item == 2:
            dog_food_count += (add_quantity)
            print(f"\n{add_quantity}x Dog Food added\n")
        elif add_item == 3:
            balls_count += (add_quantity)
            print(f"\n{add_quantity}x Balls added\n")
        elif add_item == 4:
            treats_count += (add_quantity)
            print(f"\n{add_quantity}x Treats added\n")
        else:  
            print("\nInvalid option, try the main menu again!\n")
    
    # Option 2 - Remove items from basket decreasing count
    elif menu == "2":
        print(f"\nItems available are:\n\
    1. Cat Food\n\
    2. Dog Food\n\
    3. Balls\n\
    4. Treats")

        # Loop to handle user error and ask user to try again if not 1-4 input
        while True:
            remove_item = input("What item would you like to remove? e.g '1':\t")
            if remove_item.isnumeric():
                remove_item = int(remove_item)
                if remove_item > 0 and remove_item <= 4:
                    break
                else:
                    print("Invalid option, must be between 1 and 4. Try again.")
            else:
                    print("Invalid option, must be a positive integer. Try again.")
        
        # Loop to handle user error if not a positive integer
        while True:
            remove_quantity = input("How many would you like to remove?\t")
            if remove_quantity.isnumeric():
                remove_quantity = int(remove_quantity)
                break
            else:
                print("Invalid input, must be a positive integer.  Try again.")

        if remove_item == 1:
            if cat_food_count >= remove_quantity:
                cat_food_count -= remove_quantity
                print(f"\n{remove_quantity}x Cat Food removed\n")
            else:
                print("\nSorry that is too many Cat Foods to remove\n")
        elif remove_item == 2:
            if dog_food_count >= remove_quantity:
                dog_food_count -= remove_quantity
                print(f"\n{remove_quantity}x Dog Food removed\n")
            else:
                print("\nSorry that is too many Dog Food to remove\n")
        elif remove_item == 3:
            if balls_count >= remove_quantity:
                balls_count -= remove_quantity
                print(f"\n{remove_quantity}x Balls removed\n")
            else:
                print("\nSorry that is too many Balls to remove\n")
        elif remove_item == 4:
            if treats_count >= remove_quantity:
                treats_count -= remove_quantity
                print(f"\n{remove_quantity}x Treats removed\n")
            else:
                print("'\nSorry, that is too many Treats to remove\n")
        else:
            print("\nInvalid option, try the main menu again!\n")
    
    # Option 3- Display items in basket and calculate total cost
    elif menu == "3":

        cat_food_cost = cat_food_count * cat_food_price
        dog_food_cost = dog_food_count * dog_food_price
        balls_cost = balls_count * balls_price
        treats_cost = treats_count * treats_price

        total_cost = cat_food_cost + dog_food_cost + balls_cost + treats_cost

        print("-" * 50)
        print(f"Your current basket is as follows:\n\
              {cat_food_count}x Cat Food at £{"%.2f"%(cat_food_cost)}\n\
              {dog_food_count}x Dog Food at £{"%.2f"%(dog_food_cost)}\n\
              {balls_count}x Balls at £{"%.2f"%(balls_cost)}\n\
              {treats_count}x Treats at £{"%.2f"%(treats_cost)}\n\
              \nYour Cart Total is £{"%.2f"%(total_cost)}")
        print("-" * 50)

    # Option 4 - Exit cart menu
    elif menu == "4":
        print("-" * 50)
        print("Thank you for shopping with us! Have a good day!")
        print("-" * 50)
        break

    else:
        print("\nInvalid option. Please try again!\n")
