class songObject():

	def __init__(self, title, artists, cover):
		self.title = title
		self.artists = artists
		self.cover = cover

	def get_song_name(self):
		return self.title

	def get_track_number(self):
		return 1

	def get_genres(self):
		return ['pop']

	def get_contributing_artists(self):
		return self.artists

	def get_album_name(self):
		return 'https://t.me/just_another_day_with_music'

	def get_album_artists(self):
		return self.artists

	def get_album_release(self):
		return '2022'

	def get_album_cover_url(self):
		return self.cover