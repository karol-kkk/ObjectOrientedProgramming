# contact_list.py - Defines the ContactList class

from contact import Contact  # Import the Contact class

class ContactList:
    def __init__(self):
        """Initializes an empty list of contacts."""
        self.contacts = []

    def add_contact(self, contact):
        """Adds a new contact to the contact list."""
        self.contacts.append(contact)

    def display_contacts(self):
        """Displays all contacts in the contact list."""
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)
