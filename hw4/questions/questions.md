2.[30 points] Complete the following Wireshark labs:
http://www-net.cs.umass.edu/wireshark-labs/Wireshark_IP_v6.0.pdf
http://www-net.cs.umass.edu/wireshark-labs/Wireshark_ICMP_v6.0.pdf
http://www-net.cs.umass.edu/wireshark-labs/Wireshark_Ethernet_ARP_v6.01.pdf

3. [5 points] Read carefully section 5.7 "Retrospective: A Day in the Life of a Web Page Request" (Page 495) and make a list of all the protocols involved in the scenario described in the section: "a student, Bob, connects a laptop to his school’s Ethernet switch and downloads a web page (say the home page of www.google.com)".


4. [30 points] Give an answer for the following questions:
Chapter 5 Review Questions R3,R5,R8,R9,R14
Chapter 5 Problems: P1, P5, P11, P31, P32

# Protocol List: #

# Review Questions: #
_Chapter 5:_
<s>R3</s>, <s>R5</s>, <s>R8</s>, <s>R9</s>, <s>R14</s>

**R3:**
- **Framing:** Each datagram received from the network layer is encapsulated in a frame by the Link-layer.
- **Link Access:** Link Layer specifies MAC protocol required for successful connection in case of multiple nodes using the same link.
- **Reliable Delivery:** Link-layer is responsible for having the network-layer datagram is delivered across the link without any errors.
- **Error detection and correction:** Link layer protocol is equipped with bit error detection potentially present in the frame. Link-layer is also able to correct such errors.

_Corresponding IP services:_
Framing, Link Access and Error detection and correction.

_Corresponding TCP services:_
Framing, Link Access, Reliable Delivery, Error detection and correction.

**R5:**
**Slotted ALOHA:**
1. Slotted ALOHA has a node to transmit continuously at maximum rate, all the time.
2. In slotted ALOHAm each of the nodes has a $\frac{R}{Mbps}$ throughput. Average transmission rate of $\frac{R}{M}$ for each node.
3. Each node detects collision and decides when to transmit independently (no clock). Partially decentralized.
4. Simple, efficient.

**Token Passing:**
1. Always has a node to transmit at $R$bps rate.
2. Each node has throughput of $\frac{R}{Mbps}$. Average transmission rate of $\frac{R}{M}$ for each node.
3. Decentralized.
4. Simple, inexpensive.

**R8:**
In token-ring, a node can only send the frame when it has the token. In a large lan perimeter, each node will have to wait longer for its turn. Each node has to wait until its frame propagates around the entire ring before passing the token to the next node. Therefore, token-ring is an inefficient protocol when the LAN has a large perimeter.



# Problems: #
P1, P5, P11, P31, P32

**P1:**
Bit pattern: `1110 0110 1001 1101`
Parity: Even

| Bits| Parity (row) |
| :-   | :- |
| 1110 | 1 |
| 0110 | 0 |
| 1001 | 0 |
| 1101 | 1 |

We organize the bits from last table in columns and calculate the parity vertically:

| a | b | c | d |
| :-|:- |:- |:- |
| 1 | 1 | 1 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 0 | 1 |
|parity: 1 |parity: 1 |parity: 0 |parity: 0 |

Resulting in:
`1100`, which has horizontal (row) parity of: `0`

For the final result, we interleave the original data with its row parity.

`1110 1 0110 0 1001 0 1101 1`

Now we add the resulting value from the column parity calculation and again interleave with its row parity, leaving us with the final result of:

`1110 1 0110 0 1001 0 1101 1 1100 0`

**P5:**

$G=10011$
$D=1010101010$

We start by rewriting $G$ in terms of a polynomial expression:

$=(x^4\cdot 1)+(x^3\cdot 0)+(x^2 \cdot 0)+(x^1 \cdot 1)+(x^0\cdot 1)$<br>
$=(x^4+x^1+1)$

$G(x)=x^4+x^1+1$
The degree of the expression is 4, therefore our $r=4$
So, we will append $4$ `0s` to $D$

$D=1010101010$
$D+r=1010101010\,\,0000$

To calculate the value of R:
$$R=\frac{D+r}{G}$$

