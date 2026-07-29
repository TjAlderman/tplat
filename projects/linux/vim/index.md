# Vim

Vim is a modal, open-source text editor derived from `vi`. It is fast, keyboard-driven, and designed to work well with Unix tooling.

## Overview

- Lightweight and efficient
- Strong at composable text manipulation
- Steep learning curve, high long-term payoff

## Reference

### Design philosophy

- Edit text in Vim and delegate complex processing to external tools
- Compose small commands instead of reimplementing Unix utilities

### Modes

| Mode | Purpose |
| --- | --- |
| Normal | Default mode for navigation and commands |
| Insert | Text entry |
| Visual | Select text |
| Command (`:`) | Run single-line commands |
| Replace | Overwrite existing text |
| Ex | Batch command mode |

### Mode semantics

- Normal mode is the starting point and the main control plane
- Insert mode is for text entry via `i`, `a`, or `o`
- Visual mode supports character, line, and block selection
- Command mode runs commands such as saving or search and replace
- Replace mode overwrites existing characters
- Ex mode is a lower-level batch interface exposed through `:`

```vim
:w
:q
:wq
:%s/foo/bar/g
```

### Unix integration

```vim
:!grep pattern %
```

### Learning resource

```bash
vimtutor
```

```vim
:Tutorial
```

## Mental Model

- Normal mode = control
- Insert mode = data entry
- Visual mode = selection
- Command mode = batch operations
- Efficiency comes from fewer mode switches and small composable commands
