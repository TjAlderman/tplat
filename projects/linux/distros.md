# Distributions

A Linux distribution is the Linux kernel bundled with userland tools, package management, and defaults.

## Overview

- Distros differ by package manager, default tools, desktop environment, and target use case
- Common use cases include desktop, server, embedded, and security tooling
- The same kernel can feel very different depending on the distribution

## Reference

### Common distributions

| Category | Examples |
| --- | --- |
| General purpose | Ubuntu, Fedora, Debian |
| Enterprise | Red Hat Enterprise Linux, CentOS |
| Security tooling | Kali Linux, Parrot OS, BlackArch, Pentoo, BackBox |
| Specialized | Raspberry Pi OS |

### Debian focus

- Known for stability, reliability, and conservative defaults
- Common in servers, desktops, and embedded systems
- Uses the APT ecosystem for installs, upgrades, and dependency resolution

| Property | Notes |
| --- | --- |
| Stability | Conservative package updates |
| Release cycle | Long-term support style releases |
| Security | Dedicated security updates |
| Flexibility | Highly configurable |
| Learning curve | Higher than beginner-focused distros |

### Trade-offs

- Pros: predictable behaviour, strong security track record, large package repository
- Cons: older package versions, more manual configuration, less beginner-friendly UX

## Mental Model

- A distro is an opinionated bundle around the same kernel
- The right choice depends on environment and workflow
- Most trade-offs come down to stability versus freshness and control versus convenience
