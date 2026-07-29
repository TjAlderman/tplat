# Core Linux Commands

Common commands are easier to remember when grouped by discovery, inspection, navigation, and search.

## Overview

- `man` and `apropos` help you discover commands
- `which` resolves the executable that will run
- `find` is precise and real-time; `locate` is fast and indexed

## Reference

### Discovery

| Command | Purpose |
| --- | --- |
| `man` | Read manual pages |
| `apropos` | Search manual page descriptions by keyword |
| `explainshell` | External reference for command syntax |

### System inspection

| Command | Purpose |
| --- | --- |
| `whoami` | Print the current user |
| `id` | Show user and group IDs |
| `hostname` | Get or set the hostname |
| `uname` | Show kernel and system information |
| `pwd` | Print the current directory |
| `env` | Show or set environment variables |
| `ps` | Inspect processes |
| `who` | Show logged-in users |
| `lsof` | Show open files |
| `lsblk` | List block devices |
| `lsusb` | List USB devices |
| `lspci` | List PCI devices |

### Networking

| Command | Purpose |
| --- | --- |
| `ifconfig` | Legacy network interface tool |
| `ip` | Modern network interface tool |
| `netstat` | Legacy network status tool |
| `ss` | Inspect sockets |

### File and path utilities

| Command | Purpose |
| --- | --- |
| `ls` | List directory contents |
| `cd` | Change directory |
| `which` | Show the executable path for a command |

```bash
ls -l /etc
which python
```

`ls -a` includes hidden files. `cd -` returns to the previous directory.

### File search

```bash
find / -type f -name "*.conf" -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null
locate "*.conf"
sudo updatedb
```

| Option | Purpose |
| --- | --- |
| `-type f` | Search for files |
| `-name "*.conf"` | Match a filename pattern |
| `-user root` | Filter by owner |
| `-size +20k` | Match files larger than 20 KiB |
| `-newermt DATE` | Match files modified after a date |
| `-exec ... {}` | Run a command for each result |

| Tool | Strength |
| --- | --- |
| `find` | Real-time, flexible, slower |
| `locate` | Indexed, fast, may be stale |

## Mental Model

- Use `man` or `apropos` to discover commands
- Use `which` to verify what will run
- Use `find` for precise queries
- Use `locate` for fast broad searches
