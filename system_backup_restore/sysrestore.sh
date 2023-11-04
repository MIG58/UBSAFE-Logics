#!/bin/bash

restore_snapshot() {
#   # Check if Timeshift is installed
#   if ! command -v timeshift &>/dev/null; then
#     echo "Timeshift is not installed. Please install it first."
#     exit 1
#   fi

  # List available snapshots
  sudo timeshift --list

  # Prompt the user to select a snapshot to restore
  read -p "Enter the name of the snapshot to restore: " snapshot_name

  # Check if the specified snapshot exists
  if ! sudo timeshift --list | grep -q "$snapshot_name"; then
    echo "Snapshot '$snapshot_name' does not exist."
    exit 1
  fi

  # Initiate the restore process
  sudo timeshift --restore --snapshot "$snapshot_name"
}

restore_snapshot
