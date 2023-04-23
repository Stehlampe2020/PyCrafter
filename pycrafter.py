#!/usr/bin/env python3
# -*- python3 -*-

import socket, re

class PyCrafterClient:
    def __init__(self, hostaddr='localhost:16382'):
        self.addr = {'host': hostaddr.split(':')[0], 'port': int(hostaddr.split(':')[1])}

    def send_packet(self, data, maxlen=1024, timeout=60):
        # SOCK_DGRAM is the socket type to use for UDP sockets
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, tuple(self.addr[key] for key in self.addr))
        sock.settimeout(timeout)
        return sock.recv(maxlen)

    __is_local = property(lambda self: True if re.match(r'^localhost$|^127\.0\.\d{1,2}\.\d{1,2}$|^127\.0\.0\.\d{1,2}$', self.addr('host')) else False)