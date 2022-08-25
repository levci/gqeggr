from distutils.command.config import LANG_EXT
from getpass import getuser
import threading, queue, time, os, requests, yt_dlp, glob
from deezer import deezer
from pydeezer import Downloader
from pydeezer.constants import track_formats
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from lang import getUserLang
from mutagen.easyid3 import ID3
from meta import *
from telegram import (InputMediaAudio, Audio)
from spotdl.search.spotifyClient import get_spotify_client
from spotdl.search.utils import get_playlist_tracks, get_album_tracks
from spotify import get_songObj

cap = '@just_another_day_with_music'
ext = '.mp3'
ydl_opts = {"cachedir": False, "cookiefile": "cookies.txt", 'restrictfilenames': True, 'outtmpl': '%(id)s.%(ext)s', 'writethumbnail': True, 'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}, {'key': 'EmbedThumbnail'}, {'key': 'FFmpegMetadata'}]}

def unshorten(url):
    session = requests.Session()  # so connections are recycled
    resp = session.head(url, allow_redirects=True)
    return resp.url

# def nonAscii(text):
#     title = text.encode("ascii", "ignore")
#     text = title.decode()
#     for disallowedChar in ['"','/','?', '\\', '*', '<', '>']:
#         if disallowedChar in text:
#             text = text.replace(
#                 disallowedChar, '')
#     return text


def download_song(link, ydl_opts):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info("{}".format(link))
            return result
    except Exception as e:
        print(e)
        return False

def download_youtube(update, context, link):
    data = download_song(link, ydl_opts)
    language_dict = getUserLang(update)
    if data:
        title = data['id'] + '.mp3'
        context.bot.send_chat_action(update.message.chat.id, 'upload_audio')
        cap = '@just_another_day_with_music'
        if context.chat_data['access']:
            cap = ''
        try:
            context.bot.send_audio(chat_id=update.message.chat.id, audio=open(title, 'rb'), thumb=urlopen(data['thumbnails'][-1]['url']), caption=cap, timeout=60000)
        except Exception as e:
            context.bot.send_message(update.message.chat.id, language_dict['cantDownload'])
    else:
        context.bot.send_chat_action(update.message.chat.id, 'typing')
        context.bot.send_message(update.message.chat.id, language_dict['cantDownload'])

def download_play(update, context, link):
    pid = link.split('?list=')[-1]
    ydl_opt = ydl_opts.copy()
    ydl_opt['outtmpl'] = pid+'/%(title)s-%(id)s.%(ext)s'
    cap = '@just_another_day_with_music'
    language_dict = getUserLang(update)
    try:
        with yt_dlp.YoutubeDL(ydl_opt) as ydl:
            ydl.download([link])
    except:
        context.bot.send_chat_action(update.message.chat.id, 'typing')
        context.bot.send_message(update.message.chat.id, language_dict['cantDownload'])
    if context.chat_data['access']:
        cap = ''
    for song in glob.glob(pid+'/*.mp3'):
        context.bot.send_audio(chat_id=update.message.chat.id, audio=open(song, 'rb'), caption=cap, timeout=60000)

def download_spotify(update, context, link):
    cap = '@just_another_day_with_music'
    language_dict = getUserLang(update)
    try:
        song = get_songObj(link)
    except Exception as e:
        print(e, link)
        context.bot.send_message(update.message.chat.id, language_dict['cantDownload'])
        return
    if song.get_youtube_link() is not None:
        data = download_song(song.get_youtube_link(), ydl_opts)
        ext = '.mp3'
        if data:
            title = data['id']
            context.bot.send_chat_action(update.message.chat.id, 'upload_audio')
            set_id3_data(title+ext, song)
            if context.chat_data['access']:
                cap = ''
            context.bot.send_audio(chat_id=update.message.chat.id, audio=open(title+ext, 'rb'), caption=cap, timeout=60000)
            return

    search = deezer.search_tracks(song.get_song_name())
    download_deezer(update, context, search[0]['link'])

def download_spotify_album(update, context, link):
    spotifyClient = get_spotify_client()
    trackResponse = spotifyClient.album_tracks(link)
    albumLen = len(trackResponse['items'])
    language_dict = getUserLang(update)
    if albumLen < 1:
        context.bot.send_message(update.message.chat.id, language_dict['cantDownload'])
    if albumLen > 50:
        context.bot.send_message(update.message.chat.id, language_dict['albumLimit'])
        return
    songObjList = get_album_tracks(link)
    for song in songObjList:
        if song.get_youtube_link() is not None:
            download_youtube(update, context, song.get_youtube_link())
        else:
            context.bot.send_message(update.message.chat.id, language_dict['cantDownload'] + ': ' + song.get_song_name())

def download_spotify_play(update, context, link):
    language_dict = getUserLang(update)
    spotifyClient = get_spotify_client()
    playlistResponse = spotifyClient.playlist_tracks(link)
    playlistLen = len(playlistResponse['items'])
    if playlistLen < 1:
        context.bot.send_message(update.message.chat.id, language_dict['cantDownload'])
    if playlistLen > 50:
        context.bot.send_message(update.message.chat.id, language_dict['playlistLimit'])
        return
    songObjList = get_playlist_tracks(link)
    for song in songObjList:
        if song.get_youtube_link() is not None:
            download_youtube(update, context, song.get_youtube_link())
        else:
            context.bot.send_message(update.message.chat.id, language_dict['cantDownload'] + ': ' + song.get_song_name())

def check_user(_, context, user_id):
    try:
        chat_id = '-1001466021420'
        data = context.bot.get_chat_member(chat_id, user_id)
        if data['status'] == 'member' or data['status'] == 'creator' or data['status'] == 'administrator':
            return True
    except Exception as e:
        print(e)
    return False

def download_deezer(update, context, link):
    cap = '@just_another_day_with_music'
    track_id = link.split('/track/')[1].split("?")[0]
    track = deezer.get_track(track_id)
    query = update.message or update.callback_query.message
    user_id = query.from_user.id 
    chat_id = query.chat.id
    context.chat_data['access'] = check_user(update, context, user_id)
    if track:
        print(1)
        path = os.path.dirname(__file__)
        if context.chat_data['access']:
            cap = ''
        track_name = track["download"](os.path.dirname(__file__), quality=track_formats.MP3_320)
        print(track_name)
        # track_name = track['tags']['title'] + '.mp3'
        cover = track['tags']['_albumart']['image']
        # track_name = nonAscii(track_name)
        data = get_mp3_data(track_name)
        audioFile = ID3(track_name)
        fb = open(track_name[:-4] + '.png', 'wb')
        fb.write(cover)
        fb.close()
        thumb = multipart.to_bytes(open(track_name[:-4] + '.png', 'rb'))
        context.bot.send_audio(chat_id=chat_id, audio=open(track_name, 'rb'), caption=cap, duration=track['info']['DATA']['DURATION'], thumb=thumb, timeout=60000, performer=data['artist'][0], title=data['title'][0])
    else:
        context.bot.send_chat_action(chat_id, 'typing')
        context.bot.send_message(chat_id, getUserLang(update)['cantDownload'])

def download_from_link(update, context, url=None, p=None):
    message = update.message or update.callback_query.message
    language_dict = getUserLang(update)
    startDownload = language_dict['startDownload']
    if url:
        context.bot.send_message(message.chat.id, startDownload)
        download_deezer(update, context, unshorten(url))
        return
    links = [x for x in message.text.split(' ') if 'spotify' in x or 'youtu' in x or 'deezer' in x]
    links = [unshorten(x) for x in message.text.split('\n') if 'spotify' in x or 'youtu' in x or 'deezer' in x]
    if len(links) < 1:
        return
    for link in links:
        if 'spotify' in link and 'track' in link:
            context.bot.send_message(message.chat.id, startDownload)
            download_spotify(update, context, link)
            

        elif 'youtu' in link and 'playlist' in link and p:
            context.bot.send_message(message.chat.id, startDownload)
            download_play(update, context, link)
            

        elif 'youtu' in link:
            context.bot.send_message(message.chat.id, startDownload)
            download_youtube(update, context, link)
            

        elif 'spotify' in link and 'playlist' in link and p:
            context.bot.send_message(message.chat.id, startDownload)
            download_spotify_play(update, context, link)
                

        elif 'spotify' in link and 'album' in link and p:
            context.bot.send_message(message.chat.id, startDownload)
            download_spotify_album(update, context, link)
                
                
        elif 'deezer' in link:
            link = unshorten(link)
            if 'track' in link:
                context.bot.send_message(message.chat.id, startDownload)
                download_deezer(update, context, unshorten(link))
                
            elif 'album' in link and p:
                album_id = link.split('/album/')[1].split("?")[0]
                album = deezer.get_album(album_id)
                context.bot.send_message(message.chat.id, startDownload)
                if len(album) > 50:
                    context.bot.send_message(message.chat.id, language_dict['albumLimit'])
                    return
                for track in album['tracks']['data']:
                    download_deezer(update, context, track['link'])
                    
            elif 'playlist' in link and p:
                playlist_id = link.split('/playlist/')[1].split("?")[0]
                playlist = deezer.get_playlist(playlist_id)
                context.bot.send_message(message.chat.id, startDownload)
                if len(playlist) > 50:
                    context.bot.send_message(message.chat.id, language_dict['playlistLimit'])
                    return
                for track in playlist['SONGS']['data']:
                    tl = 'https://www.deezer.com/en/track/' + track['SNG_ID']
                    download_deezer(update, context, tl)							
        
        return

def download_shazam(update, context):
    query = update.callback_query
    print(update)
    data = query.data.split('|')
    if len(data) > 2:
        search = deezer.search_tracks(data[1] + ' - ' + data[2])
        link = search[0]['link']
    else:
        link = data[1]
    ql = q.qsize()
    ql1 = q1.qsize()
    ket = []
    language_dict = getUserLang(update)
    lang_pos, lang_current = language_dict['pos_queue'], language_dict['pos_current']
    if str(query.from_user['id']) == '626516815':
        context.bot.send_message(query.message.chat.id, f'{lang_pos}: {qv.qsize()+1}')
        qv.put([link, update, context])
        return
    if ql > ql1:
        pss = context.bot_data['que_pos'][1] + ql1
        pss = pss+1 if context.bot_data['que_work'][1] == True else pss
        ket.append([InlineKeyboardButton(lang_current, callback_data=f'position|1|{pss}')])
        reply_markup = InlineKeyboardMarkup(ket)
        context.bot.send_message(query.message.chat.id, f'{lang_pos}: {ql1+1}', reply_markup=reply_markup)
        q1.put([link, update, context])
    else:
        pss = context.bot_data['que_pos'][0] + ql
        pss = pss+1 if context.bot_data['que_work'][0] == True else pss
        ket.append([InlineKeyboardButton(lang_current, callback_data=f'position|0|{pss}')])
        reply_markup = InlineKeyboardMarkup(ket)
        context.bot.send_message(query.message.chat.id, f'{lang_pos}: {ql+1}', reply_markup=reply_markup)
        q.put([link, update, context])
    query.answer()

q = queue.Queue()
def worker():
    while True:
        item = q.get()
        url, update, context = item 
        context.bot_data['que_work'][0] = True
        print(f'Working on {item[0]}')
        chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id
        try:
            download_from_link(update, context, url)
        except Exception as e:
            try:
                context.bot.send_chat_action(chat_id, 'typing')
                context.bot.send_message(chat_id, getUserLang(update)['cantDownload'])
            except:
                pass
        context.bot_data['que_pos'][0] += 1
        context.bot_data['que_work'][0] = False
        print(f'Finished {item[0]}')
        q.task_done()

q1 = queue.Queue()
def worker1():
    while True:
        time.sleep(0.05)
        item = q1.get()
        url, update, context = item 
        context.bot_data['que_work'][1] = True
        print(f'Working on {item[0]}')
        chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id
        try:
            download_from_link(update, context, url)
        except Exception as e:
            try:
                context.bot.send_chat_action(chat_id, 'typing')
                context.bot.send_message(chat_id, getUserLang(update)['cantDownload'])
            except:
                pass
        context.bot_data['que_pos'][1] += 1
        context.bot_data['que_work'][1] = False
        print(f'Finished {item[0]}')
        q1.task_done()

qv = queue.Queue()
def workervip():
    while True:
        item = qv.get()
        url, update, context = item 
        print(f'Working on {item[0]}')
        chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id
        try:
            download_from_link(update, context, url)
        except Exception as e:
            try:
                context.bot.send_chat_action(chat_id, 'typing')
                context.bot.send_message(chat_id, getUserLang(update)['cantDownload'])
            except:
                pass
        print(f'Finished {item[0]}')
        qv.task_done()

qp = queue.Queue()
def workerp():
    while True:
        item = qp.get()
        url, update, context, p = item 
        context.bot_data['que_work'][2] = True
        print(f'Working on {item[0]}')
        chat_id = update.message.chat.id if update.message else update.callback_query.message.chat.id
        try:
            download_from_link(update, context, url, p)
        except Exception as e:
            print(e)
            try:
                context.bot.send_chat_action(chat_id, 'typing')
                context.bot.send_message(chat_id, getUserLang(update)['cantDownload'])
            except:
                pass
        context.bot_data['que_pos'][2] += 1
        context.bot_data['que_work'][2] = False
        print(f'Finished {item[0]}')
        qp.task_done()

qvia = queue.Queue()
def workervia():
    while True:
        item = qvia.get()
        link, update, context, inline = item 
        context.bot_data['que_work'][3] = True
        print(f'Working on {item[0]}')
        chat_id = '-1001500010935'
        try:
            cap = '@just_another_day_with_music'
            track_id = link.split('/track/')[1].split("?")[0]
            track = deezer.get_track(track_id)
            # context.chat_data['access'] = chec_user(update, context, user_id)
            if track:
                path = os.path.dirname(__file__)
                track_name = track["download"](os.path.dirname(__file__), quality=track_formats.MP3_320)
                print(track_name)
                # track_name = track['tags']['title'] + '.mp3'
                cover = track['tags']['_albumart']['image']
                # track_name = nonAscii(track_name)
                data = get_mp3_data(track_name)
                audioFile = ID3(track_name)
                fb = open(track_name[:-4] + '.png', 'wb')
                fb.write(cover)
                fb.close()
                thumb = multipart.to_bytes(open(track_name[:-4] + '.png', 'rb'))
                msg = context.bot.send_audio(chat_id=chat_id, audio=open(track_name, 'rb'), caption=cap, duration=track['info']['DATA']['DURATION'], thumb=thumb, timeout=60000, performer=data['artist'][0], title=data['title'][0])
                context.bot.edit_message_media(media=InputMediaAudio(Audio(file_id=msg.audio.file_id, 
                    file_unique_id=msg.audio.file_unique_id, 
                    duration=msg.audio.duration),
                    caption=cap,
                    thumb=thumb),
                    inline_message_id=inline,
                )
            else:
                context.bot.send_chat_action(chat_id, 'typing')
                context.bot.send_message(chat_id, getUserLang(update)['cantDownload'])
        except Exception as e:
            print(e)
            try:
                context.bot.send_chat_action(chat_id, 'typing')
                context.bot.send_message(chat_id, getUserLang(update)['cantDownload'])
            except:
                pass
        context.bot_data['que_pos'][3] += 1
        context.bot_data['que_work'][3] = False
        print(f'Finished {item[0]}')
        qvia.task_done()

threading.Thread(target=worker, daemon=True).start()
threading.Thread(target=worker1, daemon=True).start()
threading.Thread(target=workerp, daemon=True).start()
threading.Thread(target=workervip, daemon=True).start()
threading.Thread(target=workervia, daemon=True).start()