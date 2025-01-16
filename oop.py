# 1
# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.major = ""  # third attribute added

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()  # third student added

    # Assigning values to all attributes
    student1.name = "Dominic"
    student1.age = 19
    student1.major = "Computer Science"

    student2.name = "Olivia"
    student2.age = 21
    student2.major = "Biology"

    student3.name = "Ethan"
    student3.age = 20
    student3.major = "Mathematics"

    # Printing information about all students
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, Major: {student1.major}')
    print(f'{student2.name}, {student2.age} years old, Major: {student2.major}')
    print(f'{student3.name}, {student3.age} years old, Major: {student3.major}')

if __name__ == "__main__":
    main()

# 2
class Square:
   def __init__(self, a):
      self.a = a

   def area(self):
      return self.a * self.a

   def perimeter(self):
      return 4 * self.a

# Creating squares with sides of 4 and 6
square1 = Square(4)
square2 = Square(6)

# Printing the results for both squares
print('Square with side 4:')
print(f'Area is {square1.area()}, Perimeter is {square1.perimeter()}')

print('Square with side 6:')
print(f'Area is {square2.area()}, Perimeter is {square2.perimeter()}')

# 3
class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km  # value in € 
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Distance: {self.distance} km")
        print(f"Rate: €{self.rate_per_km} per km")
        print(f"Fare: €{self.fare:.2f}")


def main():
    # Creating two TaxiRide objects with different rates
    ride1 = TaxiRide(2)  # €2 per km
    ride2 = TaxiRide(3)  # €3 per km

    # Calculating the fares for both rides
    ride1.calculate_fare(10)  # 10 km for ride 1
    ride2.calculate_fare(15)  # 15 km for ride 2

    # Printing the receipts for both rides
    print("Receipt for Ride 1:")
    ride1.print_receipt()

    print("\nReceipt for Ride 2:")
    ride2.print_receipt()


if __name__ == "__main__":
    main()

#4
class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"Timeline for {self.username}:")
        for i, post in enumerate(self.posts, 1):
            print(f"{i}. {post}")


def main():
    # Creating a user named 'johndoe'
    user = SocialMediaProfile('johndoe')

    # Adding posts to the user's timeline
    user.add_post("Hello, world!")
    user.add_post("Had a great day at the park!")
    user.add_post("What's up, Natalie? How are you?")

    # Displaying the user's timeline
    user.display_timeline()


if __name__ == "__main__":
    main()

#5
# class definition
class Book():
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price  # price attribute
        self.current_page = 1
        self.is_open = False

    def open(self):
        self.is_open = True
    
    def close(self):
        self.is_open = False
    
    def change_page(self, page):
        self.current_page = page

    def display_info(self):
        print(f"My favourite book is {self.title}.")
        print(f"Written by {self.author}.")
        print(f"This book has {self.pages} pages.")
        print(f"The price of the book is €{self.price}.")  # displaying the price
        if self.is_open:
            print(f"I am just reading the book, page {self.current_page}.")
        else:
            print("I am going to read the book later.")


def main():
    # object creation based on the Book class with price
    favourite_book = Book(
        "Harry Potter and the Philosopher's Stone",
        "J. K. Rowling", 223, 48)  

    # object manipulation
    favourite_book.open()
    favourite_book.change_page(15)
    favourite_book.display_info()
    favourite_book.close()

if __name__ == "__main__":
    main()

#6
class Phone:
    def __init__(self, battery_level, is_screen_on, is_connected):
        self.battery_level = battery_level  # Battery percentage (0-100)
        self.is_screen_on = is_screen_on  # Boolean for screen status (True/False)
        self.is_connected = is_connected  # Boolean for connectivity status (True/False)

    def charge(self, amount):
        ##Charge the phone by a certain amount.##
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Charging... Battery is now at {self.battery_level}%.")

    def turn_on_screen(self):
        ##Turn on the phone's screen.##
        self.is_screen_on = True
        print("The screen is now on.")

    def turn_off_screen(self):
        ##Turn off the phone's screen.##
        self.is_screen_on = False
        print("The screen is now off.")

    def toggle_connectivity(self):
        ##Toggle connectivity status.##
        self.is_connected = not self.is_connected
        status = "connected" if self.is_connected else "disconnected"
        print(f"Connectivity is now {status}.")

    def display_status(self):
        ##Display the current status of the phone.##
        print(f"Battery level: {self.battery_level}%")
        print(f"Screen is {'on' if self.is_screen_on else 'off'}.")
        print(f"Connectivity: {'connected' if self.is_connected else 'disconnected'}.")


def main():
    # Create a phone object with initial attributes
    my_phone = Phone(battery_level=50, is_screen_on=False, is_connected=True)

    # Display initial status
    my_phone.display_status()

    # Perform some behaviors
    my_phone.charge(30)  # Charge the phone
    my_phone.turn_on_screen()  # Turn on the screen
    my_phone.toggle_connectivity()  # Toggle connectivity

    # Display updated status
    my_phone.display_status()


if __name__ == "__main__":
    main()
