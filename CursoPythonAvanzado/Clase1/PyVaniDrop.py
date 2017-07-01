############
#API DROPBOX
############
import dropbox
class DBManager(object):
	"""Una clase envolvente para el API de DropBox

	Constructor sirve para llamar al objeto y crear sus atributos"""
	def __init__(self,key=None):
		self.key=key
		self.api=""
		self.connect()

	def connect(self): #Metodo
		"""Metodo para conectarnos a la API de DropBox"""
		self.api=dropbox.Dropbox(self.key)
		print("Conexion exitosa")
		print("Bienvenida mi amor"+self.getAccountInfo().name.display_name)

	def getAccountInfo(self):#Metodo
		return self.api.users_get_current_account()


	def listDir(self,directory):
		if not directory:
			print("No es un directorio")
		else:
			for subdir in self.api.files_list_folder("/"+directory).entries:
				print("-> ",subdir.name)

	def upload(self,file):
		with open(file,"rb") as f:
			self.api.files_upload(f.read(),"/"+file)

	def dowload(self,file):
		self.api.files_download_to_file(file,"/"+file)

if __name__ == '__main__':
	dM=DBManager("Z_RpTD0R75AAAAAAAAAACKG6O3WFXkn3bbGR1CdB9AfrXvBKIj-I6dZ5XR7wRwyw")	
	#dM=DBmanager(open("llave.txt").read())	
	dM.listDir("/")
	dM.upload("FCA.png")
	dM.dowload("algo.pdf")


