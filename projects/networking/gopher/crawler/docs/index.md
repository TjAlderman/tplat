# Crawler

The following codebase is designed to facilitate the crawling and downloading of data from Gopher servers. To enhance readability and maintainability, the code is structured into multiple files, each responsible for specific functionalities. Below is an overview of the main components of the codebase:

* **Structs:** The structs.py file contains a core class, GopherLine, used to decompose gophermap server responses.
* **Client:** The client.py file handles connection to the server.
* **Crawler:** The crawler.py file contains the code that performs the actual crawling of the server.
* **Identify:** The identify.py file contains code that is used to iterate through unique selectors identified while crawling the server.
* **Download:** The download.py file downloads identified Gopher targets from the server using the appropriate handlers.
* **Handlers:** The handlers folder contains several classes that handle downloading of supported item-types.
* **External Connect:** The external_connect.py file contains code that tests the connection to any external servers identified on the crawled server.
* **Stats:** The stats.py prints server statistics recorded over the course of the crawl.

Each file is documented using docstrings and comments. Docstrings are written in Sphinx style. All files are formatted using the PEP 8 style guide.

## Assumptions

The Gopher crawler makes the following assumptions:

* The gopher server respects the RFC 1436 standard [1] (e.g. text files are terminated by '.' CRLF, etc.).
* Text files are encoded in utf-8 format
* Downloadable files are downloaded and stored such that they duplicate the directory structure of the server, starting from your current working directory. Thus, if saving is set to True, download of filenames and server paths that are larger than the maximum supported path length of your operating system will fail.
* The printout of identified files includes files for which there were errors downloading/accessing. This can easily be modified by implementing a check whether the files associated ``GopherLine.error`` attribute is not None. Notably, in the downloading summary statistics, it is indicated to the user how many and for which files there were errors whilst downloading/accessing.

## Usage

Simply call the crawl function within ``crawler.py`` passing the appropriate service host (IP) and port.

> **Note:**

> The script requires Python>=3.10 due to the use of the typing module. There are no external dependencies.  

```py
from crawler import crawl

crawl(service_host="127.0.0.1", service_port=70, max_file_size=1e6, download_timeout=10, server_timeout=5, save=False)
```

Alternatively, you can call the function from the command line:

```py
python crawler.py comp3310.ddns.net 70 1e6 10 5 False
```

Each argument is described in the functions docstring:

```py
def crawl(
    service_host: str = "comp3310.ddns.net",
    service_port: int = 70,
    max_file_size: int = 1e6,
    download_timeout: int = 10,
    server_timeout: int = 5,
    save: bool = False,
):
    """
    Crawl a Gopher server - i.e. connect to the
    server, identify all Gopher targets, and
    download any identified binary (9), text (0)
    and image (I) files on the server.


    :param service_host:        IP of server to crawl, default comp3310.ddns.net.
    :type service_host:         str, optional
    :param service_port:        Port of server to crawl, default 70.
    :type service_port:         int, optional
    :param max_file_size:       Maximum allowable file size (bytes), default 1e6.
    :type max_file_size:        int
    :param download_timeout:    Allowable download time before timeout (seconds), default 10.
    :type download_timeout:     int
    :param server_timeout:      Time to wait for server response before timeout (seconds), default 5.
    :type server_timeout:       int
    :param save:                Specify whether saving of downloadable files is desired, default False.
    :type save:                 bool
    """
```

You will notice print-outs to the console documenting the status of the program (e.g. client server interactions, statistics, etc.).

If the save argument is set to True, the crawl function will download the identified Gopher targets into a folder called 'artifacts', placed within the current working directory. Inside the artifacts folder, the downloaded Gopher targets will be structured as per their selector on the server.

## Initial connection

Below, we document and decompose the initial transmission of the crawler and the response from the *"comp3310.ddns.net"* server.

<div align="center">
  <img src="data/init-trans.png" alt="Initial transmission" width="90%">
  <p><em><strong>Figure 1:</strong> Initial transmission (i.e. request).</em></p>
</div>

The conversation starts with the three-way handshake establishing the TCP connection.

Next, the initial message from the client (i.e. crawler) is sent to the server, requesting the top-level gophermap. This frame consists of 2-bytes in flight, so the ACK(nowledge) of the server's response jumps up by 2 (Frame 5). In frames 6 and 7, the server responds with the requested top-level gophermap. The cumulative TCP segment length of these 2 frames is 1771 bytes, so the ACK(nowledge) of the client's response (frame 8) jumps by 1771. The response occurs in 2 frames, because the total length of the response is larger than the standard Ethernet maximum transmission unit (MTU) of 1500 bytes (excluding headers).

In frame 9, the server initiates closing of the connection, which triggers a FIN(alise). In frames 10-11, the client ACK(nowledges) this FIN(alise) and sends it's own FIN(alise) as it has also finished transmitting. The server ACK(nowledges) this FIN(alise), completing the termination of the connection.

## Diving Deeper

The crawler code is built around an ``items`` dictionary, like such:

```py
items = {
        "0": [],
        "1": [],
        "2": [],
        "3": [],
        "4": [],
        "5": [],
        "6": [],
        "7": [],
        "8": [],
        "9": [],
        "+": [],
        "g": [],
        "I": [],
        "T": [],
    }
```

Each key in the dictionary corresponds to a Gopher type field, as outlined in [1]. Similar dictionaries are created to store malformed responses and responses hosted on external servers.

