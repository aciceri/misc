#!/usr/bin/env python3
import argparse
import sqlite3
from datetime import datetime

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Semplice script per creare pagine HTML da i log d ping-logger')
    parser.add_argument('SRC', action='store', help='File *.db di SQLite sorgente')
    parser.add_argument('TARGET', action='store', help='File *.html della pagina di destinazione')
    args = parser.parse_args()

    conn = sqlite3.connect(args.SRC)
    cur = conn.cursor()
    cur.execute('SELECT * FROM log')
    rows = cur.fetchall()
    conn.close()

    page = '''
                <!doctype html>
                <html>
                    <head>
                        <meta charset="utf-8">
                        <title>Ping-logger DB</title>
                        <style>
                            table {
                                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                            }
                            td {
                                border: 1px solid #888;
                                padding: 3px 6px 3px 6px;
                                background-color: #CAFDFF;
                            }
                            th {
                                border: 1px solid #000;
                                padding: 3px 6px 3px 6px;
                                background-color: #6FC0F6;
                                font-weight: bold;
                            }
                        </style>
                    </head>
                    <body>
                        <table>
                            <tr>
                                <th>ID</th>
                                <th>DATA</th>
                                <th>SORGENTE</th>
                                <th>DESTINAZIONE</th>
                                <th>PING</th>
                            </tr>\n'''

    for row in rows:
        page += '<tr>\n'
        for column in row:
            page += '<td>%s</td>\n' % column
        page += '</tr>\n'

    page += '''
                        </table>
                    *Pagina generata automaticamente il %s
                    </body>
                </html>''' % str(datetime.today())

    pagefile = open(str(args.TARGET), 'w')
    pagefile.write(page)
    pagefile.close()
