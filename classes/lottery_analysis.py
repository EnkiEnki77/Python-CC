from lottery import create_lot

import string


def lottery_difficulty_analysis():
    """Analyzes how many tickets it takes to win the lottery"""

    # Generates the winning lottery chars
    winning_lot = create_lot()
    # Declares the chars needed to win the lottery 
    print(f"The numbers you need on your ticket to win are: {winning_lot}")

    # Keeps track of how many tickets it took to win
    tickets_to_win = 0

    # The current lottery ticket being compared to the winning numbers
    current_ticket = None
    # Generates lottery tickets until one matches the winning numbers
    while current_ticket != winning_lot:
        current_ticket = create_lot()
        tickets_to_win +=  1
        print(f"The winning lot was {winning_lot}, your ticket was {current_ticket}. {tickets_to_win} tickets have been used")

        if tickets_to_win == 100_000:
            print(f"100,000 tickets have been bought, and still no winner!")
            return

    # returns number of tickets it took to win
    print(f"\nIt took {tickets_to_win} tickets to win the lottery.")


lottery_difficulty_analysis()