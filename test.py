# class definition
class Song:
    def __init__(self, artist, title, album, year):
        self.artist = artist  # Artist of the song
        self.title = title    # Title of the song
        self.album = album    # Album the song is part of
        self.year = year      # Year the song was released

    def __str__(self):
        # Returns a string representation of the song in the desired format
        return f"Performer: {self.artist}\nTitle:     {self.title}\nAlbum:     {self.album}\nYear:      {self.year}\n"


# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

## object usage
print(song1)
print(song2)
