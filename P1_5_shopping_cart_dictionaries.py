"""
Shopping cart using dictionaries and menu options. 
Display a menu with options related to a shopping cart
Implement While loop to keep the menu running (after user has selected options)
Users able to add and remove multiple items, view cart and exit program/'checkout'
"""
# line length vs readability??
# comment use?


# Dictionary to be updated and used by merchant
item_cost = {"cat food": 5.00, "dog food": 5.00, "balls": 2.50, "treats": 2.00}

# Set count for each dictionary item to zero
item_count = dict(item_cost)
for key, value in item_count.items():
    item_count[key] = 0

print("-" * 50)
print("Welcome to my shop!")

while True:
    print("-" * 50)
    menu = input("Please choose from the options \n1. Add Item \
                 \n2. Remove Item \n3. View Cart \n4. Checkout \
                 \nWhat option e.g '1':\t")
    
    # Option 1 - add items to basket increasing count
    if menu == "1":
        print("-" * 50)
        print("Items to add:")
        for key, value in item_cost.items():
                print(key.title(), "%.2f"%value, sep=" - £")

        while True:
            add_item = input("\nItem to add (e.g 'treats' or enter to exit):\t").lower()

            if add_item == "":
                print("Going back to main menu")
                break
            elif add_item in item_count.keys():
                add_quantity = input(f"How many {add_item.title()} to add?\t")
                if add_quantity.isnumeric():
                    item_count[add_item] = item_count[add_item] + int(add_quantity)  
                    print(f"{add_quantity} x {add_item.title()} added")
                    break
                else:
                    print("Not a valid quantity")
            else:
                print("Item not recognized")
          
    # Option 2 - remove items decreasing count
    elif menu == "2":
        print("-" * 50)
        print("Items to remove:")
        for key, value in item_cost.items():
            print(key.title(), "%.2f"%value, sep=" - £")
        
        while True:
            remove_item = input("\nItem to remove (e.g 'treats' or enter to exit):\t").lower()

            if remove_item == "":
                print("Going back to main menu")
                break
            elif remove_item in item_count.keys():
                remove_quantity = input(f"How many {remove_item.title()} to remove:\t")
                if remove_quantity.isnumeric():
                    remove_quantity = int(remove_quantity)
                    if remove_quantity <= item_count[remove_item]:
                        item_count[remove_item] = item_count[remove_item] - remove_quantity
                        print(f"{remove_quantity} x {remove_item.title()} removed")
                        break
                    else:
                        print("There aren't that many items in your cart")  
                else:
                    print("Not a valid quantity")
            else:
                print("Item not recognized")

    # Option 3 - view cart and totals
    elif menu == "3":
        
        item_total = {k: item_count[k]*item_cost[k] for k in item_count}
        
        print("-" * 50)
        print("Your current basket is:")
        cost_count_total = item_count.keys() and item_cost.keys() and item_total.keys()
        for k in cost_count_total:
            print(f"{item_count[k]} x {k} at £{"%.2f"%item_cost[k]} - Total £{"%.2f"%item_total[k]}")


        total_cost = sum(item_count[k]*item_cost[k] for k in item_count)
        print("\nCart Total: £", "%.2f"%total_cost)

    # Option 4 - exit cart and checkout
    elif menu == "4":
        print("-" * 50)
        print("Thank you for shopping with us! Have a good day!")
        print("-" * 50)
        break

    else:
        print("\nInvalid option. Please try again!\n")
