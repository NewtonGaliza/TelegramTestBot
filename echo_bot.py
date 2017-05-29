import telebot

bot = telebot.TeleBot(<your_token_here>)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome back!")

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
