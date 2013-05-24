import nmap


class Host:
    def __init__(self, scanner, host):
        self.hostname = scanner[host].hostname()
        self.ip = host
        self.state = scanner[host].state()
        self.protocols = []
        for protocol in scanner[host].all_protocols():
            self.protocols.append([protocol, scanner[host][protocol].keys()])

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
