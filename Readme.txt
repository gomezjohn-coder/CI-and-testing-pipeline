# CI-and-testing-pipeline
# Calculator Application - Build and Run Instructions

## Overview:
This is a simple Python-based calculator application with basic arithmetic operations like addition, subtraction, multiplication, and division. The application includes unit tests to verify functionality.

This README will guide you through the steps to build and run the application, as well as how to package it into a standalone executable.

## Prerequisites:
Before you can run the build script, ensure you have the following installed:

- **Python 3.x**: Make sure Python is installed on your system. You can download it from the official Python website: https://www.python.org/downloads/
  - To verify if Python is installed, open a terminal or command prompt and run:
    ```bash
    python --version
    ```

- **Git Bash**: Git Bash is a terminal that allows you to run bash commands on Windows. It comes with Git for Windows, which you can download here: https://git-scm.com/

- **pip**: `pip` is the package installer for Python, and it should be installed with Python by default. You can verify if **pip** is installed by running:
    ```bash
    pip --version
    ```

  If `pip` is not installed, you can install it by following the instructions here: https://pip.pypa.io/en/stable/installation/

- **PyInstaller**: PyInstaller is used to package Python applications into standalone executables. It is required to create the executable from your Python script. To install **PyInstaller**, run:
    ```bash
    pip install pyinstaller
    ```

To automatically Build and run the application: 

1. **Clone the Repository**:
   Download the repository using Git. Open **Git Bash** or your terminal and run the following command:
   ```bash
   git clone https://github.com/gomezjohn-coder/CI-and-testing-pipeline
2. After downloading it , go to the CI-and-testing-pipeline folder and right click it click the open Git Bash here 
and execute the command " ./build.sh" 
3. After executing the command, it will automatically downloads all the deployable package and automatically executes the unit test in the command prompt;
4. The command prompt will show how many success and fails the unit test will have.
