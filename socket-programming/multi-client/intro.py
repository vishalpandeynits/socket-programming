# we had one server and one client and we connected both of them using a connection object. 
# But what if we wanted to connect to multiple clients? That is, what if we wanted to control more than 
# one computer from our single server?

# Right now if you want to have multiple clients you will have to create multiple servers. 
# But that is going to be costly and not every feasible.

# We will add the functionality of handling all the clients from one single server python file
# and build the multiple client support system.

# Working: Every time we accept a connection we get back two outputs. First is a connection object and 
# second is the address list. Using the connection object we can send commands to another computer and
# the address list contains the information like port and IP address. 

# So what we are going to do is that we are going to create an empty list or you can call it an 
# array of connection objects and address. And every time we connect to client we are going to 
# append it or add it to that list.

# Then we can loop through the list of clients connected to our server and choose the one that we want.

# So we have write a program that two tasks at once.
# 1) The first task is to listen and accept connections from other clients and store them in a list
# 2) The second task is sending commands to an already connected client

# This will be achievd by threading, threads are multitasking support systems. 
# first thread is going to listen and accept connections from other clients and the second thread 
# is going to handle  connection with an already connected client and send commands to them.

