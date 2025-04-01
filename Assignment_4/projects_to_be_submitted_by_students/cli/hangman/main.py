import random  # Importing the random module to pick a random word

words = ["python", "javascript", "nextjs", "tailwindcss", "frontend", "backend","html", "css"]  # List of words
word = random.choice(words)  # Randomly selecting one word from the list

guessed_letters = set()  # A set to store guessed letters
attempts = 6  # Number of chances the player has

print("\n Welcome to Hangman Game! You have 6 attempts to guess the word. Hint: The word is related to programming!!")

while attempts > 0:  # Loop continues until attempts run out
    display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    print("\nWord:", display_word)  # Showing the word with guessed letters revealed
    print(f"Attempts left: {attempts}")  # Showing remaining attempts

    guess = input("Guess a letter: ").lower()  # Taking user input (lowercase for consistency)

    if guess in guessed_letters:  # If the letter was already guessed
        print("You already guessed that letter.")
    elif guess in word:  # If the guessed letter is in the word
        guessed_letters.add(guess)
        print("Correct guess!")
    else:  # If the guessed letter is not in the word
        guessed_letters.add(guess)
        attempts -= 1  # Decrease attempts
        print("Wrong guess!")

    if all(letter in guessed_letters for letter in word):  # If all letters are guessed
        print(f"\nCongratulations! You guessed the word: {word}")
        break  # Exit the loop

if attempts == 0:  # If no attempts are left
    print(f"Game Over! The word was: {word}")
