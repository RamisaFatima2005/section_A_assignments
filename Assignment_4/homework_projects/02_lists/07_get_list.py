# Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

my_list = []

def get_list():
    while True:
        value = input("Enter a value (press Enter to stop): ")

        if value == "":
            break

        my_list.append(value)

    print("Final list: ", my_list)

get_list()