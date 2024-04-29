# Ejercicio 5: Copia en disco de una página web
# Este programa realiza una copia en disco de una página web.

import urllib.request
url= "https://tools.ietf.org/html/rfc1180"
webpage = urllib.request.urlopen(url)

archivo_webpage= open ("dump.html" ,"wb")
for line in webpage:
    archivo_webpage.write(line)

archivo_webpage.close()