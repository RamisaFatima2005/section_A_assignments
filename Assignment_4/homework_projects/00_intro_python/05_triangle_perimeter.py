# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

def triangle_perimeter():
    # Prompt the user to enter the lengths of each side of a triangle
    side_a = float(input("Enter the length of side A: "))
    side_b = float(input("Enter the length of side B: "))
    side_c = float(input("Enter the length of side C: "))

    # Calculate the perimeter
    perimeter = side_a + side_b + side_c

    # Print the perimeter
    print(f"The perimeter of the triangle is: {perimeter}")
triangle_perimeter()