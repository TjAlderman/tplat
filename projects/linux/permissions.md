# Permissions

Linux permissions use an owner, group, and others model to control access to files and directories.

## Overview

- Permission bits define read, write, and execute access
- Files and directories interpret those bits differently
- `chmod`, `chown`, and special bits modify access rules

## Reference

### Permission types

| Symbol | Meaning |
| --- | --- |
| `r` | Read |
| `w` | Write |
| `x` | Execute |

### Permission scope

| Scope | Meaning |
| --- | --- |
| `u` | Owner |
| `g` | Group |
| `o` | Others |

### File vs directory semantics

| Object | `r` | `w` | `x` |
| --- | --- | --- | --- |
| File | Read contents | Modify contents | Execute file |
| Directory | List entries | Create or remove entries | Traverse directory |

- Directory traversal requires `x`, even if `r` is set
- `x` on a directory does not mean you can execute files inside it
- Changing directory contents requires `w` on the directory itself

### Representation

```bash
ls -l /etc/passwd
-rwxrw-r-- 1 root root 1641 May 4 23:42 /etc/passwd
```

| Segment | Meaning |
| --- | --- |
| `-` | File type |
| `rwx` | Owner permissions |
| `rw-` | Group permissions |
| `r--` | Others permissions |
| `1` | Hard link count |
| `root root` | Owner and group |
| `1641` | File size |
| `May 4 23:42` | Last modified |

### Octal notation

| Value | Permission |
| --- | --- |
| `4` | Read |
| `2` | Write |
| `1` | Execute |

| Example | Meaning |
| --- | --- |
| `7` | `rwx` |
| `6` | `rw-` |
| `5` | `r-x` |
| `4` | `r--` |

```text
rwxrw-r-- = 764
```

### Modifying permissions

```bash
chmod a+r shell
chmod 754 shell
chown <user>:<group> <file-or-directory>
```

- `chmod` adds or removes permissions with symbolic or numeric modes
- `chown` changes the owner and optionally the group

### Special bits

- SUID and SGID run a program with the file owner's or group's privileges
- The sticky bit prevents users from deleting files they do not own in shared directories
- In `ls -l`, `s` replaces `x` for SUID or SGID, and `t` marks the sticky bit

## Mental Model

- Ownership sets the baseline
- Groups extend access
- Permission bits gate operations
- Special bits change how execution and deletion behave
