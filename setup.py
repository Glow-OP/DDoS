import subprocess
import os

def setup_dependencies():
    user_input = input("Do you want to set up? (y/n): ")
    if user_input.lower() == 'y':
        packages = [
            "npm install gradient-string",
            "npm install fake-useragent",
            "npm install cluster",
            "npm install colors",
            "npm install net",
            "npm install tls",
            "npm install fs",
            "npm install crypto",
            "npm install user-agents"
        ]

        for package in packages:
            subprocess.run(package, shell=True)
        print("Packages installed successfully.")
        input("Press Enter to continue...")  # Wait for user to press Enter
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        os.system('python3 ddos.py')  # Run ddos.py
    else:
        print("No packages were installed.")

# Call the function to start the setup process
setup_dependencies()
