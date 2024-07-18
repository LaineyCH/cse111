"""
QUILT YARDAGE CALCULATOR
This program takes input from a user, including finished block size (in whole and 
quarter inches), and number of blocks (width and height) to make up the full quilt.
It calculates how large the finished quilt will be, and, using a quilt dictionary
(read from a csv file), it calculates the minimum number of colors of fabric are needed,
as well as how much of each fabric, and the total yardage.
"""
import csv
import tkinter as tk
from tkinter import Frame, Label, Button, OptionMenu, StringVar, ttk


def main():
    block_dict = read_csv("quilt_blocks.csv")

    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window/frame
    frm_main = Frame(root)
    frm_main.master.title("Quilt Yardage Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function
    populate_main_window(frm_main, block_dict)

    # Start the tkinter loop that processes user events
    root.mainloop()


def read_csv(filename):
    """ Open and read the csv file and save the contents in a dictionary 
        Parameter
            filename: the name of the csv file
        Return: block_dict, the created dictionary
    """
    KEY_INDEX = 0
    IMAGE_INDEX = 1
    NUM_COLOR_INDEX = 2
    COLOR_PROP_INDEX = 3
    block_dict = {}
    # Open the request.csv file and process it
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            block_key = row[KEY_INDEX]
            image_file = row[IMAGE_INDEX]
            num_colors = int(row[NUM_COLOR_INDEX])
            color_prop_list = []
            color_prop_counter = COLOR_PROP_INDEX
            for i in range(num_colors):
                color_prop_list.append(row[color_prop_counter])
                color_prop_counter += 1
            block_dict[block_key] = [image_file, num_colors, color_prop_list]
    return block_dict


def populate_main_window(frm_main, block_dict):
    """Populate the main window of this program.
        Parameters
            frm_main: the main frame
            block_dict: the dictionary of quilt blocks
        Return: nothing
    """
    # Create a StringVar to hold the value of the drop-down selection
    selected_block = StringVar(frm_main)
    # Set a default value
    selected_block.set("Log Cabin")  

    # Create an OptionMenu widget and label
    lbl_block = Label(frm_main, text="Select Block:", width=22, anchor="e")
    # set the list of options
    options = list(block_dict.keys())
    drop_down_menu = OptionMenu(frm_main, selected_block, *options)
    drop_down_menu.config(width=18)
    
    # Load images for the blocks
    initial_block = selected_block.get()
    img_filename = block_dict[initial_block][0]
    img_block = tk.PhotoImage(file=img_filename)
    # Create a Label widget to display the image
    lbl_image = Label(frm_main, image=img_block)
    lbl_image.image = img_block  # Keep a reference to avoid garbage collection

    # Create a label that displays "Finished Block Size:"
    lbl_size = Label(frm_main, text="Finished Block Size:", width=22, anchor="e")
    # Create an integer entry box where the user will enter the block's whole inch size.
    ent_inch_size = tk.Entry(frm_main, width=4, justify='right')
    # Create a label that displays "inch"
    lbl_inch_units = Label(frm_main, text="inch", width=3, anchor="w")
    # Create an integer entry box where the user will enter the block's quarter inch size.
    ent_quarter_size = tk.Entry(frm_main, width=2, justify='right')
    # Create a label that displays "/4 inch"
    lbl_quarter_units = Label(frm_main, text="/4 inch", width=6, anchor="w")

    # Set default value for ent_quarter_size
    ent_quarter_size.insert(0, "0")

    # Create a label that displays "Quilt Width (Number of Blocks):"
    lbl_width = Label(frm_main, text="Quilt Width (Number of Blocks):", width=22, anchor="e")
    # Create an integer entry box where the user will enter the width.
    ent_width = tk.Entry(frm_main, width=4, justify='right')
    # Create a label that displays "Quilt Height (Number of Blocks):"
    lbl_height = Label(frm_main, text="Quilt Height (Number of Blocks):", width=22, anchor="e")
    # Create an integer entry box where the user will enter the width.
    ent_height = tk.Entry(frm_main, width=4, justify='right')

    # Create a horizontal separator
    separator = ttk.Separator(frm_main, orient='horizontal')

    # Create labels that will display the results.
    # number of blocks
    lbl_blocks = Label(frm_main, text="Number of blocks:", width=22, anchor="e")
    lbl_num_blocks = Label(frm_main, width=6)
    # quilt size
    lbl_quilt_width = Label(frm_main, text="Quilt Width:", width=22, anchor="e")
    lbl_width_inch = Label(frm_main, width=6)
    lbl_width_units = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_quilt_height = Label(frm_main, text="Quilt Height", width=22, anchor="e")
    lbl_height_inch = Label(frm_main, width=6)
    lbl_height_units = Label(frm_main, text="inches", width=5, anchor="w")
    # number of colors
    lbl_colors = Label(frm_main, text="Minimum number of colors:", width=22, anchor="e")
    lbl_num_colors = Label(frm_main, width=6)
    # yardage
    lbl_fabric_width = Label(frm_main, text="Yardage required for each color", width=22, anchor="e")
    lbl_fabric_width2 = Label(frm_main, text="(width of fabric is 44 inches):", width=22, anchor="w")
    lbl_color_1 = Label(frm_main, text="Color One:", width=22, anchor="e")
    lbl_color_1_size = Label(frm_main, width=6)
    lbl_1_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_2 = Label(frm_main, text="Color Two:", width=22, anchor="e")
    lbl_color_2_size = Label(frm_main, width=6)
    lbl_2_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_3 = Label(frm_main, text="Color Three:", width=22, anchor="e")
    lbl_color_3_size = Label(frm_main, width=6)
    lbl_3_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_4 = Label(frm_main, text="Color Four:", width=22, anchor="e")
    lbl_color_4_size = Label(frm_main, width=6)
    lbl_4_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_5 = Label(frm_main, text="Color Five:", width=22, anchor="e")
    lbl_color_5_size = Label(frm_main, width=6)
    lbl_5_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_total_yardage = Label(frm_main, text="Total Yardage:", width=22, anchor="e")
    lbl_total_size = Label(frm_main, width=6)
    lbl_total_inch = Label(frm_main, text="inches", width=5, anchor="w")

    # create the Clear button
    btn_clear = Button(frm_main, text="Clear", width=15)

    # create the error message label
    lbl_error = Label(frm_main, text="", width=42, fg="red")

    # layout all the labels, entry boxes, and buttons in a grid
    # the select menu and image
    lbl_block.grid(row=0, column=0, padx=3, pady=3)
    drop_down_menu.grid(row=0, column=1, columnspan=4, padx=3, pady=3)
    lbl_image.grid(row=1, column=1, padx=3, pady=3, columnspan=4)

    # the inputs
    lbl_size.grid(row=2, column=0, padx=3, pady=3)
    ent_inch_size.grid(row=2, column=1, padx=0, pady=3)
    lbl_inch_units.grid(row=2, column=2, padx=0, pady=3)
    ent_quarter_size.grid(row=2, column=3, padx=0, pady=3)
    lbl_quarter_units.grid(row=2, column=4, padx=(0, 3), pady=3)

    lbl_width.grid(row=3, column=0, padx=3, pady=3)
    ent_width.grid(row=3, column=1, padx=3, pady=3)
    lbl_height.grid(row=4, column=0, padx=3, pady=3)
    ent_height.grid(row=4, column=1, padx=3, pady=3)

    # the separator
    separator.grid(row=5, column=0, columnspan=5, sticky='ew', pady=5)

    # the results
    # quilt size
    lbl_blocks.grid(row=6, column=0, padx=3, pady=3)
    lbl_num_blocks.grid(row=6, column=1, padx=3, pady=3)

    lbl_quilt_width.grid(row=7, column=0, padx=3, pady=3)
    lbl_width_inch.grid(row=7, column=1, padx=3, pady=3)
    lbl_width_units.grid(row=7, column=2, padx=3, pady=3, columnspan=2)

    lbl_quilt_height.grid(row=8, column=0, padx=3, pady=3)
    lbl_height_inch.grid(row=8, column=1, padx=3, pady=3)
    lbl_height_units.grid(row=8, column=2, padx=3, pady=3, columnspan=2)
    
    # yardage
    lbl_colors.grid(row=9, column=0, padx=3, pady=3)
    lbl_num_colors.grid(row=9, column=1, padx=3, pady=3)

    lbl_fabric_width.grid(row=10, column=0, padx=3, pady=3)
    lbl_fabric_width2.grid(row=10, column=1, columnspan=4, padx=3, pady=3)

    lbl_color_1.grid(row=11, column=0, padx=3, pady=3)
    lbl_color_1_size.grid(row=11, column=1, padx=3, pady=3)
    lbl_1_inch.grid(row=11, column=2, padx=3, pady=3, columnspan=2)

    lbl_color_2.grid(row=12, column=0, padx=3, pady=3)
    lbl_color_2_size.grid(row=12, column=1, padx=3, pady=3)
    lbl_2_inch.grid(row=12, column=2, padx=3, pady=3, columnspan=2)

    lbl_color_3.grid(row=13, column=0, padx=3, pady=3)
    lbl_color_3_size.grid(row=13, column=1, padx=3, pady=3)
    lbl_3_inch.grid(row=13, column=2, padx=3, pady=3, columnspan=2)

    lbl_color_4.grid(row=14, column=0, padx=3, pady=3)
    lbl_color_4_size.grid(row=14, column=1, padx=3, pady=3)
    lbl_4_inch.grid(row=14, column=2, padx=3, pady=3, columnspan=2)

    lbl_color_5.grid(row=15, column=0, padx=3, pady=3)
    lbl_color_5_size.grid(row=15, column=1, padx=3, pady=3)
    lbl_5_inch.grid(row=15, column=2, padx=3, pady=3, columnspan=2)

    lbl_total_yardage.grid(row=16, column=0, padx=3, pady=3)
    lbl_total_size.grid(row=16, column=1, padx=3, pady=3)
    lbl_total_inch.grid(row=16, column=2, padx=3, pady=3, columnspan=2)

    # error message
    lbl_error.grid(row=18, column=0, columnspan=7, padx=3, pady=3)

    # clear button
    btn_clear.grid(row=19, column=0, columnspan=7, padx=3, pady=3)

    # this function is either triggered by a KeyRelease event, or called by another function
    def validate_for_compute(event=None):
        """ Validate all entries, and if all are valid, call collect_and_compute
        """
        # when the function is called by an event
        if event:
            # Get the entry widget that triggered the event
            entry = event.widget
            entry_1_valid = validate_int_entry(ent_inch_size, 1, 20, ent_inch_size is entry, lbl_error)
            entry_2_valid = validate_int_entry(ent_quarter_size, 0, 3, ent_quarter_size is entry, lbl_error)
            entry_3_valid = validate_int_entry(ent_width, 1, 100, ent_width is entry, lbl_error)
            entry_4_valid = validate_int_entry(ent_height, 1, 100, ent_height is entry, lbl_error)
        # when the function is called from another function
        else:
            entry_1_valid = validate_int_entry(ent_inch_size, 1, 20, False, lbl_error)
            entry_2_valid = validate_int_entry(ent_quarter_size, 0, 3, False, lbl_error)
            entry_3_valid = validate_int_entry(ent_width, 1, 100, False, lbl_error)
            entry_4_valid = validate_int_entry(ent_height, 1, 100, False, lbl_error)

        # when all entries are valid
        if entry_1_valid and entry_2_valid and entry_3_valid and entry_4_valid:
            # clear error message
            lbl_error.config(text="")
            collect_and_compute()
        else:
            clear(False)


    # This function will be called if all 4 entries are input and valid
    def collect_and_compute():
        """Collect and prepare user inputs and selected block information from the block dictionary for computation.
           Display results.
           Parameters: None
           Return: None
        """
        try:
            block = selected_block.get()
            number_colors = int(block_dict[block][1])
            block_color_prop_list = block_dict[block][2]
            # Get the block's sizes.
            block_inch_size = int(ent_inch_size.get())
            block_quarter_size = int(ent_quarter_size.get())
            block_size = block_inch_size + (block_quarter_size * 0.25)
            quilt_width = int(ent_width.get())
            quilt_width_inch = quilt_width * block_size
            quilt_height = int(ent_height.get())
            quilt_height_inch = quilt_height * block_size
            number_blocks = quilt_width * quilt_height

            # call compute_yardage to get the computed yardages
            yardage_list, total_yardage = compute_yardage(block_size, number_blocks, number_colors, block_color_prop_list)

            # Display the results for the user to see.
            lbl_width_inch.config(text=f"{quilt_width_inch}")
            lbl_height_inch.config(text=f"{quilt_height_inch}")
            lbl_num_blocks.config(text=f"{number_blocks}")
            lbl_num_colors.config(text=f"{number_colors}")
            lbl_total_size.config(text=f"{total_yardage:.2f}")
            lbl_color_1_size.config(text=f"{yardage_list[0]:.2f}")
            lbl_color_2_size.config(text=f"{yardage_list[1]:.2f}")
            if number_colors > 2:
                lbl_color_3_size.config(text=f"{yardage_list[2]:.2f}")
            if number_colors > 3:
                lbl_color_4_size.config(text=f"{yardage_list[3]:.2f}")
            if number_colors > 4:
                lbl_color_5_size.config(text=f"{yardage_list[4]:.2f}")

        except ValueError:
            clear(False)
            lbl_error.config(text="Invalid input.")

    
    # This function will be called each time the user selects an option in the option menu.
    def update_ui(*args):
        """ This fuction updates the GUI when a selection is made from the drop down select menu.
            Parameter: *args, allows the function to accept and ignore parameters passed to it by tkinter's trace_add method
            Return: None
        """
        # Clear the display output labels
        clear(False)

        block = selected_block.get()
        if block in block_dict:
            img_filename = block_dict[block][0]
            new_img_block = tk.PhotoImage(file=img_filename)
            lbl_image.config(image=new_img_block)
            lbl_image.image = new_img_block

            num_colors = block_dict[block][1]
            lbl_color_3.grid_remove()
            lbl_color_3_size.grid_remove()
            lbl_3_inch.grid_remove()
            lbl_color_4.grid_remove()
            lbl_color_4_size.grid_remove()
            lbl_4_inch.grid_remove()
            lbl_color_5.grid_remove()
            lbl_color_5_size.grid_remove()
            lbl_5_inch.grid_remove()
            if num_colors > 2:
                lbl_color_3.grid()
                lbl_color_3_size.grid()
                lbl_3_inch.grid()
            if num_colors > 3:
                lbl_color_4.grid()
                lbl_color_4_size.grid()
                lbl_4_inch.grid()
            if num_colors > 4:
                lbl_color_5.grid()
                lbl_color_5_size.grid()
                lbl_5_inch.grid()

        validate_for_compute()

        # Clear the error message
        #lbl_error.config(text="")  


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear(everything: bool):
        """ Clears entries, output, and error messages from the GUI
            Parameter: everything: bool, if "True" all is cleared, if "False" only output is cleared
            Return: None
        """
        if everything:
            ent_inch_size.delete(0, tk.END)
            ent_quarter_size.delete(0, tk.END)
            ent_width.delete(0, tk.END)
            ent_height.delete(0, tk.END)
            lbl_error.config(text="")
            # Give the keyboard focus to the first entry box.
            ent_inch_size.focus()
            # Set default value for ent_quarter_size
            ent_quarter_size.insert(0, "0")

        # Clear the display output labels
        lbl_num_blocks.config(text="")
        lbl_width_inch.config(text="")
        lbl_height_inch.config(text="")
        lbl_num_colors.config(text="")
        lbl_color_1_size.config(text="")
        lbl_color_2_size.config(text="")
        lbl_color_3_size.config(text="")
        lbl_color_4_size.config(text="")
        lbl_color_5_size.config(text="")
        lbl_total_size.config(text="")


    # bind the validate_for_compute function to the entry boxes so that it
    # is called when the user changes the text in any of the entry boxes
    ent_inch_size.bind("<KeyRelease>", validate_for_compute)
    ent_quarter_size.bind("<KeyRelease>", validate_for_compute)
    ent_width.bind("<KeyRelease>", validate_for_compute)
    ent_height.bind("<KeyRelease>", validate_for_compute)

    # bind the update_ui function to the drop-down menu so that it is
    # called when the user changes the selection in the drop-down menu
    selected_block.trace_add("write", update_ui)
 
    # bind the clear function to the clear button so that it is called
    # when the user clicks the clear button
    btn_clear.config(command=clear)

    # give the keyboard focus to the first entry box.
    ent_inch_size.focus()


def validate_int_entry(entry, min_value, max_value, modified: bool, lbl_error):
    """Validates user input, ensuriing it is of type int, and within a specified range.
    Parameters
        entry: the widget for which the velue is to be validated
        min_value: minimum value for the valid range
        max_value: maximun value for th evalid range
        modified: boolean, True if the validation is for the event triggering widget, False if not
        lbl_error: the label in the GUI that th eerror messages will be sent to
    Return: Boolen: True if the value is valid, else False
    """
    try:
        # fetch the entry's value
        v = entry.get()
        # if blank, return invalid (no error message)
        if v == "":
            return False
        # if not blank, convert to int. If it is not a numerical digit, it will throw an exception
        value = int(v)
        # check that it is in range, return validity if it is, otherwise return invalid and display error message
        if min_value <= value <= max_value:
            return True
        else:
            if modified:
                lbl_error.config(text=f"Value is '{entry.get()}'. Must be between {min_value} and {max_value}.")
            return False
    except ValueError:
        if modified:
            lbl_error.config(text=f"Invalid input: '{entry.get()}'. Please enter an integer.")
        return False


def compute_yardage(block_size, number_blocks, number_colors, block_color_prop_list):
    """ Computes the yardage needed for each color, as well as the total yardage.
        Calculated from the size of the individual block and number of blocks, as well
        as the proportional area for each color.
        Parameters
            block_size: the finished size of the quilt block
            number_blocks: total number of blocks in the quilt
            number_colors: total number of colors needed to make the quilt
            block_color_prop_list: list of the proportional area for each color
        Return
            yardage_list: list of yardage in inches for each colour
            total_yardage: total yardage in inches
    """
    WIDTH_FABRIC = 44 # standard quilt fabric width
    block_area = block_size **2
    total_area = block_area * number_blocks
    total_yardage = 0
    yardage_list = []
    # for each color proportion in the list, calculate the total area for that color,
    # convert to running length, then append to yardage_list
    # add each yardage to total_yardage
    for i in range(number_colors):
        color_proportion = float(block_color_prop_list[i])
        color_area = total_area * color_proportion
        color_yardage = round((color_area / WIDTH_FABRIC), 2)
        yardage_list.append(color_yardage)
        total_yardage += color_yardage
    return yardage_list, total_yardage


# Call the main function
if __name__ == "__main__":
    main()