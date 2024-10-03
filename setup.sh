#!/bin/bash

# Update package list and install Python 3 and pip
sudo apt-get update
sudo apt-get install -y python3 python3-pip git

# Install virtualenv
pip3 install virtualenv

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Run the main Python script
python3 main.py
