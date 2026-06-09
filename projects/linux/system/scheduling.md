# Task Scheduling

## Systemd

Systemd processes can be scheduled through the use of timers. To create a timer:

```bash
tjalder@htb[/htb]$ sudo mkdir /etc/systemd/system/mytimer.timer.d
$ sudo nano /etc/systemd/system/mytimer.timer
```

```code
[Unit]
Description=My Timer

[Timer]
OnBootSec=3min
OnUnitActiveSec=1hour

[Install]
WantedBy=timers.target
```

Here it depends on how we want to use our script. For example, if we want to run our script only once after the system boot, we should use OnBootSec setting in Timer. However, if we want our script to run regularly, then we should use the OnUnitActiveSec to have the system run the script at regular intervals. We can now create a service that points to a script to be run:

```bash
tjalder@htb[/htb]$ sudo nano /etc/systemd/system/mytimer.service
```

```
[Unit]
Description=My Service

[Service]
ExecStart=/full/path/to/my/script.sh

[Install]
WantedBy=multi-user.target
```

Note that `systemd` will automatically associate between `mytimer.service` and `mytimer.timer`. We can then reload the systemd daemon `sudo systemctl daemon-reload` and then use our new timer.

## Cron

Cron is another tool for scheduling jobs. Cron tasks are structured like such:

| Time Frame |
| --- |
| Minutes (0-59) |
| Hours (0-23) |
| Days of month (1-31) |
| Months (1-12) |
| Days of the week (0-7) |

For example:

```code
# System Update
0 */6 * * * /path/to/update_software.sh # Execute once every 6 hours

# Execute Scripts
0 0 1 * * /path/to/scripts/run_scripts.sh # Execute first day of the month at midnight

# Cleanup DB
0 0 * * 0 /path/to/scripts/clean_database.sh # Execute every Sunday at midnight

# Backups
0 0 * * 7 /path/to/scripts/backup.sh # Execute every Sunday at midnight
```
