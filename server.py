#!/usr/bin/env python3
# -*- python3 -*-

import socketserver

class PyCrafterServer:
    def parse_pkg(self, data):
        return data, data[0:1]

class PyCrafterConnHandler(socketserver.BaseRequestHandler):
    def __int__(self, *args, **kwargs):
        super(*args, **kwargs)
    def handle(self):
        data = self.request[0]
        socket = self.request[1]
        global game
        ndata, details = game.parse_pkg(data)
        print(f'Packet from {self.client_address[0]}: {details=}')
        socket.sendto(ndata, self.client_address)

if __name__ == '__main__':
    game = PyCrafterServer()
    with socketserver.ThreadingUDPServer(('0.0.0.0', 16382), PyCrafterConnHandler) as server: server.serve_forever()