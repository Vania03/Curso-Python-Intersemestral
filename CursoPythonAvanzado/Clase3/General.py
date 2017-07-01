###################
#API TELEGRAM PARA BOTS
#######################

import telebot
#Asignamos el token generado por el botfather a una variable
TOKEN='437607858:AAGrDaCkqpnrYAfzZ3Lq1ujNPoXEHKQq2Ig'

#Crear un objeto de la clase telebot y con el metodo TeleBot() le pasamos el token
#Nombre del Telebot    #Instancia del bot
vanijorBot= telebot.TeleBot(TOKEN)

############# Con este metodo vemos si funciona la API
vanijorBot.get_me()
print(vanijorBot.get_me())

#######Enviar mensaje
mensaje="Yesiiiiii, te querooooo muchooooo"
chat_id=345201307
#While True:
"""vanijorBot.send_message(chat_id,mensaje)
##########enviar imagenes
foto= open('China.jpg','rb')
vanijorBot.send_photo(chat_id,foto)

######### Enviar PDF
doc=open('HA.pdf','rb')
vanijorBot.send_document(chat_id,doc)


########## Enviar video
video=open('Enya.mp4','rb')
vanijorBot.send_video(chat_id,video)

###### Enviar audio

audio=open('EnyaOnly.mp3','rb')
vanijorBot.send_audio(chat_id,audio)

############# Enviar ubicacion
latitud=19.331493
longitud= -99.185065
vanijorBot.send_location(chat_id,latitud,longitud)


#######reenviar mensaje
to_chat_id=
while True: 
	mensaje_id='Hola!!!!!' 

##########Obtener actualizaciones
vanijorBot.get_update() 

####################Crear teclado de acciones

from telebot import types

markup=types.ReplyKeyboardMarkup(row_width=2)

item1=types.KeyboardButton('TE AMOOOOOOOOOOOOOOOOOO')
item2=types.KeyboardButton('GORUU')
item3=types.KeyboardButton('<3')
markup.add(item1,item2,item3)

vanijorBot.send_message(chat_id,'Elige una letra: ',reply_markup=markup)"""


