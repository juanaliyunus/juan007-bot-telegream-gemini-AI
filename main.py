import telebot

bot = telebot.TeleBot("7785849507:AAFyRtjDHj-sQZem3Xgd4pA___ZJ_m22jQA", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
 
bot.infinity_polling()