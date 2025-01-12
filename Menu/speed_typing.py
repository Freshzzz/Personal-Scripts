import tkinter as tk
from tkinter import ttk
import sv_ttk
from tkinter import messagebox
from tkPDFViewer import tkPDFViewer as pdf


def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=3)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)
    

def grid_placement(window):
    exitButton = ttk.Button(window, text="Exit", command=lambda: destroy_program(window)
                            , width=20).grid(row=2, column=1, padx=10, pady=20, sticky='s')
    backButton = ttk.Button(window, text="Back To Main", command=lambda: start_main_menu(window)
                        , width=20).grid(row=2, column=3, padx=10, pady=20, sticky='s')


def typing_main(window):
    for widget in window.winfo_children():
        widget.destroy()
        
    window.title("Typing Speed Tester")
    window.geometry("1080x320")
    
    configure_grid(window)
    grid_placement(window)
    
