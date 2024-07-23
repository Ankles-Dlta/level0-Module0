from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Ask the user if they know how to write code.
name = simpledialog.askstring(title='Deniz', prompt="Do u know how to write code better then deniz the meniz")

    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if ("yes"):
        print("you will always be better then him")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
        elif ("no"):
            print("that is impossible")
    # Run the window's .mainloop() method
    window.mainloop()
