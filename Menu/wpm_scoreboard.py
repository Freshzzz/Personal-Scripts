import tkinter as tk
from tkinter import ttk
import sv_ttk
from tkinter import messagebox
from tkPDFViewer import tkPDFViewer as pdf


# Exits the current window, and returns the user to the main menu
def start_main_menu(window):
    
    import mainMenu
    mainMenu.main_menu(window)


def grid_placement(window):
    backButton = ttk.Button(window, text="Back To Main", command=lambda: start_main_menu(window)
                        , width=20).grid(row=2, column=0, padx=10, pady=20, sticky='s')


def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    

def scoreboard_main(window):
    # Removes the previous windows widgets.
    for widget in window.winfo_children():
        widget.destroy()
    
    # Sets the window name & resolution.
    window.title("Typing Speed Tester")
    window.geometry("1600x450")
    
    configure_grid(window)
    grid_placement(window)