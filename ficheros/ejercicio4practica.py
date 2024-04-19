def hacer_backup(nombre_origen):
    nombre_backup = nombre_origen + ".bak.txt"
    with open(nombre_origen, 'r') as origen, open(nombre_backup, 'w') as backup:
        for linea in origen:
            backup.write(linea)
    print("Backup creado correctamente:", nombre_backup)

def main():
    nombre_origen = input("Introduce el nombre del fichero de texto del que quieres hacer el backup: ")
    hacer_backup(nombre_origen)

main()
