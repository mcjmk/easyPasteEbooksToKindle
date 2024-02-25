#! python3
"""
easyPasteToKindle.py - A simple script to quickly transfer PDF, MOBI, and EPUB files to a Kindle device connected via USB.
NOTE: Adjust the KINDLE_PATH below to match your Kindle's folder location!!!
"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog

# NOTE: Adjust the KINDLE_PATH below to match your Kindle's folder location.
# If your setup differs (e.g., multiple drives, different OS), please adjust the KINDLE_PATH accordingly!!!
KINDLE_PATH = 'F:\\'


def find_kindle():
    if os.path.exists(KINDLE_PATH):
        return KINDLE_PATH
    else:
        return None


def select_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title='Choose files to add to Kindle',
        filetypes=[('E-books', '*.pdf;*.mobi;*.epub')]
    )
    return file_paths


def copy_files_to_kindle(file_paths, kindle_path):
    kindle_documents_path = os.path.join(kindle_path, 'documents')
    for file_path in file_paths:
        shutil.copy(file_path, kindle_documents_path)
        print(f"Copied {file_path} to {kindle_documents_path}")


def main():
    kindle_path = find_kindle()
    if kindle_path:
        files_path = select_files()
        print(files_path)
        copy_files_to_kindle(files_path, kindle_path)


if __name__ == '__main__':
    main()
