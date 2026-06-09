# Berkeley Packet Filters

Berkely Packet Filters (BPF)

## Primitives

| Primitive filter | Description |
| --- | --- |
| `[src\|dst] host <host>` | Matches a host as the IP source, destination, or either |
| `ether [src\|dst] host <ehost>` | Matches a host as the Ethernet source, destination, or either |
| `[src\|dst] net <network>` | Matches packets to or from the source and destination, or either |
| `[src\|dst] net <network> mask <netmask> or [src\|dst] net <network>/<len>` | Matches packets with specific netmask |
| `[src\|dst] port <port> or [tcp\|udp] [src\|dst] port <port>` | Matches packets that are sent to or from a port |
| `[src\|dst] portrange <p1>-<p2> or [tcp\|udp] [src\|dst] portrange <p1>-<p2>` | Matches packets to or from a port in a specific range |
| `less <length>` | Matches packets less than or equal to length, for example, len <= length |
| `greater <length>` | Matches packets greater than or equal to length, for example, len >= length |
| `(ether\|ip\|ip6) proto <protocol>` | Matches an Ethernet, IPv4, or IPv6 protocol |
| `(ip\|ip6) protochain <protocol>` | Matches IPv4, or IPv6 packets with a protocol header in the protocol header chain, for example ip6 protochain 6 |
| `(ether\|ip) broadcast` | Matches Ethernet or IPv4 broadcasts |
| `(ether\|ip\|ip6) multicast` | Matches Ethernet, IPv4, or IPv6 multicasts |
| `vlan [<vlan>]` | Matches 802.1Q frames with a VLAN ID of vlan |
| `mpls [<label>]` | Matches MPLS packets with a label |

## Protocols and Operators

The following list shows protocols that you can use:

* arp
* ether
* fddi
* icmp
* ip
* ip6
* link
* ppp
* radio
* rarp
* slip
* tcp
* tr
* udp
* wlan

| Description | Syntax |
| --- | --- |
| Parentheses | ( ) |
| Negation | != |
| Concatenation | '&&' or 'and' |
| Alteration | '\|\|' or 'or' |
