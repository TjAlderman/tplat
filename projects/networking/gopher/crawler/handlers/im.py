from dataclasses import dataclass
from client import Client
from typing import Optional, Tuple
import socket
from time import time


@dataclass
class ImageHandler:
    """
    Dataclass that handles downloading of
    image files (I) from a Gopher server. Takes
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
        a image file. Save returned data at
        provided save_path.

        :param selector:        Selector to send to server to initiate
                                response of image file data.
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

            # Send a request for the image file
            self.client.send_request(selector + "\r\n")

            # Receive the image data from the server
            image_data = b""
            start = time()
            while True:
                data = self.client.sock.recv(4096)
                if not data:
                    break
                image_data += data
                if len(image_data) > max_file_size:
                    raise Exception(
                        "Download filesize exceeded maximum allowable size..."
                    )
                if (time() - start) > timeout:
                    raise Exception("Download exceeded maximum allowable time...")

            # Check for errors
            if image_data.decode("utf-8").startswith("3"):
                raise Exception(f'{image_data.decode("utf-8")}')

        # This bit is a little bit confusing, but it's actually good if we received
        # this exception. It means we weren't sent utf-8 error data, and so our
        # check for error raised an Exception because it treated the valid image
        # data as utf-8 data. This means we successfully downloaded the image, so
        # we want to save what we downloaded.
        except UnicodeDecodeError as e:
            # Save the received image data to a file
            if save:
                with open(save_path, "wb") as f:
                    f.write(image_data)
            return image_data, True

        # Other exception are actually bad, so we indicate the download failed.
        except Exception as e:
            # Redefine the socket.timeout error to distinguish it from a download timeout
            if str(e) == "timed out":
                e = "Server took too long to respond..."
            print(" " * 12 + f'Error occurred during download: "{e}"')
            return e, False  # Download failed
        finally:
            # Close the connection
            self.client.close()
