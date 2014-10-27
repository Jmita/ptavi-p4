#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco
en UDP simple
"""

import SocketServer
import sys
import time

dicc = {}


class SIPRegisterHandler(SocketServer.DatagramRequestHandler):

    """
    server class
    """

    def register2file(self):
        fichero = open("registered.txt", "w")
        fichero.write('user' + "\t" + 'IP' + "\t" + 'Expires' + '\n')
        for clave, valor in dicc.items():
            Hora = valor.split(",")[-1]
            IP = valor.split(",")[0]
            x = time.gmtime(float(Hora))
            Time_actual = time.strftime('%Y­%m­%d %H:%M:%S', x)
            fichero.write(clave + "\t" + IP + "\t" + Time_actual + "\n")

    def handle(self):
        # Hora
        Hora_recibida = time.time()
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write("Hemos recibido tu peticion ")
        self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
        IP = self.client_address[0]
        Puerto = self.client_address[1]
        Line = self.rfile.read()
        print "El cliente nos manda " + Line
        # Leyendo línea a línea lo que nos envía el cliente
        Line1 = Line.split()
        Line2 = Line1[1].split(":")
        Login = Line2[1]
        Time = Line1[3]
        dicc[Login] = IP
        while 1:
            # If, evalua expire (tiempo)
            if Time == '0':
                if Login in dicc:
                    print "eyy"
                    del dicc[Login]
                    self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
                    self.register2file()
                    break
            else:
                Hora_actual = Hora_recibida + int(Time)
                dicc[Login] = IP + ',' + str(Hora_actual)
                self.wfile.write("SIP/2.0 200 OK\r\n\r\n")
                self.register2file()
                break
            if not Line1:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", 7001), SIPRegisterHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
