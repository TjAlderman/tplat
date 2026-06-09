# Shell

A shell is the command interpreter between the user and the kernel.

## Overview

- A terminal emulator provides the GUI surface
- The shell parses commands, runs programs, and manages I/O
- The kernel executes the underlying work

## Reference

### Terminal terms

| Term | Meaning |
| --- | --- |
| Terminal | Interface for interacting with a shell |
| Console | Physical or virtual text display |
| Terminal emulator | GUI application for running shell sessions |

### Terminal emulators

- GNOME Terminal
- iTerm2
- Windows Terminal

### Common shells

| Shell | Description |
| --- | --- |
| Bash | Default on many Linux systems |
| Zsh | Extended shell with more UX features |
| Fish | User-friendly modern shell |
| KornShell | Advanced scripting features |
| Tcsh | C-shell derivative |

## Mental Model

- Terminal = interface
- Shell = interpreter
- Kernel = execution layer

```text
User -> Terminal -> Shell -> Kernel -> Hardware
```
