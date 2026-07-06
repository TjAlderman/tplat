# Data Link Layer

The data link layer transfers frames between nodes on the same local network segment. It can also detect and sometimes correct errors from the physical layer.

The data link layer handles:
The data link layer transfers frames between nodes on the same local network segment. It can also detect and sometimes correct errors from the physical layer.

The data link layer handles:

* Frame encapsulation.
* Physical addressing.
* Flow and error control.
* Access methods, switching, and VLAN support.

## MAC Addresses

Medium/media Access Control (MAC) addresses live at the data link layer. They are 48-bit, six-octet identifiers represented in hexadecimal format.

## ARP

Address resolution protocol (ARP) is a communication protocol for discovering MAC addresses.

ARP enables a host to send, for example, an IPv4 packet to another node in the local network by providing a protocol to get the MAC address associated with an IP address. The host **broadcasts** a request containing the target node's IP address (i.e., all hosts on the network receive this broadcast), and the node with that IP address replies with its MAC address.

```
SENT (0.0074s) ARP who-has 10.129.2.18 tell 10.10.14.2
RCVD (0.0309s) ARP reply 10.129.2.18 is-at DE:AD:00:00:BE:EF
```

### Security

Because the request is broadcast, an attack vector is introduced where other devices may falsely respond with their MAC address. This attack is known as **ARP spoofing**. This can be particularly damaging if the attack is used to spoof the default gateway. This can be used as an opening for other attacks, such as denial of service, man in the middle, or session hijacking.

Software that detects ARP spoofing generally relies on some form of certification or cross-checking of ARP responses. Uncertified ARP responses are then blocked. These techniques may be integrated with the DHCP server so that both dynamic and static IP addresses are certified. This capability may be implemented in individual hosts or may be integrated into Ethernet switches or other network equipment. The existence of multiple IP addresses associated with a single MAC address may indicate an ARP spoof attack, although there are legitimate uses of such a configuration. In a more passive approach, a device listens for ARP replies on a network and sends a notification via email when an ARP entry changes.

Mitigated by smart switch that does dynamic ARP inspection.