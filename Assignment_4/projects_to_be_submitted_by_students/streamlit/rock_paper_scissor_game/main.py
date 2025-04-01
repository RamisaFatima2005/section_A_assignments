import streamlit as st
import random

def main():
    st.title("Rock, Paper, Scissors Game! 🎮")
    st.write("Choose rock, paper, or scissors and see if you can beat the computer!")
    
    choices = ["rock", "paper", "scissor"]
    
    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
    
    user_choice = st.selectbox("Enter your choice:", choices)
    
    if st.button("Play!"):
        computer_choice = random.choice(choices)
        
        st.write(f"Computer chose: {computer_choice}")
        
        if user_choice == computer_choice:
            st.info("It's a tie! 🤝")
        elif (user_choice == "rock" and computer_choice == "scissor") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissor" and computer_choice == "paper"):
            st.session_state.user_score += 1
            st.success("You win! 🎉")
        else:
            st.session_state.computer_score += 1
            st.error("You lose 😞, computer wins!")
        
        st.write(f"Your Score: {st.session_state.user_score} | Computer Score: {st.session_state.computer_score}")
    
    if st.button("Reset Scores"):
        st.session_state.user_score = 0
        st.session_state.computer_score = 0
        st.write("Scores have been reset!")

if __name__ == "__main__":
    main()
