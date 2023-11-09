#!/bin/bash

# USBGuard rule file
RULES_FILE="/etc/usbguard/rules.conf"

# Check if the USBGuard service is running
if systemctl is-active --quiet usbguard.service; then
    # List USB devices allowed by USBGuard rules
    allowed_devices=$(usbguard list-devices | grep "is-allowed: true" | awk '{print $2}')

    # List USB devices currently connected
    connected_devices=$(usbguard list-devices | grep "is-connected: true" | awk '{print $2}')

    # Reject all USB devices that are not in the allowed or connected list
    usbguard list-devices | while read -r line; do
        device_id=$(echo "$line" | awk '{print $2}')
        if [[ ! "$allowed_devices" =~ "$device_id" && ! "$connected_devices" =~ "$device_id" ]]; then
            echo "Rejecting device with ID: $device_id"
            usbguard reject-device "$device_id"
        fi
    done

    echo "Rejected all unauthorized USB devices."
else
    echo "USBGuard service is not running. Please ensure that USBGuard is properly configured and running."
fi