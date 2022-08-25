from pydeezer import Deezer
import os

deezer = Deezer()
arl = os.environ.get('DEEZER_TOKEN')

user_info = deezer.login_via_arl(arl)