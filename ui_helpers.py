"""

Defining functions that help in :

    1) Maintaining a consistent UI design and , 
    2) Avoid app crash if the user enters an invalid response (string response)


"""


def print_heading(title):
    """Prints a consistent heading for every menu section"""

    print("\n" + "=" * 90)
    print(title.center(90))
    print("=" * 90 + "\n")


def get_option(prompt):
    """Accepts a valid integer input from the user"""

    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid option no.")


def post_order_options():
    """Asks the user what to do after adding an item to the cart"""

    while True:
        print("\nWhat would you like to do next?\n")
        print("1. Continue ordering\n2. View Cart")

        choice = get_option("\nEnter option no. (0 to return to the previous menu):  ")

        if choice in [0, 1, 2]:
            return choice  

        else:
            print("Please enter a valid option no.")
            continue
