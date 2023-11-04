#!/bin/bash

install_timeshift() {
  # Check if Timeshift is already installed
  if command -v timeshift &>/dev/null; then
    echo "Timeshift is already installed."
  else
    # Install Timeshift
    sudo apt-get update
    sudo apt-get install timeshift -y
  fi
}

create_backup() {
  # Include all root files
  sudo timeshift --create
}

get_storage_path() {
  storage_path=$(sudo timeshift --list 2>/dev/null | grep 'Path' | awk -F': ' '{print $2}')
  if [ -n "$storage_path" ]; then
    echo "Storage Path: $storage_path"
  else
    echo "Storage Path not found."
  fi
}

install_timeshift
create_backup
get_storage_path
