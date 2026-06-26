# Berkeley Packet Filters

BPF is a filtering syntax used to match traffic by host, network, port, protocol, and other packet attributes.

## Primitives

| Primitive filter | Description |
| --- | --- |
| `[src\|dst] host <host>` | Matches a host as the IP source, destination, or either. |
| `ether [src\|dst] host <ehost>` | Matches a host as the Ethernet source, destination, or either. |
| `[src\|dst] net <network>` | Matches packets to or from the source and destination network, or either. |
| `[src\|dst] net <network> mask <netmask>` or `[src\|dst] net <network>/<len>` | Matches packets with a specific netmask. |
| `[src\|dst] port <port>` or `[tcp\|udp] [src\|dst] port <port>` | Matches packets sent to or from a port. |
| `[src\|dst] portrange <p1>-<p2>` or `[tcp\|udp] [src\|dst] portrange <p1>-<p2>` | Matches packets to or from a port range. |
| `less <length>` | Matches packets less than or equal to the length. |
| `greater <length>` | Matches packets greater than or equal to the length. |
| `(ether\|ip\|ip6) proto <protocol>` | Matches an Ethernet, IPv4, or IPv6 protocol. |
| `(ip\|ip6) protochain <protocol>` | Matches IPv4 or IPv6 packets with a protocol header in the chain, for example `ip6 protochain 6`. |
| `(ether\|ip) broadcast` | Matches Ethernet or IPv4 broadcasts. |
| `(ether\|ip\|ip6) multicast` | Matches Ethernet, IPv4, or IPv6 multicasts. |
| `vlan [<vlan>]` | Matches 802.1Q frames with a VLAN ID. |
| `mpls [<label>]` | Matches MPLS packets with a label. |

## Protocols and Operators

Common protocols include `arp`, `ether`, `fddi`, `icmp`, `ip`, `ip6`, `link`, `ppp`, `radio`, `rarp`, `slip`, `tcp`, `tr`, `udp`, and `wlan`.

| Description | Syntax |
| --- | --- |
| Parentheses | `( )` |
| Negation | `!=` |
| Concatenation | `&&` or `and` |
| Alteration | `||` or `or` |
