import tkinter as tk
from GW2TG import *
from utility import *

def normalize_strings(input_filepath, output_filepath, style, reroll_count):
    # input_filepath
    input_filepath = input_filepath

    # output_filepath
    output_filepath = output_filepath

    # style
    style = style.replace(" ", "").lower()

    if style and not style == "":
        style = style.split(",")
    else:
        style = ["support", "damage", "random"]

    # reroll_count

    if not reroll_count.isnumeric() or not reroll_count or reroll_count == "" or reroll_count == 0:
        reroll_count = 2000
    else:
        reroll_count = int(reroll_count)

    return (input_filepath, output_filepath, style, reroll_count)

def generate(input_filepath_entry, output_filepath_entry, style_entry, reroll_count_entry):

    # get strings from the GUI
    input_filepath = input_filepath_entry.get()
    output_filepath = output_filepath_entry.get()
    style = style_entry.get()
    reroll_count = reroll_count_entry.get()
    
    # normalize the input strings

    input_filepath, output_filepath, style, reroll_count = normalize_strings(input_filepath, output_filepath, style, reroll_count)
    

    # read player file, generate result and save output
    player_list = read_file(input_filepath)
    result, leftovers = generate_result(style, player_list, reroll_count)
    save_file(output_filepath, result, leftovers)

if __name__=="__main__":

    # windows options
    root = tk.Tk()
    root.title("GW2TG")
    root.minsize(300, 300)
    root.maxsize(500, 300)
    root.iconbitmap(".\icon.ico")

    # menu elements
    io_frame = tk.Frame(root)
    io_explanation = tk.Label(io_frame, text="Leave a spot empty to use its default value.")
    input_label = tk.Label(io_frame, text="Input File (Full path)")
    input_entry = tk.Entry(io_frame)
    output_label = tk.Label(io_frame, text="Output File (Full path)")
    output_entry = tk.Entry(io_frame)

    options_frame = tk.Frame(root)
    style_label = tk.Label(options_frame, text="Style")
    style_entry = tk.Entry(options_frame)
    reroll_label = tk.Label(options_frame, text="Reroll count")
    reroll_entry = tk.Entry(options_frame)

    # button to call the generate() function
    generate_button = tk.Button(root, text="Generate", command=lambda: 
                                generate(input_entry, output_entry, style_entry, reroll_entry))

    # placement of GUI elements
    ## input/output
    io_frame.pack()
    io_explanation.pack()
    input_label.pack()
    input_entry.pack()
    output_label.pack()
    output_entry.pack()

    ## options
    options_frame.pack()
    style_label.pack()
    style_entry.pack()
    reroll_label.pack()
    reroll_entry.pack()

    ## generate button
    generate_button.pack()


    root.mainloop()