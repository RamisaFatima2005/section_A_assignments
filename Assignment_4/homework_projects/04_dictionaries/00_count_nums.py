num_list = []

while True:
    num = input("Enter a number (press Enter to stop): ")

    if num == "":
        break

    num_list.append(int(num))

count_dict = {}

for num in num_list:
    if num in count_dict:
        count_dict[num] +=1
    else:
        count_dict[num] = 1

for number, count in count_dict.items():
    print(f"{number} appears {count} times.")