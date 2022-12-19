class Music_Piece():

    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return f'''
Performer: {self.artist}
Song:      {self.track_title}
Album:     {self.album}
Year:      {self.year}
        '''


song1 = Music_Piece("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
song2 = Music_Piece("Smash into pieces", "Throne", "Disconnect", "2021")
song3 = Music_Piece("aaaa", "bbbb", "cccc", "dddd")
print(song1, song2, song3)
