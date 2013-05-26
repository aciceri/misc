#!/usr/bin/env python3

from logger import Database
from scanner import NmapScanner

# scanner = NmapScanner('192.168.1.*')
# l = scanner.scan()

db = Database('lan.db', 'hosts')
# db.add_hosts(l)

print(db.all_hosts())
