#!python3
from Poblador import Poblador
import json #Libreria para usar JSON

class PoblacionTotal:
	limitesSup = [] #Lista de limites superiores
	limitesInf = [] #Lista de limites inferiores
	restricciones = [] #Lista de las restricciones
	totalVariables = 0 #Numero total de restricciones
	zMaxG = 0.0 #Mejor valor maximo de Z hallado
	zMinG = 1000000000000000000 #Mejor valor minimo de Z hallado
	puntosMaxG = [] #Puntos de la mejor solucion maxima hallada
	puntosMinG = [] #Puntos de la mejor solucion minima hallada
	zMaxP = [] #Valores maximos de Z
	zMinP = [] #Valores minimos de Z
	puntosMaxP = [] # Puntos de solucciones maxima
	puntosMinP = [] #Puntos de soluciones minimos

	def __init__(self, totalPoblacion, numPoblaciones, restricciones, z):
		#Inicializacion de variables
		self.totalPoblacion = totalPoblacion
		self.numPoblaciones = numPoblaciones
		self.restricciones = restricciones
		self.z = z

	def definirLimites(self, noNegatividad):
		#Arreglo que contiene las constantes
		constantes = [] 
		#Limpiar listas
		self.limitesSup.clear()
		self.limitesInf.clear() 

		for restriccion in self.restricciones:
			aux = ""
			constantes = []
			#Se concatena la palabra FIN para recorrer completamente la lista
			restriccion = restriccion + "FIN"

			for letra in restriccion:
				#Al encontrar estos caracteres suponemos que se trata de un numero
				if(letra == "." or letra.isdigit() or letra == "-"):
					#Concatenamos los caracteres permitidos
					aux = aux + letra
				elif(aux != ""):
					#Se guarda la constante
					constantes.append(aux)
					aux = ""

			self.totalVariables = len(constantes) - 1
			for i in range(len(self.limitesSup), self.totalVariables):
				#Se inicializan las listas con 0
				self.limitesSup.append(0)
				self.limitesInf.append(0)

			#Despeje de las ecuaciones
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
		#Limpiar variables
		self.zMaxP.clear()
		self.puntosMaxP.clear()
		self.zMinP.clear()
		self.puntosMinP.clear()
		self.puntosMaxG.clear()
		self.puntosMinG.clear()

		#Implementacion de las iteraciones
		for i in range(0, self.numPoblaciones):
			bandera = True
			puntosMax = []
			puntosMin = []
			zMax = 0.0
			zMin = 0.0
			zAux = 0.0

			for x in range(0, self.totalPoblacion):
				#Se genera un solo poblador, se limpia y se vuelve a ocupar para optimizacion del procesamiento
				#Se determina si cumple o no con las restricciones
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

			#Se obtienen los mejores resultados de todo las poblaciones
			if(zMax > self.zMaxG):
				self.zMaxG = zMax
				self.puntosMaxG = puntosMax

			if(zMin < self.zMinG):
				self.zMinG = zMin
				self.puntosMinG = puntosMin

			#Se van guardando los resultados de las poblaciones
			self.zMaxP.append(zMax)
			self.zMinP.append(zMin)
			self.puntosMaxP.append(puntosMax)
			self.puntosMinP.append(puntosMin)

	#Retorna los limites como JSON
	def getLimitesJSON(self):
		limJSON = {
					"totalVariables": str(self.totalVariables), 
					"limitesSup": self.limitesSup, 
					"limitesInf": self.limitesInf
		}
		return json.dumps(limJSON)

	#Retorna todos los resultados como JSON
	def getResultadosPoblacionJSON(self):
		resultadosPoblacionJSON = {
									"zMax": self.zMaxP,
									"puntosMax": self.puntosMaxP,
									"zMin": self.zMinP,
									"puntosMin": self.puntosMinP
		}
		return json.dumps(resultadosPoblacionJSON)

	#Retorna los mejores resultados como JSON
	def getMejoresResultadosJSON(self):
		mejoresResultadosJSON = {
							"zMaxG": self.zMaxG,
							"puntosMaxG": self.puntosMaxG,
							"zMinG": self.zMinG,
							"puntosMinG": self.puntosMinG
		}
		return json.dumps(mejoresResultadosJSON)