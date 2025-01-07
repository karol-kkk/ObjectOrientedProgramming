# smartphone.py - Main program for managing contacts

from contact_list import ContactList  # Import the ContactList class
from contact import Contact  # Import the Contact class

def main():
    # Create a ContactList object
    contact_list = ContactList()

    # Create contacts
    contact1 = Contact("John Brown", "brown@onet.pl", "555234000")
    contact2 = Contact("Anna May", "am@o2.pl", "232000199")
    contact3 = Contact("George Small", "smallg@google.pl", "222999100")
    contact4 = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")

    # Add contacts to the contact list
    contact_list.add_contact(contact1)
    contact_list.add_contact(contact2)
    contact_list.add_contact(contact3)
    contact_list.add_contact(contact4)

    # Display the contact list
    print("Contact List on Smartphone:")
    contact_list.display_contacts()

if __name__ == "__main__":
    main()
