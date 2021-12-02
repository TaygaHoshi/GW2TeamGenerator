# imports
import tkinter as tk
from tkinter import StringVar, filedialog as fd, messagebox
from tkinter import ttk
from GW2TG import *
from utility import *
import os

# global variable
root = tk.Tk()

def select_file(choice:bool, buffer:StringVar, button:tk.Button):
    
    if choice == True:
        # input
        filetypes = (
            ("Tab seperated values", ".tsv"),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
    else:
        # output
        filename = fd.askdirectory(
            title='Open a folder',
            initialdir='/'
        )

    buffer.set(filename)

    button["text"] = filename.split("/")[-1]
    button.update()


def style_select():
    # then get the list of text files in Styles file
    all_files_in_styles_folder = os.listdir(".\\Styles")

    all_style_files = []

    for file in all_files_in_styles_folder:
        if file[-4:] == '.txt':
            all_style_files.append(file) 
    
    print(all_style_files)

    return all_style_files

def generate(input_filepath, output_filepath, style_filepath, reroll_count_entry):

    # get strings from the GUI
    style_path = style_filepath.get()
    reroll_count = reroll_count_entry.get()
    
    # read player and style file
    player_list = []
    style = []
    try:
        player_list, style = read_file(input_filepath, style_path)
    except:
        messagebox.showerror("File Not Found", f"Please check if both player data file and style data file exist.")
        root.destroy()
        
    # normalize the strings
    if not reroll_count.isnumeric() or not reroll_count or reroll_count == "" or reroll_count == 0:
        reroll_count = 2000
    else:
        reroll_count = int(reroll_count)

    # generate result
    result = []
    leftovers = []
    try:
        result, leftovers = generate_result(style, player_list, reroll_count)
    except:
        messagebox.showerror("Error", "There was a problem generating teams.")
        root.destroy()

    # save output
    try:
        save_file(output_filepath, result, leftovers) 
    except:
        messagebox.showerror("Error", "There was a problem saving the result.")
        root.destroy()

if __name__=="__main__":

    # windows options
    root.title("GW2TG")
    root.minsize(300, 300)
    root.maxsize(500, 300)
    root.iconbitmap(".\icon.ico")

    # temporary variables
    input_filepath = StringVar(root, value="")
    output_filepath = StringVar(root, value="")
    style_filepath = StringVar(root, value="")

    # menu elements
    io_frame = tk.Frame(root)
    io_explanation = tk.Label(io_frame, text="Leave a spot empty to use its default value.")
    input_label = tk.Label(io_frame, text="Input File")
    input_button = tk.Button(io_frame, text="Choose Input File", command=lambda: select_file(True, input_filepath, input_button))
    output_label = tk.Label(io_frame, text="Output Folder")
    output_button = tk.Button(io_frame, text="Choose Output Folder", command=lambda: select_file(False, output_filepath, output_button))

    options_frame = tk.Frame(root)
    style_label = tk.Label(options_frame, text="Style")
    style_combobox = ttk.Combobox(options_frame, state="readonly", textvariable=style_filepath)
    style_combobox['values'] = style_select()
    style_combobox.current(0)

    reroll_label = tk.Label(options_frame, text="Reroll Count")
    reroll_entry = tk.Entry(options_frame)

    # button to call the generate() function
    generate_button = tk.Button(root, text="Generate", command=lambda: 
                                generate(input_filepath.get(), output_filepath.get(), style_filepath, reroll_entry))

    # placement of GUI elements
    ## input/output
    io_frame.pack()
    io_explanation.pack(pady=(0, 10))
    input_label.pack()
    input_button.pack(pady=(0, 10), expand=True)
    output_label.pack()
    output_button.pack(pady=(0, 10), expand=True)

    ## options
    options_frame.pack()
    style_label.pack()
    style_combobox.pack(pady=(0, 10))
    reroll_label.pack()
    reroll_entry.pack()

    ## generate button
    generate_button.pack(pady=(20, 0))


    root.mainloop()