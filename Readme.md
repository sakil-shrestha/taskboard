# Checkpoint 01 – CrewHub Server Setup

## Overview

This project demonstrates Linux user and group management, file permissions, and deployment of a Python application using `systemd`.

## Team

* **developers:** alice, bob
* **operations:** carol
* **Service Account:** crewhub (no login)

## Directory Structure

```text
/srv/crewhub/
├── code/
├── releases/
├── shared/
├── secrets/
├── app/
└── logs/
```

## Features

* Created users and groups
* Configured directory ownership and permissions
* Protected secrets using Linux permissions
* Deployed CrewHub as a `systemd` service
* Service starts on boot and restarts automatically on failure
* Environment variables loaded from `crewhub.env`
* Verified service using `curl` and `journalctl`

## Useful Commands

Start the service:

```bash
sudo systemctl start crewhub
```

Check status:

```bash
sudo systemctl status crewhub
```

View logs:

```bash
journalctl -u crewhub
```

Test the application:

```bash
curl http://localhost:8090
```

## Repository Files

* `crewhub.py`
* `crewhub.service`
* `crewhub.env.example`
* `proof.txt`
* `README.md`

