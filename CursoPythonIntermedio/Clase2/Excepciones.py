###
#Excpeciones
#Una excepcion es un tipo de error que ocurre durante la ejecucion
#Estructura try-except
#try: ->Aqui dentro va el codigo que nos puede ocacionar una excepcion
#except ->Aqui va la excepcion, nos puede enviar un mensaje
#else: -> Si no ocurre ninguna excepcion, entramos al else
#finally: -> Haya o no haya excepcion 
try:#Aqui voy a meter mi codigo que me puede lanzar una excepcion 
	numero=int(input("Ingresa un numero, lo voy a dividir: "))
	print(10/numero)
except ZeroDivisionError:
	print("Error, no puedes dividir entre cero. Esta indefinido")
except ValueError:#Aqui vamos a poner las excepciones que se van a lanzar
	print("Estamos solicitando un entero, Ingresa un entero")
else:#Sino cacho ninguna excepcion me voy al else
	print("Todo esta bien, no se levanto ninguna excepcion")
#Si quiero que algo se ejecute haya o no haya excepcion
finally:
	print("Finally Se ejecuta siempre, haya o no haya alguna excepcion")