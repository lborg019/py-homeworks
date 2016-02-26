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
path = ("/home/luke/Desktop/Bobadilla/py-netcentric/hw2/Server/web/")

import os, time
# fileList = os.listdir("/home/luke/Desktop/Bobadilla/py-netcentric/hw2/Server/web")
fileList = os.listdir(path)
print(fileList)
# (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(path)
# print "last modified: %s" % time.ctime(mtime)

# file I have is older than file user has
# if(os.stat(path) > )
#    print("server file is older, no send")
# else:
#    print("client file is older, server should send")
# we print the file modified dates for testing purposes.



# output to console that server is listening 
print ("Magic happens on port 80... ")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print ("Received From Client: ", sentence)

    if(sentence[0:5]=="GET /"):
        print("user sent a GET\n")
        fileName = sentence[5:-2]
        fileName = fileName.partition(" ")[0]
        print("fileName:", fileName)
      
    # compare this with the dir file list.
    if fileName in fileList:
        print("file found")
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n')
        # send this file
        i = fileList.index(fileName)
        webFile = open(path+fileList[i], 'rb')
        l = webFile.read(1024)
        print(l)
        while(l):
            print 'Sending...'
            connectionSocket.send(l)
            l = webFile.read(1024)
        webFile.close()
            # connectionSocket.shutdown(socket.SHUT_WR)
    else:
        print("file not found")
        # send a 404
        connectionSocket.send('\n404 Not Found\n');
        # connectionSocket.send('HTTP/1.1 404 Not Found\nContent-Type: text/html\n\n')

    # send the file
    # connectionSocket.send(sentence)

    # output to console the sentence sent back to the client 
    # print ("Sent back to Client: ", capitalizedSentence)
	 
    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()


##########################################################################
