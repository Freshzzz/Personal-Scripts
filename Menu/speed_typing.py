import tkinter as tk
from tkinter import ttk
import sv_ttk
from tkinter import messagebox
from tkPDFViewer import tkPDFViewer as pdf



def read(allSentences):
    sentences_path = r'E:\Python\Menu\typing_sentences.txt'
    
    with open(sentences_path, 'r') as f:
        sentence = f.readline()
        while sentence:
            allSentences.append(sentence)
            #print(sentence)
            sentence = f.readline()
            
        #print(allSentences)


# Splits the current window into a certain amount of rows & columns.
def configure_grid(window):
    window.grid_rowconfigure(0, weight=1)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=3)
    
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)
    window.grid_columnconfigure(4, weight=1)
    
    
    
# Exits the program completely
def destroy_program(window):
    window.destroy()
    

# Exits the current window, and returns the user to the main menu
def start_main_menu(window):
    
    import mainMenu
    mainMenu.main_menu(window)
    

# Places the buttons in their correct positions.
def grid_placement(window, allSentences, sentence_index):
    typed_sentence = tk.StringVar()
    
    sentence_label = tk.Label(window, text=allSentences[sentence_index], font=("Arial", 16, "bold"), padx=15, pady=15)
    sentence_label.grid(row=0, column=2)
    
    exitButton = ttk.Button(window, text="Exit", command=lambda: destroy_program(window)
                            , width=20).grid(row=2, column=0, padx=10, pady=20, sticky='s')
    backButton = ttk.Button(window, text="Back To Main", command=lambda: start_main_menu(window)
                        , width=20).grid(row=2, column=1, padx=10, pady=20, sticky='s')
    submit_button = ttk.Button(window, text="Submit", width=20).grid(row=2, column=2, padx=10, pady=20, sticky='s')


# speed_typing.py main function
def typing_main(window):
    
    allSentences: list[str] = []
    sentence_index = 0
    typed_sentence = ""
    
    # Removes the previous windows widgets.
    for widget in window.winfo_children():
        widget.destroy()
    
    # Sets the window name & resolution.
    window.title("Typing Speed Tester")
    window.geometry("1400x450")
    
    configure_grid(window)
    read(allSentences)
    grid_placement(window, allSentences, sentence_index)
    
    #print(allSentences)
    #print(allSentences[sentence_index])
    
    
    
    
