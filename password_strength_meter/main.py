import streamlit as st
import re

# Function to check password strength
def check_password_strength(password):
    strength = 0
    remarks = ""

    # Conditions for strength calculation
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"\d", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Categorizing strength level
    if strength == 5:
        remarks = "Strong 💪"
        color = "green"
    elif strength >= 3:
        remarks = "Medium ⚠️"
        color = "orange"
    else:
        remarks = "Weak ❌"
        color = "red"

    return remarks, color

# Streamlit UI
st.title("🔐 Password Strength Meter")

# Password Input
password = st.text_input("Enter your password:", type="password")

# Checking password strength
if password:
    strength_remarks, color = check_password_strength(password)
    st.markdown(f"### **Password Strength: <span style='color:{color};'>{strength_remarks}</span>**", unsafe_allow_html=True)
