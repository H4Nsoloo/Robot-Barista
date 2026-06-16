# Greet Customer & Ask Name
print("Hello, Welcome to Han Coffee!")
name = input("What is your name?\n" + "> ")

# Ban Ben
if name == "Ben":
    evil_status = input("Are you evil Ben? (yes/no)\n" + "> ")
    if evil_status == "yes":
        print("You're not welcome here, Get Out!")
        exit()
    else:
        print("Oh, you're not evil Ben. Welcome!")
else:
    print("\nHello " + name + ", thank you so much for coming in today.\n")

# State Menu & Ask for Order
menu = "Black coffee, Espresso, Latte, Cappucino,Frappuccino"
print(name + ", what would you like to order from the menu below?\n" + menu)
order = input("> ")

# Set the price for coffee
if order == "Black coffee":
    price = 8
elif order == "Espresso":
    price = 6
elif order == "Latte":
    price = 9
elif order == "Cappucino":
    price = 10
elif order == "Frappuccino":
    price = 12
else:
    print("We don't have that on the menu. Please choose from the menu.")
    exit()

# Ask for Quantity & Calculate Total
quantity = input("How many " + order + " would you like?\n" + "> ")
total = price * int(quantity)

# Display Order Summary
print(
    "\nSounds good "
    + name
    + ", we'll have your "
    + quantity
    + " "
    + order
    + " ready for you in a moment."
)

print("\nThank you, your total is: $" + str(total))

print("test")
