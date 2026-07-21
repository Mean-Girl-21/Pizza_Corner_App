"""
Handles customer feedback after payment
"""

import ui_helpers as ui

def collect_feedback():
    """Asks the customer to rate their experience"""

    print("\nThank you for choosing us !\n\nHow was your experience with Pizza Corner ?\n")
    print("1. Poor\n2. Average\n3. Good\n4. Very Good\n5. Excellent\n")

    while True:
        feedback = ui.get_option("\nPlease rate us from 1 to 5 (or type 0 to skip):  ")

        if 1 <= feedback <= 5:
            print("\nThank you for your feedback! We appreciate your support.")

        elif feedback == 0:
            print("\nNo worries! Thank you for ordering with us.")

        else:
            print("\nInvalid rating :(")
            continue 

        print("\nRedirecting you to the main menu...")
        return
