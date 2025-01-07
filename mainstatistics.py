# main.py - Main program to interact with the Statistics class

from statistics import Statistics  # Import the Statistics class from statistics.py

def main():
    # Create a Statistics object
    stats = Statistics()

    # List of numbers to calculate statistics
    numbers = [12, 37, 6, 9, 17]

    # Add numbers to the Statistics object
    for number in numbers:
        stats.add_number(number)

    # Display the list of numbers
    stats.display_numbers()

    # Print the statistical values
    stats.print_statistics()

if __name__ == "__main__":
    main()
