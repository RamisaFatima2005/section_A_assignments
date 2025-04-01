# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

def mad_lib():
    adjective = str(input("Enter an adjective: "))
    noun = str(input("Enter a noun: "))
    verb = str(input("Enter a verb: "))

    print("Story:")
    print(f"One day, a {adjective} {noun} went to the garden. The flowers were blooming beautifully. It slowly {verb}, the breeze was gentle, and everything felt peaceful.")
mad_lib()