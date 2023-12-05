#!/bin/bash
# Initial Rules Mandatory

# Define the flag file to check if the operation has been performed
# FLAG_FILE="/var/run/usbguard_setup_completed.flag"

# Perform the USBGuard setup
sudo sh -c 'usbguard generate-policy > /etc/usbguard/rules.conf'
sudo systemctl start usbguard.service
sudo systemctl enable usbguard.service
sudo systemctl status usbguard.service


# Create the flag file to indicate that the operation has been completed
# sudo touch "$FLAG_FILE"

# echo "USBGuard setup completed."
    


# Call the function to perform the setup
# perform_usbguard_setup

# Define the USBGuard rule file
RULES_FILE="/etc/usbguard/rules.conf"

# Remove the existing rule file
rm -f "$RULES_FILE"

# List USB devices, filter out "Linux Foundation," and allow the rest
lsusb | grep -v "Linux Foundation" | while read -r line; do
    vendor_id=$(echo "$line" | awk '{print $6}' | cut -d ':' -f 1)
    product_id=$(echo "$line" | awk '{print $6}' | cut -d ':' -f 2)
    
    echo "Allowing device with Vendor ID: $vendor_id, Product ID: $product_id"
    
    cat <<EOL >> "$RULES_FILE"
allow device with vendor_id == "$vendor_id" product_id == "$product_id"
EOL
done

# Reload USBGuard rules
systemctl restart usbguard

echo "Only non-Linux Foundation USB devices are allowed. Please reboot your system for the changes to take effect."
