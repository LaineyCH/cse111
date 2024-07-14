import csv
import math
import tk
from tkinter import Frame, Label, Button, OptionMenu, StringVar, Entry


def main():
    block_dict = read_csv("quilt_blocks.csv")

    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Quilt Yardage Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Create an Entry widget
    entry = tk.Entry(root)
    # Place the Entry widget in the window
    entry.pack()

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
            color_prop_couter = COLOR_PROP_INDEX
            for i in range(num_colors):
                color_prop_list.append(row[color_prop_couter])
                color_prop_couter += 1
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
    lbl_block = Label(frm_main, text="Select Block:", width=9, anchor="e")
    # set the list of options
    options = ["Log Cabin", "Pinwheel", "Four Patch", "Nine Patch", "Half Square Triangle", \
               "Hour Glass", "Churn Dash", "Bear Paw", "Friendship Star", "Ohio Star"]
    drop_down_menu = OptionMenu(frm_main, selected_block, *options)
    drop_down_menu.config(width=20)
    
    # Load images for the blocks
    img_filename = block_dict[selected_block][1]
    img_block = tk.PhotoImage(file=img_filename)
    # Create a Label widget to display the image
    lbl_image = Label(frm_main, image=img_block)

    # Create a label that displays "Finished Block Size:"
    lbl_size = Label(frm_main, text="Finished Block Size:", width=12)
    # Create an integer entry box where the user will enter the block's whole inch size.
    ent_inch_size = tk.Entry(frm_main, width=6,lower_bound=1, upper_bound=20)
    # Create a label that displays "inch"
    lbl_inch_units = Label(frm_main, text="cm", width=9, anchor="w")
    # Create an integer entry box where the user will enter the block's quarter inch size.
    ent_quarter_size = tk.Entry(frm_main, width=6,lower_bound=1, upper_bound=4)
    # Create a label that displays "/4 inch"
    lbl_quarter_units = Label(frm_main, text="cm", width=9, anchor="w")

    # Create a label that displays "Quilt Width (Number of Blocks):"
    lbl_width = Label(frm_main, text="Quilt Width (Number of Blocks):", width=12)
    # Create an integer entry box where the user will enter the width.
    ent_width = tk.Entry(frm_main, width=6,lower_bound=1, upper_bound=20)
    # Create a label that displays "blocks"
    # Create a label that displays "Quilt Height (Number of Blocks):"
    lbl_height = Label(frm_main, text="Quilt Height (Number of Blocks):", width=12)
    # Create an integer entry box where the user will enter the width.
    ent_height = tk.Entry(frm_main, width=6,lower_bound=1, upper_bound=20)

    # Create labels that will display the results.
    # quilt size
    lbl_quilt_width = Label(frm_main, text="inches", width=9, anchor="w")
    lbl_width_inch = Label(frm_main, width=10)
    lbl_width_units = Label(frm_main, text="inches", width=9, anchor="w")
    lbl_quilt_height = Label(frm_main, text="inches", width=9, anchor="w")
    lbl_height_inch = Label(frm_main, width=10)
    lbl_height_units = Label(frm_main, text="inches", width=9, anchor="w")
    # number of colors
    lbl_colors = Label(frm_main, text="Minimum number of colors:", width=9, anchor="e")
    lbl_num_colors = Label(frm_main, width=10)
    # yardage
    lbl_fabric_width = Label(frm_main, text="Yardage required for each color", width=9, anchor="e")
    lbl_fabric_width = Label(frm_main, text="(width of fabric is 44 inches):", width=9, anchor="e")
    lbl_color_1 = Label(frm_main, text="Color One:", width=9, anchor="e")
    lbl_color_1_size = Label(frm_main, width=10)
    lbl_1_inch = Label(frm_main, text="inches", width=10, anchor="w")
    lbl_color_2 = Label(frm_main, text="Color Two:", width=9, anchor="e")
    lbl_color_2_size = Label(frm_main, width=10)
    lbl_2_inch = Label(frm_main, text="inches", width=10, anchor="w")
    lbl_color_3 = Label(frm_main, text="Color Three:", width=9, anchor="e")
    lbl_color_3_size = Label(frm_main, width=10)
    lbl_3_inch = Label(frm_main, text="inches", width=10, anchor="w")
    lbl_color_4 = Label(frm_main, text="Color Four:", width=9, anchor="e")
    lbl_color_4_size = Label(frm_main, width=10)
    lbl_4_inch = Label(frm_main, text="inches", width=10, anchor="w")
    lbl_color_5 = Label(frm_main, text="Color Five:", width=9, anchor="e")
    lbl_color_5_size = Label(frm_main, width=10)
    lbl_5_inch = Label(frm_main, text="inches", width=10, anchor="w")

    # Create the Clear button
    btn_clear = Button(frm_main, text="Clear")

    # Create a label Add a label that acts as a status bar at the bottom of your GUI, 
    # displaying an error message in the status bar when the user enters invalid input.
    lbl_error = Label(frm_main, width=42, fg="red")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_block.grid(row=0, column=0, padx=3, pady=3)
    drop_down_menu.grid(row=0, column=1, columnspan=2, padx=3, pady=3)
    lbl_image.grid(row=0, column=3, padx=3, pady=3, rowspan=3)



 # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            block = selected_block.get()
            # Get the block's sizes.
            block_inch_size = ent_inch_size.get()
            block_quarter_size = ent_quarter_size.get()
            quilt_width = ent_width.get()
            quilt_height = ent_height.get()
            # check that all inputs have been entered
            if not block_inch_size or not block_quarter_size or not quilt_width or not quilt_height:
                # complete all inputs message
                lbl_error.config(text="Please complete all fields")

            # Display the results for the user to see.
            lbl_area_value.config(text=f"{area:.2f}")
            lbl_error.config(text="")  # Clear the error message if input is valid

        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, clear the area value labels.
            lbl_area_value.config(text="")
            lbl_error.config(text="Invalid input. Please enter a number between 1 and 999.99.")

    
     # This function will be called each time the user slects an option in the option menu.
    def update_ui(block_dict):
        """Update the UI elements based on the selected shape."""
        # Clear the display output labels
        lbl_width_inch.config(text="")
        lbl_height_inch.config(text="")
        lbl_num_colors.config(text="")
        lbl_color_1_size.config(text="")
        lbl_color_2_size.config(text="")
        lbl_color_3_size.config(text="")
        lbl_color_4_size.config(text="")
        lbl_color_5_size.config(text="")

        block = selected_block.get()
        for key, value in block_dict:
            if key == block:
                # Update image
                img_block = value[0]
                lbl_image.config(image=img_block)  
                # Hide yardage labels for excess colors
                num_colors = value[1]
                if num_colors < 5:
                    lbl_color_5.grid_remove()
                    lbl_color_5_size.grid_remove()
                    lbl_5_inch.grid_remove()
                if num_colors < 4:
                    lbl_color_4.grid_remove()
                    lbl_color_4_size.grid_remove()
                    lbl_4_inch.grid_remove()
                if num_colors < 3:
                    lbl_color_3.grid_remove()
                    lbl_color_3_size.grid_remove()
                    lbl_3_inch.grid_remove()
        
        # Clear the error message
        lbl_error.config(text="")  


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_inch_size.clear()
        ent_inch_size.focus()
        ent_quarter_size.clear()
        ent_width.clear()
        ent_height.clear()

        # Clear the display output labels
        lbl_width_inch.config(text="")
        lbl_height_inch.config(text="")
        lbl_num_colors.config(text="")
        lbl_color_1_size.config(text="")
        lbl_color_2_size.config(text="")
        lbl_color_3_size.config(text="")
        lbl_color_4_size.config(text="")
        lbl_color_5_size.config(text="")

    # Bind the calculate function to the height entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_inch_size.bind("<KeyRelease>", calculate)
    ent_quarter_size.bind("<KeyRelease>", calculate)
    ent_width.bind("<KeyRelease>", calculate)
    ent_height.bind("<KeyRelease>", calculate)

    # Bind the update_ui function to the drop-down menu so
    # that the computer will call the update_ui function when the user
    # changes the selection in the drop-down menu.
    selected_block.trace_add("write", lambda *args: update_ui())

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the first entry box.
    ent_inch_size.focus()


# Call the main function
if __name__ == "__main__":
    main()