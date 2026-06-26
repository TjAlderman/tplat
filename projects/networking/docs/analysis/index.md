# Network Traffic Analysis

If an attacker reaches a network, they must communicate with its infrastructure. Traffic analysis helps identify suspicious activity, establish baselines, and investigate incidents.

Useful tools and collection points:

* `tcpdump`: command-line capture and decode tool for live traffic or capture files.
* `TShark`: command-line variant of Wireshark.
* `Wireshark`: graphical packet analyzer for deep inspection.
* `NGrep`: pattern-matching tool for live traffic or PCAPs.
* `tcpick`: packet sniffer for tracking and reassembling TCP streams.
* Network taps: devices that copy traffic for analysis.
* SPAN ports: mirrored switch ports that send traffic to a collection point.
* Elastic Stack: ingest and visualize data from multiple sources.
* SIEMs: centralized platforms for alerting, analysis, and investigation.

The best placement for a tap is in a layer 3 link between switched segments. It allows you to capture traffic that leaves the local network, and VLAN segmentation does not change that view.

## Process

This is not an exact science. The process is dynamic and depends on what you are looking for and where you have visibility into the network.

### Descriptive Analysis

Establish a baseline and define the scope. What is the issue, what are you looking for, and which hosts or protocols matter?

### Diagnostic Analysis

Clarify the causes, effects, and interactions of the problem. Capture traffic, filter the relevant data, and interpret what the capture shows.

### Predictive Analysis

Use the findings to identify trends, detect deviations early, and anticipate future occurrences. Keep notes as you go so the findings can be reused later.

### Prescriptive Analysis

Narrow down the actions needed to eliminate the problem or prevent it from recurring.
