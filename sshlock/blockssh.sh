#!/bin/bash

#Stop the SSH Server
sudo systemctl stop ssh

# Disable the SSH Server at Boot
sudo systemctl disable ssh

# Mask the SSH Service
sudo systemctl mask ssh

# Reload Systemd
# sudo systemctl daemon-reload

# Check SSH Status:
# sudo systemctl status ssh

# Re-enable code
# sudo systemctl unmask ssh
# sudo systemctl enable ssh
# sudo systemctl start ssh
