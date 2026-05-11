def statistics(items: dict, external_items: dict, invalid_items: dict):
    """
    Print statistics following server connection.
    Statistics include: number of identified Gopher
    directories, number of identified text files and
    list of their selectors, number of binary files
    and list of their selectors, number of invalid
    references, etc.


    :param items:           Dictionary of Gopher type fields paired with lists of GopherLine's.
    :type items:            dict
    :param external_items:  Dictionary of Gopher type fields paired with lists of external GopherLine's.
                            that are on external servers.
    :type external_items:   dict
    :param invalid_items:   Dictionary of Gopher type fields paired with lists of invalid GopherLine's.
                            that are on external servers.
    :type invalid_items:    dict
    """
    print("The following unique items were identified on the Gopher server:")

    # The number of identified Gopher directories
    print(
        "\t* "
        + f'{len(items["1"])} Gopher director{"y" if len(items["1"])==1 else "ies"}'
    )
    # The number of text files, and a list of all their selectors
    print(
        "\t* "
        + f'{len(items["0"])} text file{"" if len(items["0"])==1 else "s"}{"" if len(items["0"])==0 else ", found at:"}'
    )
    for item in items["0"]:
        print("\t\t" + item.selector)
    # The number of binary files, and a list of all their selectors
    print(
        "\t* "
        + f'{len(items["9"])} binary file{"" if len(items["9"])==1 else "s"}{"" if len(items["9"])==0 else ", found at:"}'
    )
    for item in items["9"]:
        print("\t\t" + item.selector)
    # The number of image files, and a list of all their selectors
    print(
        "\t* "
        + f'{len(items["I"])} image file{"" if len(items["I"])==1 else "s"}{"" if len(items["I"])==0 else ", found at:"}'
    )
    for item in items["I"]:
        print("\t\t" + item.selector)
    # The number of invalid references
    print(
        "\t* "
        + f'{len(items["3"])} invalid reference{"" if len(items["3"])==1 else "s"}'
    )
    # The number of malforned Gopher read_lines
    print(
        "\t* "
        + f'{sum([len(invalid_items[key]) for key in invalid_items.keys()])} malformed response{"" if len(invalid_items)==1 else "s"}'
    )

    # Text file statistics
    if len(items["0"]) != 0:
        # The contents of the smallest text file
        smallest = (items["0"][0].size, 0)
        for index, item in enumerate(items["0"]):
            if item.size < smallest[0] and item.downloaded:
                smallest = (item.size, index)
        print(
            f'\nThe smallest downloaded text file was: "{items["0"][smallest[1]].selector}",\nwith a size of {items["0"][smallest[1]].size} bytes. The contents of this file were:\n\t"{items["0"][smallest[1]].contents}"'
        )
        # The size of the largest text file
        largest = (items["0"][0].size, 0)
        for index, item in enumerate(items["0"]):
            if item.size > largest[0] and item.downloaded:
                largest = (item.size, index)
        print(
            f'\nThe largest downloaded text file was: "{items["0"][largest[1]].selector}",\nwith a size of {items["0"][largest[1]].size} bytes.'
        )

    # Binary file statistics
    if len(items["9"]) != 0:
        # The size of the smallest binary file
        smallest = (items["9"][0].size, 0)
        for index, item in enumerate(items["9"]):
            if item.size < smallest[0] and item.downloaded:
                smallest = (item.size, index)
        print(
            f'\nThe smallest downloaded binary file was: "{items["9"][smallest[1]].selector}"\nwith a size of {items["9"][smallest[1]].size} bytes.'
        )
        # The size of the largest binary files
        largest = (items["9"][0].size, 0)
        for index, item in enumerate(items["9"]):
            if item.size > largest[0] and item.downloaded:
                largest = (item.size, index)
        print(
            f'\nThe largest downloaded binary file was: "{items["9"][largest[1]].selector}"\nwith a size of {items["9"][largest[1]].size} bytes.'
        )

    # Error statistics
    print("\nThe following errors were enecountered while crawling the Gopher server:")
    for item_class in [items, invalid_items, external_items]:
        for item_type in item_class.keys():
            for item in item_class[item_type]:
                if item.error is not None:
                    print(12 * " " + "* " + f'{item.selector}: "{item.error}"')
