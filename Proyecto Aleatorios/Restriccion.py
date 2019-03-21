#Clase restricción

class Restriccion:
	def __init__(self,expresion, aleatorios):
		self.expresion=expresion + "FIN"
		self.constatantes=[]
		self.aleatorios=aleatorios
		self.desigualdad=9
		self.valor=1
		for d in range(0,len(aleatorios)+1):
			self.constatantes.append(0)
	def separar(self):
		aux=""
		i=0
		#print("Len="+str(len(self.constatantes)))
		for letra in self.expresion:
			if(letra == "." or letra.isdigit() or letra=="-"):
				aux=aux+letra
			elif(aux!=""):
				#print("i="+str(i))
				self.constatantes[i]=aux
				i=i+1
				aux=""
			if(letra==">"):
				self.desigualdad=0
			elif(letra=="<"):
				self.desigualdad=1
			elif(letra=="="):
				if(self.desigualdad==0):
					self.desigualdad=2
				elif(self.desigualdad==1):
					self.desigualdad=3
				else:
					self.desigualdad=4

	def getConstantes(self):
		return self.constatantes
	def getExpresion(self):
		return self.expresion
	def evaluar(self):
		self.separar()
		valor = 0;
		for s,c in zip(self.aleatorios,self.constatantes):
			valor = valor + s*float(c)
		if(self.desigualdad==0):
			valor=self.mayor(valor)
		elif(self.desigualdad==1):
			valor=self.menor(valor)
		elif(self.desigualdad==2):
			valor=self.mayorIgual(valor)
		elif(self.desigualdad==3):
			valor=self.menorIgual(valor)
		elif(self.desigualdad==4):
			valor=self.igual(valor)

		self.valor=valor
		return valor

	def mayor(self,valor):
		if(valor>float(self.constatantes[len(self.constatantes)-1])):
			return 1
		else:
			return 0
	def menor(self,valor):
		if(valor<float(self.constatantes[len(self.constatantes)-1])):
			return 1
		else:
			return 0
	def mayorIgual(self,valor):
		aux=self.constatantes[len(self.constatantes)-1]
		if(valor > float(self.constatantes[len(self.constatantes)-1])):
			return 1
		elif(str(valor)==aux):
			return 1
		else:
			return 0
	def menorIgual(self,valor):
		if(valor <= float(self.constatantes[len(self.constatantes)-1])):
			return 1
		else:
			return 0
	def igual(self,valor):
		aux=self.constatantes[len(self.constatantes)-1]
		if(str(valor)==aux):
			return 1
		else:
			return 0

		