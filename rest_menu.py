"""
Handles the restaurant menu by displaying food categories
such as pizzas, sides, and beverages.

"""

import ui_helpers as ui
import pizza_menu as pizza
import sides_menu as sides
import beverage_menu as beverage

def restaurant_menu():
    """Displays the menu of Pizza Corner"""

    while True:
        ui.print_heading("Pizza Corner Menu")
        print("1. Pizza\n2. Snacks\n3. Drinks\n")

        print("What would you like to order ?")

        choice = ui.get_option("\nEnter option no. (0 to return to the main menu) :  ")

        if choice == 1:
            result = pizza.pizza_menu()

            if result == "paid":
                return

        elif choice == 2:
            result = sides.sides_menu()

            if result == "paid":
                return

        elif choice == 3:
            result = beverage.beverage_menu()

            if result == "paid":
                return

        elif choice == 0:
            return

        else:
            print("Please enter a valid option no.")
            continue 
