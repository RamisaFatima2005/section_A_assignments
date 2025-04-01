import streamlit as st

st.title("📖 Personalized Mad Libs Game")
st.write("Fill in the blanks to create a story about yourself!")

# Get user input
name = st.text_input("Enter your name: ")
age= st.text_input("Enter your age: ")
hobby= st.text_input("Enter your hobby: ")
personality= st.text_input("Describe your personality in one word: ")
fav_place= st.text_input("Enter your favorite where you often like to visit: ")
dream_job= st.text_input("Enter your dream job: ")

story = f"Meet {name}, a {age}-year-old who is {personality} and loves {hobby}. Whenever {name} gets free time, they enjoy visiting {fav_place}. In the future, {name} dreams of becoming a {dream_job}. The journey ahead is full of excitement!"

# Display the story
st.write(story)