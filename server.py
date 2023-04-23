#!/usr/bin/env python3
# -*- python3 -*-

import socketserver



class PyCrafterServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)

with socketserver.ThreadingUDPServer(('0.0.0.0', 16382), PyCrafterServer) as server: server.serve_forever()