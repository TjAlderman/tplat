# Network Traffic Analysis

If an attacker seeks to breach a network, they must inevitably communicate with it's infrastructure. Network traffic analysis can be a valuable tool for detecting the threat actors. Network traffic analysis can be used for:

* Collecting real-time traffic within the network to analyze upcoming threats.
* Setting a baseline for day-to-day network communications.
* Identifying and analyzing traffic from non-standard ports, suspicious hosts, and issues with networking protocols such as HTTP errors, problems with TCP, or other networking misconfigurations.
* Detecting malware on the wire, such as ransomware, exploits, and non-standard interactions.
* NTA is also useful when investigating past incidents and during threat hunting.

| Tool | Description |
| tcpdump | tcpdump is a command-line utility that, with the aid of LibPcap, captures and interprets network traffic from a network interface or capture file. |
| Tshark | TShark is a network packet analyzer much like TCPDump. It will capture packets from a live network or read and decode from a file. It is the command-line variant of Wireshark. |
| Wireshark | Wireshark is a graphical network traffic analyzer. It captures and decodes frames off the wire and allows for an in-depth look into the environment. It can run many different dissectors against the traffic to characterize the protocols and applications and provide insight into what is happening. |
| NGrep | NGrep is a pattern-matching tool built to serve a similar function as grep for Linux distributions. The big difference is that it works with network traffic packets. NGrep understands how to read live traffic or traffic from a PCAP file and utilize regex expressions and BPF syntax. This tool shines best when used to debug traffic from protocols like HTTP and FTP. |
| tcpick | tcpick is a command-line packet sniffer that specializes in tracking and reassembling TCP streams. The functionality to read a stream and reassemble it back to a file with tcpick is excellent. |
| Network Taps | Taps (Gigamon, Niagra-taps) are devices capable of taking copies of network traffic and sending them to another place for analysis. These can be in-line or out of band. They can actively capture and analyze the traffic directly or passively by putting the original packet back on the wire as if nothing had changed. |
| Networking Span Ports | Span Ports are a way to copy frames from layer two or three networking devices during egress or ingress processing and send them to a collection point. Often a port is mirrored to send those copies to a log server. |
| Elastic Stack | The Elastic Stack is a culmination of tools that can take data from many sources, ingest the data, and visualize it, to enable searching and analysis of it. |
| SIEMS | SIEMS (such as Splunk) are a central point in which data is analyzed and visualized. Alerting, forensic analysis, and day-to-day checks against the traffic are all use cases for a SIEM. |
