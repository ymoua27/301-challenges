#!/usr/bin/env python3

# Import libraries
import os

# Declaration of variables
user_path = input("Enter a directory path: ")

# Declaration of functions
def generate_directory_structure(directory_path):
    try:
        for (root, dirs, files) in os.walk(directory_path):
            # Print the current root directory
            print(f"Current Directory: {root}")
            
            # Print the subdirectories
            print(f"  Subdirectories: {dirs}")

            # Print the files
            print(f"  Files: {files}")

            # Separator for better readability
            print('-' * 50)

    except Exception as e:
        print(f"An error occurred: {e}")

# Main
generate_directory_structure(user_path)

# REF
# https://www.w3schools.com/python/ref_os_fwalk.asp
# https://chat.openai.com/share/7e8f12a8-1269-40f0-bb77-f53bf9d9cbbc
