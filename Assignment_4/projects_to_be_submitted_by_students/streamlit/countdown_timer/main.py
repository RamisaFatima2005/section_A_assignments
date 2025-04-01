import streamlit as st
import time


def countdown_timer(seconds):
    while seconds > 0:
        st.write(f"⏳ {seconds} seconds left")
        time.sleep(1)
        seconds -= 1
        st.empty()
    st.write("⌛ Time's up!")
st.title("Countdown Timer ⏲️")

seconds = st.number_input("Enter the number of seconds", min_value=1, step = 1)

if st.button("Start Countdown"):
    countdown_timer(int(seconds))
        