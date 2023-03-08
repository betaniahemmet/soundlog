
# Amplitude logger

Ett projekt som siktar mot att kunna logga och spara data om ljudvolym med hjälp av en mikrofon. Projektet syftar inte mot att mäta decibel, utan istället att se ljudvolymens skillnader under olika tider för att sedan kunna bidra till ytterligare slutsatser tillsammans med annan data. Projektet kommer även att kunna visualisera datan i grafer för att göra den mer lättillgänglig. Det bör poängteras att projektet inte samlar in ljud: Det som spelas in i femsekundersintervaller raderas efter att den högst uppmätta amplituden har dokumenterats i en csv-fil.
<br />

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
$ git clone https://github.com/betaniahemmet/soundlog.git
$ cd soundlog
$
$ # Virtualenv modules installation (Unix based systems)
$ python3 -m venv "soundlog-env"
$ source soundlog-env/bin/activate
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
$ # Start logging
$ python soundlog.py
```

<br />



## Credits & Links

- [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - PyAudio



<br />


