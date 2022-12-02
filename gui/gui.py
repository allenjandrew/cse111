import tkinter as tk
import number_entry as nent


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = tk.Frame(root)
    frm_main.master.title("Gordon Growth Model")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Required Return:"
    lbl_rr = tk.Label(frm_main, text="Required Return:")

    # Create a integer entry box where the user will enter the required return.
    ent_rr = nent.FloatEntry(frm_main, 0.0, 100.0, width=6)

    # Create a label that displays "Growth Rate:"
    lbl_growth = tk.Label(frm_main, text="Growth Rate:")

    # Create a integer entry box where the user will enter the required return.
    ent_growth = nent.FloatEntry(frm_main, 0.0, 500.0, width=6)

    # Create a label that displays "Recent Dividend:"
    lbl_div = tk.Label(frm_main, text="Recent Dividend:")

    # Create a integer entry box where the user will enter the required return.
    ent_div = nent.FloatEntry(frm_main, 0.0, 1000.0, width=6)

    # Create a label that displays "GGM Price:"
    lbl_price = tk.Label(frm_main, text="GGM Price:")

    # Create labels that will display the results.
    lbl_result = tk.Label(frm_main, width=8)

    # Create the Clear button.
    btn_clear = tk.Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_rr.grid(    row=0, column=0, padx=5, pady=5)
    ent_rr.grid(    row=0, column=1, padx=5, pady=5)
    lbl_growth.grid(row=1, column=0, padx=5, pady=5)
    ent_growth.grid(row=1, column=1, padx=5, pady=5)
    lbl_div.grid(   row=2, column=0, padx=5, pady=5)
    ent_div.grid(   row=2, column=1, padx=5, pady=5)
    lbl_price.grid( row=0, column=2, padx=5, pady=5)
    lbl_result.grid(row=0, column=3, padx=5, pady=5)
    btn_clear.grid( row=2, column=3, padx=5, pady=5, columnspan=5, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the inputs.
            req_return = ent_rr.get()
            growth = ent_growth.get()
            recent_div = ent_div.get()

            # Compute the GGM estimated stock price.
            price = (recent_div * (1 + growth)) / (req_return - growth)

            # Display the GGM estimated stock price
            # for the user to see.
            lbl_result.config(text=f"{price:.3f}")

        except ValueError:
            # When the user deletes all the digits in any
            # entry box, clear the GGM Price label.
            lbl_result.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        ent_rr.delete(0, tk.END)
        ent_growth.delete(0, tk.END)
        ent_div.delete(0, tk.END)
        lbl_result.config(text="")
        ent_rr.focus()


    # Bind the calculate function to the three entry boxes
    # so that the calculate function will be called when
    # the user changes the text in any of the entry boxes.
    ent_rr.bind("<KeyRelease>", calculate)
    ent_growth.bind("<KeyRelease>", calculate)
    ent_div.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the clear function will be called when the
    # user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the required return entry box.
    ent_rr.focus()


# If this file is executed like this:
# > python gui.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()