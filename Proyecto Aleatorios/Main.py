#!python3
#Compilar y ejecutar: python3 -B Main.py
from PoblacionTotal import PoblacionTotal
from flask import Flask, render_template, request

"""
def main():
	tamPoblacion = 2000
	numeroPoblaciones = 5

	restricciones = ["1A-1B>=0", "1A-1B>=10", "1A-1B<=30", "0A+1B>=10", "0A+1B<=30", "0A+1B>=0", "1A+0B>=0"]
	z = "0.4A+0.2B=Z"

	p = PoblacionTotal(tamPoblacion, numeroPoblaciones, restricciones, z)
	p.definirLimites()
	p.iniciar()

main()"""

app = Flask(__name__)

@app.route('/')
def crear():
   return render_template('form.html')

@app.route("/mctd_resultados", methods = ["POST"])
def resultado():
	tamPoblacion = int(request.form["tamPoblacion"])
	restricciones = ["1A-1B>=0", "1A-1B>=10", "1A-1B<=30", "0A+1B>=10", "0A+1B<=30", "0A+1B>=0", "1A+0B>=0"]
	numeroPoblaciones = int(request.form["numPoblaciones"])
	z = request.form["funcionObjetivo"]

	p = PoblacionTotal(tamPoblacion, numeroPoblaciones, restricciones, z)
	p.definirLimites()
	p.iniciar()
	return "Ok!"
  	#return render_template("results.html", tamPoblacion = tamPoblacion, numPoblaciones = numPoblaciones, funcionObjetivo = funcionObjetivo)

if __name__ == "__main__":
	app.run()