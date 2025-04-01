# Write a function that takes a list of numbers and returns the sum of those numbers.

def sum_of_numbers():
    num_list = [10,20,40]
    total = 0
    for num in num_list:
     total += num
    print(f"Total sum of {num_list}: {total}")
sum_of_numbers()
