# main.py file - Main program to interact with the Thermometer class

from thermometer import Thermometer  # Import the Thermometer class from the thermometer.py file

def main():
    # Create a Thermometer object
    thermometer = Thermometer()

    # Turn on the thermometer
    thermometer.turn_on()

    # Measure the temperature
    thermometer.measure_temperature()

    # Display the measured temperature with appropriate messages
    thermometer.display_temperature()

    # Turn off the thermometer
    thermometer.turn_off()

if __name__ == "__main__":
    main()
