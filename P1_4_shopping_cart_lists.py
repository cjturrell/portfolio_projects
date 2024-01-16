"""
Shopping cart using lists and menu options. 
Display a menu with options related to a shopping cart
Implement While loop to keep the menu running (after user has selected options)
Users able to add and remove multiple items, view cart and exit program/'checkout'
"""

print("-" * 50)
print("Welcome to my shop!")

# Stored items, count and cost using lists
items = ["Cat Food", "Dog Food", "Balls", "Treats"]
items_count = [0, 0, 0, 0]
items_cost = [5.00, 5.00, 2.50, 2.00,]

while True:
    print("-" * 50)
    menu = input("Please choose from the options \n1. Add Item \
                 \n2. Remove Item \n3. View Cart \n4. Checkout \
                 \nWhat option e.g '1':\t")
    
    # Option 1 - add items to basket increasing count
    if menu == "1":
        print("-" * 50)
        print("Items to add:")
        for number, (item, cost) in enumerate(zip(items, items_cost)):
            print(f"{number+1}. {item} - £{"%.2f"%(cost)}")
        
        # Defensive programming loop to ensure user inputs 1-4
        while True:
            add_item = input("What item would you like to add? (e.g 1):\t")
            if add_item.isnumeric():
                add_item = int(add_item)
                if add_item > 0 and add_item <= 4:
                    break
                else:
                    print("Must be between 1 and 4 - Try again")
            else:
                    print("Must be a positive integer - Try again")
        
        # Defensive programming loop to ensure user inputs positive integer
        while True:
            add_quantity = input("How many would you like to add?\t")
            if add_quantity.isnumeric():
                add_quantity = int(add_quantity)
                break
            else:
                print("Must be a positive integer - Try again")

        items_count[add_item-1] += add_quantity
        print(f"\n{add_quantity}x {items[add_item-1]} added\n")
    
    # Option 2 - remove item
    elif menu == "2":
        print("-" * 50)
        print("Items to remove:")
        for number, item in enumerate(items):
            print(f"{number+1}. {item}")
        
        # Defensive programming loop to ensure between 1 and 4
        while True:
            remove_item = input("What item would you like to remove? (e.g 1)\t")
            if remove_item.isnumeric():
                remove_item = int(remove_item)
                if remove_item > 0 and remove_item <= 4:
                    break
                else:
                    print("Must be between 1 and 4 - Try again")
            else:
                    print("Must be a positive integer - Try again")
        
        # Defensive programming loop to ensure user inputs positive integer
        while True:
            remove_quantity = input("How many would you like to remove?\t")
            if remove_quantity.isnumeric():
                remove_quantity = int(remove_quantity)
                break
            else:
                print("Positive integers only - Try again.")
        
        if items_count[remove_item-1] >= remove_quantity:
            items_count[remove_item-1] -= remove_quantity
            print(f"\n{remove_quantity}x {items[remove_item-1]} removed\n")
        else:
            print("\nSorry that's too many to remove!\n")

    # Option 3 - calculate totals and view cart
    elif menu == "3":
        items_total = []
        for i in range(len(items_count)):
            items_total.append("%.2f"%(items_count[i] * items_cost[i]))

        print("-" * 50)
        print("Your cart is as follows: \nItems \t\t Prices")   
        for i in range(len(items)):
            print(items_count[i], 'x', items[i] , '\t £', items_total[i])
        
        sum_total = sum(map(float, items_total))
        print("Your cart total is: £", "%.2f"%(sum_total))

    # Option 4 - exit cart and checkout
    elif menu == "4":
        print("-" * 50)
        print("Thank you for shopping with us! Have a good day!")
        print("-" * 50)
        break

    else:
        print("\nInvalid option. Please try again!\n")
