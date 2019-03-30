#!python3
#Compilar y ejecutar: python3 -B Main.py
from PoblacionTotal import PoblacionTotal
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/')
def crear():
   return render_template('form.html')

@app.route("/mctd_resultados", methods = ["POST"])
def resultado():
	restricciones = []
	tamPoblacion = 0
	numPoblaciones = 0
	noNegatividad = True
	z = ""

	tamPoblacion = int(request.form["tamPoblacion"])
	restricciones = request.form.getlist("restriccion")
	numeroPoblaciones = int(request.form["numPoblaciones"])
	noNegatividad = "noNegatividad" in request.form
	z = request.form["funcionObjetivo"]

	pplJSON = {
				"tamPoblacion": str(tamPoblacion),
				"numPoblaciones": str(numeroPoblaciones),
				"restricciones": restricciones,
				"noNegatividad": str(noNegatividad),
				"z": z
	};

	p = PoblacionTotal(tamPoblacion, numeroPoblaciones, restricciones, z)
	p.definirLimites(noNegatividad)
	p.calcular()

	#Obtenemos info por medio de JSON para crear vista
	limitesJSON = p.getLimitesJSON()
	resultadosPoblacionJSON = p.getResultadosPoblacionJSON()
	mejoresResultadosJSON = p.getMejoresResultadosJSON()

	#Enviamos los JSON al html apoyandonos de javascript
	return render_template("results.html", ppl = json.dumps(pplJSON), limites = limitesJSON, resultadosPoblacion = resultadosPoblacionJSON, mejoresResultados = mejoresResultadosJSON)

if __name__ == "__main__":
	app.run(debug=True)