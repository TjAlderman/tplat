from sys import argv
from copy import deepcopy
from identify import identify, remove_repetitions
from client import Client
from external_connect import test_connection
from stats import statistics
from structs import GopherLine
from download import download


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
    # Create a client
    c = Client(
        service_host=service_host, service_port=service_port, timeout=server_timeout
    )

    # Create a dict to store items
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
    external_items = deepcopy(
        items
    )  # Dict to store responses hosted on external servers
    invalid_items = deepcopy(items)  # Dict to store malformed responses

    print(
        "\n"
        + "=" * 60
        + "\nInitiating crawl through server gopherholes...\n"
        + "=" * 60
        + "\n"
    )

    # Create top-level gophermap GopherLine
    top = GopherLine(read_line="1foo\t\tcomp3310.ddns.net\t70")
    top.crawled = True
    items["1"].append(top)
    # Identify targets in the top-level gophermap
    items = identify(
        client=c,
        items=items,
        external_items=external_items,
        invalid_items=invalid_items,
        target=top.selector,
    )

    # While we have not crawled all identified submenus
    while sum([submenu.crawled for submenu in items["1"]]) != sum(
        [submenu.valid for submenu in items["1"]]
    ):
        # Identify new targets in lower-level gophermaps
        for submenu in items["1"]:
            # Remove any new repeated submenu items
            items["1"] = remove_repetitions(items=items["1"])
            # And crawl them if we have not already done so
            if not submenu.crawled and submenu.valid:
                items = identify(
                    client=c,
                    target=submenu.selector,
                    items=items,
                    external_items=external_items,
                    invalid_items=invalid_items,
                )
                submenu.crawled = True

    print("\n" + "=" * 60 + "\nCrawl complete!\n" + "=" * 60 + "\n")

    # Remove any repeated items, then download all the unique downloadable targets
    for key, value in items.items():
        # Make sure we don't remove invalid items (type field "3"), because these are all
        # duplicates.
        if key == "3":
            pass
        else:
            items[key] = remove_repetitions(items=value)
    download(
        client=c,
        items=items,
        max_file_size=max_file_size,
        timeout=download_timeout,
        save=save,
    )

    # Test connection to external servers
    test_connection(items=external_items, timeout=server_timeout)

    # Report general statistics
    statistics(items, external_items, invalid_items)


if __name__ == "__main__":
    host = argv[1] if len(argv) >= 2 else "comp3310.ddns.net"  # Default host server
    port = int(argv[2]) if len(argv) >= 3 else 70  # Default host port
    max_file_size = (
        int(float(argv[3])) if len(argv) >= 4 else 1e6
    )  # Default maximum file size (bytes)
    download_timeout = (
        int(argv[4]) if len(argv) >= 5 else 10
    )  # Default time till download timeout (seconds)
    server_timeout = (
        int(argv[5]) if len(argv) >= 6 else 5
    )  # Default time till server connection timeout (seconds)
    save = (
        bool(argv[5]) if len(argv) >= 6 else False
    )  # Default condition whether to save accessed downloadable files.
    crawl(host, port, max_file_size, download_timeout, server_timeout, save)
    # crawl(
    #     "gopher.quux.org", 70, max_file_size, download_timeout, server_timeout, save
    # )  # gopher.quux.org
    print("\nDone.")
