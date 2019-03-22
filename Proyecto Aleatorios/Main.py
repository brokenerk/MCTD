#!python3
from PoblacionTotal import PoblacionTotal

def main():
	numeroDePobladores = 2000
	numeroPoblaciones = 5

	restricciones = ["1A-1B>=0", "1A-1B>=10", "1A-1B<=30", "0A+1B>=10", "0A+1B<=30", "0A+1B>=0", "1A+0B>=0"]
	z = "0.4A+0.2B=z"

	p = PoblacionTotal(numeroDePobladores, numeroPoblaciones, restricciones, z)
	p.definirLimites()
	p.iniciar()

main()