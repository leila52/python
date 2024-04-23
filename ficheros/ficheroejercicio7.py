import os

def init():
    salir = False
    while not salir:
        print("1.Crear fichero o directorio\n2.Eliminar\n3.Salir")
        opcion = int(input("Introduce una opcion: "))
        match(opcion):
            case 1:
                crear()
            case 2:
                eliminar()
            case 3:
                print("Adios!")
                salir = True

def crear():
    atras = False
    while not atras:
        print("1.Crear fichero\n2.Crear directorio\n3.Atras")
        op = int(input("Que desea crear: "))
        match(op):
            case 1:
                crearFich()
            case 2:
                crearDir()
            case 3:
                atras = True
    
def crearFich():
    ruta = input("Introduce la ruta donde lo desea crear, en el caso de especificarlo se creará en la actual: ")
    nombreFich = input("Introduce el nombre del fichero: ")
    compRuta = ''

    if ruta == "":
        compRuta = os.getcwd()+'/'+nombreFich
    else:
        compRuta = ruta+'/'+nombreFich
        
    if os.path.exists(compRuta):
        print("El fichero ya existe")
    else:
        if ruta == "":
            file = open(os.getcwd()+'/'+nombreFich, "w")
            file.close()
        else:
            file = open(ruta+'/'+nombreFich, "w+")
            file.close()
        print("Se creo el fichero", nombreFich)
    

def crearDir():
    ruta = input("Introduce la ruta donde lo desea crear, en el caso de especificarlo se creará en la actual: ")
    nombreDir = input("Introduce el nombre del directorio: ")
    compRuta = ''
    if ruta == "":
        compRuta = os.getcwd()+'/'+nombreDir
    else:
        compRuta = ruta+'/'+nombreDir
    if os.path.exists(compRuta):
        print("La carpeta ya existe")
    else:
        if ruta == "":
            os.mkdir(os.getcwd()+'/'+nombreDir)
        else:
            os.mkdir(ruta+'/'+nombreDir)
        print("Se creo la carpeta", nombreDir)

def eliminar():
    atras = False
    while not atras:
        print("1.Eliminar fichero\n2.Eliminar directorio\n3.Atras")
        op = int(input("Que desea eliminar: "))
        match(op):
            case 1:
                eliminarFich()
            case 2:
                eliminarDir()
            case 3:
                atras = True

def eliminarFich():
    ruta = input("Introduce la ruta donde se encuentra lo que desea eliminar: ")
    nombre = input("Introduce el nombre: ")
    compRuta = ''
    if ruta == "":
        compRuta = os.getcwd()+'/'+nombre
    else:
        compRuta = ruta + "/" + nombre

    if os.path.exists(compRuta):
        os.remove(compRuta)
        print("Se ha eliminado correctamente")
    else:
        print("No se ha encontrado")

def eliminarDir():
    ruta = input("Introduce la ruta donde se encuentra lo que desea eliminar: ")
    nombre = input("Introduce el nombre: ")
    compRuta = ''
    if ruta == "":
        compRuta = os.getcwd()+'/'+nombre
    else:
        compRuta = ruta + "/" + nombre

    if os.path.exists(compRuta):
        os.rmdir(compRuta)
        print("Se ha eliminado correctamente")
    else:
        print("No se ha encontrado")

init()