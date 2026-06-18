# Greet Customer & Ask Name
print("Hello, Welcome to Han Coffee!")
name = input("What is your name?\n" + "> ")

# Ban Ben & Petricia then ask for evil status
if name == "Ben" or name == "Petricia":
    evil_status = input("Are you evil " + name + "? (yes/no)\n" + "> ")
    if evil_status == "yes":
        good_deeds = int(input("How many good deeds have you done today?\n" + "> "))
        if good_deeds > 4:
            print("Your good deeds saved you. Welcome!!")
        else:
            print("You're not welcome here, Get Out!!")
            exit()
    else:
        print("Oh, you're not evil " + name + ". Welcome!")
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
