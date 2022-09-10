#Making our warung

# Price List
# Nasih = 1000
# Ayam = 3000
# Bakso = 3500
# Lumpia = 5000

# Define the menu (later with For Loops and dir() but not now
menu = "Nasih, Ayam, Bakso, Lumpia"

# Ask customer there name
cust_name = input("Selamat Datang! What is your name? \n")

# Greet and show the menu
print("Nice to meet you " + cust_name + ", Our menu today is \n" + menu)

# Ask what they want to order
cust_order = input("What would you like to order? \n")

#repeat the order back to the customer and ask how many
cust_order_qty = input("Ok " + cust_name + ", How many " + cust_order + " would you like?\n")

#calualte the total of the order the worng way
#order_total = int(cust_order_qty) * cust_order

# 2 calculate the order the long hard way

if cust_order == "Nasih":
    price = 1000
if cust_order == "Ayam":
        price = 3000
if cust_order == "Bakso":
        price = 3500
if cust_order == "Lumpia":
        price = 5000
# if cust_order == "":
#     print("You didnt type what you want!")
#     exit()

# Calulate the total amount due
order_total = int(cust_order_qty) * price

# Repeat the order and give the total amount due
print("Your order today is " + cust_order_qty + " x " + cust_order + " and the total for that will be \n Rp" + str(order_total))