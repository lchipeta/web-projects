import time
# variable which holds inventory items
inventory = []

# function to display inventory in the terminal
def get_inventory():
    time.sleep(.8)
    num_of_items = len(inventory)
    print(" ")
    print("          -------------------")
    print("          INVENTORY")
    print("          -------------------")
    print(f"          You have {num_of_items} item(s):")
    print("")
    for i in inventory:
        print(f"              {i}.")
    print("          -------------------")
    print(" ")

# function which uses an item in the inventory
def use_item(item):
    print("Use what? ")
    for i in inventory:
        first_letter = i[0]
        rest_of_letters = i[1:]
        print(f"({first_letter}){rest_of_letters}")
    print("(N)one")

# function to add an item to the inventory
def add_item(item):
    for i in inventory:
        if i == item:
            print(f" You can only carry one {item}!")
            return
    inventory.append(item)
 
 # function to remove an item from the inventory
def remove_item(item):
    if inventory.__contains__(item):
        inventory.remove(item)
  
