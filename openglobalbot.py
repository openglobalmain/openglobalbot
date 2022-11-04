import telebot
token='5554332230:AAFnh_HngpQesOHui_kEZGSjJ0Vcl-hPj6Y'
bot=telebot.Telebot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()
