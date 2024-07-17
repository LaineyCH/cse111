"""
Calculate the area of a circle:
a = πr2
"""
import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import FloatEntry
import math

def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Circle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Circle Radius:"
    lbl_radius = Label(frm_main, text="Circle Radius:", width=9)

    # Create an integer entry box where the user will enter the circle radius.
    ent_radius = FloatEntry(frm_main, width=6, lower_bound=1, upper_bound=999.99)

    # Create a label that displays "cm"
    lbl_radius_units = Label(frm_main, text="cm", width=9, anchor="w")

    # Create a label that displays "Area:"
    lbl_area = Label(frm_main, text="Area:", width=9)

    # Create labels that will display the results.
    lbl_area_value = Label(frm_main, width=10)
    lbl_area_units = Label(frm_main, text="cm\u00b2", width=9, anchor="w")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Create a label Add a label that acts as a status bar at the bottom of your GUI, 
    # displaying an error message in the status bar when the user enters invalid input.
    lbl_error = Label(frm_main, width=42, fg="red")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_radius.grid(row=0, column=0, padx=3, pady=3)
    ent_radius.grid(row=0, column=1, padx=3, pady=3)
    lbl_radius_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_area.grid(row=1, column=0, padx=(30,3), pady=3)
    lbl_area_value.grid(row=1, column=1, padx=3, pady=3, sticky="we")
    lbl_area_units.grid(row=1, column=2, padx=0, pady=3)

    btn_clear.grid(row=2, column=1, padx=3, pady=3, columnspan=3, sticky="w")

    lbl_error.grid(row=3, column=0, columnspan=3)

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the circle's radius.
            radius = ent_radius.get()

            # Compute the circle's area.
            area = math.pi * radius**2

            # Display the area for the user to see.
            lbl_area_value.config(text=f"{area:.2f}")
            lbl_error.config(text="")  # Clear the error message if input is valid

        except ValueError:
            # When the user deletes all the digits in the radius
            # entry box, clear the area value labels.
            lbl_area_value.config(text="")
            lbl_error.config(text="Invalid input. Please enter a number between 1 and 999.99.")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_radius.clear()
        lbl_area_value.config(text="")
        ent_radius.focus()
        lbl_error.config(text="")

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_radius.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_radius.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()