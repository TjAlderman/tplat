# Core Linux Commands

## `man`

Display manual pages for commands:

```bash
man ls
```

* Comprehensive reference (syntax, options, behaviour)
* Organized into sections (e.g., user commands, system calls)

## `apropos`

Search manual page descriptions by keyword:

```bash
apropos network
```

* Useful when you don’t know the exact command name

## External Resource

* explainshell — explains command syntax interactively

## Common System Commands

| Command    | Description                       |
| ---------- | --------------------------------- |
| `whoami`   | Print current user                |
| `id`       | Show user and group IDs           |
| `hostname` | Get/set system hostname           |
| `uname`    | System/kernel information         |
| `pwd`      | Print current directory           |
| `env`      | Show or set environment variables |

## Networking

| Command    | Description                                        |
| ---------- | -------------------------------------------------- |
| `ifconfig` | Configure/view network interfaces (legacy)         |
| `ip`       | Modern network configuration tool                  |
| `netstat`  | Network status (legacy)                            |
| `ss`       | Socket inspection (modern replacement for netstat) |

## Process & System Inspection

| Command | Description             |
| ------- | ----------------------- |
| `ps`    | Process status          |
| `who`   | Logged-in users         |
| `lsof`  | Open files by processes |

## Hardware Inspection

| Command | Description           |
| ------- | --------------------- |
| `lsblk` | Block devices (disks) |
| `lsusb` | USB devices           |
| `lspci` | PCI devices           |

## File & Path Utilities

### `ls`

List directory contents:

```bash
ls -l /etc
total 40
lrwxr-xr-x   1 timothyalder  staff   146 Apr 21 00:02 bazel-bin -> /Users/timothyalder/...
lrwxr-xr-x   1 timothyalder  staff   118 Apr 21 00:02 bazel-out -> /Users/timothyalder/...
...
```

First, we see the total amount of blocks (1024-byte) used by the files and directories listed in the current directory, which indicates the total size used. That means it used 40 blocks * 1024 bytes/block = 32,768 bytes (or 32 KB) of disk space. Next, we see a few columns that are structured as follows:

| Column Content | Description |
| --- | --- |
| lrwxr-xr-x | Type and permissions |
| 1 | Number of hard links to the file/directory |
| cry0l1t3 | Owner of the file/directory |
| timothyalder | Group owner of the file/directory |
| 146 | Size of the file or the number of blocks used to store the directory information |
| Apr 21 00:02 | Date and time |
| bazel-bin | Directory name |

Hidden contents (folders and files beginning with `.`) may be listed using `ls -a`

### `cd`

Navigate to directory ("choose directory"). `cd -` will return to the previous directory

### `which`

Locate executable in `$PATH`:

```bash
which python
```

* Returns the path of the command being executed

## File Search

### `find`

Search filesystem with filters and actions.

#### Example

```bash
find / -type f -name "*.conf" -user root -size +20k -newermt 2020-03-03 -exec ls -al {} \; 2>/dev/null
```

#### Key Options

| Option           | Description                            |
| ---------------- | -------------------------------------- |
| `-type f`        | Search for files (`d` for directories) |
| `-name "*.conf"` | Match filename pattern                 |
| `-user root`     | Filter by owner                        |
| `-size +20k`     | Files larger than 20 KiB               |
| `-newermt DATE`  | Modified after date                    |
| `-exec ... {}`   | Execute command per result             |
| `2>/dev/null`    | Suppress errors (not a `find` option)  |

#### Notes

* `{}` is replaced with each match
* `\;` terminates `-exec` (escaped to avoid shell interpretation)

### `locate`

Fast file search using indexed database:

```bash
locate "*.conf"
```

#### Update Database

```bash
sudo updatedb
```

#### Characteristics

| Feature       | `find`         | `locate`       |
| ------------- | -------------- | -------------- |
| Search Method | Real-time scan | Prebuilt index |
| Speed         | Slower         | Very fast      |
| Accuracy      | Always current | May be stale   |
| Filtering     | Advanced       | Limited        |

## Mental Model

* Use **`man` / `apropos`** for discovery
* Use **`which`** to resolve execution path
* Use **`find`** for precise, real-time queries
* Use **`locate`** for fast, broad searches
