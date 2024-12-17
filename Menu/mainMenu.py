import tkinter as tk
from tkinter import ttk
import sv_ttk
import os
import subprocess
import threading


script_base_path = r"E:\Studijos\Praktika"


def first_script():
    def run_script():
        script_1_path = os.path.abspath(os.path.join(script_base_path, "Script_1\SC1.bat"))
        script_1_dir = os.path.dirname(script_1_path)
        subprocess.run(
            [script_1_path],
            cwd=script_1_dir
        )
    threading.Thread(target=run_script, daemon=True).start()


def second_script():
    def run_script():
        script_2_path = os.path.abspath(os.path.join(script_base_path, "Script_2\SC2.bat"))
        script_2_dir = os.path.dirname(script_2_path)
        subprocess.Popen(
            ["cmd", "/c", "start", script_2_path],
            cwd=script_2_dir
        )
        
    threading.Thread(target=run_script, daemon=True).start()
    
    
def third_script():
    def run_script():
        script_3_path = os.path.abspath(os.path.join(script_base_path, "Script_3\SC3.bat"))
        script_3_dir = os.path.dirname(script_3_path)
        subprocess.run(
            ["cmd", "/c", "start", script_3_path],
            cwd=script_3_dir
        )
    threading.Thread(target=run_script, daemon=True).start()
        

def first_config(window):
    window.withdraw()
    
    import subprocess
    subprocess.Popen(["python", "sc1_config.py"])

def configure_grid(window):
    window.grid_rowconfigure(0, weight=0)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=0)
    
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
    
    button7 = ttk.Button(window, text="1st Script", command=first_script, width=25).grid(row=2, column=0)
    button8 = ttk.Button(window, text="2nd Script", command=second_script, width=25).grid(row=2, column=1)
    button9 = ttk.Button(window, text="3rd Script", command=third_script, width=25).grid(row=2, column=2)
    
    button10 = ttk.Button(window, text="Script 1 Config", command=lambda: first_config(window),
                          width=25).grid(row=3, column=0)
    button11 = ttk.Button(window, text="Script 2 Config", width=25).grid(row=3, column=1)
    button12 = ttk.Button(window, text="Script 3 Config", width=25).grid(row=3, column=2)
    
    exitButton = ttk.Button(window, text="Exit", command=lambda: destroy_program(window)
                            , width=10).grid(row=4, column=1, padx=10, pady=20)

    window.mainloop()
    
    

if __name__ == "__main__":
    main_menu()

    

