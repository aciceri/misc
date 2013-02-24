#!/usr/bin/env python3

import argparse
import sqlite3
from subprocess import call, check_output
from datetime import datetime
from time import sleep
from sys import exit


class Ping:
    '''Classe d'interfaccia allo strumento Ping'''

    def __init__(self, target, deadline):
        '''Inizializza le variabile per creare i parametri di ping'''
        self.target = str(target)
        self.deadline = str(deadline)  # Il tempo limite di verifica
        self.command = 'ping -w %s %s > /dev/null' % (self.deadline, self.target)
        #L'output di ping viene rediretto in /dev/null in modo da non stampare nulla

    def execute(self):
        '''Esegue il ping e ritorna True se l'host e' raggiungibile'''
        self.status = call(self.command, shell=True)
        if self.status == 0:
            return True
        else:
            return False


class Db:
    '''Classe d'interfaccia con il DataBase'''

    def __init__(self, file='log.db'):
        '''Crea la connessione al DB e imposta la tabella'''
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

        query = '''CREATE TABLE IF NOT EXISTS log(
                Id INTEGER PRIMARY KEY,
                Date DATETIME,
                Source TEXT,
                Target TEXT,
                Pingable INTEGER)'''

        self.cursor.execute(query)  # Crea la tabella solo se non gia' presente
        self.cursor.close()

    def log(self, source, target, pingable):
        '''Inserisci i dati nella tabella'''
        now = datetime.today()
        self.cursor = self.connection.cursor()

        query = '''INSERT INTO log(Date, Source, Target, Pingable)
        VALUES("%s","%s","%s", %d);''' % (str(now), str(source), str(target), int(pingable))

        self.cursor.execute(query)
        self.cursor.close()
        self.connection.commit()


def main():
    parser = argparse.ArgumentParser(description='''Semplice ping-logger realizzato per l\'ITSOS Marie Curie''')
    parser.add_argument('-i', '--interval', dest='INTERVAL', action='store',
                        default=60, type=int, help='imposta l\'intervallo di scansione in millisecondi')
    parser.add_argument('-v', '--verbose', dest='VERBOSE', action='store_true',
                        default=False, help='mostra un semplice log durante l\'esecuzione')
    parser.add_argument('HOST', action='store',  help='indirizzo IP dell\'host con cui effettuare il ping')

    args = parser.parse_args()

    deadline = 2
    ping = Ping(args.HOST, deadline)
    db = Db('log.db')
    ip = check_output('hostname -I', shell=True, universal_newlines=True).strip('\n')
    while True:
        try:
            pingable = ping.execute()
            if args.VERBOSE:
                if pingable:
                    print('%s: Ping da %s a %s riuscito :)' % (str(datetime.today()), str(ip), str(args.HOST)))
                else:
                    print('%s: Ping da %s a %s non riuscito :(' % (str(datetime.today()), str(ip), str(args.HOST)))
            db.log(ip, args.HOST, pingable)
            sleep(args.INTERVAL - deadline)
        except KeyboardInterrupt:
            print('Esecuzione terminata, alla prossima :)')
            exit(0)


if __name__ == '__main__':
    main()
