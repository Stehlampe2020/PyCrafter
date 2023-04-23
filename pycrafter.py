#!/usr/bin/env python3
# -*- python3 -*-

import socket, re

class PyCrafterClient:
    def __init__(self, hostaddr='localhost:16382'):
        self.__address = {}
        self.addr = hostaddr


    def send_packet(self, data, maxlen=None, timeout=None):
        maxlen = 1024 if maxlen==None else maxlen
        timeout = (3 if self.__is_local else 60) if timeout==None else timeout
        # SOCK_DGRAM is the socket type to use for UDP sockets
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, tuple(self.addr[key] for key in self.addr))
        sock.settimeout(timeout)
        return sock.recv(maxlen)

    __is_local = property(lambda self: True if re.match(r'^localhost$|^127\.0\.\d{1,2}\.\d{1,2}$|^127\.0\.0\.\d{1,2}$',
                                                        self.addr['host']) else False)

    def __parse_addr(self,addr):
        """Parses an address string in the format 'host:port' and stores it"""
        return self.__address.update({'host': addr.split(':')[0], 'port': int(addr.split(':')[1])})
    addr = property((lambda self: self.__address.copy()), __parse_addr)