import os
import shutil

# Function to display license.txt and prompt user to accept or reject
def display_license():
    license_path = os.path.join(os.path.dirname(__file__), "license", "license.txt")
    with open(license_path, 'r') as file:
        license_content = file.read()
        print(license_content)

        while True:
            choice = input("Do you accept the license? (y/n): ").lower()
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

# Ask user for the folder path
folder_path = input("Enter the path to the folder containing files to be sorted: ")

# Check if the user accepts the license
if not display_license():
    print("License not accepted. Exiting.")
    exit()

# Function to find and automatically delete empty folders
def auto_delete_empty_folders(root_path):
    for foldername, subfolders, filenames in os.walk(root_path, topdown=False):
        if not subfolders and not filenames:
            try:
                os.rmdir(foldername)
                print(f"Folder '{foldername}' deleted successfully.")
            except OSError as e:
                print(f"Error deleting folder '{foldername}': {e}")

# Call the function to automatically delete empty folders
auto_delete_empty_folders(folder_path)
