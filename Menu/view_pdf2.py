import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf


def start_main_menu(window):
    
    from mainMenu import main_menu
    main_menu(window)
    
    
def destroy_program(window):
    window.destroy()
    
    
def browse_file(window, doc_path, pdf_container):
    for widget in pdf_container.winfo_children():
        widget.destroy()

    path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("PDF Documents", "*.pdf"), ("All Files", "*.*")]
    )

    if path:
        doc_path.set(path)

        # Display the PDF in the `pdf_container`
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(pdf_container, pdf_location=path, width=80, height=50)
        v2.pack(fill="both", expand=True)


def grid_placement(window):
    doc_path = tk.StringVar()
    
    pdf_container = tk.Frame(window, bg="gray", width=1600, height=1000)
    pdf_container.place(x=100, y=50)  # Place the PDF container
    
    ttk.Button(window, text="⬆").place(x=2240, y=100)
    ttk.Button(window, text="⬇").place(x=2240, y=200)
    
    ttk.Button(window, text="Exit", command=lambda: destroy_program(window)).place(x=600, y=1200)
    ttk.Button(window, text="Back", command=lambda: start_main_menu(window)).place(x=1300, y=1200)
    ttk.Button(window, text="Browse File", command=lambda: browse_file(window, doc_path, pdf_container)).place(x=1900, y=1200)
    

def config(window=None):
    if window is None:
        window = tk.Tk()
    
    for widget in window.winfo_children():
        widget.destroy()
        
    window.title("PDF Viewing")
    window.state('zoomed')
    
    doc_path = grid_placement(window)
    
    
    style=ttk.Style()
    style.configure("TButton",
                    fg="white",
                    font=("Arial", 24),
                    padding=(20, 20))