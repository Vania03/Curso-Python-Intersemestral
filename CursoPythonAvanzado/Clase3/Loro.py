##########
# El bot repite todo lo que le envias
########


import telebot

TOKEN='437607858:AAGrDaCkqpnrYAfzZ3Lq1ujNPoXEHKQq2Ig'
vanijorBot= telebot.TeleBot(TOKEN)
chat_id=345201307

def listener (mensajes):
	for m in mensajes:
		chat_id=m.chat.id
		if m.content_type=='text':
			text=m.text
			vanijorBot.send_message(chat_id,"Soy un loro, Soy un loroBot!")
			vanijorBot.send_message(chat_id,text)

vanijorBot.set_update_listener(listener)

vanijorBot.polling()
