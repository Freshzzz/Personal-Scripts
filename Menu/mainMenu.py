import tkinter as tk
from tkinter import ttk
import sv_ttk


def configure_grid(window):
    window.grid_rowconfigure(0, weight=0)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=0)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=0) # Has 0 weight, when window expands, the buttons are fixed in the middle
    window.grid_columnconfigure(2, weight=1)


# Opens a new window where the user can convert their youtube link to a mp3 file
def youtube_converter(window):
    window.withdraw()
    
    import subprocess
    subprocess.Popen(["python", "youtube_converter.py"])
    

# Exits the program completely
def destroy_program(window):
    window.destroy()
    

def main_menu():
    # Creates & Opens the Main Menu Window
    window = tk.Tk()
    window.title("Main Menu")
    window.geometry("1280x1080")
    sv_ttk.use_dark_theme()
    
    configure_grid(window)
    
    # Button Design Configuration
    style=ttk.Style()
    style.configure("TButton",
                    fg="white",
                    font=("Arial", 16),
                    padding=(0, 20))
    

    # Button Implementation
    button = ttk.Button(window, text="Youtube Converter", command=lambda: youtube_converter(window),
                        width=25).grid(row=0, column=0, pady=100)
    button2 = ttk.Button(window, text="2", width=25).grid(row=0, column=1)
    button3 = ttk.Button(window, text="3", width=25).grid(row=0, column=2)
    
    button4 = ttk.Button(window, text="4", width=25).grid(row=1, column=0)
    button5 = ttk.Button(window, text="5", width=25).grid(row=1, column=1)
    button6 = ttk.Button(window, text="6", width=25).grid(row=1, column=2)
    
    button7 = ttk.Button(window, text="7", width=25).grid(row=2, column=0)
    button8 = ttk.Button(window, text="8", width=25).grid(row=2, column=1)
    button9 = ttk.Button(window, text="9", width=25).grid(row=2, column=2)
    
    exitButton = ttk.Button(window, text="Exit", command=lambda: destroy_program(window)
                            , width=10).grid(row=3, column=1, padx=10, pady=20)

    window.mainloop()
    
    

if __name__ == "__main__":
    main_menu()

    

