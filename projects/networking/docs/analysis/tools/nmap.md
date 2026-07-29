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

## Scripts

The Nmap Scripting Engine (NSE) lets you run Lua scripts against services during a scan.

```bash
sudo nmap <target> --script <category>
sudo nmap <target> --script <script-name>,<script-name>,...
sudo nmap 10.129.2.28 -p 80 -sV --script vuln
```

```text
Nmap scan report for 10.129.2.28
Host is up (0.036s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
| http-enum:
|   /wp-login.php: Possible admin folder
|   /readme.html: Wordpress version: 2
|   /: WordPress version: 5.3.4
|   /wp-includes/images/rss.png: Wordpress version 2.2 found.
|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.
|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.
|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.
|   /wp-login.php: Wordpress login page.
|   /wp-admin/upgrade.php: Wordpress login page.
|_  /readme.html: Interesting, a readme.
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-stored-xss: Couldn't find any stored XSS vulnerabilities.
| http-wordpress-users:
| Username found: admin
|_Search stopped at ID #25. Increase the upper limit if necessary with 'http-wordpress-users.limit'
| vulners:
|   cpe:/a:apache:http_server:2.4.29:
|     	CVE-2019-0211	7.2	https://vulners.com/cve/CVE-2019-0211
|     	CVE-2018-1312	6.8	https://vulners.com/cve/CVE-2018-1312
|     	CVE-2017-15715	6.8	https://vulners.com/cve/CVE-2017-15715
<SNIP>
```

## Aggressive Scan

The aggressive scan option (`-A`) combines several checks in one run:

* Service detection (`-sV`)
* OS detection (`-O`)
* Traceroute (`--traceroute`)
* Default NSE scripts (`-sC`)

```text
sudo nmap 10.129.2.28 -p 80 -A
Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-17 01:38 CEST
Nmap scan report for 10.129.2.28
Host is up (0.012s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-generator: WordPress 5.3.4
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: blog.inlanefreight.com
MAC Address: DE:AD:00:00:BE:EF (Intel Corporate)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 2.6.32 (96%), Linux 3.2 - 4.9 (96%), Linux 2.6.32 - 3.10 (96%), Linux 3.4 - 3.10 (95%), Linux 3.1 (95%), Linux 3.2 (95%),
AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), Synology DiskStation Manager 5.2-5644 (94%), Netgear RAIDiator 4.2.28 (94%),
Linux 2.6.32 - 2.6.35 (94%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 1 hop

TRACEROUTE
HOP RTT      ADDRESS
1   11.91 ms 10.129.2.28

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.36 seconds
```

## Performance

Scanning performance matters when you are working across a large network or on a slow link. Nmap exposes several controls for timing, parallelism, retries, and timeouts:

* `-T <0-5>` sets the timing template.
* `--min-parallelism <number>` controls how many probes are sent in parallel.
* `--max-rtt-timeout <time>` caps the round-trip timeout.
* `--min-rate <number>` sets a minimum packet rate.
* `--max-retries <number>` controls how many times Nmap retries probes.

Choose conservative settings for monitored or untrusted networks. Use higher throughput only when the scan is authorized and the network can tolerate the load.

```text
-T 0 / -T paranoid
-T 1 / -T sneaky
-T 2 / -T polite
-T 3 / -T normal
-T 4 / -T aggressive
-T 5 / -T insane
```

## Evasion

Nmap includes several techniques that can help bypass firewall rules and IDS/IPS controls. Common examples include packet fragmentation and decoys.

The TCP ACK scan (`-sA`) is often harder for firewalls and IDS/IPS systems to filter than a SYN scan (`-sS`) or a TCP connect scan (`-sT`) because it sends packets with the ACK flag set. Open and closed ports both respond with RST, which makes the result less obvious from the firewall's point of view. In practice, ACK scans are mainly useful for mapping firewall behavior.

Multiple VPS endpoints with different IP addresses can be used during penetration testing to determine whether the target network is blocking or rate limiting sources. If one source is blocked first, that is a strong indicator that defensive controls are in place, and scans should be adjusted to be quieter.

### Decoy

The decoy option (`-D`) inserts one or more spoofed source addresses into the scan to obscure the real origin. For example, `-D RND:5` generates five random decoys and places the real address among them. Decoys should be reachable hosts; otherwise, the scan can trigger defensive mechanisms or fail in misleading ways.

### DNS

DNS normally uses port 53 and typically relies on UDP, though TCP is also used for larger transfers and some environments. If firewall or IDS/IPS policy is weak, DNS traffic may be permitted too broadly, which can make scan traffic harder to distinguish from legitimate queries.

## Cheat Sheet

### Scanning Options

| Nmap Option | Description |
| --- | --- |
| `10.10.10.0/24` | Target network range. |
| `-sn` | Disable port scanning. |
| `-Pn` | Disable host discovery. |
| `-n` | Disable DNS resolution. |
| `-PE` | Use ICMP echo requests for host discovery. |
| `--packet-trace` | Show all packets sent and received. |
| `--reason` | Show why Nmap assigned a result. |
| `--disable-arp-ping` | Disable ARP ping requests. |
| `--top-ports=<num>` | Scan the most common ports defined in the database. |
| `-p-` | Scan all ports. |
| `-p22-110` | Scan all ports between 22 and 110. |
| `-p22,25` | Scan only ports 22 and 25. |
| `-F` | Scan the top 100 ports. |
| `-sS` | Perform a TCP SYN scan. |
| `-sA` | Perform a TCP ACK scan. |
| `-sU` | Perform a UDP scan. |
| `-sV` | Detect service versions. |
| `-sC` | Run default NSE scripts. |
| `--script <script>` | Run the specified NSE script or scripts. |
| `-O` | Detect the target operating system. |
| `-A` | Run OS detection, service detection, and traceroute. |
| `-D RND:5` | Add five random decoys to the scan. |
| `-e` | Specify the network interface for the scan. |
| `-S 10.10.10.200` | Specify the source IP address. |
| `-g` | Specify the source port. |
| `--dns-server <ns>` | Use a specific name server for DNS resolution. |

### Output Options

| Nmap Option | Description |
| --- | --- |
| `-oA filename` | Store the results in all available formats using the given base name. |
| `-oN filename` | Store the results in normal format. |
| `-oG filename` | Store the results in grepable format. |
| `-oX filename` | Store the results in XML format. |

### Performance Options

| Nmap Option | Description |
| --- | --- |
| `--max-retries <num>` | Set the number of retries for specific ports. |
| `--stats-every=5s` | Display scan status every 5 seconds. |
| `-v/-vv` | Enable verbose output. |
| `--initial-rtt-timeout 50ms` | Set the initial RTT timeout. |
| `--max-rtt-timeout 100ms` | Set the maximum RTT timeout. |
| `--min-rate 300` | Set the minimum packet rate. |
| `-T <0-5>` | Set the timing template. |
