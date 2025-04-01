import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while True:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} number is big (b), small (s) or correct (c)? ").lower()
        
        if feedback == "c":
            print(f"🎉 The computer guessed it right! The number was {guess}.")
            break
        elif feedback == "b":
            high = guess - 1
        elif feedback == "s":
            low = guess + 1
        else:
            print("⚠️ Invalid input! Only enter 'b', 'c', or 's'.")

computer_guess(100)
