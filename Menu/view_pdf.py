import tkinter
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf


def grid_placement(window):
    
    doc_path = tk.StringVar()
    
    ttk.Button(window, text="⬆").grid(row=0, column=3, sticky='s', padx=10, pady=10)
    ttk.Button(window, text="⬇").grid(row=1, column=3)
    
    ttk.Button(window, text="Exit", command=lambda: destroy_program(window)).grid(row=2, column=0, sticky='s')
    ttk.Button(window, text="Back", command=lambda: start_main_menu(window)).grid(row=2, column=1, sticky='s')
    ttk.Button(window, text="Browse File", command=lambda: browse_file(window, doc_path)).grid(row=2, column=2, sticky='s')


def browse_file(window, doc_path):
    pdf_container = tk.Frame(window)  # Separate container for the PDF viewer
    pdf_container.grid(row=0, column=0, columnspan=3, rowspan=2, sticky='nsew', padx=10, pady=10)

    path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("PDF Documents", "*.pdf"), ("All Files", "*.*")]
    )

    if path:
        doc_path.set(path)

        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(pdf_container, pdf_location=path, width=50, height=100)
        v2.pack(fill="both", expand=True)  # Use pack() for the PDF viewer


# Exits the program completely
def destroy_program(window):
    window.destroy()


def start_main_menu(window):
    
    from mainMenu import main_menu
    main_menu(window)
    

def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=5)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)

    


def config(window=None):
    if window is None:
        window = tk.Tk()
    
    for widget in window.winfo_children():
        widget.destroy()
        
    window.title("PDF Viewing")
    window.state('zoomed')
    
    #width = window.winfo_screenwidth()
    #height = window.winfo_screenheight()
    #window.geometry("%dx%d" % (width, height))
    configure_grid(window)
    doc_path = grid_placement(window)
    
    
    style=ttk.Style()
    style.configure("TButton",
                    fg="white",
                    font=("Arial", 24),
                    padding=(20, 20))