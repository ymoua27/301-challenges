#!/usr/bin/env python3
# Script:                       Creat script using file handling commands
# Author:                       Yue Moua
# Date of latest revision:      12/8/2023
# Purpose:                      Python File Handling

# Create a new .txt file and append three lines
with open('test.txt', 'w') as file:
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')
    file.write('This is the third line.\n')

with open('test.txt', 'r') as file:
    all_lines = file.readlines()
    for line in all_lines:
        print(line.strip())

import os
os.remove('test.txt')