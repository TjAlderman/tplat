from dataclasses import dataclass
from client import Client
from typing import Optional, Tuple
from time import time


@dataclass
class BinaryHandler:
    """
    Dataclass that handles downloading of
    binary files (9) from a Gopher server. Takes
    an instantiated Client as input.
    """

    client: Client

    def download(
        self,
        selector: str,
        save_path: str,
        max_file_size: int,
        timeout: int,
        save: bool,
    ) -> Tuple[Optional[int], Optional[bool]]:
        """
        Send selector to server corresponding to
        a binary file. Save returned data at
        provided save_path.

        :param selector:        Selector to send to server to initiate
                                response of binary file data.
        :type selector:         str
        :param save_path:       Path to save downloaded data at.
        :type save_path:        str
        :param max_file_size:   Maximum allowable file size (bytes)
        :type max_file_size:    int
        :param timeout:         Time to wait before aborting download (seconds).
        :type timeout:          int
        :param save:            Specify if saving of downloadable files is desired.
        :type save:             bool
        :return:                Tuple indicating whether access/download was
                                successful, as well as size of
                                accessed/downloaded data (specified in bytes)
        :rtype:                 Tuple[Optional[int], Optional[bool]]
        """
        try:
            # Connect to the Gopher server
            self.client.connect()

            # Send a request for the text file
            self.client.send_request(selector + "\r\n")

            # Receive the text data from the server
            binary_data = b""
            start = time()
            while True:
                data = self.client.sock.recv(4096)
                if not data:
                    break
                binary_data += data
                if len(binary_data) > max_file_size:
                    raise Exception(
                        "Download filesize exceeded maximum allowable size..."
                    )
                if (time() - start) > timeout:
                    raise Exception("Download exceeded maximum allowable time...")

            # Check for errors
            if binary_data.decode("utf-8").startswith("3"):
                raise Exception(f'{binary_data.decode("utf-8")}')

            # Save the received text data to a file
            if save:
                with open(save_path, "wb") as f:
                    f.write(binary_data)
            return binary_data, True  # Download succeeded

        # Similar to the image download handler, this is confusing. We only try to decode
        # the data to confirm that an error message wasn't returned. If it wasn't, we
        # assume that the format of the downloaded data is correct. For example, a .so
        # or .dll binary file will return a decode error, but that doesn't mean the download
        # failed. The only data handler that doesn't need to handle this Exception in a special
        # way is the text handler, because a decode error for a text file explicitly means the
        # download failed.
        except UnicodeDecodeError as e:
            # Save the received text data to a file
            if save:
                with open(save_path, "wb") as f:
                    f.write(binary_data)
            return binary_data, True  # Download succeeded

        except Exception as e:
            # Redefine the socket.timeout error to distinguish it from a download timeout
            if str(e) == "timed out":
                e = "Server took too long to respond..."
            print(" " * 12 + f'Error occurred during download: "{e}"')
            return e, False  # Download failed
        finally:
            # Close the connection
            self.client.close()
