from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultAudio, InputMediaAudio, Audio, Update)
from deezer import deezer 
from download import *
from lang import getUserLang


def chosenInline(update: Update, context) -> None:
    '''
        Add selected song to queue from inline query 
    '''
    query = update.chosen_inline_result.query
    result_id = int(update.chosen_inline_result.result_id)
    search = deezer.search_tracks(query)
    link = search[result_id]['link']
    inline = update['chosen_inline_result']['inline_message_id']
    if not 'que_pos' in context.bot_data:
        context.bot_data['que_pos'] = [0,0,0,0]
        context.bot_data['que_work'] = [False, False, False, False]
    pss = context.bot_data['que_pos'][3] + qvia.qsize()
    pss = pss+1 if context.bot_data['que_work'][3] == True else pss
    ket = []
    ket.append([InlineKeyboardButton(getUserLang(update)['pos_current'], callback_data=f'position|3|{pss}')])
    reply_markup = InlineKeyboardMarkup(ket)
    context.bot.edit_message_media(media=InputMediaAudio(Audio(file_id='CQACAgIAAxkBAAIRQmMF0EI_zr_omoAJO7R7nt1i9KKCAALfHAACODcpSAqqtYKqfRT_KQQ', 
        file_unique_id='AgAD3xwAAjg3KUg', 
        duration='173'),
        caption=f"<a href='{link}'>{search[result_id]['title']} — {search[result_id]['artist']['name']}</a>",
        parse_mode="HTML"),
        inline_message_id=inline,
        reply_markup=reply_markup
        )
    context.bot.send_message('-596369085', link)
    qvia.put([link, update, context, inline])



def inlinequery(update: Update, context) -> None:
    """Handle the inline query."""
    query = update.inline_query.query
    if query == "":
        return
    search = deezer.search_tracks(query)
    if not search:
        return
    results = []
    for i in range(len(search)):
        ket = []
        ket.append([InlineKeyboardButton(getUserLang(update)['pos_current'], callback_data='hfih|0')])
        reply_markup = InlineKeyboardMarkup(ket)
        results.append(InlineQueryResultAudio(
            id=str(i),
            title=search[i]['title'],
            performer=search[i]['artist']['name'],
            audio_url=search[i]['preview'],
            audio_duration=search[i]['duration'],
            reply_markup=reply_markup
            ))
    update.inline_query.answer(results)