#!python3
#Compilar y ejecutar: python3 -B flask_app.py
from PoblacionTotal import PoblacionTotal
from flask import Flask, render_template, request #Libreria para usar python en web
import json #Libreria para usar JSON

# Variables de entorno
import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv("URL")
port = os.getenv("PORT")
urlRoot = url + ":" + port

#Indicamos que es una aplicacion Flask - PythonWEB
app = Flask(__name__)

#Creamos el template del formulario para ingresar datos al cargar el servidor
@app.route('/')
def crear():
   return render_template('form.html', urlRoot=url)

#Obtiene los datos del form por medio de POST
@app.route("/mctd_resultados", methods = ["POST"])
def resultado():
	restricciones = []
	tamPoblacion = 0
	numPoblaciones = 0
	noNegatividad = True
	z = ""

	#Obtener parametros del formulario por medio del objeto request
	tamPoblacion = int(request.form["tamPoblacion"])
	restricciones = request.form.getlist("restriccion")
	numeroPoblaciones = int(request.form["numPoblaciones"])
	noNegatividad = "noNegatividad" in request.form
	z = request.form["funcionObjetivo"]

	#Creamos un JSON para guardar el PPL
	pplJSON = {
				"tamPoblacion": str(tamPoblacion),
				"numPoblaciones": str(numeroPoblaciones),
				"restricciones": restricciones,
				"noNegatividad": str(noNegatividad),
				"z": z
	};

	#Creamos el objeto PoblacionTotal, enviandole los datos
	p = PoblacionTotal(tamPoblacion, numeroPoblaciones, restricciones, z)
	#Calculamos los limites y luego los randoms
	p.definirLimites(noNegatividad)
	p.calcular()

	#Obtenemos info por medio de JSON para crear vista
	limitesJSON = p.getLimitesJSON()
	resultadosPoblacionJSON = p.getResultadosPoblacionJSON()
	mejoresResultadosJSON = p.getMejoresResultadosJSON()

	#Enviamos los JSON al html de resultados apoyandonos de javascript
	return render_template("results.html", ppl = json.dumps(pplJSON), limites = limitesJSON, resultadosPoblacion = resultadosPoblacionJSON, mejoresResultados = mejoresResultadosJSON, urlRoot=url)

#Main
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True, port=port)