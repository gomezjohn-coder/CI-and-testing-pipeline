import subprocess
import sys
import os
from setuptools import setup, find_packages

# Function to run unit tests
def run_tests():
    print("Running unit tests...")
    result = subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-p', '*_test.py'])
    if result.returncode != 0:
        print("Unit tests failed.")
        sys.exit(result.returncode)
    else:
        print("All unit tests passed.")

# Function to create a package
def create_package():
    print("Creating a deployable package...")
    setup(
        name='my_application',
        version='1.0',
        packages=find_packages(),
        install_requires=[],  # Add your dependencies here
        entry_points={
            'console_scripts': [
                'my_application = my_application.main:main_function',  # Adjust based on your app entry point
            ],
        },
    )
    subprocess.run([sys.executable, 'setup.py', 'sdist', 'bdist_wheel'])

    # After building the package, run the test feature file directly
    test_file = 'test_feature.py'  # Make sure this file exists in your repo
    if os.path.exists(test_file):
        print(f"Running {test_file}...")
        result = subprocess.run([sys.executable, test_file])
        if result.returncode == 0:
            print(f"{test_file} executed successfully.")
        else:
            print(f"Error executing {test_file}. Please check the error messages above.")
    else:
        print(f"Error: {test_file} not found.")

if __name__ == '__main__':
    # Run tests
    run_tests()

    # Create the deployable package
    create_package()
