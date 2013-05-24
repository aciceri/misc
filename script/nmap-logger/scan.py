import nmap


class Host:
    def __init__(self, scanner, host):
        self.hostname = scanner[host].hostname()
        self.ip = host
        self.state = scanner[host].state()
        if scanner[host].has_tcp(22) or scanner[host].has_tcp(23):
            self.ports = list(scanner[host]['tcp'].keys())
        else:
            self.ports = None

    def __repr__(self):
        return self.ip


class NmapScanner:
    def __init__(self, ip, port, parameters=''):
        self.nm = nmap.PortScanner()
        self.ip, self.port, self.parameters = ip, port, parameters

    def command_line(self):
        return self.nm.command_line()

    def scan(self):
        self.nm.scan(self.ip, self.port, self.parameters)
        lhost = []
        for host in self.nm.all_hosts():
            lhost.append(Host(self.nm, host))
        return lhost
