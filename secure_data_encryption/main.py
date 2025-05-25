import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Encryption setup
if "fernet_key" not in st.session_state:
    st.session_state.fernet_key = Fernet.generate_key()

cipher_suite = Fernet(st.session_state.fernet_key)


# In-memory data storage
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "auth_attempts" not in st.session_state:
    st.session_state.auth_attempts = {}

if "authorized" not in st.session_state:
    st.session_state.authorized = True  # Default True until 3 failures

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_text(plain_text):
    return cipher_suite.encrypt(plain_text.encode()).decode()

def decrypt_text(cipher_text):
    return cipher_suite.decrypt(cipher_text.encode()).decode()

def store_user_data(user_id, text, passkey):
    hashed_key = hash_passkey(passkey)
    encrypted_text = encrypt_text(text)
    st.session_state.stored_data[user_id] = {
        "encrypted_text": encrypted_text,
        "passkey": hashed_key
    }

def retrieve_user_data(user_id, passkey):
    if user_id not in st.session_state.stored_data:
        return "User not found", False

    hashed_input = hash_passkey(passkey)
    saved_entry = st.session_state.stored_data[user_id]

    if saved_entry["passkey"] == hashed_input:
        return decrypt_text(saved_entry["encrypted_text"]), True
    return "Incorrect passkey", False

def record_failed_attempt(user_id):
    st.session_state.auth_attempts[user_id] = st.session_state.auth_attempts.get(user_id, 0) + 1
    if st.session_state.auth_attempts[user_id] >= 3:
        st.session_state.authorized = False

def reset_attempts(user_id):
    st.session_state.auth_attempts[user_id] = 0
    st.session_state.authorized = True

# Page Navigation
page = st.sidebar.selectbox("Select Page", ["Home", "Insert Data", "Retrieve Data", "Login"])

if page == "Home":
    st.title("🔐 Secure Data Encryption System")
    st.write("Welcome to your private encrypted vault!")
    st.write("Use the sidebar to store or retrieve your secure data.")

elif page == "Insert Data":
    st.title("📝 Store New Data")
    user_id = st.text_input("Enter a unique User ID")
    text = st.text_area("Enter the text to encrypt")
    passkey = st.text_input("Set your passkey", type="password")

    if st.button("Store Data"):
        if user_id and text and passkey:
            store_user_data(user_id, text, passkey)
            reset_attempts(user_id)
            st.success("Data securely stored!")
        else:
            st.error("Please fill in all fields.")

elif page == "Retrieve Data":
    if not st.session_state.authorized:
        st.warning("Too many failed attempts. Please reauthorize in the Login page.")
    else:
        st.title("🔓 Retrieve Data")
        user_id = st.text_input("Enter your User ID")
        passkey = st.text_input("Enter your passkey", type="password")

        if st.button("Decrypt Data"):
            result, success = retrieve_user_data(user_id, passkey)
            if success:
                reset_attempts(user_id)
                st.success("Decrypted Text:")
                st.code(result)
            else:
                record_failed_attempt(user_id)
                attempts = st.session_state.auth_attempts.get(user_id, 0)
                st.error(f"{result} | Attempt {attempts}/3")

elif page == "Login":
    st.title("🔐 Reauthorization Required")
    user_id = st.text_input("Enter User ID to reset attempts")
    admin_key = st.text_input("Enter admin passcode: (admin123)", type="password")

    if st.button("Reauthorize"):
        if user_id == "":
            st.error("User ID is required.")
        elif admin_key == "admin123":  
            if user_id in st.session_state.auth_attempts:
                reset_attempts(user_id)
                st.success(f"Access for '{user_id}' restored. You can now try again.")
            else:
                st.warning("No failed attempts found for this User ID.")
        else:
            st.error("Incorrect admin passcode.")
