# Service and Process Management

Services and processes are background workloads controlled with `systemd`, signals, and job control.

## Overview

- Services can be started, stopped, restarted, enabled, and inspected
- Processes are identified by PIDs and may have parent processes
- Job control and command chaining are common shell workflows

## Reference

### `systemctl`

- `start`, `stop`, `restart`, and `status` control service state
- `enable` makes a service start at boot
- `systemctl list-units --type=service` shows active services

```bash
systemctl list-units --type=service
```

### Process control

- Common states: running, waiting, stopped, zombie
- `kill`, `pkill`, `pgrep`, and `killall` send signals or locate processes
- `kill -l` lists available signals

### Job control

- `Ctrl+Z` suspends the current job
- `jobs` lists suspended or background jobs
- `bg` resumes a job in the background
- `fg <id>` returns a job to the foreground
- `&` runs a command in the background immediately

### Command chaining

- `;` runs commands sequentially
- `&&` runs the next command only on success
- `|` sends stdout from one command to the next

## Mental Model

- `systemd` manages service lifecycle on most modern distributions
- PIDs identify running processes and `/proc` exposes process details
- Signals request state changes; jobs manage interactive shell work
- Simple commands become more powerful when chained together
