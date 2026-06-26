# tcpdump

`tcpdump` is a command-line packet sniffer that can directly capture and interpret data frames from a file or network interface. `tcpdump` supports [Berkley Packet Filter](../bpf.md) syntax.

To capture network traffic from "off the wire," it uses the libraries `pcap` and `libpcap`, paired with an interface in promiscuous mode to listen for data. This allows the program to see and capture packets sourcing from or destined for any device in the local area network, not just the packets destined for us.

> In networking, "promiscuous mode" is a configuration that allows a network device (like a Network Interface Card (NIC)) to intercept and read every data packet passing through its network segment, rather than just the packets specifically addressed to it

| Switch Command | Result |
| --- | --- |
| D |	Will display any interfaces available to capture from. |
| i |	Selects an interface to capture from. ex. -i eth0 |
| n |	Do not convert addresses (i.e., host addresses, port numbers, etc.) to names. |
| e |	Will grab the ethernet header along with upper-layer data. |
| X |	Show Contents of packets in hex and ASCII. |
| XX | Same as X, but will also specify ethernet headers. (like using Xe) |
| v , vv, vvv | Increase the verbosity of output shown and saved. |
| c |	Grab a specific number of packets, then quit the program. |
| s |	Defines how much of a packet to grab. |
| S |	change relative sequence numbers in the capture display to absolute sequence numbers. (13248765839 instead of 101) |
| q |	Print less protocol information. |
| r | file.pcap	Read from a file. |
| w | file.pcap	Write into a file |

The -v, -X, and -e switches can help you increase the amount of data captured, while the -c, -n, -s, -S, and -q switches can help reduce and modify the amount of data written and seen.

## Example

![tcpdump example capture](./data/tcpdump.webp)


| Filter | Result |
| --- | --- |
| Timestamp | `Yellow` The timestamp field comes first and is configurable to show the time and date in a format we can ingest easily. |
| Protocol | `Orange` This section will tell us what the upper-layer header is. In our example, it shows IP. |
| Source & Destination IP.Port | `Orange` This will show us the source and destination of the packet along with the port number used to connect. Format == IP.port == 172.16.146.2.21 |
| Flags | `Green` This portion shows any flags utilized. |
| Sequence and Acknowledgement Numbers | `Red` This section shows the sequence and acknowledgment numbers used to track the TCP segment. Our example is utilizing low numbers to assume that relative sequence and ack numbers are being displayed. |
| Protocol Options | `Blue` Here, we will see any negotiated TCP values established between the client and server, such as window size, selective acknowledgments, window scale factors, and more. |
| Notes / Next Header | `White` Misc notes the dissector found will be present here. As the traffic we are looking at is encapsulated, we may see more header information for different protocols. In our example, we can see the TCPDump dissector recognizes FTP traffic within the encapsulation to display it for us. |