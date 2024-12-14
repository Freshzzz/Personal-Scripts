import tkinter as tk
from tkinter import ttk
import sv_ttk


# Creates & Opens the Main Menu Window
window = tk.Tk()
window.title("Main Menu")
window.geometry("1280x1080")
sv_ttk.use_dark_theme()
    

def main_menu(cwd):
    cwd.destroy()
    
    window.deiconify()



# Opens a new window where the user can convert their youtube link to a mp3 file
def youtube_converter():
    window.withdraw()
    youtube_window = tk.Toplevel()
    youtube_window.title("Youtube Video To MP3 Converter")
    youtube_window.geometry("1280x1080")
    
    exitButton = ttk.Button(youtube_window, text="Exit", command=destroy_program, width=20).pack(side="bottom", pady=10)
    backButton = ttk.Button(youtube_window, text="Back To Main", command=lambda: main_menu(youtube_window)
                            , width=20).pack(side="bottom", pady=10)
    

def destroy_program():
    window.destroy()
    

style=ttk.Style()
style.configure("TButton", fg="white", font=("Arial", 16))
    
button = ttk.Button(window, text="Youtube Converter", command=youtube_converter, width=40).place(x=25, y=25)
exitButton = ttk.Button(window, text="Exit", command=destroy_program, width=10).pack(side="bottom", pady=10)

window.mainloop()
    

