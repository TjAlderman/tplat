# Data Link Layer

The data link layer transfers frames between devices on the same local network segment. It also defines how devices identify one another on the local link and how frames move across the physical medium.

The data link layer handles:
The data link layer transfers frames between nodes on the same local network segment. It can also detect and sometimes correct errors from the physical layer.

The data link layer handles:

* Frame encapsulation.
* Physical addressing.
* Flow and error control.
* Access methods, switching, and VLAN support.

## MAC Addresses

Media Access Control (MAC) addresses live at the data link layer. They are 48-bit, six-octet identifiers represented in hexadecimal format.

## ARP

Address Resolution Protocol (ARP) maps an IP address to a MAC address on the local network.

When a host needs to send an IPv4 packet to another node on the same segment, it broadcasts an ARP request containing the target IP address. The host with that address replies with its MAC address.

```
SENT (0.0074s) ARP who-has 10.129.2.18 tell 10.10.14.2
RCVD (0.0309s) ARP reply 10.129.2.18 is-at DE:AD:00:00:BE:EF
```

### Security

Because ARP requests are broadcast, a malicious device can reply with a false MAC address and redirect traffic. This attack is known as **ARP spoofing**. It is often used to impersonate the default gateway, which can lead to denial of service, man-in-the-middle interception, or session hijacking.

Defenses usually compare ARP replies against trusted mappings or watch for conflicting IP-to-MAC associations. On managed switches, dynamic ARP inspection can help block forged replies.
