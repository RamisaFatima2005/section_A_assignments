# Write a program that doubles each element in a list of numbers.

def double():
    num_list = [1,2,3,4]
    doubled_list = []
    for i in num_list:
        doubled_list.append(i * 2)
    print(doubled_list)
double()