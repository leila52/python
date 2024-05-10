def contar_veces(nom_fichero, palabra):
  try:
    fichero = open(nom_fichero,"r")
  except FileNotFoundError:
    print("Lo siento, el archivo no existe")
    return("fin de la ejecución")
  else:
    contenido = fichero.read()
    return(contenido.count(palabra))


def main():
  print(contar_veces("/home/luis/ejercicio10.py","print"))


main()