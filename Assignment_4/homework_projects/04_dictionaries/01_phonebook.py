# In this program we show an example of using dictionaries to keep track of information in a phonebook.

phone_book = {}

while True:
    name = input("Enter name (press Enter to stop): ")
    if name == "":
        break

    while True: 
        number = input(f"Enter phone number of {name}: ")  

        if number.isdigit():  
            number = int(number)  
            break  
        else:
            print("Error: Please enter a phone number first!")

    phone_book[name] = number

    print("\nYour Phone Book:")
    for name, number in phone_book.items():  
        print(f"{name}: {number}")
