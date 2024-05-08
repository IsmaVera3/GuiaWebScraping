import pyperclip
import requests
from bs4 import BeautifulSoup
import sys

def obtener_url():
    #strip borra espacios vacios
    url = pyperclip.paste().strip()
    if not url.startswith("http"):
        print("La URL no es válida.")
        sys.exit(1)
    return url

def obtener_parrafos(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        elementos_parrafo = soup.find_all('p')
        parrafos = []
        for i in elementos_parrafo:
            parrafos.append(i.get_text())
        return parrafos
    except requests.exceptions.RequestException as e:
        print("Error al obtener la página:", e)
        sys.exit(1)

try:
    url = obtener_url()
    print("Obteniendo párrafos de:", url)
    parrafos = obtener_parrafos(url)
    print("\nLista de párrafos:")
    for parrafo in enumerate(parrafos, 1):
        print(parrafo)
except KeyboardInterrupt:
    print("\nOperación interrumpida por el usuario.")
