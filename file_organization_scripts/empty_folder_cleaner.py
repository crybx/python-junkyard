"""
Empty Folder Cleaner

This script traverses a specified directory and removes all empty folders.
It accepts Windows file paths directly pasted from Explorer and provides
a file dialog alternative if no path is entered.
"""

import os
import tkinter as tk
from tkinter import filedialog


def select_directory_dialog():
    """Open a file dialog to select a directory."""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    directory = filedialog.askdirectory()
    root.destroy()
    return directory


def is_empty(path):
    """Check if a directory is empty."""
    # List all items in the directory
    items = os.listdir(path)
    return len(items) == 0


def clean_empty_folders(directory):
    """Remove all empty folders in the given directory and its subdirectories."""
    # Track statistics
    removed_count = 0

    # Walk the directory tree from bottom to top
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if is_empty(dir_path):
                print(f"Removing empty folder: {dir_path}")
                os.rmdir(dir_path)
                removed_count += 1

    return removed_count


def main():
    print("=== Empty Folder Cleaner ===")
    print("Enter the directory path to scan (paste from Windows Explorer),")
    print("or press Enter for a directory selection dialog:")

    # Get directory from user input or dialog
    user_input = input("> ")

    if user_input.strip():
        directory = user_input.strip()
        # Remove quotes if present (sometimes added when copying from Explorer)
        directory = directory.strip('"')
    else:
        print("Opening directory selection dialog...")
        directory = select_directory_dialog()

    if not directory:
        print("No directory selected. Exiting.")
        return

    # Confirm the selected directory
    print(f"\nSelected directory: {directory}")
    confirm = input("Proceed with cleaning empty folders? (y/n): ")

    if confirm.lower() != 'y':
        print("Operation cancelled. Exiting.")
        return

    # Run the cleaning process
    print("\nScanning for empty folders...")
    removed = clean_empty_folders(directory)

    # Report results
    if removed > 0:
        print(f"\nOperation complete. Removed {removed} empty folder(s).")
    else:
        print("\nNo empty folders found.")


if __name__ == "__main__":
    main()