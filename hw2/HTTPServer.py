##########################################################################
""" HTTPServer.py                                     
HTTPServer in Python
  
[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT: Lukas Borges                  
  COURSE NAME: [CNT4713] Netcentric Computing
  SEMESTER: Spring 2016                    
  DATE 02/15/2016                                         
  DESCRIPTION: This is an HTTP server in Python.
"""

from socket import *

# HTTP servers run on port 80
serverPort = 80

# create TCP welcoming socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))

# server begins listening for incoming TCP requests
serverSocket.listen(1)

# output to console that server is listening 
print ("Magic happens on port 80... ")

#while 1:
    # server waits for incoming requests; new socket created on return
connectionSocket, addr = serverSocket.accept()
 
while 1:
    # read a sentence of bytes from socket sent by the client
    sentence = connectionSocket.recv(1024)

    # output to console the sentence received from the client 
    print ("Received From Client: ", sentence)
	 
    # convert the sentence to upper case
    capitalizedSentence = sentence.upper()
	 
    # send back modified sentence over the TCP connection
    connectionSocket.send(capitalizedSentence)

    # output to console the sentence sent back to the client 
    print ("Sent back to Client: ", capitalizedSentence)
	 
    # close the TCP connection; the welcoming socket continues
    # connectionSocket.close()


##########################################################################
