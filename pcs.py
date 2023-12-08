#!/usr/bin/env python3
# Script:                       Create if statements using these logical conditionals
# Author:                       Yue Moua
# Date of latest revision:      12/7/2023
# Purpose:                      Python Conditionals

# Comparisons:
# Equal:                  ==
# Not Equal:              !=
# Greater Than:            >
# Less Than:               <
# Greater or Equal To:     >=
# Less or Equal To:        <=

# Prompt the user to input their age
age_str = input("Please enter your age: ")

# Convert the input string to an integer
try:
    age = int(age_str)
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

# Conditional statement
if age < 13:
    print("The person is a child")
elif 13 <= age < 20:
    print("The person is a teen")
else:
    print("The person is an adult")
    
    # REF
    # https://github.com/codefellows/seattle-ops-301d14/tree/main/class-07