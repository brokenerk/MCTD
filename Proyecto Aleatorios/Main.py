#!python3
#Compilar y ejecutar: python3 -B Main.py
from PoblacionTotal import PoblacionTotal
from flask import Flask, render_template, request
import json

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
	restricciones = []
	tamPoblacion = int(request.form["tamPoblacion"])
	restricciones = request.form.getlist("restriccion")
	numeroPoblaciones = int(request.form["numPoblaciones"])
	noNegatividad = "noNegatividad" in request.form
	z = request.form["funcionObjetivo"]

	p = PoblacionTotal(tamPoblacion, numeroPoblaciones, restricciones, z)
	p.definirLimites(noNegatividad)
	p.calcular()

	#Obtenemos info por medio de JSON para crear vista
	limitesJSON = p.getLimitesJSON()
	resultadosPoblacionJSON = p.getResultadosPoblacionJSON()
	mejoresResultadosJSON = p.getMejoresResultadosJSON()

	#Enviamos los JSON al html apoyandonos de javascript
	return render_template("results.html", limites = limitesJSON, resultadosPoblacion = resultadosPoblacionJSON, mejoresResultados = mejoresResultadosJSON)

if __name__ == "__main__":
	app.run(debug=True)