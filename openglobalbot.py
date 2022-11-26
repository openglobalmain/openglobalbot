import telebot
OpenBot = telebot.TeleBot('5554332230:AAFnh_HngpQesOHui_kEZGSjJ0Vcl-hPj6Y', parse_mode = None)

@OpenBot.message_handler(commands = ['start'])
def start(message):
    mess =f'Привет, <b>{message.from_user.first_name} </b> '
    OpenBot.send_message(message.chat.id, mess, parse_mode='html')
OpenBot.polling(non_stop=True)