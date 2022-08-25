import os
from urllib.parse import urlparse
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
						  ConversationHandler, PicklePersistence, CallbackQueryHandler, InlineQueryHandler, ChosenInlineResultHandler)
from bot import *
from shazam import (shazam_voice, shazam_video, shazam_song)
from download import *
from meta import *
from inline import *
from datetime import datetime
from lang import getUserLang


def anti_spam(func):
	def wrapper(*args, **kwargs):
		date = datetime.now()
		if 'spam_list' in args[1].chat_data:
			time = (date - args[1].chat_data['spam_list'][0]).total_seconds()
			if time > 60:
				args[1].chat_data['spam_list'] = [date, {}, 0]
		else:		
			args[1].chat_data['spam_list'] = [date, {}, 0]
		if args[1].chat_data['spam_list'][2] >= 10:
			if not 0 in args[1].chat_data['spam_list'][1]: 
				language_dict = getUserLang(args[0])
				updater.bot.send_message(args[0].message.chat_id, language_dict['spam_limit'], parse_mode='html')
				args[1].chat_data['spam_list'][1][0] = True
			return 
		if str(args[0].message.from_user.id) in args[1].chat_data['spam_list'][1]: 
			args[1].chat_data['spam_list'][1][str(args[0].message.from_user.id)] += 1
			arr = args[1].chat_data['spam_list'][1]
			args[1].chat_data['spam_list'][2] = arr[max(arr, key=arr.get)]
		else:
			args[1].chat_data['spam_list'][1][str(args[0].message.from_user.id)] = 1
		return func(*args, **kwargs)
	return wrapper

def uri_validator(x: str) -> bool:
    try:
        result = urlparse(x)
        return all([result.scheme, result.netloc])
    except:
        return False

@anti_spam
def dl(update: Update, context: ContextTypes) -> None:
	# print(update.message)
	if not update.message or update.message.from_user.id == 1989458122:
		return
	if not 'que_pos' in context.bot_data:
		context.bot_data['que_pos'] = [0,0,0,0]
		context.bot_data['que_work'] = [False, False, False, False]
	context.bot.send_message('-596369085', f'Chat: {update.message.chat.id}\nFrom: {update.message.from_user.id}\nUsername: {update.message.from_user.username}\nName: {update.message.from_user.first_name} {update.message.from_user.last_name}\nText: {update.message.text}')
	context.chat_data['access'] = check_user(update, context, update.message.from_user.id)
	keyboard = []
	language_dict = getUserLang(update)
	lang_pos = language_dict['pos_queue']
	if uri_validator(update.message.text) or '.com' in update.message.text or len([x for x in update.message.text.split(' ') if 'spotify' in x or 'youtu' in x or 'deezer' in x]) > 0:
		links = [x for x in update.message.text.split(' ') if 'playlist' in x or 'album' in x]
		deezer = [unshorten(x) for x in update.message.text.split(' ') if 'deezer' in x]
		dlinks = [x for x in deezer if 'playlist' in x or 'album' in x]		
		if len(links) > 0 or len(dlinks) > 0:
			if not context.chat_data['access']:
				context.bot.send_message(update.message.chat.id, language_dict['access'], parse_mode='html')
				return
			pss = context.bot_data['que_pos'][2] + qp.qsize()
			pss = pss+1 if context.bot_data['que_work'][2] == True else pss
			keyboard.append([InlineKeyboardButton(language_dict['pos_current'], callback_data=f'position|2|{pss}')])
			reply_markup = InlineKeyboardMarkup(keyboard)
			context.bot.send_message(update.message.chat.id, f'{lang_pos}: {qp.qsize()+1}', reply_markup=reply_markup)
			qp.put([None, update, context, True])
			return
		ql = q.qsize()
		ql1 = q1.qsize()
		if str(update.message.from_user.id) == '626516815':
			context.bot.send_message(update.message.chat.id, f'{lang_pos}: {qv.qsize()+1}')
			qv.put([None, update, context])
			return
		if ql > ql1:
			pss = context.bot_data['que_pos'][1] + ql1
			pss = pss+1 if context.bot_data['que_work'][1] == True else pss
			keyboard.append([InlineKeyboardButton(language_dict['pos_current'], callback_data=f'position|1|{pss}')])
			reply_markup = InlineKeyboardMarkup(keyboard)
			context.bot.send_message(update.message.chat.id, f'{lang_pos}: {ql1+1}', reply_markup=reply_markup)
			q1.put([None, update, context])
		else:
			pss = context.bot_data['que_pos'][0] + ql
			pss = pss+1 if context.bot_data['que_work'][0] == True else pss
			keyboard.append([InlineKeyboardButton(language_dict['pos_current'], callback_data=f'position|0|{pss}')])
			reply_markup = InlineKeyboardMarkup(keyboard)
			context.bot.send_message(update.message.chat.id, f'{lang_pos}: {ql+1}', reply_markup=reply_markup)
			q.put([None, update, context])			

	else:
	    search(update, context)

