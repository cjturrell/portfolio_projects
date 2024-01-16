"""
Display a menu with options related to shopping cart
Implement While loop to keep the menu running (after user has selected options)
Users able to view, add, remove and get total cost for cart
Provide the user with the option to end the program
"""

print("-" * 50)
print("Welcome to my shop!")
print("-" * 50)

items = []
prices = []

# Continuous loop for input from menu until option '4' to checkout is entered
while True:
    # ask user to select an option form the menu
    option = input("Please select an option below (e.g: 1):\n1: Add item"\
                   "\n2: Remove Item \n3: View Basket\n4: Checkout\n")
    
    # Ask user to enter an item and add the item to shopping list
    if option == '1':
        print("-" * 50)
        item = input("What item would you like to add? ")
        price = float(input("What price is it? £"))

        items.append(item)
        prices.append(format(price, ".2f"))

        print(f"{item} costing £{price} has been added to your basket.")
        print("-" * 50)

    # Ask user to enter an item to remove from basket and remove item and price
    elif option == '2':
        print("-" * 50)
        remove = input("What item would you like to remove? ")

        if remove in items:
            index = items.index(remove)
            items.remove(remove)
            prices.pop(index)

            print(f"{remove} has been removed from your basket.")
            print("-" * 50)

        else:
            print(f"{remove} not found in basket.")
            print("-" * 50)
    
    # Shows users basket and total
    elif option == '3':
        print("-" * 50)
        
        print("Items        Prices")
        for i in range(len(items)):
            print(items[i] , '\t £', prices[i])
        
        sum_total = sum(map(float, prices))
        print("Your total is: £", "%.2f"%(sum_total))
        # print("Your total cost is £", sum(map(float, prices)))  # PRINTS 1DP ONLY
        print("-" * 50)
        
        # basket = {items[i]:prices[i] for i in range(len(prices))}
        # print(basket)
        
        # end = False
        # counter = 0
        # # Check list is not empty
        # if (len(items) > 0):
        #     while(not end):
        #         # Check if it is the last name in the list
        #         if (counter == len(items) -1):
        #             end = True
        #         print("{:25} \t R{:10.2f}".format(items[counter], prices[counter]))
        #         counter += 1

        # View all items in shopping list
        # for i, element in enumerate(items, 1):
        #     print(i, element)

        

    # To exit program
    elif option == '4':
        print("-" * 50)
        print("Thank you for shopping with us. Have a good day!")
        print("-" * 50)
        break


    else:
        print("Invalid input, please try again!")
        print("-" * 50)
        