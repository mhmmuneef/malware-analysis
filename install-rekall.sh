#!/bin/bash
# Install Rekall and dependencies

# Update package lists
sudo apt-get update

# Install pip and Rekall
sudo apt-get install -y python3-pip
pip3 install rekall-agent rekall

echo "Rekall installed successfully!"
