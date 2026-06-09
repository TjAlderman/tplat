# Permissions

Linux permissions control access to files and directories via a **user–group–others** model. Each filesystem object is associated with:

* **Owner (user)**
* **Group**
* **Permissions** defining allowed operations

Users can belong to multiple groups, inheriting access rights accordingly.

## Permission Types

| Symbol | Name    | Meaning                                       |
| ------ | ------- | --------------------------------------------- |
| `r`    | Read    | View file contents or list directory contents |
| `w`    | Write   | Modify file or directory contents             |
| `x`    | Execute | Run file or traverse directory                |

## Permission Scope

Permissions are defined for three classes:

| Scope      | Description               |
| ---------- | ------------------------- |
| User (u)   | File owner                |
| Group (g)  | Users in the file’s group |
| Others (o) | All other users           |

## Directory vs File Semantics

Permissions behave differently depending on object type.

### Files

* `r`: Read file contents
* `w`: Modify file contents
* `x`: Execute file (if binary/script)

### Directories

* `r`: List directory contents (`ls`)
* `w`: Create, delete, rename entries
* `x`: Traverse directory (`cd`, access entries)

**Important constraints:**

* Directory traversal **requires `x`**, regardless of `r`
* `x` on a directory **does not grant execution of contained files**
* Modifying directory contents requires **`w` on the directory**, not the files

## Permission Representation

Permissions are displayed via `ls -l`:

```bash
ls -l /etc/passwd

-rwxrw-r-- 1 root root 1641 May 4 23:42 /etc/passwd
```

### Breakdown

```
- rwx rw- r--
- --- --- ---
│  │   │   │
│  │   │   └── Others:  r--
│  │   └────── Group:   rw-
│  └────────── Owner:   rwx
└───────────── Type:    -
```

### Fields

| Segment       | Meaning                                          |
| ------------- | ------------------------------------------------ |
| `-`           | File type (`-` file, `d` directory, `l` symlink) |
| `rwx`         | Owner permissions                                |
| `rw-`         | Group permissions                                |
| `r--`         | Others permissions                               |
| `1`           | Number of hard links                             |
| `root root`   | Owner and group                                  |
| `1641`        | File size (bytes)                                |
| `May 4 23:42` | Last modified                                    |
| `/etc/passwd` | File path                                        |

## Octal (Numeric) Representation

Permissions map to octal values:

| Permission | Value |
| ---------- | ----- |
| `r`        | 4     |
| `w`        | 2     |
| `x`        | 1     |

Each scope is summed:

| Example       | Meaning |
| ------------- | ------- |
| `7` (`4+2+1`) | `rwx`   |
| `6` (`4+2`)   | `rw-`   |
| `5` (`4+1`)   | `r-x`   |
| `4`           | `r--`   |

### Example

```
rwxrw-r-- → 764
```

* Owner: `rwx` = 7
* Group: `rw-` = 6
* Others: `r--` = 4

## Modifying Permissions

We can modify permissions using the chmod command, permission group references (u - owner, g - Group, o - others, a - All users), and either a [+] or a [-] to add or remove the designated permissions. In the following example, let us assume we have a file called shell and we want to change permissions for it so this script is owned by that user, becomes not executable, and set with read/write permissions for all users.

```bash
cry0l1t3@htb[/htb]$ ls -l shell

-rwxr-x--x   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```

We can then apply read permissions for all users and see the result.

```bash
cry0l1t3@htb[/htb]$ chmod a+r shell && ls -l shell

-rwxr-xr-x   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```

We can also set the permissions for all other users to read only using the octal value assignment.

```bash
cry0l1t3@htb[/htb]$ chmod 754 shell && ls -l shell

-rwxr-xr--   1 cry0l1t3 htbteam 0 May  4 22:12 shell
```

## Change owner

To change the owner and/or the group assignments of a file or directory, we can use the chown command.

```bash
cry0l1t3@htb[/htb]$ chown <user>:<group> <file/directory>
```

## SUID and SGID

In addition to standard user and group permissions, Linux allows us to configure special permissions on files through the Set User ID (SUID) and Set Group ID (SGID) bits. These bits function like temporary access passes, enabling users to run certain programs with the privileges of another user or group.

The presence of these permissions is indicated by an s in place of the usual x in the file's permission set. When a program with the SUID or SGID bit set is executed, it runs with the permissions of the file's owner or group, rather than the user who launched it. This can be useful for certain system tasks but also introduces potential security risks if not used carefully.

## Sticky Bits

Sticky bits in Linux are like locks on files within shared spaces. When set on a directory, the sticky bit adds an extra layer of security, ensuring that only certain individuals can modify or delete files, even if others have access to the directory.

In a shared directory, this means only the file's owner, the directory's owner, or the root user (the system administrator) can delete or rename files. Other users can still access the directory but can’t modify files they don’t own.

```bash
cry0l1t3@htb[/htb]$ ls -l

drw-rw-r-t 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:30 scripts
drw-rw-r-T 3 cry0l1t3 cry0l1t3   4096 Jan 12 12:32 reports
```

In this example, we see that both directories have the sticky bit set. However, the reports folder has an uppercase T, and the scripts folder has a lowercase t.

If the sticky bit is capitalized (T), then this means that all other users do not have execute (x) permissions and, therefore, cannot see the contents of the folder nor run any programs from it. The lowercase sticky bit (t) is the sticky bit where the execute (x) permissions have been set.

## Mental Model

* **Ownership defines baseline control**
* **Groups extend access across users**
* **Permissions gate operations**
* **Directories control access to structure; files control access to content**
