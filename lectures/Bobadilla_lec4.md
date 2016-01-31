# Lecture 4 #

Recap:

_Protocols_
- (ISO/OSI model, 7 layers)
- TCP/IP (5 layers)
- Security
- Client server / Peer 2 Peer

_Interprocess Communcation (IPC) on the same host_

`Lukezin$ ls | cat`
- OS provides message passing
- Interprocess communication on different hosts
- Network will provide message passing

http://google.com

http://google.com:80

* IP: 209.88.25.147:80
* DNS: Domain Name System
* Port: 80 = HTTP
* Port: 21 = FTP
* Port: 22 = SFTP

Number of ports:
$$ x^{16}\, = 65,535\,ports  $$

Ports (transport service)

---

#### Transport: ####

**TCP vs UDP**

_TCP: Transmission Control Protocol_

- Reliable data transfer
- Packet sequence # register
- Every packet is ACK (Acknowledged)
- Lost packet are transmitted
- May cause long delay
- Good for reliable and delay insensitive
- HTTP, FTP, Telnet

_UDP: User datagram Protocol_
- Unreliable
- Sequence # optional
- No ACK
- No retransmission
- Quick lossy
- Good for loss tolerant and delay sensitive
- Telephony, VOIP, Streaming multimedia

#### Security TCP ####
- TCP & UDP provide no encryption
- Passwords send over sockets remain in clear text

Regular:
|App|
|:-:|
|**TCP** (TCP socket)|
|**IP**|


SSL:
|App|
|:-:|
|**SSL** (SSL socket)|
|**SSL** sublayer|
|**TCP** socket|
|**TCP**|
|**IP**|

Provide:
- Encrypted TCP connection
- Delta integrity
- End point authentication

**SLL is at the Application Layer**

#### HTTP ####
_Hyper text transfer protocol_

[RFC:1945](https://tools.ietf.org/html/rfc1945)
[RFC:2616](https://www.ietf.org/rfc/rfc2616.txt)

- Client (IE, Netscape, Firefox, Opera, Chrome)
- HTTP Server (Nginx, Apache, MIS)
- Webpages (group of objects)
- URL http://cis.fiu.edu:80

HTTP server:

- Uses TCP
- Stateless (server does not remember previous history)
- non persistent (1.0): open new TCP connection get one object, close.
- persistent (1.1 onwards): open one TCP connection, get all objects, close
- webpages written in HTML

_Works on the basis of HTTP request / response between client and server._

HTTP Request:

`$ telnet users.cis.fiu.edu:80`</br>
`GET /~jabobadi/index.html`

`GET /~jabobadi/index.html/HTTP/1.1`</br>
`Host: cis.fiu.edu`</br>
`Connection: close`</br>
`User-agent: Mozilla/SO`</br>
`Accept-language: en`</br>

`Method SP`, `URL, SP, SP, CR, LF`</br>
`header_fieldname: value CR, LF`</br>
`header_fieldname: value CR, RF`</br>
(...)

ASCII message</br>
Entity Body \\r \\n

HTTP Response:

`HTTP/1.1 200: ok`</br>
`Connection: close`</br>
`Date: Monday, 25 January, 2015 18:00:`</br>
`Server: Apache/1.3.0 (Unix)`</br>
`Content_length: 6500`</br>
`Content_type: text/html`</br>

States codes:</br>
200: OK</br>
301: Moved permanently</br>
400: Bad request</br>
404: Not found</br>
403: Forbbiden</br>
505: Version not supported</br>

## Cookies ##

Allows servers to remember previous information</br>

1. Client sends usual request msg
2. Server creates ID (e.g. 1678)
3. Usual HTTP response sets Cookies
4. Following HTTP request message contains `cookie 1678`
5. HTTP response with cookie specific action

## Memcached ##

> Not everyone at a University needs to access the data stored in a specific server's disk.

Assumptions:</br>
- Institutional network: 100Mbps
- Link to Origin servers: 15 Mbps
- Average object size: 1 Mbits
- Average request: every 15 seconds
- Access link role

RTT (round trip time)
time for small packet</br>
to go from Client to Server and back.

LAN utilization (traffic intensity):
$$ \frac{\frac{15\,requests}{second} *\frac{1Megabyte}{1Request}}{100Mbps} = 0.15 $$

Across link utilization:
$$ \frac{\frac{15 requests}{second} * \frac{1Mbit}{request}}{15Mbps} = 1 $$

$$ Total\,delay = internet\,delay + access\,delay + lan\,delay $$
$$ = 2sec + access\,delay+LAN\,delay $$
$$ (= 2sec + minutes + users)$$

If I increase 15Mbps to 100Mbps = 2.1s (expensive solution)

Average queueing delay is an exponential curve with a vertical asymptote at 1, where:
$$ \frac{La}{R} $$

So we will use cache:
Cache: (0.4, 0.7)</br>
Hit rate: 0.4 request satisfied at cache</br>
0.6 at the origin</br>
0.6 traffic intensity access link recluses</br>
0.6 corresponds to mili seconds
0.6 delay from origin server) + 0.4 (delay at cache)
0.6 * (2.01) + 0.4 (milisecond) = approx. 1.2 seconds
