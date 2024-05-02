#!/bin/sh

# Re-enable code
sudo systemctl unmask ssh
sudo systemctl enable ssh
sudo systemctl start ssh
sudo ufw allow ssh     # Allow SSH connections

# sudo systemctl status ssh
