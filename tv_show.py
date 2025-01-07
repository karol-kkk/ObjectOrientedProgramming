# tv_show.py file
# main program
import tv  # Import the TV class from the tv.py file

def main():
    # object creation
    my_tv = tv.TV()  # Create an instance of the TV class

    # object usage
    print("Create TV set")
    my_tv.show_status()  # Show TV status (Initially, it should be off)

    print("Turn TV on")
    my_tv.turn_on()  # Turn the TV on
    my_tv.show_status()  # Show the status (Now it should be on, channel 1, volume 0)

    print("Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery, Eurosport")
    my_tv.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery", "Eurosport"])  # Set the available channels
    my_tv.show_channels()  # Display the available channels list

    print("Change channel to 4")
    my_tv.set_channel(4)  # Change to channel 4 (TVN)
    my_tv.show_status()  # Show the status (TV is on, channel 4 (TVN), volume 0)

    print("Increase volume")
    my_tv.increase_volume()  # Increase the volume by 1
    my_tv.show_status()  # Show the status (TV is on, channel 4 (TVN), volume 1)

    print("Increase volume again")
    my_tv.increase_volume()  # Increase the volume by 1
    my_tv.show_status()  # Show the status (TV is on, channel 4 (TVN), volume 2)

    print("Decrease volume")
    my_tv.decrease_volume()  # Decrease the volume by 1
    my_tv.show_status()  # Show the status (TV is on, channel 4 (TVN), volume 1)

    print("Decrease volume to 0")
    my_tv.decrease_volume()  # Decrease the volume to 0
    my_tv.show_status()  # Show the status (TV is on, channel 4 (TVN), volume 0)

    print("Turn TV off")
    my_tv.turn_off()  # Turn the TV off
    my_tv.show_status()  # Show the status (Now it should be off, volume 0)

if __name__ == "__main__":
    main()
