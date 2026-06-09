# Task Scheduling

Task scheduling runs commands later, repeatedly, or at boot.

## Overview

- `systemd` timers are the native option on modern Linux systems
- cron is a simple, time-based scheduler that remains widely used

## Reference

### `systemd` timers

- A timer unit usually has a matching service unit
- `OnBootSec` runs once after boot
- `OnUnitActiveSec` repeats after the previous run
- Reload unit files with `systemctl daemon-reload`

```ini
[Unit]
Description=My Timer

[Timer]
OnBootSec=3min
OnUnitActiveSec=1hour

[Install]
WantedBy=timers.target
```

```ini
[Unit]
Description=My Service

[Service]
ExecStart=/full/path/to/my/script.sh

[Install]
WantedBy=multi-user.target
```

### Cron

| Field | Values |
| --- | --- |
| Minute | `0-59` |
| Hour | `0-23` |
| Day of month | `1-31` |
| Month | `1-12` |
| Day of week | `0-7` |

```cron
0 */6 * * * /path/to/update_software.sh
0 0 1 * * /path/to/scripts/run_scripts.sh
0 0 * * 0 /path/to/scripts/clean_database.sh
0 0 * * 7 /path/to/scripts/backup.sh
```

## Mental Model

- Use timers when you want native `systemd` integration
- Use cron when you want compact recurring schedules
- Prefer the simplest scheduler that fits the job
