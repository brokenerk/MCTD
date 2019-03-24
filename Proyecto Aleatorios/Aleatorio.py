#!python3
import random #Libreria randoms
import os #Libreria llamadas al sistema
import sys
import traceback #Libreria excepciones

class Aleatorio:
	limitesSup = []
	limitesInf = []
	restricciones = []

	def __init__(self, restricciones, limitesSup, limitesInf, iteracion):
		self.restricciones = restricciones
		self.limitesSup = limitesSup
		self.limitesInf = limitesInf
		#Random criptografico segun la iteracion
		self.semilla = int.from_bytes(os.urandom(iteracion), sys.byteorder) 
		#Semilla Aleatoria
		random.seed(self.semilla) 

	def getAleatorio(self):
		aleatorio = []
		for limMax, limMin in zip(self.limitesSup, self.limitesInf):
			aleatorio.append(random.uniform(limMin, limMax))
			
		return aleatorio