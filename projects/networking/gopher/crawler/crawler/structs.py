from dataclasses import dataclass


@dataclass
class GopherLine:
    """
    A dataclass designed to store information contained
    in a Gopher target for convenient accessing.

    :param read_line:   A single line of the servers response to a selector
    :type read_line:    str
    """

    read_line: str

    def __post_init__(self) -> bool:
        self.valid = True  # Flag to track if read_line is valid
        self.error = None  # Attribute to store any error messages returned by server for this selector
        self.read_line = self.read_line.strip("\n")  # Strip Gopher artifacts
        components = self.read_line.split("\t")
        self.type_field = components[0][0]
        self.item_name = components[0][1:]
        self.selector = components[1]
        if len(components) >= 3 and len(components[2]) > 0:
            self.host = components[2]
        else:
            self.error = (
                "Invalid reply. No host, so discarding discarding this result..."
            )
            print(
                " " * 12
                + f'Warning! Invalid reply: "{self.read_line}"\n'
                + " " * 12
                + "Returned no host. Discarding this result..."
            )
            self.valid = False
        # Only check for port if host was successfully identified
        if self.valid and len(components) >= 4 and len(components[3]) > 0:
            self.port = int(components[3])
        elif self.valid:
            self.port = 70
            self.error = "Invalid reply. No port, so setting to default port 70..."
            print(
                " " * 12
                + f'Warning! Invalid reply: "{self.read_line}"\n'
                + " " * 12
                + "Returned no port. Setting to default port 70..."
            )
            # print(
            #     " " * 12
            #     + f'Warning! Returned the following invalid result: "{self.read_line}"'
            #     + " " * 12
            #     + "No port was returned, so discarding this result..."
            # )
            # self.valid = False
        # Only check for optional if port host and port were successfully identified
        self.optional = (
            components[4] if self.valid and len(components) == 5 else None
        )  # Optional field that may be in gophermap response
        self.size = 0  # Attribute to track size of downloaded item
        self.crawled = False  # Flag to track if we have already crawled this selector
        self.downloaded = False  # Flag to track if downloadable item was successfully accessed/downloaded
        self.contents = None  # Attribute to store contents of smallest txt file
        self.server_up = False  # Flag to track if external server is up
