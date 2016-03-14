---
title: Netcentric Lecture 6

summary: Domain Name System (DNS), Transport services and protocols.
---
**Domain Name System (DNS)**
- host, router
- host-name to IP address

_example:_<br>
name: http://www.fiu.edu<br>
address: 131.94.74.137

- hierarchy of many servers
- App layer protocol to resolve names
(name/address translation)
- Core Internet functions as a ... protocol


Why not a centralized database for DNS?

- Single point of failure
- Robustness
- Proximity (delay)
- Traffic volume
- Not scalable

Host name to IP address translator

- Load distribution (load balancer)
- Many IP address to Host aliasing
- Mail Servers

|ROOT DNS SERVER level||||
|:-:|:-:|:-:|:-:|
|top level domains:|.com DNS server|.org DNS server|.edu DNS server|
|authorative DNS servers:|amazon.com DNS server|pbd.org|fiu.edu|

Root DNS servers:

- Top level domains: .com, .org, .net,
- Authorative DNS server: .uk, .fr, .ca, .gp, amazon.com (any company with a publicly available host)

Local DNS name server

- Each ISP provider has one default name server.

Local DNS Servers will connect you to the correct server, figure out which server has the information and pass that to the computer (middle man).
Local DNS server can keep information cached.

"I do not know, ask this server"

DNS caching: once the server learns the mappings, it caches it.

-- TTL (Timeout for entries)

Record structure: name, value, type, TTL (when the resource should be moved from caches)

||hostname|IP|
|:-:|:-:|:-:|
|Type-A|relay.bar.foo.com|145.37.93.126, A|
|Type-NS|foo.com|dns.foo.com, NS|
|Type-CNAME|foo.com|relay.bar.foo.com, CNAME|
|Type-MX|foo.com|mail.bar.foo.com, MX|

Inserting record into DNS

If we want to register a new domain: "mywebsite.com"

TLD:

- (mywebsite.com, dns.mywebsite.com, NS)
- (dns.mywebsite.com, 212.212.212.1, A)

Authorative DNS

- (www.mywebsite.com, ..., A)
- (website.com, mail.mywebsite.com, MX)

System has been robust, not many attacks at the Root Level.
DNS poisoning does exist though. DNS servers keep tables matching IPs with human readable URL's. Changing those could hinder access.

_Client-Server Scenario_

time to upload one copy:
$$\frac{F\,bits}{Us\,bits}\cdot n$$

where: $$F=file\,size$$<br>
$$n=number\,of\,copies$$<br>
$$Us=upload\,speed$$

- Each client must download a copy
- $$D_{min}$$ is the minimum download capacity

$$\displaystyle\frac{F}{D_{min}},$$

$$\displaystyle D_{c-s}\geq max \Bigg\{ \frac{N\,F}{U_{speed}}, \frac{F}{D_{min}} \Bigg\}$$

_Peer-to-peer Scenario_

$$D_{p2p}\geq max\Bigg\{\frac{F}{U_{speed}},\frac{F}{D_{min}},\frac{NF}{U_{speed}+\sum_{i=1}^{n} U_{i}}\Bigg\}$$

On a cartesian graph $$y$$=download time and $$x$$ =number of hosts:

client server: $$y=x$$ line

peer to peer: $$y=log_{2}(x)$$

![p2p-graph]({{ site.baseurl }}/img/lectures/p2p-graph.png)

---

# Chapter 3 #
_Transport services and protocols:_

Provide logical communication between app processes running on different hosts.

Transport runs in end systems:

- send side: break messages into segments, pass to the network
- receive side; reassemble segments into messages, pass it to the application layer.

Transport vs Network:

- network layer: logical communication between hosts
- transport layer: logical communication between processes, enhances network layer.

Example:

- Host: houses
- Processes: kids
- App messages: letters in envelopes

Transport Protocol demuxes to the kids in the host.
Network layer: postal service

_read TCP and UDP section_

UDP: Unreliable, unordered

- extension to TCP, no additions

TCP: Reliable, in order

- flow control
- congestion control

