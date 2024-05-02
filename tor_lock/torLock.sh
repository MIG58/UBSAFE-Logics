#!/bin/bash

# Function to check if a package is installed
package_installed() {
    dpkg -s $1 &> /dev/null
    return $?
}

# Function to uninstall a package
uninstall_package() {
    echo "Removing $1..."
    sudo apt-get remove --purge -y $1
}

# Function to secure Tor configuration
secure_tor_config() {
    echo "Securing Tor configuration..."
    sudo chmod 600 /etc/tor/torrc
    sudo chown -R debian-tor:debian-tor /var/lib/tor
    sudo chmod -R 700 /var/lib/tor
}

# Function to setup firewall rules for Tor
setup_firewall_rules() {
    echo "Setting up firewall rules for Tor..."
    sudo ufw allow out 9050
    sudo ufw allow out 53     # Allow DNS requests
}

# Check if Tor is installed and remove it
if package_installed tor; then
    uninstall_package tor
    echo "Tor has been uninstalled."
    secure_tor_config
    setup_firewall_rules
else
    echo "Tor is not installed."
fi

# Check if Proxychains is installed and remove it
if package_installed proxychains; then
    uninstall_package proxychains
    echo "Proxychains has been uninstalled."
else
    echo "Proxychains is not installed."
fi

echo "Script execution complete."
