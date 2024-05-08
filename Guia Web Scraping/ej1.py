import requests
import pyperclip

res = requests.get(pyperclip.waitForNewPaste())
try:
    res.raise_for_status()
except:
    print('no pudo ser perro')

playFile = open('mechi.html', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()