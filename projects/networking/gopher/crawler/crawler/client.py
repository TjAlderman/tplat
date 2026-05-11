from socket import socket, AF_INET, SOCK_STREAM
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Client:
    """
    A dataclass designed to provide simple
    connection to a server via the socket API.
    The class takes an IP (service_host) and
    port (service_port) upon instantiation.

    :param service_host: IP or DNS address of host server.
    :type service_host: str
    :param service_port: Port on host server to connect to.
    :type service_port: int
    :param timeout: Time to wait for server response (seconds).
    :type timeout: int
    """

    service_host: str
    service_port: int
    timeout: int

    def __post_init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.settimeout(self.timeout)

    def connect(self):
        """
        Connect to the server.
        """
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.sock.connect((self.service_host, self.service_port))

    def close(self):
        """
        Close connection to the server.
        """
        self.sock.close()

    def send_request(self, request):
        """
        Send a request to a server.
        """

        time = datetime.now().strftime("%H:%M:%S")
        stripped = request.strip("\r\n")
        print(f'{time} || Sending request to server: "{stripped}"')
        with self.sock.makefile("w") as sock_file:
            sock_file.writelines([request])
            sock_file.flush()
        print(" " * 12 + "Request sent...")

    def read_reply(self):
        """
        Read and print response from server
        until empty str is returned.
        """

        with self.sock.makefile("r") as sock_file:
            reply = []
            while True:
                new_reply = sock_file.readline()
                if new_reply == "":
                    break
                else:
                    reply.append(new_reply)
            print(" " * 12 + "Reply received!", end="\n")
            return reply
