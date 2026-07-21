"""
Allows users to edit quantity, remove items and pay for their order
"""

import ui_helpers as ui
from items_dict import cart

def edit_quantity():
    """Allows the user to update the quantity of an item in the cart"""

    while True: 
        item_number = ui.get_option("\nChoose the item no. whose quantity you want to edit (0 to cancel) :  ")

        if item_number == 0:
            return

        elif 1 <= item_number <= len(cart): 

            while True:

                new_quantity = ui.get_option("Enter the updated quantity:  ")

                if new_quantity > 0:
                    cart[item_number - 1]["quantity"] = new_quantity
                    print("\nQuantity updated successfully!\n")
                    return
                
                else:
                    print("\nQuantity must be at least 1\n")
                    continue

        else:
            print("\nPlease enter a valid item no.\n")
            continue


def remove_item():
    """Allows the user to remove an item from the cart"""

    while True:
        delete_item = ui.get_option("\nEnter the item no. you want to remove from the cart (0 to cancel) :  ")

        if delete_item == 0:
            return 

        elif 1 <= delete_item <= len(cart):

            removed_item = cart.pop(delete_item - 1)
            print(f"\nRemoved {removed_item["name"]} from the cart successfully!")
            return
            

        else:
            print("\nPlease enter a valid item no.")
            continue

def calculate_total_amount():
    """Calculates and returns the total bill amount"""

    total = 0
    for order in cart:
        total += order["unit_price"] * order["quantity"]

    return total


def proceed_to_payment():
    """Handles final payment"""

    total_bill = calculate_total_amount()

    print(f"\nPayment successful! We have received Rs. {total_bill}")
