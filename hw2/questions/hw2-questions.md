# Homework questions #
#### lukas_borges ####
Chapter 2 Review questions: R1, R4, R11, R14, R25
Chapter 2 Problems: P1, P4, P5, P10, P11, P14, P15

Chapter 3 Review questions: R1, R2, R14, R15, R17
Chapter 3 Problems: P1, P3, P26, P27, P31, P40

### Chapter 2: ###
#### Review questions: ####
R1.
|#|application|protocol|
|:-:|:-:|:-:|
|1|email|SMTP (simple mail transfer protocol)|
|2|file transfer|FTP (file transfer protocol)|
|3|web|HTTP (hyper text transfer protocol)|
|4|remote login|telnet|
|5|streaming services|RTP (real-time transport protocol)|

R4.
What happens in P2P is that every user is a client and a server at the same time. There is still a client-server relationship, but it is interchangeable.

R11.
HTTP, FTP, SMTP and POP3 all require reliable data transfer. TCP provides schemes for data loss and corruption, while UDP works with a best-effort policy. Basic implementations of UDP do not guarantee information integrity, so important for the listed protocols.

R14.
Easily done with Firefox developer tools (edit and resend header options)

R25.
1. Messaging
2. Real time communication (Skype)
3. File Sharing (torrent)
4. Distributed Computing

#### Problems ####
P1.
  |statement|answer|
  |:-:|:-:|
  |a|False|
  |b|True|
  |c|False|
  |d|False|
  |e|False|

P4.
a. http://gaia.cs.umass.edu/cs453/index.html
b. HTTP/1.1
c. `Connection:keep-alive`, persistent
d. ![gaia-ip](gaia-ip.png)   
`128.119.245.12`
e. Mozilla Firefox. Browser information is needed by the server in order to send different versions of the same object to different types of browsers.

P5.
a. Status code: `200 OK`.
`Date Tue 07 Mar 2008 12:39:45 GMT`
b. `Last-Modified: Sat, 10 Dec 2005 18:27:46 GMT`
c. `Content-Length: 3874` (bytes)
d. `<!doc`. Yes, according to `Connection: Keep-Alive`

P10.
**persistent HTTP:**
total time to receive all objects:
$$\left(\frac{200}{150}+T_p+\frac{200}{150}+T_p+\frac{200}{150}+T_p+\frac{100,000}{150}+T_p\right)+$$

$$\left(\frac{200}{150}+T_p+\frac{200}{150}+T_p+\frac{200}{150}+T_p+\frac{100,000}{150}+T_p \right)$$

$$=\left(\frac{200+200+200+100,000}{150}+4T_p\right)$$$$+\left(\frac{200+200+200+100,000}{15}+4T_p\right)$$

$$=\left(\frac{100,600}{150}+4T_p\right)+\left(\frac{100,600}{15}+4T_p\right)$$$$=(670+4T_p)+(6706+4T_p)$$$$=7377+8*T_p\,seconds$$

time needed:
$$\left(\frac{200}{150}+T_p+\frac{200}{150}+T_p+\frac{200}{150}+T_p+\frac{100,000}{150}+T_p\right)+$$ $$10*\left(\frac{200}{150}+T_p+\frac{100,000}{150}+T_p\right)$$ $$=\left(\frac{200+200+200+100,000}{150}+4T_p\right)+10*\left(\frac{200+100,000}{150}+2T_p\right)$$ $$=\left(\frac{100,600}{150}+4T_p\right)+10*\left(\frac{100,200}{150}+2T_p\right)$$ $$=(670+4T_p)+(6680+20T_p)$$$$=7350+24*T_p$$

propagation speed of the medium: $300*10^6m/sec$

$$T_p=\frac{10}{(300*10^6)}=0.03\,microseconds$$

For this case, persistent HTTP has no significant gain over non-persistent.

P11.
a. Yes. Bob's parallel connections will help him get pages quicker since he is using parallel instance of non-persistent HTTP while the others use non-persistent HTTP with parallel download.
b. Yes, even if all five users open five parallel instances of non-persistent HTTP. If Bob does not use parallel connections, he will get less bandwidth share. At this point, everyone (including Bob) should get equal bandwidth.

P14.
- SMTP uses period [`.`] to indicate end of message body.
- HTTP uses Content-Length header field to indicate end of message body.
HTTP cannot use the same method because there is no format for message body in HTTP.

P15.
MTA: Mail Transfer Agent.
|Mail received from|Mail received by|
|:-:|:-:|
|barmail.cs.umass.edu</br>[128.119.240.3]|cs.umass.edu</br>[8.13.1/8.12.6]|
|asusus-4b96</br>[localhost (127.0.0.1)]|barmail.cs.umass.edu|
|asusus-4b96</br>[58.88.21.177]|barmail.cs.umass.edu|
|[58.88.21.177]|lnbnd55.exchangeddd.com|

At `asusus-4b96[58.88.21.177]` the MTA does not report from where it receives the email (dishonest). If the mail is spam, only originator can be dishonest.

`asusus-4b96[58.88.21.177]` is the malicious host that generated spam.

---
### Chapter 3: ###
#### Review questions: ####

R1.
a.
Transport protocol (TP):
- Accept chunk of data, Destination's host address and port number (given by the sender)
- Maximum size of data: 1196 bytes
- Add a 4-byte header to each chunk
- Number of destinations included in header
- Destination host address and resulting segment are passed to the network layer by our TP.
- Network layer delivers segment to TP at destination.
- At destination, port number from segment is analyzed by the TP, which catches the data and sends it to the process with port number accordingly.

b.
Modified TP (mTP):
- Accept chunk of data, Destination's host address and port number (given by the sender)
- Maximum size of data: 1196 bytes
- Segment now has two header fields. One is used to specify source port and another to specify destination port.
- Add two 4-byte headers to each chunk. Include source port number and destination port number in two header fields.
- Destination host address, and resulting segment are passed to the network layer by mTCP
- Network layer delivers segment to mTCP at destination
- At destination, port number in the segment is examined by mTCP, which catches the data and sends it to the process with port number accordingly.
- It also gives the source port number to the application


c. No, transport layer only acts in the end systems.
R2.
R14.
R15.
R17.
