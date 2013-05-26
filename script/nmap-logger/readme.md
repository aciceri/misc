# Nmap logger ##

## Descrizione ##

Un semplice logger scritto in **Python 3** che permette di effettuare scansioni di una rete tramite **Nmap** e di salvare i risultati in un database **SQLite 3**.
Questo programma permette anche di visualizzare un anteprima via web dei dati acquisiti.

## Dipendenze ##

+ Python 3
  Su Debian-like: *sudo apt-get install python3*
+ Nmap (il classico programma da linea di comando)
  Su Debian-like: *sudo apt-get install nmap*
+ CherryPy (solo se si desidera l'anteprima dei dati via web)
  Su Debian-like:: *Da controllare*

## Struttura ##

+ nmap-logger: interfaccia con la shell e coordinamento moduli
+ scanner: modulo addetto alla scansione della rete
+ logger: modulo addetto al salvataggio in un database
+ webserver: modulo addetto ad una semplice consultazione via web
