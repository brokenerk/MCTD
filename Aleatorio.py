#!python3
import random #Libreria de randoms
import os #Libreria de llamadas al sistema
import sys #Libreria para definir tamaño en bytes

#Implementacion y generaciones de numeros aleatorios tomando aleatorios criptograficos del sistema operativo para generar una semilla aleatoria
class Aleatorio:
	limitesSup = [] #Lista de los limites superiores
	limitesInf = [] #Lista de los limites inferiores
	restricciones = [] #Lista de restricciones

	def __init__(self, restricciones, limitesSup, limitesInf):
		self.restricciones = restricciones #Asinar restricciones
		self.limitesSup = limitesSup #Asignar limites superiores
		self.limitesInf = limitesInf #Asiganar limites inferiores
		
		#Random criptografico con ayuda de la libreria os de 2000 bytes
		self.semilla = int.from_bytes(os.urandom(2000), sys.byteorder) 

		#Semilla Aleatoria en random()
		random.seed(self.semilla) 

	def getAleatorio(self):
		aleatorio = []
		#Se toman los limites de las restricciones para generar el numero flotante aleatorio
		for limMax, limMin in zip(self.limitesSup, self.limitesInf):
			aleatorio.append(random.uniform(limMin, limMax))
		#Retorno de la lista de aleatorio para cada individuo
		return aleatorio