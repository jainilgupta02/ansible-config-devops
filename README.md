# Ansible Configuration & DevOps Automation

This repository contains hands-on practice projects and automation experiments using **Ansible**, focusing on infrastructure automation, server configuration, and DevOps workflows.

The goal of this repository is to demonstrate practical experience with **Configuration Management, Infrastructure Automation, and Cloud Operations**.

---

# Overview

The repository includes multiple Ansible practice modules covering:

* Server configuration automation
* Nginx installation and setup
* Inventory management
* Bash script execution using Ansible
* Infrastructure provisioning experiments
* DevOps automation practices

All examples are tested using **Ubuntu servers, AWS EC2 instances, and local WSL environments**.

---

# Technologies Used

* Ansible
* Linux (Ubuntu)
* AWS EC2
* Bash scripting
* Python
* SSH
* Git & GitHub

---

# Repository Structure

```
ansible-config-devops/
│
├── ansible-nginx/
│   ├── install-nginx.yml
│   └── related playbooks for Nginx automation
│
├── ansible-scripts/
│   ├── bash automation scripts
│   └── examples of running shell scripts using Ansible
│
├── ansible-ec2/
│   ├── create-ec2.yml
│   └── inventory files for cloud automation
│
├── ansiblework/
│   └── general Ansible practice and experiments
│
├── inventory.yml
├── server_inventory_validator.py
├── .gitignore
└── README.md
```

---

# Practice Modules

## 1. Nginx Installation Automation

Automates installation and setup of Nginx on remote Linux servers.

Features:

* Package installation using Ansible
* Service management
* Remote host configuration
* Verification of deployment

Example command:

```
ansible-playbook -i inventory.yml ansible-nginx/install-nginx.yml
```

---

## 2. Running Bash Scripts via Ansible

Demonstrates how Ansible can execute shell scripts remotely.

Examples include:

* Directory creation
* Server setup scripts
* System preparation scripts

Example:

```
ansible-playbook run-script.yml
```

---

## 3. AWS EC2 Automation

This module experiments with **Infrastructure as Code** concepts using Ansible to interact with AWS.

Features:

* Fetch default VPC
* AWS automation using boto3
* EC2 infrastructure experimentation

Requirements:

* AWS credentials configured
* Python boto3 library installed

---

## 4. Inventory Management

Demonstrates how to manage servers using **Ansible inventory files**.

Example inventory:

```
[webservers]
192.168.1.10
192.168.1.11

[dbservers]
192.168.1.20
```

---

## 5. Inventory Validation Tool

A simple Python utility included in the repository to validate server inventory files.

File:

```
server_inventory_validator.py
```

Purpose:

* Validate server entries
* Improve inventory structure
* Prevent configuration mistakes

---

# Requirements

Install Ansible:

```
sudo apt update
sudo apt install ansible
```

Install Python dependencies:

```
pip install boto3 botocore
```

---

# Running Playbooks

Example command:

```
ansible-playbook -i inventory.yml playbook.yml
```

Or with a specific inventory file:

```
ansible-playbook -i hosts.ini configure-server.yml
```

---

# Learning Goals

This repository focuses on building practical DevOps skills such as:

* Infrastructure as Code
* Configuration Management
* Linux server automation
* Cloud automation with AWS
* DevOps scripting
* Remote server orchestration

---

# Security Note

Sensitive files such as:

* private SSH keys
* virtual environments
* environment configuration files

are excluded using `.gitignore`.

---

# Future Improvements

Planned enhancements for this repository:

* Ansible Roles structure
* CI/CD pipeline integration
* Docker container automation
* Terraform + Ansible integration
* Automated infrastructure deployment

---

# Author

Jay Gupta
DevOps & Cloud Enthusiast

GitHub:
https://github.com/jainilgupta02

---

# License

This project is licensed under the MIT License.
