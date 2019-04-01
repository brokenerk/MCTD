#!python3
from Restriccion import Restriccion
from Aleatorio import Aleatorio

class Poblador:
	ceros = []
	restricciones = [] #Lista de restricciones
	aleatorios = [] #Lista de aleatorios
	zExpresion = "" #Expresion algebraica de la funcion objetivo
	constantes = [] #Lista de constantes
	z = 0.0 #Valor de Z

	def __init__(self, restricciones, z, limitesSup, limitesInf):
		#Inicializacion de las variables
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

	#Retorna los aleatorios asignados al poblador
	def getAleatorios(self):
		return self.aleatorios

	def evaluar(self):
		#Evalua si los numeros aleatorios cumplen con las restricciones
		aux = 1

		for rest in self.restricciones:
			aux = aux * rest.evaluar()
			
		#En caso de ser cero se debe a que alguna restriccion no se cumplio
		if(aux == 1):
			self.valorRestricciones = True

	#Se obtiene el valor de Z
	def calcularZ(self):
		aux = ""
		self.z = 0.0
		self.constantes.clear()

		#Se rescatan las constantes de la expresion
		for letra in self.zExpresion:
			if(letra == "." or letra.isdigit() or letra == "-"):
				aux = aux + letra
			elif(aux != ""):
				self.constantes.append(aux)
				aux = ""

		#Se multiplican las constantes y los aleatorios para encontrar Z
		for num, ale in zip(self.constantes, self.aleatorios):
			self.z = self.z + float(num) * float(ale)
	
	#Retorna Z
	def getZ(self):
		if(self.valorRestricciones):
			return self.z
		else:
			return "Incumplimiento de restricciones"

	def getCeros(self):
		return self.ceros