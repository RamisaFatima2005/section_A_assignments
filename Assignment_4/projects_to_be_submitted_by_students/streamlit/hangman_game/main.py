import streamlit as st
import random

# List of words
words = ["python", "javascript", "nextjs", "tailwindcss", "frontend", "backend", "html", "css"]

# Session state to store game variables
if 'word' not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6

st.title("🎩 Hangman Game")
st.write("You have 6 attempts to guess the word. Hint: The word is related to programming!!")

# Display the word with guessed letters
display_word = " ".join([letter if letter in st.session_state.guessed_letters else "_" for letter in st.session_state.word])
st.subheader(f"Word: {display_word}")
st.write(f"Attempts left: {st.session_state.attempts}")

# Input for guessing a letter
guess = st.text_input("Guess a letter:", max_chars=1).lower()

if guess:
    if guess in st.session_state.guessed_letters:
        st.warning("You already guessed that letter.")
    elif guess in st.session_state.word:
        st.session_state.guessed_letters.add(guess)
        st.success("Correct guess!")
    else:
        st.session_state.guessed_letters.add(guess)
        st.session_state.attempts -= 1
        st.error("Wrong guess!")

# Check win condition
if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
    st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word}")
    st.session_state.word = random.choice(words)  # Reset game
    st.session_state.guessed_letters.clear()
    st.session_state.attempts = 6

# Check lose condition
if st.session_state.attempts == 0:
    st.error(f"💀 Game Over! The word was: {st.session_state.word}")
    st.session_state.word = random.choice(words)  # Reset game
    st.session_state.guessed_letters.clear()
    st.session_state.attempts = 6
