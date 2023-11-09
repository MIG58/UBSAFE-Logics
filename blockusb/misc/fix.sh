#!/bin/bash


# USBGuard rule file
RULES_FILE="/etc/usbguard/rules.conf"
sudo rm -f "$RULES_FILE"

sudo apt-get remove usbguard -y 
sudo apt-get install usbguard -y

sudo sh -c 'usbguard generate-policy > /etc/usbguard/rules.conf'
sudo systemctl start usbguard.service
sudo systemctl enable usbguard.service
# sudo reboot