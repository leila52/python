# Ejercicio 5: Copia en disco de una página web
# Este programa realiza una copia en disco de una página web.

import urllib.request

# URL de la página web a copiar.
url = "https://tools.ietf.org/html/rfc1180"

# Se descarga el contenido de la página web.
with urllib.request.urlopen(url) as response:
    html = response.read().decode("utf-8")

# Se escribe el contenido descargado en un fichero llamado "dump.html".
with open("dump.html", "w") as f:
    f.write(html)

print("Copia de la página web realizada con éxito.")