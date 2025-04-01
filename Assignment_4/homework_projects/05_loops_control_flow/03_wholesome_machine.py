affirmation = "I am capable of doing anything I put my mind to."

def prompt_affirmation():
    print(f"Please type the following affirmation: {affirmation}")
    while True:
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation. Please try again:")

# Run the program
prompt_affirmation()
