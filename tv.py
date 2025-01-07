# tv.py file
# class definition
class TV:
    def __init__(self):
        self.is_on = False  # Initially, the TV is off
        self.channel_no = 1  # Initially, the TV is set to channel 1
        self.channels = []  # Initially, there are no channels available
        self.volume = 0  # Initially, the volume is 0

    def turn_on(self):
        self.is_on = True  # Turn the TV on

    def turn_off(self):
        self.is_on = False  # Turn the TV off

    def set_channel(self, new_channel_no):
        if self.is_on and new_channel_no <= len(self.channels):  # Set the channel only if the TV is on and the channel exists
            self.channel_no = new_channel_no

    def set_channels(self, channels_list):
        self.channels = channels_list  # Set the list of available channels

    def show_channels(self):
        if self.channels:
            print("Channel list:")
            for idx, channel in enumerate(self.channels, 1):
                print(f"{idx}. {channel}")  # Print the list of available channels
        else:
            print("No channels available.")

    def show_status(self):
        if self.is_on:
            # Print the TV status, channel number, channel name (if exists), and volume level
            if self.channel_no <= len(self.channels):
                print(f"TV is on, channel {self.channel_no} ({self.channels[self.channel_no - 1]}), volume {self.volume}")
            else:
                print(f"TV is on, channel {self.channel_no}, volume {self.volume}")
        else:
            print(f"TV is off, volume {self.volume}")

    def increase_volume(self):
        if self.volume < 10:
            self.volume += 1  # Increase the volume by 1, ensuring it doesn't exceed 10

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1  # Decrease the volume by 1, ensuring it doesn't go below 0
