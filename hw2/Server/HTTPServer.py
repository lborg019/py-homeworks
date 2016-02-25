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

import os
fileList = os.listdir("/home/luke/Desktop/Bobadilla/py-netcentric/hw2/Server/web")
print(fileList)

# output to console that server is listening 
print ("Magic happens on port 80... ")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print ("Received From Client: ", sentence)
	
    if(sentence[0]=='G' and
       sentence[1]=='E' and
       sentence[2]=='T' and
       sentence[3]=='/'):
        print("user sent a GET\n")
        webFile = sentence[4:]
        print("webfile:", webFile)

        # compare this with the dir file list.
        if webFile in fileList:
            print("file found")
        else:
            print("file not found")

    # send the file
    connectionSocket.send(sentence)

    # output to console the sentence sent back to the client 
    # print ("Sent back to Client: ", capitalizedSentence)
	 
    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()


##########################################################################
