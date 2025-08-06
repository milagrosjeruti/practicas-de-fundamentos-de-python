#contar palabras de un archivo o una web

from urllib import request
from urllib.error import URLError
def ver_contenido(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return contenido
def contar_palabbras(url):
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())
    
url = 'https://es.wikipedia.org/wiki/Python'
print(ver_contenido)
print("\n-------------------------------------\n")
print(contar_palabbras(url))