# Ask the user for a number and print its square (the product of the number times itself).

def square_number():
    # Prompt the user for a number
    number = float(input("Enter a number: "))

    # Calculate the square of the number
    square = number ** 2
    #We can also use the following method to calculate the square:
    # square = number * number

    # Print the square of the number
    print(f"The square of {number} is {square}.")
square_number()