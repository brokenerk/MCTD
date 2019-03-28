#!python3
from Poblador import Poblador
import json

class PoblacionTotal:
	limitesSup = []
	limitesInf = []
	restricciones = []
	totalVariables = 0
	zMaxG = 0.0
	zMinG = 1000000000000000000
	puntosMaxG = []
	puntosMinG = []
	zMaxP = []
	zMinP = []
	puntosMaxP = []
	puntosMinP = []

	def __init__(self, totalPoblacion, numPoblaciones, restricciones, z):
		self.totalPoblacion = totalPoblacion
		self.numPoblaciones = numPoblaciones
		self.restricciones = restricciones
		self.z = z

	def definirLimites(self, noNegatividad):
		constantes = []
		self.limitesSup.clear()
		self.limitesInf.clear()

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

				if(noNegatividad and aux2 < 0.0):
					aux2 = 0.0

				if(self.limitesSup[i] < aux2):
					self.limitesSup[i] = aux2

				if(self.limitesInf[i] > aux2):
					self.limitesInf[i] = aux2

	def calcular(self):
		print ("Calculando..")
		self.zMaxP.clear()
		self.puntosMaxP.clear()
		self.zMinP.clear()
		self.puntosMinP.clear()
		self.puntosMaxG.clear()
		self.puntosMinG.clear()

		for i in range(0, self.numPoblaciones):
			bandera = True
			puntosMax = []
			puntosMin = []
			zMax = 0.0
			zMin = 0.0
			zAux = 0.0

			for x in range(0, self.totalPoblacion):
				poblador1 = Poblador(self.restricciones, self.z, self.limitesInf, self.limitesSup)
				zAux = poblador1.getZ()

				if(zAux != "Incumplimiento de restricciones" and bandera):
					zMin = float(zAux)
					bandera = False

				if(zAux != "Incumplimiento de restricciones" and float(zAux) > zMax):
					zMax = float(zAux)
					puntosMax = poblador1.getAleatorios()

				if(zAux != "Incumplimiento de restricciones" and float(zAux) < zMin):
					zMin = float(zAux)
					puntosMin = poblador1.getAleatorios()

				if(len(puntosMax) == 0):
					puntosMax = poblador1.getCeros()

				if(len(puntosMin) == 0):
					puntosMin = poblador1.getCeros()
				zAux = 0.0

			if(zMax > self.zMaxG):
				self.zMaxG = zMax
				self.puntosMaxG = puntosMax

			if(zMin < self.zMinG):
				self.zMinG = zMin
				self.puntosMinG = puntosMin

			self.zMaxP.append(zMax)
			self.zMinP.append(zMin)
			self.puntosMaxP.append(puntosMax)
			self.puntosMinP.append(puntosMin)

	def getLimitesJSON(self):
		limJSON = {
					"totalVariables": str(self.totalVariables), 
					"limitesSup": self.limitesSup, 
					"limitesInf": self.limitesInf
		}
		return json.dumps(limJSON)

	def getResultadosPoblacionJSON(self):
		resultadosPoblacionJSON = {
									"zMax": self.zMaxP,
									"puntosMax": self.puntosMaxP,
									"zMin": self.zMinP,
									"puntosMin": self.puntosMinP
		}
		return json.dumps(resultadosPoblacionJSON)

	def getMejoresResultadosJSON(self):
		mejoresResultadosJSON = {
							"zMaxG": self.zMaxG,
							"puntosMaxG": self.puntosMaxG,
							"zMinG": self.zMinG,
							"puntosMinG": self.puntosMinG
		}
		return json.dumps(mejoresResultadosJSON)