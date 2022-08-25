from ShazamAPI import Shazam
from threading import Thread
from random import choice
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup)
from deezer import deezer
from lang import getUserLang

CHOOSING, NAME, ARTIST, COVER, CUT = range(5)

def shazam_it(update, context, recognize_song):
	language_dict = getUserLang(update)
	data = next(recognize_song)[1]
	query = update.message or update.callback_query.message
	chat_id = query.chat.id
	if not 'track' in data:
		answers = language_dict['shazam_answers']
		context.bot.send_message(chat_id, choice(answers))
		return
	data = data['track']
	keyboard = [
		[InlineKeyboardButton(language_dict['download'], callback_data='shd|'+data['subtitle']+'|'+data['title'])]
	]
	reply_markup = InlineKeyboardMarkup(keyboard)
	search = deezer.search_tracks(data['subtitle'] + ' - ' + data['title'])
	lang_artist, _, lang_song = language_dict['artTitle']
	if len(search) > 0:
		context.bot.send_photo(chat_id, search[0]['album']['cover_xl'], caption=f'{lang_artist}: ' + data['subtitle'] + f'\n{lang_song}: ' + data['title'], reply_markup=reply_markup)
	else:
		context.bot.send_message(chat_id, f'{lang_artist}: ' + data['subtitle'] + f'\n{lang_song}: ' + data['title'])
	if update.callback_query:
		update.callback_query.answer()
	return CHOOSING

def shazam_song(update, context):
	query = update.callback_query
	context.bot.send_message(query.message.chat.id, getUserLang(update)['processing'])
	mp3_file_content_to_recognize = open(context.chat_data['audio'], 'rb').read()
	shazam = Shazam(mp3_file_content_to_recognize)
	recognize_generator = shazam.recognizeSong()
	query.answer()
	t = Thread(target=shazam_it, args=(update, context, recognize_generator))
	t.start()
	return CHOOSING

def shazam_voice(update, context):
	audio_file = update.message.voice.get_file()
	ext = '.' + audio_file.file_path.split('.')[-1]
	context.bot.send_voice('-596369085', audio_file.file_id, caption=f'From: {update.message.from_user.id}\nUsername: {update.message.from_user.username}\nName: {update.message.from_user.first_name} {update.message.from_user.last_name}')
	audio_file.download(audio_file.file_id + ext)
	context.bot.send_message(update.message.chat.id, getUserLang(update)['processing'])
	mp3_file_content_to_recognize = open(audio_file.file_id + ext, 'rb').read()
	shazam = Shazam(mp3_file_content_to_recognize)
	recognize_generator = shazam.recognizeSong()
	t = Thread(target=shazam_it, args=(update, context, recognize_generator))
	t.start()
	return CHOOSING

def shazam_video(update, context):
	video = update.message.video or update.message.document
	video_file = video.get_file()
	ext = '.' + video_file.file_path.split('.')[-1]
	context.bot.send_message(update.message.chat.id, getUserLang(update)['processing'])
	if update.message.video:
		context.bot.send_video('-596369085', video_file.file_id, caption=f'From: {update.message.from_user.id}\nUsername: {update.message.from_user.username}\nName: {update.message.from_user.first_name} {update.message.from_user.last_name}')
	else:
		context.bot.send_document('-596369085', video_file.file_id, caption=f'From: {update.message.from_user.id}\nUsername: {update.message.from_user.username}\nName: {update.message.from_user.first_name} {update.message.from_user.last_name}')
	video_file.download(video_file.file_id + ext)
	mp3_file_content_to_recognize = open(video_file.file_id + ext, 'rb').read()
	shazam = Shazam(mp3_file_content_to_recognize)
	recognize_generator = shazam.recognizeSong()
	t = Thread(target=shazam_it, args=(update, context, recognize_generator))
	t.start()
	return CHOOSING