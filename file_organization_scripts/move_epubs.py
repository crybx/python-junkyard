"""
Directory EPUB Mover

This script traverses through all folders in a specified starting directory,
finds all EPUB files, and moves them to a specified destination directory.
It accepts Windows-style folder paths that can be directly copied from Windows Explorer.
"""

import os
import shutil
import sys


def main():
    # Ask user for the starting directory
    start_dir = input("Enter the starting directory (paste from Windows Explorer): ")

    # Ask user for the destination directory
    dest_dir = input("Enter the destination directory (paste from Windows Explorer): ")

    # Check if directories exist
    if not os.path.isdir(start_dir):
        print(f"Error: Starting directory '{start_dir}' does not exist.")
        sys.exit(1)

    if not os.path.isdir(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist. Create it? (y/n): ", end="")
        create_dir = input().lower()
        if create_dir == "y":
            try:
                os.makedirs(dest_dir)
                print(f"Created destination directory: {dest_dir}")
            except Exception as e:
                print(f"Error creating directory: {e}")
                sys.exit(1)
        else:
            print("Operation cancelled.")
            sys.exit(1)

    # Initialize counter
    epub_moved = 0

    # Walk through all directories and subdirectories
    print(f"Searching for EPUB files in {start_dir}...")

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.lower().endswith(".zip"):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)

                # Check if file already exists in destination
                if os.path.exists(dest_file):
                    print(f"Warning: '{file}' already exists in destination. Skipping.")
                    continue

                try:
                    shutil.move(source_file, dest_file)
                    epub_moved += 1
                    print(f"Moved: {file}")
                except Exception as e:
                    print(f"Error moving '{file}': {e}")

    print(f"\nOperation complete. {epub_moved} EPUB files moved to {dest_dir}")


if __name__ == "__main__":
    main()
