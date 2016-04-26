# Lecture 25 #

04/25/2016

## 8.9 Operational Security: ##

The three types of firewalls:
type 1: stateless packet filters
type 2: stateful packet filter
type 3: application gateway

Limitations of firewalls, gateways:
- IP Spoofing: routing can't know for sure if data comes from source.
- All or nothing policy for UDP could be bad.
- trade off: communication with outside world vs level of Security
- multiple apps will need multiple gateways.

**Intrusion Detection Systems:**

other disadvantages of packet filters:
- operates on TCP/IP headers
- no correlation checked among sessions

**IDS:**
- deep packet inspection (check character strings in packet, compared to a databased of known attack strings) examine correlation among multiple packets/sessions.
- port scanning
- network mapping attack `nmap`
- DOS bandwidth attack

**Signature based systems:**
- database of attack
- single packet
- series of packet
- done by security engineers and by networks administrators

How it works: IDS will sniff every packet.
- If any packet match a signature:
(page 742): signature

|alert|icmp|\$EXTERNAL_NET any $\rightarrow$|\$HOME_NET any|
|:-|:-|:-|:-|
`(msg:"ICMP PNG NMAP"; dsize: 0; itype:8;)`

- send message to the network administrators
- log for future inspection

check: [snort](https://www.snort.org/)

**Limitations:**
- require previous knowledge of attacks (very reactive).
- computationally expensive
- subject to false alarms
- blind to new attacks

**Anomaly based IDS:**

create a traffic profile look for something that is statistically unused. ex: increase port scanning or a lot of ICMP packets.

can detect new undocumented attacks, can be hard to detect change.

---
## Summary: ##
**Network Security:**
- confidentiality: symmetric and public key (DES & RSA)
- message integrity
- end-point authentication (Message Authentication Code digital signatures)

used in:
- email
- secure transport (SSL)

Operational Security.

## CH 7 Multimedia Networking: ##

TV, and movies, (Netflix, youtube, Hulu)
Skype, GoogleTalk, VOIP, and video

- most video and voice will take place end-to-end over the internet (Wi-Fi)
- streaming stored audio/video
- conversational voice/video over IP
- streaming live audio/video

-signal processing pic-

sampling rate (N sample/sec)

Audio:
Analog Signal sampled at constant rate:
telephone: 8,000 samples/sec
CD music: 44,1000 samples/sec
each sample quantified $2^8=256 quantized values$
64,000 bps.
