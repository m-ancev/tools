import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_file(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding="utf-8") as file:
        original_content = file.read()

    # Create a modified version of the content
    modified_content = re.sub(r'ae', 'ä', original_content)
    modified_content = re.sub(r'Ae', 'Ä', modified_content)
    modified_content = re.sub(r'AE', 'Ä', modified_content)
    modified_content = re.sub(r'oe', 'ö', modified_content)
    modified_content = re.sub(r'Oe', 'Ö', modified_content)
    modified_content = re.sub(r'OE', 'Ö', modified_content)
    modified_content = re.sub(r'ue', 'ü', modified_content)
    modified_content = re.sub(r'Ue', 'Ü', modified_content)
    modified_content = re.sub(r'UE', 'Ü', modified_content)

    # Determine if any changes were made
    if original_content != modified_content:
        # Write the changes back to the file
        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(modified_content)
        return True  # Return True if changes were made
    return False  # Return False if no changes were made

def process_folder(folder_path):
    files_processed = 0
    files_changed = 0
    
    # os.walk allows recursive traversal of directories
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path):  # Ensure it's a file
                files_processed += 1
                if process_file(file_path):
                    files_changed += 1
    
    messagebox.showinfo("Processing Complete", 
                        f"Processed {files_processed} files in {folder_path}\n"
                        f"Files changed: {files_changed}")

def browse_folder():
    folder_path = filedialog.askdirectory(title="Select a directory")
    if folder_path:
        folder_label.config(text=f"Selected Directory: {folder_path}")
        process_button.config(state=tk.NORMAL)
        global selected_folder
        selected_folder = folder_path

def execute_process():
    if selected_folder:
        process_folder(selected_folder)

def create_gui():
    global folder_label, process_button

    # Set up the main application window
    root = tk.Tk()
    root.title("Umlaut Fix")
    root.geometry("400x200")

    # Create a button that allows the user to browse and select a folder
    browse_button = tk.Button(root, text="Select Directory", command=browse_folder)
    browse_button.pack(pady=20)

    # Label to show the selected folder
    folder_label = tk.Label(root, text="No Directory")
    folder_label.pack(pady=10)

    # Create a button to execute the process_folder function
    process_button = tk.Button(root, text="Process Content", command=execute_process, state=tk.DISABLED)
    process_button.pack(pady=10)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    selected_folder = None  # Initialize the global variable
    create_gui()
