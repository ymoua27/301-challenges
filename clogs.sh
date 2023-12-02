#!/bin/bash

# Script Name:              adt.sh
# Author:                   Yue Moua
# Date of last revision:    11/28/2023
# Purpose:                  Create a script that prints log files, compresses it, clear the contents, prints the compressed file, and then compare the files


# Function to print file size
print_file_size() {
  echo "File size of $1: $(du -h $1 | cut -f1)"
}

# Backup directory
backup_dir="/var/log/backups"

# Check if the backup directory exists, create if not
if [ ! -d "$backup_dir" ]; then
  echo "Creating backup directory with elevated privileges..."
  sudo mkdir -p "$backup_dir"
  sudo chown $USER:$USER "$backup_dir"
fi

# Print original file sizes
print_file_size "/var/log/syslog"
print_file_size "/var/log/wtmp"

# Timestamp for the compressed file
timestamp=$(date "+%Y%m%d%H%M%S")

# Compress log files
gzip -c /var/log/syslog > "$backup_dir/syslog-$timestamp.zip"
gzip -c /var/log/wtmp > "$backup_dir/wtmp-$timestamp.zip"

# Clear the contents of the log files
echo "" > /var/log/syslog
echo "" > /var/log/wtmp

# Print compressed file sizes
print_file_size "$backup_dir/syslog-$timestamp.zip"
print_file_size "$backup_dir/wtmp-$timestamp.zip"

# Compare file sizes
original_size_syslog=$(du -b /var/log/syslog | cut -f1)
original_size_wtmp=$(du -b /var/log/wtmp | cut -f1)
compressed_size_syslog=$(du -b "$backup_dir/syslog-$timestamp.zip" | cut -f1)
compressed_size_wtmp=$(du -b "$backup_dir/wtmp-$timestamp.zip" | cut -f1)

echo "Comparison:"
echo "Original syslog size: $original_size_syslog bytes"
echo "Compressed syslog size: $compressed_size_syslog bytes"

echo "Original wtmp size: $original_size_wtmp bytes"
echo "Compressed wtmp size: $compressed_size_wtmp bytes"

# Ref
# https://chat.openai.com/share/baf5941f-c1ea-487b-9afd-5cca53c7e18e