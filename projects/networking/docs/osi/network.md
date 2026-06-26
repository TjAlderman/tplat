# Network Layer

The network layer is responsible for packet forwarding including routing through intermediate routers. The network layer provides:

* Connectionless communication
* Host addressing
* Message forwarding

## Internet Protocol

The Internet Protocol (IP), introduced in [RFC 791](https://tools.ietf.org/html/rfc791), exists at the IP layer. IP is responsible for routing packets, the encapsulation of data, and fragmentation and reassembly of datagrams when they reach the destination host. By nature, IP is a connectionless protocol that provides no assurances that data will reach its intended recipient.

### IPv4

An IPv4 address is made up of a 32-bit four octet number represented in decimal format.

### IPv6

After a little over a decade of utilizing IPv4, it was determined that we had quickly exhausted the pool of usable IP addresses. With such large chunks sectioned off for special use or private addressing, the world had quickly used up the available space. To help solve this issue, two things were done. The first was implementing variable-length subnet masks (VLSM) and Classless Inter-Domain Routing (CIDR). This allowed us to redefine the useable IP addresses in the v4 format changing how addresses were assigned to users. The second was the creation and continued development of IPv6 as a successor to IPv4.

IPv6 provides us a much larger address space that can be utilized for any networked purpose. IPv6 is a 128-bit address 16 octets represented in Hexadecimal format. We can see an example of a shortened IPv6 address in the image below by the blue arrow.

## ICMP

The Internet Control Message Protocol (ICMP), introduced in [RFC 792](https://tools.ietf.org/html/rfc792), is used by network devices to send error messages and nd operational information indicating success or failure when communicating with another IP address.

## DNS

DNS (Domain Name System) translates domain names (e.g. `apache.org`) into IP addresses (e.g. `95.216.26.30`) so that network routing can occur. It is the first step in almost every internet connection.

### DNS lookup

When an application needs to resolve a hostname, it first checks local caches (browser and OS). If there is no valid entry, the query is sent to a recursive resolver (ISP DNS, router, or public DNS like 1.1.1.1 / 8.8.8.8).

The recursive resolver handles the full resolution process by querying a hierarchy of DNS servers: root servers, then TLD servers (e.g. `.org`), then the authoritative nameserver for the domain. The authoritative server returns the final record, which is passed back to the client and cached based on TTL.

```
App → OS cache → Recursive resolver → Root → TLD → Authoritative → IP
```

### Common record types

* **A**: IPv4 address
* **AAAA**: IPv6 address
* **CNAME**: Alias to another domain
* **MX**: Mail routing
* **NS**: Authoritative name servers
* **TXT**: Metadata (verification, SPF, etc.)

### Packet-level behavior

DNS queries typically use UDP port 53 and include transaction IDs to match requests and responses. You may see multiple queries for the same domain, such as both A and AAAA records.

Example:

```
A? apache.org
AAAA? apache.org
A 95.216.26.30, A 207.244.88.140
```

This means the domain resolves to multiple IPv4 addresses (common in CDNs/load balancing).
