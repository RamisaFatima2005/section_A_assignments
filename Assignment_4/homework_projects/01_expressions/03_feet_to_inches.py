# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def convert():
    feet = float(input("Enter number of feet: "))
    inches = feet * 12

    print(inches)
convert()