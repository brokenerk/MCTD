#!python3
import random #Libreria randoms
import os #Libreria llamadas al sistema
import sys
import traceback #Libreria excepciones

"""
Implementacion y generaciones de numeros aleatorios tomando procesos del sistema operativo para generar una semilla aleatoria
"""
class Aleatorio:
	limitesSup = []#lista de los limites superiores
	limitesInf = []#lista de los limites inferiores
	restricciones = []#lista de restricciones

	def __init__(self, restricciones, limitesSup, limitesInf):
		self.restricciones = restricciones#asinar restircciones
		self.limitesSup = limitesSup#asignar limites superiores
		self.limitesInf = limitesInf#asiganar limites inferiores
		#Random criptografico
		self.semilla = int.from_bytes(os.urandom(2000), sys.byteorder) 
		#Semilla Aleatoria
		random.seed(self.semilla) 

	def getAleatorio(self):
		aleatorio = []
		"""
		Se toman los limites de las restricciones para generar el numero flotante aleatorio
		"""
		for limMax, limMin in zip(self.limitesSup, self.limitesInf):
			aleatorio.append(random.uniform(limMin, limMax))
		return aleatorio#retorno de la lista de aleatorio para cada individuo