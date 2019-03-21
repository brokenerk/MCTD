from PoblacionTotal import PoblacionTotal

def main():
	numeroDePobladores=5000000
	#restricciones = ["3x+5y<=100","2x+3y<=75"]
	restricciones = ["0.6C+0.2A+0.2N>=1500","0.4C+0.3A+0.3N>=500","0.1C+0.45A+0.45N>=1000","0C+1A+0N<=3000","0C+0A+1N<=2000","0C+1A+0N>=1250","0C+0A+1N>=750"]
	#z = "2x+1y=z"
	z="0.8A+0.6N+0.35C=z"
	p=PoblacionTotal(numeroDePobladores,restricciones,z)
	p.iniciar()

if __name__ == "__main__":
    main()