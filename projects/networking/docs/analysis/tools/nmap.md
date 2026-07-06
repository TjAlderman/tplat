# Nmap

Network Mapper (Nmap) is an open-source network analysis and security auditing tool written in C, C++, Python, and Lua. It is designed to scan networks and identify which hosts are available on the network using raw packets, and services and applications, including the name and version, where possible. It can also identify the operating systems and versions of these hosts. Besides other features, Nmap also offers scanning capabilities that can determine if packet filters, firewalls, or intrusion detection systems (IDS) are configured as needed.

## Scan Techniques

Nmap offers many different scanning techniques:

```
tjalder@htb[/htb]$ nmap --help

<SNIP>
SCAN TECHNIQUES:
  -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon scans
  -sU: UDP Scan
  -sN/sF/sX: TCP Null, FIN, and Xmas scans
  --scanflags <flags>: Customize TCP scan flags
  -sI <zombie host[:probeport]>: Idle scan
  -sY/sZ: SCTP INIT/COOKIE-ECHO scans
  -sO: IP protocol scan
  -b <FTP relay host>: FTP bounce scan
<SNIP>
```

For example, the TCP-SYN scan (-sS) is one of the default settings unless we have defined otherwise and is also one of the most popular scan methods. This scan method makes it possible to scan several thousand ports per second. The TCP-SYN scan sends one packet with the SYN flag and, therefore, never completes the three-way handshake, which results in not establishing a full TCP connection to the scanned port.

* If our target sends a SYN-ACK flagged packet back to us, Nmap detects that the port is open.
* If the target responds with an RST flagged packet, it is an indicator that the port is closed.
* If Nmap does not receive a packet back, it will display it as filtered. Depending on the firewall configuration, certain packets may be dropped or ignored by the firewall.

> It is important to note that if nmap says a device is inactive, it may simply mean the connection was blocked by firewall filtering rules. For example, a device that ignores ICMP echo requests will be shown as inactive, though it is simply just ignoring the request.

```
tjalder@htb[/htb]$ sudo nmap 10.129.2.18 -sn -oA host 

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-14 23:59 CEST
Nmap scan report for 10.129.2.18
Host is up (0.087s latency).
MAC Address: DE:AD:00:00:BE:EF
Nmap done: 1 IP address (1 host up) scanned in 0.11 seconds
```

If we disable port scan (-sn), Nmap automatically ping scan with ICMP Echo Requests (-PE). Once such a request is sent, we usually expect an ICMP reply if the pinging host is alive. The more interesting fact is that our previous scans did not do that because before Nmap could send an ICMP echo request, it would send an ARP ping resulting in an ARP reply. We can confirm this with the "--packet-trace" option. To ensure that ICMP echo requests are sent, we also define the option (-PE) for this.

More strategies about host discovery can be found at:

https://nmap.org/book/host-discovery-strategies.html

There are a total of 6 different states for a scanned port we can obtain:

| State | Description  |
| --- | --- |
| open | This indicates that the connection to the scanned port has been  established. These connections can be TCP connections, UDP datagrams as well as SCTP associations. |
| closed | When the port is shown as closed, the TCP protocol indicates that the  packet we received back contains an RST flag. This scanning method can also be used to determine if our target is alive or not. |
| filtered | Nmap cannot correctly identify whether the scanned port is open or  closed because either no response is returned from the target for the port or we get an error code from the target. |
| unfiltered | This state of a port only occurs during the TCP-ACK scan and means  that the port is accessible, but it cannot be determined whether it is open or closed. |
| open\|filtered | If we do not get a response for a specific port, Nmap will set  it to that state. This indicates that a firewall or packet filter may protect the port. |
| closed\|filtered | This state only occurs in the IP ID idle scans and indicates  that it was impossible to determine if the scanned port is closed or filtered by a firewall. |

By default, Nmap scans the top 1000 TCP ports with the SYN scan (-sS). This SYN scan is set only to default when we run it as root because of the socket permissions required to create raw TCP packets. Otherwise, the TCP scan (-sT) is performed by default. We can define the ports one by one (-p 22,25,80,139,445), by range (-p 22-445), by top ports (--top-ports=10) from the Nmap database that have been signed as most frequent, by scanning all ports (-p-) but also by defining a fast port scan, which contains top 100 ports (-F).

### ICMP Echo (-PE)

