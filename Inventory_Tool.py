#                                                                                                                                                                       Name of Program: Inventory Tool
#                                                                                                                                                                               Creator: Jesse Tadena
# - Purpose: Allows the User To Create List of Items They Would Want to Keep Track of                                                                                                                            



#Creates a Menu
def menu():
    print("1 - Add Item To Inventory")
    print("2 - Remove Item from Inventory")
    print("3 - Veiw Inventory")
    print("4 - Quit")
    try:
        user_input = int(input("\nWhat Would You Like To Do Today?\n"))
    except ValueError:
        user_input = exception_han_int()

    return user_input

# Function that Handles Integer Related Errors
def exception_han_int():
    x = False
    while x == False:
        try:
            int_value = int(input("Invalid Response. Please Try Again\n"))
        except ValueError:
            print("Please Try Again")
        else:
            x = True
    return int_value

#Function that Handles String Realed Errors
def exception_han_str(str_value):
    x = False
    while x == False:
        try:
            str_value = int(str_value)
            number = str_value + 0
            str_value = str(input("Invalid Please Try Again. Make sure it is the Name of a item\n"))
        except ValueError:
            x = True
    return str_value

# Function that takes in a list, checks to see if it contains anything
# If it has values in it, then it prints it out 
def check_stock_list(newlist):
    if len(newlist) == 0:
        print("There are no items here")
    elif len(newlist) > 0:
        for items in newlist:
            print("-", items)
   
# Function that "Cleans" Strings
def clean_data(data):
    new_string = data.strip()
    new_string= new_string.lower()
    new_string = new_string.title()
    return new_string

# Adds items to Inventory dictionary
def increase_inventory(inventory):
    quantity_added = 0
    item_name= exception_han_str(str(input("What are you adding today?\n")))
    item_name = clean_data(item_name)
    
    if item_name not in inventory:
        print("Hmm.....\nIt looks like you don't have", item_name, "yet. \n")
        try:
            quantity_added = int(input("How many of these are you adding? Please type in an integer\n"))
        except ValueError:
            quantity_added = exception_han_int()
        inventory[item_name] = item_name
        inventory[item_name] = quantity_added
        
    elif item_name in inventory:
        try:
            quantity_added = int(input("How many of these are you adding? Please type in an integer\n"))
        except ValueError:
            quantity_added = exception_han_int(quantity_added)
        inventory[item_name] += quantity_added
        
# Subtracts "Item" values from dictionary  
def decrease_inventory(stock_inventory):
    item_name = exception_han_str(str(input("Which item are you Removing?\n")))
    item_name = clean_data(item_name)
    try:
        quantity_remove = int(input("How many items are you Removing?\n"))
    except ValueError:
        quantity_remove = exception_han_int(quantity_remove)
            
    # Checks to see if "Item" is in inventory 
    if item_name not in stock_inventory:
        print("You do not have", item_name, "in stock.")
        
    elif item_name in stock_inventory:
        stock_inventory[item_name] -= quantity_remove
        # Checks to see if the amount of items removed exceed
        # the amount in the inventory
        if stock_inventory[item_name] < 0 or stock_inventory[item_name] == 0:
            stock_inventory[item_name]+= quantity_remove
            print("You do not have enough stock to remove", quantity_remove,"from",item_name," since you only had", stock_inventory[item_name], "to begin with\n")
            print("You can only remove", stock_inventory[item_name], "of them.\n")
            print("Woud you like to proceed in Removing Everything from your inventory?")
            print("Press 1 to Remove Everything from Your Inventory. Press 2 to Exit to Main Menu\n")
            quantity_remove = int(input())
            while quantity_remove != 1 or quantity_remove !=2:
                if quantity_remove == 1:
                    del stock_inventory[item_name]
                    break
                elif quantity_remove == 2:
                    print("Exiting to Main Menu")
                    break
                else:
                    try:
                        quantity_remove = int(input("Invalid Response. Please Try again"))
                    except ValueError:
                        quantity_remove = exception_han_int(quantity_remove)
        
    
# Views Inventory 
def view_inventory(inventory):
    low_stock = []
    high_stock = []
    print("Items in Stock:")
    for item in inventory:
        print(item, ":\t", inventory[item])
    
# Calls and Opens up Menu Options
def main():
    choice = menu()
    inventory_list = {}

    while choice != 4:
        if choice == 1:
            increase_inventory(inventory_list)
        elif choice ==2:
            decrease_inventory(inventory_list)
        elif choice ==3:
            view_inventory(inventory_list)
        elif choice ==4:
            print("")
        else: 
            print(" Sorry, That Was Not a Valid Option,")
        choice = menu()
main()

    