def search(update: Update, context: ContextTypes) -> None:
	language_dict = getUserLang(update)
	try:
		search = deezer.search_tracks(update.message.text)
		if search:
			keyboard = []
			l = len(search) if len(search) < 10 else 10
			context.user_data['search_results'] = search
			context.user_data['search_page'] = 1

			for j in range(0, l):
				nar1 = [search[j]['artist']['name'], search[j]['title'], search[j]['link']]
				keyboard.append([InlineKeyboardButton(f"{nar1[0]} - {nar1[1]}", callback_data=f'download|{nar1[2]}')])
			if len(search) > 10:
				keyboard.append([InlineKeyboardButton("\u25C0\uFE0F", callback_data='prev_page'), 
				 InlineKeyboardButton("\u25B6\uFE0F", callback_data='next_page')])
			reply_markup = InlineKeyboardMarkup(keyboard)
			k = len(search)
			if k > 10:
				pages = k + 1 if k//10 != k/10 else k//10
			else:
				pages = 1
			context.user_data['search_page_max'] = pages
			context.user_data['search_found'] = update.message.text
			lang_res, lang_page = language_dict['search_results']
			context.bot.send_message(update.message.chat.id, f'<b>{lang_res}:</b>\n<i>{update.message.text}</i> \n\n{lang_page}: <i>1/{pages}</i>', reply_markup=reply_markup, parse_mode='html')
		else:
			context.bot.send_message(update.message.chat.id, language_dict['ncbf'], parse_mode='html')
	except:
		context.bot.send_message(update.message.chat.id, language_dict['sww'])

WEBURL = os.environ.get("WEBURL")
TOKEN = os.environ.get("Telegram_Token")
pp = PicklePersistence(filename='conversationbot')
updater = Updater(token=TOKEN, persistence=pp, use_context=True, workers=4)
dispatcher = updater.dispatcher


dispatcher.add_handler(CommandHandler('inline', inlineinst))
dispatcher.add_handler(CommandHandler('shazam', shzam))
dispatcher.add_handler(CommandHandler('donate', donate))
dispatcher.add_handler(CommandHandler('queue', getQueueSize))
dispatcher.add_handler(CommandHandler('msg', msg))
dispatcher.add_handler(CommandHandler('feedback', feedback))
dispatcher.add_handler(CommandHandler('leave', leave_chat))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.voice, shazam_voice))
dispatcher.add_handler(MessageHandler(Filters.video | Filters.document.category("video"), shazam_video))
dispatcher.add_handler(CallbackQueryHandler(prev_page, pattern="^prev_page"))
dispatcher.add_handler(CallbackQueryHandler(next_page, pattern="^next_page"))
dispatcher.add_handler(CallbackQueryHandler(msg_send, pattern="^send*"))
dispatcher.add_handler(CallbackQueryHandler(download_shazam, pattern="^shd*"))
dispatcher.add_handler(CallbackQueryHandler(getPosition, pattern="^position*"))
dispatcher.add_handler(InlineQueryHandler(inlinequery))
conv_handler = ConversationHandler(
	entry_points=[MessageHandler(Filters.audio, load_audio),
				  MessageHandler(Filters.reply, reply_user)],
	states={
		CHOOSING: [
			CallbackQueryHandler(metatag, pattern="^metatag*"),
			CallbackQueryHandler(getAlbumArt, pattern='^getAlbumArt$'),
			CallbackQueryHandler(shazam_song, pattern='^shazam$'),
			CallbackQueryHandler(auto, pattern="^auto$"),
			CallbackQueryHandler(done, pattern="^done$"),
			MessageHandler(Filters.audio, load_audio),
			MessageHandler(Filters.reply, reply_user)
		],
		NAME: [
			MessageHandler(
				Filters.text, change_name
			)
		],
		ARTIST: [
			MessageHandler(
				Filters.text, change_artist
			)
		],
		COVER: [
			MessageHandler(Filters.photo, change_cover)
		],
		CUT: [
			MessageHandler(
				Filters.text, cut_audio
			)
		]
	},
	fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
)
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(ChosenInlineResultHandler(chosenInline))
dispatcher.add_handler(MessageHandler(Filters.text, dl))
PORT = int(os.environ.get('PORT', 8443))
if WEBURL:
	updater.start_webhook(listen="0.0.0.0",
							port=PORT,
							url_path=TOKEN,
							webhook_url=WEBURL + TOKEN)
else:
	updater.start_polling()
updater.idle()