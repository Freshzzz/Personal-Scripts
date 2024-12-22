import tkinter as tk
from tkinter import ttk
import yaml
from tkinter import messagebox
import ruamel.yaml
from docx import Document
from docx2pdf import convert
import os
from tkinter import filedialog


def browse_file(doc_path):
    path = filedialog.askopenfilename(
        title = "Select a File",
        filetypes=[("Word Documents", "*.docx"), ("All Files", "*.*")]
    )
    
    doc_path.set(path)


def change(doc, placeholder, replacement_word):
    for paragraph in doc.paragraphs:
        if placeholder in paragraph.text:
            paragraph.text = paragraph.text.replace(placeholder, replacement_word)

            
def write(doc, name):
    doc.save(r"E:\Python\Menu\Updated Konf Sutartis.docx")
    convert(r"E:\Python\Menu\Updated Konf Sutartis.docx", fr"E:\Python\Menu\{name}.pdf")
    os.remove(r"E:\Python\Menu\Updated Konf Sutartis.docx")
    


def submit(name, dob, address, tel_nr, ct_nr, ct_date, doc_path):
    
    doc = Document(doc_path)
    
    change(doc, "[vardas]", name)
    change(doc, "[tel_nr]", tel_nr)
    change(doc, "[sutarties_nr]", ct_nr)
    change(doc, "[pasirasymo_data]", ct_date)
    change(doc, "[gim_data]", dob)
    change(doc, "[adresas]", address)
    
    
    write(doc, name)
    messagebox.showinfo("Finished", "Your .pdf file has been generated")


def start_main_menu(window):
    
    from mainMenu import main_menu
    main_menu(window)


def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=1)
    window.grid_rowconfigure(3, weight=1)
    window.grid_rowconfigure(4, weight=1)
    window.grid_rowconfigure(5, weight=1)
    window.grid_rowconfigure(6, weight=1)
    window.grid_rowconfigure(7, weight=1)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    
    
    name = tk.StringVar()
    tk.Label(window, text="Student name", font=("Arial", 16)).grid(row=0, column=0)
    tk.Entry(window, textvariable = name, font=("Arial", 16, 'normal')).grid(row=0, column=1)
    
    dob = tk.StringVar()
    tk.Label(window, text="Date Of Birth", font=("Arial", 16)).grid(row=1, column=0)
    tk.Entry(window, textvariable = dob, font=("Arial", 16)).grid(row=1, column=1)
    
    address = tk.StringVar()
    tk.Label(window, text="Address", font=("Arial", 16)).grid(row=2, column=0)
    tk.Entry(window, textvariable = address, font=("Arial", 16)).grid(row=2, column=1)
    
    tel_nr = tk.StringVar()
    tk.Label(window, text="Phone Number", font=("Arial", 16)).grid(row=3, column=0)
    tk.Entry(window, textvariable = tel_nr, font=("Arial", 16)).grid(row=3, column=1)
    
    ct_nr = tk.StringVar()
    tk.Label(window, text="Contract Number", font=("Arial", 16)).grid(row=4, column=0)
    tk.Entry(window, textvariable = ct_nr, font=("Arial", 16)).grid(row=4, column=1)
    
    ct_date = tk.StringVar()
    tk.Label(window, text="Contract Date", font=("Arial", 16)).grid(row=5, column=0)
    tk.Entry(window, textvariable = ct_date, font=("Arial", 16)).grid(row=5, column=1)
    
    
    doc_path = tk.StringVar()
    tk.Label(window, text="Document Path", font=("Arial", 16)).grid(row=6, column=0)
    #tk.Entry(window, textvariable = doc_path, font=("Arial", 16)).grid(row=6, column=1)
    
    ttk.Button(window, text="Browse File", command=lambda: browse_file(doc_path)).grid(row=6, column=1)
    
    
    return name, dob, address, tel_nr, ct_nr, ct_date, doc_path
    


def config(window=None):
    
    print("Success")
    if not window:
        window = tk.Tk()
    
    for widget in window.winfo_children():
        widget.destroy()
        
    window.title("Script 2 Config")
    window.geometry("1280x720")  
    name, dob, address, tel_nr, ct_nr, ct_date, doc_path = configure_grid(window)
    
    style=ttk.Style()
    style.configure("TButton",
                    fg="white",
                    font=("Arial", 16),
                    padding=(0, 15))
    
    
    backButton = ttk.Button(window, text="Back To Main", command=lambda: start_main_menu(window)
                            ).grid(row=7, column=0, padx=10, pady=20, sticky="ew")
    submitButton = ttk.Button(window, text="Submit", command=lambda: submit(
        name.get(), dob.get(), address.get(), tel_nr.get(),
        ct_nr.get(), ct_date.get(), doc_path.get())
                              ).grid(row=7, column=1, padx=10, pady=20, sticky="ew")
    
    
    window.mainloop()