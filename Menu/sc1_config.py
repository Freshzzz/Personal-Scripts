import tkinter as tk
from tkinter import ttk
import sv_ttk
import os
import subprocess
import threading


def grid_placement(window):
    ns_one = tk.StringVar()
    ns_two = tk.StringVar()
    ns_three = tk.StringVar()
    
    nd_one = tk.StringVar()
    nd_two = tk.StringVar()
    nd_three = tk.StringVar()
    
    dbs = tk.StringVar()
    
    ads = tk.StringVar()
    add_one = tk.StringVar()
    add_two = tk.StringVar()
    
    doc_path = tk.StringVar()
    
    name_start_label = tk.Label(window, text="Name starts after", font=("Arial", 16)).grid(row=0, column=0, sticky="s")
    name_start_entry1 = tk.Entry(window, textvariable = ns_one, font=("Arial", 16, 'normal')).grid(row=1, column=0)
    name_start_entry2 = tk.Entry(window, textvariable = ns_two, font=("Arial", 16, 'normal')).grid(row=2, column=0)
    name_start_entry3 = tk.Entry(window, textvariable = ns_three, font=("Arial", 16, 'normal')).grid(row=3, column=0)
    
    name_end_label = tk.Label(window, text="Name ends before", font=("Arial", 16)).grid(row=0, column=1, sticky="s")
    name_end_entry1 = tk.Entry(window, textvariable = nd_one, font=("Arial", 16)).grid(row=1, column=1)
    name_end_entry2 = tk.Entry(window, textvariable = nd_two, font=("Arial", 16)).grid(row=2, column=1)
    name_end_entry3 = tk.Entry(window, textvariable = nd_three, font=("Arial", 16)).grid(row=3, column=1)
    
    db_start_label = tk.Label(window, text="DOB starts after", font=("Arial", 16)).grid(row=0, column=2, sticky="s")
    db_start_entry = tk.Entry(window, textvariable = dbs, font=("Arial", 16)).grid(row=1, column=2)
    
    add_start_label = tk.Label(window, text="Address starts after", font=("Arial", 16)).grid(row=0, column=3, sticky="s")
    add_start_entry = tk.Entry(window, textvariable = ads, font=("Arial", 16)).grid(row=1, column=3)
    
    add_end_label = tk.Label(window, text="Address ends before", font=("Arial", 16)).grid(row=0, column=4, sticky='s')
    add_end_entry1 = tk.Entry(window, textvariable = add_one, font=("Arial", 16)).grid(row=1, column=4)
    add_end_entry2 = tk.Entry(window, textvariable = add_two, font=("Arial", 16)).grid(row=2, column=4)
    
    doc_path_label = tk.Label(window, text="Document Path", font=("Arial", 16)).grid(row=0, column=5, sticky='s')
    doc_path_entry = tk.Entry(window, textvariable = doc_path, font=("Arial", 16)).grid(row=1, column=5)
    

def main_menu(window):
    window.destroy()
    
    import subprocess
    subprocess.Popen(["python", "mainMenu.py"])


def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=0)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1) # Has 0 weight, when window expands, the buttons are fixed in the middle
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)
    window.grid_columnconfigure(5, weight=1)


def start():
    window = tk.Tk()
    window.title("Script 1 Config")
    window.geometry("1280x720")
    sv_ttk.use_dark_theme()
    
    configure_grid(window)
    
    style=ttk.Style()
    style.configure("TButton",
                    fg="white",
                    font=("Arial", 16),
                    padding=(0, 15))
    
    
    grid_placement(window)
    
    backButton = ttk.Button(window, text="Back To Main", command=lambda: main_menu(window),
                            width=10).grid(row=4, column=2, padx=10, pady=20, sticky="ew")
    submitButton = ttk.Button(window, text="Submit", width=10).grid(row=4, column=3, padx=10, pady=20, sticky="ew")
    
    
    window.mainloop()
    

if __name__ == "__main__":
    start()

