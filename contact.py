# contact.py - Defines the Contact class

class Contact:
    def __init__(self, name, email, telephone):
        """Initializes a contact with name, email, and telephone."""
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        """Returns a string representation of the contact."""
        return f"{self.name} - {self.email} - {self.telephone}"
