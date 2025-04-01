import random

secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

while True:
    try:
        guess = int(input("Enter a guess: "))  
        
        if guess < 0 or guess > 99:
            print("❌ Please enter a number between 0 and 99.")
            continue
        
        if guess > secret_number:
            print("Your guess is too high! ❌")
        elif guess < secret_number:
            print("Your guess is too low! ❌")
        else:
            print(f"🎉 Congrats! The number was: {secret_number}")
            break 
    except ValueError:
        print("❌ Invalid input! Please enter a number between 0 and 99.")
