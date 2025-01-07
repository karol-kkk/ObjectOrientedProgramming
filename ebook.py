# ebook.py file - Define the EBook class

class EBook:
    def __init__(self, title, author, number_of_pages):
        """Initialize the book with title, author, number of pages, and set the current page to 1 (closed state)."""
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page = 1  # Initially, the book is at page 1
        self.is_open = False  # Initially, the book is closed

    def open_book(self):
        """Open the book and set the status to open."""
        if not self.is_open:
            self.is_open = True
            self.current_page = 1  # Start reading from page 1 when the book is opened
            print(f"The book '{self.title}' is now open.")
        else:
            print(f"The book '{self.title}' is already open.")

    def close_book(self):
        """Close the book and set the status to closed."""
        if self.is_open:
            self.is_open = False
            print(f"The book '{self.title}' is now closed.")
        else:
            print(f"The book '{self.title}' is already closed.")

    def next_page(self):
        """Move to the next page if the book is open."""
        if self.is_open:
            if self.current_page < self.number_of_pages:
                self.current_page += 1
                print(f"Turned to page {self.current_page}.")
            else:
                print("You are already on the last page.")
        else:
            print("The book is closed. Please open the book first.")

    def previous_page(self):
        """Move to the previous page if the book is open."""
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f"Turned to page {self.current_page}.")
            else:
                print("You are already on the first page.")
        else:
            print("The book is closed. Please open the book first.")

    def show_status(self):
        """Display the current status of the book (title, author, page numbers, and current page)."""
        if self.is_open:
            print(f"Book Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Total Pages: {self.number_of_pages}")
            print(f"Current Page: {self.current_page}")
        else:
            print(f"The book '{self.title}' is closed.")
