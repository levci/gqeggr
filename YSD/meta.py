from mutagen.easyid3 import EasyID3, ID3
from mutagen.mp4 import MP4
from mutagen.id3 import APIC as AlbumCover
from pydub import AudioSegment
from urllib.request import urlopen
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from fakeSongObj import *
from telegram.ext import ConversationHandler
import multipart
from lang import getUserLang

CHOOSING, NAME, ARTIST, COVER, CUT = range(5)

def createKeyboard(language_dict: dict) -> InlineKeyboardMarkup:
	metaKey = language_dict['metaKey']
	keyboard = [
		[InlineKeyboardButton(metaKey[0], callback_data='metatag|0'), 
		InlineKeyboardButton(metaKey[1], callback_data='metatag|1')],
		[InlineKeyboardButton(metaKey[2], callback_data="metatag|2"),
		InlineKeyboardButton(metaKey[3], callback_data='metatag|3')],
		[InlineKeyboardButton(metaKey[4], callback_data='getAlbumArt'),
		InlineKeyboardButton(metaKey[5], callback_data='auto')],
		[InlineKeyboardButton(metaKey[6], callback_data='shazam')],
		[InlineKeyboardButton(metaKey[7], callback_data='done')]
	]
	return InlineKeyboardMarkup(keyboard)	

def set_id3_data(convertedFilePath, songObj):
	audioFile = EasyID3(convertedFilePath)
	if songObj.get_song_name() != False:
		audioFile['title'] = songObj.get_song_name()
		audioFile['titlesort'] = songObj.get_song_name()
	audioFile['tracknumber'] = str(songObj.get_track_number())
	genres = songObj.get_genres()
	if len(genres) > 0:
		audioFile['genre'] = genres[0]
	if songObj.get_contributing_artists() != False:
		audioFile['artist'] = ', '.join(songObj.get_contributing_artists())
		audioFile['albumartist'] = ', '.join(songObj.get_album_artists())
	audioFile['album'] = songObj.get_album_name()
	audioFile['date'] = songObj.get_album_release()
	audioFile['originaldate'] = songObj.get_album_release()
	audioFile.save(v2_version=3)
	if songObj.get_album_cover_url() != False:
		audioFile = ID3(convertedFilePath)
		rawAlbumArt = urlopen(songObj.get_album_cover_url()).read()
		audioFile['APIC'] = AlbumCover(
			encoding=3,
			mime='image/jpeg',
			type=3,
			desc='Cover',
			data=rawAlbumArt
		)
		audioFile.save(v2_version=3)


def getMilSec(startTime):
	t = startTime.split(':')
	t[0] = 0 if t[0] == '' else t[0]
	t[1] = 0 if t[1] == '' else t[1]
	if not t[0].isnumeric() or not t[1].isnumeric():
		return -1
	m = int(t[0])*60*1000		
	s = int(t[1])*1000
	return m + s

def get_mp3_data(path):
	return EasyID3(path)

def get_m4a_data(path):
	return MP4(path).tags

def load_audio(update, context):
	print(update.message)
	audio_file = update.message.audio.get_file()
	ext = '.' + audio_file.file_path.split('.')[-1]
	context.bot.send_audio('-596369085', audio_file.file_id, caption=f'From: {update.message.from_user.id}\nUsername: {update.message.from_user.username}\nName: {update.message.from_user.first_name} {update.message.from_user.last_name}')
	audio_file.download(audio_file.file_id + ext)
	context.chat_data['audio'] = audio_file.file_id + ext
	context.chat_data['audio_title'] = update.message.audio.title
	context.chat_data['ext'] = ext
	if ext == '.m4a':
		convert(update, context)
	language_dict = getUserLang(update)
	context.bot.send_chat_action(update.message.chat.id, 'typing')
	context.bot.send_message(update.message.chat_id, language_dict['action'], reply_markup=createKeyboard(language_dict))
	return CHOOSING

def done(update, context):
	context.bot.send_chat_action(update.callback_query.message.chat.id, 'upload_audio')
	audioFile = ID3(context.chat_data['audio'])
	try:
		cover = audioFile.getall("APIC")[0].data
		fb = open(context.chat_data['audio'].split('.')[0] + '.png', 'wb')
		fb.write(cover)
		fb.close()
		thumb = multipart.to_bytes(open(context.chat_data['audio'].split('.')[0] + '.png', 'rb'))
	except Exception as e:
		thumb = ''
	context.bot.send_audio(update.callback_query.message.chat_id, audio=open(context.chat_data['audio'], 'rb'), thumb=thumb)
	return ConversationHandler.END

def metatag(update, context):
	answers = getUserLang(update)['metatag_answers'] 
	tp = int(update.callback_query.data.split('|')[1])
	context.bot.send_chat_action(update.callback_query.message.chat.id, 'typing')
	context.bot.send_message(update.callback_query.message.chat_id, answers[tp])
	update.callback_query.answer()
	return 1 + tp