ping scan with ICMP Echo Requests (-PE). Once such a request is sent, we usually expect an ICMP reply if the pinging host is alive. The more interesting fact is that our previous scans did not do that because before Nmap could send an ICMP echo request, it would send an ARP ping resulting in an ARP reply. 

If we get an ICMP response with error code 3 (port unreachable), we know that the port is indeed closed.

For all other ICMP responses, the scanned ports are marked as (open|filtered).

### SYN Scan (-sS)

~~SYN scan must be run with sudo - nmap will craft raw TCP packets and instantly mark port as open after receiving SYN, ACK; rather than waiting for full TCP handshake~~ Is this correct?

### Connect Scan (-sT)

The Nmap TCP Connect Scan (-sT) uses the TCP three-way handshake to determine if a specific port on a target host is open or closed. The scan sends an SYN packet to the target port and waits for a response. It is considered open if the target port responds with an SYN-ACK packet and closed if it responds with an RST packet.

### UDP Scan (-sU)

Another disadvantage of this is that we often do not get a response back because Nmap sends empty datagrams to the scanned UDP ports, and we do not receive any response. So we cannot determine if the UDP packet has arrived at all or not. If the UDP port is open, we only get a response if the application is configured to do so.

## Saving Results

`Nmap` can save the results in 3 different formats.

- Normal output (-oN) with the .nmap file extension
- Grepable output (-oG) with the .gnmap file extension
- XML output (-oX) with the .xml file extension

We can also specify the option (-oA) to save the results in all formats.

With the XML output, we can easily create HTML reports that are easy to read, even for non-technical people. This is later very useful for documentation, as it presents our results in a detailed and clear way. To convert the stored results from XML format to HTML, we can use the tool xsltproc.

```
tjalder@htb[/htb]$ xsltproc target.xml -o target.html
```

If we now open the [HTML file](./data/target.html) in our browser, we see a clear and structured presentation of our results.

More information about the output formats can be found [here](https://nmap.org/book/output.html)

## Service Enumeration

We can use the version scan to scan the specific ports for services and their versions (-sV).

> I ran into some interesting troubles doing a service enumeration. Without sudo, nmap will default to TCP scan -sT. This is slow, as it relies on the full TCP handshake been established before marking the port as open. With sudo, nmap crafts raw TCP packets and operates in -sS mode. In this mode, nmap will mark a port as open as soon as it receives SYN, ACK back from host, rather than waiting for full handshake.

### Banner Grabbing

Primarily, Nmap looks at the banners of the scanned ports and prints them out. after a successful three-way handshake, the server often sends a banner for identification. This serves to let the client know which service it is working with. At the network level, this happens with a PSH flag in the TCP header. One disadvantage to Nmap's presented results is that the automatic scan can miss some information because sometimes Nmap does not know how to handle it.

If we manually connect to the host port using nc, grab the banner, and intercept the network traffic using tcpdump, we can see what Nmap did not show us.

```
sudo tcpdump -i eth0 host 10.10.14.2 and 10.129.2.28
nc -nv 10.129.2.28 25

18:28:07.128564 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [S], seq 1798872233, win 65535, options [mss 1460,nop,wscale 6,nop,nop,TS val 331260178 ecr 0,sackOK,eol], length 0
18:28:07.255151 IP 10.129.2.28.smtp > 10.10.14.2.59618: Flags [S.], seq 1130574379, ack 1798872234, win 65160, options [mss 1460,sackOK,TS val 1800383922 ecr 331260178,nop,wscale 7], length 0
18:28:07.255281 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [.], ack 1, win 2058, options [nop,nop,TS val 331260304 ecr 1800383922], length 0
18:28:07.319306 IP 10.129.2.28.smtp > 10.10.14.2.59618: Flags [P.], seq 1:36, ack 1, win 510, options [nop,nop,TS val 1800383985 ecr 331260304], length 35: SMTP: 220 inlane ESMTP Postfix (Ubuntu)
18:28:07.319426 IP 10.10.14.2.59618 > 10.129.2.28.smtp: Flags [.], ack 36, win 2058, options [nop,nop,TS val 331260368 ecr 1800383985], length 0
```

The first three lines show us the three-way handshake.

After that, the target SMTP server sends us a TCP packet with the PSH and ACK flags, where PSH states that the target server is sending data to us and with ACK simultaneously informs us that all required data has been sent.