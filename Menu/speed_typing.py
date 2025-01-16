import tkinter as tk
from tkinter import ttk
import sv_ttk
from tkinter import messagebox
from tkPDFViewer import tkPDFViewer as pdf
from time import time


results = {
    'correct': 0,
    'incorrect': 0
    }

stime = None
ptime = None
etime = None


def finish(letter_count):
    global ptime
    etime = time() # End Time
    
    
    ptime = round(time_passed(stime, etime), 2) # Elapsed Time
    speed = round(typing_speed(letter_count), 0) # User's WPM (Words Per Minute)
    
    print(ptime)
    
    

def time_passed(stime, etime):
    
    return etime - stime


def typing_speed(letter_count):
    global ptime
    
    return (letter_count / 5) * (60 / ptime)


def submit(window, allSentences, sentence_index, typed_sentence, letter_count):
    temp = typed_sentence.get()
    
    if(temp.strip() == allSentences[sentence_index].strip()):
        temp_count = len(allSentences[sentence_index]) # Counts the number of characters
        letter_count = letter_count + temp_count
        
        results['correct'] += 1
        sentence_index += 1
        
        grid_placement(window, allSentences, sentence_index, letter_count)
    else:
        results['incorrect'] += 1
        
        grid_placement(window, allSentences, sentence_index, letter_count)
        

def read(allSentences):
    sentences_path = r'E:\Python\Menu\typing_sentences.txt'
    
    with open(sentences_path, 'r') as f:
        sentence = f.readline()
        while sentence:
            allSentences.append(sentence)
            sentence = f.readline()
            


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
def grid_placement(window, allSentences, sentence_index, letter_count):
    typed_sentence = tk.StringVar()
    
    sentence_label = tk.Label(window, wraplength=600, text=allSentences[sentence_index], font=("Arial", 16, "bold"), padx=15, pady=15)
    sentence_label.grid(row=0, column=2)
    sentence_typing_entry = tk.Entry(window, textvariable = typed_sentence, font=("Arial", 16)).grid(row=1, column=2)
    
    exitButton = ttk.Button(window, text="Exit", command=lambda: destroy_program(window)
                            , width=20).grid(row=2, column=0, padx=10, pady=20, sticky='s')
    backButton = ttk.Button(window, text="Back To Main", command=lambda: start_main_menu(window)
                        , width=20).grid(row=2, column=1, padx=10, pady=20, sticky='s')
    submit_button = ttk.Button(window, text="Submit", command=lambda: submit(window, allSentences, sentence_index, typed_sentence, letter_count), width=20).grid(row=2, column=2, padx=10, pady=20, sticky='s')
    
    finish_button = ttk.Button(window, text="Finish", command=lambda: finish(letter_count), width=20).grid(row=2, column=3, padx=10, pady=20, sticky='s')


# speed_typing.py main function
def typing_main(window):
    
    global stime
    allSentences: list[str] = []
    sentence_index = 0
    letter_count = 0
    typed_sentence = ""
    results['correct'] = 0
    results['incorrect'] = 0
    
    # Removes the previous windows widgets.
    for widget in window.winfo_children():
        widget.destroy()
    
    # Sets the window name & resolution.
    window.title("Typing Speed Tester")
    window.geometry("1600x450")
    
    configure_grid(window)
    read(allSentences)
    grid_placement(window, allSentences, sentence_index, letter_count)
    
    stime = time()
    
    
    
    
    
    
