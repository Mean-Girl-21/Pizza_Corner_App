"""
Main application file for the Pizza Corner's e-menu

This module launches the app and provides the main menu where
customers can browse the restaurant menu, view their cart,
and exit the application.

"""

import ui_helpers as ui
import rest_menu as rm
import pizza_menu as pizza
import cart 


app_options = ["Menu : Order yummies", 
               "View Cart", 
               "Exit"]

def app_launch_menu():
    """Displays the main menu and allows the user to navigate to 
    the restaurant menu, view the cart, or exit the app"""

    while True:

        ui.print_heading("Welcome to the Pizza Corner !")
        for index, app_option in enumerate(app_options, start = 1):
            print(f"{index}. {app_option}")

        choice = ui.get_option("\nEnter option no. :  ")

        if choice == 1:
            rm.restaurant_menu()

        elif choice == 2:
            cart.view_cart()

        elif choice == 3:
            print("\nBye, See you later !")
            break

        else:
            print("Please enter a valid option no.\n")
            continue

# Launching the app
app_launch_menu()
