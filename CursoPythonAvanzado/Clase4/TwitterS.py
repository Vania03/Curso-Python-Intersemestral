#############
#Ejemplo TwitterSerach
############
from TwitterSearch import *

try:
	tso=TwitterSearchOrder()
	tso.set_keywords(["Python","Linux"])
	tso.set_language("es")
	tso.set_include_entities(False)

	ts=TwitterSearch(
		consumer_key="EtxZ5CJzvZU4gdjqZ0eZbuN1D",
		consumer_secret="a0F6HyFynhsGmGnL8v1trU4blISbSpmzvdqurSq6f4a1MyzIlx",
		access_token= "879726642159001600-z22X8aFFDJsY0nveIHJixZmb7LrlrvH",
		access_token_secret="i7wdpRZOO5z5dH88rcsboPMAv8hPZtIB7aV10GM8V5fnV"
		)
	for tweet in ts.search_tweets_iterable(tso):
		print("@%s twitteo: %s "%(tweet["user"]["screen_name"],tweet["text"]))

except TwitterSearchException as tse:
	print("Hubo un error: ",tse)