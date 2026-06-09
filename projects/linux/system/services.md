# Service and Process Management

Daemons and processes that run in the background. Daemons are often identified by the letter d at the end of their program names, such as `sshd` (SSH daemon) or `systemd`.

In general, there are just a few goals that we have when we deal with a service or a process:

1. Start/Restart a service/process
1. Stop a service/process
1. See what is/was happening with a service/process
1. Enable/Disable a service/process on boot
1. Find a service/process

Most modern Linux distributions have adopted `systemd` as their initialisation system (init system). It is the first process that starts during the boot process and is assigned the Process ID (PID). All processes in a Linux system are assigned a PID and can be viewed under the `/proc/` directory, which contains information about each process. Processes may also have a Parent Process ID (PPID), indicating that they were started by another process (the parent), making them child processes.

## systemctl

We can start a service using `systemctl start <service>`. We can set a service to start on boot using `systemctl enable <service>` (internally, this adds the service to the `SysV` script). Similarly, we can `stop`, `restart`, and retrieve the `status` of services.

We can list all services like:

```bash
tjalder@htb[/htb]$ systemctl list-units --type=service

UNIT                                                       LOAD   ACTIVE SUB     DESCRIPTION              
accounts-daemon.service                                    loaded active running Accounts Service         
acpid.service                                              loaded active running ACPI event daemon        
apache2.service                                            loaded active running The Apache HTTP Server   
apparmor.service                                           loaded active exited  AppArmor initialization  
apport.service                                             loaded active exited  LSB: automatic crash repor
avahi-daemon.service                                       loaded active running Avahi mDNS/DNS-SD Stack  
bolt.service                                               loaded active running Thunderbolt system service
```

## Kill a Process

A process can be in the following states:

* Running
* Waiting (waiting for an event or system resource)
* Stopped
* Zombie (stopped but still has an entry in the process table).

Processes can be controlled using `kill`, `pkill`, `pgrep`, and `killall`. To interact with a process, we must send a signal to it. We can view all signals with the following command:

```bash
tjalder@htb[/htb]$ kill -l

 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
 6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
63) SIGRTMAX-1  64) SIGRTMAX
```

## Background a Process

We can suspend a process using `[Ctrl + z]`. We can then list suspended processes with `jobs`. We can then background the process using `bg`. Another option is to finish the command with an `&` sign to automatically background the process.

## Foreground a Process

We can bring a background process listed under `jobs` back into the foreground using `fg <id>`.

## Executing Multiple Commands

There are three possibilities to run several commands, one after the other. These are separated by:

* Semicolon (;)
* Double ampersand characters (&&)
* Pipes (|)
