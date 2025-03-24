# print("Wellcome to the Personal Library App")

# def menu():
#     print("1. Add a book")
#     print("2. Remove a book")
#     print("3. Search for a book")
#     print("4. Display all books")
#     print("5. Display statistics")
#     print("6.Exit")

# all_books: list = []

# def add_book():
#     title = input("Enter Your Book Title: ")
#     author = input(f"Enter Your Book Author: ")
#     publication_year = input("Enter Your Book Publication Year: ")
#     genre = input("Enter Your Book Genre: ")
#     read_book = input("Have you read this book? (yes/no): ")
#     book = {
#     "title" : title,
#     "author" : author,
#     "publication-year": publication_year,
#     "genre" : genre,
#     "read" : read_book
#     }

#     all_books.append(book)
#     print("\nBook added successfully!\n")
#     print("\nYour Book List:")
#     for book in all_books:
#         print(book)

# def remove_book():
#     book_name = input("Enter the name of the book you want to remove: ")
#     for book in all_books:
#         if book["title"].lower() == book_name.lower():
#             all_books.remove(book)
#             print(f"\n'{book_name}' has been removed from your library.\n")
#             return
#     print(f"\n'{book_name}' is not in your library.\n")

# def search_book():
#     book_name = input("Enter the name of the book you want to search: ")
#     for book in all_books:
#         if book["title"].lower() == book_name.lower() or book["author"].lower() == book_name.lower():
#             print("Book Found")
#             print(f"Title : {book['title']}")
#             print(f"Author : {book['author']}")
#             print(f"Publication Year : {book['publication-year']}")
#             print(f"Genre : {book['genre']}")
#             print(f"Read : {book['read']}")
#             return
#     print(f"\n'{book_name}' is not found.\n")

# def display_books():
#     for book in all_books:
#         print(f"Title : {book['title']}")
#         print(f"Author : {book['author']}")
#         print(f"Publication Year : {book['publication-year']}")
#         print(f"Genre : {book['genre']}")
#         print(f"Read : {book['read']}")

# def display_statistics():
#     if not all_books:
#         print("\nNo statistics available. Your library is empty.\n")
#         return

#     total_books = len(all_books)
#     read_books = sum(1 for book in all_books if book["read"].lower() == "yes")
#     unread_books = total_books - read_books
#     read_percentage = (read_books / total_books) * 100

#     print("\n📊 Library Statistics:")
#     print(f"Total books       : {total_books}")
#     print(f"Books read        : {read_books}")
#     print(f"Books not read    : {unread_books}")
#     print(f"Percentage read   : {read_percentage:.2f}%")

# while True:
#     menu()
#     choice = input("Enter your choice: ")
#     if choice == "1":
#         print("Add a book")
#         add_book()
#     elif choice == "2":
#         print("Remove a book")
#         remove_book()      
#     elif choice == "3":
#         print("Search for a book")
#         search_book()
#     elif choice == "4":
#         print("Display all books")
#         display_books()
#     elif choice == "5":
#         print("Display statistics")
#         display_statistics()
#     elif choice == "6":
#         print("Exit")   
#         break
#     else:
#         print("Invalid choice. Please try again.")



import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Personal Library Manager",
    page_icon="📚",
    layout="centered"
)
# Check if dark theme is enabled
theme = 'light'
try:
    if st.get_option("theme.base") == "dark":
        theme = 'dark'
except:
    pass

st.markdown(f"""
<style>
        .footer {{
        text-align: center;
        margin-top: 2.5rem;
        padding: 1.5rem;
        background-color: {("#F3F4F6" if theme == 'light' else "#2D3748")};
        border-radius: 15px;
        color: {("#6B7280" if theme == 'light' else "#9CA3AF")};
        font-size: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1s ease-in-out;
    }}
    </style>
""", unsafe_allow_html=True)

# Initialize book list
if "all_books" not in st.session_state:
    st.session_state.all_books = []

st.title("📚 Personal Library App")

# Sidebar Menu
menu = st.sidebar.radio("📌 Menu", ["Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Library Statistics"])

# Function to add a book
def add_book():
    st.subheader("➕ Add a Book")
    title = st.text_input("📖 Enter Book Title")
    author = st.text_input("✍️ Enter Author Name")
    publication_year = st.text_input("📅 Enter Publication Year")
    genre = st.text_input("🎭 Enter Genre")
    read_book = st.radio("📘 Have you read this book?", ["Yes", "No"])

    if st.button("Add Book"):
        book = {
            "title": title,
            "author": author,
            "publication-year": publication_year,
            "genre": genre,
            "read": read_book
        }
        st.session_state.all_books.append(book)
        st.success("✅ Book added successfully!")

# Function to remove a book
def remove_book():
    st.subheader("❌ Remove a Book")
    if not st.session_state.all_books:
        st.warning("⚠️ No books available to remove.")
        return

    book_names = [book["title"] for book in st.session_state.all_books]
    book_to_remove = st.selectbox("📖 Select Book to Remove", book_names)

    if st.button("Remove Book"):
        st.session_state.all_books = [book for book in st.session_state.all_books if book["title"] != book_to_remove]
        st.success(f"✅ '{book_to_remove}' has been removed!")

# Function to search for a book
def search_book():
    st.subheader("🔍 Search for a Book")
    search_query = st.text_input("🔎 Enter Book Title or Author Name")

    if st.button("Search"):
        results = [book for book in st.session_state.all_books if book["title"].lower() == search_query.lower() or book["author"].lower() == search_query.lower()]
        
        if results:
            for book in results:
                st.write(f"**Title:** {book['title']}")
                st.write(f"**Author:** {book['author']}")
                st.write(f"**Publication Year:** {book['publication-year']}")
                st.write(f"**Genre:** {book['genre']}")
                st.write(f"**Read:** {book['read']}")
                st.markdown("---")
        else:
            st.warning("❌ Book not found!")

# Function to display all books
def display_books():
    st.subheader("📖 All Books in Library")
    
    if not st.session_state.all_books:
            st.info("Your library is empty.")
    else:
        df = pd.DataFrame(st.session_state.all_books)
        st.dataframe(df, use_container_width=True)

# Function to display statistics
def display_statistics():
    st.subheader("📊 Library Statistics")
    if not st.session_state.all_books:
        st.warning("⚠️ No books in the library.")
        return

    total_books = len(st.session_state.all_books)
    read_books = sum(1 for book in st.session_state.all_books if book["read"].lower() == "yes")
    unread_books = total_books - read_books
    read_percentage = (read_books / total_books) * 100

    st.write(f"📚 **Total Books:** {total_books}")
    st.write(f"✅ **Books Read:** {read_books}")
    st.write(f"📖 **Books Not Read:** {unread_books}")
    st.write(f"📊 **Percentage Read:** {read_percentage:.2f}%")

# Render Selected Menu
if menu == "Add a Book":
    add_book()
elif menu == "Remove a Book":
    remove_book()
elif menu == "Search for a Book":
    search_book()
elif menu == "Display All Books":
    display_books()
elif menu == "Library Statistics":
    display_statistics()


# Footer
st.markdown("""
<div class="footer">
    <p>Secure Personal Library Manager | Stay Safe Online | <a href="https://github.com/SitesByKashan">Made By M Kashan Malik Awan</a> </p>
</div>
""", unsafe_allow_html=True)
