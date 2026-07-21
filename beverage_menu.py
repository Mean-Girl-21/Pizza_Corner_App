"""
Handles the beverages menu by displaying available beverages,
taking the customer's order, and adding selected items to the cart.

"""

import ui_helpers as ui
import cart
from items_dict import beverage_options


def beverage_menu():
    """Displays beverage options, accepts the customer's choice and quantity, and adds the selected beverage to the cart"""

    while True:

        ui.print_heading("Beverage Menu")

        for key, beverage in beverage_options.items():
            print(
                f"{key}. {beverage["name"]}\n"
                f"\t{beverage["description"]}\n"
                f"\tPrice: Rs. {beverage["price"]}\n"
            )

        choice = ui.get_option("\nEnter option no. (0 to return to the previous menu) :  ")

        if choice == 0:
            return

        elif choice in beverage_options.keys():

            selected = beverage_options[choice]

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

                    elif next_choice == 0:
                        return  # returns the user to the previous menu (rest_menu) if 0 is chosen and result is not paid

                else:
                    print("Quantity must be at least 1.")
                    continue

        else:
            print("Please enter a valid option no.\n")
            continue
