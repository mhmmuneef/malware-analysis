#!/bin/bash
# Install Volatility and its dependencies

# Update package lists and install dependencies
sudo apt-get update
sudo apt-get install -y python3-pip git

# Install required Python modules
pip3 install --user distorm3 yara-python pycryptodome

# Clone the Volatility 3 repository
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3

# Install Volatility 3
python3 setup.py install

echo "Volatility 3 installed successfully!"
