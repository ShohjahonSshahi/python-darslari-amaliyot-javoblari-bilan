from transliterate import to_cyrillic, to_latin
import telebot
TOKEN = '6654569273:AAGBYP2EpfDsrZO_tKhSKEUfNFvQgGYI7Iw'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	javob = "Assalomu alaykum, Xo'sh kelibsiz!"
	javob += "\nLotin yoki Kirilda yozilgan birorta matn kiriting:"
	bot.reply_to(message, javob)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
	msg = message.text
	if msg.isascii():
		javob = to_cyrillic(msg)
	else:
		javob = to_latin(msg) 
	bot.reply_to(message, javob)

bot.polling()

















#matn = input("Matn kiriting: ")
#if matn.isascii():
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))