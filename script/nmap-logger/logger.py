import sqlite3


class Database:
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name

        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

        query = '''CREATE TABLE IF NOT EXISTS %s(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ip TEXT,
                    mac TEXT,
                    vendor TEXT,
                    hostname TEXT,
                    os TEXT,
                    ports TEXT)''' % self.table_name
        self.cur.execute(query)
        self.cur.close()

    def __repr__(self):
        return '<Db: %s, Table: %s>' % (self.db_name, self.table_name)

    def add_hosts(self, lhost):
        self.cur = self.conn.cursor()
        for host in lhost:
            ip = host.ip
            mac = host.mac
            vendor = host.vendor
            hostname = host.hostname
            os = host.os
            ports = str(host.ports)

            query = '''INSERT INTO %s(ip, mac, vendor, hostname, os, ports)
                        VALUES (?, ?, ?, ?, ?, ?)''' % self.table_name

            self.cur.execute(query, [ip, mac, vendor, hostname, os, ports])

        self.cur.close()
        self.conn.commit()

    def all_hosts(self):
        self.cur = self.conn.cursor()
        query = 'SELECT * FROM %s' % self.table_name
        self.cur.execute(query)

        hosts = []
        for host in self.cur:
            hosts.append(host)

        self.cur.close()
        return hosts
