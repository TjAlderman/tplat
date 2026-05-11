from structs import GopherLine
from collections import defaultdict
from typing import *
from client import Client


def remove_repetitions(items: List[GopherLine]) -> List[GopherLine]:
    """
    Takes a list of GoperLine's as input.
    Removes any repititions (i.e. GopherLine's
    with identical selector attributes), and
    returns a list of the unique GopherLine's.

    :param items:   List of GopherLine's
    :type items:    List[GopherLine]
    :return:        List of unique GopherLine's
    :rtype:         List[GopherLine]
    """
    # Create a dictionary whose keys are the unique selector(s)
    item_dict = defaultdict(list)
    for item in items:
        item_dict[item.selector].append(item)

    # Check whether we already crawled this submenu (selector)
    for key, value in item_dict.items():
        if len(value) > 1:
            crawled_status = any(item.crawled for item in value)
            # We really only care about the host, port and selector.
            # The identify() code creates unique dicts based on hosts
            # and ports, so we can assume that each item in item_dict[key]
            # has the same host and port. For the remainder of this
            # function, we will choose item[0] to be our 'master'.
            # We can discard all the other items, because they
            # do not introduce any pertinent new information.

            # Set the master item crawled flag to the crawled status
            item_dict[key][0].crawled = crawled_status

    # Return a single list of unique master items
    unique_items = [item_list[0] for item_list in item_dict.values()]

    return unique_items


def identify(
    client: Client,
    items: dict,
    external_items: dict,
    invalid_items: dict,
    target: str = "",
) -> dict:
    """
    Connect to the provided Client, send the
    provided target (selector) to the Client, and iterate
    through lines in the response, storing any
    any items of Gopher targets in the provided
    items dictionary as GopherLines, with dict
    key corresponding to their Gopher type field.

    :param client:          Instantiated Client to connect to.
    :type client:           Client
    :param items:           Dictionary to store the returned Gopher targets.
    :type items:            dict
    :param external_items:  Dictionary to store the returned Gopher targets
                            that are on external servers.
    :type external_items:   dict
    :param invalid_items:   Dictionary to store the returned Gopher targets
                            that are on external servers.
    :type invalid_items:    dict
    :param target:          Target to send to the server, defaults to "".
    :type target:           str, optional
    :return:                The updated items dictionary.
    :rtype:                 dict
    """

    try:
        # Connect to the server
        client.connect()

        # Fetch the gophermap from the target directory and close the connection
        client.send_request(target + "\r\n")
        reply = client.read_reply()
        client.close()

        # Identify all items in the gophermap
        for line in reply:
            for key in list(items.keys()):
                if line[0] == key:
                    result = GopherLine(line)
                    # Invalid type field won't have a host or port,
                    # so we deal with this edge-case manually
                    if key == "3":
                        result.valid = False
                        items[key].append(result)
                    # Well-behaving responses
                    elif (
                        result.valid
                        and result.host == client.service_host
                        and result.port == client.service_port
                    ):
                        items[key].append(result)
                    # Malformed responses for which GopherLine
                    # cannot successfully decompose (e.g.
                    # missing server, selector, or type field)
                    elif not result.valid:
                        invalid_items[key].append(result)
                    # Responses hosted on external servers
                    else:
                        external_items[key].append(result)

        # Remove any new repeated submenu items
        items["1"] = remove_repetitions(items=items["1"])
        # Return the unique identified items
        return items

    except Exception as e:
        # Redefine the socket.timeout error for consistency with download error reporting
        if str(e) == "timed out":
            e = "Server took too long to respond... If you think this is a mistake, try increasing the server_timeout argument"
        print(" " * 12 + f'Error occured during identify: "{e}"')
        raise Exception(" " * 12 + f'Error occured during identify: "{e}"')
