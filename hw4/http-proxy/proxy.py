""" proxy.py
HTTP-ProxyServer in Python

STUDENT: Lukas Borges
COURSE NAME: [CNT 4713] Netcentric Computing
SEMESTER: Spring 2016
DATE: 04/08/2016
DESCRIPTION: This is a proxy HTTP server in python
"""

from socket import * 
import os, sys

if len(sys.argv) <= 1: 
    print 'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP  Address Of Proxy Server' 
    sys.exit(2) 

# Create a server socket, bind it to a port and start listening 
tcpSerSock = socket(AF_INET, SOCK_STREAM) 

# Fill in start.
serverPort = 8888 #port proxy server is going to run on
tcpSerSock.bind(("",serverPort)) #bind port (8888)
tcpSerSock.listen(4); #server listens for incoming TCP req
flag = 0
# Fill in end. 
while 1: 
    # Start receiving data from the client 
    print 'Ready to serve...' 
    tcpCliSock, addr = tcpSerSock.accept() 
    print 'Received a connection from:', addr 
    message = tcpCliSock.recv(1024)
    print message

    if not message:
        flag = 1
        print 'Received an empty string'
    else:
        # Extract the filename from the given message 
        print message.split()[1] 
        filename = message.split()[1].partition("/")[2] 
        print filename 
        fileExist = "false" 
        filetouse = "/" + filename 
        print filetouse 
    
    try: # Check wether the file exist in the cache 
        f = open(filetouse[1:], "r")                       
        outputdata = f.readlines()                         
        fileExist = "true" 
        # ProxyServer finds a cache hit and generates a response message 
        tcpCliSock.send("HTTP/1.0 200 OK\r\n")             
        tcpCliSock.send("Content-Type:text/html\r\n") 
        # Fill in start.
        for data in outputdata:
            tcpCliSock.send(data)
        # Fill in end.
        print 'Read from cache'      
    except IOError: # Error handling for file not found in cache 
        if fileExist == "false":  
            c = socket(AF_INET, SOCK_STREAM) # Create a socket on the proxyserver 
            hostn = filename.replace("www.","",1) # google.com

            """
            import socket
            dest = socket.gethostbyname(hostn)
            print dest
            """
            print hostn
            try: 
                # Connect to the socket to port 80 
                # Fill in start.
                c.connect((hostn, 80))
                print "Proxy connected to webserver's port 80"
                # Fill in end.
                # Create a temporary file on this socket and ask port 80 for
                # the file requested by the client 
                fileobj = c.makefile('r', 0)
                fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")   

                # Read the response into buffer 
                # Fill in start. 
                buffer = fileobj.readlines()
                # Fill in end.

                # Create a new file in the cache for the requested file.  
                # Also send the response in the buffer to client socket and the 
                # corresponding file in the cache 
                tmpFile = open("./"+filename,"wb")   
                # Fill in start. 
                for data in buffer:
                    tmpFile.write(data)
                    tcpCliSock.send(data)
                # Fill in end.
            except: 
                print "Illegal request" 
        else: # HTTP response message for file not found 
            # Fill in start. 
            print "404: File not found"
            # Fill in end.
    tcpCliSock.close() # Close the client and the server sockets     
# Fill in start. 
# Fill in end. 
