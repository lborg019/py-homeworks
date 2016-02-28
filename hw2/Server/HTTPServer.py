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
# the following variables are going to have to be changed according to test enviro.:
path = ("/home/luke/Desktop/Bobadilla/py-netcentric/hw2/Server/web/")

import os, time
fileList = os.listdir(path)
print(fileList)

'''
send:
Last-Modified: Thu, 25 Feb 2016 22:59:38 GMT
Last-Modified: Sun Feb 28 07:42:30 2016
receive / parse:
If-Modified-Since: Sun Feb 28 00:34:45 2016
'''

# output to console that server is listening 
print ("Magic happens on port 80... ")

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    print ("Received From Client: ", sentence)

    if(sentence[0:5]=="GET /"):
        print("user sent a GET\n")
        fileName = sentence[5:-2] # trim GET
        fileName = fileName.partition(" ")[0] # GET file name (index.html)
        print("fileName:", fileName)
        if("If-Modified-Since:" not in sentence):
            print("Page is not cached, send")
        else:
            # we have to compare it:
            # continue
            print("Page is cached, check for 304")
    else:
        print("Server rejected HTTP method")
      
    # compare this with the dir file list.
    if fileName in fileList:
        print("file found")

        # element in list where file is at
        i = fileList.index(fileName)
        # full path with file name
        filePath = (path+fileList[i]) 

        # calculate last modified:
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(filePath)
        # print "Last-Modified: %s" % time.ctime(mtime)

        # send the file with Last-Modified header information:
        connectionSocket.send('HTTP/1.1 200 OK\nContent-Type: text/html\nLast-Modified: %s GMT\n\n' % time.ctime(mtime))

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
