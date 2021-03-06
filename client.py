#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Dirección IP del servidor.
SERVER = sys.argv[1]
PORT = int(sys.argv[2])
REGISTER = sys.argv[3]
LOGIN = sys.argv[4]
EXPIRE = int(sys.argv[5])
LINE1 = ""
LINE2 = ""
# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

if sys.argv[3] == "REGISTER":
        LINE1 = ("REGISTER " + "sip:" + LOGIN + " " + 'SIP/2.0\r\n')
        LINE2 = (str(EXPIRE) + '\r\n\r\n')
my_socket.send(LINE1 + LINE2)
data = my_socket.recv(1024)

print "Enviando: "
print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
