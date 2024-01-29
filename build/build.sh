#!/bin/bash

# Install packages using pip
pip install -r ../requirements.txt

# Check if installation was successful
if command -v pyinstaller &> /dev/null
then
    echo "PyInstaller installed successfully."
else
    echo "Failed to install PyInstaller. Please check your setup and try again."
    exit 1
fi

# Create binary using pyinstaller
pyinstaller ./run_app.spec --clean