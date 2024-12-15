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


def start_youtube_converter():
    
    # Window Configuration
    youtube_window = tk.Tk()
    youtube_window.title("Youtube Video To MP3 Converter")
    youtube_window.geometry("1280x720")
    sv_ttk.use_dark_theme()
    
    
    # Button Implementation/Configuration
    exitButton = ttk.Button(youtube_window, text="Exit", command=lambda: destroy_program(youtube_window)
                            , width=20).pack(side="bottom", pady=10)
    backButton = ttk.Button(youtube_window, text="Back To Main", command=lambda: main_menu(youtube_window)
                        , width=20).pack(side="bottom", pady=10)
    
    
    # Button Style Configuration
    style=ttk.Style()
    style.configure("TButton", fg="white", font=("Arial", 16))
    
    
    
    youtube_window.mainloop()



if __name__ == "__main__":
    start_youtube_converter()