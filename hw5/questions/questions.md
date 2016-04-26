# Homework 5 #
#### lukas_borges ####

1. [15 Points] Programming Assignment: Download and run the simple python implementation of RSA from: https://gist.github.com/JonCooperWorks/5314103#file-rsa-py and answer the following questions:

a) Run the program and enter as prime numbers 17 and 19. What is the public key and the private key?
b) Give a brief explanation (less than a paragraph) of the following functions from the python code: -gcd(a, b) (line 14)
-multiplicative_inverse(e, phi) (line 22)
-is_prime(num) (line 49)
 c) Explain differences and similarities between the RSA algorithm discussed in class (pages 685-686) and the implementation found in the code: generate_keypair (line 59), encrypt(line 86), decrypt(line 94).

2.[25 points] Complete the following Wireshark labs:
http://www-net.cs.umass.edu/wireshark-labs/Wireshark_802.11_v6.0.pdf
http://www-net.cs.umass.edu/wireshark-labs/Wireshark_SSL_v6.0.pdf

3. [25 points] Give an answer for the folowing review questions:

Chapter 6 Review R1,R2,R5,R7,R8
Chapter 6 Problems: P1, P5, P6.

[35 points] Give an answer for the folowing review questions:

Chapter 8 Review R1,R2,R3,R4, R7, R9, R12, R16, R19, R23
Chapter 8 Problems: P1, P3, P4, P7, P8

For #1 include some screenshots of the RSA Python implementation running and answer the questions. For #2 Answer the questions posed in the lab documents and include one screenshot of wireshark working for each lab. For #1, #2, #3, #4 submit evidence of your work through moodle in one report (i.e., as ONE pdf file). The deadline is on Sunday May 1st. No late submissions are allowed for this homework. This homework is worth 9% of the final grade.

## RSA encryption: ###

1. ![rsa.png](rsa.png)
a) at $GCD(a,b)$ we find the greatest common divisor between two prime numbers. It is used to make sure that $n$ (product of $p\cdot q$) has no common factors (other than 1) with $e$
b) In mathematics, the multiplicative inverse of $x$ is $\frac{1}{x}$; because $x \cdot \frac{1}{x} = 1$. It is used in this program to generate the private key, in the sense that the variable $d$ (used to decrypt) when multiplied by $e$ and subtracted 1 $((e\cdot d)-1)$ has to be exactly divisible by $z$ (no remainder).
c) page 686

## Wireshark Labs ##
### 802.11 ###

1. 30 Munroe St and linksys_SES_24086
2. `0.102400` Seconds for both.
![ws-wireless-1.png](ws-wireless-1.png)
3. `00:16:b6:f7:1d:51`
![ws-wireless-2.png](ws-wireless-2.png)
4. `ff:ff:ff:ff:ff:ff`
5. Since this is a beacon frame, the MAC Basic Service Set (BSS) ID is the same as the source address: `00:16:b6:f7:1d:51`
6. Supported rates: `1.0, 2.0, 5.5, 11.0 Mbit/s.`
Extended rates: `6.0, 9.0, 12.0, 18.0, 24.0, 36.0, 48.0, 54.0 Mbit/s`
![ws-wireless-3.png](ws-wireless-3.png)

#### Data Transfer: ####
7. Receiver, Destination, Transmitter, and Source addresses.
Receiver address: `00:16:b6:f7:1d:51`
Destination address: `00:16:b6:f4:eb:a8`
Transmitter Address and Source Address: `00:13:02:de:b6:4f`
Receiver address: `00:16:b6:f7:1d:51`
Destination address: `00:16:b6:f4:eb:a8`
Transmitter Address and Source Address: `00:13:02:de:b6:4f`
Host: `00:13:02:de:b6:4f`
Access point: `00:16:b6:f4:eb:a8`
First-hop router: `00:16:b6:f7:1d:51`
Wireless host (sending TCP segment): `192.168.1.109`
Destination IP address: `128.119.245.12`
`128.119.245.12` corresponds to the URL `gaia.cs.umass.edu`.
The destination MAC address of the frame containing the SYN is different from the destination IP address of the IP packet contained within the frame.
![ws-wireless-4.png](ws-wireless-4.png)

8.

#### Association/Dissociation: ####



#### Other Frame Types: ####

## Questions ##
#### Chapter 6 ###
#### Review Questions ####

