##########################################################################
"""  HTTPClient.py                                     
 HTTPServer in Python

[STUDENTS FILL IN THE ITEMS BELOW]  
  STUDENT: Lukas Borges 
  COURSE NAME: [CNT4713] Netcentric Computing
  SEMESTER: Spring 2016
  DATE: 02/15/2016                        
  DESCRIPTION: This is an HTTP Client in Python
"""

"""
lsof -i :80     find the process
kill -9 <pID>   kill the process

keep connection running:
https://docs.python.org/release/2.7.10/howto/sockets.html

Algorithm:
    send a string (GET), program the conditional GET
    get the response
    get the HTML, CSS and JS files (TCP File transfer)
    program should work with telnet and browser, only server
    program should check the modified date of the last file

"""

from socket import *

# STUDENTS - replace your server machine's name 
serverName = "localhost"

# STUDENTS - you should randomize your port number.         
# This port number in practice is often a "Well Known Number"  
serverPort = 80

# create TCP socket on client to use for connecting to remote
# server.  Indicate the server's remote listening port
# Error in textbook?   socket(socket.AF_INET, socket.SOCK_STREAM)  Amer 4-2013 
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName,serverPort))

while 1:
    # interactively get user's line to be converted to upper case
    # authors' use of raw_input changed to input for Python 3  Amer 4-2013
    sentence = raw_input('Input lowercase sentence:') # changed it from raw_input

    # send the user's line over the TCP connection
    # No need to specify server name, port
    # sentence casted to bytes for Python 3  Amer 4-2013

    # modified to run on windows:
    # clientSocket.send(sentence)
    clientSocket.sendto(sentence.encode(),(serverName, serverPort))

    #output to console what is sent to the server
    print("Sent to Make Upper Case Server: ", sentence)

    # get user's line back from server having been modified by the server
    modifiedSentence = clientSocket.recv(1024)

    # output the modified user's line 
    print("Received from Make Upper Case Server: ", modifiedSentence)

# close the TCP connection
# clientSocket.close()
