# Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

max_height = 50

def tall_enough_to_ride():
    height = float(input("How tall are you?"))

    if height >= max_height:
        print("You are tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")


tall_enough_to_ride()