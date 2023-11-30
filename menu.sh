# Script Name:              menu.sh
# Author:                   Yue Moua
# Date of last revision:    11/30/2023
# Purpose:                  Create a conditionals in menu systems script

while true; do 
    clear

    echo "May your choices reflect your hopes, not your fears"
    echo "1. Hello World"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    read -p "Enter your choice (1-4): " choice

    if [[ $choice == 1 ]]; then
        echo "Hello World"
        read -p "Press Enter to continue"
    elif [[ $choice == 2 ]]; then
        ping -c 4 127.0.0.1
        read -p "Press Enter to continue"
    elif [[ $choice == 3 ]]; then
        ip a
        read -p "Press Enter to continue"
    elif [[ $choice == 4 ]]; then
        exit 0
    else
        echo "Invalid choice. Please enter a number between 1 and 4."
        read -p "Press Enter to continue"
    fi
done