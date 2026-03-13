#!/bin/bash

echo "Running Ansible playbook..."

ansible-playbook -i hosts.ini nginx-install.yml

echo "Checking Nginx status..."

curl http://localhost
