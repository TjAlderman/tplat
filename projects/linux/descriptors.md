# File Descriptors and Redirection

File descriptors provide a uniform way for processes to read and write streams.

## Overview

- `0` is stdin, `1` is stdout, and `2` is stderr
- Redirection rewires those streams to files or `/dev/null`
- Pipes connect the output of one command to the input of another

## Reference

### Standard file descriptors

| FD | Name | Purpose |
| --- | --- | --- |
| `0` | STDIN | Standard input |
| `1` | STDOUT | Standard output |
| `2` | STDERR | Standard error |

### Redirection

| Operator | Meaning |
| --- | --- |
| `>` | Overwrite a file with stdout |
| `>>` | Append stdout to a file |
| `<` | Use a file as stdin |
| `2>` | Redirect stderr |
| `1>` | Redirect stdout explicitly |

```bash
find /etc/ -name networks 2>/dev/null
find /etc/ -name networks > results.txt
find /etc/ -name networks 2>/dev/null 1>stdout.txt
cat < stdout.txt
```

### Here documents

```bash
cat << EOF >> stream.txt
My
Input
Stream
EOF
```

### Pipes

```bash
find /etc/ -name "*.conf" 2>/dev/null | grep systemd | wc -l
```

## Mental Model

- Each process reads from FD `0` and writes to FD `1` or `2`
- Redirection changes where those streams go
- Pipes build dataflow pipelines between commands
- `/dev/null` is a sink for discarded output
