# Regular Expressions (Regex)

Regex patterns match and filter text. In Linux they are commonly used with `grep`, `sed`, and `awk`.

## Overview

- Regex is compact and composable
- Start with simple patterns and add anchors or grouping only when needed
- Most mistakes come from precedence, escaping, or incorrect anchoring

## Reference

### Core constructs

| Pattern | Meaning |
| --- | --- |
| `.` | Any character |
| `*` | Zero or more of the previous token |
| `+` | One or more of the previous token |
| `?` | Zero or one of the previous token |
| `^` | Start of line |
| `$` | End of line |
| `\b` | Word boundary |
| `\w` | Word character |
| `[]` | Character class |
| `()` | Grouping |
| `\|` | OR operator |

### `grep` modes

| Option | Meaning |
| --- | --- |
| `grep` | Basic regex |
| `grep -E` | Extended regex; usually preferred |
| `grep -v` | Invert the match |

### Common patterns

| Use case | Pattern |
| --- | --- |
| Starts with a word | `^word` |
| Ends with a word | `word$` |
| Contains a word | `word` |
| Word boundary | `\bword\b` |
| Starts with A, ends with B | `^A.*B$` |
| A or B | `A\|B` |

### Examples

| Task | Command |
| --- | --- |
| Exclude comment lines | `grep -v '#' /etc/ssh/sshd_config` |
| Match words starting with `Permit` | `grep -E '\bPermit\w*' /etc/ssh/sshd_config` |
| Match words ending with `Authentication` | `grep -E '\w*Authentication\b' /etc/ssh/sshd_config` |
| Match lines containing `Key` | `grep 'Key' /etc/ssh/sshd_config` |
| Match lines starting with `Password` and containing `yes` | `grep -E '^Password.*yes' /etc/ssh/sshd_config` |
| Match lines ending with `yes` | `grep -E 'yes$' /etc/ssh/sshd_config` |

### Best practices

- Prefer `grep -E` for extended regex
- Avoid unnecessary `cat`; pipe the file directly into the command
- Build patterns incrementally and verify anchors and grouping

## Mental Model

- Regex matches text by combining anchors, quantifiers, and grouping
- `^` and `$` constrain position
- `*` and `+` control repetition
- Parentheses and `|` change matching logic
