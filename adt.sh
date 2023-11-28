#!/bin/bash

# Script Name:              adt.sh
# Author:                   Yue Moua
# Date of last revision:    11/28/2023
# Purpose:                  Create a script that copies /var/log/sys/log to current working dir and appends the current date and time to the filename

# Copies syslog and creates test.txt in pathway I want

cat /var/log/syslog > /home/ymoua/Ops/301-challenges/test.txt

# Running date command from terminal gives a general output
echo `date`
# or
echo $(date)

# Here we assign variables but you can run these commands on their own without the ` outside the command string. These are modifiers shown.
year=`date +%Y`
echo $year
month=`date +%m`
echo $month
day=`date +%d`
echo $day

# The date command displays the local system's date and time

hour=`date +%H`
echo $hour
minute=`date +%M`
echo $minute
second=`date +%S`
echo $second

# Put it all together
echo "Current Date: $day-$month-$year"
echo "Current Time: $hour:$minute:$second"


# How to row append

# First create a file test.txt and add some lines to it.
echo "Original file before append:"
cat test.txt

# The >> double carrot will row append
echo "My new string with date: `date`" >> test.txt
echo "Appended file:"
cat test.txt


# Resources
# https://chat.openai.com/share/f5daf446-9e7d-47f6-8ec5-c2f3c794dacc
# https://github.com/codefellows/seattle-ops-301d14/blob/main/class-02/challenges/DEMO.md 