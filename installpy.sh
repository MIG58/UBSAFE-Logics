#!/bin/bash

# Check if the script is running with root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run this script as root."
  exit 1
fi

# Update the package list and install Python 3
apt update
apt install -y python3

# Verify the installation
python3 --version

echo "Python 3 has been successfully installed."

# Optional: You can also install pip for Python 3
apt install -y python3-pip
pip3 --version

echo "pip for Python 3 has been installed."

# Optional: You can install virtualenv for Python 3
apt install -y python3-venv

# Set alias that python3 is python
sudo apt install python-is-python3


echo "Python 3 virtual environment support has been installed."

# Optional: You can install additional packages as needed
# apt install -y python3-dev python3-setuptools python3-wheel

# Optional: You can create a virtual environment
# python3 -m venv myenv
# source myenv/bin/activate
###################################################### ALIAS PYTHON3 as Python ################################################################
# Define the alias command
alias_command="alias python='python3'"

# Check if the shell configuration file exists
if [ -f ~/.bashrc ]; then
  shell_config=~/.bashrc
elif [ -f ~/.zshrc ]; then
  shell_config=~/.zshrc
else
  echo "Unable to determine the shell configuration file."
  exit 1
fi

# Check if the alias already exists in the configuration file
if grep -q "$alias_command" "$shell_config"; then
  echo "The 'python' alias already exists in $shell_config."
  exit 0
fi

# Add the alias to the shell configuration file
echo "$alias_command" >> "$shell_config"
echo "Alias added to $shell_config."

# Apply the changes immediately
source "$shell_config"

echo "Now, 'python' points to 'python3'."
####################################### TWILIO Install ######################################################

sudo apt install python3-twilio

if ! command -v pip &>/dev/null; then
    echo "Error: 'pip' is not installed. Please install 'pip' first."
    exit 1
fi

# Install the Twilio Python library
pip install twilio

# Install Tkinter 
sudo apt install -y python3-tk

# pip install Image
# Install ImageTK
sudo apt install python3-pil.imagetk

# PyQt5 Install
sudo apt install python3-pyqt5

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "Twilio Python library has been successfully installed."
else
    echo "Error: Twilio Python library installation failed."
fi


####################################### SSH Install ######################################################
sudo apt install -y ssh

####################################### USB GUARD check ######################################################

RULES_FILE="/etc/usbguard/rules.conf"
sudo rm -f "$RULES_FILE"

sudo apt-get remove usbguard -y 
sudo apt-get install usbguard -y

sudo sh -c 'usbguard generate-policy > /etc/usbguard/rules.conf'
sudo systemctl start usbguard.service
sudo systemctl enable usbguard.service

exit 0
