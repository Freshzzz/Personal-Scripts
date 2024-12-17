import tkinter as tk
from tkinter import ttk
import sv_ttk
import os
import subprocess
import threading


def start():
    window = tk.Tk()
    window.title("Script 1 Config")
    window.geometry("640x360")
    sv_ttk.use_dark_theme()
    
    window.mainloop()
    

if __name__ == "__main__":
    start()

