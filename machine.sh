#!/bin/bash

# Prompt user for machine name
echo -e "Enter machine name:\n"
read machine_name

# Define the directory path
machines_directory="$HOME/offsec/machines/$machine_name"

# Check if the directory already exists
if [ -d "$machines_directory" ]; then
    echo "Directory already exists. Moving to $machine_name directory."
else
    # Create the directory if it doesn't exist
    mkdir "$machines_directory"
fi

# Change to the machine name directory
cd "$machines_directory" || exit 1

# Additional commands for the new directory can be added here

# Print the current working directory
echo "Current directory: $(pwd)"
