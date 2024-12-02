#!/bin/bash

# Check if Python and pip are installed
if ! command -v python &>/dev/null; then
    echo "Python is not installed. Please install Python first."
    exit 1
fi

if ! command -v pip &>/dev/null; then
    echo "pip is not installed. Please install pip first."
    exit 1
fi

# Install dependencies (if you have a requirements.txt)
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies from requirements.txt..."
    pip install -r requirements.txt
fi

# Install PyInstaller if it's not installed
if ! command -v pyinstaller &>/dev/null; then
    echo "PyInstaller not found, installing it..."
    pip install pyinstaller
fi

# Create the standalone executable using PyInstaller
echo "Building the application..."
pyinstaller --onefile test_feature.py

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Build successful! The executable is located in the dist/ directory."
    
    # Automatically run the test_feature.py file after build is successful
    TEST_FILE="test_feature.py"

    if [ -f "$TEST_FILE" ]; then
        echo "Running $TEST_FILE in the terminal..."
        
        # Run the test file using Python
        python "$TEST_FILE"
        
        if [ $? -eq 0 ]; then
            echo "$TEST_FILE executed successfully."
        else
            echo "Error executing $TEST_FILE. Please check the error messages above."
        fi
    else
        echo "Test file $TEST_FILE not found."
    fi
else
    echo "Build failed. Please check the errors above."
    exit 1
fi
