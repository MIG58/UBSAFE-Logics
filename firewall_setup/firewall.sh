#!/bin/bash

# Function to check if UFW is installed
ufw_installed() {
    dpkg -s ufw &> /dev/null
    return $?
}

# Function to install UFW
install_ufw() {
    echo "Installing UFW..."
    sudo apt-get update
    sudo apt-get install -y ufw
}

# Function to start UFW and enable basic rules
start_ufw() {
    echo "Starting UFW and enabling basic rules..."
    sudo ufw default deny incoming
    sudo ufw default allow outgoing
    sudo ufw enable
}

# Check if UFW is installed and install/start it if necessary
if ufw_installed; then
    echo "UFW is already installed."
    start_ufw
else
    install_ufw
    start_ufw
fi

echo "UFW setup complete."
