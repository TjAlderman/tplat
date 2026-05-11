from dataclasses import dataclass
from client import Client
from typing import Optional, Tuple
import socket
from time import time


@dataclass
class TextFileHandler:
    """
    Dataclass that handles downloading of
    text files (0) from a Gopher server. Takes
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
        a text file. Save returned data at
        provided save_path.

        :param selector:        Selector to send to server to initiate
                                response of text file data.
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
            text_data = b""
            start = time()
            while True:
                data = self.client.sock.recv(4096)
                if not data:
                    break
                text_data += data
                if len(text_data) > max_file_size:
                    raise Exception(
                        "Download filesize exceeded maximum allowable size..."
                    )
                if (time() - start) > timeout:
                    raise Exception("Download exceeded maximum allowable time...")

            # Check for errors
            if text_data.decode("utf-8").startswith("3"):
                raise Exception(f'{text_data.decode("utf-8")}')

            # Remove the Gopher protocol artifacts (".\r\n")
            if bytes(text_data[-3:]) == b".\r\n":
                text_data = text_data[:-3]
            # Otherwise, indicate improper termination
            else:
                raise Exception("File terminated improperly...")

            # Save the received text data to a file
            if save:
                with open(save_path, "wb") as f:
                    f.write(text_data)

            return text_data, True  # Download succeeded
        except Exception as e:
            # Redefine the socket.timeout error to distinguish it from a download timeout
            if str(e) == "timed out":
                e = "Server took too long to respond..."
            print(" " * 12 + f'Error occurred during download: "{e}"')
            return e, False  # Download failed
        finally:
            # Close the connection
            self.client.close()