**R1.** Infrastructure mode:
- Common mode wireless networks operate on.
- Used when PC is connected to a wireless access point or a wireless router.
- If hosts are connected to network via base station or access point (fixed infra structure)
- Cellular networks work in infrastructure mode because all cellphones connect to network through base stations.

If network is not in infrastructure mode, it is operating in Ad hoc mode. In Ad hoc, wireless hosts can communicate with each other without access point. No fixed infrastructure such as access point is required for the wireless hosts.

**R2.**

| type | description |
| :--- | :---------- |
|Single-hop, infrastructure-based|No base station. Base station connected to large wired network |
|Single-hop, infrastructure-less |No base station required for hosts to connect to network|
|Multi-hop, infrastructure-based |Base station is connect to larger wired network. Some nodes reach the netwok by connecting with other nodes.|
|Multi-hop, infrastructure-less  |No base station required for nodes to connect to network. Hosts relay messages among several nodes|

**R5.** In 802.11 networks The role of the beacon frame is to help a wireless station to discover and identify a nearby Access point (AP) to associate with.

**R7.** Wireless channels have high bit error rates. To mitigate this problem, 802.11 MAC protocol uses an acknowledgement scheme. In wired Ethernet bit error rates are lower and the transmission is quite reliable, therefore, there is no need for acknowledgements.

**R8.** False. There is no preamble in 802.11 because it is sent by the hardware and not treated as a part of a data link packet (unlike what happens in Ethernet).
Ethernet packets are a little bit simpler.

#### Problems ####

**P1.**
Data bits $d_0=1$, $d_1=-1$
CDMA code cm = (1, -1, 1, -1, 1, -1, 1, -1)

We calculate the sender's output $Z_{i,m}$ by multiplying data bit $d_i$ with mth bit cm in the given CDMA code:

$Z_{i,m} = d_i \cdot c_m$

| Data($d_0$) | CDMA code(cm) | Output($Z=d_0 \cdot cm$)|
| :---------: |:-------------:| :---------------------: |
| 1           | 1,-1,1,-1,1,-1,1,-1| 1,-1,1,-1,1,-1,1,-1|

| Data($d_0$) | CDMA code(cm) | Output($Z=d_0 \cdot cm$)|
| :---------: |:-------------:| :---------------------: |
| -1          | 1,-1,1,-1,1,-1,1,-1| -1,1,-1,1,-1,1,-1,1|

$d_0 = (1, -1, 1, -1, 1, -1, 1, -1)$
$d_1 = (-1, 1, -1, 1, -1, 1, -1, 1)$

**P5.** **a.** The protocol does not completely break down. The two APs will have different SSIDs and MAC addresses and one of the SSISs will be assigned to the wireless station that connect to the cafe.
A virtual link between the new station and the AP is maintained.
The two APs can work in parallel over the same channel, the transmission might be degraded (two stations transmitting over the same channel). Collision might happen if both stations attempt to transmit over the same channel at the same time.

**b.** The two stations (each from a different ISP) can transmit data at the same time without collisions. The performance will be upgraded when one AP operates over channel 1 and the other over channel 11. Both APs are using non-overlapping channels, two stations transmitting over different channels.

**P6.** **a.** CSMA/CA exists so that a station does not transmit the second frame immediately even if the channel listened is idle. It is done so to avoid collision. If station A is transmitting first frame and station B has data frames to transmit:
_In CSMA/CD:_ B senses the channel, finds out the channel is busy and waits for channel to be free (idle). After successfully transmitting the first frame, A wants to send the second frame. After A finishes transmitting the first frame, A and B both listen to the channel at the same time. Both will find the channel idle and both will start transmission of data at the same time, which will lead to collision. CSMA/CD protocol detects transmission and station A and B abort the transmission.

**b.**
_In CSMA/CA:_ After station A receives the acknowledgement for the first frame, it begins the CSMA/CA for a second frame at step 2 instead of step 1. Station A senses the channel; if it's idle it starts the counter, but does not transmit the second frame immediately. Once counter hits zero, A senses the channel again and sends the data frame if the channel is idle. If not it enters in random back-off. Station B also senses the channel, sends the first frame if it finds the channel idle. If not, it also enters the random back off time.

Whichever station finds the channel idle first sends the frame.

### Chapter 8 ###
#### Review Questions ####
R1, R2, R3, R4, R7, R9, R12, R16, R19, R23

#### Problems ####
P1, P3, P4, P7, P8
