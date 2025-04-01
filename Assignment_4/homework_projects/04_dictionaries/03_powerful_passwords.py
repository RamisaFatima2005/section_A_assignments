from hashlib import sha256

def powerful_password(password):
    return sha256(password.encode()).hexdigest()

stored_logins = {
    "user@example.com": powerful_password("mypassword123"),
    "admin@website.com": powerful_password("securePass456")
}

def login (email, password_to_check):
    hashed_input = powerful_password(password_to_check)
    return stored_logins.get(email) == hashed_input

email = input("Enter your email: ")
password = input("Enter your password: ")

if login(email, password):
    print("✅ Login Successful! Welcome!")
else:
    print("❌ Incorrect email or password. Please try again!")