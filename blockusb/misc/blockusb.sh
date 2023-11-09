#!/bin/bash
# Initial Rules Mandatory

# Define the flag file to check if the operation has been performed
FLAG_FILE="/var/run/usbguard_setup_completed.flag"

perform_usbguard_setup() {
    if [ ! -e "$FLAG_FILE" ]; then
        # Perform the USBGuard setup
        sudo sh -c 'usbguard generate-policy > /etc/usbguard/rules.conf'
        sudo systemctl start usbguard.service
        sudo systemctl enable usbguard.service

        # Create the flag file to indicate that the operation has been completed
        sudo touch "$FLAG_FILE"

        echo "USBGuard setup completed."
    else
        echo "USBGuard setup has already been performed."
    fi
}

# Call the function to perform the setup
# perform_usbguard_setup


# Check if the script is running with superuser privileges
# if [ "$(id -u)" != "0" ]; then
#     echo "Please run this script with sudo."
#     exit 1
# fi

# Define the USBGuard rule file
RULES_FILE="/etc/usbguard/rules.conf"

# Remove the existing rule file
rm -f "$RULES_FILE"

# Allow USBGuard to allow your keyboard, mouse, and the specified Realtek device
# Replace "1234" and "5678" with the correct vendor and product IDs for your devices.
cat <<EOL >> "$RULES_FILE"
# Allow keyboard and mouse
allow device with vendor_id == "10c4" product_id == "8108"
allow device with vendor_id == "1c4f" product_id == "0002"

# Allow Realtek device
allow device with vendor_id == "0bda" product_id == "f179"
EOL

# Block all other USB devices
cat <<EOL >> "$RULES_FILE"
# Block all other USB devices
deny device
EOL

# Reload USBGuard rules
systemctl restart usbguard

echo "Unused USB ports are blocked, and keyboard, mouse, and the specified Realtek device are allowed. Please reboot your system for the changes to take effect."

# Bus 005 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
# Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
# Bus 004 Device 003: ID 10c4:8108 Silicon Labs USB OPTICAL MOUSE
# Bus 004 Device 002: ID 1c4f:0002 SiGma Micro Keyboard TRACER Gamma Ivory
# Bus 004 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
# Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
# Bus 002 Device 001: ID 1d6b:0001 Linux Foundation 1.1 root hub
# Bus 007 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
# Bus 006 Device 003: ID 0bda:f179 Realtek Semiconductor Corp. RTL8188FTV 802.11b/g/n 1T1R 2.4G WLAN Adapter
# Bus 006 Device 006: ID 0781:5567 SanDisk Corp. Cruzer Blade
# Bus 006 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub


# 1. Silicon Labs USB Optical Mouse:
#    - Vendor ID: 10c4
#    - Product ID: 8108

# 2. SiGma Micro Keyboard TRACER Gamma Ivory:
#    - Vendor ID: 1c4f
#    - Product ID: 0002

# 3. Realtek Semiconductor Corp. RTL8188FTV 802.11b/g/n 1T1R 2.4G WLAN Adapter:
#    - Vendor ID: 0bda
#    - Product ID: f179

# You can use these vendor and product IDs in your USBGuard rules to allow or deny specific devices as needed.