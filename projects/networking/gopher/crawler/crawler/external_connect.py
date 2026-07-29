from client import Client
from datetime import datetime


def test_connection(items: dict, timeout: int):
    """
    _summary_

    :param items:       Dictionary of GopherLines belonging to external servers
    :type items:        dict
    :param timeout:     Time to wait for server response before timeout (seconds)
    :type timeout:      int
    """
    external_servers = {}
    # For every item
    for key, value in items.items():
        for item in value:
            # Identify the valid, unique external servers
            if hasattr(item, "host") and hasattr(item, "port") and item.valid:
                if (item.host not in list(external_servers.keys())) and (
                    item.port not in list(external_servers.values())
                ):
                    external_servers[item.host] = {"port": item.port, "up": False}

    # Remove any duplicates (i.e. references to the same external server)
    unique_servers = {}
    for key, value in external_servers.items():
        port = value["port"]
        unique_key = (key, port)
        unique_servers[unique_key] = value
    formatted_unique_servers = {}
    for key, value in unique_servers.items():
        formatted_unique_servers[key[0]] = value

    print(
        "\n"
        + "=" * 60
        + f"\nIdentified {len(formatted_unique_servers)} external servers referenced on the Gopher server\n"
        + "Now attempting to connect to these...\n"
        + "=" * 60
        + "\n"
    )

    # See if they're up
    success = len(formatted_unique_servers)
    invalid = 0
    for host, value in formatted_unique_servers.items():
        c = Client(host, value["port"], timeout=timeout)
        time = datetime.now().strftime("%H:%M:%S")
        print(
            f'{time} || Attempting to connect to host: "{host}", port: "{value["port"]}"'
        )
        try:
            c.connect()
            c.close()
            formatted_unique_servers[host]["up"] = True
            print(" " * 12 + "Successfully connected!")
        except Exception as e:
            # Redefine the socket.timeout error to distinguish it from a download timeout
            if str(e) == "timed out":
                e = "Server took too long to respond..."
            # If the error wasn't a timeout error, then the server reference was invalid
            else:
                e = "Invalid server reference..."
                invalid += 1
            # Count total number of errors
            success -= 1
            # Print the error to stdout
            print(" " * 12 + f'Error occured during connection: "{e}"')
            print(" " * 12 + "Connection failed!")

    print(
        "\n"
        + "=" * 60
        + f"\n{success}/{len(formatted_unique_servers)-invalid} of the valid external server references were up"
        + f"\n{invalid}/{len(formatted_unique_servers)} of the external server references were invalid\n"
        + "=" * 60
        + "\n"
    )
