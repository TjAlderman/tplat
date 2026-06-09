# Package Management

Packages are archives that contain binaries of software, configuration files, information about dependencies and keep track of updates and upgrades. The features that most package management systems provide are:

* Package downloading
* Dependency resolution
* A standard binary package format
* Common installation and configuration locations
* Additional system-related configuration and functionality
* Quality control

| Command | Description |
| --- | --- |
| dpkg | The dpkg is a tool to install, build, remove, and manage Debian packages. The primary and more user-friendly front-end for dpkg is aptitude. |
| apt | Apt provides a high-level command-line interface for the package management system. |
| aptitude | Aptitude is an alternative to apt and is a high-level interface to the package manager. |
| snap | Install, configure, refresh, and remove snap packages. Snaps enable the secure distribution of the latest apps and  utilities for the cloud, servers, desktops, and the internet of things. |
| gem | Gem is the front-end to RubyGems, the standard package manager for Ruby. |
| pip | Pip is a Python package installer recommended for installing Python packages that are not available in the Debian  archive. It can work with version control repositories (currently only Git, Mercurial, and Bazaar repositories), logs output extensively, and prevents partial installs by downloading all requirements before starting installation. |
| git | Git is a fast, scalable, distributed revision control system with an unusually rich command set that provides both  high-level operations and full access to internals. |

## Advanced Package Manager (APT)

Debian-based Linux distributions use the APT package manager. A package is an archive file containing multiple ".deb" files. The dpkg utility is used to install programs from the associated ".deb" file. APT makes updating and installing programs easier because many programs have dependencies. When installing a program from a standalone ".deb" file, we may run into dependency issues and need to download and install one or multiple additional packages. APT makes this easier and more efficient by packaging together all of the dependencies needed to install a program.

`/etc/apt/sources.list` points to the repositories a system may query for a desired package.

APT uses a database called the APT cache. This is used to provide information about packages installed on our system offline. We can search the APT cache, for example, to find all Impacket related packages.

```bash
tjalder@htb[/htb]$ apt-cache search impacket

impacket-scripts - Links to useful impacket scripts examples
polenum - Extracts the password policy from a Windows system
python-pcapy - Python interface to the libpcap packet capture library (Python 2)
python3-impacket - Python3 module to easily build and dissect network protocols
python3-pcapy - Python interface to the libpcap packet capture library (Python 3)
```
