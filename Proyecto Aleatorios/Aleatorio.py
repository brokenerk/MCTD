#!python3
import random #Libreria randoms
import os #Libreria llamadas al sistema (procesos)
import sys
import traceback #Libreria excepciones

class Aleatorio:
	limitesSup = []
	limitesInf = []
	restricciones = []

	def __init__(self, restricciones, limitesSup, limitesInf):
		self.restricciones = restricciones
		self.limitesSup = limitesSup
		self.limitesInf = limitesInf
		self.id_proc = 0
		self.pid = 0
		#Semilla Aleatoria
		try:
			self.id_proc = os.fork() #Nuevo proceso
			if(self.id_proc == 0):
				self.pid = os.getpid() #PID del proceso actual
				random.seed(self.pid) #Semilla aleatoria
				os._exit(1)
		except:
			print(traceback.format_exc())

	def getAleatorio(self):
		aleatorio = []
		for limMax, limMin in zip(self.limitesSup, self.limitesInf):
			aleatorio.append(random.uniform(limMin, limMax))
			
		return aleatorio