#!python3
class Restriccion:

	def __init__(self, expresion, aleatorios):
		#Inicilizacion de valores
		self.expresion = expresion + "FIN"
		self.constantes = []
		self.aleatorios = aleatorios
		self.desigualdad = 9
		self.valor = 1

		for d in range(0, len(aleatorios) + 1):
			self.constantes.append(0)

	def separar(self):
		aux = ""
		i = 0
		for letra in self.expresion:#Recuperacion de las constantes de la restriccion
			if(letra == "." or letra.isdigit() or letra == "-"):
				aux = aux + letra
			elif(aux != ""):
				self.constantes[i] = aux
				i = i + 1
				aux = ""

			#Identificacion del sentido de desigualdad o igualdad
			if(letra == ">"):
				self.desigualdad = 0
			elif(letra == "<"):
				self.desigualdad = 1
			elif(letra == "="):
				if(self.desigualdad == 0):
					self.desigualdad = 2
				elif(self.desigualdad == 1):
					self.desigualdad = 3
				else:
					self.desigualdad = 4

	def getConstantes(self):#Obtener constantes
		return self.constantes

	def getExpresion(self):#Obtner la expresion de la restriccion
		return self.expresion

	def evaluar(self):

		#Evaluacion de las restricciones
		self.separar()
		valor = 0;
		for s, c in zip(self.aleatorios, self.constantes):
			valor = valor + s * float(c)

		#Llamado a los metodos
		if(self.desigualdad == 0):
			valor = self.mayor(valor)
		elif(self.desigualdad == 1):
			valor = self.menor(valor)
		elif(self.desigualdad == 2):
			valor = self.mayorIgual(valor)
		elif(self.desigualdad == 3):
			valor = self.menorIgual(valor)
		elif(self.desigualdad == 4):
			valor = self.igual(valor)

		self.valor = valor
		return valor

	def mayor(self,valor):#Evaluacion de la desigualdad
		if(valor > float(self.constantes[len(self.constantes) - 1])):
			return 1
		else:
			return 0

	def menor(self, valor):#Evaluacion de la desigualdad
		if(valor < float(self.constantes[len(self.constantes) - 1])):
			return 1
		else:
			return 0
	
	def mayorIgual(self, valor):#Evaluacion de la desigualdad
		aux = self.constantes[len(self.constantes) - 1]
		if(valor > float(self.constantes[len(self.constantes) - 1])):
			return 1
		elif(str(valor) == aux):
			return 1
		else:
			return 0

	def menorIgual(self, valor):#Evaluacion de la desigualdad
		if(valor <= float(self.constantes[len(self.constantes) - 1])):
			return 1
		else:
			return 0

	def igual(self, valor):#Evaluacion de la igualdad
		aux = self.constantes[len(self.constantes) - 1]
		if(str(valor) == aux):
			return 1
		else:
			return 0