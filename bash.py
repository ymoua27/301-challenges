# Author:    Yue Moua
# Script:    Create script that execute BASH commands     
# Purpose:   Intro to Python

# Variables

A1= 'whoami'
A2 = 'ipa'
A3 = 'lshwshort'

import subprocess

def A1():
    subprocess.run(["whoami"])

def A2():
    subprocess.run(["ip", "a"])

def A3():
    subprocess.run(["lshw", "-short"])

while True:
    # Display menu options
    print("\nMenu:")
    print("1. Run whoami")
    print("2. Run ip a")
    print("3. Run lshw -short")
    print("4. Exit")

    # Get user input
    choice = input("Enter your choice (1-4): ")

    # Process user choice
    if choice == "1":
        A1()
    elif choice == "2":
        A2()
    elif choice == "3":
        A3()
    elif choice == "4":
        print("Exit")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        
        
        
# REF
# https://chat.openai.com/share/baf5941f-c1ea-487b-9afd-5cca53c7e18e