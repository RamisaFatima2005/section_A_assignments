# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

def fav_animal():
    animal = str(input("What is your favorite animal? "))
    print(f"My favorite animal is also {animal}!")
fav_animal()