#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys

dicc = {}

class SIPRegisterHandler(SocketServer.DatagramRequestHandler):
    """
    server class
    """   
    
    
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion ")
        self.wfile.write("SIP/1.0 200 OK\r\n\r\n")
        IP = self.client_address[0]
        Puerto = self.client_address[1]
        print "El cliente nos manda " + IP + (" ") + str(Puerto)
        # Leyendo línea a línea lo que nos envía el cliente
        Line = self.rfile.read()
        Line1 = Line.split()
        Line2 = Line1[1].split(":")
        Login = Line2[1]  
        dicc[Login] = IP
        while 1:
            #if, evalua expire (tiempo) 
            if Line1[3] == '0':
                if Login in dicc:
                    del dicc[Login]
                    self.wfile.write("SIP/1.0 200 OK\r\n\r\n")
                    break
            else:
                self.wfile.write("SIP/1.0 200 OK\r\n\r\n")
                break
            if not Line1:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", 7001), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
