import streamlit as st
import random
import string

# Streamlit UI
st.title("🔐 Random Password Generator")

# User input for password length
length = st.number_input("Enter the length of the password:", min_value=1, max_value=100, value=12)

# Generate password button
if st.button("Generate Password"):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    st.success(f"Your Generated Password: **{password}**")
