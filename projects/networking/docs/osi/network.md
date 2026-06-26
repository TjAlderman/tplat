# Network Layer

The network layer is responsible for packet forwarding, including routing through intermediate routers. It provides:

* Connectionless communication.
* Host addressing.
* Message forwarding.

## Internet Protocol

The Internet Protocol (IP), introduced in [RFC 791](https://tools.ietf.org/html/rfc791), exists at the network layer. IP routes packets, encapsulates data, and fragments and reassembles datagrams when they reach the destination host. By nature, IP is connectionless and provides no assurance that data will reach its intended recipient.

### IPv4

An IPv4 address is a 32-bit, four-octet number represented in decimal format.

### IPv6

After a little over a decade of using IPv4, the pool of usable addresses was effectively exhausted. Two changes helped: variable-length subnet masks (VLSM) and Classless Inter-Domain Routing (CIDR) extended how IPv4 space was allocated, and IPv6 was created as the long-term successor to IPv4.

IPv6 provides a much larger address space for networked systems. An IPv6 address is 128 bits, or 16 octets, represented in hexadecimal format.

## ICMP

The Internet Control Message Protocol (ICMP), introduced in [RFC 792](https://tools.ietf.org/html/rfc792), is used by network devices to send error messages and operational information indicating success or failure when communicating with another IP address.

## DNS

DNS (Domain Name System) translates domain names, such as `apache.org`, into IP addresses, such as `95.216.26.30`, so that network routing can occur. It is the first step in almost every internet connection.

### DNS lookup

When an application needs to resolve a hostname, it first checks local caches in the browser and operating system. If there is no valid entry, the query is sent to a recursive resolver, such as an ISP resolver, router, or public DNS service like 1.1.1.1 or 8.8.8.8.

The recursive resolver handles the full resolution process by querying a hierarchy of DNS servers: root servers, then TLD servers, such as `.org`, and then the authoritative nameserver for the domain. The authoritative server returns the final record, which is passed back to the client and cached based on the TTL.

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

DNS queries typically use UDP port 53 and include transaction IDs to match requests and responses. You may see multiple queries for the same domain, such as both A and AAAA records.

Example:

```
A? apache.org
AAAA? apache.org
A 95.216.26.30, A 207.244.88.140
```

This means the domain resolves to multiple IPv4 addresses, which is common in CDNs and load balancing setups.
