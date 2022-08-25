from spotdl.search.songObj import SongObj
from spotdl.search import spotifyClient
import os 

spotifyClient.initialize(
	clientId=os.environ.get("SPOTIFY_CLIENT_ID"),
	clientSecret=os.environ.get('SPOTIFY_CLIENT_SECRET')
)

def get_songObj(link: str) -> SongObj:
	return SongObj.from_url(link)