# ColonialFileHandling automates the copying, moving, and deleting
# files for the Colonial Church UCC AV station.

# Import libraries
import os
import shutil
import tkinter as tk
from tkinter import ttk

# Read file for folder paths
f = open("FolderPaths.txt", "r")
# Read first descriptive line
f.readline()

# Set up folder paths
source = f.readline() # C:\Users\UCC_TECH\Videos\CurrentWeek
moveTarget = f.readline() # C:\Users\UCC_TECH\Videos\PreviousWeek
backupTarget = f.readline() # G:\My Drive
copyTarget = f.readline() # G:\My Drive\Files Shared with Balcony Camera System

# Confirm set up
print(source)
print(moveTarget)
print(backupTarget)
print(copyTarget)

# Close file
f.close()

# Set up fonts
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)


# popupmsg1 is a class representing the first popup window to run when the program is started.
class Popupmsg1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        label = ttk.Label(
            self.frame,
            text="Warning: this will process files in multiple folders including deleting "
            "several.\nDo you wish to continue?",
            font=NORM_FONT,
        )
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(self.frame, text="Process files", command=self.processFiles)
        B2 = ttk.Button(self.frame, text="Do not process", command=self.quit)
        B1.pack()
        B2.pack()
        self.frame.pack()

    # processFiles copies, deletes, and moves files on the AV computer system.
    # @param source source directory
    # @param copyTarget target directory for copying files
    # @param moveTarget target directory for moving files
    def processFiles(self):
        # Copy files for backup
        src_files = os.listdir(source)
        for file_name in src_files:
            full_file_name = os.path.join(source, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, backupTarget)

        # Copy files for work
        src_files = os.listdir(source)
        for file_name in src_files:
            full_file_name = os.path.join(source, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, copyTarget)

        # Delete files
        for filename in os.listdir(moveTarget):
            file_path = os.path.join(moveTarget, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (file_path, e))

        # Move files
        file_names = os.listdir(source)
        for file_name in file_names:
            shutil.move(os.path.join(source, file_name), moveTarget)

        # Change windows
        self.master.destroy()  # close the current window
        self.master = tk.Tk()  # create another Tk instance
        self.app = Popupmsg2(self.master)  # create Demo2 window
        self.master.mainloop()

    # Quit closes out the current window and opens the Finished window.
    def quit(self):
        self.master.destroy()  # close the current window
        self.master = tk.Tk()  # create another Tk instance
        self.app = Popupmsg2(self.master)  # create Demo2 window
        self.master.mainloop()


# Popupmsg2
class Popupmsg2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        label = ttk.Label(self.frame, text="Finished!", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(self.frame, text="Okay", command=self.frame.quit)
        B1.pack()
        self.frame.pack()

    # quit Closes out all windows.
    def quit(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Popupmsg1(root)
    root.mainloop()


if __name__ == "__main__":
    main()
