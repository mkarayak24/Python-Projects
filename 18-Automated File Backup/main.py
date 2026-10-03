import os
import shutil
import datetime
import schedule
import time
import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder

def copy_folder_to_directory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print (f"Folder coppied to {dest_dir}")
    except FileExistsError:
        print (f"Folder already exist in: {dest_dir}")


root = tk.Tk()
root.withdraw()

source_dir = open_file_dialog()
destination_dir = open_file_dialog()

schedule.every().day.at("17:16").do(lambda: copy_folder_to_directory (source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
