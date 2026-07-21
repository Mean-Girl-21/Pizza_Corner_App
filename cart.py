"""
Cart management logic : Segmenting each part of the cart operation as a separate function 
"""

import ui_helpers as ui
import cart_operations as cart_op
import feedback as fd
from items_dict import cart

def add_to_cart(name, price, quantity):
    """Adds the customer's order (dictionary) to the cart (list)"""

    cart.append({"name": name, "unit_price": price, "quantity": quantity})


def view_cart(): 
    """Allows the user to view the ordered items and total bill in cart"""

    while True: 

        if cart:
            ui.print_heading("Your Cart")

            for index, order in enumerate(cart, start = 1):
                item_total = (order["unit_price"] * order["quantity"])

                print(
                    f"{index}. {order['name']}\n"
                    f"   Unit Price : Rs. {order['unit_price']}\n"
                    f"   Quantity   : {order['quantity']}\n"
                    f"   Item Total : Rs. {item_total}\n"
                )

            bill_amount = cart_op.calculate_total_amount()

            print("-" * 90)
            print(f"Total payable amount : Rs. {bill_amount}")
            print("-" * 90)

            print("\nWhat would you like to do next ?\n")
            print("1. Add another item\n2. Edit the quantity\n3. Remove an item\n4. Proceed to payment") 

            final_step = ui.get_option("\nEnter option no. (0 to return to the previous menu) :  ")

            if final_step == 1:
                return

            elif final_step == 2:
                cart_op.edit_quantity()
                continue

            elif final_step == 3:
                cart_op.remove_item()
                continue

            elif final_step == 4:
                cart_op.proceed_to_payment()
                fd.collect_feedback()
                cart.clear()
                return "paid"

            elif final_step == 0:
                return

            else:
                print("Please enter a valid option no.")
                continue

        else:
            print("\nYour cart is currently empty!\nTaking you back to the main menu where you can start ordering...\n")
            return
