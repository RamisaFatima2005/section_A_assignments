# Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

speed_of_light:int = 299792458

def einstein():
    mass = float(input("Enter mass in kilograms: "))
    e = mass * speed_of_light ** 2

    print(e)
einstein()