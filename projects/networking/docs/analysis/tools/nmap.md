# Nmap

Network Mapper (Nmap) is an open-source network scanning and security auditing tool. It uses raw packets to identify live hosts, open ports, services, and, when possible, operating system details.

## Host Discovery

Nmap can test whether hosts are reachable before performing a full port scan. A common discovery-only scan is `-sn`. On local networks, Nmap often uses ARP requests; on routed networks, it typically falls back to ICMP and other probes.

## Port Scanning

Nmap supports several scan types:

* `-sS`: TCP SYN scan.
* `-sT`: TCP connect scan.
* `-sU`: UDP scan.
* `-sV`: Service and version detection.
* `-O`: OS detection.
* `-p`: Specific ports or port ranges.
* `-F`: Fast scan of the most common ports.
* `--top-ports`: Scan the most common ports in the database.

The TCP SYN scan is the default when Nmap is run with sufficient privileges. It sends a SYN packet and interprets SYN-ACK as open, RST as closed, and no response as filtered.

The TCP connect scan uses the operating system's normal connect() call and completes the three-way handshake. It is slower, but it works without raw socket privileges.

UDP scans are less definitive because many services do not respond to empty datagrams. A lack of response often results in an `open|filtered` state.

Nmap reports several port states:

| State | Meaning |
| --- | --- |
| open | The service accepted the probe. |
| closed | The host replied, but no service is listening. |
| filtered | A firewall or filter prevented a determination. |
| unfiltered | The port is reachable, but open/closed could not be determined. |
| open\|filtered | Nmap could not tell whether the port is open or filtered. |
| closed\|filtered | Nmap could not tell whether the port is closed or filtered. |

## Service Enumeration

Version detection (`-sV`) probes open ports and attempts to identify the running service and version. Banner grabbing often reveals information after the three-way handshake, when the service sends application data back to the client.

For example, when connecting to an SMTP service, the server may send a banner such as:

```
220 inlane ESMTP Postfix (Ubuntu)
```

## Saving Results

Nmap can save results in several formats:

* `-oN` for normal output.
* `-oG` for grepable output.
* `-oX` for XML output.
* `-oA` for all three formats.

XML output can be converted into HTML reports with `xsltproc`:

```
xsltproc target.xml -o target.html
```

The generated HTML report can be viewed in the browser at [target.html](./data/target.html).

More information about Nmap output formats is available in the [Nmap documentation](https://nmap.org/book/output.html).
