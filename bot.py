from telegram.ext import ContextTypes
from telegram import (Update, InlineKeyboardButton, InlineKeyboardMarkup)
from lang import getUserLang
from meta import convert, createKeyboard
from download import (q, q1, qp)

def reply_user(update: Update, context: ContextTypes) -> int:
    print(update.message)
    if update.message.reply_to_message.audio:
        audio_file = update.message.reply_to_message.audio.get_file()
        ext = '.' + audio_file.file_path.split('.')[-1]
        audio_file.download(audio_file.file_id + ext)
        context.chat_data['audio_title'] = update.message.reply_to_message.audio.title
        context.chat_data['audio'] = audio_file.file_id + ext
        context.chat_data['ext'] = ext
        if ext == '.m4a':
            convert(update, context)
        context.bot.send_chat_action(update.message.chat.id, 'typing')
        language_dict = getUserLang(update)
        context.bot.send_message(update.message.chat_id, language_dict['action'], reply_markup=createKeyboard(language_dict))
        return 0

def inlineinst(update: Update, context: ContextTypes) -> None:
    '''
    Send instructions for using inline mode 
    '''
    language_dict = getUserLang(update)
    update.message.bot.forward_message('-596369085', update.message.from_user.id, update.message.message_id)
    context.bot.send_photo(update.message.chat.id, open('inline.jpg', 'rb'), caption=language_dict['inline'])

def shzam(update: Update, context: ContextTypes) -> None:
    '''
    Send instructions for using shazam 
    '''
    language_dict = getUserLang(update)
    context.bot.send_photo(update.message.chat.id, open('shazam.jpg', 'rb'), caption=language_dict['shazam'])

def donate(update: Update, context: ContextTypes) -> None:
    '''
    Send msg with requisites for the donation 
    '''
    language_dict = getUserLang(update)
    update.message.bot.forward_message('-596369085', update.message.from_user.id, update.message.message_id)
    context.bot.send_message(update.message.chat.id, language_dict['donate'], parse_mode="Markdown")

def getQueueSize(update: Update, context: ContextTypes) -> None:
    '''
    Send msg with current queues size
    '''
    context.bot.send_message(update.message.chat.id, f'Queue: {q.qsize()}\nQueue 1: {q1.qsize()}\nPlaylist queue: {qp.qsize()}')

def msg(update: Update, context: ContextTypes) -> None:
    '''
    Send msg to specific user by user_id
    '''
    if str(update.message.from_user.id) == '626516815':
        text = update.message.text.split(' ', 2)
        uid = text[1]
        ms = text[2]
        keyboard = [
            [InlineKeyboardButton("Send", callback_data=f'send|{uid}')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        context.bot.send_message(update.message.chat.id, ms, reply_markup=reply_markup)

def msg_send(update: Update, context: ContextTypes) -> None:
    '''
    Confirmation for msg to specific user
    '''
    query = update.callback_query
    if str(query.from_user['id']) == '626516815':
        rate_id = query.data.split('|')[1]
        context.bot.send_message(rate_id, query.message.text)
        context.bot.send_message(query.message.chat.id, '✅')

def feedback(update: Update, context: ContextTypes) -> None:
    language_dict = getUserLang(update)
    context.bot.send_message('-596369085', f'Chat: {update.message.chat.id}\nFrom: {update.message.from_user.id}\nUsername: {update.message.from_user.username}\nName: {update.message.from_user.first_name} {update.message.from_user.last_name}\nText: {update.message.text}')
    update.message.bot.forward_message('-596369085', update.message.from_user.id, update.message.message_id)
    context.bot.send_message(update.message.chat.id, language_dict['feedback'])

def leave_chat(update: Update, context: ContextTypes) -> None:
	if str(update.message.from_user.id) == '626516815':
		text = update.message.text.split(' ', 2)
		uid = text[1]
		context.bot.leave_chat(uid)
		context.bot.send_message(update.message.chat.id, 'Successful!')

def prev_page(update: Update, context: ContextTypes) -> None:
    query = update.callback_query
    if not 'search_page' in context.user_data or context.user_data['search_page'] == 1:
        query.answer()
        return
    context.user_data['search_page'] -= 1
    search = context.user_data['search_results']
    page, pages, found = context.user_data['search_page'], context.user_data['search_page_max'], context.user_data['search_found']
    keyboard = []
    for j in range((0+10*(page-1)), (10+10*(page-1))):
        nar1 = [search[j]['artist']['name'], search[j]['title'], search[j]['link']]
        keyboard.append([InlineKeyboardButton(f"{nar1[0]} - {nar1[1]}", callback_data=f'download|{nar1[2]}')])
    keyboard.append([InlineKeyboardButton("\u25C0\uFE0F", callback_data='prev_page'), 
        InlineKeyboardButton("\u25B6\uFE0F", callback_data='next_page')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    lang_res, lang_page = getUserLang(update)['search_results']
    text = f'<b>{lang_res}:</b>\n<i>{found}</i> \n\n{lang_page}: <i>{page}/{pages}</i>'
    query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode="html")
    query.answer()

def next_page(update: Update, context: ContextTypes) -> None:
    query = update.callback_query
    search = context.user_data['search_results']
    if context.user_data['search_page'] + 1 > len(search)/10:
        query.answer()
        return
    context.user_data['search_page'] += 1
    page, pages, found = context.user_data['search_page'], context.user_data['search_page_max'], context.user_data['search_found']
    keyboard = []
    for j in range((0+10*(page-1)), (10+10*(page-1))):
            nar1 = [search[j]['artist']['name'], search[j]['title'], search[j]['link']]
            keyboard.append([InlineKeyboardButton(f"{nar1[0]} - {nar1[1]}", callback_data=f'download|{nar1[2]}')])
    keyboard.append([InlineKeyboardButton("\u25C0\uFE0F", callback_data='prev_page'), 
            InlineKeyboardButton("\u25B6\uFE0F", callback_data='next_page')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    lang_res, lang_page = getUserLang(update)['search_results']
    text = f'<b>{lang_res}:</b>\n<i>{found}</i> \n\n{lang_page}: <i>{page}/{pages}</i>'
    query.edit_message_text(text=text, reply_markup=reply_markup, parse_mode="html")
    query.answer()

def getPosition(update: Update, context: ContextTypes) -> None:
    query = update.callback_query
    queue = int(query.data.split('|')[1])
    fpos = int(query.data.split('|')[2])
    cpos = context.bot_data['que_pos'][queue]
    pos = fpos - cpos
    language_dict = getUserLang(update)
    audio_soon = language_dict['audio_soon']
    if pos >= 0:
        query.bot.answerCallbackQuery(callback_query_id=query.id,
                                            text=f'{audio_soon}: {pos}',
                                    show_alert=True)
        return
    try:
        _ = query.inline_message_id
        query.edit_message_text(text=language_dict['sww'], reply_markup=InlineKeyboardMarkup([]), parse_mode="html")
        query.answer()
        return
    except Exception as e:
        print(e)
        pass
    query.edit_message_text(text=language_dict['downloaded'], reply_markup=InlineKeyboardMarkup([]), parse_mode="html")
    query.answer()

def start(update: Update, context: ContextTypes) -> None:
    language_dict = getUserLang(update)
    context.bot.send_message(update.message.chat.id, language_dict['hello'])