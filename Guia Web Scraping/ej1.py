import requests
import pyperclip
pyperclip.copy('https://brockhoferart.com/projects')
res = requests.get(pyperclip.paste())
try:
    res.raise_for_status()
except Exception as exc:
    print('no pudo ser perro: %s' % (exc))

playFile = open('penex.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()
