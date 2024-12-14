import tkinter as tk
from tkinter import ttk
import sv_ttk


def youtube_converter():
    print("Button Clicked")

window = tk.Tk()
window.title("Main Menu")
window.geometry("1280x1080")
sv_ttk.use_dark_theme()

style = ttk.Style()
style.configure("TButton", foreground="blue", font=("Arial", 12))

button = ttk.Button(window, text="Click Me", command=youtube_converter)
button.place(x=10, y=10)


window.mainloop()

