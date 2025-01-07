# thermometer.py file - Define the Thermometer class

import random

class Thermometer:
    def __init__(self):
        """Initializes the thermometer, which is initially turned off."""
        self.is_on = False
        self.temperature = None

    def turn_on(self):
        """Turns on the thermometer."""
        self.is_on = True
        print("Thermometer is now ON.")

    def turn_off(self):
        """Turns off the thermometer."""
        self.is_on = False
        print("Thermometer is now OFF.")

    def measure_temperature(self):
        """Simulates temperature measurement by generating a random temperature between 34.0 and 42.0 degrees Celsius."""
        if self.is_on:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
            print(f"Temperature measured: {self.temperature}°C")
        else:
            print("Please turn on the thermometer first.")

    def display_temperature(self):
        """Displays the temperature with fever and critical temperature messages if applicable."""
        if self.temperature is not None:
            message = f"Temperature: {self.temperature}°C"
            if self.temperature >= 41.0:
                message += " (CRITICAL TEMPERATURE!!)"
            elif self.temperature >= 37.0:
                message += " (fever)"
            print(message)
        else:
            print("No temperature measured yet. Please measure the temperature first.")
