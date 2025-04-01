# Write a program to solve this age-related riddle!

# Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

# Your code should store each person's age to a variable and print their names and ages at the end. 

def age():
    anton:int = 21
    beth:int = anton + 6
    chen:int = beth + 20
    drew:int = anton + chen
    ethan:int = chen
    print(f"Anton is {anton}.")
    print(f"Beth is {beth}.")
    print(f"Chen is {chen}.")
    print(f"Drew is {drew}.")
    print(f"Ethan is {ethan}.")

    # We can also use the following method to print the ages:
    # print("Anton is " + str(anton))
    # print("Beth is " + str(beth))
    # print("Chen is " + str(chen))
    # print("Drew is " + str(drew))
    # print("Ethan is " + str(ethan))
age()