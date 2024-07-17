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
from tkinter import Frame, Label, Button, OptionMenu, StringVar


def main():
    block_dict = read_csv("quilt_blocks.csv")

    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Quilt Yardage Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main, block_dict)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def read_csv(filename):
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
        Parameter
            frm_main: the main frame
            block_dict: the dictionary of quilt blocks
        Return: nothing
    """
    # Create a StringVar to hold the value of the drop-down selection
    selected_block = StringVar(frm_main)
    # Set a default value
    selected_block.set("Log Cabin")  

    # Create an OptionMenu widget and label
    lbl_block = Label(frm_main, text="Select Block:", width=25, anchor="e")
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
    lbl_size = Label(frm_main, text="Finished Block Size:", width=25, anchor="e")
    # Create an integer entry box where the user will enter the block's whole inch size.
    ent_inch_size = tk.Entry(frm_main, width=6)
    # Create a label that displays "inch"
    lbl_inch_units = Label(frm_main, text="inch", width=6, anchor="w")
    # Create an integer entry box where the user will enter the block's quarter inch size.
    ent_quarter_size = tk.Entry(frm_main, width=6)
    # Create a label that displays "/4 inch"
    lbl_quarter_units = Label(frm_main, text="/4 inch", width=6, anchor="w")

    # Set default value for ent_quarter_size
    ent_quarter_size.insert(0, "0")

    # Create a label that displays "Quilt Width (Number of Blocks):"
    lbl_width = Label(frm_main, text="Quilt Width (Number of Blocks):", width=25, anchor="e")
    # Create an integer entry box where the user will enter the width.
    ent_width = tk.Entry(frm_main, width=6)
    # Create a label that displays "Quilt Height (Number of Blocks):"
    lbl_height = Label(frm_main, text="Quilt Height (Number of Blocks):", width=25, anchor="e")
    # Create an integer entry box where the user will enter the width.
    ent_height = tk.Entry(frm_main, width=6)

    # Create labels that will display the results.
    # number of blocks
    lbl_blocks = Label(frm_main, text="Number of blocks:", width=25, anchor="e")
    lbl_num_blocks = Label(frm_main, width=6)
    # quilt size
    lbl_quilt_width = Label(frm_main, text="Quilt Width:", width=25, anchor="e")
    lbl_width_inch = Label(frm_main, width=6)
    lbl_width_units = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_quilt_height = Label(frm_main, text="Quilt Height", width=25, anchor="e")
    lbl_height_inch = Label(frm_main, width=6)
    lbl_height_units = Label(frm_main, text="inches", width=5, anchor="w")
    # number of colors
    lbl_colors = Label(frm_main, text="Minimum number of colors:", width=25, anchor="e")
    lbl_num_colors = Label(frm_main, width=6)
    # yardage
    lbl_fabric_width = Label(frm_main, text="Yardage required for each color", width=25, anchor="e")
    lbl_fabric_width2 = Label(frm_main, text="(width of fabric is 44 inches):", width=25, anchor="w")
    lbl_color_1 = Label(frm_main, text="Color One:", width=25, anchor="e")
    lbl_color_1_size = Label(frm_main, width=6)
    lbl_1_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_2 = Label(frm_main, text="Color Two:", width=25, anchor="e")
    lbl_color_2_size = Label(frm_main, width=6)
    lbl_2_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_3 = Label(frm_main, text="Color Three:", width=25, anchor="e")
    lbl_color_3_size = Label(frm_main, width=6)
    lbl_3_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_4 = Label(frm_main, text="Color Four:", width=25, anchor="e")
    lbl_color_4_size = Label(frm_main, width=6)
    lbl_4_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_color_5 = Label(frm_main, text="Color Five:", width=25, anchor="e")
    lbl_color_5_size = Label(frm_main, width=6)
    lbl_5_inch = Label(frm_main, text="inches", width=5, anchor="w")
    lbl_total_yardage = Label(frm_main, text="Total Yardage:", width=25, anchor="e")
    lbl_total_size = Label(frm_main, width=6)
    lbl_total_inch = Label(frm_main, text="inches", width=5, anchor="w")

    # Create the Clear button
    btn_clear = Button(frm_main, text="Clear")

    # Create a label Add a label that acts as a status bar at the bottom of your GUI, 
    # displaying an error message in the status bar when the user enters invalid input.
    lbl_error = Label(frm_main, text="", width=42, fg="red")

    # Layout all the labels, entry boxes, and buttons in a grid.
    # the select menu and image
    lbl_block.grid(row=0, column=0, padx=3, pady=3)
    drop_down_menu.grid(row=0, column=1, columnspan=4, padx=3, pady=3)
    lbl_image.grid(row=0, column=5, padx=3, pady=3, columnspan=2, rowspan=3)

    # the inputs
    lbl_size.grid(row=3, column=0, padx=3, pady=3)
    ent_inch_size.grid(row=3, column=1, padx=3, pady=3)
    lbl_inch_units.grid(row=3, column=2, padx=3, pady=3)
    ent_quarter_size.grid(row=3, column=3, padx=3, pady=3)
    lbl_quarter_units.grid(row=3, column=4, padx=3, pady=3)

    lbl_width.grid(row=4, column=0, padx=3, pady=3)
    ent_width.grid(row=4, column=1, padx=3, pady=3)

    lbl_height.grid(row=5, column=0, padx=3, pady=3)
    ent_height.grid(row=5, column=1, padx=3, pady=3)

    # the results
    # quilt size
    lbl_blocks.grid(row=6, column=0, padx=3, pady=3)
    lbl_num_blocks.grid(row=6, column=1, padx=3, pady=3)

    lbl_quilt_width.grid(row=7, column=0, padx=3, pady=3)
    lbl_width_inch.grid(row=7, column=1, padx=3, pady=3)
    lbl_width_units.grid(row=7, column=2, padx=3, pady=3)

    lbl_quilt_height.grid(row=8, column=0, padx=3, pady=3)
    lbl_height_inch.grid(row=8, column=1, padx=3, pady=3)
    lbl_height_units.grid(row=8, column=2, padx=3, pady=3)
    
    # yardage
    lbl_colors.grid(row=9, column=0, padx=3, pady=3)
    lbl_num_colors.grid(row=9, column=1, padx=3, pady=3)

    lbl_fabric_width.grid(row=10, column=0, padx=3, pady=3)

    lbl_fabric_width2.grid(row=10, column=1, columnspan=4, padx=3, pady=3)

    lbl_color_1.grid(row=12, column=0, padx=3, pady=3)
    lbl_color_1_size.grid(row=12, column=1, padx=3, pady=3)
    lbl_1_inch.grid(row=12, column=2, padx=3, pady=3)

    lbl_color_2.grid(row=13, column=0, padx=3, pady=3)
    lbl_color_2_size.grid(row=13, column=1, padx=3, pady=3)
    lbl_2_inch.grid(row=13, column=2, padx=3, pady=3)

    lbl_color_3.grid(row=14, column=0, padx=3, pady=3)
    lbl_color_3_size.grid(row=14, column=1, padx=3, pady=3)
    lbl_3_inch.grid(row=14, column=2, padx=3, pady=3)

    lbl_color_4.grid(row=15, column=0, padx=3, pady=3)
    lbl_color_4_size.grid(row=15, column=1, padx=3, pady=3)
    lbl_4_inch.grid(row=15, column=2, padx=3, pady=3)

    lbl_color_5.grid(row=16, column=0, padx=3, pady=3)
    lbl_color_5_size.grid(row=16, column=1, padx=3, pady=3)
    lbl_5_inch.grid(row=16, column=2, padx=3, pady=3)

    lbl_total_yardage.grid(row=17, column=0, padx=3, pady=3)
    lbl_total_size.grid(row=17, column=1, padx=3, pady=3)
    lbl_total_inch.grid(row=17, column=2, padx=3, pady=3)

    # error message
    lbl_error.grid(row=18, column=0, columnspan=5, padx=3, pady=3)

    # Place the Clear button in the grid
    btn_clear.grid(row=19, column=0, columnspan=5, padx=3, pady=3)


    def validate(event = None):
        # Get the entry widget that triggered the event
        entry = event.widget
        entry_1_valid = validate_int_entry(ent_inch_size, 1, 20, ent_inch_size is entry, lbl_error)
        entry_2_valid = validate_int_entry(ent_quarter_size, 0, 3, ent_quarter_size is entry, lbl_error)
        entry_3_valid = validate_int_entry(ent_width, 1, 100, ent_width is entry, lbl_error)
        entry_4_valid = validate_int_entry(ent_height, 1, 100, ent_height is entry, lbl_error)

        if entry_1_valid and entry_2_valid and entry_3_valid and entry_4_valid:
            lbl_error.config(text="")
            calculate()


    # This function will be called if all 4 entries are input and valid.
    def calculate():
        """Get and prepare user inputs and selected block information from the block dictionary for computation.
           Display results.
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
            # When the user deletes all the digits in a single
            # entry box, clear the displayed values.
            lbl_width_inch.config(text="")
            lbl_height_inch.config(text="")
            lbl_num_colors.config(text="")
            lbl_color_1_size.config(text="")
            lbl_color_2_size.config(text="")
            lbl_color_3_size.config(text="")
            lbl_color_4_size.config(text="")
            lbl_color_5_size.config(text="")
            lbl_error.config(text="Invalid input.")

    
    # This function will be called each time the user slects an option in the option menu.
    def update_ui(*args):
        # Clear the display output labels
        clear()

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

        # Clear the error message
        lbl_error.config(text="")  


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        ent_inch_size.delete(0, tk.END)
        ent_quarter_size.delete(0, tk.END)
        ent_width.delete(0, tk.END)
        ent_height.delete(0, tk.END)

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
        lbl_error.config(text="")

        # Give the keyboard focus to the first entry box.
        ent_inch_size.focus()

        # Set default value for ent_quarter_size
        ent_quarter_size.insert(0, "0")

    # Bind the validate function to the entry boxes so that the validate function
    # is called when the user changes the text in the entry box.
    ent_inch_size.bind("<KeyRelease>", validate)
    ent_quarter_size.bind("<KeyRelease>", validate)
    ent_width.bind("<KeyRelease>", validate)
    ent_height.bind("<KeyRelease>", validate)

    # Bind the update_ui function to the drop-down menu so that the computer will
    # call the update_ui function when the user changes the selection in the drop-down menu.
    """selected_block.trace_add("write", lambda *args: update_ui())"""
    selected_block.trace_add("write", update_ui)
 
    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the first entry box.
    ent_inch_size.focus()


def validate_int_entry(entry, min_value, max_value, modified: bool, lbl_error):
    try:
        v = entry.get()
        if v == "":
            return False
        value = int(v)
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
    WIDTH_FABRIC = 44
    block_area = block_size **2
    total_area = block_area * number_blocks
    total_yardage = 0
    yardage_list = []
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