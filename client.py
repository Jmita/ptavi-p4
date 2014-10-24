#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.
IP = sys.argv[1]
Puerto = sys.argv[2]

# Dirección IP del servidor.
SERVER = 'localhost'
PORT = 6001

# Contenido que vamos a enviar
LINE = sys.argv[3]

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((SERVER, PORT))

print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')
print IP
print Puerto

data = my_socket.recv(1024)

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
