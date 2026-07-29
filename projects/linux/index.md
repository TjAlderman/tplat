# Linux

Linux is an open-source operating system built around the Linux kernel. Distributions combine the kernel with userland tools, package managers, and default configuration.

## Overview

- Strong permission model and generally good performance
- Stable and modular, with many configuration options
- Trade-offs include a steeper learning curve and uneven hardware support

## Reference

### Core design principles

| Principle | Meaning |
| --- | --- |
| Everything is a file | Devices, processes, and resources are exposed through file-like interfaces |
| Small tools | Commands usually do one thing well |
| Composability | Pipelines combine simple tools into larger workflows |
| Shell-first interaction | The CLI is the primary control surface |
| Text configuration | Most system settings live in plain text files |

### System components

| Component | Role |
| --- | --- |
| Bootloader | Loads the kernel at startup |
| Kernel | Manages hardware and system calls |
| Daemons | Run background services |
| Shell | Accepts and runs commands |
| Graphics server | Provides graphical display support |
| Desktop environment | Supplies the GUI layer |
| Utilities | Provide user-facing tools |

### Filesystem hierarchy

| Path | Purpose |
| --- | --- |
| `/` | Root of the filesystem tree |
| `/bin` | Essential user binaries |
| `/boot` | Bootloader and kernel files |
| `/dev` | Device files |
| `/etc` | System configuration |
| `/home` | User home directories |
| `/lib` | Shared libraries |
| `/mnt` | Temporary mount point |
| `/opt` | Optional third-party software |
| `/root` | Root user's home directory |
| `/usr` | User-space programs and documentation |
| `/var` | Variable data such as logs and caches |

## Mental Model

- The kernel abstracts hardware into manageable resources
- The filesystem exposes those resources in a unified tree
- The shell and utilities manipulate that tree
- Linux workflows are built from small commands composed together
