import telebot

token = '6444948282:AAFEjZuIskPEQuvy-d0sM7lm9ut49Wf0szY'
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def send_echo(message):
    what = input( "Что делаем? (+, -): " )

bot.infinity_poling()
