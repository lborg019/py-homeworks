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
We compare old path with new path until all nodes are N'

_step 1:_
$$D(v)=min(D(v), D(w)+C(w,v))$$$$D(w)=min(D(w), D(x)+C(x,w))$$ $$=5, (1+3)$$ $$D(y)=min(D(y), D(x)+C(x,y))$$ $$=\infty, (1+1)$$
_step 2:_
$$D(w)=min\{D(w), D(y)+C(y,w)\}$$ $$=4,(2+1)$$ $$D(z)=\{D(z), C(y,z)+D(y)\}$$ $$=\infty, (2+2)$$
_step 3:_
$$D(w)=min\{D(w), D(v)+C(v,w)\}$$ $$=3,(2+3)$$
_step 4:_
$$D(z)min\{D(z), D(w)+C(w,z)\}$$ $$=4,(3+5)$$

|step| $N'$| $D(v),P(v)$|$D(w),P(w)$|$D(x),P(x)$|$D(y),P(y)$|$D(z),P(z)$|
|:--:|:---:|:----------:|:---------:|:---------:|:---------:|:---------:|
|0   |  U  |   2,U      |  5,U      |  1,U      | $\infty$  |  $\infty$ |
|1   |  UX |   2,U      |  4,X      |  1,U      | 2,X       |  $\infty$ |
|2   | UXY |   2,U      |  3,Y      |  1,U      | 2,X       |  4,Y      |
|3   |UXYV |   2,U      |  3,Y      |  1,U      | 2,X       |  4,Y      |
|4   |UXYVW|   2,U      |  3,Y      |  1,U      | 2,X       |  4,Y      |
|5   |UXYVWZ|  2,U      |  3,Y      |  1,U      | 2,X       |  4,Y      |

Shortest path tree:
```ruby
V-U-X-Y-Z
      |
      W
```

Distance Vector Algorithm
Bellman-Ford equation (dynamic programming)

$$d_x(y) = cost-of-least-cost path from x to y$$
x = cost of neighbor
d= cost from neighbor to destination y

min goes over all neighbors of x

$$
dv(z) = 5
dx(z) = 3
dw(z) = 3

dv(z)=min\{c(u,x)+d_x(z), c(u,v)+d_v(z), c(u,w)+d_w(z)\}
=\{1+3, 2+5, 5+3\}
$$

$$d_x(y)=min\{(x,v)+d_v(y)\}$$
