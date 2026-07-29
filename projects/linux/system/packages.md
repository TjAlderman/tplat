# Package Management

Package managers install software, resolve dependencies, and keep systems updated.

## Overview

- Packages bundle binaries, configuration, and dependency metadata
- Package managers add install, remove, upgrade, and repository workflows
- Debian-based systems commonly use `dpkg` and `apt`

## Reference

### Common tools

| Command | Purpose |
| --- | --- |
| `dpkg` | Install and manage Debian package files |
| `apt` | High-level package manager for Debian-based systems |
| `aptitude` | Alternative front end for Debian package management |
| `snap` | Install and manage snap packages |
| `gem` | Manage Ruby packages |
| `pip` | Install Python packages |
| `git` | Distributed version control and source retrieval |

### APT

- `dpkg` works with local `.deb` files
- `apt` handles dependency resolution through repositories
- `/etc/apt/sources.list` defines the repositories a system can query
- `apt-cache` searches the local package cache

```bash
apt-cache search impacket
```

## Mental Model

- Use `dpkg` for package files and `apt` for dependency-aware installs
- Repository metadata is as important as the package itself
- Package managers trade manual effort for repeatable installation and updates
