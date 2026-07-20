"""
Creating a simple pizza parlour app's e-menu where one can browse and order items :

- Categories in the app :  Menu , View Cart and Quit
- One can add, delete or update an item from the cart
- One can also view the cart and the total bill
- The review section will be available to the customer once the order is complete

Main menu display screen:

- menu > categories (Pizzas, Sides and Drinks)
- view your cart > CRUD operation ; merging with total bill (receipt)
- quit

"""

active = True
cart = []  # Currently, the cart is empty

app_options = ["Menu : Order yummies", "View Cart", "Exit"]

pizza_options = {
    1: {
        "name": "Classic Margherita",
        "description": "A classic pizza topped with mozzarella cheese, tomato sauce, and fresh basil.",
        "price": 150,
    },
    2: {
        "name": "Cheese & Corn Pizza",
        "description": "A cheesy delight loaded with sweet corn kernels and melted mozzarella.",
        "price": 170,
    },
    3: {
        "name": "Farmhouse Pizza",
        "description": "A hearty pizza topped with onions, capsicum, tomatoes, mushrooms, and mozzarella.",
        "price": 200,
    },
    4: {
        "name": "Paneer & Capsicum Pizza with Special Hot Sauce",
        "description": "Spicy paneer cubes and crunchy capsicum topped with a flavorful hot sauce.",
        "price": 260,
    },
    5: {
        "name": "Mexican Green Wave Pizza",
        "description": "A zesty mix of capsicum, onions, tomatoes, jalapeños, and Mexican herbs.",
        "price": 300,
    },
}


def app_launch_menu():
    """The user can choose to order items once the app is launched"""

    while True:
        # While loop used here, because we want this to keep running unless the person exits.

        print("\nWelcome to the Pizza Corner !\n")
        for index, app_option in enumerate(app_options):
            print(f"{index + 1}. {app_option}")

        choice = int(input("\nEnter option no. :  "))

        if choice == 1:
            restaurant_menu()

        elif choice == 2:
            view_cart()

        elif choice == 3:
            print("\nBye, See you later !")
            break

        else:
            print("Please enter a valid option no.")
            continue


def restaurant_menu():
    """Displays the menu of Pizza Corner"""

    print("\nHere is our menu :\n")
    print("1. Pizza\n2. Snacks\n3. Drinks\n")

    choice = int(
        input(
            "What would you like to eat ?\n(Type 0 to go back to the main menu)\nEnter option no. :  "
        )
    )

    if choice == 1:
        pizza_menu()

    elif choice == 2:
        sides_menu()

    elif choice == 3:
        drinks_menu()

    elif choice == 0:
        return

    else:
        print("Please enter a valid option no.")


def pizza_menu():
    """Display the pizza options, their prices , and allows customers to order"""

    while True:

        print(f"\nHere are our pizza options along with their prices (in Rs) :\n")

        for key, pizza_info in pizza_options.items():
            print(
                f"{key}. {pizza_info["name"]}\n\t{pizza_info["description"]}\n\tPrice : {pizza_info["price"]}"
            )

        pizza_choice = int(
            input(
                "\nWhich pizza would you like to order ?\n(Type 0 to go back to the main menu)\nEnter option no. :  "
            )
        )

        if 1 <= pizza_choice <= 5:

            selected_pizza = pizza_options[
                pizza_choice
            ]  # storing the index no. of the pizza for referencing
            pizza_price = selected_pizza[
                "price"
            ]  # storing the price of the pizza for calculations

            while True:

                # Ensures that if the customer enters an invalid number, he/she is redirected to entering quantity again

                qty_pizza = int(
                    input(
                        "\nPlease enter the quantity of pizza.\n(Type 0 to go back to the main menu)\nEnter quantity :  "
                    )
                )

                if qty_pizza > 0:

                    # once an order is complete, we need to store it inside a dictionary and later append it to the cart

                    customer_order = {
                        "name": selected_pizza["name"],
                        "unit_price": pizza_price,
                        "quantity": qty_pizza,
                    }

                    cart.append(customer_order)

                    print(
                        f"\nAdded {qty_pizza} x {selected_pizza["name"]} to the cart!"
                    )

                    while True:

                        print("\nSelect an option no. :")

                        e_choice = int(
                            input(
                                "\n1 : Continue to order more pizzas\n0 : Return to main menu\nEnter option no. :  "
                            )
                        )

                        if e_choice == 1:
                            break

                        elif e_choice == 0:
                            return

                        else:
                            print("Please enter a valid option no.")
                            continue

                    break

                elif qty_pizza == 0:

                    print("Going back to the main menu !\n")
                    return

                else:

                    print("Please enter a valid option no.")
                    continue

        elif pizza_choice == 0:
            return

        else:
            print("Please enter a valid option no.")
            continue


