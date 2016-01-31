# Lecture 4 #

## Layered Protocols ##
Pros
- Works like a blackbox, one can write applications without having to worry
about other layers
- Easy to maintain
- Easy to code
- Easy to update

Cons
- Defining which layer does what
- Possible redundancy
- One layer might affect another in a bad way because of the blackbox like usage

Protocols
- Set of rules, standard followed in order to establish communication
- All communication activities on the internet has to be governed by protocols
- Formal
- Order of messages sent and received
- Actions taken on message transmission

## ISO/OSI ##
Divided the internet protocol in seven layers:
1. Application
2. Presentation
3. Session
4. Transport
5. Network
6. Datalink (link)
7. Physical

File transfer, email, telnet, ACII, text, songs, establishing and manage
connections end-to-end communications, routing, addressing and two part
communications (link), how to transmit a signal(physical)

## TCP/IP ##

Did not follow precisely ISO/OSI

Only 5 layers:

1. Application
2. Transport
3. Internet Networking
4. Host-to-Host (Datalink)
5. Physical

|http|ftp|telnet|
|:-:|:-:|:-:|
|TCP|UCP|
|IP|
|Ethernet|WiFi|
|Coaxial|Fiber|Satellite|

New header is appended to the message for each layer. Not all layers are human
readable, check:
[Beej](http://beej.us/guide/bgnet/output/html/singlepage/bgnet.html)

A router for example, should only care about Network, Link, and Physical Layer.

Network Security:
-

- How can bad guys attack?
- How we can defend?
- How to design architecture immune to attacks?

> Internet not originally designed with security 'in mind'

_Read the history of the internet on the book_

_Read RFCS:_

- TCP/IP (RFC 801)
- DNS (RFC 1034)
- SMTP (RFC 821)


_Malware attacks_
- Virus
- Worms
- Trojan horses
- Spyware
- Rootkits
- Logic bombs
- Keyloggers

_Network attacks_
- DDOS (Denial of Service) (using botnets, syn flood attacks, requesting server's
resources until server becomes unavailable).
- DNS Poisoning
- Packet Sniffing
- Man in the Middle Attacks (solution cryptography)
- Playback Attacks
- IP Spoofing (solution end-point authentication, asymmetric encryption too)

Most security issues should be solved at the Application level because it's
more maleable than other layers

---
# Summary #
Up until now:

- Communication Media (UTP, wireless, fiber)
- Internet is a network of networks
- Performance metrics (delay, throughput, loss rate)
- Protocol Layers ISO/OSI (7 layers), TCP/IP (5 layers)
---

# Chapter 2 #
- Network application architectures
- HTTP, FTP, Email
- DNS
- P2P (apps)

*Client-server:*

Two computers. Information goes from one computer to another.
One computer starts, the other replies to it. (server is online all the time,
waiting for connections to be done).
- Server is always on
- Clients do not communicate with each other directly
- Ex: Netflix, Websites, Dropbox, Social Networks, Whatsapp.

*Peer 2 Peer:*

Every computer is a client and a server at the same time. One client can
download files / information from another client. As soon as a client acquires
information from somewhere, it also becomes an available server for this
information to be downloaded.

- Since clients are also servers, severs are not always online waiting.
- Hosts can communicate directly (peers)
- Examples: Kazaa, Bit Torrent, eMule, Kazaa, bitCoin)
- Advantages
- Highly scalable, performance, decentralized
- Highly symmetric traffic security
- Lack of incentive to share
