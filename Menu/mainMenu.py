import tkinter as tk
from tkinter import ttk
import sv_ttk


# Creates & Opens the Main Menu Window
window = tk.Tk()
window.title("Main Menu")
window.geometry("1280x1080")
sv_ttk.use_dark_theme()


# Opens a new window where the user can convert their youtube link to a mp3 file
def youtube_converter():
    window.withdraw()
    
    import subprocess
    subprocess.Popen(["python", "youtube_converter.py"])
    

# Exits the program completely
def destroy_program():
    window.destroy()
    

# Button Design Configuration
style=ttk.Style()
style.configure("TButton", fg="white", font=("Arial", 16))
    

# Button Implementation
button = ttk.Button(window, text="Youtube Converter", command=youtube_converter, width=40).place(x=25, y=25)
exitButton = ttk.Button(window, text="Exit", command=destroy_program, width=10).pack(side="bottom", pady=10)


window.mainloop()
    

