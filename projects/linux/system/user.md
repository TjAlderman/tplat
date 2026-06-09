# User Management

User management covers accounts, groups, passwords, and privilege elevation.

## Overview

- Users can be created, modified, grouped, and removed
- `sudo` is the standard way to run a command with elevated privileges without logging in as root
- Group membership is a common way to grant shared access

## Reference

| Command | Purpose |
| --- | --- |
| `sudo` | Run a command as another user, usually root |
| `su` | Switch user and start a shell |
| `useradd` | Create a user |
| `userdel` | Remove a user |
| `usermod` | Modify a user account |
| `addgroup` | Add a group |
| `delgroup` | Remove a group |
| `passwd` | Change a password |

## Mental Model

- Users own access
- Groups share access
- `sudo` provides controlled privilege escalation
