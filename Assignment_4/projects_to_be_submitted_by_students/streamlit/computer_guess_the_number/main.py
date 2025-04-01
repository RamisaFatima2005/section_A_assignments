import streamlit as st
import random

st.title("🤖 Computer Guess The Number Game")
st.write("Think of a number between 1 and 100, and let the computer guess it!")

# Initialize game state
if "low" not in st.session_state:
    st.session_state.low = 1
    st.session_state.high = 100
    st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)

st.subheader(f"Is {st.session_state.guess} too big (b), too small (s), or correct (c)?")

# 🛠 Wrap inside a form to avoid automatic reruns
with st.form("feedback_form", clear_on_submit=True):
    feedback = st.text_input("Enter 'b' for big, 's' for small, or 'c' for correct:").strip().lower()
    submit = st.form_submit_button("Submit")

if submit:  # ✅ Run logic only when the form is submitted
    if feedback == "c":
        st.success(f"🎉 The computer guessed it right! The number was {st.session_state.guess}.")
        if st.button("Play Again"):
            st.session_state.low = 1
            st.session_state.high = 100
            st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            st.rerun()

    elif feedback == "b":
        if st.session_state.high > st.session_state.low:
            st.session_state.high = st.session_state.guess - 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            st.rerun()

    elif feedback == "s":
        if st.session_state.high > st.session_state.low:
            st.session_state.low = st.session_state.guess + 1
            if st.session_state.low <= st.session_state.high:
                st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
            st.rerun()

    elif feedback:
        st.error("⚠️ Invalid input! Only enter 'b', 'c', or 's'.")

