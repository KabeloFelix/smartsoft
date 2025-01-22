import os
import zipfile
import bz2
import lzma
from pathlib import Path
from tkinter import Tk, filedialog

class SmartSoft:
    def __init__(self):
        self.supported_formats = ['zip', 'bz2', 'xz']
    
    def compress_file(self, file_path, method='zip'):
        if method not in self.supported_formats:
            raise ValueError(f"Unsupported compression method. Choose from {self.supported_formats}")

        file_path = Path(file_path)
        compressed_file_path = file_path.with_suffix(f'.{method}')

        if method == 'zip':
            with zipfile.ZipFile(compressed_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(file_path, arcname=file_path.name)
        elif method == 'bz2':
            with open(file_path, 'rb') as f_in, bz2.open(compressed_file_path, 'wb') as f_out:
                f_out.writelines(f_in)
        elif method == 'xz':
            with open(file_path, 'rb') as f_in, lzma.open(compressed_file_path, 'wb') as f_out:
                f_out.writelines(f_in)

        print(f"File compressed and saved as: {compressed_file_path}")
        return compressed_file_path

def main():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a file to compress")
    
    if not file_path:
        print("No file selected.")
        return

    compressor = SmartSoft()
    
    print("Select compression method:")
    print("1. ZIP")
    print("2. BZ2")
    print("3. XZ")

    choice = input("Enter the number of your choice: ")
    methods = {'1': 'zip', '2': 'bz2', '3': 'xz'}
    method = methods.get(choice, 'zip')

    try:
        compressor.compress_file(file_path, method)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()