def view_cart():
    """Displays the ordered items and the amount to be paid by the customer"""

    while True:

        if cart:

            print("\nHere are your order details :\n")
            for index, customer_order in enumerate(cart):
                print(f"{index + 1}. {customer_order["name"]}")
                print(f"   Unit Price : {customer_order["unit_price"]}")
                print(f"   Quantity : {customer_order["quantity"]}")
                print(
                    f"   Total Amount (in Rs) : {customer_order["unit_price"] * customer_order["quantity"]}\n"
                )

            total_bill = 0

            for customer_order in cart:
                total_bill += customer_order["unit_price"] * customer_order["quantity"]

            # Showing the total bill so that the user can decide whether to proceed with it.

            print(f"Total Bill : Rs. {total_bill}\n")

            final_step = int(
                input(
                    "\nWhat would you like to do next ?\n1. Add another item\n2. Edit the quantity\n3. Remove an item\n4. Proceed to payment\n\n(Type 0 to go back to the main menu)\n\nEnter option no. :  "
                )
            )

            if final_step == 1:
                print("\nWe'll take you to the main menu where you can add more items")
                return

            elif final_step == 2:

                item_number = int(
                    input(
                        "\nChoose the item no. whose quantity you want to edit (0 to cancel) :  "
                    )
                )

                if (
                    1 <= item_number <= len(cart)
                ):  # Ensures that the user does not enter an invalid index number

                    edit_quantity = int(input("Updated quantity :  "))

                    if edit_quantity <= 0:
                        print("The updated quantity must be at least 1.\n")

                    else:
                        cart[item_number - 1]["quantity"] = edit_quantity
                        print("\nUpdated the quantity successfully !")

                elif item_number == 0:
                    continue

                else:
                    print("Please enter a valid number")

                continue
                # After choosing a valid / invalid quantity, the user can view the cart again to decide next steps

            elif final_step == 3:

                delete_item = int(
                    input(
                        "\nType the option no. of the item that you want to delete from the cart (0 to cancel):  "
                    )
                )

                if 1 <= delete_item <= len(cart):

                    popped_item = cart.pop(delete_item - 1)

                    if cart:

                        print(
                            f"\nRemoved {popped_item["name"]} from the cart successfully !"
                        )
                        print("\nYou can view your current items in the cart.")

                    else:
                        print(
                            "Your cart is empty !\nTaking you back to the main menu.\n"
                        )
                        return

                elif delete_item == 0:
                    continue

                else:
                    print("\nPlease enter a valid option no.\n")

                continue

            elif final_step == 4:

                print(f"\nPayment successful ! We have received Rs. {total_bill} :)\n")
                print(
                    "Thank you for choosing Pizza Corner! We hope you enjoyed your meal.\n"
                )

                print(
                    "How was your experience with Pizza Corner ?\n1. Poor\n2. Average\n3. Good\n4. Very Good\n5. Excellent\n"
                )

                while True:

                    feedback = int(
                        input("Please rate us from 1 to 5 (or type 0 to skip):  ")
                    )

                    if 1 <= feedback <= 5:
                        print(
                            "\nThank you for your feedback! We appreciate your support."
                        )

                    elif feedback == 0:
                        print("\nNo worries! Thank you for ordering with us.")

                    else:
                        print("\nPlease enter a valid rating.\n")
                        continue

                    print("\nHave a wonderful day! See you later :)")

                    cart.clear()  # Ensures that the cart of the consumer is empty after the payment is done
                    exit()

            elif final_step == 0:
                return

            else:
                print("Please enter a valid option no.")
                continue

        else:
            print(
                "\nSorry, your cart is currently empty !\nWe'll take you to the main menu where you can start ordering yummy dishes :)\n "
            )
            return


def sides_menu():
    pass


def drinks_menu():
    pass


# Starting the app
app_launch_menu()
