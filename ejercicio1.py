"""
Ejercicio 1
Investiga el modulo sys para ver como se pueden pasar argumentos a un script de Python. 
Escribe un script llamado argumento que además del nombre de programa sume dos números 
que se pasen como argumentos. 
Imprime en pantalla todas la lista de argumentos. 
Si los argumentos no son numéricos lanza un error de tipo ValueError que lo indique.
Para probar el código deberás entrar en la ruta donde tienes el script y hacer:
[luis@localhost excepciones]$ python3.6 argumentos.py 4 5los argumentos son  ['argumentos.py', '4', '5']
la suma de  4.0  y  5.0  =  9.0
[luis@localhost excepciones]$ python3.6 argumentos.py 4 p
los argumentos son  ['argumentos.py', '4', 'p']
los argumentos tienen que ser númericos
[luis@localhost excepciones]$
"""
import sys

class NumeroDeArgumentosError(Exception):
	pass

print("los argumentos son ",sys.argv)
try:
	if len(sys.argv) != 3:
		raise NumeroDeArgumentosError

	primero = float(sys.argv[1])
	segundo = float(sys.argv[2])
	suma = primero + segundo

except NumeroDeArgumentosError:
	print("número de argumentos incorrecto")
	print("sintaxis: python3 nombreScript operando1 operando2")
except ValueError:
	print("los argumentos tienen que ser numéricos")
else:
	print("la suma es", suma)

