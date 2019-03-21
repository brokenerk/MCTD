import random
class Aleatorio:
	max=0
	min=0
	puntosMax=[]
	puntosMin=[]
	restricciones=[]
	totalVariables=0
	def __init__(self,restricciones):
		self.restricciones=restricciones
		self.puntosMax=[]
		self.puntosMin=[]
		self.separar()
		self.totalVariables=0
	def separar(self):
		constantes=[]
		for restriccion in self.restricciones:
			aux=""
			constantes=[]
			#print(restriccion)
			restriccion=restriccion+"FIN"
			for letra in restriccion:
				if(letra == "." or letra.isdigit() or letra=="-"):
					aux=aux+letra
				elif(aux!=""):
					constantes.append(aux)
					aux=""
			if(self.totalVariables<len(constantes)):
				self.totalVariables=len(constantes)
				for i in range(len(self.puntosMax),self.totalVariables-1):
					self.puntosMax.append(0)
					self.puntosMin.append(0)


			#print(constantes)
			#print(len(self.puntosMax))
			#print(self.puntosMax[0])
			for i in range(0,len(constantes)-1):
				#print("i=")
				#print(i)
				aux2=0
				if(float(constantes[i]) != 0.0):
					aux2=float(constantes[len(constantes)-1])/float(constantes[i])
				#print("T="+constantes[len(constantes)-1])
				#print("C"+str(i)+constantes[i])
				#print(aux2)
				if(self.puntosMax[i]<aux2):
					self.puntosMax[i]=aux2

				if(self.puntosMin[i]>aux2):
					self.puntosMin[i]=aux2

		#print("totalVariables="+str(self.totalVariables))
		#print("puntosMax:")
		#print(self.puntosMax)
		#print("puntosMin:")
		#print(self.puntosMin)
	def getAletorio(self):
		aleatorio=[]
		for puntoMax, puntoMin in zip(self.puntosMax,self.puntosMin):
			aleatorio.append(random.uniform(float(puntoMax),float(puntoMin)))
		return aleatorio
	#def __del__(self):
	#	del self
	#	print("Aleatorio destruido")