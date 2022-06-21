import re
import telebot
import wikipedia

wikipedia.set_lang('ru')
with open('Project_MyWIKIbot_token.txt', 'r') as token:
    bot = telebot.TeleBot(token.read())


def get_wiki_information(text):
    """Функция производит поиск термина на Wikipedia и подготовку текста для вывода пользователю."""

    try:
        result_of_search = wikipedia.search(text)
        page_from_wiki = wikipedia.page(result_of_search[0])
        text_from_wiki = page_from_wiki.content[:500]
        wiki_message = text_from_wiki.split('.')[:-1]
        wiki_text_result = ''
        for words in wiki_message:
            if '==' not in words:
                wiki_text_result = wiki_text_result + words + '.'
            else:
                break
        wiki_text_result = re.sub(r"\([^()]*\)", '', wiki_text_result)
        return f' Вот что мне удалось найти на Wikipedia:\n\n{wiki_text_result}'
    except Exception:
        return 'Ничего не могу найти по Вашему запросу. Возможно Вам нужно найти что-то еще?'


@bot.message_handler(commands=['start'])
def start(start_message):
    """Обработка команды /start."""

    bot.send_message(start_message.chat.id,
                     'Привет, это wiki-bot!\nОтправьте мне интересующее слово, '
                     'и я попробую найти информацию по нему на Wikipedia')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    """Получение и обработка сообщения от пользователя."""

    bot.send_message(message.chat.id, get_wiki_information(message.text))


bot.polling(none_stop=True, interval=0)  # Запуск бота.
