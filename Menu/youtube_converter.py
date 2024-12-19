import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sv_ttk
import os
import yt_dlp


def submit(link_entry):
    entered_link = link_entry.get()
    
    if not entered_link.strip():
        messagebox.showerror("Error", "Please enter a valid Youtube Link")
        return

    # File Settings
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
            'noplaylist': True,
            'ffmpeg_location': r'E:\Config\ffmpeg-master-latest-win64-gpl\bin',
        }
    
    try:
        # Downloads & Extracts the audio from a youtube video and converts it to a MP3 file
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([entered_link])
            messagebox.showinfo("Finished", "Your MP3 has finished downloading")
            
    except yt_dlp.utils.DownloadError as e:
        messagebox.showerror("Error", f"Failed to Download: {str(e)}")
        
    except Exception as e:
        messagebox.showerror("Error", "Unknown Error Has Occured")
    

# Exits the program completely
def destroy_program(window):
    window.destroy()
    

# Exits the current window, and returns the user to the main menu
def start_main_menu(window):
    
    import mainMenu
    mainMenu.main_menu(window)
    

# Splits the window into a certain amount of rows and columns
def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=0)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=0) # Has 0 weight, when window expands, the buttons are fixed in the middle
    window.grid_columnconfigure(2, weight=0)
    window.grid_columnconfigure(3, weight=0)
    window.grid_columnconfigure(4, weight=1)


def youtube_converter(window):
    
    
    for widget in window.winfo_children():
        widget.destroy()
        
    window.title("Youtube To MP3 Converter")
    window.geometry("1080x320")
    
    configure_grid(window)
    
    
    # Button Implementation/Configuration
    exitButton = ttk.Button(window, text="Exit", command=lambda: destroy_program(window)
                            , width=20).grid(row=2, column=1, padx=10, pady=20)
    backButton = ttk.Button(window, text="Back To Main", command=lambda: start_main_menu(window)
                        , width=20).grid(row=2, column=3, padx=10, pady=20)
    submitButton = ttk.Button(window, text="Submit", command=lambda: submit(link_entry),
                              width=20).grid(row=1, column=3, padx=10, pady=20)
    
    
    
    # Button Style Configuration
    style=ttk.Style()
    style.configure("TButton", fg="white", font=("Arial", 16))
    
    
    youtube_link = tk.StringVar()
    link_label = tk.Label(window, text="Enter Youtube link", font=("Arial", 16))
    link_entry = tk.Entry(window, textvariable = youtube_link, font=("Arial", 16, 'normal'))
    
    link_label.grid(row=1, column=1)
    link_entry.grid(row=1, column=2)
    
    
    window.mainloop()

