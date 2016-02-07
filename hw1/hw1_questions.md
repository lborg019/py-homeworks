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

![title](/Users/Luke/Desktop/f-1-13.jpeg)

a) What is the maximum number of simultaneous connections that can be in
progress at any one time in this network?

![title](/Users/Luke/Desktop/p3-a.jpeg)

4 links, 4 connections each.

$$4*4=16\,connections$$

b) Suppose that all connections are between switches A and C. What is the
maximum number of simultaneous connections that can be in progress?

![title](/Users/Luke/Desktop/p3-b.jpeg)

All connections are between A and C.

`A-B-C` and `A-D-C`

Total of 8 simultaneous connections.

c) Suppose we want to make four connections between switches A and C,
and another four connections between switches B and D. Can we route
these calls through the four links to accommodate all eight connections?

![title](/Users/Luke/Desktop/p3-c.jpeg)

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
$D_{prop} = D_{trans}$

$\frac{m}{s} = \frac{L}{R}$

$m=s*\frac{L}{R}$

$m=(2.5*10^{8}meters/sec)(\frac{120\,bits}{56\, kbps})$

$remember: kilo=10^3$

$m=(2.5*10^{8}meters/sec)(\frac{120\,bits}{56*10^3\,bits/sec})$

$m=535714.28\,meters$


**P8.**

**a.** When circuit switching is used, how many users can be supported?

**answer:** 20 users


**b.** For the remainder of this problem, suppose packet switching is used. Find
the probability that a given user is transmitting.

**answer:** $p=0.1$


**c.** Suppose there are 120 users. Find the probability that at any given time,
exactly n users are transmitting simultaneously. (Hint: Use the binomial
distribution.)

**answer:** $${120 \choose n}p^n(1-p)^{120-n}$$

**d.** Find the probability that there are 21 or more users transmitting
simultaneously

**answer:**
$$1-\sum_{n=0}^{20}{120 \choose n}p^n(1-p)^{120-n}$$
Central limit theorem to approximate.
$X_i$ is the independent random variables. $P(x_i=1)=p$

$$P("21\,users\,or\,more")=1-P(\sum_{j=1}^{120}X_j\leqslant21)$$

$$P(\sum_{j=1}^{120}X_j\leqslant21)=P\left(\frac{\sum_{j=1}^{120}X_j-12}{\sqrt[]{120*0.1*0.9}}\leqslant\frac{9}{\sqrt[]{120*0.1*0.9}}\right)$$

$$\approx P\left(Z\leqslant\frac{9}{3.286}\right)=P(Z\leqslant2.74)=0.997$$

$P$(21 or more users)$\approx0.003$

**P10.**

**Part 1:**
Assuming no queuing delays, in terms of $d_{i}$, $s_{i}$, $R_{i}$,
$(i=1,2,3)$, and $L$, what is the total delay ($D_{end-to-end}$) for the packet?

**answer:**
$length:d_{i}$</br>
$propagation\,speed: s_{i}$</br>
$transmission\,rate: R_{i}$</br>
$total_{end-to-end}\,delay: L$</br>

$$(propagation delay[seconds])Pd_{i}=\frac{d_{i}(meters)}{s_{i}(meters/sec)}$$

$$(transmission\,time[seconds])Tt_{i}=\frac{L(bits/packet)}{R_{i}(bits/sec)}$$

Packet-switch delay: $d_{proci}$ for $i=1,2,3$

$D_{end-to-end}=\sum(Pd_{i}+Tt_{i}+d_{proci})$
$$D_{end-to-end}=\sum_{i=1}^{3}((\frac{d_i}{s_i})+\frac{L}{R_i}+d_{proci})$$

**Part 2:** Suppose
now the packet is 1,500 bytes, the propagation speed on all three links is 2.5 ·
10 8 m/s, the transmission rates of all three links are 2 Mbps, the packet switch
processing delay is 3 msec, the length of the first link is 5,000 km, the length
of the second link is 4,000 km, and the length of the last link is 1,000 km. For
these values, what is the end-to-end delay?

**answer:**
$L=1500bytes$</br>
$s=2.5*10^8m/s$</br>
$R=2Mbps=2097152bps$</br>
$d_{proc}=3ms$</br>
$dist_1=5000km$</br>
$dist_2=4000km$</br>
$dist_3=1000km$</br>

$$D_{end-to-end}=\sum_{i=1}^3((\frac{d_{i}}{s})+(\frac{L}{R})+d_{proc})$$

$$=[(\frac{dist_1}{s})+(\frac{L}{R})+(d_{proc})]+[(\frac{dist_2}{s})+(\frac{L}{R})+(d_{proc})]+[(\frac{dist_3}{s})+(\frac{L}{R})+(d_{proc})]$$

$$=(\frac{dist_1}{s})+(\frac{dist_2}{s})+(\frac{dist_3}{s})+3(d_{proc})+3(\frac{L}{R})$$

$$=(\frac{5000km}{2.5*10^8m/s})+(\frac{4000km}{2.5*10^8m/s})+(\frac{1000km}{2.5*10^8m/s})+3(3ms)+3(\frac{1500bytes}{2097152bps})$$

$$=(0.02ms)+(0.004ms)+(0.016ms)+3(0.71ms)+3(3ms)$$
$$=11.314ms$$

Reference [link](http://www.endmemo.com/sconvert/bpsmbps.php)

**P13.**

**answer a.** First packet has queuing delay=0.</br>Second packet has delay: $1*\frac{L}{R}$seconds</br>
$n^{th}$ packet has delay: $(n-1)\frac{L}{R}$ seconds

Average delay for $N$ packets:

$$\left(\frac{ \frac{L}{R}+2\frac{L}{R}+...+(N-1)\frac{L}{R}}{N}\right)$$

$$=\frac{L}{RN} * (1+2+...+(N-1))$$

$$=\frac{L}{RN} * \frac{N(N-1)}{2}$$

$$=\frac{LN(N-1)}{2RN}$$

$$=\frac{(N-1)L}{2R}$$

**answer b.**

$$\frac{1}{n}\sum_{n=1}^N(n-1)\frac{L}{R}$$

which unwraps into:

$$\frac{L}{R}\frac{1}{N}\sum_{n=0}^{N-1}n=\frac{L}{R}\frac{1}{N}\frac{(N-1)N}{2}=\frac{L}{R}\frac{(N-1)}{2}$$

**P20.**

![title](/Users/Luke/Desktop/f-1-20-b.jpg)

**answer:** $Throughput=min[R_s, R_c, \frac{R}{M}]$

**P25.**

**answer a.**

$$R=2Mbps$$

$$2*10^6(bits/sec)* \frac{2000*10^3m}{2.5*10^8bits}=1.6*10^5bits$$

_160,000 bits_

**answer b.**

$$min(BDP, 800000)=BDP.$$
$$1.6*10^5bits$$

_160,000 bits_

**answer c.** Bandwidth-delay product of a link = maximum amount of bits that can be fit into the link

**answer d.**

$$\frac{20000*10^3m}{1.6*10^5bits}=125m$$

$$125\,meters>football\,field$$

**answer e.**

$$\frac{m}{\frac{m}{s}* R}=\frac{s}{R}$$

#### this homework is powered by $\KaTeX$
