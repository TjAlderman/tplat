# Network Layer

The network layer is responsible for packet forwarding between hosts, including routing through intermediate routers. It provides:

* Connectionless communication.
* Host addressing.
* Message forwarding.

## Internet Protocol

The Internet Protocol (IP), introduced in [RFC 791](https://tools.ietf.org/html/rfc791), exists at the network layer. IP routes packets, encapsulates data, and fragments and reassembles datagrams when they reach the destination host. By design, IP is connectionless and provides no guarantee that data will reach its intended recipient.

### IPv4

An IPv4 address is a 32-bit, four-octet number represented in decimal format.

### IPv6

IPv6 was created as the long-term successor to IPv4. It provides a much larger address space for networked systems and is represented as a 128-bit, 16-octet hexadecimal address.

IPv4 space was extended for a time through variable-length subnet masks (VLSM) and Classless Inter-Domain Routing (CIDR), but IPv6 removed the need to conserve address space in the same way.

### TTL

Time to live (TTL) limits the lifespan of a packet so it cannot circulate indefinitely.

When a device originates an IP packet, it assigns an initial TTL value. The common default TTL values are:

* 64 for Linux and macOS systems.
* 128 for Windows systems.
* 255 for network devices such as routers.

## ICMP

The Internet Control Message Protocol (ICMP), introduced in [RFC 792](https://tools.ietf.org/html/rfc792), is used by network devices to send error messages and operational information indicating success or failure when communicating with another IP address.

For example, when a router forwards an IP datagram, it decrements the TTL field by one. If the result is 0, the packet is discarded and an ICMP time exceeded message is sent to the source address.

## DNS

DNS (Domain Name System) translates domain names, such as `apache.org`, into IP addresses, such as `95.216.26.30`, so that network routing can occur. It is the first step in almost every internet connection.

### DNS lookup

When an application needs to resolve a hostname, it first checks local caches in the browser and operating system. If there is no valid entry, the query is sent to a recursive resolver, such as an ISP resolver, router, or public DNS service like 1.1.1.1 or 8.8.8.8.

The resolver handles the full resolution process by querying a hierarchy of DNS servers: root servers, then TLD servers such as `.org`, and finally the authoritative nameserver for the domain. The authoritative server returns the final record, which is cached according to the TTL.

```
App → OS cache → Recursive resolver → Root → TLD → Authoritative → IP
```

### Common record types

* **A**: IPv4 address.
* **AAAA**: IPv6 address.
* **CNAME**: Alias to another domain.
* **MX**: Mail routing.
* **NS**: Authoritative name servers.
* **TXT**: Metadata such as verification and SPF records.

### Packet-level behavior

DNS queries typically use UDP port 53 and include transaction IDs to match requests and responses. Multiple queries for the same domain are common, such as both A and AAAA records.

Example:

```
A? apache.org
AAAA? apache.org
A 95.216.26.30, A 207.244.88.140
```

This means the domain resolves to multiple IPv4 addresses, which is common in CDNs and load-balancing setups.
