import threading
from queue import Queue
import time
import sys
import socket

THREADS = 2
JOB_NUMBER = [1, 2]
all_connections = []
all_address = []

def create_socket():
    try:
        global host
        global port 
        global s
        host = ""
        port = 9999
        s = socket.socket()
        return s
    except socket.error as err:
        assert str(err)

# socket is just a connection, you need to tell the socket
# where it has to be connected to exchange data.
def bind_socket():
    try:
        global host
        global port
        global s 

        print(f"Binding the port {str(port)}")
        s.bind((host, port))
        s.listen(5) # no. of bad requests socket can tolerate
    except socket.error as ex:
        print(f"Failure while binding the connection. {str(ex)} Retrying ....")
        bind_socket() # if connection fails, try again to bind socket

# handling connections from multiple clients and saving to a list
# closing previous connections when server.py is restarted
def socket_accept():
    for con in all_connections:
        con.close()
    
    all_connections.clear()
    all_address.clear()

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1) # it prevents timeout for a client to happen otherwise if client is idle, connection will be closed

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established with ", *address)

        except:
            print("error while accepting connections")