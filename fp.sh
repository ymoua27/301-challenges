#!/bin/bash

# Script Name:              fp.sh
# Author:                   Yue Moua
# Date of last revision:    11/29/2023
# Purpose:                  Prompts user for input directory path.
#                           Prompts user for input permissions number                
#                           Navigates to the directory input by the user and changes all files inside it to the input setting.
#                           Prints to the screen the directory contents and the new permissions settings of everything in the directory.

#!/bin/bash

# Prompt user for input directory path
read -p "Enter the directory path: " directory_path

# Check if the directory exists
if [ ! -d "$directory_path" ]; then
    echo "Error: The specified directory does not exist."
    exit 1
fi

# Prompt user for input permissions number
read -p "Enter the permissions number Hint: Lucky: " permissions

# Change permissions of files in the directory
chmod -R "$permissions" "$directory_path"

# Print directory contents and new permissions settings
echo -e "\nDirectory contents after changes:"
ls -la "$directory_path"

echo -e "\nNew permissions settings:"
ls -la "$directory_path" | awk '{print $1, $9}'


# Resources
# https://chat.openai.com/share/baf5941f-c1ea-487b-9afd-5cca53c7e18e