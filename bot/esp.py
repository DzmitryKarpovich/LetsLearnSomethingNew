import telebot

bot = telebot.TeleBot("1230763312:AAGMtf6iWr27cu2iwBZTtsDzqLu3PjOrGhI")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет. Я тестовый бот. Похоже, тебя втянули в какое-то обучение. Напиши что-нибудь ниже." + "\n\n" + "Type something below:")
@bot.message_handler(content_types=['text'])
def send_weather(message):
	try:
		answer = "Я уверен, что ты только что набрал на клавиатере следущий текст: " +'\n\n' + message.text + '\n'
	except:
		answer = 'Are you kidding?' + '\n'
		answer += 'I\'ve catched an exception!'+ '\n\n'
		answer += 'Try again!'+ '\n'
	bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True )
