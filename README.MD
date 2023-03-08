
# Amplitude logger

Ett projekt som siktar mot att kunna logga och spara data om ljudvolym i ett utrymme med hjälp av en mikrofon. Projektet syftar inte mot att mäta decibel, utan istället att se ljudvolymens skillnader under olika tider för att sedan kunna bidra till ytterligare slutsatser tillsammans med annan data. Projektet kommer även att kunna visualisera datan i grafer för att göra den mer lättillgänglig. Det bör poängteras att projektet inte samlar in ljud: d Det som spelas in i femsekundersintervaller raderas efter att den högst uppmätta amplituden har dokumenterats.
<br />

> Links

- [Winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/) - Winget
- [Powershell](https://winget.run/pkg/Microsoft/PowerShell) - Winget Powershell
- [Pyenv-win](https://pyenv-win.github.io/pyenv-win/) - Pyenv-win
y



<br />

## The web interface

Gif to demo project.

<br />

![Website preview](https://github.com/betaniahemmet/fakturor/blob/main/media/demo.gif)

<br />

## Build from sources


<br />
Jag rekommenderar att man använder Winget som pakethanterare, Powershell istället för CMD och Pyenv-win istället för att installera senaste Python-versionen. Inget av detta är dock nödvändigt. Nedan följer en enkel beskrivning av hur man gör utan att använda något av detta. Beskrivningen förutsätter dock att man har Python installerat.
<br />

```bash
$ # Clone the sources
$ git clone https://github.com/betaniahemmet/fakturor.git
$ cd fakturor
$
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv "fakturor-env"
$ source fakturor-env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ python -m venv venv
$ .\venv\Scripts\activate
$
$ # Install requirements (Unix based systems)
$ pip3 install -r requirements.txt
$
$ # Install requirements (Windows)
$ pip install -r requirements.txt
$
$
$ # Set the FLASK_APP environment variable
$ (Unix/Mac) export FLASK_APP=run.py
$ (Windows) set FLASK_APP=run.py
$ (Powershell) $env:FLASK_APP = ".\run.py"
$
$ 
$ # Access the UI in browser: 
$ http://127.0.0.1:5000/
```

<br />



## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/) - The official website


<br />


