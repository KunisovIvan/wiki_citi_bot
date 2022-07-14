import telebot

from tg_bot.models import Locality
from tg_bot.utils import parse_wiki_page

bot = telebot.TeleBot('5453337195:AAETWu89Wm-FOP3IxYRWLXOLL5BOylFJCPE')


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(
        m.chat.id, 'Напишите название города полностью или его часть.\n'
                   'Для того, чтобы обновить информацию, введите "/update"'
    )


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == '/update':
        parse_wiki_page()
        bot.send_message(
            message.chat.id, 'Информация о населенных пунктах обновлена'
        )
    else:
        locality = Locality.objects.filter(title__contains=message.text)
        if not locality:
            bot.send_message(message.chat.id, 'Таких городов нету в базе')
        elif locality.count() > 1:
            bot.send_message(
                message.chat.id, ',\n'.join([l.title for l in locality])
            )
        else:
            bot.send_message(
                message.chat.id,
                f'Наименование: {locality[0].title}, \n'
                f'Население: {locality[0].population} человек, \n'
                f'Ссылка на википедию: \n'
                f'{locality[0].href}'
            )

