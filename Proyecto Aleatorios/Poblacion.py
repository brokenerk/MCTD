from Restriccion import Restriccion
from Aleatorio import Aleatorio
class Poblador:
	ceros=[]
	restriciones=[]
	aleatorios=[]
	zExpresion=""
	constatantes=[]
	z=0
	def  __init__(self,restriciones, z):
		self.valorRestricciones=False
		self.ceros=[]
		alea=Aleatorio(restriciones)
		self.aleatorios=alea.getAletorio()
		#print("Aleatorios en pesona")
		#print(self.aleatorios)
		for x in range(0,len(self.aleatorios)):
			self.ceros.append(0)
		self.zExpresion=z
		self.restriciones=[]
		for rest in restriciones:
			self.restriciones.append(Restriccion(rest,self.aleatorios))
		self.evaluar()
		self.calcularZ()
	def getAleatorios(self):
		return self.aleatorios
	def evaluar(self):
		aux=1
		for rest in self.restriciones:
			aux = aux*rest.evaluar()
		#print("aux="+str(aux))
		if(aux==1):
			self.valorRestricciones=True

	def calcularZ(self):
		aux=""
		for letra in self.zExpresion:
			if(letra == "." or letra.isdigit() or letra=="-"):
				aux=aux+letra
			elif(aux!=""):
				self.constatantes.append(aux)
				aux=""
		for num,ale in zip(self.constatantes,self.aleatorios):
			self.z=self.z+float(num)*float(ale)
		
	def getZ(self):
		if(self.valorRestricciones):
			return self.z
		else:
			return "Incumplimiento de restriciones"
	def getCeros(self):
		return self.ceros
	#def __del__(self):
	#	del alea
	#	del self.aleatorios
	#	del self
	#	del self.valorRestricciones
	#	print("Destruido")