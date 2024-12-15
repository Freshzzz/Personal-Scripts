import tkinter as tk
from tkinter import ttk
import sv_ttk


# Exits the program completely
def destroy_program(youtube_window):
    youtube_window.destroy()
    

# Exits the current window, and returns the user to the main menu
def main_menu(youtube_window):
    youtube_window.destroy()
    
    import subprocess
    subprocess.Popen(["python", "mainMenu.py"])
    

def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=0)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=0) # Has 0 weight, when window expands, the buttons are fixed in the middle
    window.grid_columnconfigure(2, weight=0)
    window.grid_columnconfigure(3, weight=1)


def start_youtube_converter():
    
    
    # Window Configuration
    youtube_window = tk.Tk()
    youtube_window.title("Youtube Video To MP3 Converter")
    youtube_window.geometry("1280x720")
    sv_ttk.use_dark_theme()
    
    configure_grid(youtube_window)
    
    
    # Button Implementation/Configuration
    exitButton = ttk.Button(youtube_window, text="Exit", command=lambda: destroy_program(youtube_window)
                            , width=20).grid(row=2, column=1, padx=10, pady=20)
    backButton = ttk.Button(youtube_window, text="Back To Main", command=lambda: main_menu(youtube_window)
                        , width=20).grid(row=2, column=2, padx=10, pady=20)
    
    
    # Button Style Configuration
    style=ttk.Style()
    style.configure("TButton", fg="white", font=("Arial", 16))
    
    
    youtube_link = tk.StringVar()
    link_label = tk.Label(youtube_window, text="Enter the Youtube link", font=("Arial", 16))
    link_entry = tk.Entry(youtube_window, textvariable = youtube_link, font=("Arial", 16, 'normal'))
    
    #link_label.grid(row=0, column=0)
    #link_entry.grid(row=0, column=1)
    
    
    youtube_window.mainloop()



if __name__ == "__main__":
    start_youtube_converter()