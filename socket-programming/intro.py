# course --
# ip addresses
# ports and sockets
# direct and reverse

""" ip addresses """
# A unique string of numbers connected with each other by dots and which identifies a node(Computer) in network
# which is using the internet protocols to communicate over a network.
# range of numbers (0-255)

# public IP Addresses -- > It is provided by internet service providers
# private IP addresses --> provided by router/ (ipconfig/ ifconfig(mac/ubuntu))

# IP addresses are of two types 
# 1. static 2. Dynamic
# 1. static: static IP addresses never change (Server and websites)
# 2. dynamic IP addresses change whenever computer restarts( computers )

# IP addresses are not so specific but ports are very specific to a computer
# if IP address is your town then port number is exact house no. of your home.

""" Sockets """
#it opens a layer of communication among devices over TCP Protocol, sockets are bound
# to an IP address and a port number. socket is an endpoint of a two way communication link b/w two
# programs running on a network

""" Socket Commands"""
import socket
s = socket.socket() # creates a socket
host, port = 'ip address', '8080'
s.bind(host, port) # making socket connection with host and port. i.e opening a socket connection
s.send() # sends data using send function
s.listen() # other computer listens the message using this method
s.close() # closing the socket connection


# Direct and reverse connections

""" Direct Connections """
# intruder(Hacker) gets IP address of its victim, and get access of his computer
# he fails because of these reasons
# 1. IP addresses are dynamic, victims's computer kep changing its IP addresses and hence intruder loose connection after a small period of time.
# 2. Nowadays computers have firewalls which prevents an intruder to connect in this way

""" Reverse connections """
# intruder creates a python script which contains IP address of intruder, script runs and send connections to intruder
# intruder's IP is also dynamic, hence he somehow mimics his computer as server/website to make connections
# and access computer of his victim.

""" Server """
# remote computers which can host websites or store files
# it has static IP address
# we need internet to access this computer

# https://www.youtube.com/watch?v=DTHJTKM_m7c&list=PLhTjy8cBISErYuLZUvVOYsR1giva2payF&index=6