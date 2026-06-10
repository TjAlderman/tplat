# Application Layer

An application layer is an abstraction layer that specifies the shared communication protocols and interface methods used by hosts in a communications network.

## HTTP

Hyper text transfer protocol (HTTP) lives at the application layer, and enables the transfer of data in clear text between a client and server over TCP. HTTP uses ports 80 or 8000. To perform operations such as fetching webpages, requesting items for download, or posting your most recent tweet all require the use of specific methods.

| Method | Description |
| --- | --- |
| HEAD | **required** is a safe method that requests a response from the server similar to a Get request except that the message body is not included. It is a great way to acquire more information about the server and its operational status. |
| GET | **required** Get is the most common method used. It requests information and content from the server. For example, GET http://10.1.1.1/Webserver/index.html requests the index.html page from the server based on our supplied URI. |
| POST | **optional** Post is a way to submit information to a server based on the fields in the request. For example, submitting a message to a Facebook post or website forum is a POST action. The actual action taken can vary based on the server, and we should pay attention to the response codes sent back to validate the action. |
| PUT | **optional** Put will take the data appended to the message and place it under the requested URI. If an item does not exist there already, it will create one with the supplied data. If an object already exists, the new PUT will be considered the most up-to-date, and the object will be modified to match. The easiest way to visualize the differences between PUT and POST is to think of it like this; PUT will create or update an object at the URI supplied, while POST will create child entities at the provided URI. The action taken can be compared with the difference between creating a new file vs. writing comments about that file on the same page. |
| DELETE | **optional** Delete does as the name implies. It will remove the object at the given URI. |
| TRACE | **optional** Allows for remote server diagnosis. The remote server will echo the same request that was sent in its response if the TRACE method is enabled. |
| OPTIONS | **optional** The Options method can gather information on the supported HTTP methods the server recognizes. This way, we can determine the requirements for interacting with a specific resource or server without actually requesting data or objects from it. |
| CONNECT | **optional** Connect is reserved for use with Proxies or other security devices like firewalls. Connect allows for tunneling over HTTP. (SSL tunnels) |

## HTTPS

HTTP secure (HTTPS) is a modification of the HTTP protocol designed to utilise transport layer security (TLS). TLS can wrap regular HTTP traffic within TLS, which means that we can encrypt our entire conversation, not just the data sent or requested. Even though it is HTTP at its base, HTTPS utilizes ports 443 and 8443 instead of the standard port 80.

Once a session is initiated via TCP, a TLS ClientHello is sent next to begin the TLS handshake. During the handshake, several parameters are agreed upon, including session identifier, peer x509 certificate, compression algorithm to be used, the cipher spec encryption algorithm, if the session is resumable, and a 48-byte master secret shared between the client and server to validate the session.

For more information on how HTTPS functions and how TLS performs security operations, see RFC 2246.

## FTP

File Transfer Protocol (FTP) is an Application Layer protocol that enables quick data transfer between computing devices. 

FTP is unique since it utilizes multiple ports at a time. FTP uses ports 20 and 21 over TCP. Port 20 is used for data transfer, while port 21 is utilized for issuing commands controlling the FTP session.

FTP is capable of running in two different modes, active or passive. Active is the default operational method utilized by FTP, meaning that the server listens for a control command PORT from the client, stating what port to use for data transfer. Passive mode enables us to access FTP servers located behind firewalls or a NAT-enabled link that makes direct TCP connections impossible. In this instance, the client would send the PASV command and wait for a response from the server informing the client what IP and port to utilize for the data transfer channel connection.

| Command | Description |
| --- | --- |
| USER | specifies the user to log in as. |
| PASS | sends the password for the user attempting to log in. |
| PORT | when in active mode, this will change the data port used. |
| PASV | switches the connection to the server from active mode to passive. |
| LIST | displays a list of the files in the current directory. |
| CWD | will change the current working directory to one specified. |
| PWD | prints out the directory you are currently working in. |
| SIZE | will return the size of a file specified. |
| RETR | retrieves the file from the FTP server. |
| QUIT | ends the session. |

For more information on FTP, see RFC 959.

## SMB

Server message block is an application layer protocol most widely seen in Windows enterprise environments that enables sharing resources between hosts over common networking architectures. SMB is a connection-oriented protocol that requires user authentication from the host to the resource to ensure the user has correct permissions to use that resource or perform actions. Previously, SMB used ports 137 and 138. Modern SMB implementations use ports 445 and 139.

**As a user, SMB provides us easy and convenient access to resources like printers, shared drives, authentication servers, and more. For this reason, SMB is very attractive to potential attackers as well.**
