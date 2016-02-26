# Lecture 12 #

How to get the IP address.
DHCP: Dynamic Host Config Protocol [RFC 2141]

Goal: Allow host to dynamically obtain IP addresses from a network server.
- can renew lease
- allow reuse of addresses
- support for mobile users

![f-4-21](f-4-21.png)
The reason for steps 3 and 4 is because there might be more than one DHCP Server in the network, the device must accept only one offer.

ICMP: Internet Control Message Protocol [RFC 792]
- ping
- traceroute
- wireshark capture

Used by routers and hosts to communicate network level information.
errors: unreachable host or unreachable port, unreachable network or unreachable protocol.

### ICMP Message: ###
- type, code, first 8 bytes of datagram causing an error

|type|code|           message             |
|:--:|:--:|:-----------------------------:|
|  0 |  0 |          echo ready           |
|  8 |  0 |          echo request         |
|  3 |  0 |destination network unreachable|

port/host (book, page, 354)

## Routing Algorithms ##
_Section 4.5_
|destination addrress|output link|
|:------------------:|:---------:|
|       range1       |     0     |
|       range2       |     1     |
|       range3       |     2     |
|       range4       |     2     |
|         "          |    ...    |


![f-4-27](f-4-27.png)
$Graph = (Nodes, Edges)$
$Nodes = \{U,V,W,X,Y,Z\}$
$Edges = \{(uv),(ux),(vx),(vw)...\}$
$c(x,x') = cost of link (x,x')$
$(w,z)=5$

Cost:
- can be related to congestion
- can be inversely related to bandwidth
- related to distance

### Classification ###
- global: (complete knowledge) in all routers
- decentralized: router knows physically connected neighbors, link, cost to other neighbors

_static:_ routes change slowly over time
_dynamic:_ routes change quickly, periodic or when cost link changes.

### Link-State Routing Algorithm: ###
(Dijkstra's Algorithm)
- net topology, cost, known to all Nodes
- all nodes have the same information
- compute least cost path from one node to all others (this gives the forwarding table to all nodes)

$C(x,y)$: link cost from $x$ to $y$ = $\infty$ if no direct neighbors.
$D(v)$: current value of cost of path from source to destination $v$
$P(v)$: predecessor in route along the path from source to destination
$N'$: set of nodes whose least cost is known

```ruby
Initialization:
N’ = {u}
for all nodes v
if v is a neighbor of u then D(v) = c(u,v)
else D(v) = ∞
Loop
find w not in N’ such that D(w) is a minimum
add w to N’
update D(v) for each neighbor v of w and not in N’:
D(v) = min( D(v), D(w) + c(w,v) )
/* new cost to v is either old cost to v or known
least path cost to w plus cost from w to v */ until N’= N
```

|step| $N'$| $D(v),P(v)$|$D(w),P(w)$|$D(x),P(x)$|$D(y),P(y)$|$D(z),P(z)$|
|:--:|:---:|:----------:|:---------:|:---------:|:---------:|:---------:|
|0   |  U  |   2,U      |  5,U      |  1,U      | $\infty$  |  $\infty$ |
|1   |  Ux |   2,U      |  4,X      |  1,U      | 2,X       |  $\infty$ |
