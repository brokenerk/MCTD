#!python3
from Poblador import Poblador

class PoblacionTotal:
	puntosMax = []
	puntosMin = []
	limitesSup = []
	limitesInf = []
	zMax = 0.0
	zMin = 0.0
	restricciones = []
	totalVariables = 0

	def __init__(self, totalPoblacion, numPoblaciones, restricciones, z):
		self.totalPoblacion = totalPoblacion
		self.numPoblaciones = numPoblaciones
		self.restricciones = restricciones
		self.z = z

	def definirLimites(self):
		constantes = []

		for restriccion in self.restricciones:
			aux = ""
			constantes = []
			restriccion = restriccion + "FIN"

			for letra in restriccion:
				if(letra == "." or letra.isdigit() or letra == "-"):
					aux = aux + letra
				elif(aux != ""):
					constantes.append(aux)
					aux = ""

			self.totalVariables = len(constantes) - 1
			for i in range(len(self.limitesSup), self.totalVariables):
				self.limitesSup.append(0)
				self.limitesInf.append(0)

			for i in range(0, self.totalVariables):
				aux2 = 0
				if(float(constantes[i]) != 0.0):
					aux2 = float(constantes[len(constantes) - 1]) / float(constantes[i])

				if(self.limitesSup[i] < aux2):
					self.limitesSup[i] = aux2

				if(self.limitesInf[i] > aux2):
					self.limitesInf[i] = aux2

		print("totalVariables = " + str(self.totalVariables))
		print("limitesSup:")
		print(self.limitesSup)
		print("limitesInf:")
		print(self.limitesInf)

	def iniciar(self):

		for i in range(0, self.numPoblaciones):
			bandera = True

			for x in range(0, self.totalPoblacion):
				poblador1 = Poblador(self.restricciones, self.z, self.limitesInf, self.limitesSup)
				#print(poblador1.getZ())

				if(poblador1.getZ() != "Incumplimiento de restricciones" and bandera):
					self.zMin = float(poblador1.getZ())
					bandera = False

				if(poblador1.getZ() != "Incumplimiento de restricciones" and float(poblador1.getZ()) > self.zMax):
					self.zMax = float(poblador1.getZ())
					self.puntosMax = poblador1.getAleatorios()

				if(poblador1.getZ() != "Incumplimiento de restricciones" and float(poblador1.getZ()) < self.zMin):
					self.zMin = float(poblador1.getZ())
					self.puntosMin = poblador1.getAleatorios()

				if(len(self.puntosMax) == 0):
					self.puntosMax = poblador1.getCeros()

				if(len(self.puntosMin) == 0):
					self.puntosMin = poblador1.getCeros()
				#del poblador1
			print ("")
			print("------------------------------------------------ Iteracion: " + str(i + 1))
			print("zMax:")
			print(self.zMax)
			print("Max:")
			print(self.puntosMax)
			print("zMin:")
			print(self.zMin)
			print("Min:")
			print(self.puntosMin)