def convert(_, context):
	if context.chat_data['ext'] != '.m4a':
		return
	wav_audio = AudioSegment.from_file(context.chat_data['audio'], format=context.chat_data['ext'][1:])
	data = get_m4a_data(context.chat_data['audio'])
	context.chat_data['audio'] = context.chat_data['audio'].split('.')[0] + ".mp3"
	context.chat_data['ext'] = '.mp3'
	wav_audio.export(context.chat_data['audio'], format="mp3")
	if data:
		d = songObject(data['©nam'], data['©ART'][0].split(', '), False)
	try:
		tags = ID3(context.chat_data['audio'])
	except ID3.ID3NoHeaderError:
		tags = ID3()
		tags.save(context.chat_data['audio'])
	set_id3_data(context.chat_data['audio'], d)
	if data and data['covr']:
		cover = data['covr'][0]
		audioFile = ID3(context.chat_data['audio'])
		audioFile['APIC'] = AlbumCover(
			encoding=3,
			mime='image/jpeg',
			type=3,
			desc='Cover',
			data=cover
		)
		audioFile.save(v2_version=3)

def auto(update, context):
	context.bot.send_chat_action(update.callback_query.message.chat.id, 'typing')
	language_dict = getUserLang(update)
	if not context.chat_data['audio_title'] or not ' - ' in context.chat_data['audio_title']:
		context.bot.send_message(update.callback_query.message.chat_id, language_dict['fra'])
		return CHOOSING
	if len(context.chat_data['audio_title'].split(' - ')) < 2:
		return
	performer, title = context.chat_data['audio_title'].split(' - ', 1)
	data = songObject(title, [performer], False)
	set_id3_data(context.chat_data['audio'], data)
	lang_artist, lang_title, _ = language_dict['artTitle']
	context.bot.send_message(update.callback_query.message.chat_id, f'{lang_artist}: {performer}\n{lang_title}: {title}', reply_markup=createKeyboard(language_dict))
	update.callback_query.answer()
	return CHOOSING

def getAlbumArt(update, context):
	context.bot.send_chat_action(update.callback_query.message.chat.id, 'upload_photo')
	audioFile = ID3(context.chat_data['audio'])
	try:
		cover = audioFile.getall("APIC")[0].data
		fb = open(context.chat_data['audio'].split('.')[0] + '.png', 'wb')
		fb.write(cover)
		fb.close()
		context.bot.send_photo(update.callback_query.message.chat_id, photo=open(context.chat_data['audio'].split('.')[0] + '.png', 'rb'))
	except Exception as e:
		context.bot.send_message(update.callback_query.message.chat_id, getUserLang(update)['ugc'])
	update.callback_query.answer()
	return CHOOSING


def change_name(update, context):
	context.bot.send_chat_action(update.message.chat.id, 'typing')
	set_id3_data(context.chat_data['audio'], songObject(update.message.text, False, False))
	language_dict = getUserLang(update)
	context.bot.send_message(update.message.chat_id, language_dict['success'], reply_markup=createKeyboard(language_dict))
	return CHOOSING

def change_artist(update, context):
	context.bot.send_chat_action(update.message.chat.id, 'typing')
	set_id3_data(context.chat_data['audio'], songObject(False, update.message.text.split(', '), False))
	language_dict = getUserLang(update)
	context.bot.send_message(update.message.chat_id, language_dict['success'], reply_markup=createKeyboard(language_dict))
	return CHOOSING

def change_cover(update, context):
	context.bot.send_chat_action(update.message.chat.id, 'typing')
	photo = update.message.photo[-1].get_file()
	set_id3_data(context.chat_data['audio'], songObject(False, False, photo.file_path))
	language_dict = getUserLang(update)
	context.bot.send_message(update.message.chat_id, language_dict['success'], reply_markup=createKeyboard(language_dict))
	return CHOOSING

def cut_audio(update, context):
	time = update.message.text.split('-')
	startTime, endTime = time if len(time) > 1 else ('0:0', update.message.text)
	language_dict = getUserLang(update)
	if startTime == -1 or endTime == -1:
		context.bot.send_message(update.message.chat_id, language_dict['sww'])
		return CHOOSING
	startTime = getMilSec(startTime)
	endTime = getMilSec(endTime)
	audioFile = ID3(context.chat_data['audio'])
	try:
		cover = audioFile.getall("APIC")[0].data
	except:
		cover = ''
	context.bot.send_chat_action(update.message.chat.id, 'typing')
	song = AudioSegment.from_mp3(context.chat_data['audio'])
	extract = song[startTime:endTime]
	ext = context.chat_data['ext']

	data = get_mp3_data(context.chat_data['audio'])

	file_name = context.chat_data['audio'].split('.')[0]
	context.chat_data['audio'] = file_name+'-extract' + ext
	extract.export( file_name+'-extract' + ext, format=ext[1:])

	set_id3_data(context.chat_data['audio'], songObject(data['title'], data['artist'], False))

	audioFile = ID3(context.chat_data['audio'])
	audioFile['APIC'] = AlbumCover(
		encoding=3,
		mime='image/jpeg',
		type=3,
		desc='Cover',
		data=cover
	)
	audioFile.save(v2_version=3)
	context.bot.send_message(update.message.chat_id, language_dict['success'], reply_markup=createKeyboard(language_dict))
	return CHOOSING