import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk    # Combobox
from tkinter import *    # Drop-down menu
import tkinter.messagebox    # Drop-down menu

# Select destination folder
def select_folder():
    folder_path = filedialog.askdirectory()
    folder_path_entry.delete(0, tk.END)
    folder_path_entry.insert(0, folder_path)

# Remove specific characters
def remove_characters(folder_path, characters_to_remove):
    for filename in os.listdir(folder_path):
        new_filename = filename.replace(characters_to_remove, '')
        if new_filename != filename:
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)

# Replace specific characters
def replace_characters(folder_path, characters_to_replace, characters_to_new):
    for filename in os.listdir(folder_path):
        new_filename = filename.replace(characters_to_replace, characters_to_new)
        if new_filename != filename:
            old_filepath = os.path.join(folder_path, filename)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)

# Read operation mode in Combobox
def modify_func():
    if cbox.get() == ('Delete'):
        folder_path = folder_path_entry.get()
        characters_to_remove = characters_entry.get()
        remove_characters(folder_path, characters_to_remove)
        tk.messagebox.showinfo("Finished", "File name modification complete!")

    elif cbox.get() == ('Replace'):
        folder_path = folder_path_entry.get()
        characters_to_replace = characters_pos_entry.get()
        characters_to_new = characters_new_entry.get()
        replace_characters(folder_path, characters_to_replace, characters_to_new)
        tk.messagebox.showinfo("Finished", "File name modification complete!")

# Show the drop-down menu function
def menuCommand():
    tkinter.messagebox.showinfo("Help", "Notice: The system is not perfect. \n\nThis tool can only select folders to batch modify files. \n\nYou can choose to delete or replace the characters in the file name. \n\nYou only need to enter the first line to delete the characters and the last two lines to replace the characters. \n\nThe second operation can be performed only after exiting the program after completing one operation.")

# Create main window
window = tk.Tk()
window.title("File Name Modification Tool")
window.geometry('800x500+10+10')

# Create the drop-down menu
mainmenu = Menu(window)
filemenu = Menu(mainmenu, tearoff = False)
filemenu.add_command(label = "Help", command = menuCommand)
filemenu.add_separator()    # Parting line
filemenu.add_command(label = "Quit", command = window.quit)
mainmenu.add_cascade(label = "File", menu = filemenu)
window.config(menu = mainmenu)

# Create a folder path selector widget
folder_path_label = tk.Label(window, text = "Folder path:", font = (10.5))
#folder_path_label.pack()    # Fix window position
folder_path_label.place(x = 50, y = 50)    # Manage window layout
# grid() and place() can be used together, but pack() can not
folder_path_entry = tk.Entry(window, width = 60)
folder_path_entry.place(x = 200, y = 50)
# 'command' - Click button execution commands
folder_path_button = tk.Button(window, text = "Select destination folder", width = 26, height = 1, command = select_folder)
folder_path_button.place(x = 550, y = 50)


# Create selected Combobox
pattern_label = tk.Label(window, text = "Select the action to be performed on the file:", font = (10.5))
pattern_label.place(x = 50, y = 100)

text = tk.StringVar()
cbox = ttk.Combobox(window, width = 57, textvariable = text)
cbox.place(x = 380, y = 100)
cbox['value'] = ('Delete', 'Replace')


# Create a specific character input widget
characters_label = tk.Label(window, text = "Enter the characters you want to delete:", font = (10.5))
characters_label.place(x = 50, y = 150)
characters_entry = tk.Entry(window, width = 60)
characters_entry.place(x = 380, y = 150)

characters_pos = tk.Label(window, text = "Enter the character you want to replace:", font = (10.5))
characters_pos.place(x = 50, y = 200)
characters_pos_entry = tk.Entry(window, width = 60)
characters_pos_entry.place(x = 380, y = 200)

characters_new = tk.Label(window, text = "Enter the new character:", font = (10.5))
characters_new.place(x = 50, y = 250)
characters_new_entry = tk.Entry(window, width = 60)
characters_new_entry.place(x = 380, y = 250)


# Create 'Confirm' buttons

confirm_button = tk.Button(window, text = "Confirm", width = 10, height = 2, font = (10), command = modify_func)
confirm_button.place(x = 350, y = 350)


# 显示窗口 - Display window
window.mainloop()
