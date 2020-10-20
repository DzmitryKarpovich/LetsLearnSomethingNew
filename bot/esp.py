import telebot
#import pyowm

#owm = pyowm.OWM('c1341c1ae2dc777c567c862bd4b17d15')
bot = telebot.TeleBot("1230763312:AAGMtf6iWr27cu2iwBZTtsDzqLu3PjOrGhI")
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Привет. Я тестовый бот. Похоже, тебя втянули в какое-то обучение. Напиши что-нибудь ниже." + "\n\n" + "Type something below:")

#@bot.message_handler(commands=['weather'])
#def send_welcome2(message):
#	bot.reply_to(message, "Type a city to see a weather:")

@bot.message_handler(content_types=['text'])
def send_weather(message):
	try:
		#observation = owm.weather_manager()
		#text = str(message.json['text'])
		#print('\n' + text)
		#w = observation.weather_at_place(text) 
		#temperatura = w.weather.temperature('celsius')['temp']
		#degree_sign= u'\N{DEGREE SIGN}'
		#print(str(round(temperatura)) + degree_sign)
		#print('----------------------------' + '\n')
		answer = "Your text is: " +'\n' + message.text + '\n'
		#answer += w.weather.detailed_status + '\n'
		#answer += "Temperature is " + str( round(temperatura, 0) ) + degree_sign + '\n\n'
		#if temperatura < 10:
		#	answer += 'It is terribly cold. Hold on there!'+ '\n'
		#	answer += 'Put on a hat !!!'
		#elif temperatura < 20:
		#	answer+= 'It\'s cold, but bearable.'
		#else:
		#	answer += 'The heat is there, I envy.'
	except:
		answer = 'Are you kidding?' + '\n'
		answer += 'I\'ve catched an exception!'+ '\n\n'
		answer += 'Try again!'+ '\n'
	#	answer += message.text+ '\n'
	bot.send_message(message.chat.id, answer)
bot.polling( none_stop = True )
