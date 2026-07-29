import os
from handlers.txt import TextFileHandler
from handlers.im import ImageHandler
from handlers.bin import BinaryHandler
from client import Client
import time
from pathlib import Path


def download(client: Client, items: dict, max_file_size: int, timeout: int, save: bool):
    """
    Connect to the provided Client and download all
    downloadable items identified on the server.
    Save the items in a folder within the cwd called
    'artifacts', duplicating the selector structure
    of the server within the artifacts folder.

    :param client:          Client to connect to.
    :type client:           Client
    :param items:           Identified items (targets) on server.
    :type items:            dict
    :param max_file_size:   Maximum allowable file size (bytes)
    :type max_file_size:    int
    :param timeout:         Time to wait before aborting download (seconds).
    :type timeout:          int
    :param save:            Specify with saving of downloadable files is desired.
    :type save:             bool
    """
    # Print statistics of all downloadable type fields
    downloadable_keys = ["0", "2", "4", "5", "6", "9", "g", "I"]
    count = sum(len(items[key]) for key in downloadable_keys)
    print(
        "\n"
        + "=" * 60
        + f"\nIdentified {count} downloadable items on the Gopher server\n"
        + "Now attempting to download these items...\n"
        + "=" * 60
        + "\n"
    )

    # Handlers with which to download each type field.
    # If a handler is None, it (1) is not downloadable,
    # or, (2) downloading is not supported by this script.
    # Unsupported type fields can easily be built out
    # by creating a handler and adding it to the below list.
    handlers = [
        TextFileHandler,  # (0)
        None,  # (1) Menu entity
        None,  # (2) CSO Handler
        None,  # (3) Error condition
        None,  # (4) Macintosh BINHEX
        None,  # (5) PC-DOS binary file
        None,  # (6) unencoded
        None,  # (7) Index server
        None,  # (8) Telnet session
        BinaryHandler,  # (9)
        None,  # (+) Duplicated server
        None,  # (g) GIF
        ImageHandler,  # (I)
        None,  # (T) tn3270 telnet
    ]
    artifacts = list(items.values())
    smallest_txt_file = None

    # Time the total duration of downloading
    t1 = time.time()

    # Attempt to download each artifact
    for handler, artifact in dict(zip(handlers, artifacts)).items():
        # Skip type fields with no associated handler
        if handler is None:
            pass
        else:
            for item in artifact:
                # Initialise the handler
                initialised_handler = handler(client=client)
                # Create the save directory
                save_path = "artifacts" + item.selector
                parent_dir = str(Path(save_path).parent)
                if not os.path.exists(parent_dir) and save:
                    os.makedirs(parent_dir)
                # Download the item
                res = initialised_handler.download(
                    selector=item.selector,
                    save_path=save_path,
                    max_file_size=max_file_size,
                    timeout=timeout,
                    save=save,
                )
                # Print statistics
                if res[1] != False:
                    item.downloaded = True
                    item.size = len(res[0])
                    print(
                        " " * 12
                        + f"Successfully {'downloaded' if save else 'Accessed'}!"
                    )
                    # Store the contents of the smallest text file
                    if item.type_field == "0" and (
                        smallest_txt_file is None
                        or item.size < len(smallest_txt_file[0])
                    ):
                        smallest_txt_file = (
                            res[0].decode(encoding="utf-8"),
                            item.selector,
                        )
                else:
                    item.error = res[0]
                    print(" " * 12 + f"{'Downloaded' if save else 'Access'} failed!")

    # Print total duration of downloading
    seconds = time.time() - t1

    # Report download statistics
    success = 0
    for artifact in artifacts:
        success += sum([item.downloaded for item in artifact])
    print(
        "\n"
        + "=" * 60
        + f"\n{success}/{count} items were successfully {'downloaded' if save else 'accessed'} in {round(seconds,4)} second(s)\n"
        + "=" * 60
        + "\n"
    )

    # Preserve the contents of the smallest text file in memory. We only preserve
    # the contents of the smallest text file to prevent memory blowouts.
    for item in items["0"]:
        if item.selector == smallest_txt_file[1]:
            item.contents = smallest_txt_file[0]
