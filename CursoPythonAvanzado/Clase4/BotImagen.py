import tweepy
import random	
from LlaveTw.py import *

from io import BytesIO
import resquests
from PIL import Image
from PIL import ImageFile

auth=tweepy.OAuthHandler(tokens["consumer_key"],tokens["consumer_secret"])
auth.set_access_token(tokens["access_token"],tokens["access_token_secret"])
api=tweepy.API(auth)
def imagenNueva(url,username,status_id):
	filename='temp.png'
	request=request.get(url,stream=True)

	if request.status_code==200:
		#Leer para descargarla en bytes y la retronamos a PIL
		i=Imagen.open(BytesIO(request.content))
		i.save(filename)
		cuadros(filename)
		api.update_with_media('nueva.png',status='@{0}'.format(username),in_reply_to_status_id=status)
	else:
		print("No se pudo descargar la imagen :( ")

def cuadros(filename):
	bloques=64

	img=Imagen.open(filename)
	width,height=img.size

	xblock=width  // bloques
	yblock=height // bloques

	mapaBloques=[(xb*bloques,yb*bloques,(xb+1)*bloques,(yb+1)*bloques)
				for xb in (xblock) for yb in range(yblock)]

	shuffle=list(mapaBloques)
	random.shuffle(shuffle)
	result=Imagen.new(img.mode,(width,height))
	for box,sbox in zip(mapaBloques,shuffle):
		crop=img.crop(sbox)
		result.paste(crop,box)
	result.save('nueva.png')
#Clase inherente tweepy

class BotsStreamer(tweepy.StreamListener):
	def on_statu0s(self,status):
		username=status.user.screen_name
		status_id=status.status_id

#entities es darnos informacion de la estructura del twwet incluyendo hashtags, menciones, palabras
		if 'media' in status.entities:
			for image in status.entities['media']:
				imagenNueva(imagen['media_url'],username,status_id)

#bot streaming
miBOt=BotsStreamer
stream=tweepy.stream(auth,miBOt)
stream.filter(track=['@VaniaMartnez4'])