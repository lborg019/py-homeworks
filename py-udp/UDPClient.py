from socket import *

# STUDENTS - replace with your server machine's name 
serverName = "127.0.0.1"

# STUDENTS - randomize your port number (use the same one in the server)         
# This port number in practice is often a "Well Known Number"  
serverPort = 12000

# create UDP socket
# Error in book? clientSocket = socket(socket.AF_INET, socket.SOCK_DGRAM)
#    corrected by  Amer 4-2013 
clientSocket = socket(AF_INET, SOCK_DGRAM)


# get user's input from keyboard
message = raw_input('Input lowercase sentence:')


# send user's sentence out socket; destination host and port number req'd

clientSocket.sendto(message,(serverName, serverPort))

print ("Sent to Make Upper Case Server running over UDP: ", message)

# receive modified sentence in all upper case letters from server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# output modified sentence and close the socket
print ("Received back from Server: ", modifiedMessage)

# close the UDP socket
clientSocket.close()
