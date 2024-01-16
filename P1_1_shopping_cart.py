"""
Display a menu with options related to a shopping cart
Implement While loop to keep the menu running (after user has selected options)
Users able to view, add, remove and get total cost for cart
Provides the user with the option to end the program
"""

print("-" * 50)
print("Welcome to my shop!")
print("-" * 50)

cat_food_count = 0
dog_food_count = 0
balls_count = 0
treats_count = 0

# Continuous loop for user input until option '4' entered
while True:  
    menu = input("Select one of the following:\n\
    1. Add Item \n\
    2. Remove Item \n\
    3. View total\n\
    4. Checkout\n\
Type number option here: ")
    
    # Option 1 - Add item to basket increasing count
    if menu == "1":
        print("\nItems available are: \n\
    1. Cat Food - £5 \n\
    2. Dog Food - £5 \n\
    3. Balls - £2 \n\
    4. Treats - £2 \n")
        add_item = input("What item would you like to add? (e.g 1):\t")
        
        if add_item == "1":
            cat_food_count += 1
            print("\nCat Food added\n")
        elif add_item == "2":
            dog_food_count +=1
            print("\nDog Food added\n")
        elif add_item == "3":
            balls_count +=1
            print("\nBalls added\n")
        elif add_item == "4":
            treats_count +=1
            print("\nTreats added\n")
        else:  
            print("\nInvalid option, try the main menu again!\n")
    
    # Option 2 - Remove items from basket decreasing count
    elif menu == "2":
        remove_item = input("What item would you like to remove? (e.g 1):\t")
        if remove_item == "1":
            if cat_food_count > 0:
                cat_food_count -= 1
                print("\nCat Food removed\n")
            else:
                print("\nThere is no Cat Food to remove\n")
        elif remove_item == "2":
            if dog_food_count > 0:
                dog_food_count -=1
                print("\nDog Food removed\n")
            else:
                print("\nThere is no Dog Food to remove\n")
        elif remove_item == "3":
            if balls_count > 0:
                balls_count -=1
                print("\nBalls removed\n")
            else:
                print("\nThere are no Balls to remove\n")
        elif remove_item == "4":
            if treats_count > 0:
                treats_count -=1
                print("\nTreats removed\n")
            else:
                print("'\nThere are no Treats to remove\n")
        else:
            print("\nInvalid option, try the main menu again!\n")
    
    # Option 3 - Display items in basket and calculate total cost
    elif menu == "3":

        cat_food_cost = cat_food_count * 5
        dog_food_cost = dog_food_count * 5
        balls_cost = balls_count * 2
        treats_cost = treats_count * 2

        total_cost = cat_food_cost + dog_food_cost + balls_cost + treats_cost

        print("-" * 50)
        print(f"Your current basket is as follows: \n\
              {cat_food_count} Cat Food Items at £{cat_food_cost} \n\
              {dog_food_count} Dog Food Items at {dog_food_cost} \n\
              {balls_count} Balls Count Items at £{balls_cost} \n\
              {treats_count} Treats Count Items at £{treats_cost} \n\
              \nYour Cart Total is £{total_cost}")
        print("-" * 50)

    # Option 4 - Exit cart menu
    elif menu == "4":
        print("-" * 50)
        print("Thank you for shopping with us! Have a good day!")
        print("-" * 50)
        break


    else:
        print("\nInvalid option. Please try again!\n")


