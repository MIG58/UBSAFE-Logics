#!/bin/bash

# Get the output of 'usbguard list-devices'
usbguard_output=$(usbguard list-devices)

# Search for the 'block' string in the output
block_string="block id"

# Extract device numbers and unblock each device
echo "$usbguard_output" | grep "$block_string" | awk '{print $2}' | while read -r device_number; do
    # Execute the command to unblock the device
    sudo usbguard allow-device "$device_number"
    echo "Unblocked USB device with number $device_number"
done
