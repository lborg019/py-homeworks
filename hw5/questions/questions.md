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

1.
![rsa.png](rsa.png)

a) at $GCD(a,b)$ we find the greatest common divisor between two prime numbers. It is used to make sure that $n$ (product of $p\cdot q$) has no common factors (other than 1) with $e$

b) In mathematics, the multiplicative inverse of $x$ is $\frac{1}{x}$; because $x \cdot \frac{1}{x} = 1$. It is used in this program to generate the private key, in the sense that the variable $d$ (used to decrypt) when multiplied by $e$ and subtracted 1 $((e\cdot d)-1)$ has to be exactly divisible by $z$ (no remainder).

c) page 686

## Wireshark Labs ##
### 802.11 ###

1. 30 Munroe St and linksys_SES_24086
2. 0.102400 Seconds for both.
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
