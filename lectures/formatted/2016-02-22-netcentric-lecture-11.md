---
title: Netcentric Lecture 11

summary: IP Addresses, Network address transmission
---

IP Fragmentation

- different link layers have different sizes
MTU (maximum transmission unit)
- large IP Datagram, fragmented.

![f-4-14]({{ site.baseurl }}/img/lectures/f-4-14.png)

Example:

(bytes)

|  length   | id | frag | offset |
|:---------:|:--:|:----:|:------:|
|   4000    |  x |  0   |   0    |

MTU = 1500

Length= 4000 bytes
Header = 20 bytes
Data = 3980 bytes
1480 datafield: $$\frac{1400}{8}$$

|#|datafield|$$\rightarrow$$|length|id|fragmentation flag|offset|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|1|1480|20|1500|x|1|0|
|2|1480|20|1500|x|1|185|
|3|1020|20|1040|x|0|370|

#### IP Addresses ####
<br>
![f-4-15]({{ site.baseurl }}/img/lectures/f-4-15.png)

**3 subnets:** they can physically reach each other, without going through a router.<br>
**Interface:** connection between host/router and physical, link layers.

- router: multiple interfaces
- host: one or two (wi-fi and ethernet)

sending message to IP: _255.255.255.255_ (broadcast)

CIDR: Classless Interdomain Routing

a.b.c.d./x, where x# subnet part of the address
high order bits: subnet part
low order bits: host part

200.23.16.0/20
The first 20 bits mean the subnet.

![f-4-18]({{ site.baseurl }}/img/lectures/f-4-18.png)

#### Network Address Translation ####

Increases the amount of IP addresses from subnetting

![f-4-22]({{ site.baseurl }}/img/lectures/f-4-22.png)

There are a few necessary corrections to NAT

