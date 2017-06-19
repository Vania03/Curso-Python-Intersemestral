def norma(slef):
		acum=0
		for n in range(self.dimension):
			acum+=(self[n])**2
		return acum**(1/2)

def normaMejorada(self):
	return reduce(lambda a,b: a+b,list(map(lambda x:x**2, self.elementos)))**(1/2)

norma()

normaMejorada()