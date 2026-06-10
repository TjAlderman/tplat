# Network Layer

The network layer is responsible for packet forwarding including routing through intermediate routers. The network layer provides:

* Connectionless communication
* Host addressing
* Message forwarding

## Internet Protocol

The internet protocol (IP) exists at the IP layer. IP is responsible for routing packets, the encapsulation of data, and fragmentation and reassembly of datagrams when they reach the destination host. By nature, IP is a connectionless protocol that provides no assurances that data will reach its intended recipient.

### IPv4

An IPv4 address is made up of a 32-bit four octet number represented in decimal format.

### IPv6

After a little over a decade of utilizing IPv4, it was determined that we had quickly exhausted the pool of usable IP addresses. With such large chunks sectioned off for special use or private addressing, the world had quickly used up the available space. To help solve this issue, two things were done. The first was implementing variable-length subnet masks (VLSM) and Classless Inter-Domain Routing (CIDR). This allowed us to redefine the useable IP addresses in the v4 format changing how addresses were assigned to users. The second was the creation and continued development of IPv6 as a successor to IPv4.

IPv6 provides us a much larger address space that can be utilized for any networked purpose. IPv6 is a 128-bit address 16 octets represented in Hexadecimal format. We can see an example of a shortened IPv6 address in the image below by the blue arrow.
