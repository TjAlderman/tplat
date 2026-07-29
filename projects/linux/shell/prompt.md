# Shell Prompt

The shell prompt shows that the shell is ready for input and often encodes the current user, host, and directory.

## Overview

- Prompt format usually includes user, host, and working directory
- `PS1` controls most Bash prompt formatting
- The ending symbol usually signals privilege level

## Reference

### Common symbols

| Symbol | Meaning |
| --- | --- |
| `~` | Home directory |
| `$` | Regular user |
| `#` | Root user |

### `PS1`

```bash
PS1="\u@\h[\w]\$ "
```

| Escape | Meaning |
| --- | --- |
| `\u` | Username |
| `\h` | Short hostname |
| `\H` | Full hostname |
| `\w` | Current working directory |
| `\d` | Date |
| `\D{format}` | Custom date format |
| `\t` | 24-hour time |
| `\T` | 12-hour time |
| `\@` | AM/PM time |
| `\j` | Number of jobs |
| `\s` | Shell name |
| `\n` | Newline |
| `\r` | Carriage return |

### Customisation and logging

- Prompt settings usually live in `~/.bashrc`
- `~/.bash_history` stores previously executed commands
- `script` records a full terminal session

### Minimal prompts

```bash
$
#
```

## Mental Model

- Prompt = context plus readiness indicator
- `PS1` defines the formatting
- Symbols such as `$` and `#` show privilege level
