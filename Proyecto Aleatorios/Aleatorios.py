#!python3
import random #Libreria randoms
import os #Libreria llamadas al sistema (procesos)
import traceback #Libreria excepciones

def semillaAleatoria():
	try:
		id_proc = os.fork() #Nuevo proceso
		if(id_proc != 0):
			pid = os.getpid() #PID del proceso actual
			random.seed(pid) #Semilla aleatoria
			print (pid)
			exit()
	except Exception as e:
		print(traceback.format_exc())

semillaAleatoria()
print (random.random() * 10)