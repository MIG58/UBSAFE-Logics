#!/bin/bash

# Perform the USBGuard setup
sudo usbguard generate-policy > /etc/usbguard/rules.conf
sudo systemctl restart usbguard.service

# Define the USBGuard rule file
RULES_FILE="/etc/usbguard/rules.conf"

# Remove existing rules
sudo rm -f "$RULES_FILE"

# List USB devices, filter out "Linux Foundation," and allow the rest
lsusb | grep -v "Linux Foundation" | while read -r line; do
    vendor_id=$(echo "$line" | awk '{print $6}' | cut -d ':' -f 1)
    product_id=$(echo "$line" | awk '{print $6}' | cut -d ':' -f 2)
    
    echo "Allowing device with Vendor ID: $vendor_id, Product ID: $product_id"
    
    cat <<EOL | sudo tee -a "$RULES_FILE"
allow device with vendor_id == "$vendor_id" product_id == "$product_id"
EOL
done

# Reload USBGuard rules
sudo systemctl restart usbguard.service

echo "Only non-Linux Foundation USB devices are allowed. Please reboot your system for the changes to take effect."
