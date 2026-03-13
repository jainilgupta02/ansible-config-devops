# Ansible Nginx Automation

Automate Nginx installation and basic server setup with Ansible.

## Overview

This repository provides a simple Infrastructure as Code workflow to:

- Configure inventory and target hosts
- Install and manage Nginx using Ansible
- Run automation through a Bash wrapper script

## Project Structure

```text
.
|-- run-nginx.sh
|-- inventory
|-- playbook.yml
`-- readme.md
```

## Prerequisites

- Ansible installed on control machine
- SSH access to target machine(s)
- Proper SSH key permissions

## Quick Start

1. Update your inventory with target host details.
2. Ensure SSH key and host access are configured.
3. Run the automation script:

```bash
chmod +x run-nginx.sh
./run-nginx.sh
```

## What This Automates

- Nginx package installation
- Service enable/start steps
- Repeatable configuration workflow

## Security Rule (Important)

Never upload sensitive key files, especially:

- ansible.pem

Always ignore private keys in .gitignore.

Example:

```gitignore
*.pem
```

## DevOps Workflow

Typical engineering flow:

```text
Laptop or EC2
	-> Git
	-> GitHub Repository
	-> CI/CD Pipeline
```

## Notes

- Keep playbooks idempotent.
- Validate inventory before execution.
- Store secrets outside the repository.