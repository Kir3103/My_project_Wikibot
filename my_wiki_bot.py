import re
import telebot
import wikipedia

wikipedia.set_lang('ru')
bot = telebot.TeleBot('5501860572:AAG2Um4f1T1Zdhg50p_ZfQ_EJRiQGt73wTU')


def get_wiki_information(text):
    """Функция производит чистку текста из статьи на Wikipedia"""
    try:
        result_of_search = wikipedia.search(text)
        page_from_wiki = wikipedia.page(result_of_search[0])
        text_from_wiki = page_from_wiki.content[:1000]
        wiki_message = text_from_wiki.split('.')[:-1]
        wiki_text_result = ''
        for words in wiki_message:
            if not ('==' in words):
                if len((words.strip())) > 3:
                    wiki_text_result = wiki_text_result + words + '.'
            else:
                break
        wiki_text_result = re.sub('\([^()]*\)', '', wiki_text_result)
        return f' Вот что мне удалось найти на Wikipedia:\n\n{wiki_text_result}'
    except Exception:
        return 'Ничего не могу найти по Вашему запросу. Возможно Вам нужно найти что-то еще?'


@bot.message_handler(commands=['start'])
def start(start_message):
    bot.send_message(start_message.chat.id,
                     'Привет, это wiki-bot 👨🏻‍💻\nОтправьте мне интересующее слово, '
                     'и я попробую найти информацию по нему на Wikipedia')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, get_wiki_information(message.text))


bot.polling(none_stop=True, interval=0)
