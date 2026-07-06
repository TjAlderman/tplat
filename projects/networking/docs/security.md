All mitigated through ingress filtering (check packet comes from a sensible place based off IP), upstream support (dedicated DoS processing system that reroutes traffic), content distribution network (don’t have single point of failure).

DoS:

UDP.

Ping of death. Large ICMP packet with multiple fragments. Reassembled by user overflowing memory.

SYN flood. Open TCP connection. Flood SYN and never ACK. Sever builds state and overflows.

Host multipliers (lots of devices controlled centrally).

Packet multipliers (send one packet, get many).

SMURF. Ping broadcast with target address as source.

Threat vectors:
	•	Eavesdropping - intercept messages (passive).
	•	Intrusion – compromise device, modify messages (active).
	•	Impersonation – identity fraud, gain content, modify messages (active).
	•	Extorsion – disrupt services (active).

Devices have remote (SMNP, telnet, ssh, port monitors) and physical (chip-sniffing, cable cutting, interference) access.

How many planes are you vulnerable. Are there single points of failure?

Replay attacks:
	•	Jam car fob frequency and listen at slightly deviated frequency with tight BP filter. Jam + listen (1), Jam + listen (2). You know have two rolling codes. Replay one so user gets into car. Know have second code for us to get in later.
	•	Can be prevented by using a key that has a temporal element to encryption.

Man-in-the-middle attacks:
	•	DHCP poisoning. Users contacts DHCP to get assigned an IP. Villain floods DHCP server to exhaust list. Offers own DHCP to user. Forwards users traffic to internet, snooping (passive) and potentially altering (active) it on the way through. Mitigated by a smart switch that limits MAC addresses per port (thereby preventing the villain from flooding the server).
	•	ARP poisoning. Send gratuitous ARP replies that convince gateway that you are user and user that you are the gateway. Mitigated by smart switch that does dynamic ARP inspection.
	•	Fill routing table with more specific prefix. Particularly bad because routing attacks can propagate globally.
	•	DNS Spoofing. Make a DNS query. Then, fake source IP of authority and flood responses to DNS query with guessed/snooped 16-bit ID. As long as you were fast enough and beat the official response, you’ve now poisoned the DNS cache. Fixed by DNSSEC (DNS with crypto – adds integrity and authentication)