import streamlit as st
import sqlite3

# Database setup
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL
)
""")
conn.commit()

# Function to add book
def add_book(title, author, year):
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()

# Function to get all books
def get_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

# Function to delete book
def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

# Streamlit UI
st.title("📚 Library Manager")

# Tabs for navigation
tab1, tab2, tab3 = st.tabs(["📖 View Books", "➕ Add Book", "❌ Delete Book"])

# View Books Tab
with tab1:
    st.subheader("📖 Book List")
    books = get_books()
    if books:
        for book in books:
            st.write(f"📘 **{book[1]}** by {book[2]} ({book[3]}) [ID: {book[0]}]")
    else:
        st.write("No books available.")

# Add Book Tab
with tab2:
    st.subheader("➕ Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1800, max_value=2100, step=1)

    if st.button("Add Book"):
        if title and author and year:
            add_book(title, author, year)
            st.success(f"Book '{title}' added successfully!")

# Delete Book Tab
with tab3:
    st.subheader("❌ Delete a Book")
    book_id = st.number_input("Enter Book ID to Delete", min_value=1, step=1)

    if st.button("Delete Book"):
        delete_book(book_id)
        st.success(f"Book with ID {book_id} deleted!")
        
conn.close()
