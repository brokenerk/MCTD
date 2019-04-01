#!python3
from Restriccion import Restriccion
from Aleatorio import Aleatorio

class Poblador:
	ceros = []
	restricciones = []#lista de restricciones
	aleatorios = []#lista de aleatoros
	zExpresion = ""#Expresion algebraica de la funcikon objetivo
	constantes = []#lista de constantes
	z = 0.0 #valor de Z

	def __init__(self, restricciones, z, limitesSup, limitesInf):
		"""
		Inicalizacion de las variables
		"""
		self.valorRestricciones = False
		self.ceros.clear()
		self.aleatorios.clear()
		alea = Aleatorio(restricciones, limitesSup, limitesInf)
		self.aleatorios = alea.getAleatorio()
		for x in range(0, len(self.aleatorios)):
			self.ceros.append(0)

		self.zExpresion = z
		self.restricciones.clear()

		for rest in restricciones:
			self.restricciones.append(Restriccion(rest, self.aleatorios))
		self.evaluar()
		self.calcularZ()

	def getAleatorios(self):#Retorna los aleatorios asignados al poblador
		return self.aleatorios

	def evaluar(self):
		#Evalua si los numeros aleatorios cumplen con las restricciones
		aux = 1

		for rest in self.restricciones:
			aux = aux * rest.evaluar()
		if(aux == 1):#En caso de ser cero se debe a que alguna restriccion no se cumpio
			self.valorRestricciones = True

	def calcularZ(self):#se obtiene el valor de Z
		aux = ""
		self.z = 0.0
		self.constantes.clear()

		for letra in self.zExpresion:#Se rescatan las constantes de la expresion
			if(letra == "." or letra.isdigit() or letra == "-"):
				aux = aux + letra
			elif(aux != ""):
				self.constantes.append(aux)
				aux = ""

		for num, ale in zip(self.constantes, self.aleatorios):#se multiplican las constantes y los aleatorios para encontrar Z
			self.z = self.z + float(num) * float(ale)
		
	def getZ(self):#Retorna Z
		if(self.valorRestricciones):
			return self.z
		else:
			return "Incumplimiento de restricciones"

	def getCeros(self):
		return self.ceros