# Homework questions #
#### lukas_borges ####

Chapter 4:

Review Questions R1,R2,R3,R4 (omit the parts of these review questions that refer to virtual circuits since we did not cover it in class), R8, R9, R12, R13, R16, R18, R21, R23, R24, R27

Problems: P7,  P10, P24, P26, P30, P37, P42

### Chapter 4: ###
#### Review questions: ####

**R1.**

Datagram.
Router's forwarding decisions are based on network-layer field value. A switch is a packet switcher whose forwarding decisions are based on the link-layer field value. Also, routers use IP addresses while link-layer switches use MAC addresses.

**R2.**

Forwarding and Routing.

**R3.**

Routing determines the end-to-end paths that packets should take from source to destination (uses routing algorithms).

Forwarding moves the packet that arrives at the input link to the correct output link (uses forwarding tables).

**R4.**

Yes they do.

For Datagram Networks:
- The forwarding tables consist of **header value** or **destination address** and **output link** fields.

Virtual Circuit Networks:
- Forwarding table consists of **incoming interface**, **incoming VC number**, **outgoing interface**, and **outgoing VC numbers** fields.

**R8.**

1. Switching via memory
2. Switching via bus
3. Switching via interconnection network

**Memory:**
Switching of input and output ports are directly controlled by CPU. Packets arrive from input port by fetching the interrupt signal in CPU. Routing processor catches the destination address from header, uses forwarding table to find appropriate output port and then copies the packet to the output port buffer.

**Bus:**
Packets are moved from input to output port directly over a shared bus. Because this bus is shared, only one packet at a time. When a packet arriving at the input port finds the bus busy, it is blocked and queued.

**Interconnection network:**
A crossbar switch is an example of such. A packet arriving at input port travels along the horizontal bus attached to the input port until it intersects with a vertical bus which leads to the appropriate output port. When the vertical bus is free, the packet can be transferred. If not, the packet is blocked and queued.

Multiple packets can be sent in parallel using switching via Interconnection network. This architecture allows packets from different input ports to each same output port.

**R9.**

Switching fabric could be slow (increasing queue size). Increased queue sizes cause router's buffering space to be completely used.
When the queue size is too large, packet losses are more likely to happen.

To eliminate packet loss, increasing switching fabric speed at least by $n$ times faster than the input line's speed. ($n$ = number of input ports)

**R12.**

Yes. Every router has an IP address to address itself and each device connected. Right now my computer is connected to my home network. My router's IP is `10.0.0.1`, and I can even use that address on my internet browser to access my router's settings page.
I can also tell that my computer's local IP address is `10.0.0.9` and laptop is `10.0.0.13`. These are local area network IPs used for intranet/router communication.

**R13.**

IP: `223.1.3.27`<br>
This is IP version 4, meaning that each number can go from 0 to 255, because each of the numbers separated by a dot is composed of 8 bits.

We can convert each of these numbers into binary and fill remaining bits (if any) with 0s:

223: `1101 1111`<br>
1: `0000 0001`<br>
3: `0000 0011`<br>
27: `0001 1011`<br>

Patching everything together, we end up with the following 32-bit sequence:

`1101 1111 0000 0001 0000 0011 0001 1011`

**R16.**

| Data            | Measure        |
| :------         | :------------- |
| Chunk           | 40 bytes       |
| Interval        | 0.020 seconds  |
| TCP Header      | 20 bytes       |
| IP Header       | 20 bytes       |

$Total\,Header\,Size = TCP\,Header+IP\,Header$<br>
$= 20\,bytes+20\,bytes$<br>
$= 40\,bytes$

$Total\,Segment\,Size = Chunk+Total\,Header\,Size$<br>
$= 40\,bytes+40\,bytes$<br>
$= 80\,bytes$

$80\,bytes = 100\%$<br>
$40\,bytes = x\%$<br>

$$x = \frac{40\cdot100}{80}$$
$$x = 50\%$$

$$50\%\,overhead\,\,50\%\,data$$

**R18.**

The router will assign IP addresses to the 5 PCs automatically using Dynamic Host Control Protocol (DHCP). The default gateway, usually `192.168.0.1` or `10.0.0.1` is the router's IP. The beginning address for devices usually starts at `Default Gateway IP's + 1`.
So, if the default gateway is `10.0.0.1`, the router might do the following:

| Device | IP         |
| :------| :--------- |
| PC 1   | `10.0.0.2` |
| PC 2   | `10.0.0.3` |
| PC 3   | `10.0.0.4` |
| PC 4   | `10.0.0.5` |
| PC 5   | `10.0.0.6` |

These are local area network (LAN) IPs.
Whenever one of the PCs requests something from the public Internet, the router keeps the requesting IP and port in a table. Then it performs the request on the PC's behalf using the public IP. When it receives a packet, it forwards it to the requesting LAN IP accordingly. This is known as NAT, and it is necessary in this scenario because Internet service providers (ISP) cannot assign a specific public IP to each device connected. There are not enough public IPs (in IPv4) to serve each device connected.

**R21.**

Both are used to compute least-cost path between source and destination.

Differences:

**Link-State:**
- Network topology and all link costs are
input.
- Computes least-cost path from source to
destination with complete knowledge of the
network.
- Uses Dijkstra's algorithm to calculate shortest path.
- Count-to-infinity problem can be averted.
- Creates routing table, neighbor table and topology table (more memory required).
- Updates are multicasted.

**Distance-Vector:**
- All associated costs with current node to all its neighbors is the input
- Computes least-cost path in iterative and distributed manner
- Uses Bellman-Ford algorithm to calculate shortest path.
- Count-to-infinity might be a problem.
- Creates a routing table (less memory space required).
- Updates are broadcasted.

**R23.**

No. In fact, it is better to have different routing algorithms because their trade-offs suite different cases more appropriately.
Each Autonomous System (AS) has administrative control for routing within it.

**R24.**

No. From the advertisement, $D$ can reach $z$ in 11 hops by using the path through $A$. $D$ can already reach to $z$ in 7 hops by using the path through $B$. As the value of $D$ through path $B$ is less than through path $A$, the table has no need to modify the entry of $z$.

**R27.**

**BGP** (Border Gateway Protocol) is used for Inter-AS Routing protocol.

**RIP** (Router Information Protocol) and **OSPF** (Open Shortest Path First) are Intra-AS protocols.

**Inter-AS:**
- BGP carries path attributes and provides controlled distribution of routing information. Its routing decisions are policy-based.
- Ability to scale and handle routing among large number of networks.
- Policy dominates quality and performance of routes.

**Intra-AS:**
- Policy is much less important when choosing routes (system goes for best choice).
- Ability to scale routing is more difficult. Might have to divide in smaller AS.
- Performance is focused on router because of single AS.

#### Problems: ####

**P7.**
**P10.**
**P24.**
**P26.**
**P30.**
**P37.**
**P42.**
