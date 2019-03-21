from Poblacion import Poblador
class PoblacionTotal:
	puntosMax=[]
	puntosMin=[]
	zMax=0.0
	zMin=0.0
	restricciones=[]
	def __init__(self,totalIteraciones,restricciones,z):
		self.totalIteraciones=totalIteraciones
		self.restricciones=restricciones
		self.z=z
	def iniciar(self):
		bandera=True
		for x in range(1,self.totalIteraciones):
			poblador1 = None
			poblador1 = Poblador(self.restricciones,self.z)
			#print(poblador1.getZ())
			if(poblador1.getZ() != "Incumplimiento de restriciones" and bandera):
				self.zMin=float(poblador1.getZ())
				bandera=False
			if(poblador1.getZ() != "Incumplimiento de restriciones" and float(poblador1.getZ())>self.zMax):
				self.zMax=float(poblador1.getZ())
				self.puntosMax=poblador1.getAleatorios()
			if(poblador1.getZ() != "Incumplimiento de restriciones" and float(poblador1.getZ())<self.zMin):
				self.zMin=float(poblador1.getZ())
				self.puntosMin=poblador1.getAleatorios()
			if(len(self.puntosMax)==0):
				self.puntosMax=poblador1.getCeros()
			if(len(self.puntosMin)==0):
				self.puntosMin=poblador1.getCeros()
			#del poblador1
		print("zMax:")
		print(self.zMax)
		print("Max:")
		print(self.puntosMax)
		print("zMin:")
		print(self.zMin)
		print("Min:")
		print(self.puntosMin)

