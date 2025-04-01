def add_three_copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

my_list = []

data = input("Enter a message to copy: ")
print("List before: ", my_list)

add_three_copies(my_list, data)
print("List after: ", my_list)