max_length = 3
user_list = []
while True:
        value = input("Enter a value (press Enter to stop): ")

        if value == "":
            break

        user_list.append(value)

while len(user_list) > max_length:
        removed_item = user_list.pop()
        print("Removing ", removed_item)

print("Final list: ", user_list)
