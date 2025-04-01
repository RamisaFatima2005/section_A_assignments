def get_first_element(lst):
    print("First element: ", lst[0])

list = []

user_input = int(input("How many elements in the list? "))

for i in range(user_input):
    element = input("Enter an element: ")
    list.append(element)

get_first_element(list)