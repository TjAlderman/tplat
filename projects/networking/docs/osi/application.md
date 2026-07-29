# Application Layer

The application layer defines the communication protocols and interface methods used by hosts in a network.

## HTTP

Hypertext Transfer Protocol (HTTP) lives at the application layer and enables cleartext communication between a client and server over TCP. HTTP commonly uses ports 80 and 8000.

| Method | Description |
| --- | --- |
| HEAD | Requests the same resource as `GET` without the response body. Useful for metadata and health checks. |
| GET | Reads data from the server. |
| POST | Submits data for processing. |
| PUT | Creates or replaces a resource at the target URI. |
| DELETE | Removes the resource at the target URI. |
| TRACE | Echoes the request for diagnostics. |
| OPTIONS | Reports the methods supported by the target resource. |
| CONNECT | Establishes a tunnel, usually through a proxy. |

## HTTPS

HTTP Secure (HTTPS) wraps HTTP in TLS so the conversation can be encrypted end to end. It commonly uses ports 443 and 8443 instead of port 80.

Once a session is initiated over TCP, a TLS `ClientHello` begins the handshake. The handshake negotiates parameters such as the session identifier, peer X.509 certificate, compression algorithm, cipher suite, session resumability, and shared master secret.

For more information on how HTTPS functions and how TLS performs security operations, see RFC 2246.

## FTP

File Transfer Protocol (FTP) is an application-layer protocol for transferring files between systems.

FTP uses ports 20 and 21 over TCP. Port 20 carries data, while port 21 carries control commands.

FTP can run in active or passive mode. In active mode, the client sends `PORT` and the server connects back to the chosen data port. In passive mode, the client sends `PASV` and waits for the server to provide the data connection details, which is useful when firewalls or NAT block direct inbound connections.

| Command | Description |
| --- | --- |
| USER | Logs in as a user. |
| PASS | Supplies the password. |
| PORT | Selects the active-mode data port. |
| PASV | Switches the session to passive mode. |
| LIST | Lists the files in the current directory. |
| CWD | Changes the current working directory. |
| PWD | Prints the current working directory. |
| SIZE | Returns the size of a file. |
| RETR | Retrieves a file from the server. |
| QUIT | Ends the session. |

For more information on FTP, see RFC 959.

## SMB

Server Message Block (SMB) is an application-layer protocol commonly used in Windows enterprise environments for sharing resources between hosts. It is connection-oriented and requires authentication so the user has permission to access or modify the resource. Modern SMB implementations use ports 445 and 139.

SMB provides easy access to resources such as printers, shared drives, and authentication servers, which also makes it attractive to attackers.
