"""
Directory Folder Counter by Initial Letter (Windows)
This script counts all folders in a specified Windows directory that begin with each letter
of the alphabet. Results are displayed in order from most frequent to least frequent initial
letter, and includes a summary of which letters are represented in the directory structure.

Usage: Run the script and paste a Windows path when prompted (e.g. R:\\books\\Novels).
"""
import os
import string
from collections import defaultdict


def count_folders_by_starting_letter(directory_path):
    # Dictionary to store counts with default value of 0
    letter_counts = defaultdict(int)

    # Initialize with all letters of the alphabet
    for letter in string.ascii_uppercase:
        letter_counts[letter] = 0

    try:
        # List all items in the directory
        for item in os.listdir(directory_path):
            full_path = os.path.join(directory_path, item)

            # Check if it's a directory and not a file
            if os.path.isdir(full_path):
                # Get the first letter and convert to uppercase
                if item and item[0].isalpha():
                    first_letter = item[0].upper()
                    letter_counts[first_letter] += 1

        return letter_counts
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return None


def main():
    # Ask user for directory path
    print("Please enter the directory path (you can copy from Windows Explorer):")
    directory_path = input().strip()

    # Remove quotes if the user copied a path with quotes
    if directory_path.startswith('"') and directory_path.endswith('"'):
        directory_path = directory_path[1:-1]

    # Count folders
    counts = count_folders_by_starting_letter(directory_path)

    if counts:
        # Sort the letters by count (highest to lowest)
        sorted_letters = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # Count how many letters have folders
        letters_with_folders = sum(1 for letter, count in counts.items() if count > 0)

        print("\nFolder counts by starting letter (highest to lowest):")
        print("-" * 40)

        # Print results in order of count
        for letter, count in sorted_letters:
            if count > 0:
                print(f"{letter}: {count}")

        # Print totals and summary
        total = sum(counts.values())
        print("-" * 40)
        print(f"Total folders: {total}")
        print(f"Letters with at least one folder: {letters_with_folders} out of 26")
        print(f"Letters with no folders: {26 - letters_with_folders}")


if __name__ == "__main__":
    main()