from os import popen
from xml.etree import ElementTree


class Host:
    def __init__(self, ip, mac, vendor, hostname, os, ports):
        self.ip = ip
        self.mac = mac
        self.vendor = vendor
        self.hostname = hostname
        self.os = os
        self.ports = ports

    def __repr__(self):
        return self.ip


class NmapScanner:
    def __init__(self, ip_range, port_range='', extra_parameters=''):
        self.ip_range = ip_range
        self.port_range = port_range
        self.extra_parameters = extra_parameters

    def __repr__(self):
        return self.ip_range

    def scan(self):
        xml_output = popen('nmap -oX - -O 192.168.1.0/29').read()
        root = ElementTree.fromstring(xml_output)

        self.command_line = root.get('args')
        self.nmap_version = root.get('version')
        self.lhost = []

        for host in root.findall('host'):
            ip = host.find('./address[@addrtype="ipv4"]').get('addr')
            mac = host.find('./address[@addrtype="mac"]').get('addr')
            vendor = host.find('./address[@addrtype="mac"]').get('vendor')
            hostname = host.find('./hostnames').text
            if host.find('./os/osmatch') is not None:
                os = host.find('./os/osmatch').get('name')
            else:
                os = ''

            ports = {}
            for port in host.findall('./os/portused'):
                ports[port.get('portid')] = port.get('state')

            self.lhost.append(Host(ip, mac, vendor, hostname, os, ports))

        return self.lhost
