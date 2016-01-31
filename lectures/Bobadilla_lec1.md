## Netcentric Chapter 1: ##
### What is a network? ###
- Enabling data transfer
- More than 2 nodes
- Heterogeneous
- e.g: LAN network, Home network

#### *Key concepts:* ###
**End systems (hosts)**: Systems that are sinks of sources of data
<br/> e.g: smartphones, laptop, printers, game console, desk, fax,
car, TV, desktops, security systems.

Server | Client

Servers are **on** all the time, providing services (print server, storage server, mail server).
Clients (end systems) request the services.

**Intermediate systems:** Forward / Switch data from one place to another <br/>
e.g: Routers, switches, etc.

**Links:** Connect the systems, characterized by a _transmission rate_ and _propagation delay_

>We currently have 8~10 billion devices <br/>
Projection for 2020:
7.6 billion people, 50 billion end systems.

#### Transmission Media ####
Guided:
* Twisted Pair
* Coaxial Cable
* Optical Fiber

Unguided:
* Microwave
* Satellite
* Wireless

#### Electromagnetic Spectrum ####
frequency: oscillations per second (Hz) (f)
wavelength: distance between two consecutive maxima (l)

More frequency = shorter wave lengths
Less frequency = longer wave lengths

$$ F * L = C $$

$$ C = 3 * 10^{8} $$

|$frequency$|$10^2$|$10^4$|$10^6$|$10^8$|$10^{10}$|$10^{12}$|$10^{14}$|$10^{16}$|
|-----------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|           ||`Radio`||`Microwave`||`Infrared`||`UV (xray, gamma)`|

Why not use UV, x-ray, gamma rays for communication?
*hard to produce/modulate
*dangerous to living organism

**Twisted Pair:**
* Copper
* Insulated pair<br/>
example: telephone networks

Shielded (STD) | Unshielded (UTP)

UTP:
cheaper, flexible, easy to install<br/>

* CAT 3 (Up to 16Mhz)
* CAT 5 Ethernet (10Mbps and 100 Mbps)
* CAT 6

**Coaxial Cable:** <br/>
* Inner conductor
* Insulation
* Outer conductor
* Plastic

Up to 500Mhz, more capability, used in cable TV.

**Fiber Optics:**

* Cylindrical mirror is formed
* Lightwave propagates by continuous reflections
* Not affected by external influences
* Longer distance / up to 100km
* 51 Mbps 39.8Gbps

_Uses_:<br/>
* Backbone of the network international communications<br/>

Disadvantage: cost

Wireless Transmission Frequencies:
* 30Mhz to 16Hz (omnidirectional, broadcast radio)
* 2.6Hz to 60Ghz (point-to-point, directional, satellite)
$$3 * 10ˆ{11}\,\,to\,\,2 * 10^{14}$$
infrared, short distances

#### How can multiple users share a network ###
* Time Division Multiplexing (TDM)
* Frequency Division Multiplexing

#### Types of Networks ####
by size:
- Local Area Network (LAN)
- Metropolitan Area Network (0-2kms single ownership)
- Wide Area Network (50 km)

by circuit: _circuit switched vs packet switched_

_circuit switched:_
bits repeated at every switches across the circuit path (point-to-point).

_packet switched:_
information is forwarded, no physical connection (broadcast).

## What is the Internet? ##
* Network connecting networks
* Billions of hosts
* Internet Service Provider (ISP)
* Provide access to internet
* Comcast, AT&T, Google Fiber, Verizon FiOS

**Structure of the Internet:**<br/>
Home/Enterprise Network -> Access Network -> Core Network

Home/Enterprise Network (Stub): Ethernet / Wi-Fi
Access Network: Users to ISP (cable, fiber, DSL)
Core Network: ISP network
