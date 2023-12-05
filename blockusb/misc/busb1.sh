#!/bin/bash

# Check if the script is running with superuser privileges
# if [ "$(id -u)" != "0" ]; then
#     echo "Please run this script with sudo."
#     exit 1
# fi

# Define the USBGuard rule file
RULES_FILE="/etc/usbguard/rules.conf"

# Remove the existing rule file
rm -f "$RULES_FILE"

# Allow USBGuard to allow keyboard, mouse, and the specified Realtek device
# Replace "03:01:01" and "03:01:02" with the correct USB interfaces for your keyboard and mouse.
# Replace "06:03:04" with the correct USB interface for the Realtek device.
cat <<EOL >> "$RULES_FILE"
# Allow keyboard and mouse
allow device with interface == "03:01:01"
allow device with interface == "03:01:02"

# Allow Realtek device
allow device with interface == "06:03:04"
EOL

# Block all other USB devices
cat <<EOL >> "$RULES_FILE"
# Block all other USB devices
deny device
EOL

# Reload USBGuard rules
systemctl restart usbguard

echo "Unused USB ports are blocked, and keyboard, mouse, and the specified Realtek device are allowed. Please reboot your system for the changes to take effect."