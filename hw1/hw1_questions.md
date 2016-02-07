# Homework 1 #
**student:** lukas_borges</br>
**panther ID:** 3008720

- **review questions:** R1, R2, R3, R12, R25, R28
- **problems:** P3, P4, P6, P8, P10, P13, P20, P25

Review questions:
---
**R1.** What is the difference between a host and an end system? List several different types of end systems. Is a Web server an end system?</br>

**Answer:** $Hosts=End\,Systems$  
- Smart phones
- Desktops
- Laptops
- TVs
- Email servers
- Web servers

Yes, since they serve user requests for _HTTP_ files.

**R2.** The word _protocol_ is often used to describe a diplomatic relations. How does Wikipedia describe diplomatic protocol?

**Answer:**
>"(...) set of rules, procedures, conventions and ceremonies that relate to relations between states. (...) Generally accepted system of international courtesy."

_Wikipedia_

**R3.** Why are standards important for protocols?

**Answer:** Protocols are important so that two devices know exactly what to actions to perform in order to send and receive data. If protocol is followed correctly, data transmission is more likely to work every time. Data communication is more reliable.

**R12.** What advantage does a circuit-switched network have over a packet-switched
network? What advantages does TDM have over FDM in a circuit-switched
network?

**Answer:** Circuit-switched network guarantees minimum end-to-end bandwidth. Packet-switched networks do not. In Frequency-division multiplexing, users occupy the frequency for as long as they use, making for less concurrent users and bandwidth waste.

**R13.** Suppose users share a 2 Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time. (See the discussion of statistical multiplexing in Section 1.3).

**a.** When circuit switching is used, how many users can be supported?

**Answer:** Two users. Each will request for half of the bandwidth.

**b.** For the remainder of this problem, suppose packet switching is used. Why will there be essentially no queuing delay before the link if two or fewer users transmit at the same time? Why will there be a queuing delay if three users transmit at the same time?

**Answer:** Each user requires 1Mbps when transmitting. If two or fewer users transmit at the same time, a maximum of 2Mbps will be required. Since the available bandwidth of the shared link is 2Mbps, there will be no queuing delay before the link. If three users transmit simultaneously, bandwidth required = 3Mbps which is more than the available of the link. There will be queuing delay.

**c.** Find the probability that a given user is transmitting:

**Answer**:
>"Each user transmits only 20 percent of the time"

$$p=0.2$$

**d.** Suppose now there are three users. Find the probability that at any given
time, all three users are transmitting simultaneously. Find the fraction of
time during which the queue grows.

**Answer:**

$$probability={{n}\choose{k}}p^n(1-p)^{n-k}$$

Where:</br>
$n$ is the number of users. $n=3$</br>
$k$ is the number of users transmitting simultaneously. $k=3$</br>
$p$ is the probability previously calculated.$p=0.2$

so for all users (3) transmitting simultaneously, we'll have:

$$probability={{3}\choose{3}}0.2^3(1-0.2)^{3-3} = 0.008$$

For this case; the fraction of time during which the queue grows is equal to the probability of having all three users transmitting at the same time; $0.008$

**R25.** Which layers in the Internet protocol stack does a router process? Which
layers does a link-layer switch process? Which layers does a host process?

**Answer:**
(Assuming 5 layers):
- Routers: layers 1 through 3.
- Link layer: switches process layers 1 through 2.
- Hosts: process all five layers.

**R28.** Suppose Alice and Bob are sending packets to each other over a computer network. Suppose Trudy positions herself in the network so that she can capture all the packets sent by Alice and send whatever she wants to Bob;
she can also capture all the packets sent by Bob and send whatever she wants to Alice. List some of the malicious things Trudy can do from this position.

**Answer:**
In this scenario, Trudy is the woman in the middle. She can:
- Listen (monitor and read the messages with)
- Jam (drop packets to and from either Bob or Alice)
- Playback attack (modify a message pretending to be either Alice or Bob)

**P3.**

a) For this case we have steady rate transmission, application has to run for a longer period of time. It is better to keep a connected for longer sessions then creating and disposing of a connection every time. A circuit-switched network would be fit.

b) If all traffic comes from the application described and the sum of the application data rates is less than the capacities of each and every link, the worst case would be some minimal queuing. No need for congestion control.

**P4.**

![title](C:\Users\Owner\Desktop\f-1-13.jpeg)

a) What is the maximum number of simultaneous connections that can be in
progress at any one time in this network?

![title](C:\Users\Owner\Desktop\p3-a.jpeg)

4 links, 4 connections each.

$$4*4=16\,connections$$

b) Suppose that all connections are between switches A and C. What is the
maximum number of simultaneous connections that can be in progress?

![title](C:\Users\Owner\Desktop\p3-b.jpeg)

All connections are between A and C.

`A-B-C` and `A-D-C`

Total of 8 simultaneous connections.

c) Suppose we want to make four connections between switches A and C,
and another four connections between switches B and D. Can we route
these calls through the four links to accommodate all eight connections?

![title](C:\Users\Owner\Desktop\p3-c.jpeg)

Yes:
- 4 connections $A \rightarrow D$
- 4 connections $B \rightarrow C$
- 2 connections $A \rightarrow B$
- 2 connections $A \leftarrow B$
- 2 connections $D \rightarrow C$
- 2 connections $D \leftarrow C$

**P6.**

**a.** Express the Propagation delay, $D_{prop}$ in terms of $m$ and $s$

**answer:** Distance over Speed cause the propagation delay:

$$D_{prop}(seconds)=\frac{m}{s}$$


**b.** Determine the transmission time of the packet, $D_{trans}$, in terms of $L$ and $R$.

**answer:**
$$D_{trans}(seconds)=\frac{L}{R}$$

**c.** Ignoring processing and queuing delays, obtain an expression for the end-
to-end delay.

**answer:**
$$D_{end-to-end}(seconds)=D_{prop}+D_{trans}=\frac{m}{s}+\frac{L}{R}$$

**d.** Suppose Host A begins to transmit the packet at time $t=0$. At time $t=d_{trans}$ ,
where is the last bit of the packet?

**answer**: $D_{trans}$= time to transmit one entire packet. So, at $t=D_{trans}$ an entire packet as just left A.

**e.** Suppose d prop is greater than d trans . At time $t=D_{trans}$ , where is the first bit of
the packet?

**answer:** The first bit of the packet is at distance $S * D_{trans}$ because the packet might leave the host while it is transmitted, but transmission delay is the weakest link. You can only go as fast as your weakest link.

**f.** Suppose $D_{prop}$ is less than $D_{trans}$. At time $t=D_{trans}$ , where is the first bit of
the packet?

**answer:** The first bit of the packet is at the destination. The time it takes for a bit to get from point A to B is less than the time is takes to transmit the whole packet.

**g.** Suppose $S=2.5*10^{8}$, $L=120\,bits$, and $R=56\,kbps$. Find the distance $m$
so that $D_{prop}$ equals $D_{trans}$.

**answer**:
$$D_{prop} = D_{trans}$$
$$\frac{m}{s} = \frac{L}{R}$$
$$m=s*\frac{L}{R}$$
$$m=(2.5*10^{8}meters/sec)(\frac{120\,bits}{56\, kbps})$$
$$remember: kilo=10^3$$
$$m=(2.5*10^{8}meters/sec)(\frac{120\,bits}{56*10^3\,bits/sec})$$
$$m=535714.28\,meters$$


**P8.**
**P10.**
**P13.**
**P20.**
**P25.**
