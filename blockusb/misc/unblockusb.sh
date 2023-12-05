#!/bin/bash

# Check if the script is running with superuser privileges
if [ "$(id -u)" != "0" ]; then
    echo "Please run this script with sudo."
    exit 1
fi
sudo systemctl stop usbguard.service

# Define the USBGuard rule file
RULES_FILE="/etc/usbguard/rules.conf"

# Remove the existing rule file
sudo rm -f "$RULES_FILE"

# Allow all USB devices
cat <<EOL >> "$RULES_FILE"
# Allow all USB devices
allow device
EOL

# Reload USBGuard rules
sudo systemctl start usbguard.service

echo "All USB devices are now allowed. Please reboot your system for the changes to take effect."
