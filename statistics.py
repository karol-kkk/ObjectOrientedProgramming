# statistics.py - Class definition for Statistics

class Statistics:
    def __init__(self):
        """Initializes the list of numbers."""
        self.numbers = []

    def add_number(self, number):
        """Adds a number to the list."""
        self.numbers.append(number)

    def display_numbers(self):
        """Displays all the numbers in the list separated by space."""
        print("Numbers:", " ".join(map(str, self.numbers)))

    def greatest_number(self):
        """Returns the greatest number in the list."""
        return max(self.numbers)

    def smallest_number(self):
        """Returns the smallest number in the list."""
        return min(self.numbers)

    def arithmetic_mean(self):
        """Returns the arithmetic mean of the numbers."""
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def median(self):
        """Returns the median of the numbers."""
        sorted_numbers = sorted(self.numbers)
        n = len(sorted_numbers)
        if n % 2 == 0:
            # If even, median is the average of the two middle values
            return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
        else:
            # If odd, median is the middle value
            return sorted_numbers[n//2]

    def print_statistics(self):
        """Prints the statistical values."""
        print(f"Greatest number: {self.greatest_number()}")
        print(f"Smallest number: {self.smallest_number()}")
        print(f"Arithmetic mean: {self.arithmetic_mean():.2f}")
        print(f"Median: {self.median()}")