The containers corresponding to each key are populated with GopherLines. A GopherLine is created by instantiation with a line returned by the Gopher server with a valid Gopher type field. For example, if we send some submenu selector to the server that returns a gophermap containing the following line:

``0something-big.txt\t/something-big.txt\t11.20.168.192.in-addr.arpa\t70\t+\n``

we can create a GopherLine using this returned line like such:

```py
item = GopherLine(read_line='0something-big.txt\t/something-big.txt\t11.20.168.192.in-addr.arpa\t70\t+\n')
```

In it's ``__post_init__()``, the GopherLine will then automatically assign the following attributes:

```py
self.valid = True  # Flag to track if read_line is valid
self.error = None  # Attribute to store any error messages returned by server for this selector
self.read_line = '0something-big.txt\t/something-big.txt\t11.20.168.192.in-addr.arpa\t70\t+\n'
self.type_field = '0'
self.item_name = 'something-big.txt'
self.selector = '/something-big.txt'
self.host = '11.20.168.192.in-addr.arpa'
self.port = '70'
self.optional = '+'
self.size = 0  # Attribute to track size of downloaded item
self.crawled = False  # Flag to track if we have already crawled this selector
self.downloaded = False  # Flag to track if item was successfully downloaded
self.contents = None  # Attribute to store contents of smallest txt file
self.server_up = False  # Flag to track if external server is up
```

The ``self.valid`` attribute is a flag used to track whether the contents of the returned read_line are valid. The ``self.error`` attribute is used to store any errors associated with the read_line throughout the crawl. The next seven attributes simply store and decompose the read_line. The ``self.size`` attribute is used to store the size of the target if it is ever downloaded from the server. The ``self.downloaded`` attribute is a flag used to track whether the target has been downloaded. The ``self.crawled`` attribute is a flag used to track whether this section has already been crawled. This is necessary to prevent loops when crawling the server. The ``self.downloaded`` attribute is a flag is used to track whether a downloadable type file was successfully downloaded. The ``self.contents`` attribute is used to store the contents of the smallest downloaded text file. Finally, if the target is on an external server, the ``self.server_up`` attribute is a flag used to track whether the target was found to be online.

The GopherLine allows for simple storage and access of this information, greatly improving readability of any subsequent code. For example, we can now request the above target from the server by passing the ``self.selector`` attribute.

Another important class is the ``Client`` class. This class is used to abstract sending and receiving of replies from the server, further improving readability.

When the crawler is initiated, a ``Client`` class is created for the server. A GopherLine is created representing the top-level gophermap request (i.e. empty string - ""), and the ``identify()`` function is used to send this request to the server and decompose each line of the response (i.e. the top-level gophermap). Each line in the gophermap is appended to it's corresponding type field in the ``items`` dictionary.

> **Note:**

> Gophermap lines with item type, "i", are ignored as they do not contain any information that is relevant to the crawler.

A loop is then initiated that iterates through each menu item type (i.e. "1") in the items dictionary until they have all being crawled. Within the loop, the items dictionary is continually updated using the server responses, and the ``remove_repititions()`` function is used to remove duplictates, thereby repeated crawls of the same selector.

After the crawl is complete, downloading of all identified downloadable targets is attempted by the ``download()`` function. If the save argument is set to True, downloaded files are saved to the users (clients) device, replicating the directory structure of the Gopher server. Statistics are printed during the downloading process.

Next, connection is attempted to any identified exteral servers using the ``external_connect()`` function. The status of the connection is printed during this process.

Finally, a summary of statistics compiled over the course of the crawl is assembled and printed using the ``statistics()`` function.

## Flexibility

In computing, the robustness principle states, "*Be conservative in what you send and reasonably liberal in what you accept*" [2]. The crawler is written with this principle in mind.

The crawler prints any encountered errors to console as well as steps taken to address the errors.

Repitions are removed to prevent sending of duplicate requests to the same server.

At a minimum, responses need a type field, selector and host. Without these fields, the response is not useable to the crawler. If no port is specified in a gophermap line, the default Gopher port 70 is assigned. This is conveyed to the user through console printouts. Notably, commented code is left in the ``GopherLine`` class code that can be used to instead set such responses to invalid.

The crawler allows the user to set attributes like download timeout limit, server timeout limit and maximum acceptable filesize. This gives the user flexibility in how they want the crawler to behave for a particular server, rather then assuming the desired parameters.

In present form, the crawler only supports downloading of text, image and binary file types. Desired functionality for other type fields can easily be implemented by creating a unique handler and appending it to the ``handlers`` list in the ``download()`` function.

## Known Limitations and Edge-cases

If you send a text, image or binary file that begins with a utf-8 "3", it will be interpreted as an error. We could make this more robust by also requiring the client to match certain expected error phrases like "Error". This will not eliminate the problem, but will make the edge cases increasingly improbable.

## References

[1] Anklesaria, F., *et al.* (1993) *The Internet Gopher Protocol*. [Onine]. Available at: [www.rfc-editor.org](https://www.rfc-editor.org/rfc/rfc1436) [Accessed 2 Apr 2024].

[2] Postel, J. (1980) *DOD Standard Transmission Control Protocol*. [Online]. Available at: [datatracker.ietf.org](https://datatracker.ietf.org/doc/html/rfc761) [Accessed 24 Apr 2024].
