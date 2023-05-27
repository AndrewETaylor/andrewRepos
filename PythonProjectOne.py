class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

def get_song_title(song):
    return song.title

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def sort_by_title(self):
        self.songs.sort(key=get_song_title,reverse=False)

    def print_songs(self,song_count):
        for index in range(len(self.songs)):
            if index < song_count:
                print(f"{index+1}. {self.songs[index].title} (by {self.songs[index].artist})")


playlist = Playlist()
while True:
    title = input('Song title (or blank to finish): ')
    if title == '':
        break
    artist = input('Artist name: ')
    song = Song(title, artist)
    playlist.add_song(song)

playlist.sort_by_title()
num_songs = int(input('How many songs do you want to display? '))
playlist.print_songs(num_songs)