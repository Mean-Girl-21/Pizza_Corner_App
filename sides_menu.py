"""
Handles the sides menu by displaying available sides,
taking the customer's order, and adding selected items to the cart.

"""

import ui_helpers as ui
import cart
from items_dict import sides_options


def sides_menu():
    """Displays sides options, accepts the customer's choice and quantity, and adds the selected side to the cart"""

    while True:

        ui.print_heading("Sides Menu")

        for key, side in sides_options.items():
            print(
                f"{key}. {side["name"]}\n"
                f"\t{side["description"]}\n"
                f"\tPrice: Rs. {side["price"]}\n"
            )

        choice = ui.get_option("\nEnter option no. (0 to return to the previous menu) :  ")

        if choice == 0:
            return

        elif choice in sides_options.keys():

            selected = sides_options[choice]

            while True:
                quantity = ui.get_option("\nEnter quantity :  ")

                if quantity > 0:
                    cart.add_to_cart(selected["name"], selected["price"], quantity)
                    print(f"\nAdded {quantity} x {selected["name"]} to the cart!\n")

                    next_choice = ui.post_order_options()

                    if next_choice == 1:
                        break

                    elif next_choice == 2:
                        result = cart.view_cart()

                        if result == "paid":
                            return "paid"
                        
                        return # returns the user to the previous menu (rest_menu) if 0 is chosen and result is not paid

                    elif next_choice == 0:
                        return

                else:
                    print("Quantity must be at least 1")
                    continue

        else:
            print("Please enter a valid option no.\n")
            continue
