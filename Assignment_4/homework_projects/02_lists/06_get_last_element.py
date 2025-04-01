def get_first_element(last):
    print("First element: ", last[-1])

list = []

user_input = int(input("How many elements in the list? "))

for i in range(user_input):
    element = input("Enter an element: ")
    list.append(element)

get_first_element(list)