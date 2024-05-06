import pyperclip
import requests

url = pyperclip.paste('https://pypi.org/project/pyperclip/')

response = requests.get(url)

if response.status_code == 200:
    with open('contenido_web.txt', 'w', encoding='utf-8') as archivo:
        archivo.write(response.text)
    print("se guardo con exito en => 'contenido_web.txt'")
else:
    print("no se encontro ninguna pagina. Código de estado:", response.status_code)
