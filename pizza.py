""" 
Creating a pizza parlour app's e-menu where one can browse and order items :

- Categories in the app :  Menu , View Cart , Review and Quit
- One can add, delete or update an item from the cart
- One can also view the cart and the total bill
- Can additional instructions to the parlour : eg., adding new toppings
- The parlour can give discounts at the total bill 
- The review section can be revisited after the payment of the meal 
- Further , the size selection , price and additional toppings option will be made available to the customer
 (eg Medium and large size pizzas' prices can be twice and thrice the price of a small pizza)

Main menu display screen:

- menu > categories and items 
- view your cart > CRUD operation ; merging with total bill (receipt)
- review section > confirm whether to give feedback 
- quit

"""
active = True

def view_cart():
    pass

def review():
    pass

def pizza_menu():
    pass

def snacks_menu():
    pass

def drinks_menu():
    pass

def rest_menu():
    print("1. Pizza\n2. Snacks\n3. Drinks\n4. Main Menu")
    choice = input("What would you like to eat ? ")

    if choice == '1':
        pizza()

    elif choice == '2' :
        snacks()

    elif choice == '3' :
        drinks()

    elif choice == '4' :
        app_launch_menu()

    else:
        print("Please enter a valid option no.")


def app_launch_menu():

    while True : 

        app_options = ['Menu : Order yummies', 
                   'View Cart', 
                   'Review : Let us know how you feel about us',
                   'Quit : Bye Bye']
        
        for index , app_option in enumerate(app_options):
            print(f"{index + 1}. {app_option}")
        
        choice = input("Enter option no. : ")
        if choice == '1' :
            rest_menu()

        elif choice == '2' :
            view_cart()
        
        elif choice == '3' :
            review()

        elif choice == '4' :
            break

        else :
            print("Please enter a valid option no.")

app_launch_menu()
