#PLS INSTALL prettytable module for smooth running by typing the following in cmd
#pip install prettytable

import Functions
from prettytable import PrettyTable

# Create a table and set the field names
table = PrettyTable(["Serial Number", "Product", "Price"])
table.align["Product"] = "l"  # Left align the product name

# Add some products to the table
table.add_row([1, "Chocolate Milkshake", 1.75])
table.add_row([2, "Fresh Milk", 7.50])
table.add_row([3, "Orange Juice", 1.75])
table.add_row([4, "Salt 500g", 4.50])
table.add_row([5, "Chocolate IceCream 1.5L", 12.75])
table.add_row([6, "Tide Liquid 2.2L", 22.75])
table.add_row([7, "Dairy Milk", 2.75])

usernames = {"Managers": ("Shanks"), "Cashiers": ("Luffy" , "Shanks")}
passwords = {usernames["Managers"]: "redhaired", usernames["Cashiers"]: "strawhat"}
members = {40489: 300, 30000: 150, 11110: 0, 10320: 450, 36600: 900}
#MAIN

print('''
WELCOME to Humaid Mohammed's CBSE Project 2022-23 for grade 11

If you are a manager please enter 1 to continue
If you are the Cashier then please enter 2 to continue
To Exit the Software enter 0
''')
import Functions as fn

mode = int(input())
price_list=[]
bill_amount = 0

if mode == 0:
    exit()
elif mode == 1:
    fn.manager_mode()
elif mode == 2:
    fn.cashier_mode(table, price_list , bill_amount)
