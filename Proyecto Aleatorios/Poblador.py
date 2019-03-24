#!python3
from Restriccion import Restriccion
from Aleatorio import Aleatorio

class Poblador:
	ceros = []
	restricciones = []
	aleatorios = []
	zExpresion = ""
	constantes = []
	z = 0

	def __init__(self, restricciones, z, limitesSup, limitesInf, iteracion):
		self.valorRestricciones = False
		self.ceros = []
		alea = Aleatorio(restricciones, limitesSup, limitesInf, iteracion)
		self.aleatorios = alea.getAleatorio()
		#print("Aleatorios en pesona")
		#print(self.aleatorios)
		for x in range(0, len(self.aleatorios)):
			self.ceros.append(0)

		self.zExpresion = z
		self.restricciones = []

		for rest in restricciones:
			self.restricciones.append(Restriccion(rest, self.aleatorios))
		self.evaluar()
		self.calcularZ()

	def getAleatorios(self):
		return self.aleatorios

	def evaluar(self):
		aux = 1

		for rest in self.restricciones:
			aux = aux * rest.evaluar()
		#print("aux="+str(aux))
		if(aux == 1):
			self.valorRestricciones = True

	def calcularZ(self):
		aux = ""

		for letra in self.zExpresion:
			if(letra == "." or letra.isdigit() or letra == "-"):
				aux = aux + letra
			elif(aux != ""):
				self.constantes.append(aux)
				aux = ""

		for num, ale in zip(self.constantes, self.aleatorios):
			self.z = self.z + float(num) * float(ale)
		
	def getZ(self):
		if(self.valorRestricciones):
			return self.z
		else:
			return "Incumplimiento de restricciones"

	def getCeros(self):
		return self.ceros