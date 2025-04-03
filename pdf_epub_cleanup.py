"""
PDF-EPUB Cleanup Tool

This script traverses through all folders in a specified directory and moves
PDF files to the Recycle Bin if they have the same filename (ignoring extension)
as an EPUB file in the same folder. This helps clean up duplicate content
when you have both PDF and EPUB versions of the same document.

Usage: Run the script and either enter a directory path or use the file dialog
to select a starting directory. The script will show you all matching PDFs
before asking for confirmation to move them to the Recycle Bin.

Requires: send2trash module (pip install send2trash)
"""

import os
import tkinter as tk
from tkinter import filedialog
from send2trash import send2trash


def main():
    # Prompt for the starting directory
    print("Please enter the starting directory path (or press Enter to use a file dialog):")
    start_dir = input().strip()

    if not start_dir:
        # Create a hidden root window for the file dialog
        root = tk.Tk()
        root.withdraw()
        start_dir = filedialog.askdirectory(title="Select Starting Directory")
        if not start_dir:
            print("No directory selected. Exiting.")
            return

    if not os.path.isdir(start_dir):
        print(f"Error: '{start_dir}' is not a valid directory.")
        return

    # List to store pairs of files that will be deleted
    files_to_delete = []

    # Traverse all directories and subdirectories
    for root, dirs, files in os.walk(start_dir):
        # Get all epub files in the current directory
        epub_files = [f for f in files if f.lower().endswith('.epub')]
        # Get all pdf files in the current directory
        pdf_files = [f for f in files if f.lower().endswith('.pdf')]

        # Extract base names (without extension) for comparison
        epub_basenames = [os.path.splitext(f)[0] for f in epub_files]

        # Check each PDF to see if it has a matching EPUB
        for pdf in pdf_files:
            pdf_basename = os.path.splitext(pdf)[0]
            if pdf_basename in epub_basenames:
                pdf_path = os.path.join(root, pdf)
                epub_path = os.path.join(root, epub_files[epub_basenames.index(pdf_basename)])
                files_to_delete.append((pdf_path, epub_path))

    # Show summary and ask for confirmation
    if not files_to_delete:
        print("No matching PDF files found to delete.")
        return

    print(f"\nFound {len(files_to_delete)} PDF files with matching EPUB files:")
    for i, (pdf_path, epub_path) in enumerate(files_to_delete, 1):
        print(f"{i}. {pdf_path}")
        print(f"   matches: {epub_path}")

    # Ask for confirmation
    print("\nDo you want to move these PDF files to the Recycle Bin? (yes/no): ")
    confirmation = input().strip().lower()

    if confirmation == 'yes':
        # Delete confirmed files (send to recycle bin)
        deleted_count = 0
        for pdf_path, _ in files_to_delete:
            try:
                # os.remove(pdf_path) # Use this to permanently delete instead of sending to recycle bin
                send2trash(pdf_path)  # This sends to recycle bin instead of permanent deletion
                print(f"Sent to Recycle Bin: {pdf_path}")
                deleted_count += 1
            except Exception as e:
                print(f"Error processing {pdf_path}: {e}")

        print(f"\nOperation complete. Moved {deleted_count} of {len(files_to_delete)} PDF files to the Recycle Bin.")
    else:
        print("Operation cancelled. No files were moved.")


if __name__ == "__main__":
    main()