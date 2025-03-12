#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 to continue."
    exit 1
fi

# Create a virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating a Python virtual environment in .venv..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment. Exiting."
        exit 1
    fi
else
    echo "Virtual environment already exists in .venv."
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source .venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Failed to activate the virtual environment. Exiting."
    exit 1
fi

# Verify the virtual environment is active
PYTHON_PATH=$(which python3)
if [[ "$PYTHON_PATH" == *".venv/bin/python3"* ]]; then
    echo "Virtual environment is active: $PYTHON_PATH"
else
    echo "Virtual environment is not active. Exiting."
    exit 1
fi

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip
if [ $? -ne 0 ]; then
    echo "Failed to upgrade pip. Exiting."
    exit 1
fi

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Failed to install dependencies. Exiting."
        exit 1
    fi
else
    echo "requirements.txt not found. Please create one with the necessary dependencies."
    exit 1
fi


echo "Setup complete. Remember to activate the virtual environment before installing any new packages with:"
echo "source .venv/bin/activate"

