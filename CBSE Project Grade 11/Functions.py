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

price_list = []
bill_amount = 0

def manager_todo():
    print("What would you like to do today")
    print('''
    View our List of members(M)
    Check Employee data(E)
    Work as Cashier(c)
    End Program (X)
    ''')

def REmanager_mode():
        manager_todo()
        manager_task = input()
        if manager_task == 'X':
            exit()
        elif manager_task == 'M':
            M()
        elif manager_task == 'E':
            E()
        elif manager_task == 'c':
            cashier_mode(table, price_list, bill_amount)

def M():
    print("The following are the phone numbers of our members: ", list(members.keys()), sep='\n')
    print("The following are the royalty points of our members: ", list(members.values()), sep='\n')
    print("Would you like to add a new member? (y/n)")
    a = input()
    if a == 'y':
        print("Please ask the customer to buy as product and make membership account from the cashier mode")
    elif a == 'n':
        print("Is there anything else you would like to do (Y/N)")
        ab = input()
        if ab == 'Y':
            REmanager_mode()
        elif ab == 'N':
            exit()

def E():
    print("The following are the managers: ", usernames["Managers"])
    print("The following are the Cashiers: ", list(usernames["Cashiers"]))
    print("Is there anything else you would like to do (Y/N)")
    ab = input()
    if ab == 'Y':
        REmanager_mode()
    elif ab == 'N':
        exit()

def c(table, price_list, bill_amount):
    print(table)

    product_found = False
    action = True
    while action:
        serial_number = int(input("Enter the serial number of the product you want to purchase (or 0 to exit): "))
        for row in table._rows:
            if row[0] == serial_number:
                product_found = True
                product = row[1]
                price = row[2]
                bill_amount += price
                break
            elif serial_number == 0:
                action = False
        if product_found:
            price_list.append(price)

    print("Your total bill is: ", bill_amount)
    print("Press r if you want to collect royalty points (E to exit and print bill)")
    royalty_mode = input()
    if royalty_mode == "E":
        print("then your final bill amount is: ", bill_amount)
    elif royalty_mode == "r":
        customer = int(input("Enter customer phone number: "))
        if customer in members.keys():
            points = members[customer]
            final_bill = bill_amount - (points // 150)
            print("Your final bill amount is: ", final_bill)
        else:
            print("You dont have an account with us")
            print("Enter c to create a new user with us (E to exit and print bill)")
            account_Y_N = input()
            if account_Y_N == 'E':
                print("Please pay your bill of ", bill_amount, "Thank you")
            elif account_Y_N == 'c':
                members[int(customer)] = bill_amount//150
                print("welcome to our family we hope to see you here again")
                print("Your final bill for today is: ", bill_amount - 5)

    print("Is there anything else you would like to do (Y/N)")
    ab = input()
    if ab == 'Y':
        REmanager_mode()
    elif ab == 'N':
        exit()

def manager_mode():
    user = input("Enter your name: ")
    ID = input("Enter your password: ")
    if user in usernames["Managers"] and ID in passwords.values():
        manager_todo()
        manager_task = input()
        if manager_task == 'X':
            exit()
        elif manager_task == 'M':
            M()
        elif manager_task == 'E':
            E()
        elif manager_task == 'c':
            c(table, price_list, bill_amount)

def cashier_mode(table, price_list, bill_amount):
    user = input("Enter your name: ")
    ID = input("Enter your password: ")
    if user in usernames["Cashiers"] and ID in passwords.values():
        print(table)
        
        product_found = False
        action = True
        while action:
            serial_number = int(input("Enter the serial number of the product you want to purchase (or 0 to exit): "))
            for row in table._rows:
                if row[0] == serial_number:
                    product_found = True
                    product = row[1]
                    price = row[2]
                    bill_amount += price
                    break
                elif serial_number == 0:
                    action = False
            if product_found:
                price_list.append(price)

        print("Your total bill is: ", bill_amount)
        print("Press r if you want to collect royalty points (E to exit and print bill)")
        royalty_mode = input()
        if royalty_mode == "E":
            print("then your final bill amount is: ", bill_amount)
        elif royalty_mode == "r":
            customer = int(input("Enter customer phone number: "))
            if customer in members.keys():
                points = members[customer]
                final_bill = bill_amount - (points//150)
                print("Your final bill amount is: ", final_bill)
            else:
                print("You dont have an account with us")
                print("Enter c to create a new user with us (E to exit and print bill)")
                account_Y_N = input()
                if account_Y_N == 'E':
                    print("Please pay your bill of ", bill_amount , "Thank you")
                elif account_Y_N == 'c':
                    members[int(customer)] = bill_amount//150
                    print("welcome to our family we hope to see you here again")
                    print("Your final bill for today is: ", bill_amount - 5)
    else:
        print("You are not a Cashier")

