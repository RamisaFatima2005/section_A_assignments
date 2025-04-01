# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

import random 

sides = 6
def roll_dice():
    # Simulate rolling two dice, three times.
    die1 = random.randint(1, sides)  # Roll the first die
    die2 = random.randint(1, sides)  # Roll the second die
    total:int = die1 + die2  # Calculate the total of both dice
    
    print(f"The total of the two dice is: {total}")  # Print the total
def main():
    die1 = 10
    print(f"die1 in main starts as {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main starts as {die1}")

main()