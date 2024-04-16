# Ejercicio 4: Backup de un fichero de texto
# Este programa realiza una copia de seguridad de un fichero de texto.

# Se solicita al usuario el nombre del fichero de texto a respaldar.
nombre_fichero = input("Ingrese el nombre del fichero de texto a respaldar: ")

# Se crea el nombre del nuevo fichero de backup.
nombre_backup = nombre_fichero + "_bak.txt"

# Se abren ambos ficheros, el original y el de backup.
with open(nombre_fichero, "r") as origen, open(nombre_backup, "w") as destino:
    # Se lee el fichero original línea por línea y se escribe en el fichero de backup.
    for linea in origen:
        destino.write(linea)

# Se cierran ambos ficheros.
print("Copia de seguridad creada exitosamente.")