- CRC operation used for division is the XOR operator
- XOR operations results in 0 when both the bits are equal; 1 otherwise.
We divide $$\frac{10101010100000}{10011}$$

![p5.png](p5.png)

$R=0100$

**P11:**
number of packets at each node $= \infty$
probability required by each node to transmit packet in each slot is $p$
Assuming probability of success $= p$
number of failures $q=1-p$

_Probability of A succeeding in a slot is:_
$P(A)=(A\,transmits)(B\, not)(C\, not)(D\, not)$
$P(A)=p\cdot (1-p)\cdot (1-p)\cdot (1-p)$
$P(A)=p(1-p)^3$

**a:**
_Probability of A succeeding for the first time in slot 5:_
$P=P(A\, fails\, slot\, 1)\cdot(A\, fails\,slot\,2)\cdot (A\,fails\,slot\,3)\cdot(A\,succeeds\,slot\,5)$
$P=(1-P(A))^4\cdot P(A)$
$P=(1-(p(1-p)^3))^4\cdot p(1-p)^3$

**b:**
_Probability of A succeeding in a slot 4:_
$P(A)=(A\,not)(A\,not)(A\,not)(A\,succeeds)$
$P(A)=p\cdot (1-p)\cdot (1-p)\cdot (1-p)$
$P(A)=p\cdot(1-p)^3$

Similarly;
_Probability of B succeeding in slot 4:_
$P(B)=p\cdot (1-p)^3$

_Probability of C succeeding in slot 4:_
$P(C)=p\cdot (1-p)^3$

_Probability of D succeeding in slot 4:_
$P(C)=p\cdot (1-p)^3$

**b.** _Probability of any node succeeding in slot 4:_
Since the nodes are mutually exclusive;
$=[p\cdot(1-p)^3]+[p\cdot(1-p)^3]+[p\cdot(1-p)^3]+[p\cdot(1-p)^3]$
$=4\cdot p \cdot (1-p)^3$

**c.**

_Probability that any node succeed in a slot:_
$4p(1-p)^3$

_Probability that any node does not succeed in a slot:_
$1-4p(1-p)^3$

_Probability of success is first for slot 3 is:_
$P=P(fails\,first)\cdot P(fails\, second)\cdot P(success\, third)$
$P=(1-(4p(1-p)^3))\cdot (1-(4p(1-p)^3))\cdot (4p(1-p)^3)$
$P=(1-(4p(1-p)^3))^2(4p(1-p)^3)$
$P=1-(4p(1-p)^3)^2(4p(1-p)^3)$

**d.**
_Efficiency of the 4 node system:_

Efficiency can be described as the probability of any node succeeding in a slot:
$P=4p(1-p)^3$

**P31:**

1. Connect PC to the network using Ethernet Interface
2. DHCP provides an IP address to the PC (steps follow):
1.. PC creates an IP datagram with dest: `255.255.255.255` in DHCP's server discovery step.
2.. Datagram is placed in an Ethernet frame, sent and the router broadcasts it to the network.
3.. DHCP server residing in the DHCP provides the PC with a list of addresses of the routes with one hop, as well as subnet mask and subnet where the PC resides. Also a DNS server if it exists.
3. The ARP cache for the PC is starts empty. ARP protocol is used by the PC in order to obtain MAC address of first-hop routers and local DNS server.
4. PC first obtains IP address of the webpage requested. If local DNS server does not have it, DNS protocol is used so the computer can obtain the appropriate IP address.
5. Once this IP is obtained, PC will send an HTTP request using the first-hop router.
6. The PC then sends the Ethernet frames to the router.
7. The PC sends Ethernet frames destined to the router.
8. Upon receiving, the first-hop router passes the frames up to the IP layer, and checks its routing table. The router sends the packets to the right interface.
9. IP packets are routed through the internet until they arrive at the Web server.
10. Server hosting the Web page will send back the Web page to the PC using HTTP messages.
11. Such TCP messages are then encapsulated into TCP packets and further into IP packets.
12. IP packets then follow IP routes and eventually reach first-hop router.
13. Router forwards these IP packets to the user PC by encapsulating them into Ethernet frames.

**P32:**
