# Nmap logger ##

## Descrizione ##

Un semplice logger che utilizza nmap per scansionare la rete e che poi salva i risultati in un database.

## Dipendenze ##

+ Python 3
+ Nmap (il classico programma da linea di comando)
+ Python-nmap (modulo python per interfacciarsi con nmap)
+ SQLAlchemy (modulo python per interfacciarsi con qualsiasi database)

## Struttura ##

+ nmap-logger: interfaccia con la shell e coordinamento moduli
+ scan: scansione rete
+ log: salvataggio dati
+ webserver: visualizzazione realtime del database
