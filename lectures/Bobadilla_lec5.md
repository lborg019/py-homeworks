# Lecture 5 #
See page 110 of the book

Conditional GET
- Every request sent to proxy server
- Proxy server caches object
- Only new objects are requested from server

### FTP ###
_File Transfer Protocol_

Uses two parallel connections:</br>
Control and Data.

- control connection is persistent
- data connections are non persistent:

  (new tcp connection for each file)
- stateful: server keeps track of users.

First establish connection between file and server. Every time you request an FTP server you need a new socket

`CWD ietf/ftpext/`

### SMTP ###
_Single mail transfer Protocol_

- User agent
- Mail agent
- SMTP

SMTP vs. HTTP

_differences_

SMTP:
- ASCII
- Mostly put

HTTP:
- Accepts binary objects
- Mostly pull

_similarities_

- both use tcp

**SMTP** delivery/storage to receive server

mail access protocol: retrieves mail from server
- POP3 post office version 3 (authorization, download)
- IMAP ...
