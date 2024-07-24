from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block
if __name__ == '__main__':
    # Make a new window variable
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()

    # Ask the user if they know how to write code
    name = simpledialog.askstring(title='Deniz', prompt="Do you know how to write code better then Deniz the Meniz?")

    # Check user's response
    if name and name.lower() == "yes":
        # If they say "yes", tell them they will rule the world in a message box pop-up
        messagebox.showinfo("Great!", "You will always be better then him")
    else:
        # Otherwise, tell them something else in an error box pop-up
        messagebox.showerror("Error", "That is impossible")

    # Run the window's .mainloop() method
    window.mainloop()