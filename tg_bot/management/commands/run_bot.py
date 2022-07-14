import logging

from django.core.management.base import BaseCommand

from tg_bot.tg_bot import bot

log = logging.getLogger(__name__)
log.setLevel('DEBUG')


class Command(BaseCommand):
    help = 'Запускает телеграмм бота'

    def handle(self, *args, **options):
        log.info('---------------------start bot----------------------')
        bot.polling(none_stop=True, interval=0)
        log.info('----------------------stop bot------------------------')
