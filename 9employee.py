class Employee:
    def __init__(self, name, surname, age, seniority):
        """Initializes an employee with the given attributes."""
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        """Returns the text representation of the employee."""
        first_letter_name = self.name[0]
        last_name = self.surname
        seniority = self.seniority
        
        # If employee is an adult (18 or older), use uppercase letters
        if self.age >= 18:
            return f"{last_name.upper()}{first_letter_name.upper()}{seniority}"
        else:
            return f"{last_name.lower()}{first_letter_name.lower()}{seniority}"

# Example usage:

# Creating employee objects and printing their text representations
employee1 = Employee("Anna", "May", 17, 7)
employee2 = Employee("George", "Brown", 21, 4)

print(employee1)  # Output: maya7
print(employee2)  # Output: BROWNG4
