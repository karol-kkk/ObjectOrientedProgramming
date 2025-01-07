# main.py file - Main program to interact with the EBook class

from ebook import EBook  # Import the EBook class from the ebook.py file

def main():
    # Create an e-book object with title, author, and number of pages
    my_book = EBook("Python Programming", "John Doe", 100)

    # Show book status (initially closed)
    my_book.show_status()

    # Open the book
    print("\nOpening the book...")
    my_book.open_book()

    # Display book status after opening
    my_book.show_status()

    # Read a few pages (move to the next pages)
    print("\nReading a few pages...")
    my_book.next_page()
    my_book.next_page()
    my_book.next_page()

    # Display book status after reading a few pages
    my_book.show_status()

    # Close the book
    print("\nClosing the book...")
    my_book.close_book()

    # Attempt to read a few more pages after closing the book (should display message that the book is closed)
    print("\nTrying to read after closing the book...")
    my_book.next_page()

if __name__ == "__main__":
    main()
