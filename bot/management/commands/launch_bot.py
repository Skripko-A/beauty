from django.core.management.base import BaseCommand
from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater, MessageHandler, Filters, CallbackQueryHandler

from bot.bot import start, show_main_menu, show_my_appointments, show_salons, show_staffs, show_services, \
    show_administration_contacts, cancel_booking, button, handle_contact, check_administrator, conversation_handler


class Command(BaseCommand):
    help = 'Starts the Telegram bot'

    def handle(self, *args, **kwargs):

        updater = Updater(token='7138163431:AAGgcLN-qfvHv7DVnCRMfg7KRiZ_488gTwI', use_context=True, request_kwargs={'read_timeout': 10, 'connect_timeout': 5})
        dp = updater.dispatcher
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(MessageHandler(Filters.text("Записаться"), show_main_menu))
        dp.add_handler(MessageHandler(Filters.text("Мои записи"), show_my_appointments))
        dp.add_handler(MessageHandler(Filters.text("Салоны"), show_salons))
        dp.add_handler(MessageHandler(Filters.text("Мастера"), show_staffs))
        dp.add_handler(MessageHandler(Filters.text("Услуги"), show_services))
        dp.add_handler(MessageHandler(Filters.text("Администратор"), show_administration_contacts))
        dp.add_handler(CallbackQueryHandler(cancel_booking, pattern='^cancel_booking$'))
        dp.add_handler(CallbackQueryHandler(button))

        dp.add_handler(CallbackQueryHandler(cancel_booking, pattern='^cancel_booking$'))
        dp.add_handler(MessageHandler(Filters.contact, handle_contact))
        dp.add_handler(MessageHandler(Filters.regex(r'^/admin:\w+'), check_administrator))
        # dp.add_handler(CommandHandler("remind_tomorrow", remind_tomorrow_command))
        dp.add_handler(conversation_handler)

        updater.start_polling()
        updater.idle()
