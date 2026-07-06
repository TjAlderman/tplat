# Network Security

Network security focuses on protecting availability, integrity, and confidentiality in connected systems. Common attacks target bandwidth, routing, name resolution, and device access, so defenses usually combine filtering, redundancy, and monitoring.

## Denial of Service

Denial-of-service attacks aim to exhaust bandwidth, state tables, or processing capacity. Common examples include UDP floods, ping of death, SYN floods, and amplification attacks such as Smurf.

Amplification attacks use reflector or broadcast behavior so that a small request generates a much larger response toward the victim. Mitigations usually rely on ingress filtering, upstream scrubbing services, and redundant delivery paths such as content delivery networks.

## Common Threats

Common threat vectors include:

* **Eavesdropping** — intercepting traffic passively.
* **Intrusion** — compromising a device and altering traffic actively.
* **Impersonation** — forging identity to gain access or modify content.
* **Extortion** — disrupting services to coerce payment or action.

Attackers can reach devices remotely through services such as SSH, Telnet, SNMP, or exposed management ports, or physically through cable access, interference, or hardware tampering.

## Replay Attacks

Replay attacks reuse previously observed authentication material, such as rolling codes from a key fob. They are prevented by adding a time-dependent or otherwise freshness-based element to the exchanged value.

## Man-in-the-Middle Attacks

Man-in-the-middle attacks place an attacker between two parties so traffic can be observed or modified. Common examples include DHCP poisoning, ARP spoofing, route hijacking, and DNS spoofing.

Many of these attacks are reduced by switch controls such as port security and dynamic ARP inspection, while DNSSEC helps protect DNS responses with cryptographic integrity and authentication.
