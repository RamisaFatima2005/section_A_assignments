import streamlit as st
import random

def reset_game():
    st.session_state.number_to_guess = random.randint(50, 100)
    st.session_state.chances = 5
    st.session_state.guess_counter = 0
    st.session_state.game_over = False

def main():
    st.title("🔢 User Guess The Number Game!")
    st.write("You have 5 attempts to guess the number between 50 and 100. Let's start the game!")
    
    if "number_to_guess" not in st.session_state:
        reset_game()
    
    if not st.session_state.game_over:
        guess = st.number_input("Enter your guess:", min_value=50, max_value=100, step=1, format="%d")
        
        if st.button("Submit Guess"):
            st.session_state.guess_counter += 1
            attempts_left = st.session_state.chances - st.session_state.guess_counter
            
            if guess == st.session_state.number_to_guess:
                st.success(f"The number is {st.session_state.number_to_guess}! You found it in {st.session_state.guess_counter} attempt(s)!")
                st.session_state.game_over = True
            elif st.session_state.guess_counter >= st.session_state.chances:
                st.error(f"Oops, the number was {st.session_state.number_to_guess}. Better luck next time!")
                st.session_state.game_over = True
            elif guess < st.session_state.number_to_guess:
                st.warning(f"Your guess is too low, try again! Attempts left: {attempts_left}")
            elif guess > st.session_state.number_to_guess:
                st.warning(f"Your guess is too high, try again! Attempts left: {attempts_left}")
    
    if st.session_state.game_over:
        if st.button("Play Again"):
            reset_game()

if __name__ == "__main__":
    main()