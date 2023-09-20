#!/bin/sh

# Re-enable code
sudo systemctl unmask ssh
sudo systemctl enable ssh
sudo systemctl start ssh
# sudo systemctl status ssh
