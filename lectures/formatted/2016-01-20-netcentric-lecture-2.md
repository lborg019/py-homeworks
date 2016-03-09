---
title: Netcentric Lecture 2

summary: recap, network performance, throughput and packet loss
---

Recap from last class:
end systems
packet vs circuit switches

Internet Service Provider (ISP)
End system (host) connect to the internet using and access ISP (residential,
commercial, university)

Reason why we don't have a Global ISP is the economic factor, we cannot have one
company owning everything. Tier 1 are ISP's that have their own connectivity,
routers and so on.

Network performance
- delay
- throughput
- losses (packet)

Delay Circuit Switching Networks:
How long will it take to send a file 640 Kilobits
from host A to host B.

- All links are 1.535 Mbps
- Each link is shared by 24 users
- 500 ms to establish end-to-end circuit

$${1.535 Mbps} /\,24\,users = 63.9 Kbps$$
$$640Kbs / 63.9 Kbps = ~10seconds$$
$$10 + 500 ms = 10s + 0.5 s$$

$$10.5s$$

##Types of delay:##

 - Processing Delay (decide where to send)
 - Queueing Delay (wait time behind other packets)
 - Transmission Delay (first bit to last)
 - Propagation Delay (time for a bit to travel)
 
##Transmission vs Propagation:##

 Cars travel 100km at 100km/h (constant) but have to stop for 12 seconds at
 a toll booth. For 10 cars we will take (10 * 12 = 120 seconds), 2 minutes on
 the booth; transmission delay. Plus 1 hour traveling (propagation delay).
 Both together is the total delay.

 $$ Transmission\,Delay: $$

 $$ D_{trans} = Packet Length (bits)\,/\,Link Bandwidth (R) $$

 $$ D_{node} = D_{proc} + D_{queue} + D_{trans} + D_{prop} $$

 $$ D_{prop} = distance (d)\,/\,signal speed (s) $$

Example:

 $$Packet\,length=1500\,Bytes$$
 $$Bandwidth=Ethernet\,10Mbps$$
 $$Distance=1km\,segment$$
 $$S=2*10^{8}$$


Transmission delay:

$$(1500 * 8) / 10Mbps = 1200 microseconds$$

Propagation delay:

$$(1000 / 2 * {10^8}m/s) = 5microseconds$$

We add both to get 1205 microseconds

### Throughput ###
> Only as fast as your weakest link, you shall be

_- Yoda_

`host1 - Rs - Switch - Rc - host2`

If Rs < Rc, we can only be as fast as Rs

If Rc < Rs, we can only be as fast as Rc

min{R1, R2, R3 .., Rn} {bottleneck}

### Packet Loss ###
 - Queueing (buffer overflow)
 - Bit error rate on the link
