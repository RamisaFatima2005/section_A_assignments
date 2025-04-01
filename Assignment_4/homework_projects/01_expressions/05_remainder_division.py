# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def modulus():
    dividend = float(input("Enter the first number: "))
    divisor = float(input("Enter the second number: "))

    quotient = dividend // divisor
    remainder = dividend % divisor

    print(f"Result of division: {quotient}")
    print(f"Remainder: {remainder}")
modulus()